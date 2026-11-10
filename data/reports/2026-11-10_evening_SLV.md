# 期权晚报 2026-11-10（快照 16:40 ET）

📊 市场环境

SPY $749.92 ｜ QQQ $674.76
VIX 19.46 ↓2.3%（5D -6.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-16 48C ΔOI +357（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-16 50C ΔOI +1,788 占该期限总 OI 16.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 46.85 → 收盘 46.48（-0.8%） ｜ 今日高 46.99 ｜ 低 46.15 ｜ 昨收 48.14 → 收盘 46.48（-3.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.72 | OI比 0.65 | ATM IV 47.1% | Skew 4.5pp | Term 0.87 | ExpMove ±1.9%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 4.5pp）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-11（1D）±1.9% ｜ 11-13（3D）±3.5% ｜ 11-16（6D）±4.1% ｜ 11-18（8D）±4.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 24,522,971 | GEX Change vs 上次快照 -11,686,229 | Flip: Primary Flip: 45.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 744 / LOW 135 / INVALID 381
结构观察区: Primary Flip 45.70（全链重定价，覆盖 98%）
最近结构参考: Flip 46（现价高于该位 1.7%）
量化视角： 正 Gamma（2452万，无历史分位）｜正 Gamma 减弱（1169万）｜现价位于 Flip 上方 1.70%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 46（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 46（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-11  C +12.9k / P +6.3k ｜ Activity HIGH ｜ 1D
11-13  C +6.8k / P +2.6k ｜ Activity HIGH ｜ 3D
11-16  C +4.6k / P +1.2k ｜ Activity HIGH ｜ 6D
11-18  C +0.5k / P +2.4k ｜ Activity HIGH ｜ 8D

📆 11-11 Forward Structure
存量OI: C 31.4k / P 20.4k，今日变化ΔOI: C +12.9k / P +6.3k，平值价格ATM: C $0.45 / P $0.45 ｜ ATM IV 47.1%，净 delta 敞口 -34k shares
Top ΔOI: C 49 +2,349 ｜ C 50 +1,850
仓位参考: Max Pain 46 ｜ Call Wall 51（+9.7%，弱）（OI 4.4k） ｜ Put Wall 44（-5.3%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 47.1%｜历史 Rank 78%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 33,877 股

📆 11-13 Forward Structure
存量OI: C 69.3k / P 35.5k，今日变化ΔOI: C +6.8k / P +2.6k，平值价格ATM: C $0.82 / P $0.79 ｜ ATM IV 47.7%，净 delta 敞口 18k shares
Top ΔOI: C 50 +1,222 ｜ C 49 +803 ｜ C 49 +675
仓位参考: Max Pain 48 ｜ Call Wall 50（+7.6%）（OI 8.7k） ｜ Put Wall 45（-3.2%，弱）（OI 3.2k）
量化解读： 存量 Call 重｜ATM IV 47.7%｜历史 Rank 78%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 17,671 股

📆 11-16 Forward Structure
存量OI: C 8.1k / P 2.8k，今日变化ΔOI: C +4.6k / P +1.2k，平值价格ATM: C $0.97 / P $0.93 ｜ ATM IV 39.9%，净 delta 敞口 -4k shares
Top ΔOI: C 50 +1,788 ｜ C 48 +357
仓位参考: Max Pain 47 ｜ Call Wall 50（+7.6%，弱）（OI 2.0k） ｜ Put Wall 46.5（+0.0%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 39.9%｜历史 Rank 78%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 4,176 股

📆 11-18 Forward Structure
存量OI: C 2.2k / P 3.4k，今日变化ΔOI: C +0.5k / P +2.4k，平值价格ATM: C $1.17 / P $1.11 ｜ ATM IV 41.9%，净 delta 敞口 -42k shares
Top ΔOI: P 44 +2,145 ｜ C 49 +98 ｜ C 47 +70
仓位参考: Max Pain 45 ｜ Call Wall 50（+7.6%）（OI 0.5k） ｜ Put Wall 44.5（-4.3%）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 41.9%｜历史 Rank 78%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 41,720 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/SLV_evening.json