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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 423.02 → 收盘 427.64（+1.1%） ｜ 今日高 429.27 ｜ 低 421.03 ｜ 昨收 423.96 → 收盘 427.64（+0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.53 | OI比 0.93 | ATM IV 34.6% | Skew 1.0pp | Term 1.27 | ExpMove ±3.1%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常偏陡（Term 1.27）｜保护溢价薄（Skew 1.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（4D）±3.1% ｜ 10-23（11D）±8.0% ｜ 10-30（18D）±0.0% ｜ 11-06（25D）±10.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,235,344 | GEX Change vs 上次快照 -396,795 | Flip: Primary Flip: 406.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 324 / LOW 157 / INVALID 423
结构观察区: Primary Flip 406.14（全链重定价，覆盖 85%）
Call Wall 420（弱结构｜现价高于该位 1.8%）
最近结构参考: Call Wall 420（现价高于该位 1.8%）
量化视角： 正 Gamma（324万，无历史分位）｜正 Gamma 减弱（40万）｜现价位于 Flip 上方 5.29%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 406（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 457.5C — Vol 0 | 最新价 $0.30 | OI 0→219 (ΔOI +219张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增219张（量数据缺失），以日内换手为主
10-30 510.0C — Vol 0 | 最新价 $1.68 | OI 0→146 (ΔOI +146张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增146张（量数据缺失），以日内换手为主
10-23 340.0P — Vol 1 | 最新价 $0.71 | OI 8→147 (ΔOI +139张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增139张（+1737.5% vs前日OI），值得跟踪（方向未知）
10-16 450.0C — Vol 18 | 最新价 $0.99 | OI 563→702 (ΔOI +139张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增139张（+24.7% vs前日OI），值得跟踪（方向未知）
10-16 440.0C — Vol 71 | 最新价 $2.15 | OI 523→623 (ΔOI +100张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增100张（+19.1% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 743 张（Put 139 / Call 604），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.6k / P +53 ｜ Activity HIGH ｜ 4D
10-23  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 11D
10-30  C +0.3k / P +81 ｜ Activity MEDIUM △ ｜ 18D
11-06  C +11 / P +10 ｜ Activity MEDIUM △ ｜ 25D

📆 10-16 Forward Structure
存量OI: C 11.5k / P 10.6k，今日变化ΔOI: C +0.6k / P +53，平值价格ATM: C $6.20 / P $7.07 ｜ ATM IV 34.6%，净 delta 敞口 725 shares
Top ΔOI: C 457 +219 ｜ C 450 +139 ｜ C 440 +100
仓位参考: Max Pain 395 ｜ Call Wall 400（-6.5%，弱）（OI 0.9k） ｜ Put Wall 400（-6.5%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 34.6%｜历史 Rank 24%（近端代理）｜IV/RV 1.38×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 725 股

📆 10-23 Forward Structure
存量OI: C 1.9k / P 1.6k，今日变化ΔOI: C +0.1k / P +0.2k，平值价格ATM: C $17.54 / P $16.80 ｜ ATM IV 58.5%，净 delta 敞口 4k shares
Top ΔOI: C 465 +18
仓位参考: Max Pain 415 ｜ Call Wall 425（-0.6%）（OI 0.5k） ｜ Put Wall 415（-3.0%）（OI 0.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.5%｜历史 Rank 24%（近端代理）｜IV/RV 2.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,014 股

10-30（MEDIUM △）仓位参考: Max Pain 395 ｜ Call Wall 460（+7.6%，弱）（OI 94） ｜ Put Wall 400（-6.5%，弱）（OI 43）

11-06（MEDIUM △）Top ΔOI: 420C +3 ｜ 395P +2
11-06（MEDIUM △）仓位参考: Max Pain 400 ｜ Call Wall 455（+6.4%，弱）（OI 49） ｜ Put Wall 400（-6.5%，弱）（OI 37）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/ISRG_evening.json