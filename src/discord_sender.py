# -*- coding: utf-8 -*-
"""Discord 发送：超长消息自动分块（单条上限约 2000 字符）"""

import sys

import requests


def chunk_message(text, max_len=1900):
    if len(text) <= max_len:
        return [text]
    chunks = []
    current = ""
    for line in text.split("\n"):
        candidate = (current + "\n" + line) if current else line
        if len(candidate) > max_len:
            if current:
                chunks.append(current)
            current = line
        else:
            current = candidate
    if current:
        chunks.append(current)
    return chunks


def send_discord_message(webhook_url, content, dry_run=False):
    if dry_run:
        try:
            sys.stdout.reconfigure(errors="replace")
        except Exception:
            pass
        print("===== DRY RUN 消息预览 =====")
        print(content)
        print("===== 结束 =====")
        return
    for chunk in chunk_message(content):
        resp = requests.post(webhook_url, json={"content": chunk}, timeout=30)
        if resp.status_code not in (200, 204):
            raise RuntimeError(f"Discord webhook 发送失败: HTTP {resp.status_code} — {resp.text[:300]}")
    print("已发送到 Discord")
