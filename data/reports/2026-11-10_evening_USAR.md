# 期权晚报 2026-11-10（快照 16:40 ET）

📊 市场环境

SPY $749.92 ｜ QQQ $674.76
VIX 19.46 ↓2.3%（5D -6.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔵 **期限 OI 集中**: 11-13 9C ΔOI +3,453 占该期限总 OI 10.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 8.27 → 收盘 7.92（-4.2%） ｜ 今日高 8.60 ｜ 低 7.62 ｜ 昨收 8.76 → 收盘 7.92（-9.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.35 | OI比 0.20 | ATM IV 108.3% | Skew 14.2pp | Term 0.94 | ExpMove ±8.0%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 0.94）｜保护溢价显著（Skew 14.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.20×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±8.0% ｜ 11-20（10D）±13.9% ｜ 11-27（17D）±18.2% ｜ 12-04（24D）±22.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 621,568 | GEX Change vs 上次快照 -703,551 | Flip: Primary Flip: 7.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 236 / LOW 93 / INVALID 95
结构观察区: Primary Flip 7.76（全链重定价，覆盖 100%）
最近结构参考: Flip 8（现价高于该位 2.1%）
量化视角： 正 Gamma（62万，无历史分位）｜正 Gamma 减弱（70万）｜现价位于 Flip 上方 2.08%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 8（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 8（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +8.0k / P +1.3k ｜ Activity HIGH ｜ 3D
11-20  C +2.2k / P -0.1k ｜ Activity HIGH ｜ 10D
11-27  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 17D
12-04  C +0.4k / P +0.1k ｜ Activity HIGH ｜ 24D

📆 11-13 Forward Structure
存量OI: C 27.6k / P 5.6k，今日变化ΔOI: C +8.0k / P +1.3k，平值价格ATM: C $0.27 / P $0.36 ｜ ATM IV 108.3%，净 delta 敞口 -3k shares
仓位参考: Max Pain 8 ｜ Call Wall 8（+1.0%，弱）（OI 1.8k） ｜ Put Wall 8（+1.0%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 108.3%｜历史 Rank 40%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,019 股

📆 11-20 Forward Structure
存量OI: C 47.2k / P 32.4k，今日变化ΔOI: C +2.2k / P -0.1k，平值价格ATM: C $0.50 / P $0.60 ｜ ATM IV 108.8%，净 delta 敞口 60k shares
Top ΔOI: P 11 -318
仓位参考: Max Pain 10 ｜ Call Wall 8（+1.0%，弱）（OI 1.8k） ｜ Put Wall 8（+1.0%，弱）（OI 7.0k）
量化解读： 存量 Call 重｜ATM IV 108.8%｜历史 Rank 40%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 60,381 股

📆 11-27 Forward Structure
存量OI: C 10.5k / P 3.2k，今日变化ΔOI: C +0.6k / P +0.2k，平值价格ATM: C $0.65 / P $0.79 ｜ ATM IV 100.1%，净 delta 敞口 16k shares
仓位参考: Max Pain 9 ｜ Call Wall 8.5（+7.3%，弱）（OI 1.1k） ｜ Put Wall 8（+1.0%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 100.1%｜历史 Rank 40%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 15,744 股

📆 12-04 Forward Structure
存量OI: C 2.3k / P 1.5k，今日变化ΔOI: C +0.4k / P +0.1k，平值价格ATM: C $0.90 / P $0.90 ｜ ATM IV 100.2%，净 delta 敞口 2k shares
Top ΔOI: P 8 +101
仓位参考: Max Pain 10 ｜ Call Wall 8.5（+7.3%，弱）（OI 97） ｜ Put Wall 8.5（+7.3%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 100.2%｜历史 Rank 40%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 1,522 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/USAR_evening.json