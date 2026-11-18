# 期权晚报 2026-11-17（快照 21:00 ET）

📊 市场环境

SPY $732.44 ｜ QQQ $nan
VIX 25.46 ↑11.1%（5D +30.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 10.69 → 收盘 10.49（-1.9%） ｜ 今日高 10.77 ｜ 低 9.98 ｜ 昨收 10.74 → 收盘 10.49（-2.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.03 | OI比 0.31 | ATM IV 95.2% | Skew 14.2pp | Term 1.01 | ExpMove ±8.1%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 1.01）｜保护溢价显著（Skew 14.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（3D）±8.1% ｜ 11-27（10D）±9.5% ｜ 12-04（17D）±20.8% ｜ 12-11（24D）±16.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 743,141 | GEX Change vs 上次快照 -81,063 | Flip: Primary Flip: 9.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 157 / LOW 70 / INVALID 137
结构观察区: Primary Flip 9.37（全链重定价，覆盖 85%）
Put Wall 10（弱结构｜现价高于该位 4.9%）
最近结构参考: Put Wall 10（现价高于该位 4.9%）
量化视角： 正 Gamma（74万，无历史分位）｜正 Gamma 减弱（8万）｜现价位于 Flip 上方 11.90%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（Put Wall，弱结构）；上方 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 10D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 17D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 11-20 Forward Structure
存量OI: C 6.8k / P 2.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.30 / P $0.55 ｜ ATM IV 95.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 12 ｜ Call Wall 11.5（+9.6%，弱）（OI 0.4k） ｜ Put Wall 11（+4.9%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 95.2%｜历史 Rank 36%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-27（Activity LOW）仓位参考: Max Pain 12 ｜ Put Wall 10（-4.7%，弱）（OI 0.1k）

12-04（Activity LOW）仓位参考: Max Pain 13 ｜ Put Wall 9.5（-9.4%）（OI 0.2k）

12-11（Activity LOW）仓位参考: Max Pain 11 ｜ Call Wall 11（+4.9%，弱）（OI 41） ｜ Put Wall 11（+4.9%，弱）（OI 14）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/NNE_evening.json