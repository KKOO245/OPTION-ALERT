# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $770.58 ｜ QQQ $721.80
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　⏰ 今日
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4　⏰ 今日
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **事件差分**: 10-30（2D）ATM IV 132.3% vs 11-06 86.9%（差 +45.4pp），覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 160C ΔOI +513（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 161.09 → 今开 156.64（-2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 160.89 ｜ 低 156.64

Options: P/C成交量 0.37 | OI比 0.49 | ATM IV 132.3% | Skew -2.5pp | Term 0.52 | ExpMove ±8.4%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±8.4% ｜ 11-06（9D）±11.2% ｜ 11-13（16D）±13.2% ｜ 11-20（23D）±14.5%
   ⇒ IV–VIX Spread: +114.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,671,275 | GEX Change vs 上次快照 -782,406 | Flip: Primary Flip: 151.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 468 / LOW 119 / INVALID 303
结构观察区: Primary Flip 151.53（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 6.2%）
最近结构参考: Flip 152（现价高于该位 5.2%）
量化视角： 正 Gamma（867万，无历史分位）｜正 Gamma 减弱（78万）｜现价位于 Flip 上方 5.25%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 152（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 160.0C — Vol 944 | 最新价 $7.25 | OI 576→1089 (ΔOI +513张) | ΔOI/Volume 54.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增513张（+89.1% vs前日OI），连续性待观察（方向未知）
11-06 185.0C — Vol 728 | 最新价 $2.15 | OI 369→811 (ΔOI +442张) | ΔOI/Volume 60.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增442张（+119.8% vs前日OI），连续性待观察（方向未知）
11-06 175.0P — Vol 483 | 最新价 $17.82 | OI 305→730 (ΔOI +425张) | ΔOI/Volume 88.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增425张（+139.3% vs前日OI），连续性待观察（方向未知）
11-06 175.0C — Vol 488 | 最新价 $4.08 | OI 469→859 (ΔOI +390张) | ΔOI/Volume 79.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增390张（+83.2% vs前日OI），连续性待观察（方向未知）
11-06 250.0C — Vol 351 | 最新价 $0.08 | OI 267→617 (ΔOI +350张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增350张（+131.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,120 张（Put 425 / Call 1,695），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +1.1k / P +0.2k ｜ Activity HIGH ｜ 2D
11-06  C +1.8k / P +1.1k ｜ Activity MEDIUM △ ｜ 9D
11-13  C +0.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 16D
11-20  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 71.7k / P 35.3k，今日变化ΔOI: C +1.1k / P +0.2k，平值价格ATM: C $6.20 / P $7.18 ｜ ATM IV 132.3%，净 delta 敞口 52k shares
Top ΔOI: C 160 +513
仓位参考: Max Pain 170 ｜ Call Wall 172.5（+8.2%，弱）（OI 11.8k） ｜ Put Wall 155（-2.8%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 132.3%｜历史 Rank 96%（近端代理）｜IV/RV 2.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 51,921 股

11-06（MEDIUM △）Top ΔOI: 185C +442 ｜ 175P +425
11-06（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 175（+9.7%，弱）（OI 0.9k）

11-13（MEDIUM △）Top ΔOI: 175C -113 ｜ 170C +70
11-13（MEDIUM △）仓位参考: Max Pain 172 ｜ Call Wall 170（+6.6%，弱）（OI 0.3k） ｜ Put Wall 155（-2.8%，弱）（OI 1.0k）

11-20（MEDIUM △）Top ΔOI: 125P +344 ｜ 175C +159
11-20（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 170（+6.6%）（OI 13.6k） ｜ Put Wall 150（-5.9%，弱）（OI 3.1k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 132.3% vs 11-06 86.9%（差 +45.4pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/COIN_morning.json