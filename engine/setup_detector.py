# -*- coding: utf-8 -*-
"""机械 Setup 检测器：零自由度，只消费快照字段，不做解释。

输入：snapshot（经过 SnapshotStore 校验与哈希）
输出：事件 payload 列表（待 logger 分配 event_id / 哈希） + 每日触发审计记录。

重要：
  - 触发判定完全机械化；Confirmation 只更新确认状态，不决定事件是否存在。
  - 字段缺失 → 触发不成立并记录 INSUFFICIENT_DATA，绝不编造数值。
  - P0.1 阶段 Decision 恒为 WATCH 占位（Gate 在 P0.2 实现），不产生方向判断。
"""

from __future__ import annotations

from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Tuple

from engine import yaml_mini


OPS = frozenset({"eq", "ne", "gt", "ge", "lt", "le", "in", "is_true", "is_false"})


class SetupDetector:
    def __init__(self, config_root: str | Path):
        self.config_root = Path(config_root)
        self.cfg = yaml_mini.load(self.config_root / "setups.yaml")
        self.thresholds = yaml_mini.load(self.config_root / "thresholds.yaml")
        self.regimes_cfg = yaml_mini.load(self.config_root / "regimes.yaml")
        self.setups = self.cfg["setups"]

    @staticmethod
    def _resolve(snapshot: Dict[str, Any], dotted: str) -> Tuple[Any, bool]:
        """按点号路径取值；返回 (值, 是否存在)。"""
        parts = dotted.split(".")
        node: Any = snapshot
        for p in parts:
            if isinstance(node, dict) and p in node:
                node = node[p]
            else:
                return None, False
        return node, True

    @staticmethod
    def _cmp(op: str, actual: Any, expected: Any) -> bool:
        if op == "eq":
            return actual == expected
        if op == "ne":
            return actual != expected
        if op == "in":
            return actual in expected
        if op == "is_true":
            return actual is True
        if op == "is_false":
            return actual is False
        if op in ("gt", "ge", "lt", "le"):
            try:
                a, b = float(actual), float(expected)
            except (TypeError, ValueError):
                return False
            return {
                "gt": a > b,
                "ge": a >= b,
                "lt": a < b,
                "le": a <= b,
            }[op]
        raise ValueError(f"不支持的 op: {op}")

    def _eval_condition(self, cond: Dict[str, Any], snapshot: Dict[str, Any]) -> Tuple[bool | None, str]:
        field, op, expected = cond["field"], cond["op"], cond.get("value")
        if op not in OPS:
            raise ValueError(f"不支持的 op: {op}（setup 定义错误）")
        actual, exists = self._resolve(snapshot, field)
        if not exists:
            return None, f"INSUFFICIENT_DATA: 字段 {field} 缺失"
        if op in ("is_true", "is_false") and actual is None:
            return None, f"INSUFFICIENT_DATA: 字段 {field} 为 null"
        return self._cmp(op, actual, expected), f"{field}={actual!r} vs 条件 {op} {expected!r}"

    def detect(
        self, snapshot: Dict[str, Any], as_of: str | None = None
    ) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """返回 (事件 payload 列表, 审计记录列表)。"""
        snap = dict(snapshot)
        if not snap.get("snapshot_hash"):
            # 允许直接消费未经过存储层的原始快照；哈希与存储层同一 canonical 算法
            from engine.hash import snapshot_hash

            snap["snapshot_hash"] = snapshot_hash(snapshot)
        events: List[Dict[str, Any]] = []
        audits: List[Dict[str, Any]] = []
        ts = as_of or datetime.now().astimezone().isoformat()

        for s in self.setups:
            core_results = [self._eval_condition(c, snap) for c in s["core"]]
            missing = [r for r in core_results if r[0] is None]
            unmet = [r for r in core_results if r[0] is False]
            trigger_met = not missing and not unmet
            if missing:
                reason = "; ".join(r[1] for r in missing)
            elif unmet:
                reason = "condition not met: " + "; ".join(r[1] for r in unmet)
            else:
                reason = "triggered"

            confirmations: List[Dict[str, Any]] = []
            for c in s.get("confirmation", []):
                met, note = self._eval_condition(c, snapshot)
                confirmations.append(
                    {
                        "name": c["name"],
                        "field": c["field"],
                        "met": met,
                        "rule_version": s["confirmation_rule_version"],
                        "note": note,
                    }
                )

            audits.append(
                {
                    "audit_id": f"AUDIT_{snap['ticker']}_{snap['created_at'][:10]}_{s['setup_id']}_{snap['session']}",
                    "created_at": ts,
                    "ticker": snap["ticker"],
                    "date": snap["created_at"][:10],
                    "session": snap["session"],
                    "setup_id": s["setup_id"],
                    "trigger_rule_version": s["trigger_rule_version"],
                    "checked": True,
                    "trigger_met": trigger_met,
                    "trigger_reason": reason,
                    "snapshot_hash": snap.get("snapshot_hash"),
                }
            )

            if not trigger_met:
                continue

            events.append(self._build_event(s, snap, confirmations))
        return events, audits

    def _build_event(
        self,
        s: Dict[str, Any],
        snapshot: Dict[str, Any],
        confirmations: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        regime_version = snapshot.get("regime", {}).get("version") or self.regimes_cfg.get(
            "regime_version", "regimes_v1"
        )
        return {
            "schema_version": "event_v1",
            "data_version": snapshot.get("data_version", "unknown"),
            "setup_id": s["setup_id"],
            "setup_version": s["version"],
            "trigger_rule_version": s["trigger_rule_version"],
            "confirmation_rule_version": s["confirmation_rule_version"],
            "target_version": s["target_version"],
            "regime_version": regime_version,
            "rule_freeze_date": self.cfg["rule_freeze_date"],
            "created_at": snapshot["created_at"],
            "snapshot_hash": snapshot["snapshot_hash"],
            "ticker": snapshot["ticker"],
            "spot": snapshot["spot"],
            "regime": snapshot.get("regime") or {},
            "location": snapshot.get("location") or {},
            "momentum": snapshot.get("momentum") or {},
            "confirmation": snapshot.get("confirmation") or {},
            "context": snapshot.get("context") or {},
            "primary_target": s["primary_target"],
            "secondary_attribution": s["secondary_attribution"],
            "direction_signal": {
                "label": "NEUTRAL",
                "evidence": "LOW",
                "note": "P0.1 事件引擎阶段：分类 Edge 未实现，不提供方向判断",
            },
            "vol_edge": {"label": "UNKNOWN", "evidence": "LOW", "note": "P0.1 未实现"},
            "pricing_proxy": {"label": "UNKNOWN", "value": None, "note": "P0.1 未实现"},
            "mechanism_confidence": {
                "level": "LOW",
                "note": "基于估算的做市商仓位；客户/做市商方向不可直接观测",
            },
            "data_quality": snapshot.get("data_quality") or {},
            "data_sufficiency": snapshot.get("data_sufficiency") or {},
            "setup_trigger_met": True,
            "confirmation_status": confirmations,
            "target_status": "NOT_EVALUATED",
            "decision": "WATCH",
            "no_trade_reason": None,
            "lifecycle": "OPEN",
            "outcome": "PENDING",
            "evaluation_status": "EVALUABLE",
            "episode_id": None,
        }
