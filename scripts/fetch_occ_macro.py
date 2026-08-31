#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""OCC 全市场 Call/Put OI 汇总历史（免费、公开批量端点）。

输出：data/oi_history/OCC_DAILY.csv
列：date, equity_call_oi, equity_put_oi, equity_pcr_oi,
    index_call_oi, index_put_oi, index_pcr_oi,
    occ_call_oi, occ_put_oi, occ_total_oi

端点：https://marketdata.theocc.com/daily-open-interest?reportDate=MM/DD/YYYY&action=download&format=csv
说明：这是"按资产类别"的汇总表（不是逐合约），用于晨报宏观情绪参考线。
     断点续传：已存在输出文件时从最后日期之后继续。

用法：
  python scripts/fetch_occ_macro.py                    # 2023-06-01 → 昨天
  python scripts/fetch_occ_macro.py --start 2021-01-01 # 自定义起点
"""

from __future__ import annotations

import argparse
import csv
import datetime
import gzip
import io
import os
import sys
import time
import urllib.request
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_OUT = REPO_ROOT / "data" / "oi_history" / "OCC_DAILY.csv"
URL = "https://marketdata.theocc.com/daily-open-interest"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/126.0 Safari/537.36",
    "Accept": "text/csv,text/plain,application/octet-stream,*/*",
    "Accept-Encoding": "identity",  # 明确要未压缩内容；若仍返回 gzip 则自动解压兜底
    "Accept-Language": "en-US,en;q=0.9",
    "Origin": "https://www.theocc.com",
    "Referer": "https://www.theocc.com/",
    "Connection": "keep-alive",
}
COLUMNS = [
    "date", "equity_call_oi", "equity_put_oi", "equity_pcr_oi",
    "index_call_oi", "index_put_oi", "index_pcr_oi",
    "occ_call_oi", "occ_put_oi", "occ_total_oi",
]


def _log(msg: str) -> None:
    print(f"[occ] {msg}", flush=True)


def _business_days(start: datetime.date, end: datetime.date):
    d = start
    while d <= end:
        if d.weekday() < 5:
            yield d
        d += datetime.timedelta(days=1)


def _fetch(date: datetime.date) -> str | None:
    url = f"{URL}?reportDate={date.month:02d}/{date.day:02d}/{date.year}&action=download&format=csv"
    req = urllib.request.Request(url, headers=HEADERS)
    last_err: Exception | None = None
    for attempt in range(2):
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                raw = resp.read()
            # 兜底解压：个别情况即使要求 identity 仍返回 gzip
            if raw[:2] == b"\x1f\x8b":
                raw = gzip.decompress(raw)
            for enc in ("utf-8-sig", "utf-8", "latin-1"):
                try:
                    return raw.decode(enc)
                except UnicodeDecodeError:
                    continue
            return raw.decode("utf-8", errors="replace")
        except Exception as e:  # noqa: BLE001
            last_err = e
            time.sleep(1.0)
    raise last_err or RuntimeError("download failed")


def _parse(text: str) -> list[list[str]] | None:
    """从 OCC 汇总 CSV 提取 Equity/Index/OCC Total 的 Call/Put/Total 行。

    返回 [[date, eq_c, eq_p, eq_t, idx_c, idx_p, idx_t, occ_c, occ_p, occ_t], ...]
    解析失败返回 None。
    """
    rows = list(csv.reader(io.StringIO(text)))
    header_idx = None
    for i, row in enumerate(rows):
        cells = [c.strip() for c in row]
        if cells and cells[0].upper() == "DATE":
            header_idx = i
            break
    if header_idx is None:
        return None
    out: list[list[str]] = []
    for row in rows[header_idx + 1 :]:
        cells = [c.strip() for c in row]
        if not cells or not cells[0]:
            continue
        first = cells[0].strip().strip('"')
        # 子表头行（Calls,Puts,Total）或非日期行 → 跳过
        try:
            datetime.datetime.strptime(first, "%m/%d/%Y")
        except ValueError:
            try:
                datetime.datetime.strptime(first, "%Y-%m-%d")
            except ValueError:
                continue
        if len(cells) < 15:
            continue

        def num(s: str) -> float:
            return float(s.replace(",", "").strip() or 0.0)

        eq_c, eq_p, eq_t = num(cells[1]), num(cells[2]), num(cells[3])
        idx_c, idx_p, idx_t = num(cells[4]), num(cells[5]), num(cells[6])
        occ_c, occ_p, occ_t = num(cells[13]), num(cells[14]), num(cells[15])
        out.append(
            [
                first,
                f"{eq_c:.0f}", f"{eq_p:.0f}",
                f"{eq_p / eq_c:.4f}" if eq_c > 0 else "",
                f"{idx_c:.0f}", f"{idx_p:.0f}",
                f"{idx_p / idx_c:.4f}" if idx_c > 0 else "",
                f"{occ_c:.0f}", f"{occ_p:.0f}", f"{occ_t:.0f}",
            ]
        )
    return out or None


def _probe(date: datetime.date) -> None:
    """拉一天并打印原始内容与解析结果，用于诊断格式/编码问题。"""
    try:
        raw_text = _fetch(date)
    except Exception as e:  # noqa: BLE001
        _log(f"下载失败: {e}")
        return
    _log(f"日期 {date} 原始内容（前 500 字符）:")
    _log(repr(raw_text[:500]))
    parsed = _parse(raw_text)
    _log(f"解析结果: {parsed[0] if parsed else 'None'}")


def main() -> int:
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass
    p = argparse.ArgumentParser(description="OCC 全市场 Call/Put OI 汇总历史")
    p.add_argument("--start", default="2023-06-01", help="YYYY-MM-DD（默认 2023-06-01）")
    p.add_argument("--end", default=None, help="YYYY-MM-DD（默认昨天）")
    p.add_argument("--out", default=str(DEFAULT_OUT))
    p.add_argument("--sleep", type=float, default=0.2, help="请求间隔秒（默认 0.2）")
    p.add_argument("--probe", default=None, help="YYYY-MM-DD：只拉这一天并打印原始内容/解析结果")
    args = p.parse_args()

    start = datetime.date.fromisoformat(args.start)
    end = datetime.date.fromisoformat(args.end) if args.end else datetime.date.today() - datetime.timedelta(days=1)
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)

    if args.probe:
        _probe(datetime.date.fromisoformat(args.probe))
        return 0

    # 断点续传
    seen: set[str] = set()
    if out.exists() and out.stat().st_size > 0:
        with open(out, encoding="utf-8") as f:
            for line in f:
                if line.startswith("date,"):
                    continue
                d = line.split(",", 1)[0].strip()
                if d:
                    seen.add(d)
        _log(f"输出已存在，续传（已收录 {len(seen)} 天）")

    ok = skip = fail = 0
    new_rows: list[list[str]] = []
    for d in _business_days(start, end):
        key = d.strftime("%m/%d/%Y")
        if key in seen:
            continue
        try:
            text = _fetch(d)
        except Exception as e:  # noqa: BLE001
            fail += 1
            _log(f"{d} 下载失败: {e}")
            continue
        parsed = _parse(text)
        if not parsed:
            skip += 1  # 节假日/无数据日
            if skip <= 3:
                _log(f"{d} 解析为空（前 200 字符: {text[:200]!r}）")
            continue
        row = parsed[0]
        if row[0] != key:
            row = [key] + row[1:]
        new_rows.append(row)
        seen.add(key)
        ok += 1
        if ok % 50 == 0:
            _log(f"已拉取 {ok} 天（最近 {row[0]}）...")
        time.sleep(args.sleep)

    if new_rows:
        with open(out, "a", encoding="utf-8", newline="") as f:
            w = csv.writer(f)
            if out.stat().st_size == 0:
                w.writerow(COLUMNS)
            for r in new_rows:
                w.writerow(r)
        _log(f"新增 {len(new_rows)} 天 → {out}")
    _log(f"完成：成功 {ok} | 跳过（无数据日）{skip} | 失败 {fail} | 累计 {len(seen)} 天")
    if ok and new_rows:
        _log("样例（首/尾）：")
        with open(out, encoding="utf-8") as f:
            lines = f.read().splitlines()
        for line in lines[:2] + lines[-2:]:
            _log("  " + line)
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
