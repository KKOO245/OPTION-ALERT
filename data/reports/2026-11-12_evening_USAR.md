# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（1D）ATM IV 133.3% vs 11-20 105.2%（差 +28.1pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-13 8P ΔOI +624（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 7.90 → 收盘 8.07（+2.2%） ｜ 今日高 8.47 ｜ 低 7.69 ｜ 昨收 8.27 → 收盘 8.07（-2.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.74 | OI比 0.25 | ATM IV 133.3% | Skew -12.0pp | Term 0.76 | ExpMove ±5.6%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜Put 保护异常便宜（Skew -12.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.25×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±5.6% ｜ 11-20（8D）±12.3% ｜ 11-27（15D）±15.6% ｜ 12-04（22D）±18.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,936,485 | GEX Change vs 上次快照 2,863,670 | Flip: Primary Flip: 7.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 166 / LOW 97 / INVALID 161
结构观察区: Primary Flip 7.54（全链重定价，覆盖 98%）
最近结构参考: Flip 8（现价高于该位 7.0%）
量化视角： 正 Gamma（294万，无历史分位）｜正 Gamma 增强（+286万）｜现价位于 Flip 上方 7.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 8（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 8（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 1D
11-20  C +1.0k / P -3 ｜ Activity MEDIUM △ ｜ 8D
11-27  C +1.0k / P +79 ｜ Activity HIGH ｜ 15D
12-04  C +91 / P +3 ｜ Activity MEDIUM △ ｜ 22D

📆 11-13 Forward Structure
存量OI: C 28.0k / P 7.1k，今日变化ΔOI: C +0.2k / P +0.4k，平值价格ATM: C $0.27 / P $0.18 ｜ ATM IV 133.3%，净 delta 敞口 -33k shares
Top ΔOI: P 8 +624
仓位参考: Max Pain 8 ｜ Call Wall 8（-0.9%，弱）（OI 1.8k） ｜ Put Wall 8（-0.9%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 133.3%｜历史 Rank 72%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 33,087 股

11-20（MEDIUM △）Top ΔOI: 8C +741 ｜ 8P +301
11-20（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 8（-0.9%，弱）（OI 1.7k） ｜ Put Wall 8（-0.9%，弱）（OI 7.2k）

📆 11-27 Forward Structure
存量OI: C 11.6k / P 3.2k，今日变化ΔOI: C +1.0k / P +79，平值价格ATM: C $0.70 / P $0.56 ｜ ATM IV 96.6%，净 delta 敞口 50k shares
Top ΔOI: C 8 +920
仓位参考: Max Pain 8 ｜ Call Wall 8（-0.9%，弱）（OI 1.3k） ｜ Put Wall 8（-0.9%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 96.6%｜历史 Rank 72%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 49,728 股

12-04（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 8（-0.9%，弱）（OI 0.1k） ｜ Put Wall 8.5（+5.3%）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 133.3% vs 11-20 105.2%（差 +28.1pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/USAR_evening.json