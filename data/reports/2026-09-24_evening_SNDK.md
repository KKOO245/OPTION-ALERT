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
🟡 **近现价集中开仓**: 10-09 1800C ΔOI +132（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,785.47 → 收盘 1,753.62（-1.8%） ｜ 今日高 1802.99 ｜ 低 1726.39 ｜ 昨收 1,816.57 → 收盘 1,753.62（-3.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.59 | OI比 1.12 | ATM IV 70.4% | Skew -4.5pp | Term 1.00 | ExpMove ±3.0%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -4.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（1D）±3.0% ｜ 10-02（8D）±8.6% ｜ 10-09（15D）±11.6% ｜ 10-16（22D）±13.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 339,083 | GEX Change vs 上次快照 -14,109,582 | Flip: Primary Flip: 1751.24（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1999 / LOW 482 / INVALID 959
结构观察区: Primary Flip 1751.24（全链重定价，覆盖 98%）
最近结构参考: Flip 1751（现价高于该位 0.1%）
量化视角： 正 Gamma（34万，无历史分位）｜正 Gamma 减弱（1411万）｜现价位于 Flip 上方 0.14%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,760（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1751（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +16.4k / P +13.7k ｜ Activity HIGH ｜ 1D（新行权价 C 0.1k）
10-02  C +4.2k / P +5.2k ｜ Activity HIGH ｜ 8D（新行权价 C 0.2k）
10-09  C +1.5k / P +1.4k ｜ Activity HIGH ｜ 15D（新行权价 C 43）
10-16  C +2.6k / P +2.2k ｜ Activity HIGH ｜ 22D（新行权价 C 1）

📆 09-25 Forward Structure
存量OI: C 55.9k / P 62.7k，今日变化ΔOI: C +16.4k / P +13.7k（新行权价 C 0.1k），平值价格ATM: C $25.40 / P $26.50 ｜ ATM IV 70.4%，净 delta 敞口 -699k shares
Top ΔOI: P 1850 +1,193 ｜ C 1900 +933
仓位参考: Max Pain 1,760 ｜ Call Wall 1900（+8.3%，弱）（OI 2.7k） ｜ Put Wall 1700（-3.1%，弱）（OI 2.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 70.4%｜历史 Rank 24%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 699,037 股

📆 10-02 Forward Structure
存量OI: C 24.1k / P 20.0k，今日变化ΔOI: C +4.2k / P +5.2k（新行权价 C 0.2k），平值价格ATM: C $76.00 / P $74.48 ｜ ATM IV 73.1%，净 delta 敞口 -104k shares
Top ΔOI: C 2250 -1,130 ｜ C 2000 +672
仓位参考: Max Pain 1,625 ｜ Call Wall 1600（-8.8%）（OI 4.3k） ｜ Put Wall 1600（-8.8%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.1%｜历史 Rank 24%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 104,208 股

📆 10-09 Forward Structure
存量OI: C 8.2k / P 7.2k，今日变化ΔOI: C +1.5k / P +1.4k（新行权价 C 43），平值价格ATM: C $101.40 / P $101.20 ｜ ATM IV 70.0%，净 delta 敞口 -5k shares
Top ΔOI: C 1800 +132 ｜ C 1900 +118 ｜ P 1800 +97
仓位参考: Max Pain 1,550 ｜ Put Wall 1600（-8.8%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 70.0%｜历史 Rank 24%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 负 4,926 股

📆 10-16 Forward Structure
存量OI: C 35.1k / P 43.7k，今日变化ΔOI: C +2.6k / P +2.2k（新行权价 C 1），平值价格ATM: C $123.00 / P $118.25 ｜ ATM IV 70.2%，净 delta 敞口 -8k shares
Top ΔOI: C 2550 +388 ｜ C 1820 +251
仓位参考: Max Pain 1,630 ｜ Call Wall 1800（+2.6%，弱）（OI 1.1k） ｜ Put Wall 1600（-8.8%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 70.2%｜历史 Rank 24%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 负 7,617 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/SNDK_evening.json