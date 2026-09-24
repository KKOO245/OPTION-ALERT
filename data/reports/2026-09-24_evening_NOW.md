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
🟡 **近现价集中开仓**: 09-25 138C ΔOI +739（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 139.90 → 收盘 137.78（-1.5%） ｜ 今日高 141.04 ｜ 低 137.53 ｜ 昨收 140.78 → 收盘 137.78（-2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.57 | OI比 0.64 | ATM IV 55.1% | Skew -1.4pp | Term 1.00 | ExpMove ±2.4%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±2.4% ｜ 10-02（8D）±6.0% ｜ 10-09（15D）±8.3% ｜ 10-16（22D）±10.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,316,382 | GEX Change vs 上次快照 5,639,896 | Flip: Primary Flip: 133.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 602 / LOW 54 / INVALID 70
结构观察区: Primary Flip 133.49（全链重定价，覆盖 99%）
Call Wall 150（现价低于该位 8.1%）
最近结构参考: Flip 133（现价高于该位 3.2%）
量化视角： 正 Gamma（1432万，无历史分位）｜正 Gamma 增强（+564万）｜现价位于 Flip 上方 3.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 136（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +4.2k / P +3.1k ｜ Activity HIGH ｜ 1D
10-02  C +4.7k / P +4.2k ｜ Activity HIGH ｜ 8D
10-09  C +3.0k / P +1.1k ｜ Activity HIGH ｜ 15D
10-16  C +1.7k / P +1.9k ｜ Activity HIGH ｜ 22D

📆 09-25 Forward Structure
存量OI: C 34.2k / P 22.0k，今日变化ΔOI: C +4.2k / P +3.1k，平值价格ATM: C $1.59 / P $1.65 ｜ ATM IV 55.1%，净 delta 敞口 99k shares
Top ΔOI: C 138 +739 ｜ C 150 -645 ｜ C 130 +498
仓位参考: Max Pain 136 ｜ Call Wall 150（+8.9%，弱）（OI 5.4k） ｜ Put Wall 130（-5.6%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 55.1%｜历史 Rank 24%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 99,434 股

📆 10-02 Forward Structure
存量OI: C 17.7k / P 15.4k，今日变化ΔOI: C +4.7k / P +4.2k，平值价格ATM: C $4.31 / P $3.97 ｜ ATM IV 52.2%，净 delta 敞口 95k shares
Top ΔOI: C 146 +701 ｜ C 150 +648
仓位参考: Max Pain 134 ｜ Call Wall 150（+8.9%）（OI 3.0k） ｜ Put Wall 130（-5.6%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜ATM IV 52.2%｜历史 Rank 24%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 95,270 股

📆 10-09 Forward Structure
存量OI: C 8.1k / P 6.6k，今日变化ΔOI: C +3.0k / P +1.1k，平值价格ATM: C $5.85 / P $5.56 ｜ ATM IV 51.7%，净 delta 敞口 60k shares
Top ΔOI: C 150 +1,356
仓位参考: Max Pain 136 ｜ Call Wall 150（+8.9%）（OI 2.4k） ｜ Put Wall 140（+1.6%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 51.7%｜历史 Rank 24%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 60,232 股

📆 10-16 Forward Structure
存量OI: C 69.8k / P 56.7k，今日变化ΔOI: C +1.7k / P +1.9k，平值价格ATM: C $7.40 / P $6.76 ｜ ATM IV 51.5%，净 delta 敞口 -7k shares
Top ΔOI: C 150 +327
仓位参考: Max Pain 125 ｜ Call Wall 150（+8.9%）（OI 11.5k） ｜ Put Wall 130（-5.6%，弱）（OI 4.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 51.5%｜历史 Rank 24%（近端代理）｜净 delta 敞口 负 7,344 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/NOW_evening.json