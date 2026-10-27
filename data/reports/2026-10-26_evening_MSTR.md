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
🟡 **事件差分**: 10-30 ATM IV 90.4% vs 11-06 79.0%（差 +11.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 144.43 → 收盘 139.82（-3.2%） ｜ 今日高 144.70 ｜ 低 137.26 ｜ 昨收 146.01 → 收盘 139.82（-4.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.97 | OI比 0.80 | ATM IV 90.4% | Skew 1.8pp | Term 0.78 | ExpMove ±7.6%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价薄（Skew 1.8pp）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.97×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（4D）±7.6% ｜ 11-06（11D）±11.3% ｜ 11-13（18D）±13.5% ｜ 11-20（25D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 18,594,898 | GEX Change vs 上次快照 -14,205,023 | Flip: Primary Flip: 134.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 594 / LOW 60 / INVALID 202
结构观察区: Primary Flip 134.98（全链重定价，覆盖 99%）
Call Wall 135（弱结构｜现价高于该位 3.6%）
最近结构参考: Call Wall 135（现价高于该位 3.6%）
量化视角： 正 Gamma（1859万，无历史分位）｜正 Gamma 减弱（1421万）｜现价位于 Flip 上方 3.58%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Call Wall，弱结构）；上方 147（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 135（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 152.5C — Vol 3,167 | 最新价 $1.39 | OI 5848→37825 (ΔOI +31977张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31977张（+546.8% vs前日OI），连续性待观察（方向未知）
10-30 160.0C — Vol 5,724 | 最新价 $0.56 | OI 6726→34397 (ΔOI +27671张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27671张（+411.4% vs前日OI），连续性待观察（方向未知）
10-30 90.0P — Vol 646 | 最新价 $0.04 | OI 3885→30745 (ΔOI +26860张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增26860张（+691.4% vs前日OI），连续性待观察（方向未知）
10-30 162.5C — Vol 4,160 | 最新价 $0.42 | OI 3128→24543 (ΔOI +21415张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21415张（+684.6% vs前日OI），连续性待观察（方向未知）
10-30 155.0C — Vol 4,420 | 最新价 $1.01 | OI 5104→25884 (ΔOI +20780张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20780张（+407.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 128,703 张（Put 26,860 / Call 101,843），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-30 Forward Structure
存量OI: C 209.4k / P 166.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.29 / P $5.31 ｜ ATM IV 90.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 147 ｜ Call Wall 152.5（+9.1%，弱）（OI 37.8k）
量化解读： 存量 Call 重｜ATM IV 90.4%｜历史 Rank 69%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 158 ｜ Call Wall 150（+7.3%，弱）（OI 1.3k） ｜ Put Wall 150（+7.3%，弱）（OI 2.3k）

11-13（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 144（+3.0%，弱）（OI 0.8k） ｜ Put Wall 150（+7.3%，弱）（OI 2.0k）

11-20（Activity LOW）仓位参考: Max Pain 135 ｜ Call Wall 135（-3.4%）（OI 42.3k） ｜ Put Wall 130（-7.0%，弱）（OI 4.4k）

📅 事件差分（观察，非因果）: 10-30（4D）ATM IV 90.4% vs 11-06 79.0%（差 +11.4pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/MSTR_evening.json