# -*- coding: utf-8 -*-
"""报告内提醒行（预提交规则，全部带可执行命令）。

规则（预提交）：
  - 每周五（早报+晚报）：提醒本地镜像 git pull。
  - 每两周周五（逢基准周）：提醒周六 10:30 数据归档自动运行（含手动命令）。
  - 每月最后一个周五：提醒月度备份（SQLite 拷贝到备份目录/网盘）。
  - 每月第一个工作日（晚报）：提醒下载上个月 Releases 归档（保留原逻辑）。
"""

from __future__ import annotations

import datetime
from typing import List

MIRROR_DIR = r"D:\git\Option Alert-数据储存"
PYTHON = r"D:\git\python\python.exe"
ARCHIVE_SCRIPT = (
    r"C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py"
)
DB_PATH = r"D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db"
ARCHIVE_REF_FRIDAY = datetime.date(2026, 8, 28)  # 双周基准周五


def is_first_business_day(d: datetime.date) -> bool:
    if d.weekday() >= 5:
        return False
    for day in range(1, d.day):
        if datetime.date(d.year, d.month, day).weekday() < 5:
            return False
    return True


def _is_archive_friday(d: datetime.date) -> bool:
    """逢双周的周五（归档提醒周）。"""
    return d.weekday() == 4 and (d - ARCHIVE_REF_FRIDAY).days % 14 == 0


def _is_last_friday(d: datetime.date) -> bool:
    """每月最后一个周五（22~31 号之间的周五必是最后一个周五）。"""
    return d.weekday() == 4 and d.day >= 22


def _weekend_lines(now: datetime.datetime) -> List[str]:
    lines: List[str] = []
    lines.append(f"• 每周同步：cd {MIRROR_DIR}；git pull")
    if _is_archive_friday(now.date()):
        lines.append(
            f"• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；"
            f"若未自动运行，手动执行：{PYTHON} {ARCHIVE_SCRIPT}"
        )
    if _is_last_friday(now.date()):
        lines.append(f"• 月度备份：把 {DB_PATH} 拷贝到网盘/移动盘保存")
    return lines


def morning_reminder_lines(now: datetime.datetime) -> List[str]:
    """周五早报：周末待办速览（含命令）。"""
    if now.weekday() != 4:
        return []
    lines = ["📌 周末待办（详情见今晚晚报）："]
    lines += _weekend_lines(now)
    return lines


def evening_reminder_lines(now: datetime.datetime) -> List[str]:
    lines: List[str] = []
    if now.weekday() == 4:  # 周五
        lines.append("📌 周末待办：")
        lines += _weekend_lines(now)
    if is_first_business_day(now.date()):
        lines.append(
            "📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，"
            f"请在 {MIRROR_DIR} 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。"
        )
    return lines
