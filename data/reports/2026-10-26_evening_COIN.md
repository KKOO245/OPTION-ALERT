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
🔴 **事件差分**: 10-30（4D）ATM IV 106.0% vs 11-06 83.0%（差 +23.0pp），覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 168.00 → 收盘 159.60（-5.0%） ｜ 今日高 162.47 ｜ 低 155.31 ｜ 昨收 164.45 → 收盘 159.60（-2.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-02，窗口结束前不做对错判定）

Options: P/C成交量 0.67 | OI比 0.49 | ATM IV 106.0% | Skew 1.5pp | Term 0.65 | ExpMove ±8.9%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（4D）±8.9% ｜ 11-06（11D）±11.3% ｜ 11-13（18D）±12.7% ｜ 11-20（25D）±15.0%
   ⇒ IV–VIX Spread: +87.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,600,880 | GEX Change vs 上次快照 -369,537 | Flip: Primary Flip: 152.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 454 / LOW 105 / INVALID 285
结构观察区: Primary Flip 152.17（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 6.1%）
最近结构参考: Flip 152（现价高于该位 4.9%）
量化视角： 正 Gamma（760万，无历史分位）｜正 Gamma 减弱（37万）｜现价位于 Flip 上方 4.89%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 152（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 172.5C — Vol 749 | 最新价 $2.65 | OI 1830→11600 (ΔOI +9770张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9770张（+533.9% vs前日OI），连续性待观察（方向未知）
10-30 180.0C — Vol 1,068 | 最新价 $1.40 | OI 2784→11977 (ΔOI +9193张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9193张（+330.2% vs前日OI），连续性待观察（方向未知）
10-30 170.0C — Vol 1,357 | 最新价 $3.30 | OI 388→5533 (ΔOI +5145张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5145张（+1326.0% vs前日OI），连续性待观察（方向未知）
10-30 177.5C — Vol 312 | 最新价 $1.92 | OI 1997→6435 (ΔOI +4438张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4438张（+222.2% vs前日OI），连续性待观察（方向未知）
11-06 90.0P — Vol 2,274 | 最新价 $0.07 | OI 3160→5145 (ΔOI +1985张) | ΔOI/Volume 87.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1985张（+62.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 30,531 张（Put 1,985 / Call 28,546），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-30 Forward Structure
存量OI: C 66.6k / P 32.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.90 / P $7.29 ｜ ATM IV 106.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 170 ｜ Call Wall 172.5（+8.1%，弱）（OI 11.6k） ｜ Put Wall 150（-6.0%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 106.0%｜历史 Rank 90%（近端代理）｜IV/RV 2.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 172 ｜ Call Wall 175（+9.6%，弱）（OI 0.5k）

11-13（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 170（+6.5%，弱）（OI 0.2k） ｜ Put Wall 160（+0.3%，弱）（OI 0.6k）

11-20（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 170（+6.5%）（OI 13.6k） ｜ Put Wall 150（-6.0%，弱）（OI 3.1k）

📅 事件差分（观察，非因果）: 10-30（4D）ATM IV 106.0% vs 11-06 83.0%（差 +23.0pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/COIN_evening.json