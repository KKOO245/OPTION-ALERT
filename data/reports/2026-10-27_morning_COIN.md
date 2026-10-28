# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $nan
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🔴 **事件差分**: 10-30（3D）ATM IV 117.3% vs 11-06 86.5%（差 +30.9pp），覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 160C ΔOI +523（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 159.60 → 今开 160.33（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 161.87 ｜ 低 157.75

Options: P/C成交量 0.30 | OI比 0.50 | ATM IV 117.3% | Skew -0.9pp | Term 0.61 | ExpMove ±8.9%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.30×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±8.9% ｜ 11-06（10D）±11.4% ｜ 11-13（17D）±13.7% ｜ 11-20（24D）±15.2%
   ⇒ IV–VIX Spread: +99.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,108,135 | GEX Change vs 上次快照 507,256 | Flip: Primary Flip: 150.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 463 / LOW 109 / INVALID 318
结构观察区: Primary Flip 150.61（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 6.5%）
最近结构参考: Flip 151（现价高于该位 5.6%）
量化视角： 正 Gamma（811万，无历史分位）｜正 Gamma 增强（+51万）｜现价位于 Flip 上方 5.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 155.0P — Vol 958 | 最新价 $8.30 | OI 228→1033 (ΔOI +805张) | ΔOI/Volume 84.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增805张（+353.1% vs前日OI），连续性待观察（方向未知）
11-13 55.0P — Vol 800 | 最新价 $0.02 | OI 1→801 (ΔOI +800张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增800张（+80000.0% vs前日OI），连续性待观察（方向未知）
10-30 170.0C — Vol 1,357 | 最新价 $3.30 | OI 5533→6070 (ΔOI +537张) | ΔOI/Volume 39.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增537张（+9.7% vs前日OI），连续性待观察（方向未知）
11-06 152.5P — Vol 563 | 最新价 $6.03 | OI 33→557 (ΔOI +524张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增524张（+1587.9% vs前日OI），连续性待观察（方向未知）
10-30 160.0C — Vol 1,346 | 最新价 $6.90 | OI 53→576 (ΔOI +523张) | ΔOI/Volume 38.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增523张（+986.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,189 张（Put 2,129 / Call 1,060），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +4.0k / P +2.2k ｜ Activity MEDIUM △ ｜ 3D
11-06  C +1.0k / P +2.5k ｜ Activity MEDIUM △ ｜ 10D
11-13  C +0.6k / P +1.8k ｜ Activity HIGH ｜ 17D
11-20  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 24D

📆 10-30 Forward Structure
存量OI: C 70.6k / P 35.1k，今日变化ΔOI: C +4.0k / P +2.2k，平值价格ATM: C $6.70 / P $7.50 ｜ ATM IV 117.3%，净 delta 敞口 102k shares
Top ΔOI: C 170 +537 ｜ C 160 +523
仓位参考: Max Pain 170 ｜ Call Wall 172.5（+8.5%，弱）（OI 11.9k） ｜ Put Wall 150（-5.7%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 117.3%｜历史 Rank 93%（近端代理）｜IV/RV 2.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 101,919 股

11-06（MEDIUM △）Top ΔOI: 152P +524
11-06（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 170（+6.9%，弱）（OI 0.3k）

📆 11-13 Forward Structure
存量OI: C 7.4k / P 10.4k，今日变化ΔOI: C +0.6k / P +1.8k，平值价格ATM: C $11.20 / P $10.51 ｜ ATM IV 77.4%，净 delta 敞口 -18k shares
Top ΔOI: P 155 +805 ｜ C 180 +199
仓位参考: Max Pain 175 ｜ Call Wall 170（+6.9%，弱）（OI 0.3k） ｜ Put Wall 155（-2.5%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 77.4%｜历史 Rank 93%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 18,181 股

11-20（MEDIUM △）Top ΔOI: 200C -277 ｜ 165C +266
11-20（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 170（+6.9%）（OI 13.6k） ｜ Put Wall 150（-5.7%，弱）（OI 3.2k）

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 117.3% vs 11-06 86.5%（差 +30.9pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/COIN_morning.json