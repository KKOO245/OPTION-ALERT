# -*- coding: utf-8 -*-
"""确定性 Outcome 引擎。

规则（写死）：
  - CONFIRMED = Primary Target 在窗口内达标
  - REJECTED  = Primary Target 在窗口内明确未达标（唯一算"预测失败"）
  - EXPIRED   = 到达评价窗口但无法有效评价（INSUFFICIENT_DATA）
  - INVALIDATED = 规则 Bug 或数据污染作废（统计时排除）
  - 幂等：同一 (event, evaluation_rule_version, evaluation_anchor_date) 只写一次 revision。
  - 评价只使用触发时点可获得的数据 + 未来价格；禁止用修订后的历史数据回填。
"""

from __future__ import annotations

from datetime import date, datetime, timedelta
from typing import Any, Dict, List, Optional

from engine.schema import parse_horizon


def _iso_day(s: str) -> date:
    return date.fromisoformat(s[:10])


def _weekdays_between(a: date, b: date) -> int:
    """a 与 b 之间的工作日数量（不含两端）。"""
    n = 0
    d = a + timedelta(days=1)
    while d < b:
        if d.weekday() < 5:
            n += 1
        d += timedelta(days=1)
    return n


class OutcomeEngine:
    def __init__(self, store):
        self.store = store

    # ---------- 主评价 ----------
    def evaluate(
        self,
        event: Dict[str, Any],
        prices: List[Dict[str, Any]],
        rv: Optional[List[Dict[str, Any]]] = None,
        path: Optional[List[Dict[str, Any]]] = None,
        trading_days: Optional[List[str]] = None,
        now: Optional[str] = None,
    ) -> Optional[Dict[str, Any]]:
        pt = event["primary_target"]
        metric = pt["metric"]
        horizon = parse_horizon(pt["horizon"])
        rule = pt["evaluation_rule"]
        anchor = _iso_day(event["created_at"])
        as_of = datetime.fromisoformat(now).date() if now else date.today()

        start_close = start_date = None
        if metric in ("3D_close_return", "3D_mdd"):
            start_close, start_date = _close_at(prices, anchor)
            if start_close is None:
                return self._expired(event, anchor, "起点收盘缺失", as_of)

        end_date = _horizon_end(anchor, horizon, trading_days)
        if end_date is None:
            return self._expired(event, anchor, "评价日历无法计算终点", as_of)
        if as_of < end_date:
            return None  # 窗口未结束：保持 PENDING，不写 revision

        if metric == "3D_close_return":
            end_close, end_close_date = _close_at(prices, end_date)
            if end_close is None:
                return self._expired(
                    event, anchor, f"终点 {end_date} 无收盘价（数据不足）", as_of
                )
            value = end_close / start_close - 1.0
            data_ts = end_close_date
            hit = _check(pt["direction"], pt["threshold"], value)
            if hit is None:
                return self._expired(event, anchor, "方向/阈值配置无法判定", as_of)
            return self._revision(event, "CONFIRMED" if hit else "REJECTED", value, anchor,
                                  end_date, horizon, as_of, data_ts)

        if metric in ("5D_rv_expansion", "5D_rv_contraction"):
            if not rv:
                return self._expired(event, anchor, "缺少 rv 序列", as_of)
            row = _rv_at(rv, end_date)
            if row is None or row["rv20d"] is None or row["rv20d"] == 0 or row["rv5d"] is None:
                return self._expired(event, anchor, f"终点 {end_date} 无 rv5d/rv20d", as_of)
            value = row["rv5d"] / row["rv20d"]
            hit = _check(pt["direction"], pt["threshold"], value)
            if hit is None:
                return self._expired(event, anchor, "方向/阈值配置无法判定", as_of)
            return self._revision(event, "CONFIRMED" if hit else "REJECTED", value, anchor,
                                  end_date, horizon, as_of, end_date)

        if metric == "3D_mdd":
            if not path:
                return self._expired(event, anchor, "缺少路径序列（无法计算 MDD）", as_of)
            seg = _path_between(path, start_date, end_date, start_close)
            if not seg:
                return self._expired(event, anchor, f"{start_date}~{end_date} 无路径数据", as_of)
            value = _max_drawdown(seg)
            hit = _check(pt["direction"], pt["threshold"], value)
            if hit is None:
                return self._expired(event, anchor, "方向/阈值配置无法判定", as_of)
            return self._revision(event, "CONFIRMED" if hit else "REJECTED", value, anchor,
                                  end_date, horizon, as_of, end_date)

        return self._expired(event, anchor, f"未知 metric: {metric}", as_of)

    # ---------- 未终局时的临时状态（供晚报 Scorecard 展示，不写 revision） ----------
    def provisional_status(
        self,
        event: Dict[str, Any],
        prices: List[Dict[str, Any]],
        trading_days: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        anchor = _iso_day(event["created_at"])
        start_close, _ = _close_at(prices, anchor)
        horizon = parse_horizon(event["primary_target"]["horizon"])
        end_date = _horizon_end(anchor, horizon, trading_days)
        if start_close is None or end_date is None:
            return {"target_status": "NOT_EVALUATED", "value": None}
        end_close, _ = _close_at(prices, end_date)
        if end_close is None:
            return {"target_status": "TEMPORARILY_MISSED", "value": None,
                    "note": "终点收盘未到"}
        value = end_close / start_close - 1.0
        hit = _check(event["primary_target"]["direction"],
                     event["primary_target"]["threshold"], value)
        return {
            "target_status": "TEMPORARILY_MET" if hit else "TEMPORARILY_MISSED",
            "value": value,
        }

    # ---------- 作废 ----------
    def invalidate(self, event: Dict[str, Any], reason: str, as_of: Optional[str] = None) -> Dict[str, Any]:
        anchor = _iso_day(event["created_at"])
        return self._revision(event, "INVALIDATED", None, anchor, anchor, 0,
                              as_of or datetime.now().astimezone().isoformat(),
                              anchor, reason=reason, evaluation_status="SUPERSEDED",
                              target_status="INVALIDATED")

    # ---------- 内部 ----------
    def _expired(self, event, anchor, reason, as_of) -> Dict[str, Any]:
        return self._revision(event, "EXPIRED", None, anchor, anchor, 0, as_of, anchor,
                              reason=reason, evaluation_status="INSUFFICIENT_DATA",
                              target_status="EXPIRED")

    def _revision(
        self,
        event,
        result,
        value,
        anchor,
        end_date,
        horizon,
        as_of,
        data_ts,
        reason=None,
        evaluation_status=None,
        target_status=None,
    ) -> Optional[Dict[str, Any]]:
        rev = {
            "revision_id": None,  # 由 store 内幂等检查后生成
            "event_id": event["event_id"],
            "result": result,
            "target_status": target_status or result,
            "evaluation_status": evaluation_status or "EVALUABLE",
            "evaluation_rule_version": event.get("target_version", "targets_v1"),
            "snapshot_hash": event["snapshot_hash"],
            "data_timestamp": _iso(data_ts),
            "ts": _iso(as_of),
            "evaluation_anchor_date": anchor.isoformat(),
            "evaluation_end_date": end_date.isoformat(),
            "evaluation_horizon_days": horizon,
            "metric_value": value,
            "reason": reason,
        }
        rev["revision_id"] = f"REV_{event['event_id']}_{_revision_seq(self.store, event['event_id'])}"
        return self.store.append_revision(rev)


def _revision_seq(store, event_id: str) -> int:
    return 1 + sum(1 for r in store.load_revisions() if r["event_id"] == event_id)


def _iso(d: Any) -> str:
    if isinstance(d, str):
        return d
    if isinstance(d, datetime):
        return d.isoformat()
    return date.isoformat(d)


def _check(direction: str, threshold: float, value: float) -> Optional[bool]:
    if direction == ">=":
        return value >= threshold
    if direction == "<=":
        return value <= threshold
    if direction == ">":
        return value > threshold
    if direction == "<":
        return value < threshold
    return None


def _close_at(prices: List[Dict[str, Any]], day: date) -> tuple:
    """返回 (close, data_date)。只做精确匹配。

    禁止用"之后最近收盘"代替缺失的锚点收盘——那会把评价起点悄悄后移，
    造成隐蔽 look-ahead。锚点缺数据就如实判 INSUFFICIENT_DATA。
    """
    for r in prices:
        if r["date"][:10] == day.isoformat():
            return float(r["close"]), day
    return None, None


def _rv_at(rv: List[Dict[str, Any]], day: date) -> Optional[Dict[str, Any]]:
    rows = sorted(rv, key=lambda r: r["date"][:10])
    for r in rows:
        if r["date"][:10] == day.isoformat():
            rv5 = r.get("rv5d")
            rv20 = r.get("rv20d")
            if rv5 is None or rv20 is None:
                return None
            return {
                "rv5d": float(rv5),
                "rv20d": float(rv20),
                "date": day.isoformat(),
            }
    return None


def _path_between(path, start_day, end_day, start_close):
    out = [{"date": start_day.isoformat(), "close": start_close}]
    for r in sorted(path, key=lambda r: r["date"][:10]):
        d = _iso_day(r["date"])
        if start_day < d <= end_day:
            out.append({"date": d.isoformat(), "close": float(r["close"])})
    return out


def _max_drawdown(seg: List[Dict[str, Any]]) -> float:
    peak = seg[0]["close"]
    mdd = 0.0
    for r in seg[1:]:
        if r["close"] > peak:
            peak = r["close"]
        dd = (peak - r["close"]) / peak if peak else 0.0
        mdd = max(mdd, dd)
    return mdd


def _horizon_end(anchor: date, horizon: int, trading_days: Optional[List[str]]) -> Optional[date]:
    if trading_days:
        days = sorted(d[:10] for d in trading_days)
        if anchor.isoformat() in days:
            idx = days.index(anchor.isoformat())
            target = idx + horizon
            if target < len(days):
                return date.fromisoformat(days[target])
        return None
    # 无交易日历时按工作日推进（Mon-Fri），与周末语义一致但不含节假日
    d = anchor
    steps = 0
    while steps < horizon:
        d += timedelta(days=1)
        if d.weekday() < 5:
            steps += 1
    return d
