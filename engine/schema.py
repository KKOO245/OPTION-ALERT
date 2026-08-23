# -*- coding: utf-8 -*-
"""事件 / 快照 / revision 的 schema 校验（冻结 v1）。"""

from __future__ import annotations

from datetime import datetime
from typing import Any, Dict, List


class SchemaError(ValueError):
    pass


# 枚举（冻结）
DECISIONS = frozenset(
    {"DIRECTIONAL_BULL", "DIRECTIONAL_BEAR", "VOLATILITY_SETUP", "WATCH", "NO_TRADE"}
)
NO_TRADE_REASONS = frozenset({"EVIDENCE", "PRICING", "TIMING", "MECHANISM", "LIQUIDITY"})
LIFECYCLE = frozenset({"CREATED", "OPEN", "CLOSED"})
OUTCOMES = frozenset({"PENDING", "CONFIRMED", "REJECTED", "EXPIRED", "INVALIDATED"})
TARGET_STATUSES = frozenset(
    {
        "NOT_EVALUATED",
        "TEMPORARILY_MET",
        "TEMPORARILY_MISSED",
        "CONFIRMED",
        "REJECTED",
        "EXPIRED",
        "INVALIDATED",
    }
)
EVAL_STATUSES = frozenset({"EVALUABLE", "INSUFFICIENT_DATA", "SUPERSEDED"})
METRICS = frozenset({"3D_close_return", "5D_rv_expansion", "5D_rv_contraction", "3D_mdd"})
DIRECTIONS = frozenset({">=", "<=", ">", "<"})
EVAL_RULES = frozenset({"close_to_close", "rv_ratio", "mdd_path"})
SECONDARY_KEYS = frozenset({"mfe", "mdd", "rv", "path"})
SESSIONS = frozenset({"morning", "evening"})

REQUIRED_EVENT_FIELDS = [
    "event_id",
    "schema_version",
    "data_version",
    "setup_id",
    "setup_version",
    "trigger_rule_version",
    "confirmation_rule_version",
    "target_version",
    "regime_version",
    "rule_freeze_date",
    "created_at",
    "snapshot_hash",
    "ticker",
    "spot",
    "regime",
    "location",
    "momentum",
    "confirmation",
    "context",
    "primary_target",
    "secondary_attribution",
    "direction_signal",
    "vol_edge",
    "pricing_proxy",
    "mechanism_confidence",
    "data_quality",
    "data_sufficiency",
    "setup_trigger_met",
    "confirmation_status",
    "target_status",
    "decision",
    "no_trade_reason",
    "lifecycle",
    "outcome",
    "evaluation_status",
    "episode_id",
    "content_hash",
    "prev_hash",
    "event_hash",
]

REQUIRED_SNAPSHOT_FIELDS = [
    "schema_version",
    "ticker",
    "created_at",
    "session",
    "source",
    "spot",
]


def _is_iso_datetime(value: Any) -> bool:
    if not isinstance(value, str):
        return False
    try:
        datetime.fromisoformat(value)
        return True
    except ValueError:
        return False


def parse_horizon(horizon: Any) -> int:
    """'3D' / '5D' / 数字 → 交易日数。"""
    if isinstance(horizon, int):
        return horizon
    if isinstance(horizon, str) and horizon.endswith("D") and horizon[:-1].isdigit():
        return int(horizon[:-1])
    raise SchemaError(f"无法解析 horizon: {horizon!r}")


def _errors_missing(obj: Dict[str, Any], fields: List[str]) -> List[str]:
    return [f"缺少字段: {f}" for f in fields if f not in obj]


