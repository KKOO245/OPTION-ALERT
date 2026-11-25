# 期权晚报 2026-11-25（快照 16:40 ET）

📊 市场环境

SPY $716.70 ｜ QQQ $633.93
VIX 28.29 ↑7.3%（5D +15.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-27（2D）ATM IV 68.8% vs 11-30 50.7%（差 +18.2pp），覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-27 380P ΔOI +1,264（距现价 -0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 370.23 → 收盘 380.14（+2.7%） ｜ 今日高 383.73 ｜ 低 357.64 ｜ 昨收 384.68 → 收盘 380.14（-1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.79 | OI比 1.04 | ATM IV 52.7% | Skew -1.6pp | Term 1.04 | ExpMove ±0.0%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构正常（Term 1.04）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-27（2D）±0.0% ｜ 11-30（5D）±4.6% ｜ 12-02（7D）±6.0% ｜ 12-04（9D）±0.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 56,339,004 | GEX Change vs 上次快照 59,586,586 | Flip: Primary Flip: 363.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 1242 / LOW 265 / INVALID 901
结构观察区: Primary Flip 363.88（全链重定价，覆盖 94%）
Call Wall 400（弱结构｜现价低于该位 5.0%）
最近结构参考: Flip 364（现价高于该位 4.5%）
量化视角： 正 Gamma（5634万，无历史分位）｜由负转正（+5959万）｜现价位于 Flip 上方 4.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 380（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 364（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +7.0k / P +11.1k ｜ Activity HIGH ｜ 2D
11-30  C +7.9k / P +4.5k ｜ Activity HIGH ｜ 5D
12-02  C +2.8k / P +5.0k ｜ Activity HIGH ｜ 7D
12-04  C +4.5k / P +5.5k ｜ Activity HIGH ｜ 9D

📆 11-27 Forward Structure
存量OI: C 150.1k / P 218.2k，今日变化ΔOI: C +7.0k / P +11.1k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 68.8%，净 delta 敞口 -108k shares
Top ΔOI: C 400 +1,859 ｜ P 380 +1,264 ｜ P 360 +1,030
仓位参考: Max Pain 368 ｜ Call Wall 410（+7.9%，弱）（OI 10.2k）
量化解读： 存量 Put 重｜ATM IV 68.8%｜历史 Rank 52%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 108,303 股

📆 11-30 Forward Structure
存量OI: C 26.7k / P 14.3k，今日变化ΔOI: C +7.9k / P +4.5k，平值价格ATM: C $8.95 / P $8.54 ｜ ATM IV 50.7%，净 delta 敞口 29k shares
Top ΔOI: C 420 +2,833 ｜ P 370 +902 ｜ C 400 +766
仓位参考: Max Pain 388 ｜ Put Wall 392.5（+3.3%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 50.7%｜历史 Rank 52%（近端代理）｜IV/RV 0.70×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 28,910 股

📆 12-02 Forward Structure
存量OI: C 7.3k / P 8.3k，今日变化ΔOI: C +2.8k / P +5.0k，平值价格ATM: C $11.80 / P $11.00 ｜ ATM IV 52.5%，净 delta 敞口 -27k shares
Top ΔOI: P 352 +4,104 ｜ C 395 +402
仓位参考: Max Pain 372 ｜ Call Wall 372.5（-2.0%，弱）（OI 0.8k） ｜ Put Wall 352.5（-7.3%）（OI 4.2k）
量化解读： 存量两侧均衡｜ATM IV 52.5%｜历史 Rank 52%（近端代理）｜IV/RV 0.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 27,344 股

📆 12-04 Forward Structure
存量OI: C 60.0k / P 58.2k，今日变化ΔOI: C +4.5k / P +5.5k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 50.2%，净 delta 敞口 67k shares
Top ΔOI: P 295 +1,400
仓位参考: Max Pain 378 ｜ Call Wall 400（+5.2%）（OI 7.0k） ｜ Put Wall 350（-7.9%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 50.2%｜历史 Rank 52%（近端代理）｜IV/RV 0.69×（近似）｜净 delta 敞口 正 66,721 股

📅 事件差分（观察，非因果）: 11-27（2D）ATM IV 68.8% vs 11-30 50.7%（差 +18.2pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/TSLA_evening.json