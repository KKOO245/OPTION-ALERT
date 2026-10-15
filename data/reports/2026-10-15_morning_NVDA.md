# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $771.47 ｜ QQQ $728.00
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
🔴 **事件差分**: 10-16（1D）ATM IV 53.5% vs 10-19 37.6%（差 +15.9pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 217P ΔOI +10,207（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 221.30 → 今开 215.34（-2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 216.48 ｜ 低 212.85

Options: P/C成交量 0.53 | OI比 0.83 | ATM IV 53.5% | Skew 5.3pp | Term 0.67 | ExpMove ±2.5%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价中性（Skew 5.3pp）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.5% ｜ 10-19（4D）±3.2% ｜ 10-21（6D）±4.1% ｜ 10-23（8D）±4.7%
   ⇒ IV–VIX Spread: +36.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -34,658,024 | GEX Change vs 上次快照 -159,039,730 | Flip: Primary Flip: 216.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 683 / LOW 191 / INVALID 608
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 216.18（全链重定价，覆盖 98%）
Put Wall 220（弱结构｜现价低于该位 2.3%）
最近结构参考: Flip 216（现价低于该位 0.6%）
量化视角： 负 Gamma（3466万，无历史分位）｜由正转负（1.59亿）｜现价位于 Flip 下方 0.57%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 220（Put Wall，弱结构） / 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 216（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 227.5C — Vol 14,951 | 最新价 $2.49 | OI 2553→12804 (ΔOI +10251张) | ΔOI/Volume 68.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10251张（+401.5% vs前日OI），连续性待观察（方向未知）
10-16 217.5P — Vol 31,920 | 最新价 $1.51 | OI 9150→19357 (ΔOI +10207张) | ΔOI/Volume 32.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10207张（+111.5% vs前日OI），连续性待观察（方向未知）
10-16 135.0P — Vol 10,128 | 最新价 $0.01 | OI 11821→21123 (ΔOI +9302张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9302张（+78.7% vs前日OI），连续性待观察（方向未知）
10-26 237.5C — Vol 9,624 | 最新价 $0.75 | OI 37→9074 (ΔOI +9037张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9037张（+24424.3% vs前日OI），连续性待观察（方向未知）
10-19 180.0P — Vol 8,536 | 最新价 $0.08 | OI 66→8587 (ΔOI +8521张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8521张（+12910.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 47,318 张（Put 28,030 / Call 19,288），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C -11.0k / P +52.9k ｜ Activity HIGH ｜ 1D
10-19  C +9.3k / P +18.1k ｜ Activity HIGH ｜ 4D
10-21  C +6.4k / P +4.4k ｜ Activity HIGH ｜ 6D
10-23  C +22.5k / P +20.4k ｜ Activity HIGH ｜ 8D

📆 10-16 Forward Structure
存量OI: C 1065.0k / P 882.3k，今日变化ΔOI: C -11.0k / P +52.9k，平值价格ATM: C $2.93 / P $2.45 ｜ ATM IV 53.5%，净 delta 敞口 -868k shares
Top ΔOI: C 235 -18,863 ｜ P 217 +10,207
仓位参考: Max Pain 220 ｜ Call Wall 220（+2.4%，弱）（OI 100.4k） ｜ Put Wall 220（+2.4%，弱）（OI 71.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 53.5%｜历史 Rank 78%（近端代理）｜IV/RV 2.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 867,732 股

📆 10-19 Forward Structure
存量OI: C 58.0k / P 36.5k，今日变化ΔOI: C +9.3k / P +18.1k，平值价格ATM: C $3.75 / P $3.19 ｜ ATM IV 37.6%，净 delta 敞口 -311k shares
Top ΔOI: P 180 +8,521 ｜ P 217 +3,149 ｜ C 225 +2,813
仓位参考: Max Pain 225 ｜ Call Wall 225（+4.7%，弱）（OI 4.6k） ｜ Put Wall 230（+7.0%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 37.6%｜历史 Rank 78%（近端代理）｜IV/RV 1.72×（近似）｜净 delta 敞口 负 311,126 股

📆 10-21 Forward Structure
存量OI: C 28.1k / P 17.0k，今日变化ΔOI: C +6.4k / P +4.4k，平值价格ATM: C $4.69 / P $4.10 ｜ ATM IV 39.1%，净 delta 敞口 -91k shares
Top ΔOI: C 225 +1,212 ｜ C 230 +1,009
仓位参考: Max Pain 225 ｜ Call Wall 230（+7.0%，弱）（OI 4.2k） ｜ Put Wall 220（+2.4%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 39.1%｜历史 Rank 78%（近端代理）｜IV/RV 1.79×（近似）｜净 delta 敞口 负 90,528 股

📆 10-23 Forward Structure
存量OI: C 192.2k / P 155.2k，今日变化ΔOI: C +22.5k / P +20.4k，平值价格ATM: C $5.36 / P $4.75 ｜ ATM IV 39.2%，净 delta 敞口 -425k shares
Top ΔOI: C 227 +10,251 ｜ P 220 +7,030 ｜ P 217 +5,033
仓位参考: Max Pain 225 ｜ Call Wall 235（+9.3%，弱）（OI 15.0k） ｜ Put Wall 220（+2.4%，弱）（OI 13.3k）
量化解读： 存量 Call 重｜ATM IV 39.2%｜历史 Rank 78%（近端代理）｜IV/RV 1.79×（近似）｜净 delta 敞口 负 425,476 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 53.5% vs 10-19 37.6%（差 +15.9pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/NVDA_morning.json