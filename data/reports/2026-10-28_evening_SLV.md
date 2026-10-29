# 期权晚报 2026-10-28（快照 21:00 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 16.91 ↓3.5%（5D +1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-30 ATM IV 45.1% vs 11-02 34.7%（差 +10.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 48.83 → 收盘 49.06（+0.5%） ｜ 今日高 49.08 ｜ 低 48.12 ｜ 昨收 49.16 → 收盘 49.06（-0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.41 | OI比 0.42 | ATM IV 45.1% | Skew 1.2pp | Term 0.83 | ExpMove ±3.0%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜存量 Call 偏重（OI比 0.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±3.0% ｜ 11-02（5D）±3.1% ｜ 11-04（7D）±4.2% ｜ 11-06（9D）±5.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,576,455 | GEX Change vs 上次快照 850,222 | Flip: Primary Flip: 48.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 685 / LOW 97 / INVALID 310
结构观察区: Primary Flip 48.96（全链重定价，覆盖 98%）
Put Wall 50（弱结构｜现价低于该位 1.9%）
最近结构参考: Flip 49（现价高于该位 0.2%）
量化视角： 正 Gamma（258万，无历史分位）｜正 Gamma 增强（+85万）｜现价位于 Flip 上方 0.21%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 5D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-30 Forward Structure
存量OI: C 91.4k / P 38.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.70 / P $0.75 ｜ ATM IV 45.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 50 ｜ Call Wall 50（+1.9%，弱）（OI 4.3k） ｜ Put Wall 45（-8.3%，弱）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 45.1%｜历史 Rank 76%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-02（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 50（+1.9%，弱）（OI 0.6k） ｜ Put Wall 45（-8.3%，弱）（OI 0.8k）

11-04（Activity LOW）仓位参考: Max Pain 48 ｜ Call Wall 51.5（+5.0%，弱）（OI 3.1k）

11-06（Activity LOW）仓位参考: Max Pain 52 ｜ Put Wall 50（+1.9%，弱）（OI 2.2k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 45.1% vs 11-02 34.7%（差 +10.4pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/SLV_evening.json