def validate_primary_target(t: Any) -> List[str]:
    errs: List[str] = []
    if not isinstance(t, dict):
        return ["primary_target 必须是 dict"]
    for f in ("metric", "direction", "threshold", "horizon", "evaluation_rule"):
        if f not in t:
            errs.append(f"primary_target 缺少字段: {f}")
    if t.get("metric") not in METRICS:
        errs.append(f"primary_target.metric 不在允许集合: {sorted(METRICS)}")
    if t.get("direction") not in DIRECTIONS:
        errs.append(f"primary_target.direction 不在允许集合: {sorted(DIRECTIONS)}")
    if not isinstance(t.get("threshold"), (int, float)):
        errs.append("primary_target.threshold 必须是数字")
    try:
        parse_horizon(t.get("horizon"))
    except SchemaError as e:
        errs.append(str(e))
    if t.get("evaluation_rule") not in EVAL_RULES:
        errs.append(f"primary_target.evaluation_rule 不在允许集合: {sorted(EVAL_RULES)}")
    return errs


def validate_secondary_attribution(sa: Any) -> List[str]:
    if not isinstance(sa, (dict, list)):
        return ["secondary_attribution 必须是 dict 或 list"]
    if isinstance(sa, list):
        bad = [k for k in sa if k not in SECONDARY_KEYS]
        if bad:
            return [f"secondary_attribution 含未允许键: {bad}（允许: {sorted(SECONDARY_KEYS)}）"]
        return []
    bad = [k for k in sa if k not in SECONDARY_KEYS]
    return [f"secondary_attribution 含未允许键: {bad}"] if bad else []


def validate_confirmation_status(cs: Any) -> List[str]:
    errs: List[str] = []
    if not isinstance(cs, list):
        return ["confirmation_status 必须是 list"]
    for item in cs:
        if not isinstance(item, dict) or "name" not in item or "met" not in item:
            errs.append(f"confirmation_status 项格式错误: {item!r}")
            continue
        if item["met"] is not None and not isinstance(item["met"], bool):
            errs.append(f"confirmation_status.{item['name']}.met 必须是 bool 或 null")
    return errs


def validate_event(event: Dict[str, Any]) -> List[str]:
    errs = _errors_missing(event, REQUIRED_EVENT_FIELDS)
    if errs:
        return errs
    if not isinstance(event["event_id"], str) or not event["event_id"]:
        errs.append("event_id 必须是非空字符串")
    if not _is_iso_datetime(event["created_at"]):
        errs.append("created_at 必须是 ISO 8601 时间戳")
    if not isinstance(event["spot"], (int, float)) or event["spot"] <= 0:
        errs.append("spot 必须是正数")
    if not isinstance(event["ticker"], str) or not event["ticker"]:
        errs.append("ticker 必须是非空字符串")
    if event["decision"] not in DECISIONS:
        errs.append(f"decision 不在允许集合: {sorted(DECISIONS)}")
    if event["no_trade_reason"] is not None and event["no_trade_reason"] not in NO_TRADE_REASONS:
        errs.append(f"no_trade_reason 不在允许集合: {sorted(NO_TRADE_REASONS)}")
    if event["decision"] == "NO_TRADE" and event["no_trade_reason"] is None:
        errs.append("decision=NO_TRADE 时必须提供 no_trade_reason")
    if event["lifecycle"] not in LIFECYCLE:
        errs.append(f"lifecycle 不在允许集合: {sorted(LIFECYCLE)}")
    if event["outcome"] not in OUTCOMES:
        errs.append(f"outcome 不在允许集合: {sorted(OUTCOMES)}")
    if event["target_status"] not in TARGET_STATUSES:
        errs.append(f"target_status 不在允许集合: {sorted(TARGET_STATUSES)}")
    if event["evaluation_status"] not in EVAL_STATUSES:
        errs.append(f"evaluation_status 不在允许集合: {sorted(EVAL_STATUSES)}")
    if not isinstance(event["setup_trigger_met"], bool):
        errs.append("setup_trigger_met 必须是 bool")
    errs += validate_primary_target(event["primary_target"])
    errs += validate_secondary_attribution(event["secondary_attribution"])
    errs += validate_confirmation_status(event["confirmation_status"])
    for field in ("regime", "location", "momentum", "confirmation", "context", "data_quality", "data_sufficiency"):
        if not isinstance(event.get(field), dict):
            errs.append(f"{field} 必须是 dict")
    if "evidence" in event:
        ev = event["evidence"]
        if not isinstance(ev, dict):
            errs.append("evidence 必须是 dict（supporting/contradicting/unknown 各为 list）")
        else:
            for k in ("supporting", "contradicting", "unknown"):
                if k in ev and not isinstance(ev[k], list):
                    errs.append(f"evidence.{k} 必须是 list")
    for field in ("content_hash", "prev_hash", "event_hash"):
        val = event.get(field)
        if field == "prev_hash":
            # 链首事件的 prev_hash 允许为空串
            if not (isinstance(val, str) and (val == "" or len(val) == 64)):
                errs.append("prev_hash 必须是 64 位 hex 字符串或空串（链首）")
        elif not isinstance(val, str) or len(val) != 64:
            errs.append(f"{field} 必须是 64 位 hex 字符串")
    if event.get("episode_id") is not None and not isinstance(event["episode_id"], str):
        errs.append("episode_id 必须是 null 或字符串")
    return errs


