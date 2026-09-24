# 期权晨报 2026-09-24（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $737.02
VIX 15.64 ↑3.0%（5D -11.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 162.20 → 今开 161.00（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 165.14 ｜ 低 159.48

Options: P/C成交量 0.55 | OI比 0.80 | ATM IV 78.7% | Skew -10.4pp | Term 0.90 | ExpMove ±5.7%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜Put 保护异常便宜（Skew -10.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±5.7% ｜ 10-02（8D）±9.4% ｜ 10-09（15D）±12.0% ｜ 10-16（22D）±14.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 61,771,663 | GEX Change vs 上次快照 -8,118,726 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 900 / LOW 59 / INVALID 113
结构观察区: NO_CROSS
量化视角： 正 Gamma（6177万，无历史分位）｜正 Gamma 减弱（812万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 141（MaxPain，仅结算参考）。
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
存量OI: C 264.5k / P 210.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.80 / P $4.83 ｜ ATM IV 78.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 141 ｜ Call Wall 155（-7.7%，弱）（OI 20.0k） ｜ Put Wall 155（-7.7%，弱）（OI 5.6k）
量化解读： 存量 Call 重｜ATM IV 78.7%｜历史 Rank 46%（近端代理）｜IV/RV 0.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 140 ｜ Call Wall 180（+7.2%，弱）（OI 5.3k）

10-09（Activity LOW）仓位参考: Max Pain 140 ｜ Call Wall 160（-4.7%，弱）（OI 4.9k）

10-16（Activity LOW）仓位参考: Max Pain 115 ｜ Call Wall 180（+7.2%，弱）（OI 10.5k） ｜ Put Wall 160（-4.7%，弱）（OI 2.6k）

📅 事件差分（观察，非因果）: 09-25（1D）ATM IV 78.7% vs 10-02 71.9%（差 +6.8pp）——覆盖 耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/MSTR_morning.json