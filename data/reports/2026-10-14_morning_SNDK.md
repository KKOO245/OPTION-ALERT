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
🟡 **事件差分**: 10-16 ATM IV 80.1% vs 10-23 65.5%（差 +14.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 1500C ΔOI +836（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,482.33 → 今开 1,427.38（-3.7%） | 较昨收变动（含盘初走势） ｜ 今日高 1461.80 ｜ 低 1427.38

Options: P/C成交量 0.52 | OI比 0.92 | ATM IV 80.1% | Skew 0.6pp | Term 0.85 | ExpMove ±5.1%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价薄（Skew 0.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±5.1% ｜ 10-23（9D）±8.3% ｜ 10-30（16D）±12.5% ｜ 11-06（23D）±15.0%
   ⇒ IV–VIX Spread: +64.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,384,981 | GEX Change vs 上次快照 393,131 | Flip: Primary Flip: 1511.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1873 / LOW 504 / INVALID 903
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1511.21（全链重定价，覆盖 100%）
最近结构参考: Flip 1511（现价低于该位 4.6%）
量化视角： 负 Gamma（738万，无历史分位）｜负 Gamma 缓解（+39万）｜现价位于 Flip 下方 4.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,570（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1511（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 1700.0C — Vol 2,452 | 最新价 $9.60 | OI 541→2402 (ΔOI +1861张) | ΔOI/Volume 75.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1861张（+344.0% vs前日OI），连续性待观察（方向未知）
10-16 1600.0C — Vol 5,312 | 最新价 $7.58 | OI 2462→3373 (ΔOI +911张) | ΔOI/Volume 17.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增911张（+37.0% vs前日OI），连续性待观察（方向未知）
10-30 1500.0C — Vol 1,095 | 最新价 $88.54 | OI 575→1411 (ΔOI +836张) | ΔOI/Volume 76.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增836张（+145.4% vs前日OI），连续性待观察（方向未知）
10-16 1300.0P — Vol 2,682 | 最新价 $2.10 | OI 1530→2335 (ΔOI +805张) | ΔOI/Volume 30.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增805张（+52.6% vs前日OI），连续性待观察（方向未知）
10-16 1675.0C — Vol 969 | 最新价 $2.60 | OI 1230→1981 (ΔOI +751张) | ΔOI/Volume 77.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增751张（+61.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,164 张（Put 805 / Call 4,359），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +7.4k / P +1.5k ｜ Activity HIGH ｜ 2D
10-23  C +5.0k / P +1.3k ｜ Activity HIGH ｜ 9D
10-30  C +3.2k / P +0.1k ｜ Activity HIGH ｜ 16D
11-06  C +0.4k / P +0.5k ｜ Activity MEDIUM △ ｜ 23D

📆 10-16 Forward Structure
存量OI: C 77.1k / P 70.7k，今日变化ΔOI: C +7.4k / P +1.5k，平值价格ATM: C $39.19 / P $34.20 ｜ ATM IV 80.1%，净 delta 敞口 237k shares
Top ΔOI: C 1600 +911 ｜ P 1300 +805 ｜ C 1675 +751
仓位参考: Max Pain 1,570 ｜ Call Wall 1500（+4.0%，弱）（OI 1.8k） ｜ Put Wall 1400（-2.9%，弱）（OI 3.4k）
量化解读： 存量两侧均衡｜ATM IV 80.1%｜历史 Rank 38%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 237,302 股

📆 10-23 Forward Structure
存量OI: C 23.7k / P 17.3k，今日变化ΔOI: C +5.0k / P +1.3k，平值价格ATM: C $61.50 / P $58.49 ｜ ATM IV 65.5%，净 delta 敞口 79k shares
Top ΔOI: C 1700 +1,861 ｜ C 1580 +452 ｜ C 1550 +299
仓位参考: Max Pain 1,555 ｜ Call Wall 1500（+4.0%，弱）（OI 1.4k） ｜ Put Wall 1500（+4.0%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 65.5%｜历史 Rank 38%（近端代理）｜IV/RV 1.37×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 79,323 股

📆 10-30 Forward Structure
存量OI: C 14.8k / P 12.6k，今日变化ΔOI: C +3.2k / P +0.1k，平值价格ATM: C $94.60 / P $86.30 ｜ ATM IV 74.5%，净 delta 敞口 99k shares
Top ΔOI: C 1500 +836
仓位参考: Max Pain 1,600 ｜ Call Wall 1500（+4.0%）（OI 1.4k） ｜ Put Wall 1400（-2.9%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 74.5%｜历史 Rank 38%（近端代理）｜IV/RV 1.56×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 99,174 股

11-06（MEDIUM △）Top ΔOI: 1100P +284 ｜ 1800C +50
11-06（MEDIUM △）仓位参考: Max Pain 1,640 ｜ Call Wall 1560（+8.2%，弱）（OI 0.1k） ｜ Put Wall 1400（-2.9%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 80.1% vs 10-23 65.5%（差 +14.6pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/SNDK_morning.json