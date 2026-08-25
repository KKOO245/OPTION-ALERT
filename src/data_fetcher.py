# -*- coding: utf-8 -*-
"""
数据获取层（v3）
----------------
主源：CBOE 官方延迟期权接口（全链 + IV + 全部希腊字母，免费、无需 key）
兜底：yfinance（现价 + 期权链；yfinance 没有希腊字母，用 vollib 按 Black-Scholes 补算）

CBOE 抓取与 OCC 合约解析借鉴 global-stock-data
(Apache-2.0, https://github.com/simonlin1212/global-stock-data)。
CBOE 数据仅供个人研究；商用或再分发前需取得 Cboe 授权。
"""

import datetime
import re
import threading
import time

import requests

CBOE_BASE = "https://cdn.cboe.com/api/global/delayed_quotes"
USER_AGENT = "Mozilla/5.0 (option-alert-report/3.0)"

RISK_FREE_RATE = 0.05  # 参考无风险利率，用于 vollib 希腊字母估算


class DataNotAvailable(Exception):
    """该标的确没有数据（无期权 / 不在 CBOE 覆盖范围）"""


class DataSourceError(Exception):
    """网络 / 限流 / 接口变更等真错误，需要冒泡给上层"""


# ---------- OCC 合约代码解析 ----------
# 标的 + YYMMDD + C/P + 8 位行权价（千分之一美元）；root 允许含数字（拆股调整合约如 NVDA1）
_OSI = re.compile(
    r"^(?P<root>[A-Z][A-Z0-9]*)(?P<y>\d{2})(?P<m>\d{2})(?P<d>\d{2})"
    r"(?P<cp>[CP])(?P<strike>\d{8})$"
)


def parse_osi(symbol):
    m = _OSI.match(symbol or "")
    if not m:
        return {}
    g = m.groupdict()
    return {
        "expiration": f"20{g['y']}-{g['m']}-{g['d']}",
        "type": "call" if g["cp"] == "C" else "put",
        "strike": int(g["strike"]) / 1000.0,
    }


# ---------- CBOE 请求封装（限速 + 错误分类） ----------
_lock = threading.Lock()
_last_request = 0.0
_MAX_PER_SEC = 4.0


def _throttle():
    global _last_request
    with _lock:
        gap = 1.0 / _MAX_PER_SEC - (time.monotonic() - _last_request)
        if gap > 0:
            time.sleep(gap)
        _last_request = time.monotonic()


def official_get(url, as_json=False, timeout=30):
    _throttle()
    try:
        r = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=timeout)
        r.raise_for_status()
    except requests.HTTPError as e:
        code = e.response.status_code
        if code == 404:
            raise DataNotAvailable(
                f"HTTP 404 {url[:80]} — 资源不存在（该标的可能无期权或不在 CBOE 覆盖范围）"
            ) from e
        hint = {403: "被拒绝：限流、封禁或权限问题", 429: "请求过快"}.get(code, "")
        raise DataSourceError(f"HTTP {code} {url[:80]} — {hint}") from e
    except requests.RequestException as e:
        raise DataSourceError(
            f"请求失败 {url[:80]} — {type(e).__name__}: {e}"
        ) from e
    return r.json() if as_json else r.text


def fetch_chain_cboe(ticker):
    """CBOE 官方延时期权全链（仅美股），一次请求返回全部到期日"""
    raw = official_get(f"{CBOE_BASE}/options/{ticker}.json", as_json=True)
    data = raw.get("data") or {}
    contracts = []
    for o in data.get("options") or []:
        meta = parse_osi(o.get("option", ""))
        if not meta:
            continue
        contracts.append({
            "contract_symbol": o["option"],
            "expiration": meta["expiration"],
            "type": meta["type"],
            "strike": meta["strike"],
            "last": o.get("last_trade_price"),
            "bid": o.get("bid"),
            "ask": o.get("ask"),
            "volume": o.get("volume") or 0,
            "open_interest": o.get("open_interest") or 0,
            "iv": o.get("iv"),
            "delta": o.get("delta"),
            "gamma": o.get("gamma"),
            "theta": o.get("theta"),
            "vega": o.get("vega"),
            "rho": o.get("rho"),
        })
    if not contracts:
        raise DataNotAvailable(
            f"{ticker} 未返回任何期权合约（可能无期权或不在 CBOE 覆盖范围）"
        )
    return {
        "contracts": contracts,
        "spot": data.get("current_price"),
        "timestamp": raw.get("timestamp"),
        "source": "cboe",
    }


