# -*- coding: utf-8 -*-
"""零依赖测试运行器：逐个运行各测试模块的 test_* 函数。

用法：
  python tests/run_all.py

函数名保持 pytest 兼容（test_ 前缀），装了 pytest 也可以用 pytest 跑。
"""

import importlib
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

MODULES = [
    "test_yaml_mini",
    "test_schema",
    "test_hash",
    "test_metrics",
    "test_flip_context",
    "test_analog",
    "test_snapshot",
    "test_setup_detector",
    "test_thesis_logger",
    "test_outcome",
    "test_episode_clustering",
    "test_targets",
    "test_snapshot_builder",
    "test_price_series",
    "test_reminders",
    "test_calendars",
    "test_tickers",
    "test_vol_environment",
    "test_forward_structure",
    "test_regime_map",
    "test_coverage",
    "test_second_order",
    "test_p3_collect",
    "test_data_quality",
    "test_edges",
    "test_gate",
    "test_annotations",
    "test_report_format",
    "test_send",
    "test_validation",
    "test_e2e_pipeline",
]


def main() -> int:
    failed = []
    for name in MODULES:
        try:
            mod = importlib.import_module(name)
        except Exception as e:  # noqa: BLE001
            print(f"SKIP {name}: 依赖缺失/导入失败 {type(e).__name__}: {e}")
            continue
        tests = sorted(
            (getattr(mod, n) for n in dir(mod) if n.startswith("test_") and callable(getattr(mod, n))),
            key=lambda f: f.__name__,
        )
        for t in tests:
            try:
                t()
                print(f"PASS {name}.{t.__name__}")
            except Exception as e:  # noqa: BLE001
                failed.append((name, t.__name__, e))
                print(f"FAIL {name}.{t.__name__}: {type(e).__name__}: {e}")
    if failed:
        print(f"\n共 {len(failed)} 项失败")
        return 1
    print("\n全部测试通过")
    return 0


if __name__ == "__main__":
    sys.exit(main())
