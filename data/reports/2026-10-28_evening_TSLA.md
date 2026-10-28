# 期权晚报 2026-10-28（快照 16:40 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 16.91 ↓3.5%（5D +1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 420C ΔOI +3,955（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 410.21 → 收盘 404.22（-1.5%） ｜ 今日高 410.85 ｜ 低 397.18 ｜ 昨收 407.46 → 收盘 404.22（-0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.90 | OI比 1.46 | ATM IV 31.7% | Skew 5.0pp | Term 1.16 | ExpMove ±2.5%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常偏陡（Term 1.16）｜保护溢价中性（Skew 5.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.46×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±2.5% ｜ 11-02（5D）±3.2% ｜ 11-04（7D）±4.2% ｜ 11-06（9D）±4.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 116,888,771 | GEX Change vs 上次快照 17,609,545 | Flip: Primary Flip: 380.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 1245 / LOW 127 / INVALID 1064
结构观察区: Primary Flip 380.04（全链重定价，覆盖 90%）
Call Wall 400（弱结构｜现价高于该位 1.1%）
最近结构参考: Call Wall 400（现价高于该位 1.1%）
量化视角： 正 Gamma（1.17亿，无历史分位）｜正 Gamma 增强（+1761万）｜现价位于 Flip 上方 6.36%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 400（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 380（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +15.6k / P +29.5k ｜ Activity HIGH ｜ 2D
11-02  C +5.3k / P +4.3k ｜ Activity HIGH ｜ 5D
11-04  C +3.5k / P +3.2k ｜ Activity HIGH ｜ 7D
11-06  C +9.2k / P +10.3k ｜ Activity HIGH ｜ 9D

📆 10-30 Forward Structure
存量OI: C 204.5k / P 253.3k，今日变化ΔOI: C +15.6k / P +29.5k，平值价格ATM: C $4.90 / P $5.20 ｜ ATM IV 42.0%，净 delta 敞口 -621k shares
Top ΔOI: C 420 +3,955 ｜ P 390 +2,717
仓位参考: Max Pain 382 ｜ Call Wall 420（+3.9%，弱）（OI 22.0k） ｜ Put Wall 380（-6.0%，弱）（OI 8.4k）
量化解读： 存量 Put 重｜ATM IV 42.0%｜历史 Rank 5%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 620,754 股

📆 11-02 Forward Structure
存量OI: C 38.2k / P 16.0k，今日变化ΔOI: C +5.3k / P +4.3k，平值价格ATM: C $6.20 / P $6.58 ｜ ATM IV 33.2%，净 delta 敞口 -62k shares
Top ΔOI: C 440 +758 ｜ C 407 +716
仓位参考: Max Pain 392 ｜ Put Wall 380（-6.0%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 33.2%｜历史 Rank 5%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 62,149 股

📆 11-04 Forward Structure
存量OI: C 8.8k / P 7.3k，今日变化ΔOI: C +3.5k / P +3.2k，平值价格ATM: C $8.08 / P $8.85 ｜ ATM IV 38.0%，净 delta 敞口 22k shares
Top ΔOI: C 425 +580 ｜ P 400 +574 ｜ C 410 +431
仓位参考: Max Pain 398 ｜ Call Wall 410（+1.4%，弱）（OI 1.3k） ｜ Put Wall 385（-4.8%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 38.0%｜历史 Rank 5%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 22,157 股

📆 11-06 Forward Structure
存量OI: C 57.9k / P 65.0k，今日变化ΔOI: C +9.2k / P +10.3k，平值价格ATM: C $9.85 / P $10.10 ｜ ATM IV 38.8%，净 delta 敞口 46k shares
Top ΔOI: C 420 +2,048 ｜ P 400 +927
仓位参考: Max Pain 380 ｜ Call Wall 420（+3.9%，弱）（OI 4.6k）
量化解读： 存量两侧均衡｜ATM IV 38.8%｜历史 Rank 5%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 正 45,748 股

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 42.0% vs 11-02 33.2%（差 +8.8pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/TSLA_evening.json