def validate_snapshot(snapshot: Dict[str, Any]) -> List[str]:
    errs = _errors_missing(snapshot, REQUIRED_SNAPSHOT_FIELDS)
    if errs:
        return errs
    if snapshot["session"] not in SESSIONS:
        errs.append(f"session 不在允许集合: {sorted(SESSIONS)}")
    if not _is_iso_datetime(snapshot["created_at"]):
        errs.append("created_at 必须是 ISO 8601 时间戳")
    if not isinstance(snapshot["spot"], (int, float)) or snapshot["spot"] <= 0:
        errs.append("spot 必须是正数")
    if not isinstance(snapshot["ticker"], str) or not snapshot["ticker"]:
        errs.append("ticker 必须是非空字符串")
    for field in ("regime", "location", "momentum", "confirmation", "context", "data_quality", "data_sufficiency"):
        if field in snapshot and not isinstance(snapshot[field], dict):
            errs.append(f"{field} 必须是 dict")
    if "snapshot_hash" in snapshot and (
        not isinstance(snapshot["snapshot_hash"], str) or len(snapshot["snapshot_hash"]) != 64
    ):
        errs.append("snapshot_hash 必须是 64 位 hex 字符串")
    return errs


def validate_revision(rev: Dict[str, Any]) -> List[str]:
    errs: List[str] = []
    for f in (
        "revision_id",
        "event_id",
        "result",
        "ts",
        "evaluation_rule_version",
        "snapshot_hash",
        "data_timestamp",
    ):
        if f not in rev:
            errs.append(f"revision 缺少字段: {f}")
    if rev.get("result") not in OUTCOMES:
        errs.append(f"revision.result 不在允许集合: {sorted(OUTCOMES)}")
    if not _is_iso_datetime(rev.get("ts")):
        errs.append("revision.ts 必须是 ISO 8601 时间戳")
    if rev.get("result") == "INVALIDATED" and not rev.get("reason"):
        errs.append("revision.result=INVALIDATED 时必须提供 reason")
    if rev.get("result") == "EXPIRED" and not rev.get("reason"):
        errs.append("revision.result=EXPIRED 时建议提供 reason（缺数据的具体原因）")
    if "evaluation_status" in rev and rev["evaluation_status"] not in EVAL_STATUSES:
        errs.append(f"revision.evaluation_status 不在允许集合: {sorted(EVAL_STATUSES)}")
    return errs


def assert_valid_event(event: Dict[str, Any]) -> None:
    errs = validate_event(event)
    if errs:
        raise SchemaError("; ".join(errs))


def assert_valid_snapshot(snapshot: Dict[str, Any]) -> None:
    errs = validate_snapshot(snapshot)
    if errs:
        raise SchemaError("; ".join(errs))


def assert_valid_revision(rev: Dict[str, Any]) -> None:
    errs = validate_revision(rev)
    if errs:
        raise SchemaError("; ".join(errs))
