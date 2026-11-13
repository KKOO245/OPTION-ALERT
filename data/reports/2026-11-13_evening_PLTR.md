# 期权晚报 2026-11-13（快照 16:40 ET）

📊 市场环境

SPY $754.37 ｜ QQQ $679.89
VIX 19.30 ↑3.2%（5D -24.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 175C ΔOI +2,017（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 171.98 → 收盘 167.99（-2.3%） ｜ 今日高 172.28 ｜ 低 164.75 ｜ 昨收 171.58 → 收盘 167.99（-2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.78 | OI比 0.66 | ATM IV 56.4% | Skew -59.8pp | Term 0.90 | ExpMove ±6.2%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -59.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±6.2% ｜ 11-27（14D）±7.9% ｜ 12-04（21D）±9.9% ｜ 12-11（28D）±11.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 15,793,096 | GEX Change vs 上次快照 -24,471,549 | Flip: Primary Flip: 163.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 408 / LOW 181 / INVALID 351
结构观察区: Primary Flip 163.45（全链重定价，覆盖 83%）
最近结构参考: Flip 163（现价高于该位 2.8%）
量化视角： 正 Gamma（1579万，无历史分位）｜正 Gamma 减弱（2447万）｜现价位于 Flip 上方 2.78%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 165（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +8.7k / P +3.2k ｜ Activity MEDIUM △ ｜ 7D
11-27  C +0.8k / P -0.1k ｜ Activity MEDIUM △ ｜ 14D
12-04  C +0.5k / P +0.5k ｜ Activity HIGH ｜ 21D
12-11  C +0.7k / P +0.9k ｜ Activity HIGH ｜ 28D

📆 11-20 Forward Structure
存量OI: C 194.9k / P 193.1k，今日变化ΔOI: C +8.7k / P +3.2k，平值价格ATM: C $5.50 / P $4.90 ｜ ATM IV 56.0%，净 delta 敞口 131k shares
Top ΔOI: C 177 +2,352 ｜ C 182 +2,079 ｜ C 175 +2,017
仓位参考: Max Pain 175 ｜ Call Wall 180（+7.1%，弱）（OI 11.9k） ｜ Put Wall 180（+7.1%，弱）（OI 9.7k）
量化解读： 存量两侧均衡｜ATM IV 56.0%｜历史 Rank 66%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 131,280 股

11-27（MEDIUM △）Top ΔOI: 145C +300 ｜ 210P -297
11-27（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 180（+7.1%，弱）（OI 1.4k） ｜ Put Wall 170（+1.2%，弱）（OI 1.3k）

📆 12-04 Forward Structure
存量OI: C 16.4k / P 13.3k，今日变化ΔOI: C +0.5k / P +0.5k，平值价格ATM: C $7.77 / P $8.81 ｜ ATM IV 50.4%，净 delta 敞口 3k shares
Top ΔOI: P 155 +276
仓位参考: Max Pain 175 ｜ Call Wall 175（+4.2%，弱）（OI 0.9k） ｜ Put Wall 155（-7.7%）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 50.4%｜历史 Rank 66%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 3,422 股

📆 12-11 Forward Structure
存量OI: C 8.8k / P 9.6k，今日变化ΔOI: C +0.7k / P +0.9k，平值价格ATM: C $9.22 / P $10.30 ｜ ATM IV 50.9%，净 delta 敞口 -6k shares
Top ΔOI: P 170 +374 ｜ C 175 +314
仓位参考: Max Pain 170 ｜ Call Wall 180（+7.1%，弱）（OI 0.8k） ｜ Put Wall 160（-4.8%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 50.9%｜历史 Rank 66%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 负 5,760 股

📅 事件差分（观察，非因果）: 11-20（7D）ATM IV 56.0% vs 11-27 50.6%（差 +5.5pp）——覆盖 PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/PLTR_evening.json