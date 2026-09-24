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


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 95.18 → 收盘 93.56（-1.7%） ｜ 今日高 95.27 ｜ 低 93.07 ｜ 昨收 97.83 → 收盘 93.56（-4.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.78 | OI比 0.43 | ATM IV 45.8% | Skew -1.5pp | Term 0.95 | ExpMove ±5.3%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.43）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.43×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（2D）±5.3% ｜ 10-02（9D）±6.3% ｜ 10-09（16D）±2.6% ｜ 10-16（23D）±2.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -12,787,660 | GEX Change vs 上次快照 -94,666,125 | Flip: Primary Flip: 94.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 489 / LOW 99 / INVALID 274
结构观察区: Primary Flip 94.13（全链重定价，覆盖 97%）
Put Wall 90（弱结构｜现价高于该位 4.0%）
最近结构参考: Flip 94（现价低于该位 0.6%）
量化视角： 负 Gamma（1279万，无历史分位）｜由正转负（9467万）｜现价位于 Flip 下方 0.61%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 90（Put Wall，弱结构）；上方 95（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 94（全链重定价，覆盖 97%）。
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
存量OI: C 117.5k / P 50.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.70 / P $0.31 ｜ ATM IV 45.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 95 ｜ Call Wall 97（+3.7%，弱）（OI 19.7k） ｜ Put Wall 93（-0.6%）（OI 8.5k）
量化解读： 存量 Call 重｜ATM IV 45.8%｜历史 Rank 74%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 97 ｜ Call Wall 96（+2.6%，弱）（OI 2.0k） ｜ Put Wall 97（+3.7%）（OI 11.4k）

10-09（Activity LOW）仓位参考: Max Pain 94 ｜ Call Wall 94（+0.5%，弱）（OI 0.7k） ｜ Put Wall 90（-3.8%，弱）（OI 1.9k）

10-16（Activity LOW）仓位参考: Max Pain 93 ｜ Call Wall 95（+1.5%，弱）（OI 5.6k） ｜ Put Wall 90（-3.8%，弱）（OI 9.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/GDX_evening.json