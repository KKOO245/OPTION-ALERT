# 期权晚报 2026-10-06（快照 21:00 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 760.54 → 收盘 759.66（-0.1%） ｜ 今日高 762.86 ｜ 低 759.10 ｜ 昨收 756.20 → 收盘 759.66（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.33 | OI比 1.72 | ATM IV 13.8% | Skew 1.7pp | Term 1.35 | ExpMove ±0.6%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构正常偏陡（Term 1.35）｜保护溢价薄（Skew 1.7pp）｜当日成交偏 Put（P/C量 1.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.33×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.72×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 95% ｜ P/C OI(近端) 57%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 95%）｜近端持仓结构中性（P/C OI 分位 57%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-07（1D）±0.6% ｜ 10-08（2D）±0.9% ｜ 10-09（3D）±1.1% ｜ 10-12（6D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 696,255,462 | GEX Change vs 上次快照 181,194,558 | Flip: Primary Flip: 748.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 3096 / LOW 176 / INVALID 1504
结构观察区: Primary Flip 748.38（全链重定价，覆盖 100%）
Call Wall 760（现价低于该位 0.0%）
最近结构参考: Call Wall 760（现价低于该位 0.0%）
量化视角： 正 Gamma（6.96亿，历史分位偏正区，比 95% 的交易日更正）｜正 Gamma 增强（+1.81亿）｜现价位于 Flip 上方 1.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 750（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 748（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-07  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-08  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-12  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-07 Forward Structure
存量OI: C 66.0k / P 113.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.29 / P $2.13 ｜ ATM IV 13.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 750 ｜ Call Wall 762（+0.3%）（OI 13.0k） ｜ Put Wall 750（-1.3%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 13.8%｜历史 Rank 23%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-08（Activity LOW）仓位参考: Max Pain 749 ｜ Call Wall 760（+0.0%，弱）（OI 1.8k） ｜ Put Wall 749（-1.4%）（OI 13.4k）

10-09（Activity LOW）仓位参考: Max Pain 747 ｜ Call Wall 754（-0.7%）（OI 21.2k） ｜ Put Wall 750（-1.3%，弱）（OI 8.6k）

10-12（Activity LOW）仓位参考: Max Pain 750 ｜ Call Wall 755（-0.6%，弱）（OI 1.3k） ｜ Put Wall 738（-2.9%）（OI 12.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/QQQ_evening.json