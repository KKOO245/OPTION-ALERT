# 期权晚报 2026-11-17（快照 16:40 ET）

📊 市场环境

SPY $732.44 ｜ QQQ $656.95
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
🟡 **近现价集中开仓**: 11-20 450C ΔOI +56（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


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
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,874,798 | GEX Change vs 上次快照 -507,351 | Flip: Primary Flip: 415.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 281 / LOW 204 / INVALID 481
结构观察区: Primary Flip 415.50（全链重定价，覆盖 91%）
最近结构参考: Flip 416（现价高于该位 3.6%）
量化视角： 正 Gamma（187万，无历史分位）｜正 Gamma 减弱（51万）｜现价位于 Flip 上方 3.62%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 410（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 416（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +87 / P +0.1k ｜ Activity MEDIUM △ ｜ 3D
11-27  C +34 / P +58 ｜ Activity HIGH ｜ 10D
12-04  C +18 / P +26 ｜ Activity MEDIUM △ ｜ 17D
12-11  C +51 / P +5 ｜ Activity HIGH ｜ 24D

📆 11-20 Forward Structure
存量OI: C 10.7k / P 10.7k，今日变化ΔOI: C +87 / P +0.1k，平值价格ATM: C $8.00 / P $6.80 ｜ ATM IV 44.3%，净 delta 敞口 -2k shares
Top ΔOI: C 467 +81 ｜ C 450 +56 ｜ P 427 +40
仓位参考: Max Pain 410 ｜ Call Wall 420（-2.4%，弱）（OI 0.8k） ｜ Put Wall 390（-9.4%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 44.3%｜历史 Rank 76%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,902 股

📆 11-27 Forward Structure
存量OI: C 0.7k / P 0.7k，今日变化ΔOI: C +34 / P +58，平值价格ATM: C $16.10 / P $9.61 ｜ ATM IV 35.5%，净 delta 敞口 -1k shares
Top ΔOI: P 405 +26 ｜ P 435 +12
仓位参考: Max Pain 430 ｜ Call Wall 430（-0.1%，弱）（OI 64） ｜ Put Wall 395（-8.3%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 35.5%｜历史 Rank 76%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,354 股

12-04（MEDIUM △）Top ΔOI: 455P +19 ｜ 437C +3
12-04（MEDIUM △）仓位参考: Max Pain 450 ｜ Call Wall 460（+6.8%，弱）（OI 34） ｜ Put Wall 405（-5.9%，弱）（OI 24）

📆 12-11 Forward Structure
存量OI: C 0.4k / P 0.1k，今日变化ΔOI: C +51 / P +5，平值价格ATM: C $26.78 / P $11.23 ｜ ATM IV 34.5%，净 delta 敞口 2k shares
Top ΔOI: C 445 +39 ｜ P 415 +2 ｜ C 440 +2
仓位参考: Max Pain 440 ｜ Call Wall 450（+4.5%）（OI 0.1k） ｜ Put Wall 435（+1.0%）（OI 23）
量化解读： 存量 Call 重｜ATM IV 34.5%｜历史 Rank 76%（近端代理）｜IV/RV 0.82×（近似）｜净 delta 敞口 正 1,563 股

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 44.3% vs 11-27 35.5%（差 +8.8pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/ISRG_evening.json