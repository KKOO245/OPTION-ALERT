# 期权晚报 2026-11-24（快照 16:40 ET）

📊 市场环境

SPY $718.78 ｜ QQQ $638.10
VIX 26.36 ↓1.0%（5D +3.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 12-04 167C ΔOI +620（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 157.80 → 收盘 161.18（+2.1%） ｜ 今日高 163.01 ｜ 低 157.80 ｜ 昨收 159.36 → 收盘 161.18（+1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.71 | OI比 0.53 | ATM IV 64.2% | Skew 9.4pp | Term 0.89 | ExpMove ±4.5%（近端） | Rank 75%
量化视角： IV 中性（Rank 75%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价显著（Skew 9.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±4.5% ｜ 12-04（10D）±8.2% ｜ 12-11（17D）±10.5% ｜ 12-18（24D）±12.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 28,608,060 | GEX Change vs 上次快照 -1,687,430 | Flip: Primary Flip: 151.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 463 / LOW 176 / INVALID 269
结构观察区: Primary Flip 151.25（全链重定价，覆盖 100%）
Call Wall 165（弱结构｜现价低于该位 2.3%）
最近结构参考: Call Wall 165（现价低于该位 2.3%）
量化视角： 正 Gamma（2861万，无历史分位）｜正 Gamma 减弱（169万）｜现价位于 Flip 上方 6.57%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +18.9k / P +6.2k ｜ Activity HIGH ｜ 3D
12-04  C +8.8k / P +3.5k ｜ Activity HIGH ｜ 10D
12-11  C +1.6k / P +0.6k ｜ Activity HIGH ｜ 17D
12-18  C +1.4k / P +3.9k ｜ Activity HIGH ｜ 24D

📆 11-27 Forward Structure
存量OI: C 104.8k / P 56.0k，今日变化ΔOI: C +18.9k / P +6.2k，平值价格ATM: C $4.20 / P $3.05 ｜ ATM IV 64.2%，净 delta 敞口 -55k shares
Top ΔOI: C 175 +9,273 ｜ C 177 +6,935 ｜ C 172 +1,776
仓位参考: Max Pain 152 ｜ Call Wall 175（+8.6%，弱）（OI 10.7k） ｜ Put Wall 150（-6.9%，弱）（OI 5.1k）
量化解读： 存量 Call 重｜ATM IV 64.2%｜历史 Rank 75%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 54,778 股

📆 12-04 Forward Structure
存量OI: C 32.7k / P 24.6k，今日变化ΔOI: C +8.8k / P +3.5k，平值价格ATM: C $7.20 / P $6.00 ｜ ATM IV 62.2%，净 delta 敞口 97k shares
Top ΔOI: C 180 +4,955 ｜ P 147 +1,050 ｜ C 167 +620
仓位参考: Max Pain 160 ｜ Call Wall 175（+8.6%，弱）（OI 1.6k） ｜ Put Wall 155（-3.8%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 62.2%｜历史 Rank 75%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 97,053 股

📆 12-11 Forward Structure
存量OI: C 12.1k / P 14.8k，今日变化ΔOI: C +1.6k / P +0.6k，平值价格ATM: C $9.17 / P $7.80 ｜ ATM IV 60.9%，净 delta 敞口 35k shares
Top ΔOI: C 175 +325 ｜ C 162 +260 ｜ C 160 +219
仓位参考: Max Pain 162 ｜ Call Wall 175（+8.6%，弱）（OI 1.2k） ｜ Put Wall 150（-6.9%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 60.9%｜历史 Rank 75%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,513 股

📆 12-18 Forward Structure
存量OI: C 265.7k / P 262.1k，今日变化ΔOI: C +1.4k / P +3.9k，平值价格ATM: C $10.55 / P $9.15 ｜ ATM IV 59.4%，净 delta 敞口 47k shares
Top ΔOI: P 115 +1,619
仓位参考: Max Pain 140 ｜ Call Wall 165（+2.4%，弱）（OI 14.2k） ｜ Put Wall 160（-0.7%，弱）（OI 18.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 59.4%｜历史 Rank 75%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 47,378 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/PLTR_evening.json