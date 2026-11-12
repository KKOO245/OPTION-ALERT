# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 17.49 ↓10.1%（5D +5.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-12 287C ΔOI +24,261（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-12 287C ΔOI +24,261 占该期限总 OI 36.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 282.99 → 收盘 283.09（+0.0%） ｜ 今日高 283.72 ｜ 低 281.48 ｜ 昨收 280.58 → 收盘 283.09（+0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.78 | OI比 0.48 | ATM IV 10.2% | Skew -9.3pp | Term 1.73 | ExpMove ±0.7%（近端） | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 1.73）｜Put 保护异常便宜（Skew -9.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-12（1D）±0.7% ｜ 11-13（2D）±1.0% ｜ 11-16（5D）±1.3% ｜ 11-17（6D）±1.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -54,225,606 | GEX Change vs 上次快照 108,601,034 | Flip: Primary Flip: 283.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1430 / LOW 237 / INVALID 1059
结构观察区: Primary Flip 283.46（全链重定价，覆盖 97%）
Put Wall 270（弱结构｜现价高于该位 4.8%） | Call Wall 290（弱结构｜现价低于该位 2.4%）
最近结构参考: Flip 283（现价低于该位 0.1%）
量化视角： 负 Gamma（5423万，无历史分位）｜负 Gamma 缓解（+1.09亿）｜现价位于 Flip 下方 0.13%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 280（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 283（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-12  C +26.2k / P +2.3k ｜ Activity HIGH ｜ 1D
11-13  C +6.2k / P +5.9k ｜ Activity HIGH ｜ 2D
11-16  C +5.4k / P +3.9k ｜ Activity HIGH ｜ 5D
11-17  C +1.7k / P +2.5k ｜ Activity HIGH ｜ 6D

📆 11-12 Forward Structure
存量OI: C 48.8k / P 17.8k，今日变化ΔOI: C +26.2k / P +2.3k，平值价格ATM: C $1.07 / P $0.98 ｜ ATM IV 17.4%，净 delta 敞口 241k shares
Top ΔOI: C 287 +24,261 ｜ C 277 +491 ｜ P 274 +434
仓位参考: Max Pain 278 ｜ Call Wall 287（+1.4%）（OI 25.4k） ｜ Put Wall 265（-6.4%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 17.4%｜历史 Rank 0%（近端代理）｜IV/RV 0.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 241,195 股

📆 11-13 Forward Structure
存量OI: C 111.7k / P 183.2k，今日变化ΔOI: C +6.2k / P +5.9k，平值价格ATM: C $1.59 / P $1.36 ｜ ATM IV 17.5%，净 delta 敞口 160k shares
Top ΔOI: P 278 +2,187 ｜ C 285 +1,635 ｜ P 280 +923
仓位参考: Max Pain 279 ｜ Call Wall 302（+6.7%，弱）（OI 13.7k） ｜ Put Wall 272（-3.9%，弱）（OI 13.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 17.5%｜历史 Rank 0%（近端代理）｜IV/RV 0.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 160,371 股

📆 11-16 Forward Structure
存量OI: C 13.7k / P 18.9k，今日变化ΔOI: C +5.4k / P +3.9k，平值价格ATM: C $2.00 / P $1.78 ｜ ATM IV 14.2%，净 delta 敞口 215k shares
Top ΔOI: C 285 +1,666 ｜ C 282 +1,446 ｜ P 277 +892
仓位参考: Max Pain 279 ｜ Call Wall 285（+0.7%，弱）（OI 2.3k） ｜ Put Wall 270（-4.6%）（OI 3.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 14.2%｜历史 Rank 0%（近端代理）｜IV/RV 0.59×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 215,307 股

📆 11-17 Forward Structure
存量OI: C 6.4k / P 10.4k，今日变化ΔOI: C +1.7k / P +2.5k，平值价格ATM: C $2.24 / P $2.08 ｜ ATM IV 15.2%，净 delta 敞口 45k shares
Top ΔOI: P 275 +398 ｜ P 276 +392 ｜ P 277 +358
仓位参考: Max Pain 278 ｜ Call Wall 289（+2.1%，弱）（OI 0.6k） ｜ Put Wall 260（-8.2%）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 15.2%｜历史 Rank 0%（近端代理）｜IV/RV 0.63×（近似）｜净 delta 敞口 正 45,350 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/IWM_evening.json