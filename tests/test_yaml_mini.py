# -*- coding: utf-8 -*-
from engine import yaml_mini
from tests._helpers import ROOT


def _expect_error(fn, exc=yaml_mini.YAMLSubsetError):
    try:
        fn()
    except exc:
        return
    raise AssertionError(f"应抛出 {exc.__name__}")


def test_parse_basic_scalars():
    d = yaml_mini.loads(
        """
name: SOXX
spot: 497.2
count: 3
negative: -0.02
active: true
missing: null
date: "2026-08-22"
quoted: '>='
plain: below_flip
"""
    )
    assert d["name"] == "SOXX"
    assert d["spot"] == 497.2
    assert d["count"] == 3
    assert d["negative"] == -0.02
    assert d["active"] is True
    assert d["missing"] is None
    assert d["date"] == "2026-08-22"
    assert d["quoted"] == ">="
    assert d["plain"] == "below_flip"


def test_parse_nested_map_and_list():
    d = yaml_mini.loads(
        """
setups:
  - setup_id: A
    name: Trend
    core:
      - field: regime.trend
        op: in
        value:
          - DOWN
      - field: regime.gamma
        op: eq
        value: NEGATIVE
  - setup_id: B1
    name: IV Momentum
"""
    )
    assert d["setups"][0]["setup_id"] == "A"
    assert d["setups"][0]["core"][0]["value"] == ["DOWN"]
    assert d["setups"][1]["name"] == "IV Momentum"


def test_comments_stripped():
    d = yaml_mini.loads(
        """
# 整行注释
key: value  # 行内注释
"""
    )
    assert d == {"key": "value"}


def test_tab_rejected():
    _expect_error(lambda: yaml_mini.loads("a: 1\n\tb: 2"))


def test_flow_syntax_rejected():
    _expect_error(lambda: yaml_mini.loads("value: [DOWN, UP]"))
    _expect_error(lambda: yaml_mini.loads("value: {a: 1}"))


def test_root_config_files_load():
    for name in ("setups", "thresholds", "universe", "regimes", "targets"):
        d = yaml_mini.load(str(ROOT / "config" / f"{name}.yaml"))
        assert isinstance(d, dict) and d, name
