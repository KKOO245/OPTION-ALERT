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
🔴 **事件差分**: 11-13（1D）ATM IV 105.3% vs 11-20 87.2%（差 +18.1pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-13 11P ΔOI +23（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 11.04 → 收盘 11.09（+0.5%） ｜ 今日高 11.59 ｜ 低 10.91 ｜ 昨收 11.59 → 收盘 11.09（-4.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.90 | OI比 0.40 | ATM IV 105.3% | Skew 19.6pp | Term 0.79 | ExpMove ±6.8%（近端） | Rank 51%
量化视角： IV 中性（Rank 51%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价显著（Skew 19.6pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.40）+ 当日成交偏 Put（P/C量 1.90）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.90×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±6.8% ｜ 11-20（8D）±16.1% ｜ 11-27（15D）±11.7% ｜ 12-04（22D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,189,943 | GEX Change vs 上次快照 96,007 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 174 / LOW 80 / INVALID 132
结构观察区: NO_CROSS
Put Wall 11（现价高于该位 0.8%）
最近结构参考: Put Wall 11（现价高于该位 0.8%）
量化视角： 正 Gamma（119万，无历史分位）｜正 Gamma 增强（+10万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall）；上方 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +32 / P +1 ｜ Activity MEDIUM △ ｜ 1D
11-20  C +41 / P -0.2k ｜ Activity MEDIUM △ ｜ 8D
11-27  C +43 / P -76 ｜ Activity MEDIUM △ ｜ 15D
12-04  C +3 / P +6 ｜ Activity LOW ｜ 22D

📆 11-13 Forward Structure
存量OI: C 3.1k / P 1.2k，今日变化ΔOI: C +32 / P +1，平值价格ATM: C $0.40 / P $0.35 ｜ ATM IV 105.3%，净 delta 敞口 165 shares
Top ΔOI: P 11 +23 ｜ P 12 -16
仓位参考: Max Pain 12 ｜ Call Wall 12（+8.2%，弱）（OI 0.3k） ｜ Put Wall 11（-0.8%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 105.3%｜历史 Rank 51%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 165 股

11-20（MEDIUM △）Top ΔOI: 11P -146 ｜ 11P -109
11-20（MEDIUM △）仓位参考: Max Pain 12 ｜ Call Wall 12（+8.2%，弱）（OI 0.7k） ｜ Put Wall 12（+8.2%，弱）（OI 0.3k）

11-27（MEDIUM △）Top ΔOI: 12C +14
11-27（MEDIUM △）仓位参考: Max Pain 12

12-04（Activity LOW）仓位参考: Max Pain 13

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 105.3% vs 11-20 87.2%（差 +18.1pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/NNE_evening.json