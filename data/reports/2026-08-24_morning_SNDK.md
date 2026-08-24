# 期权晨报 2026-08-24

市场背景： SPY $764.19 ｜ VIX 15.67 ｜ CNN 恐惧贪婪 56.0（greed）

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布


## SNDK

Options: P/C量 0.62 | OI比 0.89 | ATM IV 89.4% | Skew -1.3pp | Term 0.88 | ExpMove ±7.6% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.62×（Call 成交高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（Put OI 低于 Call OI）→ 存量 Call-dominant
   ⇒ 两者结构一致
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma: NEGATIVE | GEX(存量) N/A | GEX Change N/A | Flip: N/A
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: N/A（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 800: +87.0% | 距 Call Wall 2,000: -25.2%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 800（Put Wall）；上方 2,000（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 800.0P — Vol N/A | OI 0→3652 (ΔOI +3652张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增3652张（前日OI缺失），值得跟踪（方向未知）
08-28 800.0P — Vol N/A | OI 286→3040 (ΔOI +2754张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增2754张（+962.9% vs前日OI），连续性待观察（方向未知）
09-18 1350.0P — Vol N/A | OI 0→2566 (ΔOI +2566张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增2566张（前日OI缺失），值得跟踪（方向未知）
09-18 650.0P — Vol N/A | OI 0→2506 (ΔOI +2506张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增2506张（前日OI缺失），值得跟踪（方向未知）
08-28 2000.0C — Vol N/A | OI 637→3127 (ΔOI +2490张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增2490张（+390.9% vs前日OI），连续性待观察（方向未知）
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-24/SNDK_morning.json