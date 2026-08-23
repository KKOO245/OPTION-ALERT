# 期权晚报 2026-08-23

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
SLV: 晨报缺失（当日未生成），只报收盘事实
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## SLV

Options: P/C量 0.32 | OI比 0.39 | ATM IV 28.8% | Skew -5.5pp | Term 1.55 | ExpMove ±2.1% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.32×（Call 成交高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（Put OI 低于 Call OI）→ 存量 Call-dominant
   ⇒ 两者结构一致
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma: POSITIVE | GEX(存量) N/A | GEX Change N/A | Flip: ≈57.88 / ≈59.73 / ≈60.98
结构观察区: 58–60（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 50: +25.4% | 距 Call Wall 70: -10.4%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall）；上方 70（Call Wall）。
• Gamma 区域：切换参考 58（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 70.0C — Vol N/A | OI 7438→12720 (ΔOI +5282张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增5282张（+71.0%），连续性待观察（方向未知）
09-18 70.0C — Vol N/A | OI 57196→60424 (ΔOI +3228张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增3228张（+5.6% vs前日OI），值得跟踪（方向未知）
08-26 62.0P — Vol N/A | OI 13→2714 (ΔOI +2701张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增2701张（+20776.9%），连续性待观察（方向未知）
08-24 62.0C — Vol N/A | OI 1437→3159 (ΔOI +1722张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增1722张（+119.8%），连续性待观察（方向未知）
08-26 61.5C — Vol N/A | OI 170→1695 (ΔOI +1525张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增1525张（+897.1%），连续性待观察（方向未知）
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-23/SLV_evening.json