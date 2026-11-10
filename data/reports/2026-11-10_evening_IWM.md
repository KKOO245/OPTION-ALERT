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
🟡 **近现价集中开仓**: 11-11 290C ΔOI +17,351（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-11 290C ΔOI +17,351 占该期限总 OI 16.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 279.79 → 收盘 280.58（+0.3%） ｜ 今日高 281.33 ｜ 低 277.91 ｜ 昨收 282.51 → 收盘 280.58（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.53 | OI比 1.00 | ATM IV 17.5% | Skew -12.5pp | Term 1.11 | ExpMove ±0.8%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构正常（Term 1.11）｜Put 保护异常便宜（Skew -12.5pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.53×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-11（1D）±0.8% ｜ 11-12（2D）±1.2% ｜ 11-13（3D）±1.5% ｜ 11-16（6D）±1.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -463,284,455 | GEX Change vs 上次快照 -24,517,963 | Flip: Primary Flip: 283.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1453 / LOW 222 / INVALID 993
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 283.91（全链重定价，覆盖 98%）
Put Wall 270（弱结构｜现价高于该位 3.9%） | Call Wall 290（弱结构｜现价低于该位 3.2%）
最近结构参考: Flip 284（现价低于该位 1.2%）
量化视角： 负 Gamma（4.63亿，无历史分位）｜负 Gamma 加深（2452万）｜现价位于 Flip 下方 1.17%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 280（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 284（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-11  C +61.0k / P +7.2k ｜ Activity HIGH ｜ 1D
11-12  C +3.5k / P +4.1k ｜ Activity HIGH ｜ 2D
11-13  C +12.8k / P +13.7k ｜ Activity HIGH ｜ 3D
11-16  C +3.5k / P +2.8k ｜ Activity HIGH ｜ 6D

📆 11-11 Forward Structure
存量OI: C 74.9k / P 31.8k，今日变化ΔOI: C +61.0k / P +7.2k，平值价格ATM: C $0.98 / P $1.32 ｜ ATM IV 19.1%，净 delta 敞口 -17k shares
Top ΔOI: C 290 +17,351 ｜ C 289 +13,207 ｜ C 287 +7,613
仓位参考: Max Pain 280 ｜ Call Wall 290（+3.4%，弱）（OI 18.0k） ｜ Put Wall 280（-0.2%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜ATM IV 19.1%｜历史 Rank 18%（近端代理）｜IV/RV 0.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 16,568 股

📆 11-12 Forward Structure
存量OI: C 22.6k / P 15.4k，今日变化ΔOI: C +3.5k / P +4.1k，平值价格ATM: C $1.51 / P $1.76 ｜ ATM IV 19.4%，净 delta 敞口 -11k shares
Top ΔOI: C 290 +1,576 ｜ P 265 +1,247 ｜ P 263 +782
仓位参考: Max Pain 278 ｜ Call Wall 285（+1.6%）（OI 4.6k） ｜ Put Wall 265（-5.6%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 19.4%｜历史 Rank 18%（近端代理）｜IV/RV 0.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 10,877 股

📆 11-13 Forward Structure
存量OI: C 105.5k / P 177.4k，今日变化ΔOI: C +12.8k / P +13.7k，平值价格ATM: C $1.98 / P $2.14 ｜ ATM IV 19.9%，净 delta 敞口 -385k shares
Top ΔOI: P 277 +9,406 ｜ P 268 +4,181 ｜ P 265 -4,061
仓位参考: Max Pain 278 ｜ Call Wall 302（+7.6%，弱）（OI 13.7k） ｜ Put Wall 272（-3.1%，弱）（OI 12.7k）
量化解读： 存量 Put 重｜ATM IV 19.9%｜历史 Rank 18%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 385,312 股

📆 11-16 Forward Structure
存量OI: C 8.3k / P 15.1k，今日变化ΔOI: C +3.5k / P +2.8k，平值价格ATM: C $2.37 / P $2.40 ｜ ATM IV 16.8%，净 delta 敞口 -26k shares
Top ΔOI: C 287 +1,022 ｜ P 265 -757 ｜ P 279 +480
仓位参考: Max Pain 280 ｜ Call Wall 287（+2.3%，弱）（OI 1.3k） ｜ Put Wall 270（-3.8%）（OI 3.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.8%｜历史 Rank 18%（近端代理）｜IV/RV 0.70×（近似）｜净 delta 敞口 负 26,416 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/IWM_evening.json