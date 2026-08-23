# -*- coding: utf-8 -*-
"""不可变 Thesis Event 存储。

文件（data_root 下）：
  thesis/events.jsonl             事件本体（append-only，核心字段永不修改）
  thesis/outcome_revisions.jsonl  outcome 追加 revision（append-only）
  thesis/audit.jsonl              每日触发审计（append-only）
  episodes/episodes.jsonl         Episode 聚类结果（派生视图，可确定性重算）

不可变规则：
  - 事件写入后不再修改；Outcome 以 revision 形式追加。
  - 每次写入前先校验哈希链，发现篡改/断裂则拒绝继续写入。
  - read_model() 把 revision 与 episode 合并成"读取视图"，不修改原始行。
"""

from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from engine import hash as hashing
from engine.schema import SchemaError, assert_valid_event, assert_valid_revision


class IntegrityError(RuntimeError):
    pass


class EventStore:
    def __init__(self, data_root: str | Path):
        self.root = Path(data_root)
        self.events_path = self.root / "thesis" / "events.jsonl"
        self.revisions_path = self.root / "thesis" / "outcome_revisions.jsonl"
        self.audit_path = self.root / "thesis" / "audit.jsonl"
        self.episodes_path = self.root / "episodes" / "episodes.jsonl"

    # ---------- 读取 ----------
    def load_events(self, verify: bool = True) -> Tuple[List[Dict[str, Any]], List[str]]:
        if not self.events_path.exists():
            return [], []
        events: List[Dict[str, Any]] = []
        errors: List[str] = []
        for no, line in enumerate(
            self.events_path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if not line.strip():
                continue
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError as e:
                errors.append(f"events.jsonl 第 {no} 行 JSON 解析失败: {e}")
        if verify:
            ok, chain_errors = hashing.verify_chain(events)
            if not ok:
                errors.extend(chain_errors)
        return events, errors

    def load_revisions(self) -> List[Dict[str, Any]]:
        if not self.revisions_path.exists():
            return []
        out: List[Dict[str, Any]] = []
        for no, line in enumerate(
            self.revisions_path.read_text(encoding="utf-8").splitlines(), start=1
        ):
            if not line.strip():
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                continue  # 损坏行由 verify() 汇报
        return out

    def load_audits(self) -> List[Dict[str, Any]]:
        if not self.audit_path.exists():
            return []
        out: List[Dict[str, Any]] = []
        for line in self.audit_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        return out

    def load_episodes(self) -> List[Dict[str, Any]]:
        if not self.episodes_path.exists():
            return []
        out: List[Dict[str, Any]] = []
        for line in self.episodes_path.read_text(encoding="utf-8").splitlines():
            if line.strip():
                try:
                    out.append(json.loads(line))
                except json.JSONDecodeError:
                    continue
        return out

    def read_model(self, verify: bool = True) -> Dict[str, Any]:
        """读取视图：事件 + outcome revisions + episode 归属合并。"""
        events, errors = self.load_events(verify=verify)
        revisions = self.load_revisions()
        episodes = self.load_episodes()

        rev_index: Dict[str, List[Dict[str, Any]]] = {}
        for r in revisions:
            rev_index.setdefault(r["event_id"], []).append(r)
        episode_by_event: Dict[str, Dict[str, Any]] = {}
        for ep in episodes:
            for eid in ep.get("event_ids", []):
                episode_by_event[eid] = ep

        merged: List[Dict[str, Any]] = []
        for ev in events:
            copy = dict(ev)
            revs = sorted(rev_index.get(copy["event_id"], []), key=lambda r: r["ts"])
            copy["outcome_revisions"] = revs
            if revs:
                latest = revs[-1]
                copy["outcome"] = latest["result"]
                copy["target_status"] = latest.get("target_status", copy["target_status"])
                copy["evaluation_status"] = latest.get(
                    "evaluation_status", copy["evaluation_status"]
                )
                copy["lifecycle"] = "CLOSED"
                copy["latest_revision"] = latest
            ep = episode_by_event.get(copy["event_id"])
            copy["episode_id"] = ep["episode_id"] if ep else None
            merged.append(copy)
        return {"events": merged, "revisions": revisions, "episodes": episodes, "errors": errors}

    # ---------- 写入 ----------
    def _last_hash(self) -> str:
        events, errors = self.load_events(verify=True)
        if errors:
            raise IntegrityError("哈希链校验失败，拒绝写入: " + "; ".join(errors))
        return events[-1]["event_hash"] if events else ""

    def append_event(self, payload: Dict[str, Any]) -> Dict[str, Any]:
        self.events_path.parent.mkdir(parents=True, exist_ok=True)
        prev_hash = self._last_hash()

        event = dict(payload)
        event["event_id"] = self._next_event_id(event)
        event["episode_id"] = None
        event["content_hash"] = hashing.content_hash(event)
        event["prev_hash"] = prev_hash
        event["event_hash"] = hashing.event_hash(event, prev_hash)
        assert_valid_event(event)

        with self.events_path.open("a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(event, ensure_ascii=False) + "\n")
        return event

    def _next_event_id(self, payload: Dict[str, Any]) -> str:
        day = payload["created_at"][:10].replace("-", "")
        prefix = f"{payload['ticker']}_{day}_{payload['setup_id']}_"
        events, _ = self.load_events(verify=False)
        existing = {ev.get("event_id") for ev in events}
        seq = 1
        while f"{prefix}{seq:03d}" in existing:
            seq += 1
        return f"{prefix}{seq:03d}"

    def append_revision(self, rev: Dict[str, Any]) -> Optional[Dict[str, Any]]:
        """追加 outcome revision；相同 (event_id, rule, anchor) 幂等跳过。"""
        events, errors = self.load_events(verify=True)
        if errors:
            raise IntegrityError("哈希链校验失败，拒绝写入 revision: " + "; ".join(errors))
        event_ids = {ev["event_id"] for ev in events}
        if rev["event_id"] not in event_ids:
            raise KeyError(f"event 不存在: {rev['event_id']}")
        existing = self.load_revisions()
        for r in existing:
            if (
                r["event_id"] == rev["event_id"]
                and r.get("evaluation_rule_version") == rev.get("evaluation_rule_version")
                and r.get("evaluation_anchor_date") == rev.get("evaluation_anchor_date")
            ):
                return None  # 幂等：不重复写入
        assert_valid_revision(rev)
        self.revisions_path.parent.mkdir(parents=True, exist_ok=True)
        with self.revisions_path.open("a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(rev, ensure_ascii=False) + "\n")
        return rev

    def audit(self, record: Dict[str, Any]) -> Dict[str, Any]:
        self.audit_path.parent.mkdir(parents=True, exist_ok=True)
        existing = {a.get("audit_id") for a in self.load_audits()}
        if record.get("audit_id") in existing:
            return record
        with self.audit_path.open("a", encoding="utf-8", newline="\n") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
        return record

    def write_episodes(self, episodes: List[Dict[str, Any]]) -> None:
        self.episodes_path.parent.mkdir(parents=True, exist_ok=True)
        tmp = self.episodes_path.with_suffix(".jsonl.tmp")
        with tmp.open("w", encoding="utf-8", newline="\n") as f:
            for ep in episodes:
                f.write(json.dumps(ep, ensure_ascii=False) + "\n")
        tmp.replace(self.episodes_path)

    # ---------- 完整性审计 ----------
    def verify(self) -> Tuple[bool, List[str]]:
        events, errors = self.load_events(verify=True)
        revisions = self.load_revisions()
        event_ids = {ev["event_id"] for ev in events}
        snap_hashes = {ev["event_id"]: ev["snapshot_hash"] for ev in events}
        for r in revisions:
            if r["event_id"] not in event_ids:
                errors.append(f"revision 引用不存在的 event: {r['event_id']}")
            elif snap_hashes[r["event_id"]] != r.get("snapshot_hash"):
                errors.append(
                    f"revision {r.get('revision_id')} 的 snapshot_hash 与 event 不一致"
                )
        return not errors, errors
