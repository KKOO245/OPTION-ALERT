# -*- coding: utf-8 -*-
"""实时快照生成器（P0.2 第一步的"活"入口）。

在你本机运行（需要 requests / pandas / numpy / scipy / yfinance，即现有 requirements）：

    python src/pipeline_snapshot.py --ticker SOXX --session morning

流程：CBOE 期权链（yfinance 兜底）→ compute_metrics() → snapshot_builder
      → SnapshotStore 落盘（state/ + analytics/daily/）。

注意：本文件不修改现有 options_report.py；它只负责"把真实抓取数据转成
snapshot_v1 并入库"，报告层（P0.3）再消费快照。
"""

from __future__ import annotations

import argparse
import datetime
import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)
sys.path.insert(0, os.path.join(BASE_DIR, "src"))

import data_fetcher as fetcher  # noqa: E402
import metrics as metrics_mod  # noqa: E402
import storage  # noqa: E402
from engine import yaml_mini  # noqa: E402
from engine.snapshot import SnapshotStore  # noqa: E402
from engine.snapshot_builder import build_snapshot, load_analytics_rows  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description="实时快照生成器（CBOE/yfinance → snapshot_v1）")
    p.add_argument("--ticker", required=True)
    p.add_argument("--session", choices=["morning", "evening", "早报", "晚报"], default="morning")
    p.add_argument("--config-root", default=os.path.join(BASE_DIR, "config"))
    p.add_argument("--data-root", default=os.environ.get("OPTION_ALERT_DATA_ROOT", BASE_DIR))
    p.add_argument("--created-at", help="ISO 时间戳；缺省用当前时间")
    args = p.parse_args()

    ticker = args.ticker.upper()
    contracts, spot, source = fetcher.fetch_chain(ticker)
    prev = storage.load_prev_snapshot(ticker)
    m = metrics_mod.compute_metrics(contracts, spot, prev=prev)
    if not m:
        print("compute_metrics 返回空，无法生成快照")
        return 1

    created_at = args.created_at or datetime.datetime.now().astimezone().isoformat(timespec="seconds")
    thresholds = yaml_mini.load(os.path.join(args.config_root, "thresholds.yaml"))
    analytics_path = os.path.join(args.data_root, "analytics", f"{ticker}.csv")
    if not os.path.exists(analytics_path):
        analytics_path = os.path.join(args.data_root, "data", "analytics", f"{ticker}.csv")
    rows = load_analytics_rows(analytics_path)
    vol_environment = None
    try:
        from src.vol_environment import build_vol_environment_for_run

        vol_environment = build_vol_environment_for_run(
            datetime.datetime.now().astimezone(),
            args.session,
            args.data_root,
            args.config_root,
        )
    except Exception as e:
        print(f"[警告] vol_environment 构建失败: {e}")
    snap = build_snapshot(
        ticker, args.session, m, spot, created_at,
        analytics_rows=rows, thresholds=thresholds, source=source,
        vol_environment=vol_environment,
    )
    stored = SnapshotStore(args.data_root).store(snap)
    missing = sum(
        1 for v in stored["data_sufficiency"].values()
        if v in ("INSUFFICIENT_DATA", "N/A")
    )
    print(
        f"快照已存储: {stored['ticker']} {stored['session']} {stored['created_at']} "
        f"hash={stored['snapshot_hash'][:12]}... 待积累/缺失字段={missing}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
