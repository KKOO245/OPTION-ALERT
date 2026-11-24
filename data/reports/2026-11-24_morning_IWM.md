# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $718.15 ｜ QQQ $638.10
VIX 27.25 ↑2.4%（5D +7.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 11-25 263P ΔOI +2,702（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-01 270C ΔOI +2,965 占该期限总 OI 10.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 265.74 → 今开 264.02（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 267.45 ｜ 低 263.97

Options: P/C成交量 0.56 | OI比 2.12 | ATM IV 36.7% | Skew 5.7pp | Term 0.66 | ExpMove ±1.4%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价中性（Skew 5.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.12×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-25（1D）±1.4% ｜ 11-27（3D）±1.8% ｜ 11-30（6D）±2.2% ｜ 12-01（7D）±2.5%
   ⇒ IV–VIX Spread: +9.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -805,271,595 | GEX Change vs 上次快照 75,407,338 | Flip: Primary Flip: 283.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1250 / LOW 251 / INVALID 1219
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 283.25（全链重定价，覆盖 98%）
Put Wall 260（弱结构｜现价高于该位 2.7%）
最近结构参考: Put Wall 260（现价高于该位 2.7%）
量化视角： 负 Gamma（8.05亿，无历史分位）｜负 Gamma 缓解（+7541万）｜现价位于 Flip 下方 5.72%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 266（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 283（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 252.0P — Vol 42,973 | 最新价 $3.07 | OI 27279→49113 (ΔOI +21834张) | ΔOI/Volume 50.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21834张（+80.0% vs前日OI），连续性待观察（方向未知）
12-18 251.0P — Vol 53,865 | 最新价 $2.85 | OI 22100→36587 (ΔOI +14487张) | ΔOI/Volume 26.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14487张（+65.5% vs前日OI），连续性待观察（方向未知）
12-04 260.0P — Vol 11,767 | 最新价 $2.62 | OI 7056→16981 (ΔOI +9925张) | ΔOI/Volume 84.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9925张（+140.7% vs前日OI），连续性待观察（方向未知）
12-04 240.0P — Vol 9,604 | 最新价 $0.47 | OI 668→9402 (ΔOI +8734张) | ΔOI/Volume 90.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8734张（+1307.5% vs前日OI），连续性待观察（方向未知）
11-24 247.5P — Vol 9,724 | 最新价 $0.01 | OI 4714→11778 (ΔOI +7064张) | ΔOI/Volume 72.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7064张（+149.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 62,044 张（Put 62,044 / Call 0），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $13M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 36.4k / P 77.3k，今日成交量: C 122.7k / P 68.8k，平值价格ATM: C $1.29 / P $0.87 ｜ ATM IV 36.7%，预期波动 ±0.8%，Max Pain 266
Top ΔOI: P 247 +7,064 ｜ P 255 +4,577 ｜ P 245 +4,521

📆 Forward Expiration Structure

11-25  C +6.0k / P +4.5k ｜ Activity HIGH ｜ 1D
11-27  C +15.5k / P -2.4k ｜ Activity HIGH ｜ 3D
11-30  C +5.4k / P +6.4k ｜ Activity HIGH ｜ 6D
12-01  C +4.2k / P +4.0k ｜ Activity HIGH ｜ 7D

📆 11-25 Forward Structure
存量OI: C 29.8k / P 43.1k，今日变化ΔOI: C +6.0k / P +4.5k，平值价格ATM: C $2.15 / P $1.69 ｜ ATM IV 30.1%，净 delta 敞口 62k shares
Top ΔOI: P 263 +2,702 ｜ C 270 +2,591
仓位参考: Max Pain 266 ｜ Call Wall 277（+3.7%，弱）（OI 4.4k） ｜ Put Wall 261（-2.3%，弱）（OI 6.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 30.1%｜历史 Rank 82%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 62,264 股

📆 11-27 Forward Structure
存量OI: C 112.0k / P 240.4k，今日变化ΔOI: C +15.5k / P -2.4k，平值价格ATM: C $2.53 / P $2.15 ｜ ATM IV 23.5%，净 delta 敞口 1.5M shares
Top ΔOI: P 255 +6,537 ｜ C 270 +6,434 ｜ P 276 -5,280
仓位参考: Max Pain 270 ｜ Call Wall 270（+1.1%，弱）（OI 9.7k） ｜ Put Wall 270（+1.1%，弱）（OI 35.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 23.5%｜历史 Rank 82%（近端代理）｜IV/RV 0.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,474,724 股

📆 11-30 Forward Structure
存量OI: C 21.7k / P 61.3k，今日变化ΔOI: C +5.4k / P +6.4k，平值价格ATM: C $3.22 / P $2.75 ｜ ATM IV 21.3%，净 delta 敞口 63k shares
Top ΔOI: P 257 +4,562 ｜ C 273 +1,561 ｜ C 270 +1,122
仓位参考: Max Pain 269 ｜ Call Wall 276（+3.3%，弱）（OI 3.9k） ｜ Put Wall 255（-4.5%，弱）（OI 10.0k）
量化解读： 存量 Put 重｜ATM IV 21.3%｜历史 Rank 82%（近端代理）｜IV/RV 0.70×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 63,363 股

📆 12-01 Forward Structure
存量OI: C 13.7k / P 14.5k，今日变化ΔOI: C +4.2k / P +4.0k，平值价格ATM: C $3.60 / P $3.13 ｜ ATM IV 22.4%，净 delta 敞口 60k shares
Top ΔOI: C 270 +2,965 ｜ P 260 +2,164 ｜ C 271 +459
仓位参考: Max Pain 265 ｜ Call Wall 270（+1.1%，弱）（OI 3.1k） ｜ Put Wall 260（-2.6%）（OI 6.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 22.4%｜历史 Rank 82%（近端代理）｜IV/RV 0.74×（近似）｜净 delta 敞口 正 60,283 股

📅 事件差分（观察，非因果）: 11-25（1D）ATM IV 30.1% vs 11-27 23.5%（差 +6.6pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/IWM_morning.json