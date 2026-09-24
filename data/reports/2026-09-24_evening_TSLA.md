# 期权晚报 2026-09-24（快照 16:40 ET）

📊 市场环境

SPY $767.18 ｜ QQQ $741.10
VIX 15.67 ↑3.2%（5D -11.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **事件差分**: 09-25 ATM IV 41.8% vs 09-28 30.8%（差 +11.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-25 390C ΔOI +9,732（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 377.35 → 收盘 377.94（+0.2%） ｜ 今日高 383.33 ｜ 低 375.70 ｜ 昨收 380.12 → 收盘 377.94（-0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.74 | OI比 1.01 | ATM IV 41.8% | Skew -1.2pp | Term 1.05 | ExpMove ±1.8%（近端） | Rank 13%
量化视角： IV 历史低位（Rank 13%，期权偏便宜）｜期限结构正常（Term 1.05）｜Put 保护异常便宜（Skew -1.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（1D）±1.8% ｜ 09-28（4D）±2.6% ｜ 09-30（6D）±3.6% ｜ 10-02（8D）±5.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 158,710,720 | GEX Change vs 上次快照 26,562,610 | Flip: Primary Flip: 360.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1189 / LOW 117 / INVALID 506
结构观察区: Primary Flip 360.37（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 5.5%）
最近结构参考: Flip 360（现价高于该位 4.9%）
量化视角： 正 Gamma（1.59亿，无历史分位）｜正 Gamma 增强（+2656万）｜现价位于 Flip 上方 4.88%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 368（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 360（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +53.7k / P +22.9k ｜ Activity HIGH ｜ 1D
09-28  C +13.0k / P +11.3k ｜ Activity HIGH ｜ 4D
09-30  C +7.8k / P +6.8k ｜ Activity HIGH ｜ 6D
10-02  C +29.5k / P +16.7k ｜ Activity HIGH ｜ 8D

📆 09-25 Forward Structure
存量OI: C 242.6k / P 244.9k，今日变化ΔOI: C +53.7k / P +22.9k，平值价格ATM: C $3.65 / P $3.05 ｜ ATM IV 41.8%，净 delta 敞口 -164k shares
Top ΔOI: C 390 +9,732 ｜ C 400 +7,059 ｜ C 392 +6,708
仓位参考: Max Pain 368 ｜ Call Wall 400（+5.8%，弱）（OI 21.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.8%｜历史 Rank 13%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 负 164,459 股

📆 09-28 Forward Structure
存量OI: C 28.5k / P 18.9k，今日变化ΔOI: C +13.0k / P +11.3k，平值价格ATM: C $5.12 / P $4.64 ｜ ATM IV 30.8%，净 delta 敞口 -59k shares
Top ΔOI: C 400 +1,744
仓位参考: Max Pain 375 ｜ Call Wall 400（+5.8%，弱）（OI 3.1k） ｜ Put Wall 377.5（-0.1%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 30.8%｜历史 Rank 13%（近端代理）｜IV/RV 0.72×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 58,696 股

📆 09-30 Forward Structure
存量OI: C 16.3k / P 12.0k，今日变化ΔOI: C +7.8k / P +6.8k，平值价格ATM: C $7.15 / P $6.50 ｜ ATM IV 35.0%，净 delta 敞口 -50k shares
Top ΔOI: C 400 +1,543 ｜ P 377 +1,445 ｜ C 385 +1,089
仓位参考: Max Pain 375 ｜ Call Wall 400（+5.8%，弱）（OI 2.3k） ｜ Put Wall 377.5（-0.1%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 35.0%｜历史 Rank 13%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 49,750 股

📆 10-02 Forward Structure
存量OI: C 112.7k / P 104.3k，今日变化ΔOI: C +29.5k / P +16.7k，平值价格ATM: C $10.16 / P $9.31 ｜ ATM IV 43.4%，净 delta 敞口 414k shares
Top ΔOI: C 385 +7,694 ｜ C 400 +2,791
仓位参考: Max Pain 360 ｜ Call Wall 360（-4.7%）（OI 16.7k）
量化解读： 存量两侧均衡｜ATM IV 43.4%｜历史 Rank 13%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 正 413,534 股

📅 事件差分（观察，非因果）: 09-25（1D）ATM IV 41.8% vs 09-28 30.8%（差 +11.0pp）——覆盖 耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/TSLA_evening.json