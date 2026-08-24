# -*- coding: utf-8 -*-
"""铁律：config/tickers.txt 是标的范围的唯一事实来源。"""

from tests._helpers import ROOT

TICKERS_FILE = ROOT / "config" / "tickers.txt"
MAX_TICKERS = 20


def _load_tickers():
    out = []
    for line in TICKERS_FILE.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#"):
            out.append(line.upper())
    return out


def test_tickers_file_nonempty_unique_and_within_cap():
    tickers = _load_tickers()
    assert tickers, "config/tickers.txt 不能为空（至少一个有效标的）"
    assert len(tickers) == len(set(tickers)), "config/tickers.txt 不允许重复标的"
    assert len(tickers) <= MAX_TICKERS, (
        f"铁律：标的数量上限 {MAX_TICKERS} 个，当前 {len(tickers)} 个"
    )


def test_tickers_parse_same_as_main():
    """主程序读取标的的路径必须与本测试一致（唯一事实来源，无第二份清单）。"""
    import importlib.util
    import sys

    spec = importlib.util.spec_from_file_location("_main_tickers", ROOT / "main.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["_main_tickers"] = mod
    try:
        spec.loader.exec_module(mod)
    except SystemExit:
        pass  # main.py 顶部不执行 main()
    assert mod._load_tickers() == _load_tickers()
