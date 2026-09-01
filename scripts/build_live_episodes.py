#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""live snapshot → episode 接线（P 待办）：让每日实盘快照进入 analog 样本库。

- 读取 analytics/daily/{date}/{T}_{session}.json（同一天优先晚报）；
- 映射为 replay_v1 的 iv / oi 两层 episode（字段与 engine/replay 对齐）；
- 结果只用未来收盘（无未来泄漏）；当日/近端无 outcome 的天数跳过（自动延迟补）。
- 输出 thesis/live_episodes.jsonl（幂等：按 ticker/date/layer 去重）。

用法：python scripts/build_live_episodes.py [--tickers ...]
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
SNAPSHOT_DIR = REPO_ROOT / "analytics" / "daily"
OUT = REPO_ROOT / "thesis" / "live_episodes.jsonl"
SCHEMA = "replay_v1"


def _tickers() -> list[str]:
    out = []
    for line in (REPO_ROOT / "config" / "tickers.txt").read_text(encoding="utf-8").splitlines():
        s = line.strip()
        if s and not s.startswith("#"):
            out.append(s.upper())
    return out


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _rank_pct(rank):
    r = _num(rank)
    if r is None:
        return None
    return round(r * 100.0 if r <= 1.0 else r, 1)


def _outcome(ticker: str, date_str: str):
    """复用回放口径：未来 1/3/5D 收益、5D RV、5D MAE。"""
    from engine.replay import _closes, _outcome as _replay_outcome

    closes = _closes(ticker)
    if not closes:
        return None
    cdates = [c["date"] for c in closes]
    if date_str not in cdates:
        return None
    return _replay_outcome(closes, cdates.index(date_str))


def build_day(ticker: str, date_str: str, day_dir: Path) -> list[dict]:
    """单日单标的 → [iv episode?, oi episode?]。"""
    e_path = day_dir / f"{ticker}_evening.json"
    m_path = day_dir / f"{ticker}_morning.json"
    snap_path = e_path if e_path.exists() else (m_path if m_path.exists() else None)
    if snap_path is None:
        return []
    try:
        snap = json.loads(snap_path.read_text(encoding="utf-8"))
    except Exception:  # noqa: BLE001
        return []
    oc = _outcome(ticker, date_str)
    if oc is None:
        return []  # 未来数据不足，暂不构造（后续自动补）
    m = snap.get("momentum") or {}
    p3 = snap.get("p3") or {}
    loc = snap.get("location") or {}
    spot = _num(snap.get("spot"))
    out: list[dict] = []
    # iv 层
    atm = _num(m.get("atm_iv"))
    iv_pct = _rank_pct(m.get("iv_rank"))
    rv20 = _num((p3.get("iv_rv") or {}).get("rv_20d"))
    spread_pp = (atm - rv20) * 100.0 if (atm is not None and rv20 is not None) else None
    term = _num(m.get("term_ratio"))
    iv_ep = {
        "schema_version": SCHEMA,
        "ticker": ticker,
        "date": date_str,
        "layer": "iv",
        "conditions": [],
        "inputs": {
            "atm_iv": round(atm, 4) if atm is not None else None,
            "rv20": round(rv20, 4) if rv20 is not None else None,
            "spread_pp": round(spread_pp, 2) if spread_pp is not None else None,
            "iv_pct": iv_pct,
            "term_ratio": round(term, 3) if term is not None else None,
        },
        "outcome": oc,
    }
    out.append(iv_ep)
    # oi 层
    gex = _num((p3.get("gex") or {}).get("net_gex"))
    flip_primary = _num(loc.get("flip_primary"))
    flip_raw = None
    flips = loc.get("flip_levels") or []
    if flips:
        flip_raw = _num(flips[0])
    so = p3.get("second_order") or {}
    cond: list[str] = []
    if gex is not None:
        cond.append("GAMMA_POSITIVE" if gex >= 0 else "GAMMA_NEGATIVE")
    if flip_primary and spot and spot > 0 and abs(spot / flip_primary - 1.0) <= 0.005:
        cond.append("NEAR_FLIP")
    for w in (loc.get("call_wall"), loc.get("put_wall")):
        if w and spot and spot > 0 and abs(spot / w - 1.0) <= 0.01:
            cond.append("NEAR_WALL")
    oi_ep = {
        "schema_version": SCHEMA,
        "ticker": ticker,
        "date": date_str,
        "layer": "oi",
        "conditions": cond,
        "inputs": {
            "spot": round(spot, 2) if spot else None,
            "net_gex": round(gex, 0) if gex is not None else None,
            "atm_iv": round(atm, 4) if atm is not None else None,
            "iv_pct": iv_pct,
            "flip": round(flip_raw, 2) if flip_raw is not None else None,
            "primary_flip": round(flip_primary, 2) if flip_primary is not None else None,
            "call_wall": loc.get("call_wall"),
            "put_wall": loc.get("put_wall"),
            "call_wall_class": loc.get("call_wall_class"),
            "put_wall_class": loc.get("put_wall_class"),
            "pcr_oi_all": None,
            "pcr_oi_near": _num(m.get("pc_oi_ratio")),
            "net_vanna": _num(so.get("net_vanna")),
            "net_charm": _num(so.get("net_charm")),
        },
        "outcome": oc,
    }
    out.append(oi_ep)
    return out


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    p = argparse.ArgumentParser(description="live snapshot → episode 接线")
    p.add_argument("--tickers", nargs="*", help="默认全部")
    args = p.parse_args()
    tickers = [t.upper() for t in args.tickers] if args.tickers else _tickers()
    existing: set = set()
    if OUT.exists():
        with open(OUT, encoding="utf-8") as f:
            for line in f:
                try:
                    r = json.loads(line)
                    existing.add((r["ticker"], r["date"], r["layer"]))
                except Exception:  # noqa: BLE001
                    continue
    OUT.parent.mkdir(parents=True, exist_ok=True)
    written = 0
    with open(OUT, "a", encoding="utf-8") as f:
        for day_dir in sorted(SNAPSHOT_DIR.iterdir()):
            if not day_dir.is_dir():
                continue
            date_str = day_dir.name
            for t in tickers:
                for ep in build_day(t, date_str, day_dir):
                    key = (ep["ticker"], ep["date"], ep["layer"])
                    if key in existing:
                        continue
                    f.write(json.dumps(ep, ensure_ascii=False) + "\n")
                    existing.add(key)
                    written += 1
    print(f"[live-ep] 新增 {written} 条 → {OUT}", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
