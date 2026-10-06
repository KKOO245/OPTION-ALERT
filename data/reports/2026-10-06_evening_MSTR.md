# 期权晚报 2026-10-06（快照 16:40 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 160P ΔOI +1,343（距现价 -2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 165.82 → 收盘 164.55（-0.8%） ｜ 今日高 168.73 ｜ 低 163.18 ｜ 昨收 164.43 → 收盘 164.55（+0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.49 | OI比 0.73 | ATM IV 65.7% | Skew -6.1pp | Term 0.90 | ExpMove ±4.8%（近端） | Rank 21%
量化视角： IV 历史低位（Rank 21%，期权偏便宜）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -6.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±4.8% ｜ 10-16（10D）±8.0% ｜ 10-23（17D）±10.3% ｜ 10-30（24D）±12.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 80,251,136 | GEX Change vs 上次快照 -11,377,069 | Flip: Primary Flip: 149.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 597 / LOW 88 / INVALID 247
结构观察区: Primary Flip 149.96（全链重定价，覆盖 98%）
最近结构参考: Flip 150（现价高于该位 9.7%）
量化视角： 正 Gamma（8025万，无历史分位）｜正 Gamma 减弱（1138万）｜现价位于 Flip 上方 9.73%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 150（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +8.4k / P +3.0k ｜ Activity MEDIUM △ ｜ 3D
10-16  C -0.5k / P +5.5k ｜ Activity MEDIUM △ ｜ 10D
10-23  C +0.9k / P +2.0k ｜ Activity HIGH ｜ 17D
10-30  C +0.4k / P +4.1k ｜ Activity MEDIUM △ ｜ 24D

📆 10-09 Forward Structure
存量OI: C 210.4k / P 153.6k，今日变化ΔOI: C +8.4k / P +3.0k，平值价格ATM: C $3.80 / P $4.12 ｜ ATM IV 65.7%，净 delta 敞口 -59k shares
Top ΔOI: C 185 +2,089 ｜ C 175 +1,678 ｜ P 160 +1,343
仓位参考: Max Pain 155 ｜ Call Wall 165（+0.3%，弱）（OI 25.3k）
量化解读： 存量 Call 重｜ATM IV 65.7%｜历史 Rank 21%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 59,346 股

10-16（MEDIUM △）Top ΔOI: 180C -1,467
10-16（MEDIUM △）仓位参考: Max Pain 130 ｜ Call Wall 155（-5.8%，弱）（OI 10.5k） ｜ Put Wall 150（-8.8%，弱）（OI 4.8k）

📆 10-23 Forward Structure
存量OI: C 25.5k / P 36.9k，今日变化ΔOI: C +0.9k / P +2.0k，平值价格ATM: C $8.25 / P $8.75 ｜ ATM IV 60.5%，净 delta 敞口 4k shares
仓位参考: Max Pain 160 ｜ Call Wall 172.5（+4.8%，弱）（OI 2.5k） ｜ Put Wall 155（-5.8%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 60.5%｜历史 Rank 21%（近端代理）｜IV/RV 0.82×（近似）｜净 delta 敞口 正 4,249 股

10-30（MEDIUM △）Top ΔOI: 125P +2,273 ｜ 210C +525
10-30（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 162.5（-1.2%，弱）（OI 2.6k） ｜ Put Wall 160（-2.8%，弱）（OI 2.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/MSTR_evening.json