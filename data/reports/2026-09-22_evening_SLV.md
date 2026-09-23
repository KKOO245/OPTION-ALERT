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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 59.31 → 收盘 60.73（+2.4%） ｜ 今日高 61.00 ｜ 低 59.05 ｜ 昨收 59.63 → 收盘 60.73（+1.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.39 | OI比 0.71 | ATM IV 40.8% | Skew -3.9pp | Term 0.92 | ExpMove ±1.7%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -3.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-23（1D）±1.7% ｜ 09-25（3D）±2.9% ｜ 09-28（6D）±3.3% ｜ 09-30（8D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 119,804,187 | GEX Change vs 上次快照 36,308,995 | Flip: Primary Flip: 57.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 806 / LOW 177 / INVALID 371
结构观察区: Primary Flip 57.14（全链重定价，覆盖 98%）
Put Wall 60（弱结构｜现价高于该位 1.2%）
最近结构参考: Put Wall 60（现价高于该位 1.2%）
量化视角： 正 Gamma（1.20亿，无历史分位）｜正 Gamma 增强（+3631万）｜现价位于 Flip 上方 6.29%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 60（Put Wall，弱结构） / 59（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-23  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 6D
09-30  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 09-23 Forward Structure
存量OI: C 25.2k / P 18.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.64 / P $0.40 ｜ ATM IV 40.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 59 ｜ Call Wall 62（+2.1%）（OI 3.6k） ｜ Put Wall 55（-9.4%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 40.8%｜历史 Rank 68%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 60 ｜ Put Wall 55（-9.4%，弱）（OI 4.7k）

09-28（Activity LOW）仓位参考: Max Pain 60 ｜ Call Wall 62.5（+2.9%）（OI 2.2k） ｜ Put Wall 56（-7.8%，弱）（OI 1.3k）

09-30（Activity LOW）仓位参考: Max Pain 62 ｜ Put Wall 58（-4.5%，弱）（OI 3.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/SLV_evening.json