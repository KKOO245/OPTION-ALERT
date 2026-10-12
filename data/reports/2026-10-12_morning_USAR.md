# 期权晨报 2026-10-12（快照 10:20 ET）

📊 市场环境

SPY $778.43 ｜ QQQ $745.68
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


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 12.56 → 今开 12.36（-1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 12.45 ｜ 低 12.03

Options: P/C成交量 0.21 | OI比 0.32 | ATM IV 69.1% | Skew -4.3pp | Term 1.11 | ExpMove ±6.1%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常（Term 1.11）｜Put 保护异常便宜（Skew -4.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.32）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.21×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.32×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（4D）±6.1% ｜ 10-23（11D）±10.4% ｜ 10-30（18D）±11.9% ｜ 11-06（25D）±14.8%
   ⇒ IV–VIX Spread: +53.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,649,372 | GEX Change vs 上次快照 341,815 | Flip: Primary Flip: 13.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 155 / LOW 79 / INVALID 140
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 13.61（全链重定价，覆盖 100%）
最近结构参考: Flip 14（现价低于该位 11.4%）
量化视角： 负 Gamma（165万，无历史分位）｜负 Gamma 缓解（+34万）｜现价位于 Flip 下方 11.41%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 13.0C — Vol 1,956 | 最新价 $0.25 | OI 665→1326 (ΔOI +661张) | ΔOI/Volume 33.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增661张（+99.4% vs前日OI），连续性待观察（方向未知）
10-16 12.5P — Vol 491 | 最新价 $0.38 | OI 690→1017 (ΔOI +327张) | ΔOI/Volume 66.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增327张（+47.4% vs前日OI），连续性待观察（方向未知）
10-16 12.0P — Vol 533 | 最新价 $0.15 | OI 429→679 (ΔOI +250张) | ΔOI/Volume 46.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增250张（+58.3% vs前日OI），连续性待观察（方向未知）
10-23 13.5P — Vol 246 | 最新价 $1.16 | OI 504→749 (ΔOI +245张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增245张（+48.6% vs前日OI），连续性待观察（方向未知）
10-16 13.0P — Vol 427 | 最新价 $0.66 | OI 1681→1922 (ΔOI +241张) | ΔOI/Volume 56.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增241张（+14.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,724 张（Put 1,063 / Call 661），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +1.0k / P +0.2k ｜ Activity HIGH ｜ 4D
10-23  C +0.3k / P +0.2k ｜ Activity MEDIUM △ ｜ 11D
10-30  C +0.4k / P +15 ｜ Activity MEDIUM △ ｜ 18D
11-06  C +0.2k / P +0.6k ｜ Activity HIGH ｜ 25D

📆 10-16 Forward Structure
存量OI: C 52.1k / P 16.5k，今日变化ΔOI: C +1.0k / P +0.2k，平值价格ATM: C $0.44 / P $0.30 ｜ ATM IV 69.1%，净 delta 敞口 43k shares
Top ΔOI: C 13 +661 ｜ P 15 -349 ｜ P 12 +327
仓位参考: Max Pain 15 ｜ Put Wall 13（+7.8%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 69.1%｜历史 Rank 5%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 正 43,424 股

10-23（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 12（-0.5%，弱）（OI 0.4k）

10-30（MEDIUM △）Top ΔOI: 13C +93
10-30（MEDIUM △）仓位参考: Max Pain 15 ｜ Call Wall 12.5（+3.6%，弱）（OI 0.2k） ｜ Put Wall 12.5（+3.6%，弱）（OI 1.3k）

📆 11-06 Forward Structure
存量OI: C 1.8k / P 3.3k，今日变化ΔOI: C +0.2k / P +0.6k，平值价格ATM: C $0.98 / P $0.80 ｜ ATM IV 72.2%，净 delta 敞口 -39k shares
Top ΔOI: P 15 +183 ｜ P 13 +104
仓位参考: Max Pain 16 ｜ Call Wall 13（+7.8%，弱）（OI 0.2k） ｜ Put Wall 13（+7.8%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 72.2%｜历史 Rank 5%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 负 38,703 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=45 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=45）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/USAR_morning.json