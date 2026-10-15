# 期权晚报 2026-10-15（快照 16:40 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 16.46 ↓2.4%（5D +6.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🔴 **事件差分**: 10-16（1D）ATM IV 117.4% vs 10-23 84.2%（差 +33.2pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 175.48 → 收盘 188.41（+7.4%） ｜ 今日高 189.33 ｜ 低 163.36 ｜ 昨收 186.01 → 收盘 188.41（+1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.56 | OI比 0.74 | ATM IV 117.4% | Skew -3.9pp | Term 0.77 | ExpMove ±4.9%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±4.9% ｜ 10-23（8D）±10.1% ｜ 10-30（15D）±13.0% ｜ 11-06（22D）±16.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -15,418,706 | GEX Change vs 上次快照 6,423,599 | Flip: Primary Flip: 199.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 542 / LOW 50 / INVALID 190
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 199.77（全链重定价，覆盖 99%）
Put Wall 200（弱结构｜现价低于该位 5.8%）
最近结构参考: Flip 200（现价低于该位 5.7%）
量化视角： 负 Gamma（1542万，无历史分位）｜负 Gamma 缓解（+642万）｜现价位于 Flip 下方 5.69%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 200（Put Wall，弱结构） / 210（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 200（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +28.9k / P -3.8k ｜ Activity HIGH ｜ 1D
10-23  C +16.4k / P +13.7k ｜ Activity HIGH ｜ 8D
10-30  C +4.2k / P +1.8k ｜ Activity HIGH ｜ 15D
11-06  C +7.9k / P +92 ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 162.4k / P 119.5k，今日变化ΔOI: C +28.9k / P -3.8k，平值价格ATM: C $5.11 / P $4.16 ｜ ATM IV 117.4%，净 delta 敞口 1.5M shares
Top ΔOI: C 230 +14,684 ｜ P 220 -2,906 ｜ C 200 +2,725
仓位参考: Max Pain 210 ｜ Call Wall 200（+6.2%，弱）（OI 6.1k） ｜ Put Wall 190（+0.8%，弱）（OI 7.1k）
量化解读： 存量 Call 重｜ATM IV 117.4%｜历史 Rank 69%（近端代理）｜IV/RV 1.65×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,465,001 股

📆 10-23 Forward Structure
存量OI: C 47.3k / P 34.9k，今日变化ΔOI: C +16.4k / P +13.7k，平值价格ATM: C $10.25 / P $8.75 ｜ ATM IV 84.2%，净 delta 敞口 -308k shares
Top ΔOI: C 200 +3,833 ｜ C 275 +3,011 ｜ P 220 +2,705
仓位参考: Max Pain 212 ｜ Call Wall 200（+6.2%，弱）（OI 4.1k） ｜ Put Wall 200（+6.2%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 84.2%｜历史 Rank 69%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 308,171 股

📆 10-30 Forward Structure
存量OI: C 30.2k / P 20.8k，今日变化ΔOI: C +4.2k / P +1.8k，平值价格ATM: C $12.45 / P $12.10 ｜ ATM IV 83.2%，净 delta 敞口 110k shares
Top ΔOI: C 200 +1,171 ｜ C 240 +791 ｜ P 170 +502
仓位参考: Max Pain 215 ｜ Call Wall 200（+6.2%，弱）（OI 1.3k） ｜ Put Wall 200（+6.2%）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 83.2%｜历史 Rank 69%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 110,147 股

📆 11-06 Forward Structure
存量OI: C 19.2k / P 13.5k，今日变化ΔOI: C +7.9k / P +92，平值价格ATM: C $15.11 / P $16.78 ｜ ATM IV 83.4%，净 delta 敞口 193k shares
Top ΔOI: C 240 +3,131 ｜ C 230 +2,994 ｜ P 200 -722
仓位参考: Max Pain 220 ｜ Put Wall 200（+6.2%）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 83.4%｜历史 Rank 69%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 193,056 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 117.4% vs 10-23 84.2%（差 +33.2pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/NBIS_evening.json