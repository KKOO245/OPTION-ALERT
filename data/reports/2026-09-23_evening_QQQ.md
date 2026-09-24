# 期权晚报 2026-09-23（快照 21:00 ET）

📊 市场环境

SPY $767.81 ｜ QQQ $nan
VIX 15.18 ↑2.1%（5D -11.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布　✅ 今日已公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 746.99 → 收盘 741.21（-0.8%） ｜ 今日高 747.12 ｜ 低 738.19 ｜ 昨收 747.46 → 收盘 741.21（-0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.75 | OI比 1.28 | ATM IV 17.0% | Skew 1.9pp | Term 1.07 | ExpMove ±1.2%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构正常（Term 1.07）｜保护溢价薄（Skew 1.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.28×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 86% ｜ P/C OI(近端) 20%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 86%）｜近端持仓结构中性（P/C OI 分位 20%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-24（1D）±1.2% ｜ 09-25（2D）±1.5% ｜ 09-28（5D）±1.8% ｜ 09-29（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 422,037,198 | GEX Change vs 上次快照 -241,174,451 | Flip: Primary Flip: 729.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 3040 / LOW 146 / INVALID 1622
结构观察区: Primary Flip 729.53（全链重定价，覆盖 100%）
Call Wall 725（弱结构｜现价高于该位 2.2%）
最近结构参考: Flip 730（现价高于该位 1.6%）
量化视角： 正 Gamma（4.22亿，历史分位偏正区，比 86% 的交易日更正）｜正 Gamma 减弱（2.41亿）｜现价位于 Flip 上方 1.60%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 728（MaxPain，仅结算参考） / 725（Call Wall，弱结构）。
• Gamma 区域：切换参考 730（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-24  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-29  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-24 Forward Structure
存量OI: C 42.1k / P 53.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $7.66 / P $1.34 ｜ ATM IV 17.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 728 ｜ Call Wall 732（-1.2%，弱）（OI 4.5k） ｜ Put Wall 735（-0.8%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 17.0%｜历史 Rank 42%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 726 ｜ Call Wall 755（+1.9%，弱）（OI 13.0k）

09-28（Activity LOW）仓位参考: Max Pain 730 ｜ Call Wall 750（+1.2%，弱）（OI 1.9k） ｜ Put Wall 723（-2.5%，弱）（OI 3.0k）

09-29（Activity LOW）仓位参考: Max Pain 725 ｜ Call Wall 740（-0.2%，弱）（OI 0.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/QQQ_evening.json