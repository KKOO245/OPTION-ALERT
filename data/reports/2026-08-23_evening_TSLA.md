# 期权晚报 2026-08-23

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
TSLA: 晨报缺失（当日未生成），只报收盘事实
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## TSLA

Options: P/C量 0.68 | OI比 0.53 | ATM IV 31.1% | Skew -0.8pp | Term 1.31 | ExpMove ±2.3% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.68×（Call 成交高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（Put OI 低于 Call OI）→ 存量 Call-dominant
   ⇒ 两者结构一致
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma: POSITIVE | GEX(存量) N/A | GEX Change N/A | Flip: ≈155.05 / ≈345.10 / ≈375.82
结构观察区: 155–345（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 300: +21.3% | 距 Call Wall 400: -9.0%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 300（Put Wall）；上方 400（Call Wall）。
• Gamma 区域：切换参考 155（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 390.0C — Vol N/A | OI 595→4846 (ΔOI +4251张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增4251张（+714.5%），连续性待观察（方向未知）
08-28 347.5C — Vol N/A | OI 1110→4801 (ΔOI +3691张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增3691张（+332.5%），连续性待观察（方向未知）
08-28 350.0C — Vol N/A | OI 4717→7863 (ΔOI +3146张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增3146张（+66.7%），连续性待观察（方向未知）
08-28 150.0P — Vol N/A | OI 3809→6502 (ΔOI +2693张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增2693张（+70.7%），连续性待观察（方向未知）
08-28 360.0C — Vol N/A | OI 3994→6675 (ΔOI +2681张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增2681张（+67.1%），连续性待观察（方向未知）
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-23/TSLA_evening.json