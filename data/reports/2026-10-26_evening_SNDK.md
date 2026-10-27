# 期权晚报 2026-10-26（快照 21:54 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 18.39 ↓5.5%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：无更新，来源自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🔴 **事件差分**: 10-30（4D）ATM IV 118.1% vs 11-06 93.4%（差 +24.7pp），覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,271.62 → 收盘 1,255.58（-1.3%） ｜ 今日高 1287.84 ｜ 低 1229.00 ｜ 昨收 1,238.03 → 收盘 1,255.58（+1.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-29，窗口结束前不做对错判定）

Options: P/C成交量 0.57 | OI比 0.81 | ATM IV 118.1% | Skew 1.1pp | Term 0.64 | ExpMove ±9.9%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价薄（Skew 1.1pp）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（4D）±9.9% ｜ 11-06（11D）±12.9% ｜ 11-13（18D）±15.2% ｜ 11-20（25D）±16.5%
   ⇒ IV–VIX Spread: +99.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,901,336 | GEX Change vs 上次快照 -1,142,779 | Flip: Primary Flip: 1376.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1787 / LOW 420 / INVALID 1107
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1376.89（全链重定价，覆盖 100%）
最近结构参考: Flip 1377（现价低于该位 8.8%）
量化视角： 负 Gamma（390万，无历史分位）｜负 Gamma 加深（114万）｜现价位于 Flip 下方 8.81%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,400（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1377（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 640.0P — Vol 47 | 最新价 $0.20 | OI 178→1705 (ΔOI +1527张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1527张（+857.9% vs前日OI），连续性待观察（方向未知）
10-30 780.0P — Vol 11 | 最新价 $0.60 | OI 0→1249 (ΔOI +1249张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1249张（前日OI缺失），值得跟踪（方向未知）
10-30 1450.0C — Vol 1,281 | 最新价 $9.17 | OI 587→1331 (ΔOI +744张) | ΔOI/Volume 58.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增744张（+126.8% vs前日OI），连续性待观察（方向未知）
10-30 1000.0P — Vol 684 | 最新价 $3.70 | OI 731→1357 (ΔOI +626张) | ΔOI/Volume 91.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增626张（+85.6% vs前日OI），连续性待观察（方向未知）
10-30 800.0P — Vol 585 | 最新价 $0.65 | OI 363→863 (ΔOI +500张) | ΔOI/Volume 85.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增500张（+137.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,646 张（Put 3,902 / Call 744），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-30 Forward Structure
存量OI: C 36.8k / P 29.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $62.50 / P $61.47 ｜ ATM IV 118.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 1,400 ｜ Call Wall 1300（+3.5%，弱）（OI 1.0k） ｜ Put Wall 1350（+7.5%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 118.1%｜历史 Rank 77%（近端代理）｜IV/RV 2.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 1,400 ｜ Call Wall 1300（+3.5%，弱）（OI 0.5k） ｜ Put Wall 1200（-4.4%）（OI 0.8k）

11-13（Activity LOW）仓位参考: Max Pain 1,500 ｜ Call Wall 1300（+3.5%，弱）（OI 0.1k） ｜ Put Wall 1200（-4.4%，弱）（OI 0.2k）

11-20（Activity LOW）仓位参考: Max Pain 1,500 ｜ Call Wall 1300（+3.5%，弱）（OI 0.5k） ｜ Put Wall 1200（-4.4%，弱）（OI 1.3k）

📅 事件差分（观察，非因果）: 10-30（4D）ATM IV 118.1% vs 11-06 93.4%（差 +24.7pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=67 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=67）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/SNDK_evening.json