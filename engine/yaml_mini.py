# -*- coding: utf-8 -*-
"""严格受限的 YAML 子集解析器（仅用于本项目自有配置文件）。

支持：
  - 注释（整行 # 或行内 " #"）
  - 嵌套 mapping（2 空格缩进，禁止 tab）
  - 列表（- item）
  - 标量：null / true / false / int / float / 引号字符串 / 普通字符串
  - 列表项后跟更深缩进的 mapping 子块（- key: value ... 续行）

不支持（遇到即报错，防止静默误解析）：
  - 流式语法 {...} / [...] / 锚点 / 多行字符串
  - 复杂类型

只用于解析本项目 config/ 下我们完全掌控的五个 YAML 文件；
不要在未经评估的地方用这个解析器解析第三方 YAML。
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, List, Optional, Tuple


class YAMLSubsetError(ValueError):
    pass


def _indent(line: str) -> int:
    if line.startswith("\t"):
        raise YAMLSubsetError("tab 缩进不支持，请使用空格")
    return len(line) - len(line.lstrip(" "))


def _strip_comment(line: str) -> str:
    # 仅去掉 " #" 开头的行内注释与整行注释；引号内 # 保留（本子集不处理转义）
    in_single = in_double = False
    for i, ch in enumerate(line):
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == "#" and not in_single and not in_double and (i == 0 or line[i - 1] in " \t"):
            return line[:i].rstrip()
    return line.rstrip()


def _scalar(text: str) -> Any:
    t = text.strip()
    if t == "":
        return None
    if t.startswith("{") or t.startswith("["):
        raise YAMLSubsetError(f"流式语法（{t[:20]}...）不支持，请改用缩进块")
    if t == "null" or t == "~":
        return None
    if t == "true":
        return True
    if t == "false":
        return False
    if len(t) >= 2 and t[0] == t[-1] and t[0] in ("'", '"'):
        return t[1:-1]
    # 数字（int / float / 负数）
    try:
        if t.lstrip("-").isdigit():
            return int(t)
        float(t)
        return float(t)
    except ValueError:
        pass
    return t


def _partition(text: str) -> Tuple[str, str, str]:
    """按第一个冒号切分 key: value。"""
    in_single = in_double = False
    for i, ch in enumerate(text):
        if ch == "'" and not in_double:
            in_single = not in_single
        elif ch == '"' and not in_single:
            in_double = not in_double
        elif ch == ":" and not in_single and not in_double:
            return text[:i].strip(), text[i + 1 :].strip(), text[i + 1 :].strip()
    return text.strip(), "", ""


class _Line:
    __slots__ = ("indent", "content", "no")

    def __init__(self, indent: int, content: str, no: int):
        self.indent = indent
        self.content = content
        self.no = no


def _prepare(text: str) -> List[_Line]:
    out: List[_Line] = []
    for no, raw in enumerate(text.splitlines(), start=1):
        if "\t" in raw[: len(raw) - len(raw.lstrip(" \t"))]:
            raise YAMLSubsetError(f"第 {no} 行：缩进使用了 tab")
        cleaned = _strip_comment(raw)
        if cleaned.strip() == "":
            continue
        out.append(_Line(_indent(cleaned), cleaned.strip(), no))
    return out


def _parse_block(lines: List[_Line], idx: int, parent_indent: int) -> Tuple[Any, int]:
    if idx >= len(lines):
        return {}, idx
    block_indent = lines[idx].indent
    if block_indent <= parent_indent:
        return {}, idx
    if lines[idx].content.startswith("-"):
        return _parse_list(lines, idx, block_indent)
    return _parse_map(lines, idx, block_indent)


def _parse_list(lines: List[_Line], idx: int, block_indent: int) -> Tuple[List[Any], int]:
    items: List[Any] = []
    n = len(lines)
    while idx < n and lines[idx].indent == block_indent and lines[idx].content.startswith("-"):
        rest = lines[idx].content[1:].strip()
        item: Any
        if rest == "":
            item, idx = _parse_block(lines, idx + 1, block_indent)
            if isinstance(item, dict) and not item:
                item = None
        elif ":" in rest:
            key, val, _ = _partition(rest)
            item = {key: _scalar(val) if val else None}
            idx += 1
            if idx < n and lines[idx].indent > block_indent:
                child, idx = _parse_block(lines, idx, block_indent)
                if not val:
                    item[key] = child
                else:
                    item.update(child)
            items.append(item)
            continue
        else:
            item = _scalar(rest)
            idx += 1
        items.append(item)
    return items, idx


def _parse_map(lines: List[_Line], idx: int, block_indent: int) -> Tuple[dict, int]:
    d: dict = {}
    n = len(lines)
    while idx < n and lines[idx].indent == block_indent and not lines[idx].content.startswith("-"):
        key, rest, raw_rest = _partition(lines[idx].content)
        if key == "":
            raise YAMLSubsetError(f"第 {lines[idx].no} 行：无法解析的 mapping 行：{lines[idx].content!r}")
        idx += 1
        value: Any = _scalar(rest) if rest != "" else None
        if idx < n and lines[idx].indent > block_indent:
            child, idx = _parse_block(lines, idx, block_indent)
            if rest == "":
                value = child
            else:
                raise YAMLSubsetError(
                    f"第 {lines[idx - 1].no} 行：键 {key!r} 已有内联值，不允许再跟缩进子块"
                )
        d[key] = value
    return d, idx


def loads(text: str) -> Any:
    lines = _prepare(text)
    if not lines:
        return {}
    if lines[0].indent != 0:
        raise YAMLSubsetError(f"第 {lines[0].no} 行：根级内容不允许缩进")
    value, consumed = _parse_block(lines, 0, -1)
    if consumed != len(lines):
        raise YAMLSubsetError(f"第 {lines[consumed].no} 行：存在无法归属的缩进块")
    return value


def load(path: str) -> Any:
    p = Path(path)
    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        text = p.read_text(encoding="utf-8-sig")
    return loads(text)
