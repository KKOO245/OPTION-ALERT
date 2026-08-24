# -*- coding: utf-8 -*-
"""VIX / Volatility Environment v1.1（冻结 2026-08-24）。

职责：把 VIX 转成系统的"上层波动率环境锚"——
  - vix 块：当前值 + 时间口径（intraday/close）+ 1D/5D 变化
  - regime 块：vol_regime_v1 分桶标签 + 规则版本 + 原始 inputs + transition
  - shock 块：vix_shock_v1（后台记录，v1 不显示、不计分）

纪律：
  - VIX 不判方向，不进 Direction Edge / Gate / Setup 触发条件；
  - 标签只由 vix_level（required input）决定，辅助证据缺失只降 evidence_completeness；
  - 抓不到的数据一律 null / INSUFFICIENT_DATA，不估算、不编造；
  - 时间口径写死：晨报=intraday，晚报=close；1D/5D 变化相对前收盘/5 个交易日收盘。
"""

from __future__ import annotations

import json
import os
import datetime
from datetime import date
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_CONFIG_ROOT = os.path.join(BASE_DIR, "config")
REGIMES_FILE = "regimes.yaml"

INSUFFICIENT = "INSUFFICIENT_DATA"

try:
    from zoneinfo import ZoneInfo

    ET = ZoneInfo("America/New_York")
    _HAS_ET = True
except Exception:
    ET = datetime.timezone.utc
    _HAS_ET = False


def normalize_session(session: Optional[str]) -> str:
    if session in ("evening", "晚报"):
        return "evening"
    return "morning"


def _load_rules(config_root: Optional[str] = None) -> Dict[str, Any]:
    from engine import yaml_mini

    root = Path(config_root) if config_root else Path(DEFAULT_CONFIG_ROOT)
    cfg = yaml_mini.load(root / REGIMES_FILE)
    vol = cfg.get("vol_regime") or {}
    shock = cfg.get("vix_shock") or {}
    if not vol.get("buckets"):
        raise ValueError("regimes.yaml 缺少 vol_regime.buckets（规则未冻结）")
    return {"vol_regime": vol, "vix_shock": shock}


def classify_regime(vix_value: Optional[float], rules: Dict[str, Any]) -> str:
    """v1 只由 VIX 绝对水平定档（半开区间 [min, max)）；required input 缺失 → INSUFFICIENT_DATA。"""
    if vix_value is None:
        return INSUFFICIENT
    try:
        v = float(vix_value)
    except (TypeError, ValueError):
        return INSUFFICIENT
    buckets = rules["vol_regime"]["buckets"]
    for label, b in buckets.items():
        lo = b.get("min")
        hi = b.get("max")
        if (lo is None or v >= lo) and (hi is None or v < hi):
            return label
    return INSUFFICIENT


def _series_stats(
    vix_value: Optional[float],
    timestamp: str,
    vix_series: Optional[List[Tuple[str, float]]],
) -> Tuple[Optional[float], Optional[float], Optional[float], Optional[float]]:
    """返回 (prior_close, 1d_pct, 5d_pct, 20d_percentile)。

    vix_series 为 [(date_iso, close), ...]，只使用严格早于快照日期的收盘，
    避免晨报盘中值把"今天"混进前收盘。
    """
    if not vix_series:
        return None, None, None, None
    try:
        today = date.fromisoformat(str(timestamp)[:10])
    except (TypeError, ValueError):
        return None, None, None, None
    closes = []
    for item in vix_series:
        try:
            d = date.fromisoformat(str(item[0])[:10])
            c = float(item[1])
        except (TypeError, ValueError):
            continue
        if d < today:
            closes.append((d, c))
    closes.sort(key=lambda x: x[0])
    if not closes:
        return None, None, None, None
    prior_close = closes[-1][1]
    if vix_value is None:
        return prior_close, None, None, None
    v = float(vix_value)
    chg1 = (v / prior_close - 1.0) * 100.0 if prior_close else None
    chg5 = None
    if len(closes) >= 5:
        five_ago = closes[-5][1]
        chg5 = (v / five_ago - 1.0) * 100.0 if five_ago else None
    pct20 = None
    if len(closes) >= 20:
        window = [c for _, c in closes[-20:]]
        pct20 = sum(1 for c in window if c <= v) / len(window) * 100.0
    return prior_close, chg1, chg5, pct20


def _shock(chg1: Optional[float], rules: Dict[str, Any]) -> Tuple[Optional[str], Optional[int]]:
    thresholds = (rules.get("vix_shock") or {}).get("thresholds") or {}
    elevated = thresholds.get("elevated", 10.0)
    extreme = thresholds.get("extreme", 20.0)
    if chg1 is None:
        return None, None
    a = abs(chg1)
    if a >= extreme:
        return "EXTREME", 2
    if a >= elevated:
        return "ELEVATED", 1
    return "NONE", 0


def _basis_from_timestamp(timestamp: str) -> str:
    """按实际美东时间判定数据口径：≥16:00 才标 close，其余一律 intraday。

    防止 FORCE 手动运行在盘中把"晚报"错标成 close（诚实原则）。
    """
    try:
        dt = datetime.datetime.fromisoformat(str(timestamp))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=ET)  # 无时区信息时按 ET 假设
        elif _HAS_ET:
            dt = dt.astimezone(ET)
        # 无 tzdata 时：我们的时间戳均按 ET/Toronto 本地生成，直接用其本地时刻
        return "close" if dt.hour >= 16 else "intraday"
    except (TypeError, ValueError):
        return "intraday"


