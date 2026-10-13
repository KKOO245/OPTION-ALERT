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
🟡 **近现价集中开仓**: 10-16 140P ΔOI +765（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 140.19 → 收盘 138.61（-1.1%） ｜ 今日高 145.17 ｜ 低 138.20 ｜ 昨收 140.32 → 收盘 138.61（-1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.45 | OI比 0.77 | ATM IV 58.9% | Skew 0.0pp | Term 1.03 | ExpMove ±4.3%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构正常（Term 1.03）｜保护溢价薄（Skew 0.0pp）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（3D）±4.3% ｜ 10-23（10D）±7.0% ｜ 10-30（17D）±12.7% ｜ 11-06（24D）±13.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,967,631 | GEX Change vs 上次快照 -13,413,910 | Flip: Primary Flip: 133.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 514 / LOW 43 / INVALID 79
结构观察区: Primary Flip 133.34（全链重定价，覆盖 98%）
Put Wall 125（弱结构｜现价高于该位 10.9%） | Call Wall 150（现价低于该位 7.6%）
最近结构参考: Flip 133（现价高于该位 4.0%）
量化视角： 正 Gamma（1497万，无历史分位）｜正 Gamma 减弱（1341万）｜现价位于 Flip 上方 3.95%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 125（Put Wall，弱结构） / 130（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0.6k / P +1.8k ｜ Activity MEDIUM △ ｜ 3D
10-23  C +2.8k / P +0.4k ｜ Activity HIGH ｜ 10D
10-30  C +0.6k / P +0.6k ｜ Activity HIGH ｜ 17D
11-06  C +0.2k / P +0.5k ｜ Activity HIGH ｜ 24D

📆 10-16 Forward Structure
存量OI: C 88.4k / P 68.1k，今日变化ΔOI: C +0.6k / P +1.8k，平值价格ATM: C $2.79 / P $3.15 ｜ ATM IV 58.9%，净 delta 敞口 -108k shares
Top ΔOI: C 150 -949 ｜ P 140 +765 ｜ P 130 +425
仓位参考: Max Pain 130 ｜ Call Wall 150（+8.2%）（OI 15.3k） ｜ Put Wall 125（-9.8%，弱）（OI 5.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.9%｜历史 Rank 59%（近端代理）｜IV/RV 2.14×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 108,073 股

📆 10-23 Forward Structure
存量OI: C 18.7k / P 19.1k，今日变化ΔOI: C +2.8k / P +0.4k，平值价格ATM: C $4.60 / P $5.05 ｜ ATM IV 51.4%，净 delta 敞口 18k shares
Top ΔOI: C 145 +542 ｜ C 150 +458
仓位参考: Max Pain 136 ｜ Call Wall 150（+8.2%，弱）（OI 1.5k） ｜ Put Wall 125（-9.8%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.4%｜历史 Rank 59%（近端代理）｜IV/RV 1.87×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 18,108 股

📆 10-30 Forward Structure
存量OI: C 9.0k / P 11.4k，今日变化ΔOI: C +0.6k / P +0.6k，平值价格ATM: C $9.00 / P $8.60 ｜ ATM IV 70.2%，净 delta 敞口 -2k shares
Top ΔOI: P 135 +286 ｜ P 144 +78 ｜ C 130 +72
仓位参考: Max Pain 135 ｜ Call Wall 150（+8.2%，弱）（OI 1.0k） ｜ Put Wall 130（-6.2%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 70.2%｜历史 Rank 59%（近端代理）｜IV/RV 2.55×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,129 股

📆 11-06 Forward Structure
存量OI: C 3.7k / P 2.9k，今日变化ΔOI: C +0.2k / P +0.5k，平值价格ATM: C $9.27 / P $9.35 ｜ ATM IV 65.7%，净 delta 敞口 -18k shares
Top ΔOI: P 140 +486
仓位参考: Max Pain 140 ｜ Call Wall 150（+8.2%，弱）（OI 0.3k） ｜ Put Wall 140（+1.0%）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 65.7%｜历史 Rank 59%（近端代理）｜IV/RV 2.38×（近似）｜净 delta 敞口 负 17,729 股

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 58.9% vs 10-23 51.4%（差 +7.5pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/NOW_evening.json