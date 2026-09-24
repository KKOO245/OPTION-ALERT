# 期权晨报 2026-09-23（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $nan
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 34.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布　✅ 今日已公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 60.73 → 今开 59.00（-2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 59.03 ｜ 低 58.12

Options: P/C成交量 0.39 | OI比 0.71 | ATM IV 40.8% | Skew -3.9pp | Term 0.92 | ExpMove ±2.9%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -3.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（2D）±2.9% ｜ 09-28（5D）±3.3% ｜ 09-30（7D）±4.2% ｜ 10-02（9D）±5.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 119,804,187 | GEX Change vs 上次快照 0 | Flip: Primary Flip: 57.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 806 / LOW 177 / INVALID 371
结构观察区: Primary Flip 57.14（全链重定价，覆盖 98%）
Put Wall 60（弱结构｜现价高于该位 1.2%）
最近结构参考: Put Wall 60（现价高于该位 1.2%）
量化视角： 正 Gamma（1.20亿，无历史分位）｜正 Gamma 减弱（0万）｜现价位于 Flip 上方 6.29%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 60（Put Wall，弱结构） / 59（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
🎯 今日到期（0DTE）
存量OI: C 25.2k / P 18.0k，今日成交量: C 38.7k / P 15.1k，平值价格ATM: C $0.56 / P $0.47 ｜ ATM IV 40.8%，预期波动 ±1.7%，Max Pain 59

📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-30  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-25 Forward Structure
存量OI: C 111.9k / P 45.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.02 / P $0.72 ｜ ATM IV 40.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 60 ｜ Put Wall 55（-9.4%，弱）（OI 4.7k）
量化解读： 存量 Call 重｜ATM IV 40.1%｜历史 Rank 68%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-28（Activity LOW）仓位参考: Max Pain 60 ｜ Call Wall 62.5（+2.9%）（OI 2.2k） ｜ Put Wall 56（-7.8%，弱）（OI 1.3k）

09-30（Activity LOW）仓位参考: Max Pain 62 ｜ Put Wall 58（-4.5%，弱）（OI 3.3k）

10-02（Activity LOW）仓位参考: Max Pain 59 ｜ Call Wall 66（+8.7%，弱）（OI 9.6k） ｜ Put Wall 56（-7.8%，弱）（OI 3.8k）

📅 事件差分（观察，非因果）: 09-25（2D）ATM IV 40.1% vs 09-28 33.4%（差 +6.7pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/SLV_morning.json