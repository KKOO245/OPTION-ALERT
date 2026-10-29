# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $765.98 ｜ QQQ $715.34
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 10-30（1D）ATM IV 62.3% vs 11-02 44.6%（差 +17.7pp），覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 150C ΔOI +6,114（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 145.23 → 今开 142.30（-2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 144.53 ｜ 低 141.03

Options: P/C成交量 0.52 | OI比 0.72 | ATM IV 62.3% | Skew 0.5pp | Term 0.79 | ExpMove ±2.9%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价薄（Skew 0.5pp）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.9% ｜ 11-02（4D）±3.9% ｜ 11-04（6D）±5.4% ｜ 11-06（8D）±6.2%
   ⇒ IV–VIX Spread: +45.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -53,334,922 | GEX Change vs 上次快照 1,131,662 | Flip: Primary Flip: 147.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 739 / LOW 127 / INVALID 564
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 147.31（全链重定价，覆盖 100%）
Put Wall 140（弱结构｜现价高于该位 2.9%）
最近结构参考: Flip 147（现价低于该位 2.2%）
量化视角： 负 Gamma（5333万，无历史分位）｜负 Gamma 缓解（+113万）｜现价位于 Flip 下方 2.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 150.0C — Vol 40,439 | 最新价 $0.88 | OI 13571→19685 (ΔOI +6114张) | ΔOI/Volume 15.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6114张（+45.0% vs前日OI），连续性待观察（方向未知）
10-30 140.0P — Vol 18,083 | 最新价 $0.77 | OI 9821→14217 (ΔOI +4396张) | ΔOI/Volume 24.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4396张（+44.8% vs前日OI），连续性待观察（方向未知）
11-06 160.0C — Vol 8,085 | 最新价 $0.75 | OI 5800→10134 (ΔOI +4334张) | ΔOI/Volume 53.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4334张（+74.7% vs前日OI），连续性待观察（方向未知）
11-06 170.0C — Vol 7,120 | 最新价 $0.25 | OI 6068→9534 (ΔOI +3466张) | ΔOI/Volume 48.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3466张（+57.1% vs前日OI），连续性待观察（方向未知）
10-30 145.0C — Vol 27,021 | 最新价 $2.69 | OI 1998→5115 (ΔOI +3117张) | ΔOI/Volume 11.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3117张（+156.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 21,427 张（Put 4,396 / Call 17,031），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +11.6k / P +11.5k ｜ Activity HIGH ｜ 1D
11-02  C +7.0k / P +4.0k ｜ Activity HIGH ｜ 4D
11-04  C +3.0k / P +2.7k ｜ Activity HIGH ｜ 6D
11-06  C +19.1k / P +7.0k ｜ Activity MEDIUM △ ｜ 8D

📆 10-30 Forward Structure
存量OI: C 287.1k / P 205.7k，今日变化ΔOI: C +11.6k / P +11.5k，平值价格ATM: C $2.34 / P $1.90 ｜ ATM IV 62.3%，净 delta 敞口 826k shares
Top ΔOI: C 150 +6,114 ｜ P 140 +4,396
仓位参考: Max Pain 150 ｜ Call Wall 155（+7.6%，弱）（OI 19.7k） ｜ Put Wall 150（+4.1%，弱）（OI 20.1k）
量化解读： 存量 Call 重｜ATM IV 62.3%｜历史 Rank 72%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 826,399 股

📆 11-02 Forward Structure
存量OI: C 27.3k / P 15.8k，今日变化ΔOI: C +7.0k / P +4.0k，平值价格ATM: C $3.02 / P $2.59 ｜ ATM IV 44.6%，净 delta 敞口 34k shares
Top ΔOI: C 157 +1,339 ｜ C 155 +1,115
仓位参考: Max Pain 147 ｜ Call Wall 157.5（+9.3%，弱）（OI 3.4k） ｜ Put Wall 145（+0.7%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 44.6%｜历史 Rank 72%（近端代理）｜IV/RV 0.85×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 33,646 股

📆 11-04 Forward Structure
存量OI: C 10.7k / P 7.4k，今日变化ΔOI: C +3.0k / P +2.7k，平值价格ATM: C $4.05 / P $3.70 ｜ ATM IV 50.5%，净 delta 敞口 55k shares
Top ΔOI: C 147 +627 ｜ C 150 +458 ｜ C 146 +293
仓位参考: Max Pain 148 ｜ Call Wall 155（+7.6%，弱）（OI 1.1k） ｜ Put Wall 135（-6.3%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 50.5%｜历史 Rank 72%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 正 55,069 股

11-06（MEDIUM △）Top ΔOI: 160C +4,334 ｜ 170C +3,466
11-06（MEDIUM △）仓位参考: Max Pain 150 ｜ Put Wall 140（-2.8%）（OI 11.8k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 62.3% vs 11-02 44.6%（差 +17.7pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/SPCX_morning.json