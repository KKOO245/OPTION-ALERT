# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 111.7% vs 11-20 99.9%（差 +11.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 888.10 → 收盘 937.46（+5.6%） ｜ 今日高 953.18 ｜ 低 869.49 ｜ 昨收 977.69 → 收盘 937.46（-4.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.68 | OI比 0.67 | ATM IV 111.7% | Skew 8.6pp | Term 0.79 | ExpMove ±4.7%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价显著（Skew 8.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±4.7% ｜ 11-20（8D）±11.9% ｜ 11-27（15D）±14.3% ｜ 12-04（22D）±17.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 804,155 | GEX Change vs 上次快照 -313,710 | Flip: Primary Flip: 929.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2006 / LOW 796 / INVALID 1230
结构观察区: Primary Flip 929.85（全链重定价，覆盖 98%）
最近结构参考: Flip 930（现价高于该位 0.8%）
量化视角： 正 Gamma（80万，无历史分位）｜正 Gamma 减弱（31万）｜现价位于 Flip 上方 0.82%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 930（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 930（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +6.4k / P +6.1k ｜ Activity HIGH ｜ 1D
11-20  C +2.0k / P +1.7k ｜ Activity MEDIUM △ ｜ 8D
11-27  C -0.7k / P +0.3k ｜ Activity MEDIUM △ ｜ 15D
12-04  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 22D

📆 11-13 Forward Structure
存量OI: C 54.7k / P 36.7k，今日变化ΔOI: C +6.4k / P +6.1k，平值价格ATM: C $22.86 / P $21.24 ｜ ATM IV 111.7%，净 delta 敞口 -363k shares
Top ΔOI: C 1050 +927
仓位参考: Max Pain 930 ｜ Call Wall 1000（+6.7%，弱）（OI 2.3k） ｜ Put Wall 850（-9.3%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 111.7%｜历史 Rank 69%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 362,729 股

11-20（MEDIUM △）Top ΔOI: 1080C -580 ｜ 1030C +468
11-20（MEDIUM △）仓位参考: Max Pain 1,100 ｜ Call Wall 1000（+6.7%，弱）（OI 2.1k） ｜ Put Wall 870（-7.2%，弱）（OI 2.4k）

11-27（MEDIUM △）Top ΔOI: 1300C -1,259 ｜ 1270C -447
11-27（MEDIUM △）仓位参考: Max Pain 1,130 ｜ Put Wall 930（-0.8%，弱）（OI 0.2k）

📆 12-04 Forward Structure
存量OI: C 8.6k / P 5.9k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $84.50 / P $83.50 ｜ ATM IV 89.2%，净 delta 敞口 8k shares
Top ΔOI: C 1000 +76 ｜ C 970 +55
仓位参考: Max Pain 990 ｜ Call Wall 950（+1.3%，弱）（OI 0.2k） ｜ Put Wall 970（+3.5%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 89.2%｜历史 Rank 69%（近端代理）｜IV/RV 0.67×（近似）｜净 delta 敞口 正 7,688 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 111.7% vs 11-20 99.9%（差 +11.8pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/SNDK_evening.json