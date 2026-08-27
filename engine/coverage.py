# -*- coding: utf-8 -*-
"""全链覆盖审计（coverage_v1）：IV 有效性三态 + 暴露加权覆盖率。

纪律：
  - Garbage IV → Garbage Gamma → Garbage GEX → Garbage Flip；
  - IV 有效性状态机 v1：VALID / LOW_LIQUIDITY / INVALID（无逐档时间戳 → 不设 STALE）；
  - 覆盖率按 OI 加权（暴露加权），并单独给 Flip 搜索带（±band_pct）内的 OI 加权有效覆盖，
    因为远离现价的深虚值缺口不影响近端 Flip。
"""

from __future__ import annotations

from typing import Any, Dict, List, Optional


def _num(v):
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def classify_iv(c: Dict[str, Any]) -> str:
    """单合约 IV 有效性：
    VALID           iv>0 且 OI>0 且有成交价（last>0）
    LOW_LIQUIDITY   iv>0 且 OI>0，但报价不完整（无 bid/ask 或 last<=0）——能算但置信低
    INVALID         iv 缺失/<=0，或 OI<=0 —— 不参与任何计算
    """
    iv = _num(c.get("iv"))
    oi = _num(c.get("open_interest", c.get("oi")))
    last = _num(c.get("last"))
    bid = _num(c.get("bid"))
    ask = _num(c.get("ask"))
    if iv is None or iv <= 0 or oi is None or oi <= 0:
        return "INVALID"
    if last is None or last <= 0 or bid is None or ask is None or bid <= 0 or ask <= 0:
        return "LOW_LIQUIDITY"
    return "VALID"


WEIGHT = {"VALID": 1.0, "LOW_LIQUIDITY": 0.5, "INVALID": 0.0}


def coverage_audit(
    contracts: Optional[List[Dict[str, Any]]],
    spot: Optional[float],
    band_pct: float = 15.0,
) -> Dict[str, Any]:
    """全链覆盖审计。

    返回：
      total_contracts           链上合约总数
      iv_valid                  {VALID: n, LOW_LIQUIDITY: n, INVALID: n}
      strike_coverage_pct       有效（VALID+LOW_LIQUIDITY）合约数占比（行权价口径）
      oi_coverage_pct           全链 OI 加权有效占比
      valid_only_oi_coverage_pct 全链仅 VALID（无流动性疑点）OI 占比
      band_oi_coverage_pct      Flip 搜索带内 OI 有效占比（VALID+LOW 全额，未加权）
      effective_gex_coverage_pct 带内 OI 加权有效占比（VALID=1 / LOW=0.5，质量门槛使用）
    """
    rows = contracts or []
    total = len(rows)
    counts = {"VALID": 0, "LOW_LIQUIDITY": 0, "INVALID": 0}
    oi_all = 0.0
    oi_valid = 0.0
    oi_valid_only = 0.0
    band_oi_all = 0.0
    band_oi_valid = 0.0
    band_oi_weighted = 0.0
    for c in rows:
        oi = _num(c.get("open_interest", c.get("oi"))) or 0.0
        oi_all += oi
        status = classify_iv(c)
        counts[status] += 1
        if status in ("VALID", "LOW_LIQUIDITY"):
            oi_valid += oi
        if status == "VALID":
            oi_valid_only += oi
        if spot is not None:
            strike = _num(c.get("strike"))
            if strike is not None and abs(strike / spot - 1.0) * 100.0 <= band_pct:
                band_oi_all += oi
                if status in ("VALID", "LOW_LIQUIDITY"):
                    band_oi_valid += oi
                band_oi_weighted += oi * WEIGHT.get(status, 0.0)

    def pct(num: float, den: float) -> Optional[float]:
        return round(num / den * 100.0, 1) if den > 0 else None

    return {
        "schema_version": "coverage_v1",
        "total_contracts": total,
        "iv_valid": counts,
        "strike_coverage_pct": pct(counts["VALID"] + counts["LOW_LIQUIDITY"], total),
        "oi_coverage_pct": pct(oi_valid, oi_all),
        "valid_only_oi_coverage_pct": pct(oi_valid_only, oi_all),
        "band_oi_coverage_pct": pct(band_oi_valid, band_oi_all),
        "effective_gex_coverage_pct": pct(band_oi_weighted, band_oi_all),
    }
