# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.39 ｜ QQQ $651.03
VIX 27.37 ↓23.7%（5D +19.5%） ｜ Vol Regime: STRESS
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
🟡 **事件差分**: 11-27 ATM IV 135.2% vs 12-04 122.8%（差 +12.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 12-04 95C ΔOI +3,252（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-11 80P ΔOI +10,556 占该期限总 OI 10.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 79.24 → 今开 98.56（+24.4%） | 较昨收变动（含盘初走势） ｜ 今日高 99.00 ｜ 低 88.30

Options: P/C成交量 0.67 | OI比 0.42 | ATM IV 135.2% | Skew 19.0pp | Term 0.78 | ExpMove ±11.2%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 19.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±11.2% ｜ 12-04（11D）±16.8% ｜ 12-11（18D）±21.8% ｜ 12-18（25D）±22.7%
   ⇒ IV–VIX Spread: +107.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,449,816 | GEX Change vs 上次快照 -3,743,116 | Flip: Primary Flip: 95.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1093 / LOW 1091 / INVALID 3720
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 95.58（全链重定价，覆盖 100%）
最近结构参考: Flip 96（现价低于该位 3.1%）
量化视角： 负 Gamma（745万，无历史分位）｜负 Gamma 加深（374万）｜现价位于 Flip 下方 3.14%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 100（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 96（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 75.0P — Vol 8,317 | 最新价 $8.60 | OI 8577→69040 (ΔOI +60463张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60463张（+704.9% vs前日OI），连续性待观察（方向未知）
12-18 10.0P — Vol 32 | 最新价 $0.05 | OI 4210→33680 (ΔOI +29470张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29470张（+700.0% vs前日OI），连续性待观察（方向未知）
11-27 100.0C — Vol 11,889 | 最新价 $0.55 | OI 2178→23856 (ΔOI +21678张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21678张（+995.3% vs前日OI），连续性待观察（方向未知）
12-18 87.5P — Vol 3,743 | 最新价 $15.58 | OI 3306→24118 (ΔOI +20812张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20812张（+629.5% vs前日OI），连续性待观察（方向未知）
12-18 62.5P — Vol 3,974 | 最新价 $4.30 | OI 2813→21815 (ΔOI +19002张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19002张（+675.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 151,425 张（Put 129,747 / Call 21,678），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +255.4k / P +106.8k ｜ Activity HIGH ｜ 4D
12-04  C +110.8k / P +57.0k ｜ Activity HIGH ｜ 11D
12-11  C +52.4k / P +39.7k ｜ Activity HIGH ｜ 18D
12-18  C +490.6k / P +482.6k ｜ Activity HIGH ｜ 25D

📆 11-27 Forward Structure
存量OI: C 284.6k / P 119.6k，今日变化ΔOI: C +255.4k / P +106.8k，平值价格ATM: C $5.00 / P $5.40 ｜ ATM IV 135.2%，净 delta 敞口 -1.1M shares
Top ΔOI: C 100 +21,678 ｜ C 158 +11,578
仓位参考: Max Pain 100 ｜ Call Wall 100（+8.0%，弱）（OI 23.9k） ｜ Put Wall 100（+8.0%，弱）（OI 6.2k）
量化解读： 存量 Call 重｜ATM IV 135.2%｜历史 Rank 85%（近端代理）｜IV/RV 0.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,088,485 股

📆 12-04 Forward Structure
存量OI: C 123.5k / P 64.6k，今日变化ΔOI: C +110.8k / P +57.0k，平值价格ATM: C $7.91 / P $7.60 ｜ ATM IV 122.8%，净 delta 敞口 -1.2M shares
Top ΔOI: C 85 +3,311 ｜ C 95 +3,252
仓位参考: Max Pain 102 ｜ Call Wall 85（-8.2%，弱）（OI 3.3k） ｜ Put Wall 87.5（-5.5%，弱）（OI 3.5k）
量化解读： 存量 Call 重｜ATM IV 122.8%｜历史 Rank 85%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,181,012 股

📆 12-11 Forward Structure
存量OI: C 58.6k / P 43.8k，今日变化ΔOI: C +52.4k / P +39.7k，平值价格ATM: C $9.40 / P $10.80 ｜ ATM IV 115.1%，净 delta 敞口 -880k shares
Top ΔOI: P 80 +10,556 ｜ P 60 +2,260
仓位参考: Max Pain 106 ｜ Call Wall 97.5（+5.3%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 115.1%｜历史 Rank 85%（近端代理）｜IV/RV 0.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 879,996 股

📆 12-18 Forward Structure
存量OI: C 560.5k / P 552.3k，今日变化ΔOI: C +490.6k / P +482.6k，平值价格ATM: C $10.60 / P $10.41 ｜ ATM IV 111.0%，净 delta 敞口 -8.6M shares
Top ΔOI: P 75 +60,463 ｜ P 10 +29,470 ｜ P 87 +20,812
仓位参考: Max Pain 119 ｜ Call Wall 100（+8.0%，弱）（OI 4.3k） ｜ Put Wall 87.5（-5.5%，弱）（OI 24.1k）
量化解读： 存量两侧均衡｜ATM IV 111.0%｜历史 Rank 85%（近端代理）｜IV/RV 0.14×（近似）｜净 delta 敞口 负 8,586,063 股

📅 事件差分（观察，非因果）: 11-27（4D）ATM IV 135.2% vs 12-04 122.8%（差 +12.4pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/SNDK_morning.json