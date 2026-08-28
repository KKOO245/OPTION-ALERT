# -*- coding: utf-8 -*-
from main import _chunk_text


def test_short_text_single_chunk():
    chunks = _chunk_text("a\nb\nc", limit=1900)
    assert chunks == ["a\nb\nc"]


def test_multiline_respects_limit():
    lines = ["x" * 500 for _ in range(8)]
    text = "\n".join(lines)  # 4007 字符
    chunks = _chunk_text(text, limit=1900)
    assert all(len(c) <= 1900 for c in chunks)
    assert "\n".join(chunks) == text  # 按行重建应还原原文


def test_long_single_line_hard_split():
    line = "y" * 5000
    chunks = _chunk_text(line, limit=1900)
    assert all(len(c) <= 1900 for c in chunks)
    assert "".join(chunks) == line


def test_chunk_count():
    text = "\n".join("z" * 500 for _ in range(10))  # 5000 chars total
    chunks = _chunk_text(text, limit=1900)
    # 每行 500，3 行约 1502 上限内 → 每 chunk 3 行；10 行 → 4 chunks
    assert len(chunks) == 4
