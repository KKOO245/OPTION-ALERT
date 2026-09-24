# 期权晨报 2026-09-23（快照 10:20 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $nan
VIX 14.54 ↓2.2%（5D -15.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 34.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布　✅ 今日已公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 747.46 → 今开 746.99（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 747.12 ｜ 低 738.66

Options: P/C成交量 0.95 | OI比 1.40 | ATM IV 14.8% | Skew 1.4pp | Term 1.20 | ExpMove ±0.9%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常偏陡（Term 1.20）｜保护溢价薄（Skew 1.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.40×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 94% ｜ P/C OI(近端) 28%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 94%）｜近端持仓结构中性（P/C OI 分位 28%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-24（1D）±0.9% ｜ 09-25（2D）±1.2% ｜ 09-28（5D）±1.4% ｜ 09-29（6D）±1.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 663,211,649 | GEX Change vs 上次快照 24,031,219 | Flip: Primary Flip: 733.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3188 / LOW 189 / INVALID 1797
结构观察区: Primary Flip 733.33（全链重定价，覆盖 99%）
最近结构参考: Flip 733（现价高于该位 2.0%）
量化视角： 正 Gamma（6.63亿，历史分位偏正区，比 94% 的交易日更正）｜正 Gamma 增强（+2403万）｜现价位于 Flip 上方 2.04%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 731（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 733（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
🎯 今日到期（0DTE）
存量OI: C 78.7k / P 110.0k，今日成交量: C 505.1k / P 478.8k，平值价格ATM: C $1.98 / P $2.67 ｜ ATM IV 14.8%，预期波动 ±0.6%，Max Pain 731

📆 Forward Expiration Structure

09-24  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-29  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-24 Forward Structure
存量OI: C 42.1k / P 53.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.10 / P $3.67 ｜ ATM IV 15.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 728 ｜ Call Wall 732（-2.2%，弱）（OI 4.5k） ｜ Put Wall 735（-1.8%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 15.3%｜历史 Rank 28%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 726 ｜ Call Wall 755（+0.9%，弱）（OI 13.0k）

09-28（Activity LOW）仓位参考: Max Pain 730 ｜ Call Wall 750（+0.2%，弱）（OI 1.9k） ｜ Put Wall 730（-2.4%，弱）（OI 2.9k）

09-29（Activity LOW）仓位参考: Max Pain 725 ｜ Call Wall 740（-1.1%，弱）（OI 0.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/QQQ_morning.json