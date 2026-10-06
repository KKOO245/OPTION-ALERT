# 期权晚报 2026-10-06（快照 16:40 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 242C ΔOI -2,746（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 290C ΔOI +2,913 占该期限总 OI 10.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 237.22 → 收盘 249.87（+5.3%） ｜ 今日高 255.08 ｜ 低 237.00 ｜ 昨收 232.57 → 收盘 249.87（+7.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.61 | OI比 0.94 | ATM IV 78.8% | Skew -3.2pp | Term 0.94 | ExpMove ±5.7%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -3.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（3D）±5.7% ｜ 10-16（10D）±9.8% ｜ 10-23（17D）±12.4% ｜ 10-30（24D）±14.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,569,093 | GEX Change vs 上次快照 2,419,081 | Flip: Primary Flip: 229.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 522 / LOW 29 / INVALID 101
结构观察区: Primary Flip 229.91（全链重定价，覆盖 100%）
最近结构参考: Flip 230（现价高于该位 8.7%）
量化视角： 正 Gamma（1957万，无历史分位）｜正 Gamma 增强（+242万）｜现价位于 Flip 上方 8.68%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 232（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 230（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +5.0k / P +15.0k ｜ Activity HIGH ｜ 3D
10-16  C +10.5k / P +4.7k ｜ Activity HIGH ｜ 10D
10-23  C +2.9k / P +0.9k ｜ Activity HIGH ｜ 17D
10-30  C +4.2k / P +2.8k ｜ Activity HIGH ｜ 24D

📆 10-09 Forward Structure
存量OI: C 47.0k / P 44.0k，今日变化ΔOI: C +5.0k / P +15.0k，平值价格ATM: C $7.11 / P $7.05 ｜ ATM IV 78.8%，净 delta 敞口 91k shares
Top ΔOI: P 220 +3,140 ｜ C 242 -2,746 ｜ P 215 +2,313
仓位参考: Max Pain 232 ｜ Call Wall 242.5（-2.9%，弱）（OI 4.4k） ｜ Put Wall 225（-10.0%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.8%｜历史 Rank 10%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 90,871 股

📆 10-16 Forward Structure
存量OI: C 82.9k / P 95.8k，今日变化ΔOI: C +10.5k / P +4.7k，平值价格ATM: C $12.30 / P $12.20 ｜ ATM IV 73.7%，净 delta 敞口 404k shares
Top ΔOI: C 245 +3,477 ｜ C 310 +3,470 ｜ C 210 +1,473
仓位参考: Max Pain 220 ｜ Call Wall 270（+8.1%，弱）（OI 6.2k） ｜ Put Wall 225（-10.0%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 73.7%｜历史 Rank 10%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 403,866 股

📆 10-23 Forward Structure
存量OI: C 11.5k / P 10.4k，今日变化ΔOI: C +2.9k / P +0.9k，平值价格ATM: C $15.69 / P $15.26 ｜ ATM IV 71.6%，净 delta 敞口 127k shares
Top ΔOI: C 237 +883 ｜ C 320 +365
仓位参考: Max Pain 225 ｜ Call Wall 237.5（-5.0%，弱）（OI 0.9k） ｜ Put Wall 225（-10.0%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 71.6%｜历史 Rank 10%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 正 127,264 股

📆 10-30 Forward Structure
存量OI: C 15.4k / P 13.1k，今日变化ΔOI: C +4.2k / P +2.8k，平值价格ATM: C $19.00 / P $18.00 ｜ ATM IV 72.1%，净 delta 敞口 82k shares
Top ΔOI: C 290 +2,913 ｜ P 200 +811 ｜ P 220 +477
仓位参考: Max Pain 230 ｜ Put Wall 240（-4.0%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 72.1%｜历史 Rank 10%（近端代理）｜IV/RV 1.38×（近似）｜净 delta 敞口 正 81,638 股

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 78.8% vs 10-16 73.7%（差 +5.1pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/NBIS_evening.json