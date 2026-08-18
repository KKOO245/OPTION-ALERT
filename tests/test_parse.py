# -*- coding: utf-8 -*-
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from data_fetcher import parse_osi


def test_parse_standard_contract():
    r = parse_osi("NVDA260918C00150000")
    assert r == {"expiration": "2026-09-18", "type": "call", "strike": 150.0}


def test_parse_put_contract():
    r = parse_osi("AAPL260918P00200000")
    assert r == {"expiration": "2026-09-18", "type": "put", "strike": 200.0}


def test_parse_adjusted_root():
    r = parse_osi("BRKB1260920C00095000")
    assert r == {"expiration": "2026-09-20", "type": "call", "strike": 95.0}


def test_parse_invalid():
    assert parse_osi("") == {}
    assert parse_osi("garbage") == {}


if __name__ == "__main__":
    for fn in (test_parse_standard_contract, test_parse_put_contract,
               test_parse_adjusted_root, test_parse_invalid):
        fn()
        print(f"PASS {fn.__name__}")
