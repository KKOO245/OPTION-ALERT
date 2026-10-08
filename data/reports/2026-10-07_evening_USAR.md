# 期权晚报 2026-10-07（快照 21:00 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $757.73
VIX 15.08 ↑0.5%（5D -7.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 13.35 → 收盘 13.23（-0.9%） ｜ 今日高 13.39 ｜ 低 13.03 ｜ 昨收 13.74 → 收盘 13.23（-3.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-12，窗口结束前不做对错判定）

Options: P/C成交量 0.46 | OI比 0.40 | ATM IV 67.8% | Skew -1.0pp | Term 1.02 | ExpMove ±4.2%（近端） | Rank 4%
量化视角： IV 历史低位（Rank 4%，期权偏便宜）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -1.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±4.2% ｜ 10-16（9D）±7.9% ｜ 10-23（16D）±11.0% ｜ 10-30（23D）±13.2%
   ⇒ IV–VIX Spread: +52.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,404,696 | GEX Change vs 上次快照 -663,292 | Flip: Primary Flip: 13.78（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 207 / LOW 79 / INVALID 104
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 13.78（全链重定价，覆盖 100%）
最近结构参考: Flip 14（现价低于该位 4.0%）
量化视角： 负 Gamma（340万，无历史分位）｜负 Gamma 加深（66万）｜现价位于 Flip 下方 4.00%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 10-09 Forward Structure
存量OI: C 19.0k / P 7.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.40 / P $0.16 ｜ ATM IV 67.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 14 ｜ Call Wall 14.5（+9.6%，弱）（OI 3.3k） ｜ Put Wall 13（-1.7%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 67.8%｜历史 Rank 4%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 14（+5.8%，弱）（OI 2.0k）

10-23（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 14（+5.8%，弱）（OI 0.6k）

10-30（Activity LOW）仓位参考: Max Pain 16 ｜ Call Wall 14（+5.8%，弱）（OI 0.3k） ｜ Put Wall 14（+5.8%）（OI 2.5k）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 67.8% vs 10-16 60.4%（差 +7.4pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/USAR_evening.json