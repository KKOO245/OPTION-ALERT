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


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 749.34 → 收盘 756.20（+0.9%） ｜ 今日高 756.91 ｜ 低 749.08 ｜ 昨收 749.58 → 收盘 756.20（+0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 2.57 | OI比 3.07 | ATM IV 14.6% | Skew 1.8pp | Term 1.31 | ExpMove ±0.6%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常偏陡（Term 1.31）｜保护溢价薄（Skew 1.8pp）｜当日成交偏 Put（P/C量 2.57）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.57×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 3.07×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 91% ｜ P/C OI(近端) 98%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 91%）｜近端 Put 显著偏重（P/C OI 分位 98%，历史高位区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-06（1D）±0.6% ｜ 10-07（2D）±0.9% ｜ 10-08（3D）±1.2% ｜ 10-09（4D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 561,415,818 | GEX Change vs 上次快照 175,838,122 | Flip: Primary Flip: 745.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2792 / LOW 183 / INVALID 1823
结构观察区: Primary Flip 745.16（全链重定价，覆盖 99%）
Call Wall 760（现价低于该位 0.5%）
最近结构参考: Call Wall 760（现价低于该位 0.5%）
量化视角： 正 Gamma（5.61亿，历史分位偏正区，比 91% 的交易日更正）｜正 Gamma 增强（+1.76亿）｜现价位于 Flip 上方 1.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 745（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 745（全链重定价，覆盖 99%）。
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
存量OI: C 33.7k / P 103.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.40 / P $2.28 ｜ ATM IV 14.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 745 ｜ Call Wall 770（+1.8%，弱）（OI 2.9k） ｜ Put Wall 740（-2.1%）（OI 25.5k）
量化解读： 存量 Put 重｜ATM IV 14.6%｜历史 Rank 28%（近端代理）｜IV/RV 1.03×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-07（Activity LOW）仓位参考: Max Pain 743 ｜ Call Wall 760（+0.5%）（OI 5.4k）

10-08（Activity LOW）仓位参考: Max Pain 745 ｜ Call Wall 740（-2.1%，弱）（OI 1.5k） ｜ Put Wall 749（-1.0%，弱）（OI 2.2k）

10-09（Activity LOW）仓位参考: Max Pain 742 ｜ Call Wall 754（-0.3%）（OI 21.1k） ｜ Put Wall 749（-1.0%，弱）（OI 7.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/QQQ_evening.json