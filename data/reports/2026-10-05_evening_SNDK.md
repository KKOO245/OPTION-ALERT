# 期权晚报 2026-10-05（快照 16:51 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $756.20
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 1700C ΔOI +163（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,723.80 → 收盘 1,704.16（-1.1%） ｜ 今日高 1743.24 ｜ 低 1681.00 ｜ 昨收 1,719.99 → 收盘 1,704.16（-0.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-08，窗口结束前不做对错判定）

Options: P/C成交量 0.78 | OI比 1.09 | ATM IV 57.9% | Skew -2.0pp | Term 1.08 | ExpMove ±4.9%（近端） | Rank 15%
量化视角： IV 历史低位（Rank 15%，期权偏便宜）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -2.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（4D）±4.9% ｜ 10-16（11D）±7.9% ｜ 10-23（18D）±10.1% ｜ 10-30（25D）±13.2%
   ⇒ IV–VIX Spread: +42.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,132,621 | GEX Change vs 上次快照 -1,139,278 | Flip: Primary Flip: 1718.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1556 / LOW 394 / INVALID 1150
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1718.36（全链重定价，覆盖 100%）
最近结构参考: Flip 1718（现价低于该位 0.8%）
量化视角： 负 Gamma（113万，无历史分位）｜由正转负（114万）｜现价位于 Flip 下方 0.83%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,700（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1718（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 1000.0P — Vol 27 | 最新价 $0.09 | OI 705→1883 (ΔOI +1178张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1178张（+167.1% vs前日OI），连续性待观察（方向未知）
10-09 1850.0C — Vol 1,687 | 最新价 $6.08 | OI 503→1415 (ΔOI +912张) | ΔOI/Volume 54.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增912张（+181.3% vs前日OI），连续性待观察（方向未知）
10-09 1800.0C — Vol 2,769 | 最新价 $12.34 | OI 559→1391 (ΔOI +832张) | ΔOI/Volume 30.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增832张（+148.8% vs前日OI），连续性待观察（方向未知）
10-09 1695.0P — Vol 402 | 最新价 $36.50 | OI 44→595 (ΔOI +551张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增551张（+1252.3% vs前日OI），连续性待观察（方向未知）
10-09 1500.0P — Vol 1,383 | 最新价 $1.44 | OI 582→1105 (ΔOI +523张) | ΔOI/Volume 37.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增523张（+89.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,996 张（Put 2,252 / Call 1,744），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +8.8k / P +8.9k ｜ Activity HIGH ｜ 4D
10-16  C +1.3k / P +0.8k ｜ Activity MEDIUM △ ｜ 11D
10-23  C +1.2k / P +0.9k ｜ Activity HIGH ｜ 18D
10-30  C +0.5k / P +0.7k ｜ Activity HIGH ｜ 25D

📆 10-09 Forward Structure
存量OI: C 26.2k / P 28.6k，今日变化ΔOI: C +8.8k / P +8.9k，平值价格ATM: C $41.80 / P $41.32 ｜ ATM IV 57.9%，净 delta 敞口 -24k shares
Top ΔOI: C 1850 +912 ｜ C 1800 +832
仓位参考: Max Pain 1,700 ｜ Call Wall 1850（+8.6%，弱）（OI 1.4k） ｜ Put Wall 1800（+5.6%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 57.9%｜历史 Rank 15%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 23,800 股

10-16（MEDIUM △）Top ΔOI: 1700C +163
10-16（MEDIUM △）仓位参考: Max Pain 1,670 ｜ Call Wall 1800（+5.6%，弱）（OI 1.2k） ｜ Put Wall 1600（-6.1%，弱）（OI 1.3k）

📆 10-23 Forward Structure
存量OI: C 7.7k / P 8.8k，今日变化ΔOI: C +1.2k / P +0.9k，平值价格ATM: C $86.40 / P $85.19 ｜ ATM IV 57.7%，净 delta 敞口 21k shares
Top ΔOI: C 1850 +167 ｜ P 1420 +111 ｜ C 1750 +105
仓位参考: Max Pain 1,725 ｜ Call Wall 1800（+5.6%，弱）（OI 0.3k） ｜ Put Wall 1650（-3.2%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 57.7%｜历史 Rank 15%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 20,720 股

📆 10-30 Forward Structure
存量OI: C 4.7k / P 8.1k，今日变化ΔOI: C +0.5k / P +0.7k，平值价格ATM: C $115.11 / P $109.32 ｜ ATM IV 62.7%，净 delta 敞口 4k shares
Top ΔOI: P 1500 +73 ｜ C 1870 +59
仓位参考: Max Pain 1,720 ｜ Call Wall 1800（+5.6%，弱）（OI 0.2k） ｜ Put Wall 1600（-6.1%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 62.7%｜历史 Rank 15%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 4,404 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=40 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=40）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/SNDK_evening.json