# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $717.83 ｜ QQQ $637.27
VIX 27.25 ↑2.4%（5D +7.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🔴 **事件差分**: 11-25（1D）ATM IV 80.1% vs 11-27 62.9%（差 +17.2pp），覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 138.43 → 今开 131.90（-4.7%） | 较昨收变动（含盘初走势） ｜ 今日高 132.50 ｜ 低 126.53
⚠️ 标的停更 2 个交易日：以下对比基于 2026-11-19 晚报，趋势与 OI 增仓指标需 2 个交易日数据恢复

Options: P/C成交量 0.71 | OI比 0.92 | ATM IV 80.1% | Skew 12.7pp | Term 0.74 | ExpMove ±3.7%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 12.7pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-25（1D）±3.7% ｜ 11-27（3D）±4.6% ｜ 11-30（6D）±6.0% ｜ 12-02（8D）±7.3%
   ⇒ IV–VIX Spread: +52.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -33,991,430 | GEX Change vs 上次快照 16,629,986 | Flip: Primary Flip: 131.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 752 / LOW 174 / INVALID 622
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 131.99（全链重定价，覆盖 98%）
最近结构参考: Flip 132（现价低于该位 2.5%）
量化视角： 负 Gamma（3399万，无历史分位）｜负 Gamma 缓解（+1663万）｜现价位于 Flip 下方 2.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 136（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- ⚠️ OI 增仓/异动基于 2026-11-19 快照对比（标的停更 2 个交易日），前几日数据可能失真，请谨慎解读
12-04 160.0C — Vol 41,128 | 最新价 $0.19 | OI 2614→41824 (ΔOI +39210张) | ΔOI/Volume 95.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增39210张（+1500.0% vs前日OI），连续性待观察（方向未知）
11-27 146.0C — Vol 24,998 | 最新价 $0.19 | OI 302→23904 (ΔOI +23602张) | ΔOI/Volume 94.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23602张（+7815.2% vs前日OI），连续性待观察（方向未知）
11-27 144.0C — Vol 26,878 | 最新价 $0.30 | OI 2177→25006 (ΔOI +22829张) | ΔOI/Volume 84.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22829张（+1048.6% vs前日OI），连续性待观察（方向未知）
12-04 137.0C — Vol 10,485 | 最新价 $3.95 | OI 0→10143 (ΔOI +10143张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10143张（前日OI缺失），连续性待观察（方向未知）
12-04 80.0P — Vol 124 | 最新价 $0.03 | OI 97→9311 (ΔOI +9214张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9214张（+9499.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 104,998 张（Put 9,214 / Call 95,784），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-25  C +30.3k / P +29.4k ｜ Activity HIGH ｜ 1D（新行权价 C 2.6k / P 1.9k）
11-27  C +72.9k / P +36.9k ｜ Activity HIGH ｜ 3D（新行权价 C 26 / P 1.4k）
11-30  C N/A / P N/A ｜ Activity LOW ｜ 6D（新上架）
12-02  C N/A / P N/A ｜ Activity LOW ｜ 8D（新上架）

📆 11-25 Forward Structure
存量OI: C 38.5k / P 35.4k，今日变化ΔOI: C +30.3k / P +29.4k（新行权价 C 2.6k / P 1.9k），平值价格ATM: C $2.18 / P $2.54 ｜ ATM IV 80.1%，净 delta 敞口 -1.3M shares
Top ΔOI: C 140 +4,118
仓位参考: Max Pain 136 ｜ Call Wall 140（+8.8%，弱）（OI 4.3k） ｜ Put Wall 130（+1.0%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜ATM IV 80.1%｜历史 Rank 88%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,266,438 股

📆 11-27 Forward Structure
存量OI: C 203.4k / P 100.8k，今日变化ΔOI: C +72.9k / P +36.9k（新行权价 C 26 / P 1.4k），平值价格ATM: C $2.79 / P $3.15 ｜ ATM IV 62.9%，净 delta 敞口 -635k shares
Top ΔOI: C 146 +23,602 ｜ C 144 +22,829
仓位参考: Max Pain 137 ｜ Call Wall 140（+8.8%，弱）（OI 7.0k） ｜ Put Wall 125（-2.9%，弱）（OI 8.1k）
量化解读： 存量 Call 重｜ATM IV 62.9%｜历史 Rank 88%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 635,319 股

11-30（Activity LOW）仓位参考: Max Pain 135 ｜ Call Wall 140（+8.8%）（OI 5.7k）

12-02（Activity LOW）仓位参考: Max Pain 133 ｜ Call Wall 140（+8.8%，弱）（OI 0.4k） ｜ Put Wall 130（+1.0%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-25（1D）ATM IV 80.1% vs 11-27 62.9%（差 +17.2pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/SPCX_morning.json