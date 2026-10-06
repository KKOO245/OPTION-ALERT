# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.74 ｜ QQQ $760.82
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 49.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **事件差分**: 10-09 ATM IV 43.9% vs 10-16 33.6%（差 +10.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 150P ΔOI +502（距现价 -2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 156.19 → 今开 156.87（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 157.47 ｜ 低 149.92

Options: P/C成交量 0.20 | OI比 2.54 | ATM IV 43.9% | Skew -6.1pp | Term 0.77 | ExpMove ±2.5%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.20×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.54×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±2.5% ｜ 10-16（10D）±5.2% ｜ 10-23（17D）±6.3% ｜ 10-30（24D）±6.7%
   ⇒ IV–VIX Spread: +28.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -45,692,770 | GEX Change vs 上次快照 -9,867,819 | Flip: Primary Flip: 164.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 319 / LOW 72 / INVALID 343
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 164.67（全链重定价，覆盖 94%）
Put Wall 150（现价高于该位 2.4%）
最近结构参考: Put Wall 150（现价高于该位 2.4%）
量化视角： 负 Gamma（4569万，无历史分位）｜负 Gamma 加深（987万）｜现价位于 Flip 下方 6.72%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall）；上方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 150.0P — Vol 709 | 最新价 $2.58 | OI 7015→7517 (ΔOI +502张) | ΔOI/Volume 70.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增502张（+7.2% vs前日OI），连续性待观察（方向未知）
10-09 157.0C — Vol 425 | 最新价 $1.93 | OI 80→501 (ΔOI +421张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增421张（+526.2% vs前日OI），连续性待观察（方向未知）
10-16 165.0C — Vol 328 | 最新价 $0.78 | OI 3027→3326 (ΔOI +299张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增299张（+9.9% vs前日OI），连续性待观察（方向未知）
10-23 172.0C — Vol 245 | 最新价 $0.39 | OI 4→248 (ΔOI +244张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增244张（+6100.0% vs前日OI），连续性待观察（方向未知）
10-16 160.0C — Vol 285 | 最新价 $1.93 | OI 1285→1489 (ΔOI +204张) | ΔOI/Volume 71.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增204张（+15.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,670 张（Put 502 / Call 1,168），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +1.1k / P +0.3k ｜ Activity HIGH ｜ 3D
10-16  C +0.3k / P -0.8k ｜ Activity MEDIUM △ ｜ 10D
10-23  C +0.3k / P +37 ｜ Activity MEDIUM △ ｜ 17D
10-30  C +0.2k / P +0.8k ｜ Activity HIGH ｜ 24D

📆 10-09 Forward Structure
存量OI: C 4.3k / P 10.8k，今日变化ΔOI: C +1.1k / P +0.3k，平值价格ATM: C $2.25 / P $1.61 ｜ ATM IV 43.9%，净 delta 敞口 21k shares
Top ΔOI: C 157 +421 ｜ C 164 +126 ｜ P 148 +99
仓位参考: Max Pain 155 ｜ Call Wall 145（-5.6%）（OI 1.0k） ｜ Put Wall 148（-3.6%，弱）（OI 3.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 43.9%｜历史 Rank 92%（近端代理）｜IV/RV 1.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 20,663 股

10-16（MEDIUM △）Top ΔOI: 154P -524 ｜ 165C +299
10-16（MEDIUM △）仓位参考: Max Pain 160 ｜ Put Wall 150（-2.3%）（OI 22.6k）

10-23（MEDIUM △）Top ΔOI: 164C +42 ｜ 158P +15
10-23（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 154（+0.3%，弱）（OI 84） ｜ Put Wall 153（-0.4%，弱）（OI 0.4k）

📆 10-30 Forward Structure
存量OI: C 2.2k / P 18.0k，今日变化ΔOI: C +0.2k / P +0.8k，平值价格ATM: C $5.90 / P $4.40 ｜ ATM IV 34.6%，净 delta 敞口 -13k shares
Top ΔOI: P 150 +502 ｜ P 140 +172 ｜ C 150 +75
仓位参考: Max Pain 156 ｜ Call Wall 159（+3.5%，弱）（OI 0.4k） ｜ Put Wall 150（-2.3%，弱）（OI 7.5k）
量化解读： 存量 Put 重｜ATM IV 34.6%｜历史 Rank 92%（近端代理）｜IV/RV 1.42×（近似）｜净 delta 敞口 负 12,948 股

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 43.9% vs 10-16 33.6%（差 +10.3pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=42 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=42）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/XBI_morning.json