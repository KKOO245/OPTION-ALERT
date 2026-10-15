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
🟡 **近现价集中开仓**: 10-16 40C ΔOI +565（距现价 -3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 38.80 → 收盘 41.61（+7.2%） ｜ 今日高 41.71 ｜ 低 38.60 ｜ 昨收 39.95 → 收盘 41.61（+4.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.89 | OI比 0.56 | ATM IV 65.3% | Skew 2.7pp | Term 0.96 | ExpMove ±4.1%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构正常（Term 0.96）｜保护溢价中性（Skew 2.7pp）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±4.1% ｜ 10-23（8D）±7.0% ｜ 10-30（15D）±9.2% ｜ 11-06（22D）±14.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,024,553 | GEX Change vs 上次快照 562,962 | Flip: Primary Flip: 43.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 270 / LOW 73 / INVALID 103
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 43.06（全链重定价，覆盖 84%）
Put Wall 45（现价低于该位 7.5%）
最近结构参考: Flip 43（现价低于该位 3.4%）
量化视角： 负 Gamma（302万，无历史分位）｜负 Gamma 缓解（+56万）｜现价位于 Flip 下方 3.36%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 45（Put Wall） / 45（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 43（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +1.3k / P -2.8k ｜ Activity HIGH ｜ 1D
10-23  C +0.6k / P +1.1k ｜ Activity HIGH ｜ 8D
10-30  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 15D
11-06  C +0.5k / P +0.6k ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 25.2k / P 14.2k，今日变化ΔOI: C +1.3k / P -2.8k，平值价格ATM: C $0.68 / P $1.04 ｜ ATM IV 65.3%，净 delta 敞口 340k shares
Top ΔOI: P 45 -817 ｜ C 40 +565 ｜ P 42 -422
仓位参考: Max Pain 45 ｜ Call Wall 45（+8.1%，弱）（OI 1.4k） ｜ Put Wall 45（+8.1%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 65.3%｜历史 Rank 48%（近端代理）｜IV/RV 1.38×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 339,690 股

📆 10-23 Forward Structure
存量OI: C 4.7k / P 3.6k，今日变化ΔOI: C +0.6k / P +1.1k，平值价格ATM: C $1.55 / P $1.35 ｜ ATM IV 58.0%，净 delta 敞口 -12k shares
Top ΔOI: P 42 +420 ｜ P 42 +251 ｜ P 38 +157
仓位参考: Max Pain 45 ｜ Call Wall 45（+8.1%，弱）（OI 0.2k） ｜ Put Wall 42（+0.9%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.0%｜历史 Rank 48%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 11,722 股

📆 10-30 Forward Structure
存量OI: C 6.4k / P 5.0k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $1.61 / P $2.24 ｜ ATM IV 57.7%，净 delta 敞口 14k shares
Top ΔOI: C 45 +181 ｜ C 44 +139
仓位参考: Max Pain 46 ｜ Call Wall 45（+8.1%，弱）（OI 0.2k） ｜ Put Wall 44（+5.7%）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 57.7%｜历史 Rank 48%（近端代理）｜IV/RV 1.22×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 14,062 股

📆 11-06 Forward Structure
存量OI: C 3.3k / P 3.0k，今日变化ΔOI: C +0.5k / P +0.6k，平值价格ATM: C $2.90 / P $3.25 ｜ ATM IV 69.3%，净 delta 敞口 22k shares
Top ΔOI: C 40 +396 ｜ C 45 +194
仓位参考: Max Pain 45 ｜ Call Wall 40（-3.9%，弱）（OI 0.4k） ｜ Put Wall 38（-8.7%）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 69.3%｜历史 Rank 48%（近端代理）｜IV/RV 1.46×（近似）｜净 delta 敞口 正 22,026 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 65.3% vs 10-23 58.0%（差 +7.2pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/MP_evening.json