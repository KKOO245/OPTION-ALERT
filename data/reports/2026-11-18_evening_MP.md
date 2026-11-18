# 期权晚报 2026-11-18（快照 16:40 ET）

📊 市场环境

SPY $730.20 ｜ QQQ $659.51
VIX 24.56 ↓3.5%（5D +40.4%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 87.5% vs 11-27 72.5%（差 +15.0pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 12-11 38C ΔOI +645 占该期限总 OI 21.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 34.77 → 收盘 35.95（+3.4%） ｜ 今日高 38.16 ｜ 低 34.69 ｜ 昨收 34.86 → 收盘 35.95（+3.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 0.30 | OI比 0.41 | ATM IV 87.5% | Skew -2.8pp | Term 0.77 | ExpMove ±5.1%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.30×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.41×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±5.1% ｜ 11-27（9D）±8.3% ｜ 12-04（16D）±10.9% ｜ 12-11（23D）±13.7%
   ⇒ IV–VIX Spread: +63.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,085,147 | GEX Change vs 上次快照 -2,908,763 | Flip: Primary Flip: 34.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 227 / LOW 75 / INVALID 136
结构观察区: Primary Flip 34.17（全链重定价，覆盖 98%）
Put Wall 35（现价高于该位 2.7%）
最近结构参考: Put Wall 35（现价高于该位 2.7%）
量化视角： 正 Gamma（409万，无历史分位）｜正 Gamma 减弱（291万）｜现价位于 Flip 上方 5.20%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 38（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 34（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +0.8k / P -1.6k ｜ Activity HIGH ｜ 2D
11-27  C +0.2k / P -87 ｜ Activity MEDIUM △ ｜ 9D
12-04  C +94 / P -10 ｜ Activity MEDIUM △ ｜ 16D
12-11  C +0.7k / P +0.1k ｜ Activity HIGH ｜ 23D

📆 11-20 Forward Structure
存量OI: C 30.4k / P 12.4k，今日变化ΔOI: C +0.8k / P -1.6k，平值价格ATM: C $0.94 / P $0.88 ｜ ATM IV 87.5%，净 delta 敞口 196k shares
Top ΔOI: P 44 -1,036 ｜ P 45 -445 ｜ C 36 +264
仓位参考: Max Pain 38 ｜ Call Wall 39.5（+9.9%，弱）（OI 1.8k） ｜ Put Wall 35（-2.6%）（OI 4.0k）
量化解读： 存量 Call 重｜ATM IV 87.5%｜历史 Rank 83%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 195,798 股

11-27（MEDIUM △）Top ΔOI: 42P -101
11-27（MEDIUM △）仓位参考: Max Pain 40 ｜ Put Wall 33（-8.2%）（OI 2.5k）

12-04（MEDIUM △）Top ΔOI: 54P -35 ｜ 39C +32
12-04（MEDIUM △）仓位参考: Max Pain 38 ｜ Call Wall 35（-2.6%）（OI 0.5k） ｜ Put Wall 34（-5.4%，弱）（OI 0.2k）

📆 12-11 Forward Structure
存量OI: C 2.1k / P 0.9k，今日变化ΔOI: C +0.7k / P +0.1k，平值价格ATM: C $2.69 / P $2.25 ｜ ATM IV 70.6%，净 delta 敞口 18k shares
Top ΔOI: C 38 +645 ｜ P 42 +99
仓位参考: Max Pain 38 ｜ Call Wall 38（+5.7%，弱）（OI 0.7k） ｜ Put Wall 34（-5.4%，弱）（OI 45）
量化解读： 存量 Call 重｜ATM IV 70.6%｜历史 Rank 83%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 18,339 股

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 87.5% vs 11-27 72.5%（差 +15.0pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/MP_evening.json