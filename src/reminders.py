# -*- coding: utf-8 -*-
"""报告内提醒行（方案 A：本地每周镜像 + 每月归档下载）。

规则（预提交）：
  - 每周五晚报：提醒在本地镜像目录执行 git pull。
  - 每月第一个工作日晚报：提醒下载上个月的 Releases 归档到本地。
    选"第一个工作日"而不是最后一个：归档是次月 1 日才生成的，
    最后一个工作日提醒时归档还不存在。
"""

from __future__ import annotations

import datetime
from typing import List

MIRROR_DIR = "D:\\git\\Option Alert-数据储存"


def is_first_business_day(d: datetime.date) -> bool:
    if d.weekday() >= 5:
        return False
    for day in range(1, d.day):
        if datetime.date(d.year, d.month, day).weekday() < 5:
            return False
    return True


def evening_reminder_lines(now: datetime.datetime) -> List[str]:
    lines: List[str] = []
    if now.weekday() == 4:  # 周五
        lines.append(
            f"💾 每周本地备份提醒：请在 `{MIRROR_DIR}` 运行 `git pull`，"
            "把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。"
        )
    if is_first_business_day(now.date()):
        lines.append(
            "📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，"
            "请在本地镜像目录下载解压保存（以后仓库做月度清理时，归档就是完整副本）。"
        )
    return lines
