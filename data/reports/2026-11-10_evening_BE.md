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
🟡 **事件差分**: 11-13 ATM IV 114.5% vs 11-20 101.4%（差 +13.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 187P ΔOI +628（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 185.00 → 收盘 185.42（+0.2%） ｜ 今日高 194.68 ｜ 低 181.01 ｜ 昨收 193.88 → 收盘 185.42（-4.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.81 | OI比 0.77 | ATM IV 114.5% | Skew 9.8pp | Term 0.80 | ExpMove ±8.3%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 9.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±8.3% ｜ 11-20（10D）±13.3% ｜ 11-27（17D）±16.0% ｜ 12-04（24D）±18.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,916,119 | GEX Change vs 上次快照 -2,298,299 | Flip: Primary Flip: 202.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 607 / LOW 140 / INVALID 181
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 202.26（全链重定价，覆盖 100%）
Put Wall 200（现价低于该位 7.3%）
最近结构参考: Put Wall 200（现价低于该位 7.3%）
量化视角： 负 Gamma（692万，无历史分位）｜负 Gamma 加深（230万）｜现价位于 Flip 下方 8.33%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall） / 190（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 202（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +10.5k / P +7.6k ｜ Activity HIGH ｜ 3D
11-20  C +1.8k / P +1.4k ｜ Activity HIGH ｜ 10D
11-27  C +0.3k / P +1.2k ｜ Activity HIGH ｜ 17D
12-04  C +0.6k / P +0.8k ｜ Activity HIGH ｜ 24D

📆 11-13 Forward Structure
存量OI: C 41.2k / P 31.7k，今日变化ΔOI: C +10.5k / P +7.6k，平值价格ATM: C $7.95 / P $7.40 ｜ ATM IV 114.5%，净 delta 敞口 -94k shares
Top ΔOI: C 220 +1,198 ｜ P 157 +1,028
仓位参考: Max Pain 190 ｜ Call Wall 180（-2.9%，弱）（OI 2.1k） ｜ Put Wall 175（-5.6%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 114.5%｜历史 Rank 72%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 94,338 股

📆 11-20 Forward Structure
存量OI: C 75.5k / P 80.0k，今日变化ΔOI: C +1.8k / P +1.4k，平值价格ATM: C $12.65 / P $12.07 ｜ ATM IV 101.4%，净 delta 敞口 -11k shares
Top ΔOI: C 222 +680 ｜ P 187 +628 ｜ C 195 +557
仓位参考: Max Pain 220 ｜ Call Wall 200（+7.9%，弱）（OI 3.4k） ｜ Put Wall 200（+7.9%，弱）（OI 5.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 101.4%｜历史 Rank 72%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 10,552 股

📆 11-27 Forward Structure
存量OI: C 8.6k / P 10.2k，今日变化ΔOI: C +0.3k / P +1.2k，平值价格ATM: C $15.25 / P $14.35 ｜ ATM IV 92.0%，净 delta 敞口 -30k shares
Top ΔOI: P 175 +357 ｜ P 177 +284
仓位参考: Max Pain 220 ｜ Call Wall 200（+7.9%，弱）（OI 0.6k） ｜ Put Wall 190（+2.5%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 92.0%｜历史 Rank 72%（近端代理）｜IV/RV 0.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 30,246 股

📆 12-04 Forward Structure
存量OI: C 6.2k / P 6.6k，今日变化ΔOI: C +0.6k / P +0.8k，平值价格ATM: C $17.50 / P $17.10 ｜ ATM IV 91.0%，净 delta 敞口 -15k shares
Top ΔOI: P 185 +477 ｜ C 205 +291 ｜ P 200 +180
仓位参考: Max Pain 205 ｜ Call Wall 200（+7.9%，弱）（OI 0.5k） ｜ Put Wall 200（+7.9%）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 91.0%｜历史 Rank 72%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 负 14,838 股

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 114.5% vs 11-20 101.4%（差 +13.1pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/BE_evening.json