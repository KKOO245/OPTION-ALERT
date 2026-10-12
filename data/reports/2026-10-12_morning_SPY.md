# 期权晨报 2026-10-12（快照 10:20 ET）

📊 市场环境

SPY $778.43 ｜ QQQ $745.73
VIX 15.29 ↑3.0%（5D -1.5%） ｜ Vol Regime: NORMAL
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
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-13 748P ΔOI +4,844（距现价 -3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 778.57 → 今开 778.78（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 779.40 ｜ 低 777.60

Options: P/C成交量 1.22 | OI比 2.18 | ATM IV 9.4% | Skew 1.5pp | Term 1.32 | ExpMove ±0.4%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常偏陡（Term 1.32）｜保护溢价薄（Skew 1.5pp）｜当日成交偏 Put（P/C量 1.22）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.22×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.18×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 65% ｜ P/C OI(近端) 74%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 65%）｜近端持仓结构中性（P/C OI 分位 74%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-13（1D）±0.4% ｜ 10-14（2D）±0.7% ｜ 10-15（3D）±0.8% ｜ 10-16（4D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 474,278,909 | GEX Change vs 上次快照 -116,234,032 | Flip: Primary Flip: 776.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3035 / LOW 356 / INVALID 1489
结构观察区: Primary Flip 776.87（全链重定价，覆盖 97%）
Call Wall 800（弱结构｜现价低于该位 2.7%）
最近结构参考: Flip 777（现价高于该位 0.2%）
量化视角： 正 Gamma（4.74亿，历史分位 65%，中性区）｜正 Gamma 减弱（1.16亿）｜现价位于 Flip 上方 0.22%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 776（MaxPain，仅结算参考）；上方 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 777（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 785.0C — Vol 53,508 | 最新价 $1.63 | OI 44310→73902 (ΔOI +29592张) | ΔOI/Volume 55.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29592张（+66.8% vs前日OI），连续性待观察（方向未知）
10-16 772.0P — Vol 32,387 | 最新价 $1.80 | OI 15109→36422 (ΔOI +21313张) | ΔOI/Volume 65.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21313张（+141.1% vs前日OI），连续性待观察（方向未知）
10-12 748.0P — Vol 23,181 | 最新价 $0.02 | OI 393→21425 (ΔOI +21032张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21032张（+5351.6% vs前日OI），连续性待观察（方向未知）
10-12 726.0P — Vol 54,968 | 最新价 $0.01 | OI 49→15519 (ΔOI +15470张) | ΔOI/Volume 28.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15470张（+31571.4% vs前日OI），连续性待观察（方向未知）
10-23 790.0C — Vol 24,438 | 最新价 $1.80 | OI 5254→19691 (ΔOI +14437张) | ΔOI/Volume 59.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14437张（+274.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 101,844 张（Put 57,815 / Call 44,029），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜彩票/名义 2 档（价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 178.1k / P 387.7k，今日成交量: C 353.1k / P 484.9k，平值价格ATM: C $0.55 / P $1.12 ｜ ATM IV 9.4%，预期波动 ±0.2%，Max Pain 776
Top ΔOI: P 748 +21,032 ｜ P 726 +15,470 ｜ P 746 +14,065

📆 Forward Expiration Structure

10-13  C +23.7k / P +26.1k ｜ Activity HIGH ｜ 1D
10-14  C -2.6k / P +21.2k ｜ Activity HIGH ｜ 2D
10-15  C +6.0k / P +10.9k ｜ Activity HIGH ｜ 3D
10-16  C +49.0k / P +83.8k ｜ Activity MEDIUM △ ｜ 4D

📆 10-13 Forward Structure
存量OI: C 88.0k / P 121.2k，今日变化ΔOI: C +23.7k / P +26.1k，平值价格ATM: C $1.42 / P $1.92 ｜ ATM IV 9.1%，净 delta 敞口 -19k shares
Top ΔOI: P 748 +4,844 ｜ C 795 +3,067 ｜ C 785 +3,048
仓位参考: Max Pain 776 ｜ Call Wall 790（+1.5%，弱）（OI 5.4k） ｜ Put Wall 774（-0.6%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 9.1%｜历史 Rank 20%（近端代理）｜IV/RV 1.06×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 18,795 股

📆 10-14 Forward Structure
存量OI: C 90.6k / P 103.5k，今日变化ΔOI: C -2.6k / P +21.2k，平值价格ATM: C $2.40 / P $2.87 ｜ ATM IV 10.6%，净 delta 敞口 -133k shares
Top ΔOI: C 790 -9,400 ｜ P 742 +4,604 ｜ P 736 +1,879
仓位参考: Max Pain 776 ｜ Call Wall 790（+1.5%）（OI 19.1k） ｜ Put Wall 770（-1.1%，弱）（OI 5.1k）
量化解读： 存量两侧均衡｜ATM IV 10.6%｜历史 Rank 20%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 负 132,568 股

📆 10-15 Forward Structure
存量OI: C 30.6k / P 69.5k，今日变化ΔOI: C +6.0k / P +10.9k，平值价格ATM: C $2.94 / P $3.33 ｜ ATM IV 10.7%，净 delta 敞口 -99k shares
Top ΔOI: P 710 +2,837 ｜ P 754 +2,008 ｜ C 796 +1,257
仓位参考: Max Pain 776 ｜ Call Wall 796（+2.2%，弱）（OI 2.0k） ｜ Put Wall 772（-0.8%，弱）（OI 4.2k）
量化解读： 存量 Put 重｜ATM IV 10.7%｜历史 Rank 20%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 负 98,622 股

10-16（MEDIUM △）Top ΔOI: 785C +29,592 ｜ 772P +21,313
10-16（MEDIUM △）仓位参考: Max Pain 770 ｜ Call Wall 785（+0.8%）（OI 73.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/SPY_morning.json