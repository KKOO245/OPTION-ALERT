# -*- coding: utf-8 -*-
"""报告格式工具：表格/代码块/标题（P0.3 规格 v1 格式修复）。"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


def fmt(v: Any, digits: int = 2, suffix: str = "") -> str:
    if v is None:
        return "N/A"
    try:
        return f"{v:,.{digits}f}{suffix}"
    except (TypeError, ValueError):
        return str(v)


def fmt_pct(v: Any, digits: int = 1) -> str:
    if v is None:
        return "N/A"
    try:
        return f"{v * 100:.{digits}f}%"
    except (TypeError, ValueError):
        return str(v)


def ticker_heading(ticker: str) -> str:
    """ticker 大标题：独立成行 + 前后空行，杜绝小字标题。"""
    return f"\n## {ticker}\n"


def code_block(text: str) -> str:
    return "```\n" + text + "\n```"


def table(rows: List[Dict[str, Any]], col_map: Dict[str, str], title: Optional[str] = None) -> str:
    """表格独立代码块，标题在代码块外，保证闭合。"""
    if not rows:
        body = "(无数据)"
    else:
        headers = list(col_map.keys())
        labels = [col_map[h] for h in headers]

        def cell(v: Any) -> str:
            if v is None:
                return "N/A"
            if isinstance(v, float):
                return f"{v:,.2f}" if abs(v) >= 1 else f"{v:.4f}"
            if isinstance(v, int):
                return f"{v:,}"
            return str(v)

        body_rows = [[cell(r.get(h)) for h in headers] for r in rows]
        widths = [len(l) for l in labels]
        for row in body_rows:
            for i, c in enumerate(row):
                widths[i] = max(widths[i], len(c))

        def pad(cells):
            return " | ".join(c.ljust(widths[i]) for i, c in enumerate(cells))

        body_lines = [pad(labels), "-+-".join("-" * w for w in widths)]
        body_lines += [pad(r) for r in body_rows]
        body = "\n".join(body_lines)
    block = code_block(body)
    return f"**{title}**\n{block}" if title else block


def sep() -> str:
    return "---"
