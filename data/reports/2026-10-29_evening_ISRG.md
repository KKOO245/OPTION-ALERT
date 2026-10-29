# 期权晚报 2026-10-29（快照 16:40 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 17.20 ↑1.7%（5D -9.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 470C ΔOI +2（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 447.85 → 收盘 448.76（+0.2%） ｜ 今日高 450.40 ｜ 低 443.65 ｜ 昨收 444.18 → 收盘 448.76（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.20 | OI比 0.90 | ATM IV 36.7% | Skew 14.5pp | Term 0.86 | ExpMove ±1.6%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价显著（Skew 14.5pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.20×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（1D）±1.6% ｜ 11-06（8D）±4.0% ｜ 11-13（15D）±8.3% ｜ 11-20（22D）±6.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,222,528 | GEX Change vs 上次快照 -132,126 | Flip: Primary Flip: 420.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 281 / LOW 198 / INVALID 513
结构观察区: Primary Flip 420.27（全链重定价，覆盖 90%）
Call Wall 420（弱结构｜现价高于该位 6.8%）
最近结构参考: Flip 420（现价高于该位 6.8%）
量化视角： 正 Gamma（222万，无历史分位）｜正 Gamma 减弱（13万）｜现价位于 Flip 上方 6.78%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 435（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 420（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +15 / P +12 ｜ Activity LOW ｜ 1D
11-06  C +0.1k / P +20 ｜ Activity HIGH ｜ 8D
11-13  C +6 / P -7 ｜ Activity LOW ｜ 15D
11-20  C +22 / P +17 ｜ Activity LOW ｜ 22D

📆 10-30 Forward Structure
存量OI: C 2.4k / P 2.2k，今日变化ΔOI: C +15 / P +12，平值价格ATM: C $3.45 / P $3.85 ｜ ATM IV 36.7%，净 delta 敞口 -1k shares
Top ΔOI: C 455 +15 ｜ C 460 +11 ｜ P 450 +10
仓位参考: Max Pain 435 ｜ Call Wall 455（+1.4%，弱）（OI 0.1k） ｜ Put Wall 455（+1.4%）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 36.7%｜历史 Rank 29%（近端代理）｜IV/RV 1.61×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,157 股

📆 11-06 Forward Structure
存量OI: C 1.4k / P 0.9k，今日变化ΔOI: C +0.1k / P +20，平值价格ATM: C $8.00 / P $9.90 ｜ ATM IV 35.2%，净 delta 敞口 1k shares
Top ΔOI: C 470 +59
仓位参考: Max Pain 428 ｜ Call Wall 430（-4.2%，弱）（OI 0.1k） ｜ Put Wall 420（-6.4%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 35.2%｜历史 Rank 29%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,002 股

11-13（Activity LOW）仓位参考: Max Pain 425 ｜ Call Wall 440（-2.0%，弱）（OI 0.1k） ｜ Put Wall 420（-6.4%，弱）（OI 81）

11-20（Activity LOW）仓位参考: Max Pain 400 ｜ Call Wall 420（-6.4%，弱）（OI 0.8k） ｜ Put Wall 410（-8.6%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/ISRG_evening.json