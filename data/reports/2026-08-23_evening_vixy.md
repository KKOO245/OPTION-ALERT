# 期权晚报 2026-08-23

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
VIXY: 晨报缺失（当日未生成），只报收盘事实
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## VIXY

Options: P/C量 0.10 | OI比 0.17 | ATM IV 51.7% | Skew -17.0pp | Term N/A | ExpMove ±11.4% | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.10×（Call 成交高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.17×（Put OI 低于 Call OI）→ 存量 Call-dominant
   ⇒ 两者结构一致
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma: POSITIVE | GEX(存量) N/A | GEX Change N/A | Flip: N/A
结构观察区: N/A（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 18: +1.1% | 距 Call Wall 19: -4.2%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 18（Put Wall）；上方 19（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 17.0C — Vol N/A | OI 281→386 (ΔOI +105张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增105张（+37.4% vs前日OI），值得跟踪（方向未知）
09-18 20.0C — Vol N/A | OI 682→741 (ΔOI +59张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增59张（+8.7% vs前日OI），值得跟踪（方向未知）
09-18 25.0C — Vol N/A | OI 496→538 (ΔOI +42张) | ΔOI/Volume N/A | Magnitude: LOW | 完整度: LOW
   ⇒ 净增42张（量数据缺失），以日内换手为主
09-18 26.0C — Vol N/A | OI 145→161 (ΔOI +16张) | ΔOI/Volume N/A | Magnitude: LOW | 完整度: LOW
   ⇒ 净增16张（量数据缺失），以日内换手为主
09-18 18.0P — Vol N/A | OI 372→387 (ΔOI +15张) | ΔOI/Volume N/A | Magnitude: LOW | 完整度: LOW
   ⇒ 净增15张（量数据缺失），以日内换手为主
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-23/VIXY_evening.json