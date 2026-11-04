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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-05 290C ΔOI +13,353（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-05 290C ΔOI +13,353 占该期限总 OI 25.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 284.17 → 收盘 284.02（-0.1%） ｜ 今日高 286.17 ｜ 低 281.30 ｜ 昨收 279.79 → 收盘 284.02（+1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.13 | OI比 1.43 | ATM IV 14.7% | Skew 4.0pp | Term 1.18 | ExpMove ±0.8%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常偏陡（Term 1.18）｜保护溢价中性（Skew 4.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.13×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.43×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-05（1D）±0.8% ｜ 11-06（2D）±1.2% ｜ 11-09（5D）±1.5% ｜ 11-10（6D）±1.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -44,034,308 | GEX Change vs 上次快照 90,002,019 | Flip: Primary Flip: 284.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1232 / LOW 170 / INVALID 1064
结构观察区: Primary Flip 284.41（全链重定价，覆盖 96%）
Put Wall 270（弱结构｜现价高于该位 5.2%） | Call Wall 285（弱结构｜现价低于该位 0.3%）
最近结构参考: Flip 284（现价低于该位 0.1%）
量化视角： 负 Gamma（4403万，无历史分位）｜负 Gamma 缓解（+9000万）｜现价位于 Flip 下方 0.14%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 280（MaxPain，仅结算参考）；上方 285（Call Wall，弱结构）。
• Gamma 区域：切换参考 284（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-05  C +20.5k / P +1.7k ｜ Activity HIGH ｜ 1D
11-06  C +14.3k / P +21.6k ｜ Activity HIGH ｜ 2D
11-09  C +5.9k / P +6.1k ｜ Activity HIGH ｜ 5D
11-10  C +1.8k / P +3.8k ｜ Activity HIGH ｜ 6D

📆 11-05 Forward Structure
存量OI: C 31.2k / P 20.5k，今日变化ΔOI: C +20.5k / P +1.7k，平值价格ATM: C $1.27 / P $1.01 ｜ ATM IV 18.9%，净 delta 敞口 212k shares
Top ΔOI: C 290 +13,353 ｜ C 286 +5,208 ｜ P 282 +688
仓位参考: Max Pain 280 ｜ Call Wall 290（+2.1%）（OI 14.3k） ｜ Put Wall 282（-0.7%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 18.9%｜历史 Rank 3%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 211,645 股

📆 11-06 Forward Structure
存量OI: C 132.7k / P 296.2k，今日变化ΔOI: C +14.3k / P +21.6k，平值价格ATM: C $1.90 / P $1.54 ｜ ATM IV 20.3%，净 delta 敞口 138k shares
Top ΔOI: P 275 +5,128
仓位参考: Max Pain 280 ｜ Call Wall 285（+0.3%，弱）（OI 13.4k） ｜ Put Wall 277（-2.5%，弱）（OI 33.0k）
量化解读： 存量 Put 重｜ATM IV 20.3%｜历史 Rank 3%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 138,414 股

📆 11-09 Forward Structure
存量OI: C 18.9k / P 23.4k，今日变化ΔOI: C +5.9k / P +6.1k，平值价格ATM: C $2.20 / P $2.05 ｜ ATM IV 15.7%，净 delta 敞口 42k shares
Top ΔOI: P 265 +2,295 ｜ P 275 +1,452 ｜ C 292 +1,303
仓位参考: Max Pain 280 ｜ Call Wall 285（+0.3%）（OI 7.1k） ｜ Put Wall 275（-3.2%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜ATM IV 15.7%｜历史 Rank 3%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 42,163 股

📆 11-10 Forward Structure
存量OI: C 5.9k / P 10.2k，今日变化ΔOI: C +1.8k / P +3.8k，平值价格ATM: C $2.40 / P $2.47 ｜ ATM IV 17.0%，净 delta 敞口 10k shares
Top ΔOI: P 277 +555 ｜ P 265 +436 ｜ P 275 +434
仓位参考: Max Pain 281 ｜ Call Wall 287（+1.0%，弱）（OI 0.9k） ｜ Put Wall 280（-1.4%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 17.0%｜历史 Rank 3%（近端代理）｜净 delta 敞口 正 10,308 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/IWM_evening.json