def fetch_spot_cboe(ticker):
    """CBOE 个股快照现价（可与期权链配合定 ATM）"""
    try:
        d = official_get(f"{CBOE_BASE}/quotes/{ticker}.json", as_json=True).get("data") or {}
        return d.get("current_price")
    except Exception:
        return None


# ---------- yfinance 兜底 ----------
def _days_to_exp(exp_str):
    exp = datetime.datetime.strptime(exp_str, "%Y-%m-%d").date()
    return (exp - datetime.date.today()).days


def _vollib_greeks(flag, spot, strike, dte, sigma):
    """用 vollib（Black-Scholes）估算希腊字母；ETF 期权实际为美式，这里仅作参考级估算"""
    if sigma is None or sigma <= 0 or spot is None or strike is None or strike <= 0:
        return None, None, None, None, None
    try:
        from vollib.black_scholes.greeks import analytical as g

        t = max(dte, 1) / 365.0
        delta = g.delta(flag, spot, strike, t, RISK_FREE_RATE, sigma)
        gamma = g.gamma(flag, spot, strike, t, RISK_FREE_RATE, sigma)
        theta = g.theta(flag, spot, strike, t, RISK_FREE_RATE, sigma)
        vega = g.vega(flag, spot, strike, t, RISK_FREE_RATE, sigma)
        rho = g.rho(flag, spot, strike, t, RISK_FREE_RATE, sigma)
        return delta, gamma, theta, vega, rho
    except Exception:
        return None, None, None, None, None


def fetch_spot_yfinance(ticker):
    """yfinance 现价，返回 (现价, 前收盘价)"""
    import yfinance as yf

    tk = yf.Ticker(ticker)
    price, prev_close = None, None
    try:
        fi = tk.fast_info
        price = fi.get("last_price") if hasattr(fi, "get") else getattr(fi, "last_price", None)
        prev_close = fi.get("previous_close") if hasattr(fi, "get") else getattr(fi, "previous_close", None)
    except Exception as e:
        print(f"[警告] fast_info 获取 {ticker} 现价失败: {e}")
    if price is None:
        try:
            hist = tk.history(period="5d")
            if not hist.empty:
                price = float(hist["Close"].iloc[-1])
                if len(hist) > 1:
                    prev_close = float(hist["Close"].iloc[-2])
        except Exception as e:
            print(f"[警告] history 获取 {ticker} 现价失败: {e}")
    return price, prev_close


def fetch_day_range_yfinance(ticker):
    """yfinance 当日 OHLC bar，返回 (day_high, day_low)；失败返回 (None, None)，不猜测。

    晨报取到的是截至抓取时刻的盘中高/低；晚报取到的是当日完整高/低。
    时间口径随快照 created_at 保存，报告据此展示。
    """
    import yfinance as yf

    try:
        hist = yf.Ticker(ticker).history(period="1d", interval="1d")
        if hist is None or hist.empty:
            return None, None
        row = hist.iloc[-1]
        high = float(row["High"])
        low = float(row["Low"])
        return high, low
    except Exception as e:
        print(f"[警告] 获取 {ticker} 当日高/低失败: {e}")
        return None, None


