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
🟡 **近现价集中开仓**: 10-13 748P ΔOI +4,844（距现价 -3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 778.78 → 收盘 778.10（-0.1%） ｜ 今日高 779.40 ｜ 低 777.05 ｜ 昨收 778.57 → 收盘 778.10（-0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.01 | OI比 2.18 | ATM IV 5.7% | Skew -0.8pp | Term 2.19 | ExpMove ±0.3%（近端） | Rank 2%
量化视角： IV 历史低位（Rank 2%，期权偏便宜）｜期限结构正常偏陡（Term 2.19）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.18×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 62% ｜ P/C OI(近端) 74%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 62%）｜近端持仓结构中性（P/C OI 分位 74%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-13（1D）±0.3% ｜ 10-14（2D）±0.6% ｜ 10-15（3D）±0.8% ｜ 10-16（4D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 306,091,023 | GEX Change vs 上次快照 -168,187,886 | Flip: Primary Flip: 776.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2871 / LOW 439 / INVALID 1570
结构观察区: Primary Flip 776.62（全链重定价，覆盖 94%）
Call Wall 800（弱结构｜现价低于该位 2.7%）
最近结构参考: Flip 777（现价高于该位 0.2%）
量化视角： 正 Gamma（3.06亿，历史分位 62%，中性区）｜正 Gamma 减弱（1.68亿）｜现价位于 Flip 上方 0.19%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 776（MaxPain，仅结算参考）；上方 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 777（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 785.0C — Vol 51,916 | 最新价 $1.03 | OI 44310→73902 (ΔOI +29592张) | ΔOI/Volume 57.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29592张（+66.8% vs前日OI），连续性待观察（方向未知）
10-16 772.0P — Vol 16,018 | 最新价 $1.42 | OI 15109→36422 (ΔOI +21313张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21313张（+141.1% vs前日OI），连续性待观察（方向未知）
10-23 790.0C — Vol 14,666 | 最新价 $1.25 | OI 5254→19691 (ΔOI +14437张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14437张（+274.8% vs前日OI），连续性待观察（方向未知）
量化视角： 3 个事件合计 ΔOI ≈ 65,342 张（Put 21,313 / Call 44,029），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-13  C +23.7k / P +26.1k ｜ Activity HIGH ｜ 1D
10-14  C -2.6k / P +21.2k ｜ Activity HIGH ｜ 2D
10-15  C +6.0k / P +10.9k ｜ Activity HIGH ｜ 3D
10-16  C +49.0k / P +83.8k ｜ Activity HIGH ｜ 4D

📆 10-13 Forward Structure
存量OI: C 88.0k / P 121.2k，今日变化ΔOI: C +23.7k / P +26.1k，平值价格ATM: C $1.43 / P $1.33 ｜ ATM IV 8.5%，净 delta 敞口 -94k shares
Top ΔOI: P 748 +4,844 ｜ C 795 +3,067 ｜ C 785 +3,048
仓位参考: Max Pain 776 ｜ Call Wall 790（+1.5%，弱）（OI 5.4k） ｜ Put Wall 774（-0.5%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 8.5%｜历史 Rank 2%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 93,819 股

📆 10-14 Forward Structure
存量OI: C 90.6k / P 103.5k，今日变化ΔOI: C -2.6k / P +21.2k，平值价格ATM: C $2.52 / P $2.34 ｜ ATM IV 10.5%，净 delta 敞口 -128k shares
Top ΔOI: C 790 -9,400 ｜ P 742 +4,604 ｜ P 736 +1,879
仓位参考: Max Pain 776 ｜ Call Wall 790（+1.5%）（OI 19.1k） ｜ Put Wall 755（-3.0%，弱）（OI 5.1k）
量化解读： 存量两侧均衡｜ATM IV 10.5%｜历史 Rank 2%（近端代理）｜IV/RV 1.23×（近似）｜净 delta 敞口 负 128,146 股

📆 10-15 Forward Structure
存量OI: C 30.6k / P 69.5k，今日变化ΔOI: C +6.0k / P +10.9k，平值价格ATM: C $3.13 / P $2.87 ｜ ATM IV 10.6%，净 delta 敞口 -109k shares
Top ΔOI: P 710 +2,837 ｜ P 754 +2,008 ｜ C 796 +1,257
仓位参考: Max Pain 776 ｜ Call Wall 796（+2.3%，弱）（OI 2.0k） ｜ Put Wall 772（-0.8%，弱）（OI 4.2k）
量化解读： 存量 Put 重｜ATM IV 10.6%｜历史 Rank 2%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 负 108,564 股

📆 10-16 Forward Structure
存量OI: C 682.1k / P 2358.8k，今日变化ΔOI: C +49.0k / P +83.8k，平值价格ATM: C $3.78 / P $3.30 ｜ ATM IV 10.8%，净 delta 敞口 -297k shares
Top ΔOI: C 785 +29,592 ｜ P 772 +21,313
仓位参考: Max Pain 770 ｜ Call Wall 785（+0.9%）（OI 73.9k）
量化解读： 存量 Put 重｜ATM IV 10.8%｜历史 Rank 2%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 负 297,181 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/SPY_evening.json