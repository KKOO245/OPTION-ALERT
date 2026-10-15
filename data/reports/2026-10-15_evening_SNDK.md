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
🔴 **事件差分**: 10-16（1D）ATM IV 95.2% vs 10-23 71.9%（差 +23.3pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-16 1450C ΔOI +687（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,312.97 → 收盘 1,394.83（+6.2%） ｜ 今日高 1397.64 ｜ 低 1276.07 ｜ 昨收 1,403.34 → 收盘 1,394.83（-0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.57 | OI比 0.85 | ATM IV 95.1% | Skew -0.7pp | Term 0.77 | ExpMove ±4.0%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±4.0% ｜ 10-23（8D）±8.7% ｜ 10-30（15D）±0.0% ｜ 11-06（22D）±0.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,034,422 | GEX Change vs 上次快照 1,189,841 | Flip: Primary Flip: 1473.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1926 / LOW 487 / INVALID 939
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1473.31（全链重定价，覆盖 100%）
最近结构参考: Flip 1473（现价低于该位 5.3%）
量化视角： 负 Gamma（1003万，无历史分位）｜负 Gamma 缓解（+119万）｜现价位于 Flip 下方 5.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,520（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1473（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +4.8k / P -1.2k ｜ Activity HIGH ｜ 1D
10-23  C +0.5k / P +1.9k ｜ Activity HIGH ｜ 8D
10-30  C +1.0k / P +0.2k ｜ Activity HIGH ｜ 15D
11-06  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 22D

📆 10-16 Forward Structure
存量OI: C 81.8k / P 69.6k，今日变化ΔOI: C +4.8k / P -1.2k，平值价格ATM: C $28.50 / P $27.76 ｜ ATM IV 95.2%，净 delta 敞口 440k shares
Top ΔOI: C 1450 +687 ｜ P 1400 -648
仓位参考: Max Pain 1,520 ｜ Call Wall 1500（+7.5%，弱）（OI 2.1k） ｜ Put Wall 1400（+0.4%，弱）（OI 2.7k）
量化解读： 存量两侧均衡｜ATM IV 95.2%｜历史 Rank 51%（近端代理）｜IV/RV 1.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 440,459 股

📆 10-23 Forward Structure
存量OI: C 24.2k / P 19.2k，今日变化ΔOI: C +0.5k / P +1.9k，平值价格ATM: C $60.00 / P $60.65 ｜ ATM IV 71.9%，净 delta 敞口 24k shares
Top ΔOI: C 1700 -1,537 ｜ P 1100 +399 ｜ C 1500 +255
仓位参考: Max Pain 1,540 ｜ Call Wall 1500（+7.5%）（OI 1.6k） ｜ Put Wall 1500（+7.5%）（OI 1.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 71.9%｜历史 Rank 51%（近端代理）｜IV/RV 1.43×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 23,884 股

📆 10-30 Forward Structure
存量OI: C 15.8k / P 12.8k，今日变化ΔOI: C +1.0k / P +0.2k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 80.9%，净 delta 敞口 20k shares
Top ΔOI: C 1750 +154 ｜ P 1100 +122 ｜ C 1600 +117
仓位参考: Max Pain 1,595 ｜ Call Wall 1500（+7.5%）（OI 1.5k） ｜ Put Wall 1400（+0.4%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 80.9%｜历史 Rank 51%（近端代理）｜IV/RV 1.61×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 19,867 股

11-06（MEDIUM △）Top ΔOI: 1340P +100
11-06（MEDIUM △）仓位参考: Max Pain 1,630 ｜ Call Wall 1450（+4.0%，弱）（OI 66） ｜ Put Wall 1400（+0.4%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 95.2% vs 10-23 71.9%（差 +23.3pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/SNDK_evening.json