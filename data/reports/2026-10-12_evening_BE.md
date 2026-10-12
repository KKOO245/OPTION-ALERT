# 期权晚报 2026-10-12（快照 16:40 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-16 265P ΔOI +569（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 275.33 → 收盘 262.28（-4.7%） ｜ 今日高 275.74 ｜ 低 257.78 ｜ 昨收 280.50 → 收盘 262.28（-6.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-15，窗口结束前不做对错判定）

Options: P/C成交量 0.75 | OI比 1.12 | ATM IV 73.1% | Skew -0.3pp | Term 1.02 | ExpMove ±6.1%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（4D）±6.1% ｜ 10-23（11D）±12.3% ｜ 10-30（18D）±13.8% ｜ 11-06（25D）±16.5%
   ⇒ IV–VIX Spread: +57.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,773,052 | GEX Change vs 上次快照 -3,394,641 | Flip: Primary Flip: 266.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 602 / LOW 85 / INVALID 155
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 266.31（全链重定价，覆盖 99%）
Put Wall 240（弱结构｜现价高于该位 9.3%）
最近结构参考: Flip 266（现价低于该位 1.5%）
量化视角： 负 Gamma（277万，无历史分位）｜由正转负（339万）｜现价位于 Flip 下方 1.51%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 240（Put Wall，弱结构）；上方 270（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 266（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 320.0C — Vol 812 | 最新价 $4.35 | OI 925→1623 (ΔOI +698张) | ΔOI/Volume 86.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增698张（+75.5% vs前日OI），连续性待观察（方向未知）
10-23 155.0P — Vol 93 | 最新价 $0.07 | OI 205→777 (ΔOI +572张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增572张（+279.0% vs前日OI），连续性待观察（方向未知）
10-16 265.0P — Vol 1,676 | 最新价 $9.00 | OI 1374→1943 (ΔOI +569张) | ΔOI/Volume 34.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增569张（+41.4% vs前日OI），连续性待观察（方向未知）
10-23 322.5C — Vol 32 | 最新价 $1.90 | OI 2→390 (ΔOI +388张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增388张（+19400.0% vs前日OI），值得跟踪（方向未知）
10-16 300.0C — Vol 3,140 | 最新价 $0.52 | OI 4897→5266 (ΔOI +369张) | ΔOI/Volume 11.8% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增369张（+7.5% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,596 张（Put 1,141 / Call 1,455），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +2.3k / P +2.8k ｜ Activity MEDIUM △ ｜ 4D
10-23  C +1.8k / P +1.4k ｜ Activity HIGH ｜ 11D
10-30  C +0.8k / P +0.2k ｜ Activity HIGH ｜ 18D
11-06  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 25D

📆 10-16 Forward Structure
存量OI: C 89.0k / P 99.6k，今日变化ΔOI: C +2.3k / P +2.8k，平值价格ATM: C $8.20 / P $7.88 ｜ ATM IV 73.1%，净 delta 敞口 -174k shares
Top ΔOI: P 265 +569
仓位参考: Max Pain 270 ｜ Call Wall 270（+2.9%，弱）（OI 6.9k） ｜ Put Wall 260（-0.9%，弱）（OI 4.8k）
量化解读： 存量两侧均衡｜ATM IV 73.1%｜历史 Rank 31%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 174,146 股

📆 10-23 Forward Structure
存量OI: C 16.9k / P 19.5k，今日变化ΔOI: C +1.8k / P +1.4k，平值价格ATM: C $15.98 / P $16.25 ｜ ATM IV 86.2%，净 delta 敞口 17k shares
Top ΔOI: C 322 +388 ｜ C 282 +246
仓位参考: Max Pain 270 ｜ Call Wall 280（+6.8%，弱）（OI 1.0k） ｜ Put Wall 240（-8.5%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 86.2%｜历史 Rank 31%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,549 股

📆 10-30 Forward Structure
存量OI: C 11.6k / P 20.1k，今日变化ΔOI: C +0.8k / P +0.2k，平值价格ATM: C $17.50 / P $18.62 ｜ ATM IV 81.0%，净 delta 敞口 7k shares
Top ΔOI: C 320 +698 ｜ P 265 +129
仓位参考: Max Pain 280 ｜ Call Wall 280（+6.8%，弱）（OI 0.7k） ｜ Put Wall 285（+8.7%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 81.0%｜历史 Rank 31%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,952 股

11-06（MEDIUM △）Top ΔOI: 300C +81
11-06（MEDIUM △）仓位参考: Max Pain 275 ｜ Call Wall 240（-8.5%，弱）（OI 0.2k） ｜ Put Wall 240（-8.5%，弱）（OI 2.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=45 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=45）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/BE_evening.json