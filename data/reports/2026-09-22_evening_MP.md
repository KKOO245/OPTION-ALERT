# 期权晚报 2026-09-22（快照 21:00 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $nan
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

🔍 重点速览
🟡 **事件差分**: 09-25 ATM IV 74.6% vs 10-02 64.6%（差 +10.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 50.68 → 收盘 51.04（+0.7%） ｜ 今日高 51.33 ｜ 低 48.67 ｜ 昨收 50.00 → 收盘 51.04（+2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.63 | OI比 0.78 | ATM IV 74.6% | Skew -8.6pp | Term 0.77 | ExpMove ±5.3%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±5.3% ｜ 10-02（10D）±8.4% ｜ 10-09（17D）±10.2% ｜ 10-16（24D）±13.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,006,645 | GEX Change vs 上次快照 2,540,155 | Flip: Primary Flip: 49.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 310 / LOW 62 / INVALID 112
结构观察区: Primary Flip 49.20（全链重定价，覆盖 99%）
Put Wall 55（弱结构｜现价低于该位 7.2%） | Call Wall 55（弱结构｜现价低于该位 7.2%）
最近结构参考: Flip 49（现价高于该位 3.7%）
量化视角： 正 Gamma（301万，无历史分位）｜正 Gamma 增强（+254万）｜现价位于 Flip 上方 3.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（MaxPain，仅结算参考）；上方 55（Put Wall，弱结构） / 55（Call Wall，弱结构）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 09-25 Forward Structure
存量OI: C 13.8k / P 10.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.49 / P $1.22 ｜ ATM IV 74.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 50 ｜ Call Wall 55（+7.8%，弱）（OI 1.9k） ｜ Put Wall 47（-7.9%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 74.6%｜历史 Rank 61%（近端代理）｜IV/RV 1.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 49（-4.0%，弱）（OI 1.2k） ｜ Put Wall 50（-2.0%）（OI 1.3k）

10-09（Activity LOW）仓位参考: Max Pain 52 ｜ Call Wall 55（+7.8%）（OI 1.2k） ｜ Put Wall 47（-7.9%）（OI 1.1k）

10-16（Activity LOW）仓位参考: Max Pain 55 ｜ Call Wall 50（-2.0%，弱）（OI 2.8k） ｜ Put Wall 55（+7.8%，弱）（OI 4.0k）

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 74.6% vs 10-02 64.6%（差 +10.0pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/MP_evening.json