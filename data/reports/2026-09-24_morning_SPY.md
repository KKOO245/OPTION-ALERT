# 期权晨报 2026-09-24（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $737.14
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


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 767.81 → 今开 764.07（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 766.43 ｜ 低 763.62

Options: P/C成交量 0.97 | OI比 1.07 | ATM IV 9.8% | Skew 0.9pp | Term 1.20 | ExpMove ±0.8%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构正常偏陡（Term 1.20）｜保护溢价薄（Skew 0.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.97×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.07×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 71% ｜ P/C OI(近端) 3%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 71%）｜近端持仓极端 Call 重（P/C OI 分位 3%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-25（1D）±0.8% ｜ 09-28（4D）±0.9% ｜ 09-29（5D）±1.0% ｜ 09-30（6D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 725,647,595 | GEX Change vs 上次快照 840,483,094 | Flip: Primary Flip: 768.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2743 / LOW 276 / INVALID 1545
结构观察区: Primary Flip 768.49（全链重定价，覆盖 100%）
Call Wall 785（弱结构｜现价低于该位 1.5%）
最近结构参考: Flip 768（现价高于该位 0.6%）
量化视角： 正 Gamma（7.26亿，历史分位 71%，中性区）｜由负转正（+8.40亿）｜现价位于 Flip 上方 0.64%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 764（MaxPain，仅结算参考）；上方 785（Call Wall，弱结构）。
• Gamma 区域：切换参考 768（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
🎯 今日到期（0DTE）
存量OI: C 62.3k / P 66.7k，今日成交量: C 101.6k / P 98.2k，平值价格ATM: C $2.64 / P $1.90 ｜ ATM IV 9.8%，预期波动 ±0.6%，Max Pain 764

📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-29  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-30  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-25 Forward Structure
存量OI: C 284.9k / P 624.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.40 / P $2.43 ｜ ATM IV 10.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 766 ｜ Call Wall 772（-0.2%，弱）（OI 30.3k）
量化解读： 存量 Put 重｜ATM IV 10.2%｜历史 Rank 22%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-28（Activity LOW）仓位参考: Max Pain 770 ｜ Call Wall 780（+0.9%）（OI 10.8k） ｜ Put Wall 770（-0.4%，弱）（OI 3.5k）

09-29（Activity LOW）仓位参考: Max Pain 766 ｜ Call Wall 771（-0.3%，弱）（OI 1.0k）

09-30（Activity LOW）仓位参考: Max Pain 761 ｜ Call Wall 786（+1.6%，弱）（OI 21.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/SPY_morning.json