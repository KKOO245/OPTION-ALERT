# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 17.49 ↓10.1%（5D +5.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（2D）ATM IV 114.0% vs 11-20 97.5%（差 +16.5pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-13 8C ΔOI +485（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 8.28 → 收盘 8.27（-0.2%） ｜ 今日高 8.83 ｜ 低 8.18 ｜ 昨收 7.92 → 收盘 8.27（+4.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.58 | OI比 0.24 | ATM IV 114.0% | Skew -7.8pp | Term 0.84 | ExpMove ±6.7%（近端） | Rank 49%
量化视角： IV 中性（Rank 49%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.24×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±6.7% ｜ 11-20（9D）±11.7% ｜ 11-27（16D）±15.5% ｜ 12-04（23D）±18.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,911,166 | GEX Change vs 上次快照 634,961 | Flip: Primary Flip: 7.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 194 / LOW 88 / INVALID 142
结构观察区: Primary Flip 7.75（全链重定价，覆盖 99%）
Put Wall 9（弱结构｜现价低于该位 8.2%） | Call Wall 9（现价低于该位 8.2%）
最近结构参考: Flip 8（现价高于该位 6.7%）
量化视角： 正 Gamma（291万，无历史分位）｜正 Gamma 增强（+63万）｜现价位于 Flip 上方 6.66%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 9（Put Wall，弱结构） / 8（MaxPain，仅结算参考） / 9（Call Wall）。
• Gamma 区域：切换参考 8（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0.2k / P +1.1k ｜ Activity HIGH ｜ 2D
11-20  C -0.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 9D
11-27  C +0.1k / P -8 ｜ Activity LOW ｜ 16D
12-04  C +0.1k / P +33 ｜ Activity HIGH ｜ 23D

📆 11-13 Forward Structure
存量OI: C 27.8k / P 6.7k，今日变化ΔOI: C +0.2k / P +1.1k，平值价格ATM: C $0.18 / P $0.37 ｜ ATM IV 114.0%，净 delta 敞口 -70k shares
Top ΔOI: P 9 +787 ｜ C 8 +485 ｜ C 9 -302
仓位参考: Max Pain 8 ｜ Call Wall 9（+8.9%，弱）（OI 3.3k） ｜ Put Wall 9（+8.9%）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 114.0%｜历史 Rank 49%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 69,729 股

11-20（MEDIUM △）Top ΔOI: 9P -786
11-20（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 9（+8.9%，弱）（OI 4.3k） ｜ Put Wall 8（-3.2%，弱）（OI 7.2k）

11-27（Activity LOW）仓位参考: Max Pain 9 ｜ Call Wall 8.5（+2.8%，弱）（OI 1.1k） ｜ Put Wall 8（-3.2%，弱）（OI 0.5k）

📆 12-04 Forward Structure
存量OI: C 2.5k / P 1.5k，今日变化ΔOI: C +0.1k / P +33，平值价格ATM: C $0.77 / P $0.75 ｜ ATM IV 96.7%，净 delta 敞口 6k shares
Top ΔOI: C 8 +83 ｜ P 7 +26
仓位参考: Max Pain 10 ｜ Call Wall 9（+8.9%，弱）（OI 0.2k） ｜ Put Wall 8.5（+2.8%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 96.7%｜历史 Rank 49%（近端代理）｜IV/RV 0.93×（近似）｜净 delta 敞口 正 6,415 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 114.0% vs 11-20 97.5%（差 +16.5pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/USAR_evening.json