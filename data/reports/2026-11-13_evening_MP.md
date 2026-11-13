# 期权晚报 2026-11-13（快照 16:40 ET）

📊 市场环境

SPY $754.37 ｜ QQQ $679.89
VIX 19.30 ↑3.2%（5D -24.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 40C ΔOI +278（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 33P ΔOI +2,498 占该期限总 OI 22.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 37.34 → 收盘 38.76（+3.8%） ｜ 今日高 39.75 ｜ 低 37.21 ｜ 昨收 37.45 → 收盘 38.76（+3.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-20，窗口结束前不做对错判定）

Options: P/C成交量 0.26 | OI比 0.31 | ATM IV 106.9% | Skew -6.8pp | Term 0.62 | ExpMove ±7.4%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±7.4% ｜ 11-27（14D）±14.4% ｜ 12-04（21D）±18.9% ｜ 12-11（28D）±14.9%
   ⇒ IV–VIX Spread: +87.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,562,036 | GEX Change vs 上次快照 -1,582,612 | Flip: Primary Flip: 35.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 240 / LOW 70 / INVALID 182
结构观察区: Primary Flip 35.68（全链重定价，覆盖 87%）
Put Wall 35（现价高于该位 10.7%）
最近结构参考: Flip 36（现价高于该位 8.6%）
量化视角： 正 Gamma（556万，无历史分位）｜正 Gamma 减弱（158万）｜现价位于 Flip 上方 8.64%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall） / 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 36（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +0.6k / P +0.3k ｜ Activity MEDIUM △ ｜ 7D
11-27  C +1.6k / P +2.7k ｜ Activity HIGH ｜ 14D
12-04  C +73 / P +6 ｜ Activity MEDIUM △ ｜ 21D
12-11  C +0.2k / P +47 ｜ Activity HIGH ｜ 28D

📆 11-20 Forward Structure
存量OI: C 26.2k / P 13.5k，今日变化ΔOI: C +0.6k / P +0.3k，平值价格ATM: C $1.34 / P $1.54 ｜ ATM IV 66.4%，净 delta 敞口 37k shares
Top ΔOI: C 40 +278 ｜ C 42 +277
仓位参考: Max Pain 40 ｜ Call Wall 39.5（+1.9%，弱）（OI 2.0k） ｜ Put Wall 35（-9.7%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 66.4%｜历史 Rank 94%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 37,135 股

📆 11-27 Forward Structure
存量OI: C 6.7k / P 4.3k，今日变化ΔOI: C +1.6k / P +2.7k，平值价格ATM: C $1.77 / P $3.80 ｜ ATM IV 60.5%，净 delta 敞口 -13k shares
Top ΔOI: P 33 +2,498
仓位参考: Max Pain 42
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 60.5%｜历史 Rank 94%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 12,982 股

12-04（MEDIUM △）Top ΔOI: 40C +13
12-04（MEDIUM △）仓位参考: Max Pain 35 ｜ Call Wall 35（-9.7%）（OI 0.5k） ｜ Put Wall 35（-9.7%，弱）（OI 0.1k）

📆 12-11 Forward Structure
存量OI: C 0.6k / P 0.7k，今日变化ΔOI: C +0.2k / P +47，平值价格ATM: C $2.80 / P $2.97 ｜ ATM IV 66.3%，净 delta 敞口 5k shares
Top ΔOI: C 37 +44 ｜ C 39 +23
仓位参考: Max Pain 42 ｜ Call Wall 37（-4.5%，弱）（OI 71） ｜ Put Wall 42（+8.4%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.3%｜历史 Rank 94%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 正 5,222 股

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 66.4% vs 11-27 60.5%（差 +5.9pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/MP_evening.json