# 期权晚报 2026-11-04（快照 16:40 ET）

📊 市场环境

SPY $766.81 ｜ QQQ $691.95
VIX 16.61 ↓20.3%（5D -1.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **事件差分**: 11-06 ATM IV 82.1% vs 11-13 68.3%（差 +13.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 141.98 → 收盘 151.50（+6.7%） ｜ 今日高 153.33 ｜ 低 141.88 ｜ 昨收 145.45 → 收盘 151.50（+4.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.70 | OI比 0.75 | ATM IV 82.1% | Skew 1.8pp | Term 0.78 | ExpMove ±5.0%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±5.0% ｜ 11-13（9D）±8.7% ｜ 11-20（16D）±11.0% ｜ 11-27（23D）±13.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,350,533 | GEX Change vs 上次快照 -532,550 | Flip: Primary Flip: 134.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 441 / LOW 152 / INVALID 257
结构观察区: Primary Flip 134.72（全链重定价，覆盖 100%）
最近结构参考: Flip 135（现价高于该位 12.5%）
量化视角： 正 Gamma（2335万，无历史分位）｜正 Gamma 减弱（53万）｜现价位于 Flip 上方 12.45%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 135（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +4.8k / P +5.5k ｜ Activity HIGH ｜ 2D
11-13  C +1.8k / P +1.1k ｜ Activity HIGH ｜ 9D
11-20  C +0.5k / P +4.4k ｜ Activity HIGH ｜ 16D
11-27  C +5 / P +0.2k ｜ Activity LOW ｜ 23D

📆 11-06 Forward Structure
存量OI: C 72.7k / P 54.2k，今日变化ΔOI: C +4.8k / P +5.5k，平值价格ATM: C $3.22 / P $4.30 ｜ ATM IV 82.1%，净 delta 敞口 78k shares
Top ΔOI: C 160 +819
仓位参考: Max Pain 141 ｜ Call Wall 148（-2.3%，弱）（OI 8.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 82.1%｜历史 Rank 66%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 77,589 股

📆 11-13 Forward Structure
存量OI: C 13.3k / P 19.4k，今日变化ΔOI: C +1.8k / P +1.1k，平值价格ATM: C $6.17 / P $7.05 ｜ ATM IV 68.3%，净 delta 敞口 55k shares
Top ΔOI: C 170 +448 ｜ C 145 +199
仓位参考: Max Pain 155 ｜ Call Wall 150（-1.0%，弱）（OI 0.6k） ｜ Put Wall 155（+2.3%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 68.3%｜历史 Rank 66%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 55,371 股

📆 11-20 Forward Structure
存量OI: C 73.1k / P 57.3k，今日变化ΔOI: C +0.5k / P +4.4k，平值价格ATM: C $9.25 / P $7.45 ｜ ATM IV 68.8%，净 delta 敞口 26k shares
Top ΔOI: P 120 +1,836
仓位参考: Max Pain 170 ｜ Put Wall 140（-7.6%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 68.8%｜历史 Rank 66%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,220 股

11-27（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 155（+2.3%，弱）（OI 0.2k） ｜ Put Wall 140（-7.6%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 82.1% vs 11-13 68.3%（差 +13.8pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/COIN_evening.json