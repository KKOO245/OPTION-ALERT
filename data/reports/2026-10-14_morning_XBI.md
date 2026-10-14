# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $773.15 ｜ QQQ $736.47
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **事件差分**: 10-16 ATM IV 44.9% vs 10-23 33.2%（差 +11.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 150P ΔOI -7,675（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 146.80 → 今开 146.17（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 148.82 ｜ 低 145.26

Options: P/C成交量 2.93 | OI比 1.47 | ATM IV 44.9% | Skew 7.5pp | Term 0.72 | ExpMove ±2.7%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价显著（Skew 7.5pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.93）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.93×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.47×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±2.7% ｜ 10-23（9D）±4.0% ｜ 10-30（16D）±4.9% ｜ 11-06（23D）±0.0%
   ⇒ IV–VIX Spread: +29.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -66,694,777 | GEX Change vs 上次快照 1,808,987 | Flip: Primary Flip: 159.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 366 / LOW 123 / INVALID 285
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 159.41（全链重定价，覆盖 92%）
Put Wall 150（现价低于该位 0.9%）
最近结构参考: Put Wall 150（现价低于该位 0.9%）
量化视角： 负 Gamma（6669万，无历史分位）｜负 Gamma 缓解（+181万）｜现价位于 Flip 下方 6.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall） / 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 148.0P — Vol 2,471 | 最新价 $2.33 | OI 970→3260 (ΔOI +2290张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2290张（+236.1% vs前日OI），连续性待观察（方向未知）
10-30 146.0P — Vol 1,252 | 最新价 $3.17 | OI 14→1257 (ΔOI +1243张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1243张（+8878.6% vs前日OI），连续性待观察（方向未知）
10-16 151.0C — Vol 1,252 | 最新价 $0.61 | OI 162→1292 (ΔOI +1130张) | ΔOI/Volume 90.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1130张（+697.5% vs前日OI），连续性待观察（方向未知）
10-16 144.0P — Vol 1,021 | 最新价 $0.69 | OI 4017→4966 (ΔOI +949张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增949张（+23.6% vs前日OI），连续性待观察（方向未知）
10-16 147.0P — Vol 1,100 | 最新价 $1.59 | OI 1959→2890 (ΔOI +931张) | ΔOI/Volume 84.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增931张（+47.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,543 张（Put 5,413 / Call 1,130），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +2.4k / P -6.2k ｜ Activity MEDIUM △ ｜ 2D
10-23  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 9D
10-30  C +0.5k / P +1.3k ｜ Activity MEDIUM △ ｜ 16D
11-06  C -3 / P +0.2k ｜ Activity MEDIUM △ ｜ 23D

📆 10-16 Forward Structure
存量OI: C 47.2k / P 69.5k，今日变化ΔOI: C +2.4k / P -6.2k，平值价格ATM: C $1.40 / P $2.57 ｜ ATM IV 44.9%，净 delta 敞口 676k shares
Top ΔOI: P 150 -7,675 ｜ P 148 +2,290 ｜ C 151 +1,130
仓位参考: Max Pain 155 ｜ Call Wall 155（+4.3%，弱）（OI 2.5k） ｜ Put Wall 150（+0.9%）（OI 15.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.9%｜历史 Rank 93%（近端代理）｜IV/RV 1.58×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 675,885 股

📆 10-23 Forward Structure
存量OI: C 2.5k / P 2.9k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $2.50 / P $3.37 ｜ ATM IV 33.2%，净 delta 敞口 6k shares
Top ΔOI: C 154 +420 ｜ P 145 +243
仓位参考: Max Pain 154 ｜ Call Wall 154（+3.6%）（OI 0.6k） ｜ Put Wall 140（-5.8%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.2%｜历史 Rank 93%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,858 股

10-30（MEDIUM △）Top ΔOI: 146P +1,243 ｜ 161C +99
10-30（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 155（+4.3%）（OI 1.4k） ｜ Put Wall 150（+0.9%，弱）（OI 7.2k）

11-06（MEDIUM △）Top ΔOI: 143P +56 ｜ 157P +24
11-06（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 150（+0.9%，弱）（OI 35） ｜ Put Wall 143（-3.8%）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 44.9% vs 10-23 33.2%（差 +11.7pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/XBI_morning.json