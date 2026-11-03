# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $753.95 ｜ QQQ $686.04
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-04（1D）ATM IV 99.6% vs 11-06 81.8%（差 +17.8pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-04 140P ΔOI +2,877（距现价 -0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 136.37 → 今开 137.65（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 141.67 ｜ 低 137.56

Options: P/C成交量 0.58 | OI比 1.34 | ATM IV 99.6% | Skew 9.1pp | Term 0.57 | ExpMove ±4.7%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜保护溢价显著（Skew 9.1pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.34×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-04（1D）±4.7% ｜ 11-06（3D）±6.1% ｜ 11-09（6D）±7.0% ｜ 11-11（8D）±8.0%
   ⇒ IV–VIX Spread: +78.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,931,081 | GEX Change vs 上次快照 37,557,435 | Flip: Primary Flip: 142.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 690 / LOW 160 / INVALID 600
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 142.09（全链重定价，覆盖 100%）
Put Wall 135（弱结构｜现价高于该位 4.2%） | Call Wall 150（弱结构｜现价低于该位 6.2%）
最近结构参考: Flip 142（现价低于该位 1.0%）
量化视角： 负 Gamma（1393万，无历史分位）｜负 Gamma 缓解（+3756万）｜现价位于 Flip 下方 1.02%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Put Wall，弱结构） / 140（MaxPain，仅结算参考）；上方 150（Call Wall，弱结构）。
• Gamma 区域：切换参考 142（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 155.0C — Vol 33,522 | 最新价 $0.26 | OI 12603→38073 (ΔOI +25470张) | ΔOI/Volume 76.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25470张（+202.1% vs前日OI），连续性待观察（方向未知）
11-06 157.5C — Vol 28,169 | 最新价 $0.17 | OI 2874→27331 (ΔOI +24457张) | ΔOI/Volume 86.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增24457张（+851.0% vs前日OI），连续性待观察（方向未知）
11-06 150.0C — Vol 23,953 | 最新价 $0.64 | OI 12573→22403 (ΔOI +9830张) | ΔOI/Volume 41.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9830张（+78.2% vs前日OI），连续性待观察（方向未知）
11-04 130.0P — Vol 11,997 | 最新价 $1.41 | OI 868→8298 (ΔOI +7430张) | ΔOI/Volume 61.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7430张（+856.0% vs前日OI），连续性待观察（方向未知）
11-13 125.0P — Vol 5,986 | 最新价 $2.29 | OI 1564→5908 (ΔOI +4344张) | ΔOI/Volume 72.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4344张（+277.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 71,531 张（Put 11,774 / Call 59,757），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-04  C +15.5k / P +22.6k ｜ Activity HIGH ｜ 1D
11-06  C +74.8k / P +20.6k ｜ Activity HIGH ｜ 3D
11-09  C +1.5k / P +1.4k ｜ Activity HIGH ｜ 6D
11-11  C +0.6k / P +0.4k ｜ Activity HIGH ｜ 8D

📆 11-04 Forward Structure
存量OI: C 34.4k / P 46.1k，今日变化ΔOI: C +15.5k / P +22.6k，平值价格ATM: C $3.04 / P $3.56 ｜ ATM IV 99.6%，净 delta 敞口 94k shares
Top ΔOI: P 130 +7,430 ｜ P 140 +2,877 ｜ C 140 +2,441
仓位参考: Max Pain 140 ｜ Call Wall 145（+3.1%，弱）（OI 3.5k） ｜ Put Wall 130（-7.6%）（OI 8.3k）
量化解读： 存量 Put 重｜ATM IV 99.6%｜历史 Rank 96%（近端代理）｜IV/RV 1.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 94,130 股

📆 11-06 Forward Structure
存量OI: C 244.1k / P 167.8k，今日变化ΔOI: C +74.8k / P +20.6k，平值价格ATM: C $4.15 / P $4.40 ｜ ATM IV 81.8%，净 delta 敞口 881k shares
Top ΔOI: C 155 +25,470 ｜ C 157 +24,457 ｜ C 150 +9,830
仓位参考: Max Pain 144 ｜ Call Wall 150（+6.7%，弱）（OI 22.4k） ｜ Put Wall 135（-4.0%，弱）（OI 20.2k）
量化解读： 存量 Call 重｜ATM IV 81.8%｜历史 Rank 96%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 881,060 股

📆 11-09 Forward Structure
存量OI: C 7.0k / P 4.9k，今日变化ΔOI: C +1.5k / P +1.4k，平值价格ATM: C $4.68 / P $5.10 ｜ ATM IV 64.7%，净 delta 敞口 3k shares
Top ΔOI: C 150 +389 ｜ P 130 +247
仓位参考: Max Pain 143 ｜ Call Wall 150（+6.7%，弱）（OI 1.0k） ｜ Put Wall 134（-4.7%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 64.7%｜历史 Rank 96%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,974 股

📆 11-11 Forward Structure
存量OI: C 2.6k / P 2.0k，今日变化ΔOI: C +0.6k / P +0.4k，平值价格ATM: C $5.00 / P $6.30 ｜ ATM IV 64.0%，净 delta 敞口 3k shares
Top ΔOI: P 135 +95
仓位参考: Max Pain 142 ｜ Call Wall 150（+6.7%，弱）（OI 0.4k） ｜ Put Wall 135（-4.0%）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 64.0%｜历史 Rank 96%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 3,047 股

📅 事件差分（观察，非因果）: 11-04（1D）ATM IV 99.6% vs 11-06 81.8%（差 +17.8pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/SPCX_morning.json