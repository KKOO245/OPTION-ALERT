# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
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
🔴 **事件差分**: 10-16（1D）ATM IV 114.0% vs 10-23 81.4%（差 +32.6pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,403.34 → 今开 1,312.97（-6.4%） | 较昨收变动（含盘初走势） ｜ 今日高 1325.00 ｜ 低 1276.07

Options: P/C成交量 0.61 | OI比 0.85 | ATM IV 114.0% | Skew 5.2pp | Term 0.68 | ExpMove ±5.3%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.68，近月 IV 高于远月）｜保护溢价中性（Skew 5.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±5.3% ｜ 10-23（8D）±9.8% ｜ 10-30（15D）±14.4% ｜ 11-06（22D）±16.1%
   ⇒ IV–VIX Spread: +96.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -11,224,263 | GEX Change vs 上次快照 -28,271 | Flip: Primary Flip: 1418.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 1789 / LOW 542 / INVALID 1021
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1418.45（全链重定价，覆盖 95%）
最近结构参考: Flip 1418（现价低于该位 8.6%）
量化视角： 负 Gamma（1122万，无历史分位）｜负 Gamma 加深（3万）｜现价位于 Flip 下方 8.59%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,520（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1418（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 1450.0C — Vol 5,213 | 最新价 $16.80 | OI 392→1079 (ΔOI +687张) | ΔOI/Volume 13.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增687张（+175.3% vs前日OI），连续性待观察（方向未知）
10-16 1675.0C — Vol 628 | 最新价 $0.55 | OI 1981→2404 (ΔOI +423张) | ΔOI/Volume 67.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增423张（+21.4% vs前日OI），连续性待观察（方向未知）
10-23 1100.0P — Vol 578 | 最新价 $1.81 | OI 204→603 (ΔOI +399张) | ΔOI/Volume 69.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增399张（+195.6% vs前日OI），连续性待观察（方向未知）
10-16 1550.0C — Vol 2,468 | 最新价 $2.45 | OI 1351→1744 (ΔOI +393张) | ΔOI/Volume 15.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增393张（+29.1% vs前日OI），连续性待观察（方向未知）
10-16 1430.0C — Vol 1,522 | 最新价 $23.44 | OI 138→489 (ΔOI +351张) | ΔOI/Volume 23.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增351张（+254.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,253 张（Put 399 / Call 1,854），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +4.8k / P -1.2k ｜ Activity HIGH ｜ 1D
10-23  C +0.5k / P +1.9k ｜ Activity HIGH ｜ 8D
10-30  C +1.0k / P +0.2k ｜ Activity HIGH ｜ 15D
11-06  C +0.2k / P +0.4k ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 81.8k / P 69.6k，今日变化ΔOI: C +4.8k / P -1.2k，平值价格ATM: C $36.00 / P $32.92 ｜ ATM IV 114.0%，净 delta 敞口 311k shares
Top ΔOI: C 1450 +687 ｜ P 1400 -648
仓位参考: Max Pain 1,520 ｜ Put Wall 1400（+8.0%，弱）（OI 2.7k）
量化解读： 存量两侧均衡｜ATM IV 114.0%｜历史 Rank 73%（近端代理）｜IV/RV 2.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 310,659 股

📆 10-23 Forward Structure
存量OI: C 24.2k / P 19.2k，今日变化ΔOI: C +0.5k / P +1.9k，平值价格ATM: C $63.30 / P $63.50 ｜ ATM IV 81.4%，净 delta 敞口 -25k shares
Top ΔOI: C 1700 -1,537 ｜ P 1100 +399 ｜ C 1500 +255
仓位参考: Max Pain 1,540 ｜ Put Wall 1400（+8.0%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.4%｜历史 Rank 73%（近端代理）｜IV/RV 1.62×（近似）｜净 delta 敞口 负 24,754 股

📆 10-30 Forward Structure
存量OI: C 15.8k / P 12.8k，今日变化ΔOI: C +1.0k / P +0.2k，平值价格ATM: C $91.29 / P $96.03 ｜ ATM IV 88.1%，净 delta 敞口 11k shares
Top ΔOI: C 1750 +154 ｜ P 1100 +122 ｜ C 1600 +117
仓位参考: Max Pain 1,595 ｜ Put Wall 1400（+8.0%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 88.1%｜历史 Rank 73%（近端代理）｜IV/RV 1.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,101 股

📆 11-06 Forward Structure
存量OI: C 5.0k / P 5.8k，今日变化ΔOI: C +0.2k / P +0.4k，平值价格ATM: C $102.40 / P $106.28 ｜ ATM IV 82.0%，净 delta 敞口 -7k shares
Top ΔOI: P 1340 +100 ｜ P 1000 +60
仓位参考: Max Pain 1,630 ｜ Put Wall 1400（+8.0%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 82.0%｜历史 Rank 73%（近端代理）｜IV/RV 1.63×（近似）｜净 delta 敞口 负 6,807 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 114.0% vs 10-23 81.4%（差 +32.6pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/SNDK_morning.json