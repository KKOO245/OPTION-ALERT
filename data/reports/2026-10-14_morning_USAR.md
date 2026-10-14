# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $769.08 ｜ QQQ $728.95
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔵 **期限 OI 集中**: 11-06 18C ΔOI +999 占该期限总 OI 12.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 11.28 → 今开 10.89（-3.5%） | 较昨收变动（含盘初走势） ｜ 今日高 11.07 ｜ 低 10.60

Options: P/C成交量 0.33 | OI比 0.25 | ATM IV 76.5% | Skew -3.8pp | Term 1.08 | ExpMove ±5.3%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -3.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.33×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.25×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±5.3% ｜ 10-23（9D）±9.3% ｜ 10-30（16D）±19.3% ｜ 11-06（23D）±14.1%
   ⇒ IV–VIX Spread: +60.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 53,272 | GEX Change vs 上次快照 2,127,427 | Flip: Primary Flip: 10.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 152 / LOW 101 / INVALID 125
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 10.65（全链重定价，覆盖 95%）
最近结构参考: Flip 11（现价高于该位 0.3%）
量化视角： 正 Gamma（5万，无历史分位）｜由负转正（+213万）｜现价位于 Flip 上方 0.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 18.0C — Vol 1,010 | 最新价 $0.04 | OI 154→1153 (ΔOI +999张) | ΔOI/Volume 98.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增999张（+648.7% vs前日OI），连续性待观察（方向未知）
11-06 9.0P — Vol 816 | 最新价 $0.10 | OI 20→815 (ΔOI +795张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增795张（+3975.0% vs前日OI），连续性待观察（方向未知）
10-16 11.5C — Vol 899 | 最新价 $0.22 | OI 69→572 (ΔOI +503张) | ΔOI/Volume 56.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增503张（+729.0% vs前日OI），连续性待观察（方向未知）
10-16 12.0C — Vol 1,923 | 最新价 $0.08 | OI 580→1082 (ΔOI +502张) | ΔOI/Volume 26.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增502张（+86.5% vs前日OI），连续性待观察（方向未知）
10-16 11.0C — Vol 559 | 最新价 $0.46 | OI 119→607 (ΔOI +488张) | ΔOI/Volume 87.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增488张（+410.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,287 张（Put 795 / Call 2,492），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +1.6k / P -2.2k ｜ Activity MEDIUM △ ｜ 2D
10-23  C +0.8k / P -0.1k ｜ Activity HIGH ｜ 9D
10-30  C +0.6k / P +60 ｜ Activity MEDIUM △ ｜ 16D
11-06  C +1.3k / P +1.2k ｜ Activity HIGH ｜ 23D

📆 10-16 Forward Structure
存量OI: C 56.6k / P 14.1k，今日变化ΔOI: C +1.6k / P -2.2k，平值价格ATM: C $0.42 / P $0.15 ｜ ATM IV 76.5%，净 delta 敞口 279k shares
Top ΔOI: P 15 -746 ｜ P 14 -528 ｜ P 13 -508
仓位参考: Max Pain 14
量化解读： 存量 Call 重｜ATM IV 76.5%｜历史 Rank 10%（近端代理）｜IV/RV 1.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 279,081 股

📆 10-23 Forward Structure
存量OI: C 14.0k / P 4.9k，今日变化ΔOI: C +0.8k / P -0.1k，平值价格ATM: C $0.67 / P $0.32 ｜ ATM IV 70.1%，净 delta 敞口 52k shares
Top ΔOI: C 11 +290 ｜ P 15 -172
仓位参考: Max Pain 14 ｜ Put Wall 10（-6.4%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 70.1%｜历史 Rank 10%（近端代理）｜IV/RV 1.78×（近似）｜净 delta 敞口 正 52,295 股

10-30（MEDIUM △）Top ΔOI: 13P -354 ｜ 10P +258
10-30（MEDIUM △）仓位参考: Max Pain 14

📆 11-06 Forward Structure
存量OI: C 3.4k / P 4.8k，今日变化ΔOI: C +1.3k / P +1.2k，平值价格ATM: C $0.82 / P $0.69 ｜ ATM IV 72.1%，净 delta 敞口 -12k shares
Top ΔOI: P 11 +201
仓位参考: Max Pain 15 ｜ Put Wall 10（-6.4%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 72.1%｜历史 Rank 10%（近端代理）｜IV/RV 1.83×（近似）｜净 delta 敞口 负 12,152 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 76.5% vs 10-23 70.1%（差 +6.4pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/USAR_morning.json