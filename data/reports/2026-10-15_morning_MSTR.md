# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $770.81 ｜ QQQ $723.63
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.9（fear）
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
🔴 **事件差分**: 10-16（1D）ATM IV 101.4% vs 10-23 74.0%（差 +27.4pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 142P ΔOI -3,713（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 143.24 → 今开 137.72（-3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 140.93 ｜ 低 134.89

Options: P/C成交量 0.23 | OI比 0.64 | ATM IV 101.4% | Skew 4.0pp | Term 0.70 | ExpMove ±4.8%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±4.8% ｜ 10-23（8D）±8.4% ｜ 10-30（15D）±11.9% ｜ 11-06（22D）±15.3%
   ⇒ IV–VIX Spread: +83.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -24,666,133 | GEX Change vs 上次快照 -4,921,576 | Flip: Primary Flip: 143.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 554 / LOW 112 / INVALID 218
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 143.77（全链重定价，覆盖 99%）
Call Wall 135（弱结构｜现价高于该位 1.8%）
最近结构参考: Call Wall 135（现价高于该位 1.8%）
量化视角： 负 Gamma（2467万，无历史分位）｜负 Gamma 加深（492万）｜现价位于 Flip 下方 4.45%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Call Wall，弱结构）；上方 139（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 144（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 110.0P — Vol 3,625 | 最新价 $0.29 | OI 1577→4300 (ΔOI +2723张) | ΔOI/Volume 75.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2723张（+172.7% vs前日OI），连续性待观察（方向未知）
10-16 150.0C — Vol 9,388 | 最新价 $1.30 | OI 5887→8233 (ΔOI +2346张) | ΔOI/Volume 25.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2346张（+39.9% vs前日OI），连续性待观察（方向未知）
10-23 150.0P — Vol 3,187 | 最新价 $10.29 | OI 3307→5550 (ΔOI +2243张) | ΔOI/Volume 70.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2243张（+67.8% vs前日OI），连续性待观察（方向未知）
10-16 90.0P — Vol 3,695 | 最新价 $0.03 | OI 12422→14423 (ΔOI +2001张) | ΔOI/Volume 54.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2001张（+16.1% vs前日OI），连续性待观察（方向未知）
10-16 152.5C — Vol 6,221 | 最新价 $0.84 | OI 2947→4565 (ΔOI +1618张) | ΔOI/Volume 26.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1618张（+54.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,931 张（Put 6,967 / Call 3,964），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C -8.0k / P -13.8k ｜ Activity HIGH ｜ 1D
10-23  C +4.3k / P +12.2k ｜ Activity HIGH ｜ 8D
10-30  C +0.4k / P +4.4k ｜ Activity MEDIUM △ ｜ 15D
11-06  C +0.4k / P +1.0k ｜ Activity MEDIUM △ ｜ 22D

📆 10-16 Forward Structure
存量OI: C 344.6k / P 221.1k，今日变化ΔOI: C -8.0k / P -13.8k，平值价格ATM: C $3.96 / P $2.61 ｜ ATM IV 101.4%，净 delta 敞口 1.2M shares
Top ΔOI: P 142 -3,713
仓位参考: Max Pain 139 ｜ Call Wall 130（-5.4%，弱）（OI 12.5k） ｜ Put Wall 125（-9.0%，弱）（OI 10.2k）
量化解读： 存量 Call 重｜ATM IV 101.4%｜历史 Rank 81%（近端代理）｜IV/RV 2.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,235,289 股

📆 10-23 Forward Structure
存量OI: C 50.5k / P 108.6k，今日变化ΔOI: C +4.3k / P +12.2k，平值价格ATM: C $6.06 / P $5.51 ｜ ATM IV 74.0%，净 delta 敞口 -262k shares
Top ΔOI: P 110 +2,723 ｜ P 150 +2,243 ｜ C 167 +1,160
仓位参考: Max Pain 155 ｜ Call Wall 150（+9.2%，弱）（OI 1.8k） ｜ Put Wall 150（+9.2%，弱）（OI 5.5k）
量化解读： 存量 Put 重｜ATM IV 74.0%｜历史 Rank 81%（近端代理）｜IV/RV 1.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 262,371 股

10-30（MEDIUM △）Top ΔOI: 160C -1,279 ｜ 152P +952
10-30（MEDIUM △）仓位参考: Max Pain 160 ｜ Put Wall 125（-9.0%）（OI 11.6k）

11-06（MEDIUM △）Top ΔOI: 140P +223 ｜ 145P +165
11-06（MEDIUM △）仓位参考: Max Pain 160 ｜ Put Wall 150（+9.2%，弱）（OI 2.1k）

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 101.4% vs 10-23 74.0%（差 +27.4pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/MSTR_morning.json