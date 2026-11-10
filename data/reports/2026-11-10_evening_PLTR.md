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
🟡 **近现价集中开仓**: 11-13 165P ΔOI +2,335（距现价 -2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 168.20 → 收盘 168.82（+0.4%） ｜ 今日高 169.34 ｜ 低 164.00 ｜ 昨收 169.20 → 收盘 168.82（-0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.61 | OI比 0.64 | ATM IV 57.5% | Skew 6.2pp | Term 0.85 | ExpMove ±4.3%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价显著（Skew 6.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±4.3% ｜ 11-20（10D）±7.2% ｜ 11-27（17D）±8.4% ｜ 12-04（24D）±10.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 35,119,365 | GEX Change vs 上次快照 -2,228,102 | Flip: Primary Flip: 159.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 501 / LOW 177 / INVALID 256
结构观察区: Primary Flip 159.68（全链重定价，覆盖 100%）
Call Wall 165（弱结构｜现价高于该位 2.3%）
最近结构参考: Call Wall 165（现价高于该位 2.3%）
量化视角： 正 Gamma（3512万，无历史分位）｜正 Gamma 减弱（223万）｜现价位于 Flip 上方 5.73%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考） / 165（Call Wall，弱结构）。
• Gamma 区域：切换参考 160（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +27.4k / P +7.8k ｜ Activity HIGH ｜ 3D
11-20  C -6.8k / P +7.4k ｜ Activity HIGH ｜ 10D
11-27  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 17D
12-04  C +1.0k / P +0.6k ｜ Activity HIGH ｜ 24D

📆 11-13 Forward Structure
存量OI: C 133.3k / P 84.8k，今日变化ΔOI: C +27.4k / P +7.8k，平值价格ATM: C $3.10 / P $4.10 ｜ ATM IV 57.5%，净 delta 敞口 194k shares
Top ΔOI: C 185 +10,099 ｜ C 182 +8,911 ｜ P 165 +2,335
仓位参考: Max Pain 162 ｜ Call Wall 165（-2.3%，弱）（OI 14.2k） ｜ Put Wall 165（-2.3%，弱）（OI 4.2k）
量化解读： 存量 Call 重｜ATM IV 57.5%｜历史 Rank 73%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 194,153 股

📆 11-20 Forward Structure
存量OI: C 177.7k / P 188.9k，今日变化ΔOI: C -6.8k / P +7.4k，平值价格ATM: C $5.67 / P $6.50 ｜ ATM IV 54.6%，净 delta 敞口 -322k shares
Top ΔOI: C 165 -5,555 ｜ P 165 -1,766
仓位参考: Max Pain 175 ｜ Call Wall 180（+6.6%，弱）（OI 10.4k） ｜ Put Wall 185（+9.6%，弱）（OI 9.9k）
量化解读： 存量两侧均衡｜ATM IV 54.6%｜历史 Rank 73%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 321,932 股

11-27（MEDIUM △）Top ΔOI: 160C -122
11-27（MEDIUM △）仓位参考: Max Pain 178 ｜ Call Wall 180（+6.6%，弱）（OI 0.9k） ｜ Put Wall 160（-5.2%，弱）（OI 1.3k）

📆 12-04 Forward Structure
存量OI: C 15.4k / P 9.4k，今日变化ΔOI: C +1.0k / P +0.6k，平值价格ATM: C $8.75 / P $9.55 ｜ ATM IV 49.9%，净 delta 敞口 5k shares
Top ΔOI: C 185 +477 ｜ P 175 +156
仓位参考: Max Pain 175 ｜ Call Wall 185（+9.6%，弱）（OI 1.0k） ｜ Put Wall 155（-8.2%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 49.9%｜历史 Rank 73%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 5,155 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/PLTR_evening.json