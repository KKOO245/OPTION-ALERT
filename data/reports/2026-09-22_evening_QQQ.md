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


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 741.01 → 收盘 747.46（+0.9%） ｜ 今日高 748.35 ｜ 低 741.00 ｜ 昨收 741.47 → 收盘 747.46（+0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.95 | OI比 1.40 | ATM IV 15.0% | Skew 1.4pp | Term 1.18 | ExpMove ±0.6%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常偏陡（Term 1.18）｜保护溢价薄（Skew 1.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.40×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 94% ｜ P/C OI(近端) 28%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 94%）｜近端持仓结构中性（P/C OI 分位 28%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-23（1D）±0.6% ｜ 09-24（2D）±0.9% ｜ 09-25（3D）±1.2% ｜ 09-28（6D）±1.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 639,180,430 | GEX Change vs 上次快照 4,216,876 | Flip: Primary Flip: 733.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3188 / LOW 189 / INVALID 1797
结构观察区: Primary Flip 733.31（全链重定价，覆盖 99%）
最近结构参考: Flip 733（现价高于该位 1.9%）
量化视角： 正 Gamma（6.39亿，历史分位偏正区，比 94% 的交易日更正）｜正 Gamma 增强（+422万）｜现价位于 Flip 上方 1.93%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 731（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 733（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-23  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-24  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-23 Forward Structure
存量OI: C 78.7k / P 110.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.49 / P $2.20 ｜ ATM IV 15.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 731 ｜ Call Wall 755（+1.0%，弱）（OI 7.4k） ｜ Put Wall 735（-1.7%，弱）（OI 7.8k）
量化解读： 存量 Put 重｜ATM IV 15.0%｜历史 Rank 29%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-24（Activity LOW）仓位参考: Max Pain 728 ｜ Call Wall 732（-2.1%，弱）（OI 4.5k） ｜ Put Wall 735（-1.7%，弱）（OI 1.9k）

09-25（Activity LOW）仓位参考: Max Pain 726 ｜ Call Wall 755（+1.0%，弱）（OI 13.0k）

09-28（Activity LOW）仓位参考: Max Pain 730 ｜ Call Wall 750（+0.3%，弱）（OI 1.9k） ｜ Put Wall 730（-2.3%，弱）（OI 2.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/QQQ_evening.json