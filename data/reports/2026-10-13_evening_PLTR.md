# 期权晚报 2026-10-13（快照 16:40 ET）

📊 市场环境

SPY $778.01 ｜ QQQ $743.57
VIX 15.27 ↑0.4%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 215C ΔOI -3,857（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 207.90 → 收盘 208.67（+0.4%） ｜ 今日高 210.88 ｜ 低 205.97 ｜ 昨收 209.00 → 收盘 208.67（-0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.69 | OI比 1.09 | ATM IV 45.8% | Skew 1.3pp | Term 1.26 | ExpMove ±3.3%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常偏陡（Term 1.26）｜保护溢价薄（Skew 1.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±3.3% ｜ 10-23（10D）±5.7% ｜ 10-30（17D）±7.5% ｜ 11-06（24D）±12.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 90,495,581 | GEX Change vs 上次快照 -1,676,818 | Flip: Primary Flip: 188.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 627 / LOW 69 / INVALID 102
结构观察区: Primary Flip 188.63（全链重定价，覆盖 100%）
Call Wall 220（弱结构｜现价低于该位 5.2%）
最近结构参考: Call Wall 220（现价低于该位 5.2%）
量化视角： 正 Gamma（9050万，无历史分位）｜正 Gamma 减弱（168万）｜现价位于 Flip 上方 10.63%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（MaxPain，仅结算参考）；上方 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 189（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +11.1k / P +12.1k ｜ Activity MEDIUM △ ｜ 3D
10-23  C +4.8k / P +4.0k ｜ Activity HIGH ｜ 10D
10-30  C +0.4k / P +2.5k ｜ Activity HIGH ｜ 17D
11-06  C +1.7k / P +1.7k ｜ Activity HIGH ｜ 24D

📆 10-16 Forward Structure
存量OI: C 237.9k / P 259.1k，今日变化ΔOI: C +11.1k / P +12.1k，平值价格ATM: C $4.05 / P $2.89 ｜ ATM IV 45.8%，净 delta 敞口 -606k shares
Top ΔOI: C 222 +8,252 ｜ C 220 +4,183 ｜ C 215 -3,857
仓位参考: Max Pain 180 ｜ Call Wall 220（+5.4%，弱）（OI 18.4k） ｜ Put Wall 190（-8.9%，弱）（OI 9.0k）
量化解读： 存量两侧均衡｜ATM IV 45.8%｜历史 Rank 36%（近端代理）｜IV/RV 1.76×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 606,172 股

📆 10-23 Forward Structure
存量OI: C 39.3k / P 53.7k，今日变化ΔOI: C +4.8k / P +4.0k，平值价格ATM: C $6.64 / P $5.25 ｜ ATM IV 42.9%，净 delta 敞口 57k shares
Top ΔOI: C 220 +1,608 ｜ C 207 +757 ｜ P 200 +581
仓位参考: Max Pain 190 ｜ Call Wall 220（+5.4%，弱）（OI 4.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.9%｜历史 Rank 36%（近端代理）｜IV/RV 1.65×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 57,205 股

📆 10-30 Forward Structure
存量OI: C 36.2k / P 35.2k，今日变化ΔOI: C +0.4k / P +2.5k，平值价格ATM: C $8.55 / P $7.00 ｜ ATM IV 43.1%，净 delta 敞口 -49k shares
Top ΔOI: P 210 +306 ｜ P 205 +264
仓位参考: Max Pain 192 ｜ Call Wall 205（-1.8%，弱）（OI 2.9k） ｜ Put Wall 190（-8.9%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 43.1%｜历史 Rank 36%（近端代理）｜IV/RV 1.66×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 48,535 股

📆 11-06 Forward Structure
存量OI: C 15.9k / P 15.1k，今日变化ΔOI: C +1.7k / P +1.7k，平值价格ATM: C $13.78 / P $12.05 ｜ ATM IV 60.6%，净 delta 敞口 33k shares
Top ΔOI: C 230 +335 ｜ P 195 +334 ｜ C 207 +281
仓位参考: Max Pain 190 ｜ Call Wall 220（+5.4%，弱）（OI 1.4k） ｜ Put Wall 190（-8.9%）（OI 2.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 60.6%｜历史 Rank 36%（近端代理）｜IV/RV 2.33×（近似）｜净 delta 敞口 正 32,604 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/PLTR_evening.json