def compute_vol_environment(
    vix_value: Optional[float],
    timestamp: str,
    session: Optional[str] = None,
    vix_series: Optional[List[Tuple[str, float]]] = None,
    prev_regime_label: Optional[str] = None,
    config_root: Optional[str] = None,
) -> Dict[str, Any]:
    """按 vol_environment v1.1 schema 构建完整对象（永不抛异常，缺数据就标 null）。"""
    try:
        rules = _load_rules(config_root)
    except Exception as e:
        print(f"[警告] vol_regime 规则加载失败: {e}，本快照 regime 标 INSUFFICIENT_DATA")
        rules = {"vol_regime": {"buckets": {}}, "vix_shock": {"thresholds": {}}}

    basis = _basis_from_timestamp(timestamp)
    prior_close, chg1, chg5, pct20 = _series_stats(vix_value, timestamp, vix_series)
    label = classify_regime(vix_value, rules)

    inputs = {
        "vix_level": vix_value,
        "vix_1d_pct": round(chg1, 2) if chg1 is not None else None,
        "vix_5d_pct": round(chg5, 2) if chg5 is not None else None,
        "vix_percentile_20d": round(pct20, 1) if pct20 is not None else None,
        "vix_term_structure": None,  # v1 未启用（数据源待验证），诚实标 null
    }
    optional = inputs["vix_1d_pct"], inputs["vix_5d_pct"], inputs["vix_percentile_20d"], inputs["vix_term_structure"]
    completeness = "full" if all(x is not None for x in optional) else "partial"

    to_label = label if label != INSUFFICIENT else None
    changed = bool(
        prev_regime_label
        and to_label is not None
        and prev_regime_label != to_label
    )
    transition = {"from": prev_regime_label, "to": to_label, "changed": changed}

    shock_level, shock_value = _shock(chg1, rules)
    vol = rules["vol_regime"]
    return {
        "vix": {
            "value": vix_value,
            "timestamp": timestamp,
            "basis": basis,
            "prior_close": prior_close,
            "change_1d_pct": inputs["vix_1d_pct"],
            "change_5d_pct": inputs["vix_5d_pct"],
        },
        "regime": {
            "label": label,
            "rule_version": vol.get("version", "vol_regime_v1"),
            "classification_type": vol.get("classification_type", "descriptive"),
            "calibration_status": vol.get("calibration_status", "uncalibrated"),
            "inputs": inputs,
            "evidence_completeness": completeness,
            "transition": transition,
        },
        "shock": {
            "version": (rules.get("vix_shock") or {}).get("version", "vix_shock_v1"),
            "level": shock_level,
            "value": shock_value,
            "display": False,
        },
    }


def fetch_vix_series(days: int = 35) -> Optional[List[Tuple[str, float]]]:
    """抓 ^VIX 近端日线收盘（yfinance）；失败返回 None，不猜测。"""
    try:
        import yfinance as yf

        hist = yf.Ticker("^VIX").history(period=f"{days}d", interval="1d")
        if hist is None or hist.empty:
            return None
        rows = []
        for d, r in hist.iterrows():
            try:
                rows.append((d.date().isoformat(), float(r["Close"])))
            except (TypeError, ValueError):
                continue
        return rows or None
    except Exception as e:
        print(f"[警告] VIX 历史数据获取失败: {e}")
        return None


def load_prev_regime_label(
    data_root: str,
    as_of_date: str,
    session: Optional[str] = None,
) -> Optional[str]:
    """从已存快照读最近一次的 vol regime label（晚报优先当日晨报）。"""
    root = Path(data_root) / "analytics" / "daily"
    if not root.is_dir():
        return None
    sess = normalize_session(session)
    candidates: List[Tuple[str, str]] = []
    if sess == "evening":
        candidates.append(("morning", as_of_date))
    for d in sorted((p.name for p in root.iterdir() if p.is_dir() and p.name < as_of_date), reverse=True):
        candidates.append(("evening", d))
        candidates.append(("morning", d))
    for s, d in candidates:
        folder = root / d
        if not folder.is_dir():
            continue
        for f in sorted(folder.glob(f"*_{s}.json")):
            try:
                snap = json.loads(f.read_text(encoding="utf-8"))
                ve = (snap.get("context") or {}).get("vol_environment") or {}
                label = (ve.get("regime") or {}).get("label")
                if label and label != INSUFFICIENT:
                    return label
            except Exception:
                continue
    return None


def _fetch_vix_spot() -> Tuple[Optional[float], Optional[float]]:
    try:
        from src import data_fetcher as fetcher

        return fetcher.fetch_spot_yfinance("^VIX")
    except Exception:
        try:
            import data_fetcher as fetcher  # type: ignore

            return fetcher.fetch_spot_yfinance("^VIX")
        except Exception:
            return None, None


def build_vol_environment_for_run(
    now,
    session: Optional[str] = None,
    data_root: Optional[str] = None,
    config_root: Optional[str] = None,
) -> Dict[str, Any]:
    """生产入口：抓当前 VIX + 历史，算出完整 vol_environment（含 transition）。"""
    vix, _ = _fetch_vix_spot()
    series = fetch_vix_series()
    prev = load_prev_regime_label(
        data_root or BASE_DIR,
        now.date().isoformat() if hasattr(now, "date") else str(now)[:10],
        session,
    )
    return compute_vol_environment(
        vix,
        now.isoformat(timespec="seconds") if hasattr(now, "isoformat") else str(now),
        session=session,
        vix_series=series,
        prev_regime_label=prev,
        config_root=config_root,
    )
