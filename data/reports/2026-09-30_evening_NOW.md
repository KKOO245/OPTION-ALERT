# 期权晚报 2026-09-30（快照 16:40 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $739.77
VIX 16.34 ↑1.9%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 132C ΔOI +1,125（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 129.75 → 收盘 134.01（+3.3%） ｜ 今日高 135.06 ｜ 低 128.85 ｜ 昨收 129.94 → 收盘 134.01（+3.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.38 | OI比 0.81 | ATM IV 55.3% | Skew -2.2pp | Term 1.06 | ExpMove ±3.4%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常（Term 1.06）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（2D）±3.4% ｜ 10-09（9D）±6.2% ｜ 10-16（16D）±8.3% ｜ 10-23（23D）±10.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,839,089 | GEX Change vs 上次快照 3,556,107 | Flip: Primary Flip: 131.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 553 / LOW 35 / INVALID 108
结构观察区: Primary Flip 131.84（全链重定价，覆盖 100%）
Put Wall 125（弱结构｜现价高于该位 7.2%）
最近结构参考: Flip 132（现价高于该位 1.6%）
量化视角： 正 Gamma（684万，无历史分位）｜正 Gamma 增强（+356万）｜现价位于 Flip 上方 1.65%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 125（Put Wall，弱结构） / 132（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +4.0k / P +1.1k ｜ Activity HIGH ｜ 2D
10-09  C +1.0k / P +1.3k ｜ Activity HIGH ｜ 9D
10-16  C +1.5k / P +0.7k ｜ Activity HIGH ｜ 16D
10-23  C +0.4k / P +2.5k ｜ Activity HIGH ｜ 23D

📆 10-02 Forward Structure
存量OI: C 31.4k / P 25.4k，今日变化ΔOI: C +4.0k / P +1.1k，平值价格ATM: C $2.41 / P $2.12 ｜ ATM IV 55.3%，净 delta 敞口 227k shares
Top ΔOI: C 132 +1,125 ｜ C 131 +747 ｜ P 129 +446
仓位参考: Max Pain 132 ｜ Call Wall 140（+4.5%，弱）（OI 2.8k） ｜ Put Wall 125（-6.7%）（OI 4.2k）
量化解读： 存量 Call 重｜ATM IV 55.3%｜历史 Rank 28%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 226,587 股

📆 10-09 Forward Structure
存量OI: C 15.3k / P 11.6k，今日变化ΔOI: C +1.0k / P +1.3k，平值价格ATM: C $4.35 / P $3.93 ｜ ATM IV 49.3%，净 delta 敞口 28k shares
Top ΔOI: C 134 +307
仓位参考: Max Pain 134 ｜ Put Wall 125（-6.7%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 49.3%｜历史 Rank 28%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 27,903 股

📆 10-16 Forward Structure
存量OI: C 76.0k / P 62.8k，今日变化ΔOI: C +1.5k / P +0.7k，平值价格ATM: C $5.90 / P $5.25 ｜ ATM IV 49.0%，净 delta 敞口 57k shares
Top ΔOI: C 140 +998 ｜ P 125 +445
仓位参考: Max Pain 130 ｜ Call Wall 140（+4.5%，弱）（OI 5.6k） ｜ Put Wall 125（-6.7%，弱）（OI 6.1k）
量化解读： 存量 Call 重｜ATM IV 49.0%｜历史 Rank 28%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 57,306 股

📆 10-23 Forward Structure
存量OI: C 8.1k / P 15.3k，今日变化ΔOI: C +0.4k / P +2.5k，平值价格ATM: C $7.05 / P $6.52 ｜ ATM IV 50.5%，净 delta 敞口 -22k shares
Top ΔOI: P 122 +1,008 ｜ P 117 +996 ｜ C 137 +283
仓位参考: Max Pain 133 ｜ Call Wall 140（+4.5%，弱）（OI 0.9k） ｜ Put Wall 122（-9.0%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 50.5%｜历史 Rank 28%（近端代理）｜IV/RV 1.28×（近似）｜净 delta 敞口 负 21,684 股

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 55.3% vs 10-09 49.3%（差 +6.0pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/NOW_evening.json