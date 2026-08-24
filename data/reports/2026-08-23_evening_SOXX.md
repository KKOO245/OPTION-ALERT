# 期权晚报 2026-08-23

市场背景： SPY $765.72 ｜ VIX 15.13 ｜ CNN 恐惧贪婪 55.2（greed）

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
SOXX: 晨报缺失（当日未生成），只报收盘事实
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞


## SOXX

Options: P/C量 4.24 | OI比 0.68 | ATM IV 39.5% | Skew 3.7pp | Term 1.02 | ExpMove ±4.4% | Rank — (历史不足)
   ⇒ Put/Call Volume: 4.24×（Put 成交显著高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（Put OI 低于 Call OI）→ 存量 Call-dominant
   ⇒ 两者结构不一致
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma: NEGATIVE | GEX(存量) N/A | GEX Change N/A | Flip: N/A
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: N/A（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 500: +3.9% | 距 Call Wall 670: -22.5%
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall）；上方 670（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-23/SOXX_evening.json