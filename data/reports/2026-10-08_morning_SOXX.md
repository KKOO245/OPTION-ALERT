# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $775.90 ｜ QQQ $755.85
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
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
🟡 **近现价集中开仓**: 10-09 572P ΔOI +755（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 582.82 → 今开 573.00（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 575.68 ｜ 低 568.05

Options: P/C成交量 1.77 | OI比 2.05 | ATM IV 38.8% | Skew 3.3pp | Term 0.94 | ExpMove ±2.5%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 3.3pp）｜当日成交偏 Put（P/C量 1.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.77×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.05×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.5% ｜ 10-16（8D）±4.0% ｜ 10-23（15D）±5.6% ｜ 10-30（22D）±7.1%
   ⇒ IV–VIX Spread: +23.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,965,607 | GEX Change vs 上次快照 -10,166,121 | Flip: Primary Flip: 580.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 550 / LOW 297 / INVALID 699
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 580.33（全链重定价，覆盖 92%）
Call Wall 600（现价低于该位 4.8%）
最近结构参考: Flip 580（现价低于该位 1.6%）
量化视角： 负 Gamma（697万，无历史分位）｜由正转负（1017万）｜现价位于 Flip 下方 1.59%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 570（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 580（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 550.0P — Vol 1,513 | 最新价 $2.45 | OI 419→1836 (ΔOI +1417张) | ΔOI/Volume 93.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1417张（+338.2% vs前日OI），连续性待观察（方向未知）
10-16 540.0P — Vol 1,016 | 最新价 $1.77 | OI 472→1318 (ΔOI +846张) | ΔOI/Volume 83.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增846张（+179.2% vs前日OI），连续性待观察（方向未知）
10-09 572.5P — Vol 762 | 最新价 $2.14 | OI 51→806 (ΔOI +755张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增755张（+1480.4% vs前日OI），连续性待观察（方向未知）
10-30 520.0P — Vol 507 | 最新价 $3.80 | OI 54→544 (ΔOI +490张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增490张（+907.4% vs前日OI），连续性待观察（方向未知）
10-30 610.0C — Vol 214 | 最新价 $10.10 | OI 48→249 (ΔOI +201张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增201张（+418.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,709 张（Put 3,508 / Call 201），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.3k / P +1.1k ｜ Activity MEDIUM △ ｜ 1D
10-16  C -2.2k / P +1.5k ｜ Activity MEDIUM △ ｜ 8D
10-23  C -11 / P +0.4k ｜ Activity MEDIUM △ ｜ 15D
10-30  C +0.2k / P +0.7k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 5.9k / P 12.2k，今日变化ΔOI: C +0.3k / P +1.1k，平值价格ATM: C $10.60 / P $3.54 ｜ ATM IV 38.8%，净 delta 敞口 -9k shares
Top ΔOI: P 572 +755 ｜ P 577 -310 ｜ C 600 +164
仓位参考: Max Pain 570 ｜ Call Wall 600（+5.1%，弱）（OI 0.4k） ｜ Put Wall 555（-2.8%）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 38.8%｜历史 Rank 66%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,712 股

10-16（MEDIUM △）Top ΔOI: 600C -1,716 ｜ 550P +1,417
10-16（MEDIUM △）仓位参考: Max Pain 535 ｜ Call Wall 600（+5.1%）（OI 7.0k）

10-23（MEDIUM △）Top ΔOI: 567P +198 ｜ 565P +136
10-23（MEDIUM △）仓位参考: Max Pain 560 ｜ Call Wall 555（-2.8%，弱）（OI 91）

10-30（MEDIUM △）Top ΔOI: 520P +490 ｜ 610C +201
10-30（MEDIUM △）仓位参考: Max Pain 560 ｜ Put Wall 550（-3.7%，弱）（OI 3.2k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 38.8% vs 10-16 33.3%（差 +5.5pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/SOXX_morning.json