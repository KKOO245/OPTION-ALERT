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


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 192.70 → 收盘 194.12（+0.7%） ｜ 今日高 194.70 ｜ 低 190.11 ｜ 昨收 192.07 → 收盘 194.12（+1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.43 | OI比 0.65 | ATM IV 45.1% | Skew 2.2pp | Term 1.25 | ExpMove ±2.7%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构正常偏陡（Term 1.25）｜保护溢价中性（Skew 2.2pp）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±2.7% ｜ 10-16（9D）±5.2% ｜ 10-23（16D）±7.0% ｜ 10-30（23D）±8.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 98,275,544 | GEX Change vs 上次快照 28,859,465 | Flip: Primary Flip: 185.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 517 / LOW 108 / INVALID 187
结构观察区: Primary Flip 185.08（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 2.9%）
最近结构参考: Call Wall 200（现价低于该位 2.9%）
量化视角： 正 Gamma（9828万，无历史分位）｜正 Gamma 增强（+2886万）｜现价位于 Flip 上方 4.89%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 188（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 185（全链重定价，覆盖 100%）。
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
存量OI: C 122.3k / P 79.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.20 / P $3.00 ｜ ATM IV 45.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 188 ｜ Call Wall 205（+5.6%，弱）（OI 20.5k） ｜ Put Wall 185（-4.7%，弱）（OI 8.1k）
量化解读： 存量 Call 重｜ATM IV 45.1%｜历史 Rank 30%（近端代理）｜IV/RV 2.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 200（+3.0%）（OI 16.9k） ｜ Put Wall 175（-9.8%，弱）（OI 8.2k）

10-23（Activity LOW）仓位参考: Max Pain 180 ｜ Call Wall 180（-7.3%）（OI 4.7k） ｜ Put Wall 175（-9.8%，弱）（OI 2.1k）

10-30（Activity LOW）仓位参考: Max Pain 185 ｜ Call Wall 200（+3.0%，弱）（OI 3.3k） ｜ Put Wall 180（-7.3%，弱）（OI 1.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/PLTR_evening.json