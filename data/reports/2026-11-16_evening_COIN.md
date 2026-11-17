# 期权晚报 2026-11-16（快照 21:00 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（4D）ATM IV 88.3% vs 11-27 72.9%（差 +15.5pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 119.31 → 收盘 119.84（+0.4%） ｜ 今日高 122.98 ｜ 低 117.32 ｜ 昨收 127.64 → 收盘 119.84（-6.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.65 | OI比 0.46 | ATM IV 88.3% | Skew 6.5pp | Term 0.83 | ExpMove ±7.3%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价显著（Skew 6.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±7.3% ｜ 11-27（11D）±9.8% ｜ 12-04（18D）±13.2% ｜ 12-11（25D）±15.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,295,951 | GEX Change vs 上次快照 -5,025,022 | Flip: Primary Flip: 123.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 348 / LOW 198 / INVALID 362
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 123.66（全链重定价，覆盖 100%）
Put Wall 110（现价高于该位 8.9%）
最近结构参考: Flip 124（现价低于该位 3.1%）
量化视角： 负 Gamma（630万，无历史分位）｜负 Gamma 加深（503万）｜现价位于 Flip 下方 3.09%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 110（Put Wall）；上方 134（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 124（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 11D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 18D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 11-20 Forward Structure
存量OI: C 133.7k / P 61.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.35 / P $4.40 ｜ ATM IV 88.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 134 ｜ Call Wall 131（+9.3%，弱）（OI 7.1k） ｜ Put Wall 120（+0.1%，弱）（OI 6.6k）
量化解读： 存量 Call 重｜ATM IV 88.3%｜历史 Rank 78%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-27（Activity LOW）仓位参考: Max Pain 138 ｜ Call Wall 130（+8.5%，弱）（OI 0.3k） ｜ Put Wall 120（+0.1%，弱）（OI 0.6k）

12-04（Activity LOW）仓位参考: Max Pain 140 ｜ Put Wall 125（+4.3%，弱）（OI 0.6k）

12-11（Activity LOW）仓位参考: Max Pain 135 ｜ Call Wall 130（+8.5%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 88.3% vs 11-27 72.9%（差 +15.5pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/COIN_evening.json