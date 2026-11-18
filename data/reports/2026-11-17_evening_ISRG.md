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


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 437.33 → 收盘 430.53（-1.6%） ｜ 今日高 441.29 ｜ 低 428.71 ｜ 昨收 437.75 → 收盘 430.53（-1.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.64 | OI比 1.00 | ATM IV 44.3% | Skew 6.7pp | Term 0.81 | ExpMove ±3.4%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 6.7pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（3D）±3.4% ｜ 11-27（10D）±6.0% ｜ 12-04（17D）±7.8% ｜ 12-11（24D）±8.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,913,499 | GEX Change vs 上次快照 -468,651 | Flip: Primary Flip: 417.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 281 / LOW 204 / INVALID 481
结构观察区: Primary Flip 417.18（全链重定价，覆盖 91%）
最近结构参考: Flip 417（现价高于该位 3.2%）
量化视角： 正 Gamma（191万，无历史分位）｜正 Gamma 减弱（47万）｜现价位于 Flip 上方 3.20%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 410（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 417（全链重定价，覆盖 91%）。
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
存量OI: C 10.7k / P 10.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $8.00 / P $6.80 ｜ ATM IV 44.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 410 ｜ Call Wall 420（-2.4%，弱）（OI 0.8k） ｜ Put Wall 390（-9.4%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 44.3%｜历史 Rank 76%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-27（Activity LOW）仓位参考: Max Pain 430 ｜ Call Wall 430（-0.1%，弱）（OI 64） ｜ Put Wall 395（-8.3%，弱）（OI 0.2k）

12-04（Activity LOW）仓位参考: Max Pain 450 ｜ Call Wall 460（+6.8%，弱）（OI 34） ｜ Put Wall 405（-5.9%，弱）（OI 24）

12-11（Activity LOW）仓位参考: Max Pain 440 ｜ Call Wall 450（+4.5%）（OI 0.1k） ｜ Put Wall 435（+1.0%）（OI 23）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 44.3% vs 11-27 35.5%（差 +8.8pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/ISRG_evening.json