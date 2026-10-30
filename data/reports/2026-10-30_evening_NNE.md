# 期权晚报 2026-10-30（快照 16:40 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 19.42 ↑12.9%（5D -0.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 11.49 → 收盘 11.65（+1.4%） ｜ 今日高 11.66 ｜ 低 11.13 ｜ 昨收 12.21 → 收盘 11.65（-4.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-06，窗口结束前不做对错判定）

Options: P/C成交量 0.79 | OI比 0.14 | ATM IV 142.2% | Skew -12.6pp | Term 0.53 | ExpMove ±8.6%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜Put 保护异常便宜（Skew -12.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.14）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.14×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±8.6% ｜ 11-13（14D）±15.6% ｜ 11-20（21D）±4.0% ｜ 11-27（28D）±5.6%
   ⇒ IV–VIX Spread: +122.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 82,162 | GEX Change vs 上次快照 71,837 | Flip: Primary Flip: 11.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 139 / LOW 78 / INVALID 191
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 11.31（全链重定价，覆盖 83%）
Put Wall 12（弱结构｜现价低于该位 2.9%）
最近结构参考: Put Wall 12（现价低于该位 2.9%）
量化视角： 正 Gamma（8万，无历史分位）｜正 Gamma 增强（+7万）｜现价位于 Flip 上方 3.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 12（Put Wall，弱结构） / 13（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0.4k / P -69 ｜ Activity MEDIUM △ ｜ 7D
11-13  C +26 / P -3 ｜ Activity MEDIUM △ ｜ 14D
11-20  C +29 / P -2 ｜ Activity MEDIUM △ ｜ 21D
11-27  C +12 / P +0 ｜ Activity LOW ｜ 28D

📆 11-06 Forward Structure
存量OI: C 2.3k / P 1.4k，今日变化ΔOI: C +0.4k / P -69，平值价格ATM: C $0.55 / P $0.45 ｜ ATM IV 77.0%，净 delta 敞口 8k shares
Top ΔOI: P 11 -76
仓位参考: Max Pain 14 ｜ Put Wall 11.5（-1.3%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 77.0%｜历史 Rank 84%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,648 股

11-13（MEDIUM △）仓位参考: Max Pain 14 ｜ Put Wall 12.5（+7.3%，弱）（OI 67）

11-20（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 12（+3.0%，弱）（OI 0.3k）

11-27（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 12.5（+7.3%）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/NNE_evening.json