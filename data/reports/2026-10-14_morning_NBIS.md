# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $773.15 ｜ QQQ $736.40
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.8（fear）
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
🔴 **事件差分**: 10-16（2D）ATM IV 107.1% vs 10-23 84.0%（差 +23.1pp），覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-16 195P ΔOI +2,122（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 206.86 → 今开 195.00（-5.7%） | 较昨收变动（含盘初走势） ｜ 今日高 198.60 ｜ 低 185.61

Options: P/C成交量 0.44 | OI比 0.92 | ATM IV 107.1% | Skew 3.6pp | Term 0.81 | ExpMove ±6.8%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价中性（Skew 3.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±6.8% ｜ 10-23（9D）±10.6% ｜ 10-30（16D）±13.7% ｜ 11-06（23D）±16.1%
   ⇒ IV–VIX Spread: +91.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -19,979,919 | GEX Change vs 上次快照 -4,468,113 | Flip: Primary Flip: 211.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 525 / LOW 48 / INVALID 123
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 211.23（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价低于该位 7.0%）
最近结构参考: Put Wall 200（现价低于该位 7.0%）
量化视角： 负 Gamma（1998万，无历史分位）｜负 Gamma 加深（447万）｜现价位于 Flip 下方 11.90%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall，弱结构） / 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 211（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 230.0C — Vol 11,974 | 最新价 $0.92 | OI 8964→14221 (ΔOI +5257张) | ΔOI/Volume 43.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5257张（+58.6% vs前日OI），连续性待观察（方向未知）
11-13 130.0P — Vol 2,252 | 最新价 $0.48 | OI 30→2272 (ΔOI +2242张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2242张（+7473.3% vs前日OI），连续性待观察（方向未知）
10-16 195.0P — Vol 4,806 | 最新价 $1.87 | OI 3360→5482 (ΔOI +2122张) | ΔOI/Volume 44.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2122张（+63.1% vs前日OI），连续性待观察（方向未知）
11-06 220.0C — Vol 2,357 | 最新价 $10.65 | OI 88→2062 (ΔOI +1974张) | ΔOI/Volume 83.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1974张（+2243.2% vs前日OI），连续性待观察（方向未知）
10-16 210.0C — Vol 7,994 | 最新价 $4.98 | OI 3436→5082 (ΔOI +1646张) | ΔOI/Volume 20.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1646张（+47.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,241 张（Put 4,364 / Call 8,877），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +7.0k / P +1.8k ｜ Activity HIGH ｜ 2D
10-23  C +6.5k / P +2.3k ｜ Activity HIGH ｜ 9D
10-30  C +3.4k / P +1.4k ｜ Activity HIGH ｜ 16D
11-06  C +3.5k / P +0.4k ｜ Activity HIGH ｜ 23D

📆 10-16 Forward Structure
存量OI: C 133.5k / P 123.3k，今日变化ΔOI: C +7.0k / P +1.8k，平值价格ATM: C $7.25 / P $5.50 ｜ ATM IV 107.1%，净 delta 敞口 123k shares
Top ΔOI: C 230 +5,257 ｜ P 195 +2,122
仓位参考: Max Pain 220 ｜ Call Wall 200（+7.5%，弱）（OI 3.4k） ｜ Put Wall 190（+2.1%，弱）（OI 7.3k）
量化解读： 存量两侧均衡｜ATM IV 107.1%｜历史 Rank 58%（近端代理）｜IV/RV 1.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 123,056 股

📆 10-23 Forward Structure
存量OI: C 30.9k / P 21.2k，今日变化ΔOI: C +6.5k / P +2.3k，平值价格ATM: C $10.75 / P $8.90 ｜ ATM IV 84.0%，净 delta 敞口 -49k shares
Top ΔOI: P 190 +684
仓位参考: Max Pain 215 ｜ Put Wall 200（+7.5%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 84.0%｜历史 Rank 58%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 48,937 股

📆 10-30 Forward Structure
存量OI: C 26.0k / P 19.0k，今日变化ΔOI: C +3.4k / P +1.4k，平值价格ATM: C $13.78 / P $11.66 ｜ ATM IV 81.0%，净 delta 敞口 -35k shares
Top ΔOI: C 240 +470
仓位参考: Max Pain 220 ｜ Put Wall 200（+7.5%）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 81.0%｜历史 Rank 58%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 负 34,629 股

📆 11-06 Forward Structure
存量OI: C 11.3k / P 13.4k，今日变化ΔOI: C +3.5k / P +0.4k，平值价格ATM: C $15.80 / P $14.26 ｜ ATM IV 81.6%，净 delta 敞口 80k shares
Top ΔOI: C 220 +1,974 ｜ C 225 +889 ｜ C 210 +165
仓位参考: Max Pain 220 ｜ Put Wall 200（+7.5%）（OI 3.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 81.6%｜历史 Rank 58%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 正 80,177 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 107.1% vs 10-23 84.0%（差 +23.1pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/NBIS_morning.json