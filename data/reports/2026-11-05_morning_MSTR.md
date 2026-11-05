# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $732.06 ｜ QQQ $647.05
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（1D）ATM IV 112.8% vs 11-13 83.8%（差 +29.0pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-20 135P ΔOI +2,062（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 142.54 → 今开 139.37（-2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 141.17 ｜ 低 129.93

Options: P/C成交量 1.21 | OI比 0.61 | ATM IV 112.8% | Skew 8.4pp | Term 0.65 | ExpMove ±5.3%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价显著（Skew 8.4pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.61）+ 当日成交偏 Put（P/C量 1.21）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±5.3% ｜ 11-13（8D）±10.1% ｜ 11-20（15D）±13.0% ｜ 11-27（22D）±15.3%
   ⇒ IV–VIX Spread: +91.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 65,782,260 | GEX Change vs 上次快照 -54,703,769 | Flip: Primary Flip: 125.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 514 / LOW 110 / INVALID 216
结构观察区: Primary Flip 125.23（全链重定价，覆盖 100%）
Call Wall 135（现价低于该位 1.5%）
最近结构参考: Call Wall 135（现价低于该位 1.5%）
量化视角： 正 Gamma（6578万，无历史分位）｜正 Gamma 减弱（5470万）｜现价位于 Flip 上方 6.23%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 135（MaxPain，仅结算参考） / 135（Call Wall）。
• Gamma 区域：切换参考 125（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 150.0C — Vol 20,181 | 最新价 $1.16 | OI 5462→12413 (ΔOI +6951张) | ΔOI/Volume 34.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6951张（+127.3% vs前日OI），连续性待观察（方向未知）
11-13 85.0P — Vol 5,649 | 最新价 $0.09 | OI 941→5975 (ΔOI +5034张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5034张（+535.0% vs前日OI），连续性待观察（方向未知）
11-06 146.0C — Vol 17,649 | 最新价 $2.23 | OI 15519→18544 (ΔOI +3025张) | ΔOI/Volume 17.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3025张（+19.5% vs前日OI），连续性待观察（方向未知）
11-20 110.0P — Vol 4,318 | 最新价 $0.80 | OI 10753→13535 (ΔOI +2782张) | ΔOI/Volume 64.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2782张（+25.9% vs前日OI），连续性待观察（方向未知）
11-13 70.0P — Vol 2,704 | 最新价 $0.04 | OI 1330→3626 (ΔOI +2296张) | ΔOI/Volume 84.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2296张（+172.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 20,088 张（Put 10,112 / Call 9,976），跨 3 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +10.1k / P +3.8k ｜ Activity HIGH ｜ 1D
11-13  C +7.8k / P +12.4k ｜ Activity HIGH ｜ 8D
11-20  C +1.3k / P +6.7k ｜ Activity HIGH ｜ 15D
11-27  C +0.3k / P +3.8k ｜ Activity MEDIUM △ ｜ 22D

📆 11-06 Forward Structure
存量OI: C 246.3k / P 150.4k，今日变化ΔOI: C +10.1k / P +3.8k，平值价格ATM: C $3.35 / P $3.67 ｜ ATM IV 112.8%，净 delta 敞口 -273k shares
Top ΔOI: C 150 +6,951 ｜ C 139 -3,229 ｜ C 146 +3,025
仓位参考: Max Pain 135 ｜ Call Wall 136（+2.2%，弱）（OI 27.0k） ｜ Put Wall 125（-6.0%，弱）（OI 6.1k）
量化解读： 存量 Call 重｜ATM IV 112.8%｜历史 Rank 88%（近端代理）｜IV/RV 1.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 273,382 股

📆 11-13 Forward Structure
存量OI: C 35.2k / P 82.5k，今日变化ΔOI: C +7.8k / P +12.4k，平值价格ATM: C $6.65 / P $6.83 ｜ ATM IV 83.8%，净 delta 敞口 -46k shares
Top ΔOI: P 85 +5,034
仓位参考: Max Pain 150 ｜ Call Wall 144（+8.2%，弱）（OI 1.0k） ｜ Put Wall 125（-6.0%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 83.8%｜历史 Rank 88%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 45,705 股

📆 11-20 Forward Structure
存量OI: C 154.8k / P 139.6k，今日变化ΔOI: C +1.3k / P +6.7k，平值价格ATM: C $8.70 / P $8.60 ｜ ATM IV 79.6%，净 delta 敞口 -84k shares
Top ΔOI: P 110 +2,782 ｜ P 135 +2,062 ｜ P 120 -1,068
仓位参考: Max Pain 135 ｜ Call Wall 135（+1.5%）（OI 42.8k） ｜ Put Wall 120（-9.8%，弱）（OI 6.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.6%｜历史 Rank 88%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 83,592 股

11-27（MEDIUM △）Top ΔOI: 100P +760 ｜ 105P +653
11-27（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 145（+9.0%，弱）（OI 0.9k） ｜ Put Wall 140（+5.2%，弱）（OI 2.6k）

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 112.8% vs 11-13 83.8%（差 +29.0pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/MSTR_morning.json