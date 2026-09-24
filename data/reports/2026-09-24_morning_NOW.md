# 期权晨报 2026-09-24（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $735.86
VIX 15.64 ↑3.0%（5D -11.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 140.78 → 今开 139.90（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 141.04 ｜ 低 137.53

Options: P/C成交量 0.29 | OI比 0.63 | ATM IV 58.6% | Skew -2.8pp | Term 0.95 | ExpMove ±4.2%（近端） | Rank 39%
量化视角： IV 中性（Rank 39%）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±4.2% ｜ 10-02（8D）±7.1% ｜ 10-09（15D）±8.5% ｜ 10-16（22D）±10.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,676,486 | GEX Change vs 上次快照 -10,223,306 | Flip: Primary Flip: 133.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 614 / LOW 36 / INVALID 76
结构观察区: Primary Flip 133.13（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 8.8%）
最近结构参考: Flip 133（现价高于该位 2.8%）
量化视角： 正 Gamma（868万，无历史分位）｜正 Gamma 减弱（1022万）｜现价位于 Flip 上方 2.80%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 136（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 8D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 15D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 09-25 Forward Structure
存量OI: C 30.0k / P 18.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.98 / P $2.74 ｜ ATM IV 58.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 136 ｜ Call Wall 150（+9.6%，弱）（OI 6.1k） ｜ Put Wall 130（-5.0%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 58.6%｜历史 Rank 39%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 132 ｜ Call Wall 150（+9.6%）（OI 2.3k） ｜ Put Wall 130（-5.0%）（OI 1.1k）

10-09（Activity LOW）仓位参考: Max Pain 136 ｜ Call Wall 150（+9.6%）（OI 1.0k） ｜ Put Wall 140（+2.3%，弱）（OI 0.5k）

10-16（Activity LOW）仓位参考: Max Pain 125 ｜ Call Wall 150（+9.6%）（OI 11.2k） ｜ Put Wall 130（-5.0%，弱）（OI 4.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/NOW_morning.json