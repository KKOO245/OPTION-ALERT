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

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 775.77 → 收盘 777.22（+0.2%） ｜ 今日高 779.10 ｜ 低 773.61 ｜ 昨收 779.09 → 收盘 777.22（-0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.37 | OI比 1.38 | ATM IV 10.2% | Skew 1.0pp | Term 1.24 | ExpMove ±0.4%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常偏陡（Term 1.24）｜保护溢价薄（Skew 1.0pp）｜当日成交偏 Put（P/C量 1.37）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.37×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 65% ｜ P/C OI(近端) 15%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 65%）｜近端持仓结构中性（P/C OI 分位 15%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-08（1D）±0.4% ｜ 10-09（2D）±0.6% ｜ 10-12（5D）±0.8% ｜ 10-13（6D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 466,587,661 | GEX Change vs 上次快照 688,068,718 | Flip: Primary Flip: 775.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 2555 / LOW 345 / INVALID 1660
结构观察区: Primary Flip 775.54（全链重定价，覆盖 97%）
Call Wall 785（弱结构｜现价低于该位 1.0%）
最近结构参考: Flip 776（现价高于该位 0.2%）
量化视角： 正 Gamma（4.67亿，历史分位 65%，中性区）｜由负转正（+6.88亿）｜现价位于 Flip 上方 0.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 775（MaxPain，仅结算参考）；上方 785（Call Wall，弱结构）。
• Gamma 区域：切换参考 776（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-08  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-12  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-13  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-08 Forward Structure
存量OI: C 82.3k / P 113.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.89 / P $1.46 ｜ ATM IV 10.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 775 ｜ Call Wall 796（+2.4%，弱）（OI 7.0k） ｜ Put Wall 770（-0.9%，弱）（OI 4.0k）
量化解读： 存量 Put 重｜ATM IV 10.2%｜历史 Rank 26%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-09（Activity LOW）仓位参考: Max Pain 772 ｜ Call Wall 785（+1.0%）（OI 123.0k） ｜ Put Wall 767（-1.3%，弱）（OI 70.5k）

10-12（Activity LOW）仓位参考: Max Pain 775 ｜ Call Wall 800（+2.9%，弱）（OI 3.7k） ｜ Put Wall 770（-0.9%，弱）（OI 3.5k）

10-13（Activity LOW）仓位参考: Max Pain 775 ｜ Call Wall 780（+0.4%，弱）（OI 1.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/SPY_evening.json