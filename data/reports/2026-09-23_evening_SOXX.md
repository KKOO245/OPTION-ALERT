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


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 570.28 → 收盘 565.72（-0.8%） ｜ 今日高 571.55 ｜ 低 557.07 ｜ 昨收 572.78 → 收盘 565.72（-1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.05 | OI比 1.49 | ATM IV 36.9% | Skew -0.8pp | Term 1.05 | ExpMove ±2.9%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构正常（Term 1.05）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.49×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（2D）±2.9% ｜ 10-02（9D）±4.6% ｜ 10-09（16D）±6.4% ｜ 10-16（23D）±8.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,896,679 | GEX Change vs 上次快照 -4,261,845 | Flip: Primary Flip: 545.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 564 / LOW 266 / INVALID 676
结构观察区: Primary Flip 545.22（全链重定价，覆盖 98%）
Call Wall 600（现价低于该位 5.7%）
最近结构参考: Flip 545（现价高于该位 3.8%）
量化视角： 正 Gamma（1090万，无历史分位）｜正 Gamma 减弱（426万）｜现价位于 Flip 上方 3.76%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 530（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 545（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-25 Forward Structure
存量OI: C 11.5k / P 17.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $12.10 / P $4.51 ｜ ATM IV 36.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 530 ｜ Call Wall 580（+2.5%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 36.9%｜历史 Rank 61%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 520 ｜ Call Wall 542.5（-4.1%，弱）（OI 2.8k）

10-09（Activity LOW）仓位参考: Max Pain 518 ｜ Call Wall 537.5（-5.0%，弱）（OI 0.4k）

10-16（Activity LOW）仓位参考: Max Pain 525 ｜ Call Wall 600（+6.1%）（OI 13.6k） ｜ Put Wall 530（-6.3%，弱）（OI 2.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/SOXX_evening.json