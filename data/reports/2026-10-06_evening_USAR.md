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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-09 14C ΔOI +928（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 13.81 → 收盘 13.74（-0.5%） ｜ 今日高 14.06 ｜ 低 13.73 ｜ 昨收 13.65 → 收盘 13.74（+0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.19 | OI比 0.42 | ATM IV 63.4% | Skew -7.9pp | Term 1.08 | ExpMove ±5.0%（近端） | Rank 1%
量化视角： IV 历史低位（Rank 1%，期权偏便宜）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -7.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±5.0% ｜ 10-16（10D）±8.5% ｜ 10-23（17D）±10.5% ｜ 10-30（24D）±13.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 117,033 | GEX Change vs 上次快照 -75,533 | Flip: Primary Flip: 13.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 180 / LOW 68 / INVALID 142
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 13.71（全链重定价，覆盖 98%）
Put Wall 15（弱结构｜现价低于该位 8.4%）
最近结构参考: Flip 14（现价高于该位 0.2%）
量化视角： 正 Gamma（12万，无历史分位）｜正 Gamma 减弱（8万）｜现价位于 Flip 上方 0.21%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（Put Wall，弱结构） / 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +3.8k / P +0.2k ｜ Activity HIGH ｜ 3D
10-16  C +1.1k / P -0.6k ｜ Activity HIGH ｜ 10D
10-23  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 17D
10-30  C +1.1k / P +0.7k ｜ Activity HIGH ｜ 24D

📆 10-09 Forward Structure
存量OI: C 17.8k / P 7.5k，今日变化ΔOI: C +3.8k / P +0.2k，平值价格ATM: C $0.48 / P $0.20 ｜ ATM IV 63.4%，净 delta 敞口 158k shares
Top ΔOI: C 14 +1,234 ｜ C 14 +928 ｜ P 13 +700
仓位参考: Max Pain 14 ｜ Call Wall 14.5（+5.5%，弱）（OI 2.8k） ｜ Put Wall 13（-5.4%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 63.4%｜历史 Rank 1%（近端代理）｜IV/RV 1.25×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 158,142 股

📆 10-16 Forward Structure
存量OI: C 48.7k / P 16.2k，今日变化ΔOI: C +1.1k / P -0.6k，平值价格ATM: C $0.74 / P $0.43 ｜ ATM IV 63.9%，净 delta 敞口 96k shares
Top ΔOI: C 15 +497 ｜ P 15 -338 ｜ C 14 +250
仓位参考: Max Pain 16 ｜ Put Wall 15（+9.2%）（OI 5.6k）
量化解读： 存量 Call 重｜ATM IV 63.9%｜历史 Rank 1%（近端代理）｜IV/RV 1.27×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 95,637 股

📆 10-23 Forward Structure
存量OI: C 10.5k / P 5.4k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $0.90 / P $0.54 ｜ ATM IV 62.5%，净 delta 敞口 -2k shares
Top ΔOI: P 15 +567 ｜ P 16 -205 ｜ C 13 +196
仓位参考: Max Pain 16 ｜ Put Wall 14（+1.9%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 62.5%｜历史 Rank 1%（近端代理）｜IV/RV 1.24×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 2,131 股

📆 10-30 Forward Structure
存量OI: C 5.6k / P 7.2k，今日变化ΔOI: C +1.1k / P +0.7k，平值价格ATM: C $1.16 / P $0.73 ｜ ATM IV 68.6%，净 delta 敞口 -15k shares
Top ΔOI: P 16 +440 ｜ P 17 -192
仓位参考: Max Pain 16 ｜ Call Wall 15（+9.2%，弱）（OI 0.3k） ｜ Put Wall 14（+1.9%）（OI 2.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 68.6%｜历史 Rank 1%（近端代理）｜IV/RV 1.36×（近似）｜净 delta 敞口 负 15,491 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/USAR_evening.json