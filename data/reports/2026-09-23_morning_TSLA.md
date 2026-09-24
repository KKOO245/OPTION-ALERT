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


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 378.90 → 今开 379.93（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 386.70 ｜ 低 378.78

Options: P/C成交量 0.67 | OI比 0.74 | ATM IV 42.4% | Skew -2.6pp | Term 1.06 | ExpMove ±3.1%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构正常（Term 1.06）｜Put 保护异常便宜（Skew -2.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（2D）±3.1% ｜ 09-28（5D）±3.6% ｜ 09-30（7D）±4.5% ｜ 10-02（9D）±5.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 147,787,355 | GEX Change vs 上次快照 1,386,961 | Flip: Primary Flip: 358.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1250 / LOW 108 / INVALID 478
结构观察区: Primary Flip 358.72（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 5.2%）
最近结构参考: Call Wall 400（现价低于该位 5.2%）
量化视角： 正 Gamma（1.48亿，无历史分位）｜正 Gamma 增强（+139万）｜现价位于 Flip 上方 5.69%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 359（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
🎯 今日到期（0DTE）
存量OI: C 54.6k / P 40.5k，今日成交量: C 542.4k / P 365.4k，平值价格ATM: C $2.88 / P $3.95 ｜ ATM IV 42.4%，预期波动 ±1.8%，Max Pain 370

📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-30  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-25 Forward Structure
存量OI: C 188.9k / P 222.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.40 / P $6.34 ｜ ATM IV 42.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 362 ｜ Call Wall 367.5（-3.1%，弱）（OI 16.5k）
量化解读： 存量两侧均衡｜ATM IV 42.4%｜历史 Rank 14%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 0 股

09-28（Activity LOW）仓位参考: Max Pain 368 ｜ Call Wall 410（+8.1%，弱）（OI 1.4k） ｜ Put Wall 375（-1.1%，弱）（OI 0.8k）

09-30（Activity LOW）仓位参考: Max Pain 368 ｜ Call Wall 400（+5.5%，弱）（OI 0.8k） ｜ Put Wall 370（-2.4%，弱）（OI 0.6k）

10-02（Activity LOW）仓位参考: Max Pain 360 ｜ Call Wall 360（-5.1%）（OI 16.6k）

📅 事件差分（观察，非因果）: 09-25（2D）ATM IV 42.4% vs 09-28 35.5%（差 +6.9pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/TSLA_morning.json