# 期权晨报 2026-10-12（快照 10:20 ET）

📊 市场环境

SPY $778.00 ｜ QQQ $745.63
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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-16 265P ΔOI +569（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 280.50 → 今开 275.33（-1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 275.74 ｜ 低 264.58

Options: P/C成交量 0.68 | OI比 1.12 | ATM IV 70.8% | Skew 0.9pp | Term 1.07 | ExpMove ±6.2%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常（Term 1.07）｜保护溢价薄（Skew 0.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（4D）±6.2% ｜ 10-23（11D）±13.0% ｜ 10-30（18D）±14.4% ｜ 11-06（25D）±15.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 621,589 | GEX Change vs 上次快照 -5,426,475 | Flip: Primary Flip: 266.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 582 / LOW 95 / INVALID 165
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 266.32（全链重定价，覆盖 99%）
最近结构参考: Flip 266（现价高于该位 0.3%）
量化视角： 正 Gamma（62万，无历史分位）｜正 Gamma 减弱（543万）｜现价位于 Flip 上方 0.33%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 270（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 266（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 320.0C — Vol 724 | 最新价 $7.50 | OI 925→1623 (ΔOI +698张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增698张（+75.5% vs前日OI），连续性待观察（方向未知）
10-23 155.0P — Vol 635 | 最新价 $0.04 | OI 205→777 (ΔOI +572张) | ΔOI/Volume 90.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增572张（+279.0% vs前日OI），连续性待观察（方向未知）
10-16 265.0P — Vol 1,292 | 最新价 $3.80 | OI 1374→1943 (ΔOI +569张) | ΔOI/Volume 44.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增569张（+41.4% vs前日OI），连续性待观察（方向未知）
10-23 322.5C — Vol 521 | 最新价 $2.35 | OI 2→390 (ΔOI +388张) | ΔOI/Volume 74.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增388张（+19400.0% vs前日OI），连续性待观察（方向未知）
10-16 300.0C — Vol 2,277 | 最新价 $3.25 | OI 4897→5266 (ΔOI +369张) | ΔOI/Volume 16.2% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增369张（+7.5% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,596 张（Put 1,141 / Call 1,455），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +2.3k / P +2.8k ｜ Activity HIGH ｜ 4D
10-23  C +1.8k / P +1.4k ｜ Activity HIGH ｜ 11D
10-30  C +0.8k / P +0.2k ｜ Activity HIGH ｜ 18D
11-06  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 25D

📆 10-16 Forward Structure
存量OI: C 89.0k / P 99.6k，今日变化ΔOI: C +2.3k / P +2.8k，平值价格ATM: C $8.00 / P $8.50 ｜ ATM IV 70.8%，净 delta 敞口 -149k shares
Top ΔOI: P 265 +569
仓位参考: Max Pain 270 ｜ Call Wall 270（+1.0%，弱）（OI 6.9k） ｜ Put Wall 260（-2.7%，弱）（OI 4.8k）
量化解读： 存量两侧均衡｜ATM IV 70.8%｜历史 Rank 26%（近端代理）｜IV/RV 0.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 148,510 股

📆 10-23 Forward Structure
存量OI: C 16.9k / P 19.5k，今日变化ΔOI: C +1.8k / P +1.4k，平值价格ATM: C $17.56 / P $17.20 ｜ ATM IV 91.6%，净 delta 敞口 26k shares
Top ΔOI: C 322 +388 ｜ C 282 +246
仓位参考: Max Pain 270 ｜ Call Wall 280（+4.8%，弱）（OI 1.0k） ｜ Put Wall 250（-6.4%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 91.6%｜历史 Rank 26%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,378 股

📆 10-30 Forward Structure
存量OI: C 11.6k / P 20.1k，今日变化ΔOI: C +0.8k / P +0.2k，平值价格ATM: C $19.70 / P $18.79 ｜ ATM IV 82.5%，净 delta 敞口 10k shares
Top ΔOI: C 320 +698 ｜ P 265 +129
仓位参考: Max Pain 280 ｜ Call Wall 280（+4.8%，弱）（OI 0.7k） ｜ Put Wall 285（+6.7%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 82.5%｜历史 Rank 26%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,464 股

11-06（MEDIUM △）Top ΔOI: 300C +81
11-06（MEDIUM △）仓位参考: Max Pain 275 ｜ Call Wall 290（+8.5%，弱）（OI 0.2k） ｜ Put Wall 250（-6.4%，弱）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/BE_morning.json