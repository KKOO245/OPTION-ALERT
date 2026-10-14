# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $771.45 ｜ QQQ $732.63
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
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
🔴 **事件差分**: 10-16（2D）ATM IV 85.2% vs 10-23 68.3%（差 +16.9pp），覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-16 14C ΔOI +71（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 14.35 → 今开 13.91（-3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 13.99 ｜ 低 13.45

Options: P/C成交量 0.77 | OI比 0.20 | ATM IV 85.2% | Skew 10.3pp | Term 0.82 | ExpMove ±8.6%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 10.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.20×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±8.6% ｜ 10-23（9D）±8.8% ｜ 10-30（16D）±12.6% ｜ 11-06（23D）±19.4%
   ⇒ IV–VIX Spread: +69.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -218,710 | GEX Change vs 上次快照 -165,497 | Flip: Primary Flip: 14.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 179 / LOW 106 / INVALID 119
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 14.15（全链重定价，覆盖 96%）
Put Wall 14（弱结构｜现价低于该位 3.3%）
最近结构参考: Put Wall 14（现价低于该位 3.3%）
量化视角： 负 Gamma（22万，无历史分位）｜负 Gamma 加深（17万）｜现价位于 Flip 下方 4.28%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall，弱结构） / 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 14.5C — Vol 253 | 最新价 $0.33 | OI 108→274 (ΔOI +166张) | ΔOI/Volume 65.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增166张（+153.7% vs前日OI），连续性待观察（方向未知）
10-16 14.0C — Vol 139 | 最新价 $0.61 | OI 17→88 (ΔOI +71张) | ΔOI/Volume 51.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增71张（+417.6% vs前日OI），连续性待观察（方向未知）
10-16 15.0C — Vol 159 | 最新价 $0.18 | OI 310→377 (ΔOI +67张) | ΔOI/Volume 42.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增67张（+21.6% vs前日OI），连续性待观察（方向未知）
10-23 14.5C — Vol 56 | 最新价 $0.61 | OI 53→105 (ΔOI +52张) | ΔOI/Volume 92.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52张（+98.1% vs前日OI），连续性待观察（方向未知）
10-16 13.5P — Vol 53 | 最新价 $0.21 | OI 58→102 (ΔOI +44张) | ΔOI/Volume 83.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44张（+75.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 400 张（Put 44 / Call 356），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.3k / P +34 ｜ Activity MEDIUM △ ｜ 2D
10-23  C +58 / P +48 ｜ Activity MEDIUM △ ｜ 9D
10-30  C +51 / P +7 ｜ Activity MEDIUM △ ｜ 16D
11-06  C +29 / P +17 ｜ Activity MEDIUM △ ｜ 23D

📆 10-16 Forward Structure
存量OI: C 22.7k / P 4.6k，今日变化ΔOI: C +0.3k / P +34，平值价格ATM: C $0.95 / P $0.21 ｜ ATM IV 85.2%，净 delta 敞口 19k shares
Top ΔOI: C 14 +166 ｜ C 14 +71
仓位参考: Max Pain 17 ｜ Put Wall 14（+3.4%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 85.2%｜历史 Rank 17%（近端代理）｜IV/RV 1.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,896 股

10-23（MEDIUM △）Top ΔOI: 14C +52
10-23（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 14（+3.4%）（OI 0.6k）

10-30（MEDIUM △）Top ΔOI: 13C +13
10-30（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 14（+3.4%）（OI 0.3k）

11-06（MEDIUM △）Top ΔOI: 13P +14 ｜ 14C +7
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（-4.0%，弱）（OI 24）

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 85.2% vs 10-23 68.3%（差 +16.9pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/NNE_morning.json