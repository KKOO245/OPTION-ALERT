# 期权晚报 2026-09-22（快照 16:40 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $747.46
VIX 14.21 ↓4.4%（5D -17.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 274.16 → 收盘 276.53（+0.9%） ｜ 今日高 284.25 ｜ 低 269.00 ｜ 昨收 272.89 → 收盘 276.53（+1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.73 | OI比 1.22 | ATM IV 83.3% | Skew -2.7pp | Term 0.93 | ExpMove ±5.9%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.22×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±5.9% ｜ 10-02（10D）±10.4% ｜ 10-09（17D）±13.8% ｜ 10-16（24D）±15.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,231,493 | GEX Change vs 上次快照 -105,204 | Flip: Primary Flip: 259.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 660 / LOW 94 / INVALID 174
结构观察区: Primary Flip 259.07（全链重定价，覆盖 100%）
Call Wall 270（弱结构｜现价高于该位 2.4%）
最近结构参考: Call Wall 270（现价高于该位 2.4%）
量化视角： 正 Gamma（1023万，无历史分位）｜正 Gamma 减弱（11万）｜现价位于 Flip 上方 6.74%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 262（MaxPain，仅结算参考） / 270（Call Wall，弱结构）。
• Gamma 区域：切换参考 259（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +8.4k / P +6.7k ｜ Activity HIGH ｜ 3D
10-02  C +1.6k / P +2.1k ｜ Activity HIGH ｜ 10D
10-09  C +0.4k / P +0.5k ｜ Activity HIGH ｜ 17D
10-16  C +3.3k / P +4.0k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 37.2k / P 45.5k，今日变化ΔOI: C +8.4k / P +6.7k，平值价格ATM: C $7.80 / P $8.55 ｜ ATM IV 83.3%，净 delta 敞口 36k shares
Top ΔOI: C 300 +1,383 ｜ P 250 +856
仓位参考: Max Pain 262 ｜ Call Wall 300（+8.5%，弱）（OI 4.2k） ｜ Put Wall 250（-9.6%，弱）（OI 4.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 83.3%｜历史 Rank 42%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,167 股

📆 10-02 Forward Structure
存量OI: C 19.5k / P 17.5k，今日变化ΔOI: C +1.6k / P +2.1k，平值价格ATM: C $14.10 / P $14.65 ｜ ATM IV 78.2%，净 delta 敞口 12k shares
Top ΔOI: P 245 +231 ｜ C 290 +228
仓位参考: Max Pain 250 ｜ Call Wall 270（-2.4%）（OI 5.5k） ｜ Put Wall 250（-9.6%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.2%｜历史 Rank 42%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 12,172 股

📆 10-09 Forward Structure
存量OI: C 4.3k / P 7.7k，今日变化ΔOI: C +0.4k / P +0.5k，平值价格ATM: C $19.00 / P $19.06 ｜ ATM IV 77.0%，净 delta 敞口 -1k shares
Top ΔOI: P 260 +67
仓位参考: Max Pain 255 ｜ Call Wall 295（+6.7%）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 77.0%｜历史 Rank 42%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 负 1,455 股

📆 10-16 Forward Structure
存量OI: C 64.8k / P 70.1k，今日变化ΔOI: C +3.3k / P +4.0k，平值价格ATM: C $20.79 / P $22.38 ｜ ATM IV 77.4%，净 delta 敞口 1k shares
Top ΔOI: C 280 -799 ｜ P 257 +628
仓位参考: Max Pain 252 ｜ Call Wall 280（+1.3%，弱）（OI 8.2k） ｜ Put Wall 260（-6.0%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜ATM IV 77.4%｜历史 Rank 42%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 1,037 股

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 83.3% vs 10-02 78.2%（差 +5.1pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/BE_evening.json