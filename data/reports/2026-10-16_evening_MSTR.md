# 期权晚报 2026-10-16（快照 16:40 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $709.80
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔵 **期限 OI 集中**: 11-13 80P ΔOI +3,899 占该期限总 OI 14.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 146.14 → 收盘 136.83（-6.4%） ｜ 今日高 146.83 ｜ 低 134.11 ｜ 昨收 151.29 → 收盘 136.83（-9.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-23，窗口结束前不做对错判定）

Options: P/C成交量 0.62 | OI比 0.76 | ATM IV 102.2% | Skew 8.7pp | Term 0.70 | ExpMove ±8.0%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 8.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±8.0% ｜ 10-30（14D）±11.8% ｜ 11-06（21D）±14.4% ｜ 11-13（28D）±16.2%
   ⇒ IV–VIX Spread: +82.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -20,309,638 | GEX Change vs 上次快照 -30,719,393 | Flip: Primary Flip: 145.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 557 / LOW 83 / INVALID 244
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 145.67（全链重定价，覆盖 84%）
Call Wall 135（弱结构｜现价高于该位 1.4%）
最近结构参考: Call Wall 135（现价高于该位 1.4%）
量化视角： 负 Gamma（2031万，无历史分位）｜由正转负（3072万）｜现价位于 Flip 下方 6.07%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Call Wall，弱结构）；上方 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 146（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +44.5k / P +15.0k ｜ Activity HIGH ｜ 7D
10-30  C +5.1k / P +5.2k ｜ Activity HIGH ｜ 14D
11-06  C +0.7k / P +2.7k ｜ Activity HIGH ｜ 21D
11-13  C +0.8k / P +6.3k ｜ Activity HIGH ｜ 28D

📆 10-23 Forward Structure
存量OI: C 95.0k / P 123.5k，今日变化ΔOI: C +44.5k / P +15.0k，平值价格ATM: C $5.42 / P $5.50 ｜ ATM IV 71.4%，净 delta 敞口 105k shares
Top ΔOI: C 152 +9,879 ｜ C 155 +9,250 ｜ C 160 +8,996
仓位参考: Max Pain 152 ｜ Put Wall 150（+9.6%，弱）（OI 5.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 71.4%｜历史 Rank 82%（近端代理）｜IV/RV 1.53×（近似）｜净 delta 敞口 正 104,833 股

📆 10-30 Forward Structure
存量OI: C 39.7k / P 62.5k，今日变化ΔOI: C +5.1k / P +5.2k，平值价格ATM: C $8.15 / P $8.06 ｜ ATM IV 75.6%，净 delta 敞口 -31k shares
仓位参考: Max Pain 158 ｜ Put Wall 125（-8.6%）（OI 11.7k）
量化解读： 存量 Put 重｜ATM IV 75.6%｜历史 Rank 82%（近端代理）｜IV/RV 1.62×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 30,505 股

📆 11-06 Forward Structure
存量OI: C 11.5k / P 23.8k，今日变化ΔOI: C +0.7k / P +2.7k，平值价格ATM: C $10.70 / P $9.07 ｜ ATM IV 73.1%，净 delta 敞口 -72k shares
Top ΔOI: P 115 +552 ｜ P 110 +315
仓位参考: Max Pain 160 ｜ Put Wall 150（+9.6%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 73.1%｜历史 Rank 82%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 72,388 股

📆 11-13 Forward Structure
存量OI: C 9.7k / P 17.2k，今日变化ΔOI: C +0.8k / P +6.3k，平值价格ATM: C $12.10 / P $10.08 ｜ ATM IV 71.7%，净 delta 敞口 -82k shares
Top ΔOI: P 80 +3,899 ｜ P 110 +408 ｜ P 105 +369
仓位参考: Max Pain 165 ｜ Put Wall 150（+9.6%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 71.7%｜历史 Rank 82%（近端代理）｜IV/RV 1.53×（近似）｜净 delta 敞口 负 81,684 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/MSTR_evening.json