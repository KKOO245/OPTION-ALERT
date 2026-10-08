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


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 576.72 → 收盘 582.82（+1.1%） ｜ 今日高 583.89 ｜ 低 574.13 ｜ 昨收 589.45 → 收盘 582.82（-1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 2.88 | OI比 1.97 | ATM IV 34.3% | Skew 3.6pp | Term 1.06 | ExpMove ±1.9%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构正常（Term 1.06）｜保护溢价中性（Skew 3.6pp）｜当日成交偏 Put（P/C量 2.88）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.88×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.97×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±1.9% ｜ 10-16（9D）±7.2% ｜ 10-23（16D）±2.8% ｜ 10-30（23D）±8.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,200,514 | GEX Change vs 上次快照 4,549,214 | Flip: Primary Flip: 578.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 551 / LOW 292 / INVALID 679
结构观察区: Primary Flip 578.33（全链重定价，覆盖 96%）
Call Wall 600（现价低于该位 2.9%）
最近结构参考: Flip 578（现价高于该位 0.8%）
量化视角： 正 Gamma（320万，无历史分位）｜由负转正（+455万）｜现价位于 Flip 上方 0.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 570（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 578（全链重定价，覆盖 96%）。
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
存量OI: C 5.7k / P 11.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.90 / P $5.10 ｜ ATM IV 34.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 570 ｜ Put Wall 555（-4.8%）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 34.3%｜历史 Rank 54%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 530 ｜ Call Wall 600（+2.9%）（OI 8.7k）

10-23（Activity LOW）仓位参考: Max Pain 555 ｜ Call Wall 555（-4.8%，弱）（OI 92）

10-30（Activity LOW）仓位参考: Max Pain 560 ｜ Put Wall 550（-5.6%，弱）（OI 3.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/SOXX_evening.json