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
🟡 **近现价集中开仓**: 11-24 255P ΔOI +5,619（距现价 -4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 266.04 → 收盘 265.74（-0.1%） ｜ 今日高 266.08 ｜ 低 263.00 ｜ 昨收 256.61 → 收盘 265.74（+3.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.23 | OI比 1.82 | ATM IV 30.3% | Skew 1.5pp | Term 0.78 | ExpMove ±1.2%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜当日成交偏 Put（P/C量 1.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.23×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.82×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-24（1D）±1.2% ｜ 11-25（2D）±1.7% ｜ 11-27（4D）±1.9% ｜ 11-30（7D）±2.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -861,515,513 | GEX Change vs 上次快照 28,291,966 | Flip: Primary Flip: 283.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 1196 / LOW 315 / INVALID 1211
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 283.99（全链重定价，覆盖 95%）
Put Wall 260（弱结构｜现价高于该位 2.2%）
最近结构参考: Put Wall 260（现价高于该位 2.2%）
量化视角： 负 Gamma（8.62亿，无历史分位）｜负 Gamma 缓解（+2829万）｜现价位于 Flip 下方 6.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构）；上方 268（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 284（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 254.0P — Vol 2,732 | 最新价 $1.55 | OI 1744→57841 (ΔOI +56097张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增56097张（+3216.6% vs前日OI），连续性待观察（方向未知）
12-18 249.0P — Vol 359 | 最新价 $2.53 | OI 1326→22779 (ΔOI +21453张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21453张（+1617.9% vs前日OI），连续性待观察（方向未知）
12-18 245.0P — Vol 28,071 | 最新价 $2.01 | OI 71773→91888 (ΔOI +20115张) | ΔOI/Volume 71.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20115张（+28.0% vs前日OI），连续性待观察（方向未知）
12-18 248.0P — Vol 1,907 | 最新价 $2.36 | OI 2217→19781 (ΔOI +17564张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17564张（+792.2% vs前日OI），连续性待观察（方向未知）
12-18 247.0P — Vol 670 | 最新价 $2.25 | OI 2212→16392 (ΔOI +14180张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14180张（+641.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 129,409 张（Put 129,409 / Call 0），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $26M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-24  C +6.5k / P +25.4k ｜ Activity HIGH ｜ 1D
11-25  C +6.6k / P +2.7k ｜ Activity HIGH ｜ 2D
11-27  C +17.6k / P +39.2k ｜ Activity HIGH ｜ 4D
11-30  C +2.4k / P +25.4k ｜ Activity HIGH ｜ 7D

📆 11-24 Forward Structure
存量OI: C 17.4k / P 39.1k，今日变化ΔOI: C +6.5k / P +25.4k，平值价格ATM: C $1.44 / P $1.77 ｜ ATM IV 28.7%，净 delta 敞口 210k shares
Top ΔOI: P 255 +5,619 ｜ P 247 +4,714 ｜ P 250 +4,621
仓位参考: Max Pain 269 ｜ Call Wall 271（+2.0%）（OI 2.5k） ｜ Put Wall 255（-4.0%，弱）（OI 7.2k）
量化解读： 存量 Put 重｜ATM IV 28.7%｜历史 Rank 62%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 209,570 股

📆 11-25 Forward Structure
存量OI: C 23.8k / P 38.6k，今日变化ΔOI: C +6.6k / P +2.7k，平值价格ATM: C $2.10 / P $2.40 ｜ ATM IV 28.3%，净 delta 敞口 415k shares
Top ΔOI: P 257 +2,255 ｜ C 267 +1,417 ｜ P 255 +1,079
仓位参考: Max Pain 267 ｜ Call Wall 277（+4.2%，弱）（OI 4.3k） ｜ Put Wall 261（-1.8%，弱）（OI 6.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 28.3%｜历史 Rank 62%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 415,355 股

📆 11-27 Forward Structure
存量OI: C 96.6k / P 242.8k，今日变化ΔOI: C +17.6k / P +39.2k，平值价格ATM: C $2.47 / P $2.67 ｜ ATM IV 23.8%，净 delta 敞口 735k shares
Top ΔOI: P 250 +11,115 ｜ P 255 +9,320 ｜ C 263 +3,866
仓位参考: Max Pain 275 ｜ Call Wall 275（+3.5%，弱）（OI 6.8k） ｜ Put Wall 270（+1.6%，弱）（OI 35.0k）
量化解读： 存量 Put 重｜ATM IV 23.8%｜历史 Rank 62%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 734,627 股

📆 11-30 Forward Structure
存量OI: C 16.3k / P 54.9k，今日变化ΔOI: C +2.4k / P +25.4k，平值价格ATM: C $3.11 / P $3.27 ｜ ATM IV 21.7%，净 delta 敞口 -12k shares
Top ΔOI: P 250 +6,681 ｜ P 255 +6,381 ｜ P 235 +3,841
仓位参考: Max Pain 269 ｜ Call Wall 276（+3.9%，弱）（OI 3.9k） ｜ Put Wall 255（-4.0%，弱）（OI 10.2k）
量化解读： 存量 Put 重｜ATM IV 21.7%｜历史 Rank 62%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 负 11,938 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/IWM_evening.json