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
🟡 **近现价集中开仓**: 11-13 395C ΔOI +2,183（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 386.58 → 收盘 390.84（+1.1%） ｜ 今日高 395.43 ｜ 低 386.35 ｜ 昨收 379.78 → 收盘 390.84（+2.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.58 | OI比 1.20 | ATM IV 28.9% | Skew 2.6pp | Term 1.46 | ExpMove ±0.0%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常偏陡（Term 1.46）｜保护溢价中性（Skew 2.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.20×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±0.0% ｜ 11-16（5D）±3.6% ｜ 11-18（7D）±4.8% ｜ 11-20（9D）±0.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 99,020,467 | GEX Change vs 上次快照 -26,953,421 | Flip: Primary Flip: 365.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 1250 / LOW 240 / INVALID 1172
结构观察区: Primary Flip 365.16（全链重定价，覆盖 90%）
Call Wall 400（现价低于该位 2.3%）
最近结构参考: Call Wall 400（现价低于该位 2.3%）
量化视角： 正 Gamma（9902万，无历史分位）｜正 Gamma 减弱（2695万）｜现价位于 Flip 上方 7.03%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 375（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 365（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +9.1k / P +9.9k ｜ Activity HIGH ｜ 2D
11-16  C +2.1k / P +2.8k ｜ Activity HIGH ｜ 5D
11-18  C +1.7k / P +2.1k ｜ Activity HIGH ｜ 7D
11-20  C +1.1k / P +11.3k ｜ Activity MEDIUM △ ｜ 9D

📆 11-13 Forward Structure
存量OI: C 162.0k / P 233.1k，今日变化ΔOI: C +9.1k / P +9.9k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 0.0%，净 delta 敞口 378k shares
Top ΔOI: C 395 +2,183 ｜ C 400 +1,890
仓位参考: Max Pain 360 ｜ Call Wall 400（+2.3%）（OI 13.6k）
量化解读： 存量 Put 重｜净 delta 敞口 正 378,089 股

📆 11-16 Forward Structure
存量OI: C 23.3k / P 13.1k，今日变化ΔOI: C +2.1k / P +2.8k，平值价格ATM: C $7.52 / P $6.50 ｜ ATM IV 38.7%，净 delta 敞口 29k shares
Top ΔOI: C 400 +495 ｜ C 415 +323
仓位参考: Max Pain 375 ｜ Call Wall 400（+2.3%，弱）（OI 1.6k） ｜ Put Wall 380（-2.8%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.7%｜历史 Rank 3%（近端代理）｜IV/RV 0.68×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 28,534 股

📆 11-18 Forward Structure
存量OI: C 7.5k / P 7.2k，今日变化ΔOI: C +1.7k / P +2.1k，平值价格ATM: C $9.25 / P $9.60 ｜ ATM IV 42.7%，净 delta 敞口 50k shares
Top ΔOI: C 410 +317 ｜ C 390 +225
仓位参考: Max Pain 370 ｜ Call Wall 410（+4.9%，弱）（OI 0.6k） ｜ Put Wall 355（-9.2%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.7%｜历史 Rank 3%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 正 50,465 股

11-20（MEDIUM △）Top ΔOI: 372P +5,918
11-20（MEDIUM △）仓位参考: Max Pain 375 ｜ Call Wall 400（+2.3%，弱）（OI 21.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/TSLA_evening.json