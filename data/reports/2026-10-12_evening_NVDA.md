# 期权晚报 2026-10-12（快照 16:40 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-14 235C ΔOI +3,277（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-14 195P ΔOI +9,450 占该期限总 OI 11.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 228.73 → 收盘 226.32（-1.1%） ｜ 今日高 228.86 ｜ 低 224.92 ｜ 昨收 229.28 → 收盘 226.32（-1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.72 | OI比 1.04 | ATM IV 31.8% | Skew -29.3pp | Term 0.95 | ExpMove ±2.0%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -29.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-14（2D）±2.0% ｜ 10-16（4D）±2.9% ｜ 10-19（7D）±3.2% ｜ 10-21（9D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 289,436,826 | GEX Change vs 上次快照 -36,479,828 | Flip: Primary Flip: 215.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 729 / LOW 204 / INVALID 605
结构观察区: Primary Flip 215.31（全链重定价，覆盖 96%）
Call Wall 240（弱结构｜现价低于该位 5.7%）
最近结构参考: Flip 215（现价高于该位 5.1%）
量化视角： 正 Gamma（2.89亿，无历史分位）｜正 Gamma 减弱（3648万）｜现价位于 Flip 上方 5.11%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 230（MaxPain，仅结算参考） / 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 215（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 110.0P — Vol 10 | 最新价 $0.01 | OI 9601→53629 (ΔOI +44028张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44028张（+458.6% vs前日OI），连续性待观察（方向未知）
10-16 237.5C — Vol 16,720 | 最新价 $0.35 | OI 12685→42425 (ΔOI +29740张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29740张（+234.4% vs前日OI），连续性待观察（方向未知）
10-16 232.5C — Vol 24,892 | 最新价 $1.08 | OI 17359→39819 (ΔOI +22460张) | ΔOI/Volume 90.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22460张（+129.4% vs前日OI），连续性待观察（方向未知）
10-16 235.0C — Vol 27,710 | 最新价 $0.63 | OI 53070→72867 (ΔOI +19797张) | ΔOI/Volume 71.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19797张（+37.3% vs前日OI），连续性待观察（方向未知）
10-16 242.5C — Vol 7,080 | 最新价 $0.12 | OI 22250→39928 (ΔOI +17678张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17678张（+79.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 133,703 张（Put 44,028 / Call 89,675），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-14  C +15.4k / P +21.6k ｜ Activity HIGH ｜ 2D
10-16  C +73.0k / P +94.4k ｜ Activity HIGH ｜ 4D
10-19  C +6.0k / P +1.8k ｜ Activity HIGH ｜ 7D
10-21  C +3.5k / P +0.4k ｜ Activity HIGH ｜ 9D

📆 10-14 Forward Structure
存量OI: C 48.0k / P 37.6k，今日变化ΔOI: C +15.4k / P +21.6k，平值价格ATM: C $1.79 / P $2.80 ｜ ATM IV 33.6%，净 delta 敞口 -193k shares
Top ΔOI: P 195 +9,450 ｜ C 235 +3,277 ｜ C 230 +2,887
仓位参考: Max Pain 230 ｜ Call Wall 237.5（+4.9%，弱）（OI 6.1k） ｜ Put Wall 215（-5.0%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.6%｜历史 Rank 12%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 193,438 股

📆 10-16 Forward Structure
存量OI: C 1022.1k / P 804.5k，今日变化ΔOI: C +73.0k / P +94.4k，平值价格ATM: C $2.83 / P $3.67 ｜ ATM IV 33.9%，净 delta 敞口 -2.6M shares
Top ΔOI: C 180 -29,978 ｜ C 237 +29,740
仓位参考: Max Pain 220 ｜ Call Wall 220（-2.8%，弱）（OI 99.3k） ｜ Put Wall 220（-2.8%，弱）（OI 60.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 33.9%｜历史 Rank 12%（近端代理）｜IV/RV 1.71×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,602,239 股

📆 10-19 Forward Structure
存量OI: C 30.4k / P 6.1k，今日变化ΔOI: C +6.0k / P +1.8k，平值价格ATM: C $3.18 / P $3.98 ｜ ATM IV 28.5%，净 delta 敞口 48k shares
Top ΔOI: C 235 +1,830 ｜ C 240 +675 ｜ C 245 +550
仓位参考: Max Pain 230 ｜ Call Wall 247.5（+9.4%，弱）（OI 9.3k） ｜ Put Wall 220（-2.8%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 28.5%｜历史 Rank 12%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 正 47,562 股

📆 10-21 Forward Structure
存量OI: C 6.7k / P 2.4k，今日变化ΔOI: C +3.5k / P +0.4k，平值价格ATM: C $3.90 / P $4.55 ｜ ATM IV 29.4%，净 delta 敞口 41k shares
Top ΔOI: C 240 +2,176 ｜ C 230 +308 ｜ C 242 +286
仓位参考: Max Pain 230 ｜ Call Wall 240（+6.0%）（OI 3.1k） ｜ Put Wall 227.5（+0.5%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 29.4%｜历史 Rank 12%（近端代理）｜IV/RV 1.48×（近似）｜净 delta 敞口 正 40,740 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/NVDA_evening.json