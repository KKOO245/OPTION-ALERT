# 期权晚报 2026-09-23（快照 21:00 ET）

📊 市场环境

SPY $767.81 ｜ QQQ $nan
VIX 15.18 ↑2.1%（5D -11.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布　✅ 今日已公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 228.08 → 收盘 225.51（-1.1%） ｜ 今日高 228.95 ｜ 低 224.02 ｜ 昨收 228.87 → 收盘 225.51（-1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.50 | OI比 0.68 | ATM IV 32.1% | Skew 0.4pp | Term 0.99 | ExpMove ±2.8%（近端） | Rank 11%
量化视角： IV 历史低位（Rank 11%，期权偏便宜）｜期限结构正常（Term 0.99）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（2D）±2.8% ｜ 09-28（5D）±3.2% ｜ 09-30（7D）±3.9% ｜ 10-02（9D）±4.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 572,185,119 | GEX Change vs 上次快照 -210,173,379 | Flip: Primary Flip: 214.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 679 / LOW 179 / INVALID 388
结构观察区: Primary Flip 214.44（全链重定价，覆盖 100%）
Call Wall 230（弱结构｜现价低于该位 2.0%）
最近结构参考: Call Wall 230（现价低于该位 2.0%）
量化视角： 正 Gamma（5.72亿，无历史分位）｜正 Gamma 减弱（2.10亿）｜现价位于 Flip 上方 5.16%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（MaxPain，仅结算参考）；上方 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 214（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-30  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-25 Forward Structure
存量OI: C 478.0k / P 327.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.12 / P $1.14 ｜ ATM IV 32.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 220 ｜ Call Wall 230（+2.0%，弱）（OI 78.8k） ｜ Put Wall 210（-6.9%，弱）（OI 19.9k）
量化解读： 存量 Call 重｜ATM IV 32.1%｜历史 Rank 11%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-28（Activity LOW）仓位参考: Max Pain 220 ｜ Call Wall 235（+4.2%，弱）（OI 10.1k） ｜ Put Wall 210（-6.9%，弱）（OI 3.1k）

09-30（Activity LOW）仓位参考: Max Pain 218 ｜ Call Wall 240（+6.4%）（OI 3.0k） ｜ Put Wall 212.5（-5.8%，弱）（OI 3.4k）

10-02（Activity LOW）仓位参考: Max Pain 220 ｜ Call Wall 230（+2.0%，弱）（OI 17.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/NVDA_evening.json