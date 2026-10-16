# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
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
🔴 **事件差分**: 10-16（1D）ATM IV 77.4% vs 10-23 59.8%（差 +17.6pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-16 40C ΔOI +565（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 39.95 → 今开 38.80（-2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 39.66 ｜ 低 38.60

Options: P/C成交量 0.67 | OI比 0.56 | ATM IV 77.4% | Skew 10.2pp | Term 0.85 | ExpMove ±4.0%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价显著（Skew 10.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±4.0% ｜ 10-23（8D）±7.0% ｜ 10-30（15D）±10.8% ｜ 11-06（22D）±6.4%
   ⇒ IV–VIX Spread: +59.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,587,515 | GEX Change vs 上次快照 1,731,724 | Flip: Primary Flip: 43.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 278 / LOW 76 / INVALID 92
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 43.77（全链重定价，覆盖 98%）
最近结构参考: Flip 44（现价低于该位 11.0%）
量化视角： 负 Gamma（359万，无历史分位）｜负 Gamma 缓解（+173万）｜现价位于 Flip 下方 10.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 45（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 44（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 40.0C — Vol 842 | 最新价 $0.71 | OI 91→656 (ΔOI +565张) | ΔOI/Volume 67.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增565张（+620.9% vs前日OI），连续性待观察（方向未知）
10-23 42.0P — Vol 435 | 最新价 $3.03 | OI 100→520 (ΔOI +420张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增420张（+420.0% vs前日OI），连续性待观察（方向未知）
11-06 40.0C — Vol 397 | 最新价 $2.35 | OI 46→442 (ΔOI +396张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增396张（+860.9% vs前日OI），连续性待观察（方向未知）
11-06 35.0P — Vol 332 | 最新价 $0.77 | OI 74→400 (ΔOI +326张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增326张（+440.5% vs前日OI），连续性待观察（方向未知）
10-23 42.5P — Vol 271 | 最新价 $3.10 | OI 173→424 (ΔOI +251张) | ΔOI/Volume 92.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增251张（+145.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,958 张（Put 997 / Call 961），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +1.3k / P -2.8k ｜ Activity MEDIUM △ ｜ 1D
10-23  C +0.6k / P +1.1k ｜ Activity HIGH ｜ 8D
10-30  C +0.6k / P +0.5k ｜ Activity MEDIUM △ ｜ 15D
11-06  C +0.5k / P +0.6k ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 25.2k / P 14.2k，今日变化ΔOI: C +1.3k / P -2.8k，平值价格ATM: C $0.75 / P $0.80 ｜ ATM IV 77.4%，净 delta 敞口 315k shares
Top ΔOI: P 45 -817 ｜ C 40 +565 ｜ P 42 -422
仓位参考: Max Pain 45 ｜ Put Wall 40（+2.6%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 77.4%｜历史 Rank 68%（近端代理）｜IV/RV 1.63×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 315,049 股

📆 10-23 Forward Structure
存量OI: C 4.7k / P 3.6k，今日变化ΔOI: C +0.6k / P +1.1k，平值价格ATM: C $1.33 / P $1.39 ｜ ATM IV 59.8%，净 delta 敞口 -47k shares
Top ΔOI: P 42 +420 ｜ P 42 +251 ｜ P 38 +157
仓位参考: Max Pain 45 ｜ Call Wall 41（+5.2%，弱）（OI 0.1k） ｜ Put Wall 42（+7.8%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 59.8%｜历史 Rank 68%（近端代理）｜IV/RV 1.26×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 47,146 股

10-30（MEDIUM △）仓位参考: Max Pain 46 ｜ Put Wall 42（+7.8%，弱）（OI 0.4k）

📆 11-06 Forward Structure
存量OI: C 3.3k / P 3.0k，今日变化ΔOI: C +0.5k / P +0.6k，平值价格ATM: C $0.00 / P $2.50 ｜ ATM IV 69.8%，净 delta 敞口 9k shares
Top ΔOI: C 40 +396
仓位参考: Max Pain 45 ｜ Call Wall 40（+2.6%，弱）（OI 0.4k） ｜ Put Wall 38（-2.5%）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 69.8%｜历史 Rank 68%（近端代理）｜IV/RV 1.47×（近似）｜净 delta 敞口 正 8,894 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 77.4% vs 10-23 59.8%（差 +17.6pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/MP_morning.json