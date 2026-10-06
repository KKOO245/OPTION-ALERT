# 期权晚报 2026-10-05（快照 21:00 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $nan
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 586.76 → 收盘 589.51（+0.5%） ｜ 今日高 589.62 ｜ 低 582.08 ｜ 昨收 588.90 → 收盘 589.51（+0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 4.45 | OI比 1.23 | ATM IV 30.9% | Skew 2.9pp | Term 1.21 | ExpMove ±2.6%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常偏陡（Term 1.21）｜保护溢价中性（Skew 2.9pp）｜当日成交偏 Put（P/C量 4.45）——观察点，非方向信号
   ⇒ Put/Call Volume: 4.45×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±2.6% ｜ 10-16（11D）±4.4% ｜ 10-23（18D）±6.2% ｜ 10-30（25D）±7.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,757,290 | GEX Change vs 上次快照 2,986,895 | Flip: Primary Flip: 569.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 463 / LOW 264 / INVALID 773
结构观察区: Primary Flip 569.93（全链重定价，覆盖 89%）
Call Wall 600（现价低于该位 1.7%）
最近结构参考: Call Wall 600（现价低于该位 1.7%）
量化视角： 正 Gamma（876万，无历史分位）｜正 Gamma 增强（+299万）｜现价位于 Flip 上方 3.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 550（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 570（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-09 Forward Structure
存量OI: C 5.3k / P 6.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $7.70 / P $7.80 ｜ ATM IV 30.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 550 ｜ Put Wall 570（-3.3%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 30.9%｜历史 Rank 40%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 530 ｜ Call Wall 600（+1.8%）（OI 9.1k）

10-23（Activity LOW）仓位参考: Max Pain 540 ｜ Call Wall 570（-3.3%，弱）（OI 89）

10-30（Activity LOW）仓位参考: Max Pain 555

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/SOXX_evening.json