# 期权晚报 2026-11-10（快照 16:40 ET）

📊 市场环境

SPY $749.92 ｜ QQQ $674.76
VIX 19.46 ↓2.3%（5D -6.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 900C ΔOI +961（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 861.34 → 收盘 859.99（-0.2%） ｜ 今日高 914.82 ｜ 低 826.67 ｜ 昨收 886.51 → 收盘 859.99（-3.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.74 | OI比 0.62 | ATM IV 111.4% | Skew 6.2pp | Term 0.82 | ExpMove ±8.2%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 6.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±8.2% ｜ 11-20（10D）±13.6% ｜ 11-27（17D）±17.7% ｜ 12-04（24D）±19.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,920,161 | GEX Change vs 上次快照 -2,461,726 | Flip: Primary Flip: 887.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1743 / LOW 840 / INVALID 1427
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 887.05（全链重定价，覆盖 100%）
最近结构参考: Flip 887（现价低于该位 3.1%）
量化视角： 负 Gamma（192万，无历史分位）｜由正转负（246万）｜现价位于 Flip 下方 3.05%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 900（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 887（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +8.8k / P +3.3k ｜ Activity HIGH ｜ 3D
11-20  C +3.2k / P +0.5k ｜ Activity HIGH ｜ 10D
11-27  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 17D
12-04  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 24D

📆 11-13 Forward Structure
存量OI: C 45.0k / P 28.0k，今日变化ΔOI: C +8.8k / P +3.3k，平值价格ATM: C $35.50 / P $35.10 ｜ ATM IV 111.4%，净 delta 敞口 112k shares
Top ΔOI: C 1100 +1,028 ｜ C 900 +961 ｜ C 1000 +703
仓位参考: Max Pain 900 ｜ Call Wall 900（+4.7%，弱）（OI 1.7k） ｜ Put Wall 820（-4.7%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 111.4%｜历史 Rank 69%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 112,392 股

📆 11-20 Forward Structure
存量OI: C 72.0k / P 52.6k，今日变化ΔOI: C +3.2k / P +0.5k，平值价格ATM: C $59.75 / P $57.46 ｜ ATM IV 105.3%，净 delta 敞口 106k shares
Top ΔOI: C 900 +533 ｜ C 1000 +451 ｜ C 925 +315
仓位参考: Max Pain 1,130 ｜ Call Wall 900（+4.7%，弱）（OI 1.5k） ｜ Put Wall 870（+1.2%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 105.3%｜历史 Rank 69%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 105,520 股

📆 11-27 Forward Structure
存量OI: C 16.6k / P 9.2k，今日变化ΔOI: C +0.6k / P +0.2k，平值价格ATM: C $73.80 / P $78.55 ｜ ATM IV 95.1%，净 delta 敞口 10k shares
仓位参考: Max Pain 1,150 ｜ Put Wall 930（+8.1%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 95.1%｜历史 Rank 69%（近端代理）｜IV/RV 0.76×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,896 股

📆 12-04 Forward Structure
存量OI: C 7.1k / P 5.4k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $83.00 / P $84.45 ｜ ATM IV 93.0%，净 delta 敞口 5k shares
Top ΔOI: C 980 +102 ｜ P 770 +100
仓位参考: Max Pain 1,010 ｜ Call Wall 880（+2.3%，弱）（OI 76） ｜ Put Wall 820（-4.7%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 93.0%｜历史 Rank 69%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 正 4,668 股

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 111.4% vs 11-20 105.3%（差 +6.1pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/SNDK_evening.json