# 期权晚报 2026-10-02（快照 16:40 ET）

📊 市场环境

SPY $769.64 ｜ QQQ $749.58
VIX 15.31 ↓6.6%（5D +3.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔵 **期限 OI 集中**: 10-30 20C ΔOI +4,917 占该期限总 OI 77.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 16.37 → 收盘 15.62（-4.6%） ｜ 今日高 16.40 ｜ 低 15.60 ｜ 昨收 15.73 → 收盘 15.62（-0.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-09，窗口结束前不做对错判定）

Options: P/C成交量 0.38 | OI比 0.32 | ATM IV 174.3% | Skew 10.6pp | Term 0.41 | ExpMove ±7.4%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.41，近月 IV 高于远月）｜保护溢价显著（Skew 10.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.32）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.32×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±7.4% ｜ 10-16（14D）±12.8% ｜ 10-23（21D）±13.6% ｜ 10-30（28D）±15.0%
   ⇒ IV–VIX Spread: +159.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,206,621 | GEX Change vs 上次快照 -273,401 | Flip: Primary Flip: 14.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 166 / LOW 93 / INVALID 177
结构观察区: Primary Flip 14.35（全链重定价，覆盖 84%）
Put Wall 15（弱结构｜现价高于该位 4.1%）
最近结构参考: Put Wall 15（现价高于该位 4.1%）
量化视角： 正 Gamma（121万，无历史分位）｜正 Gamma 减弱（27万）｜现价位于 Flip 上方 8.86%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 7D
10-16  C +39 / P -0.2k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +30 / P +0.3k ｜ Activity HIGH ｜ 21D
10-30  C +4.9k / P +10 ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 5.4k / P 1.8k，今日变化ΔOI: C +0.2k / P +0.3k，平值价格ATM: C $0.80 / P $0.35 ｜ ATM IV 63.9%，净 delta 敞口 -4k shares
Top ΔOI: P 15 -174 ｜ P 14 +170 ｜ C 16 +100
仓位参考: Max Pain 18 ｜ Put Wall 16（+2.4%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 63.9%｜历史 Rank 96%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 4,339 股

10-16（MEDIUM △）Top ΔOI: 23P -78 ｜ 24P -75
10-16（MEDIUM △）仓位参考: Max Pain 19 ｜ Put Wall 15（-4.0%，弱）（OI 0.9k）

📆 10-23 Forward Structure
存量OI: C 4.8k / P 1.0k，今日变化ΔOI: C +30 / P +0.3k，平值价格ATM: C $1.27 / P $0.85 ｜ ATM IV 70.3%，净 delta 敞口 -3k shares
仓位参考: Max Pain 18 ｜ Put Wall 16（+2.4%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.3%｜历史 Rank 96%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 负 3,321 股

📆 10-30 Forward Structure
存量OI: C 5.7k / P 0.6k，今日变化ΔOI: C +4.9k / P +10，平值价格ATM: C $1.31 / P $1.03 ｜ ATM IV 71.2%，净 delta 敞口 77k shares
Top ΔOI: C 20 +4,917
仓位参考: Max Pain 16 ｜ Put Wall 15（-4.0%，弱）（OI 89）
量化解读： 存量 Call 重｜ATM IV 71.2%｜历史 Rank 96%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 77,142 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/NNE_evening.json