# 期权晚报 2026-10-14（快照 16:42 ET）

📊 市场环境

SPY $769.60 ｜ QQQ $728.95
VIX 16.87 ↑10.5%（5D +11.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 207P ΔOI +3,306（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 207.36 → 收盘 200.97（-3.1%） ｜ 今日高 209.28 ｜ 低 199.74 ｜ 昨收 208.67 → 收盘 200.97（-3.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.21 | OI比 1.17 | ATM IV 52.3% | Skew 3.9pp | Term 1.16 | ExpMove ±3.1%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构正常偏陡（Term 1.16）｜保护溢价中性（Skew 3.9pp）｜当日成交偏 Put（P/C量 1.21）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.21×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±3.1% ｜ 10-23（9D）±5.7% ｜ 10-30（16D）±7.5% ｜ 11-06（23D）±12.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 43,050,739 | GEX Change vs 上次快照 -39,227,917 | Flip: Primary Flip: 191.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 626 / LOW 72 / INVALID 214
结构观察区: Primary Flip 191.96（全链重定价，覆盖 100%）
Call Wall 220（弱结构｜现价低于该位 8.6%）
最近结构参考: Flip 192（现价高于该位 4.7%）
量化视角： 正 Gamma（4305万，无历史分位）｜正 Gamma 减弱（3923万）｜现价位于 Flip 上方 4.69%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）；上方 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 192（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C -5.8k / P +11.6k ｜ Activity MEDIUM △ ｜ 2D
10-23  C +3.4k / P +4.2k ｜ Activity HIGH ｜ 9D
10-30  C +1.7k / P +1.2k ｜ Activity MEDIUM △ ｜ 16D
11-06  C +1.1k / P +1.0k ｜ Activity HIGH ｜ 23D

📆 10-16 Forward Structure
存量OI: C 232.1k / P 270.7k，今日变化ΔOI: C -5.8k / P +11.6k，平值价格ATM: C $3.68 / P $2.60 ｜ ATM IV 52.3%，净 delta 敞口 -1.5M shares
Top ΔOI: C 185 -5,269 ｜ P 207 +3,306 ｜ P 205 +2,316
仓位参考: Max Pain 185 ｜ Call Wall 220（+9.5%，弱）（OI 17.7k） ｜ Put Wall 200（-0.5%，弱）（OI 9.2k）
量化解读： 存量两侧均衡｜ATM IV 52.3%｜历史 Rank 72%（近端代理）｜IV/RV 2.10×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,503,032 股

📆 10-23 Forward Structure
存量OI: C 42.7k / P 57.9k，今日变化ΔOI: C +3.4k / P +4.2k，平值价格ATM: C $6.17 / P $5.28 ｜ ATM IV 45.4%，净 delta 敞口 -101k shares
Top ΔOI: C 210 +528 ｜ C 217 +510
仓位参考: Max Pain 192 ｜ Call Wall 220（+9.5%，弱）（OI 4.3k） ｜ Put Wall 200（-0.5%，弱）（OI 2.6k）
量化解读： 存量 Put 重｜ATM IV 45.4%｜历史 Rank 72%（近端代理）｜IV/RV 1.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 100,834 股

10-30（MEDIUM △）Top ΔOI: 220C +308 ｜ 215C +291
10-30（MEDIUM △）仓位参考: Max Pain 192 ｜ Call Wall 205（+2.0%，弱）（OI 3.1k） ｜ Put Wall 190（-5.5%，弱）（OI 3.5k）

📆 11-06 Forward Structure
存量OI: C 17.0k / P 16.2k，今日变化ΔOI: C +1.1k / P +1.0k，平值价格ATM: C $13.50 / P $12.35 ｜ ATM IV 64.3%，净 delta 敞口 353 shares
Top ΔOI: P 205 +161
仓位参考: Max Pain 192 ｜ Call Wall 220（+9.5%，弱）（OI 1.4k） ｜ Put Wall 190（-5.5%）（OI 2.9k）
量化解读： 存量两侧均衡｜ATM IV 64.3%｜历史 Rank 72%（近端代理）｜IV/RV 2.58×（近似）｜净 delta 敞口 正 353 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 52.3% vs 10-23 45.4%（差 +6.9pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/PLTR_evening.json