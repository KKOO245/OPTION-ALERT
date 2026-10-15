# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $767.19 ｜ QQQ $720.56
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 10.32 → 今开 9.89（-4.2%） | 较昨收变动（含盘初走势） ｜ 今日高 10.17 ｜ 低 9.82

Options: P/C成交量 0.29 | OI比 0.22 | ATM IV 88.7% | Skew 6.9pp | Term 0.93 | ExpMove ±4.5%（近端） | Rank 19%
量化视角： IV 历史低位（Rank 19%，期权偏便宜）｜期限结构正常（Term 0.93）｜保护溢价显著（Skew 6.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.22）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.22×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±4.5% ｜ 10-23（8D）±8.7% ｜ 10-30（15D）±12.9% ｜ 11-06（22D）±16.8%
   ⇒ IV–VIX Spread: +71.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -795,001 | GEX Change vs 上次快照 1,266,453 | Flip: Primary Flip: 10.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 190 / LOW 101 / INVALID 121
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 10.26（全链重定价，覆盖 99%）
最近结构参考: Flip 10（现价低于该位 3.3%）
量化视角： 负 Gamma（80万，无历史分位）｜负 Gamma 缓解（+127万）｜现价位于 Flip 下方 3.26%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 13（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 11.0C — Vol 2,642 | 最新价 $0.06 | OI 607→2535 (ΔOI +1928张) | ΔOI/Volume 73.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1928张（+317.6% vs前日OI），连续性待观察（方向未知）
10-23 9.5P — Vol 1,128 | 最新价 $0.21 | OI 0→1063 (ΔOI +1063张) | ΔOI/Volume 94.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1063张（前日OI缺失），连续性待观察（方向未知）
10-23 11.0C — Vol 975 | 最新价 $0.25 | OI 44→868 (ΔOI +824张) | ΔOI/Volume 84.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增824张（+1872.7% vs前日OI），连续性待观察（方向未知）
11-06 9.0P — Vol 743 | 最新价 $0.29 | OI 815→1525 (ΔOI +710张) | ΔOI/Volume 95.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增710张（+87.1% vs前日OI），连续性待观察（方向未知）
10-16 11.5C — Vol 1,190 | 最新价 $0.03 | OI 572→1152 (ΔOI +580张) | ΔOI/Volume 48.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增580张（+101.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,105 张（Put 1,773 / Call 3,332），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +2.6k / P -1.0k ｜ Activity HIGH ｜ 1D
10-23  C +1.9k / P +1.1k ｜ Activity HIGH ｜ 8D
10-30  C +0.6k / P +0.3k ｜ Activity MEDIUM △ ｜ 15D
11-06  C +0.2k / P +0.6k ｜ Activity MEDIUM △ ｜ 22D

📆 10-16 Forward Structure
存量OI: C 59.2k / P 13.1k，今日变化ΔOI: C +2.6k / P -1.0k，平值价格ATM: C $0.17 / P $0.28 ｜ ATM IV 88.7%，净 delta 敞口 162k shares
Top ΔOI: P 13 -671
仓位参考: Max Pain 13
量化解读： 存量 Call 重｜ATM IV 88.7%｜历史 Rank 19%（近端代理）｜IV/RV 1.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 162,176 股

📆 10-23 Forward Structure
存量OI: C 15.8k / P 5.9k，今日变化ΔOI: C +1.9k / P +1.1k，平值价格ATM: C $0.41 / P $0.45 ｜ ATM IV 80.5%，净 delta 敞口 36k shares
Top ΔOI: P 9 +1,063
仓位参考: Max Pain 12 ｜ Put Wall 9.5（-4.3%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 80.5%｜历史 Rank 19%（近端代理）｜IV/RV 1.76×（近似）｜净 delta 敞口 正 36,197 股

10-30（MEDIUM △）Top ΔOI: 10P +317 ｜ 9P +208
10-30（MEDIUM △）仓位参考: Max Pain 14

11-06（MEDIUM △）Top ΔOI: 9P +710 ｜ 10P +119
11-06（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 9（-9.4%）（OI 1.5k）

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 88.7% vs 10-23 80.5%（差 +8.2pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/USAR_morning.json