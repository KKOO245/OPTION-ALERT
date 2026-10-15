# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $767.19 ｜ QQQ $720.47
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🔴 **事件差分**: 10-16（1D）ATM IV 97.3% vs 10-23 80.6%（差 +16.7pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 12P ΔOI +31（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 13.01 → 今开 12.50（-3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 12.68 ｜ 低 12.01

Options: P/C成交量 0.98 | OI比 0.17 | ATM IV 97.3% | Skew 1.5pp | Term 0.73 | ExpMove ±6.9%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜存量 Call 偏重（OI比 0.17）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.17×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±6.9% ｜ 10-23（8D）±7.8% ｜ 10-30（15D）±13.7% ｜ 11-06（22D）±28.0%
   ⇒ IV–VIX Spread: +79.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -69,046 | GEX Change vs 上次快照 331,335 | Flip: Primary Flip: 13.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 128 / LOW 119 / INVALID 169
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 13.39（全链重定价，覆盖 98%）
最近结构参考: Flip 12（现价高于该位 1.2%）
量化视角： 负 Gamma（7万，无历史分位）｜负 Gamma 缓解（+33万）｜现价位于 Flip 下方 8.05%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 13（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 13.5C — Vol 250 | 最新价 $0.15 | OI 12→200 (ΔOI +188张) | ΔOI/Volume 75.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增188张（+1566.7% vs前日OI），连续性待观察（方向未知）
10-16 14.0C — Vol 277 | 最新价 $0.09 | OI 88→262 (ΔOI +174张) | ΔOI/Volume 62.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增174张（+197.7% vs前日OI），连续性待观察（方向未知）
10-16 13.0P — Vol 145 | 最新价 $0.40 | OI 422→561 (ΔOI +139张) | ΔOI/Volume 95.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增139张（+32.9% vs前日OI），连续性待观察（方向未知）
10-30 14.0P — Vol 108 | 最新价 $1.52 | OI 315→396 (ΔOI +81张) | ΔOI/Volume 75.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增81张（+25.7% vs前日OI），连续性待观察（方向未知）
10-30 13.5C — Vol 91 | 最新价 $0.60 | OI 17→80 (ΔOI +63张) | ΔOI/Volume 69.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增63张（+370.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 645 张（Put 220 / Call 425），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.4k / P -0.7k ｜ Activity MEDIUM △ ｜ 1D
10-23  C +0.1k / P -37 ｜ Activity MEDIUM △ ｜ 8D
10-30  C +71 / P +0.1k ｜ Activity HIGH ｜ 15D
11-06  C -3 / P +57 ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 23.1k / P 3.9k，今日变化ΔOI: C +0.4k / P -0.7k，平值价格ATM: C $0.65 / P $0.20 ｜ ATM IV 97.3%，净 delta 敞口 91k shares
Top ΔOI: P 17 -525 ｜ C 13 +188
仓位参考: Max Pain 15 ｜ Put Wall 13（+5.6%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 97.3%｜历史 Rank 36%（近端代理）｜IV/RV 1.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 91,326 股

10-23（MEDIUM △）Top ΔOI: 13C +56 ｜ 12C +20
10-23（MEDIUM △）仓位参考: Max Pain 16

📆 10-30 Forward Structure
存量OI: C 6.3k / P 0.9k，今日变化ΔOI: C +71 / P +0.1k，平值价格ATM: C $1.15 / P $0.54 ｜ ATM IV 76.4%，净 delta 敞口 -2k shares
Top ΔOI: C 13 +63 ｜ P 12 +31
仓位参考: Max Pain 16
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 76.4%｜历史 Rank 36%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,405 股

📆 11-06 Forward Structure
存量OI: C 1.5k / P 0.4k，今日变化ΔOI: C -3 / P +57，平值价格ATM: C $3.17 / P $0.28 ｜ ATM IV 75.1%，净 delta 敞口 -3k shares
Top ΔOI: P 13 +52
仓位参考: Max Pain 16 ｜ Put Wall 13（+5.6%，弱）（OI 76）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 75.1%｜历史 Rank 36%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 负 2,538 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 97.3% vs 10-23 80.6%（差 +16.7pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/NNE_morning.json