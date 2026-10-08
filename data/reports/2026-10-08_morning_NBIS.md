# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $774.21 ｜ QQQ $747.58
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-09 225P ΔOI -3,202（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 237.15 → 今开 233.13（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 234.15 ｜ 低 225.22

Options: P/C成交量 0.38 | OI比 0.86 | ATM IV 77.4% | Skew -2.2pp | Term 0.92 | ExpMove ±3.6%（近端） | Rank 9%
量化视角： IV 历史低位（Rank 9%，期权偏便宜）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.6% ｜ 10-16（8D）±8.2% ｜ 10-23（15D）±10.5% ｜ 10-30（22D）±13.5%
   ⇒ IV–VIX Spread: +61.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,221,298 | GEX Change vs 上次快照 -16,490,431 | Flip: Primary Flip: 232.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 471 / LOW 59 / INVALID 162
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 232.80（全链重定价，覆盖 99%）
Put Wall 220（弱结构｜现价高于该位 3.1%）
最近结构参考: Flip 233（现价低于该位 2.6%）
量化视角： 负 Gamma（1322万，无历史分位）｜由正转负（1649万）｜现价位于 Flip 下方 2.61%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构）；上方 238（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 233（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 250.0C — Vol 9,246 | 最新价 $5.80 | OI 7112→9313 (ΔOI +2201张) | ΔOI/Volume 23.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2201张（+30.9% vs前日OI），连续性待观察（方向未知）
10-16 220.0P — Vol 2,493 | 最新价 $3.45 | OI 5876→7793 (ΔOI +1917张) | ΔOI/Volume 76.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1917张（+32.6% vs前日OI），连续性待观察（方向未知）
10-16 230.0P — Vol 1,930 | 最新价 $6.65 | OI 3036→4092 (ΔOI +1056张) | ΔOI/Volume 54.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1056张（+34.8% vs前日OI），连续性待观察（方向未知）
10-16 260.0C — Vol 1,890 | 最新价 $3.55 | OI 3204→4236 (ΔOI +1032张) | ΔOI/Volume 54.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1032张（+32.2% vs前日OI），连续性待观察（方向未知）
10-09 250.0C — Vol 5,888 | 最新价 $1.50 | OI 2939→3945 (ΔOI +1006张) | ΔOI/Volume 17.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1006张（+34.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,212 张（Put 2,973 / Call 4,239），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +4.7k / P -3.3k ｜ Activity HIGH ｜ 1D
10-16  C +4.8k / P +5.2k ｜ Activity HIGH ｜ 8D
10-23  C +2.4k / P +1.4k ｜ Activity MEDIUM △ ｜ 15D
10-30  C +0.9k / P +2.5k ｜ Activity HIGH ｜ 22D

📆 10-09 Forward Structure
存量OI: C 58.7k / P 50.5k，今日变化ΔOI: C +4.7k / P -3.3k，平值价格ATM: C $4.10 / P $4.09 ｜ ATM IV 77.4%，净 delta 敞口 268k shares
Top ΔOI: P 225 -3,202 ｜ C 237 +938
仓位参考: Max Pain 238 ｜ Call Wall 242.5（+7.0%，弱）（OI 3.8k） ｜ Put Wall 225（-0.8%，弱）（OI 5.9k）
量化解读： 存量两侧均衡｜ATM IV 77.4%｜历史 Rank 9%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 267,693 股

📆 10-16 Forward Structure
存量OI: C 95.9k / P 105.7k，今日变化ΔOI: C +4.8k / P +5.2k，平值价格ATM: C $8.93 / P $9.77 ｜ ATM IV 68.7%，净 delta 敞口 -15k shares
Top ΔOI: C 270 -2,275 ｜ C 250 +2,201 ｜ P 220 +1,917
仓位参考: Max Pain 228 ｜ Call Wall 240（+5.9%，弱）（OI 6.0k） ｜ Put Wall 220（-3.0%，弱）（OI 7.8k）
量化解读： 存量两侧均衡｜ATM IV 68.7%｜历史 Rank 9%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 负 15,095 股

10-23（MEDIUM △）Top ΔOI: 240C +638 ｜ 245C +557
10-23（MEDIUM △）仓位参考: Max Pain 225 ｜ Call Wall 240（+5.9%，弱）（OI 1.0k） ｜ Put Wall 225（-0.8%，弱）（OI 0.7k）

📆 10-30 Forward Structure
存量OI: C 18.3k / P 15.3k，今日变化ΔOI: C +0.9k / P +2.5k，平值价格ATM: C $16.20 / P $14.34 ｜ ATM IV 70.2%，净 delta 敞口 -27k shares
Top ΔOI: P 200 +715 ｜ C 300 +712 ｜ C 320 -550
仓位参考: Max Pain 235 ｜ Call Wall 235（+3.6%，弱）（OI 0.6k） ｜ Put Wall 215（-5.2%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.2%｜历史 Rank 9%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 负 27,141 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 77.4% vs 10-16 68.7%（差 +8.7pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/NBIS_morning.json