# -*- coding: utf-8 -*-
"""SHA-256 哈希与哈希链。

- content_hash：剔除哈希字段后的事件内容哈希（检测内容篡改）。
- event_hash：content + prev_hash 的哈希（检测中间记录被删除/插入）。
- snapshot_hash：快照内容哈希（剔除自身哈希字段）。
"""

from __future__ import annotations

import hashlib
import json
from datetime import date, datetime
from typing import Any, Iterable, List, Tuple

HASH_FIELDS = ("content_hash", "prev_hash", "event_hash", "snapshot_hash")


def _default(obj: Any) -> str:
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    raise TypeError(f"不可序列化类型: {type(obj).__name__}")


def canonical_json(obj: Any) -> str:
    return json.dumps(
        obj,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        default=_default,
    )


def _sha256_hex(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def content_hash(obj: Any, exclude: Tuple[str, ...] = HASH_FIELDS) -> str:
    """事件/快照内容哈希：剔除哈希字段后 canonical JSON 的 SHA-256。"""
    if isinstance(obj, dict):
        payload = {k: v for k, v in obj.items() if k not in exclude}
    else:
        payload = obj
    return _sha256_hex(canonical_json(payload).encode("utf-8"))


def event_hash(obj: dict, prev_hash: str) -> str:
    """事件哈希：content + prev_hash，形成哈希链。"""
    body = content_hash(obj)
    return _sha256_hex(f"{body}|{prev_hash}".encode("utf-8"))


def snapshot_hash(obj: dict) -> str:
    return content_hash(obj, exclude=("snapshot_hash",))


def verify_chain(events: Iterable[dict]) -> Tuple[bool, List[str]]:
    """校验内容哈希与链式连续性。返回 (是否全部通过, 错误列表)。"""
    errors: List[str] = []
    prev: str = ""
    for i, ev in enumerate(events):
        pos = f"event[{i}] {ev.get('event_id', '?')}"
        exp_content = content_hash(ev)
        if ev.get("content_hash") != exp_content:
            errors.append(f"{pos}: content_hash 不匹配（记录被修改）")
        exp_event = event_hash(ev, prev)
        if ev.get("event_hash") != exp_event:
            errors.append(f"{pos}: event_hash 不匹配（链断裂或被篡改）")
        if prev and ev.get("prev_hash") != prev:
            errors.append(f"{pos}: prev_hash 与上一事件不连续")
        prev = ev.get("event_hash") or ""
    return not errors, errors
