# 期权晚报 2026-10-12（快照 16:40 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 10-23 200P ΔOI +778（距现价 -4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 217.03 → 收盘 210.06（-3.2%） ｜ 今日高 217.03 ｜ 低 206.90 ｜ 昨收 221.07 → 收盘 210.06（-5.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-15，窗口结束前不做对错判定）

Options: P/C成交量 0.69 | OI比 1.02 | ATM IV 74.3% | Skew -0.8pp | Term 1.02 | ExpMove ±6.2%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.02×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（4D）±6.2% ｜ 10-23（11D）±9.2% ｜ 10-30（18D）±12.2% ｜ 11-06（25D）±14.4%
   ⇒ IV–VIX Spread: +59.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,291,070 | GEX Change vs 上次快照 -2,012,154 | Flip: Primary Flip: 223.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 494 / LOW 43 / INVALID 137
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 223.67（全链重定价，覆盖 99%）
Put Wall 200（弱结构｜现价高于该位 5.0%）
最近结构参考: Put Wall 200（现价高于该位 5.0%）
量化视角： 负 Gamma（1429万，无历史分位）｜负 Gamma 加深（201万）｜现价位于 Flip 下方 6.09%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 225（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 224（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 300.0C — Vol 526 | 最新价 $0.03 | OI 9546→11512 (ΔOI +1966张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1966张（+20.6% vs前日OI），连续性待观察（方向未知）
10-16 230.0C — Vol 8,473 | 最新价 $1.23 | OI 4520→6421 (ΔOI +1901张) | ΔOI/Volume 22.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1901张（+42.1% vs前日OI），连续性待观察（方向未知）
10-16 250.0C — Vol 4,185 | 最新价 $0.26 | OI 9891→10887 (ΔOI +996张) | ΔOI/Volume 23.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增996张（+10.1% vs前日OI），连续性待观察（方向未知）
10-16 220.0P — Vol 1,413 | 最新价 $12.74 | OI 8249→9228 (ΔOI +979张) | ΔOI/Volume 69.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增979张（+11.9% vs前日OI），连续性待观察（方向未知）
10-23 200.0P — Vol 3,134 | 最新价 $5.24 | OI 1525→2303 (ΔOI +778张) | ΔOI/Volume 24.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增778张（+51.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,620 张（Put 1,757 / Call 4,863），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +8.0k / P +5.0k ｜ Activity HIGH ｜ 4D
10-23  C +0.5k / P +1.8k ｜ Activity HIGH ｜ 11D
10-30  C +1.3k / P +0.5k ｜ Activity HIGH ｜ 18D
11-06  C +0.3k / P +1.2k ｜ Activity HIGH ｜ 25D

📆 10-16 Forward Structure
存量OI: C 113.8k / P 116.2k，今日变化ΔOI: C +8.0k / P +5.0k，平值价格ATM: C $6.70 / P $6.35 ｜ ATM IV 74.3%，净 delta 敞口 -168k shares
Top ΔOI: C 230 +1,901
仓位参考: Max Pain 225 ｜ Call Wall 230（+9.5%，弱）（OI 6.4k） ｜ Put Wall 220（+4.7%，弱）（OI 9.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 74.3%｜历史 Rank 7%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 168,406 股

📆 10-23 Forward Structure
存量OI: C 19.2k / P 15.2k，今日变化ΔOI: C +0.5k / P +1.8k，平值价格ATM: C $9.81 / P $9.45 ｜ ATM IV 66.1%，净 delta 敞口 -48k shares
Top ΔOI: P 200 +778 ｜ P 195 +173
仓位参考: Max Pain 220 ｜ Call Wall 212.5（+1.2%，弱）（OI 1.8k） ｜ Put Wall 200（-4.8%）（OI 2.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.1%｜历史 Rank 7%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 负 47,749 股

📆 10-30 Forward Structure
存量OI: C 20.9k / P 16.6k，今日变化ΔOI: C +1.3k / P +0.5k，平值价格ATM: C $12.75 / P $12.82 ｜ ATM IV 65.9%，净 delta 敞口 -6k shares
Top ΔOI: C 270 +718 ｜ P 210 +146
仓位参考: Max Pain 230 ｜ Call Wall 225（+7.1%，弱）（OI 0.6k） ｜ Put Wall 200（-4.8%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 65.9%｜历史 Rank 7%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 5,739 股

📆 11-06 Forward Structure
存量OI: C 7.2k / P 11.3k，今日变化ΔOI: C +0.3k / P +1.2k，平值价格ATM: C $14.50 / P $15.67 ｜ ATM IV 67.1%，净 delta 敞口 -30k shares
Top ΔOI: P 200 +577 ｜ P 210 +206
仓位参考: Max Pain 230 ｜ Call Wall 230（+9.5%，弱）（OI 0.4k） ｜ Put Wall 200（-4.8%）（OI 2.5k）
量化解读： 存量 Put 重｜ATM IV 67.1%｜历史 Rank 7%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 负 29,638 股

📅 事件差分（观察，非因果）: 10-16（4D）ATM IV 74.3% vs 10-23 66.1%（差 +8.3pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=45 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=45）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/NBIS_evening.json