# 期权晚报 2026-11-23（快照 16:40 ET）

📊 市场环境

SPY $722.29 ｜ QQQ $651.03
VIX 26.62 ↓25.8%（5D +16.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.4 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🔴 **事件差分**: 11-25（2D）ATM IV 62.8% vs 11-27 38.2%（差 +24.5pp），覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-25 370C ΔOI +1,057（距现价 -4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 120P ΔOI +66,217 占该期限总 OI 22.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 374.84 → 收盘 385.46（+2.8%） ｜ 今日高 393.83 ｜ 低 371.99 ｜ 昨收 345.82 → 收盘 385.46（+11.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.79 | OI比 0.97 | ATM IV 40.6% | Skew 8.8pp | Term 1.36 | ExpMove ±3.7%（近端） | Rank 13%
量化视角： IV 历史低位（Rank 13%，期权偏便宜）｜期限结构正常偏陡（Term 1.36）｜保护溢价显著（Skew 8.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-25（2D）±3.7% ｜ 11-27（4D）±0.1% ｜ 11-30（7D）±5.3% ｜ 12-02（9D）±6.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 57,209,743 | GEX Change vs 上次快照 -5,676,251 | Flip: Primary Flip: 359.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 1158 / LOW 237 / INVALID 983
结构观察区: Primary Flip 359.45（全链重定价，覆盖 94%）
Call Wall 400（弱结构｜现价低于该位 3.6%）
最近结构参考: Call Wall 400（现价低于该位 3.6%）
量化视角： 正 Gamma（5721万，无历史分位）｜正 Gamma 减弱（568万）｜现价位于 Flip 上方 7.24%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 359（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 120.0P — Vol 831 | 最新价 $0.01 | OI 2233→68450 (ΔOI +66217张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增66217张（+2965.4% vs前日OI），连续性待观察（方向未知）
11-27 130.0P — Vol 1,491 | 最新价 $0.01 | OI 350→17272 (ΔOI +16922张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16922张（+4834.9% vs前日OI），连续性待观察（方向未知）
11-27 200.0P — Vol 616 | 最新价 $0.02 | OI 5031→14921 (ΔOI +9890张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9890张（+196.6% vs前日OI），连续性待观察（方向未知）
11-30 420.0C — Vol 6,917 | 最新价 $0.69 | OI 3290→11309 (ΔOI +8019张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8019张（+243.7% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 101,048 张（Put 93,029 / Call 8,019），跨 2 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-25  C +5.9k / P +4.4k ｜ Activity HIGH ｜ 2D
11-27  C +30.9k / P +113.1k ｜ Activity HIGH ｜ 4D
11-30  C +10.7k / P +4.9k ｜ Activity HIGH ｜ 7D
12-02  C +1.4k / P +1.2k ｜ Activity HIGH ｜ 9D

📆 11-25 Forward Structure
存量OI: C 13.8k / P 13.6k，今日变化ΔOI: C +5.9k / P +4.4k，平值价格ATM: C $7.50 / P $6.80 ｜ ATM IV 62.8%，净 delta 敞口 366k shares
Top ΔOI: C 370 +1,057 ｜ C 375 +624
仓位参考: Max Pain 372 ｜ Call Wall 400（+3.8%，弱）（OI 1.2k） ｜ Put Wall 382.5（-0.8%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 62.8%｜历史 Rank 13%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 366,500 股

📆 11-27 Forward Structure
存量OI: C 118.0k / P 179.5k，今日变化ΔOI: C +30.9k / P +113.1k，平值价格ATM: C $0.00 / P $0.42 ｜ ATM IV 38.2%，净 delta 敞口 2.0M shares
Top ΔOI: P 120 +66,217
仓位参考: Max Pain 362 ｜ Call Wall 410（+6.4%，弱）（OI 9.8k）
量化解读： 存量 Put 重｜ATM IV 38.2%｜历史 Rank 13%（近端代理）｜IV/RV 0.61×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,004,255 股

📆 11-30 Forward Structure
存量OI: C 17.7k / P 9.6k，今日变化ΔOI: C +10.7k / P +4.9k，平值价格ATM: C $10.82 / P $9.80 ｜ ATM IV 47.9%，净 delta 敞口 -19k shares
Top ΔOI: C 420 +8,019 ｜ P 395 +1,511 ｜ P 392 +1,488
仓位参考: Max Pain 395 ｜ Call Wall 420（+9.0%）（OI 11.3k） ｜ Put Wall 395（+2.5%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 47.9%｜历史 Rank 13%（近端代理）｜IV/RV 0.77×（近似）｜净 delta 敞口 负 19,081 股

📆 12-02 Forward Structure
存量OI: C 3.1k / P 2.4k，今日变化ΔOI: C +1.4k / P +1.2k，平值价格ATM: C $12.88 / P $11.35 ｜ ATM IV 49.8%，净 delta 敞口 74k shares
Top ΔOI: C 372 +442 ｜ C 400 +247
仓位参考: Max Pain 372 ｜ Call Wall 400（+3.8%，弱）（OI 0.5k） ｜ Put Wall 360（-6.6%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 49.8%｜历史 Rank 13%（近端代理）｜IV/RV 0.80×（近似）｜净 delta 敞口 正 73,888 股

📅 事件差分（观察，非因果）: 11-25（2D）ATM IV 62.8% vs 11-27 38.2%（差 +24.5pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/TSLA_evening.json