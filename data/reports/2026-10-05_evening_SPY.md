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


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 769.69 → 收盘 774.83（+0.7%） ｜ 今日高 776.60 ｜ 低 769.69 ｜ 昨收 769.64 → 收盘 774.83（+0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.35 | OI比 0.56 | ATM IV 9.7% | Skew 1.1pp | Term 1.33 | ExpMove ±0.4%（近端） | Rank 21%
量化视角： IV 历史低位（Rank 21%，期权偏便宜）｜期限结构正常偏陡（Term 1.33）｜保护溢价薄（Skew 1.1pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.56）+ 当日成交偏 Put（P/C量 1.35）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.35×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 72% ｜ P/C OI(近端) 0%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 72%）｜近端持仓极端 Call 重（P/C OI 分位 0%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-06（1D）±0.4% ｜ 10-07（2D）±0.6% ｜ 10-08（3D）±0.8% ｜ 10-09（4D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 796,735,185 | GEX Change vs 上次快照 638,577,928 | Flip: Primary Flip: 771.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2502 / LOW 284 / INVALID 1880
结构观察区: Primary Flip 771.47（全链重定价，覆盖 97%）
Call Wall 787（弱结构｜现价低于该位 1.5%）
最近结构参考: Flip 771（现价高于该位 0.4%）
量化视角： 正 Gamma（7.97亿，历史分位 72%，中性区）｜正 Gamma 增强（+6.39亿）｜现价位于 Flip 上方 0.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 768（MaxPain，仅结算参考）；上方 787（Call Wall，弱结构）。
• Gamma 区域：切换参考 771（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-06  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-07  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-08  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 4D

📆 10-06 Forward Structure
存量OI: C 155.5k / P 87.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.52 / P $1.64 ｜ ATM IV 9.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 768 ｜ Put Wall 760（-1.9%，弱）（OI 7.3k）
量化解读： 存量 Call 重｜ATM IV 9.7%｜历史 Rank 21%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-07（Activity LOW）仓位参考: Max Pain 768 ｜ Put Wall 760（-1.9%，弱）（OI 5.2k）

10-08（Activity LOW）仓位参考: Max Pain 766 ｜ Call Wall 795（+2.6%，弱）（OI 6.7k）

10-09（Activity LOW）仓位参考: Max Pain 767 ｜ Call Wall 787（+1.6%）（OI 234.1k） ｜ Put Wall 767（-1.0%，弱）（OI 46.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/SPY_evening.json