def fetch_chain_yfinance(ticker, spot=None, max_days=40):
    """yfinance 期权链（max_days 天内），IV 有、希腊字母用 vollib 补算"""
    import yfinance as yf

    tk = yf.Ticker(ticker)
    today = datetime.date.today()
    try:
        expirations = tk.options
    except Exception as e:
        raise DataSourceError(f"yfinance 无法获取 {ticker} 的到期日列表: {e}") from e

    contracts = []
    for exp_str in expirations:
        exp_date = datetime.datetime.strptime(exp_str, "%Y-%m-%d").date()
        if not (0 <= (exp_date - today).days <= max_days):
            continue
        try:
            chain = tk.option_chain(exp_str)
        except Exception as e:
            print(f"[警告] yfinance 跳过 {ticker} {exp_str}: {e}")
            continue
        for side, flag in (("calls", "c"), ("puts", "p")):
            for row in getattr(chain, side).to_dict("records"):
                iv = row.get("impliedVolatility")
                dte = (exp_date - today).days
                delta, gamma, theta, vega, rho = _vollib_greeks(
                    flag, spot, row.get("strike"), dte, iv
                )
                contracts.append({
                    "contract_symbol": row.get("contractSymbol"),
                    "expiration": exp_str,
                    "type": side[:-1],
                    "strike": row.get("strike"),
                    "last": row.get("lastPrice"),
                    "bid": row.get("bid"),
                    "ask": row.get("ask"),
                    "volume": row.get("volume") or 0,
                    "open_interest": row.get("openInterest") or 0,
                    "iv": iv,
                    "delta": delta,
                    "gamma": gamma,
                    "theta": theta,
                    "vega": vega,
                    "rho": rho,
                })
    if not contracts:
        raise DataNotAvailable(f"{ticker} 在 {max_days} 天内没有抓到任何期权合约")
    return {
        "contracts": contracts,
        "spot": spot,
        "timestamp": datetime.datetime.now().isoformat(timespec="seconds"),
        "source": "yfinance",
    }


def normalize_contracts(contracts, spot):
    """补全 dte / mid / premium / vol_oi_ratio / moneyness 字段"""
    for c in contracts:
        c["dte"] = _days_to_exp(c["expiration"])
        bid, ask, last = c.get("bid"), c.get("ask"), c.get("last")
        mid = None
        if bid is not None and ask is not None:
            mid = (bid + ask) / 2.0
        elif last is not None:
            mid = last
        c["mid"] = mid
        vol = c.get("volume") or 0
        oi = c.get("open_interest") or 0
        c["premium"] = mid * vol if mid else 0.0
        c["vol_oi_ratio"] = (vol / oi) if oi > 0 else (None if vol == 0 else float("inf"))
        c["moneyness"] = (c["strike"] / spot - 1.0) if spot else None
    return contracts


def fetch_spot(ticker):
    """现价：CBOE 优先，yfinance 兜底"""
    price = fetch_spot_cboe(ticker)
    prev_close = None
    if price is None:
        try:
            price, prev_close = fetch_spot_yfinance(ticker)
        except Exception as e:
            print(f"[警告] {ticker} 现价获取失败: {e}")
    return price, prev_close


def fetch_chain(ticker, max_days=40):
    """主入口：CBOE 优先，失败自动降级 yfinance；返回 (contracts, spot, source)"""
    try:
        result = fetch_chain_cboe(ticker)
    except (DataNotAvailable, DataSourceError) as e:
        print(f"[降级] {ticker} CBOE 不可用，改用 yfinance: {e}")
        spot, _ = fetch_spot(ticker)
        result = fetch_chain_yfinance(ticker, spot=spot, max_days=max_days)

    contracts = normalize_contracts(result["contracts"], result.get("spot"))
    contracts = [c for c in contracts if 0 <= c["dte"] <= max_days]
    if not contracts:
        raise DataNotAvailable(f"{ticker} 在 {max_days} 天内没有有效合约")
    return contracts, result.get("spot"), result.get("source")
