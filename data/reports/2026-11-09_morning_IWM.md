# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-10 283C ΔOI +6,509（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-12 285C ΔOI +3,962 占该期限总 OI 13.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 273.67 → 今开 277.44（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 279.56 ｜ 低 276.81

Options: P/C成交量 0.41 | OI比 0.95 | ATM IV 27.8% | Skew 3.1pp | Term 0.75 | ExpMove ±1.3%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价中性（Skew 3.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-10（1D）±1.3% ｜ 11-11（2D）±1.5% ｜ 11-12（3D）±1.8% ｜ 11-13（4D）±2.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -554,122,381 | GEX Change vs 上次快照 289,119,263 | Flip: Primary Flip: 284.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1425 / LOW 175 / INVALID 1076
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 284.87（全链重定价，覆盖 98%）
Put Wall 260（弱结构｜现价高于该位 7.3%） | Call Wall 290（弱结构｜现价低于该位 3.8%）
最近结构参考: Flip 285（现价低于该位 2.0%）
量化视角： 负 Gamma（5.54亿，无历史分位）｜负 Gamma 缓解（+2.89亿）｜现价位于 Flip 下方 2.04%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 276（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 285（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 260.0P — Vol 51,694 | 最新价 $1.65 | OI 115488→160408 (ΔOI +44920张) | ΔOI/Volume 86.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增44920张（+38.9% vs前日OI），连续性待观察（方向未知）
11-20 267.0P — Vol 31,016 | 最新价 $2.88 | OI 45591→75914 (ΔOI +30323张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30323张（+66.5% vs前日OI），连续性待观察（方向未知）
11-27 267.0P — Vol 30,439 | 最新价 $3.17 | OI 1972→32084 (ΔOI +30112张) | ΔOI/Volume 98.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增30112张（+1527.0% vs前日OI），连续性待观察（方向未知）
11-09 279.0C — Vol 14,096 | 最新价 $0.24 | OI 537→9825 (ΔOI +9288张) | ΔOI/Volume 65.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9288张（+1729.6% vs前日OI），连续性待观察（方向未知）
11-09 282.0C — Vol 8,963 | 最新价 $0.05 | OI 1155→8733 (ΔOI +7578张) | ΔOI/Volume 84.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7578张（+656.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 122,221 张（Put 105,355 / Call 16,866），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $26M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 63.6k / P 60.2k，今日成交量: C 107.1k / P 43.5k，平值价格ATM: C $1.02 / P $0.69 ｜ ATM IV 27.8%，预期波动 ±0.6%，Max Pain 276
Top ΔOI: C 279 +9,288 ｜ C 282 +7,578 ｜ P 240 +4,012

📆 Forward Expiration Structure

11-10  C +19.3k / P +5.5k ｜ Activity HIGH ｜ 1D
11-11  C +1.7k / P +1.1k ｜ Activity HIGH ｜ 2D
11-12  C +11.4k / P +2.3k ｜ Activity HIGH ｜ 3D
11-13  C +14.4k / P +27.7k ｜ Activity HIGH ｜ 4D

📆 11-10 Forward Structure
存量OI: C 43.5k / P 32.2k，今日变化ΔOI: C +19.3k / P +5.5k，平值价格ATM: C $1.96 / P $1.60 ｜ ATM IV 27.2%，净 delta 敞口 879k shares
Top ΔOI: C 283 +6,509 ｜ C 275 +5,130 ｜ C 281 +3,181
仓位参考: Max Pain 277 ｜ Call Wall 283（+1.4%，弱）（OI 6.9k） ｜ Put Wall 265（-5.0%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 27.2%｜历史 Rank 60%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 879,018 股

📆 11-11 Forward Structure
存量OI: C 14.0k / P 24.6k，今日变化ΔOI: C +1.7k / P +1.1k，平值价格ATM: C $2.23 / P $1.98 ｜ ATM IV 24.7%，净 delta 敞口 140k shares
Top ΔOI: P 255 -2,469 ｜ P 270 +2,211 ｜ P 266 -1,970
仓位参考: Max Pain 279 ｜ Call Wall 286（+2.5%，弱）（OI 1.8k） ｜ Put Wall 270（-3.2%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 24.7%｜历史 Rank 60%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 140,284 股

📆 11-12 Forward Structure
存量OI: C 19.1k / P 11.3k，今日变化ΔOI: C +11.4k / P +2.3k，平值价格ATM: C $2.60 / P $2.39 ｜ ATM IV 23.6%，净 delta 敞口 428k shares
Top ΔOI: C 285 +3,962 ｜ C 279 +1,606 ｜ C 283 +1,170
仓位参考: Max Pain 277 ｜ Call Wall 285（+2.1%）（OI 4.6k） ｜ Put Wall 257.5（-7.7%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 23.6%｜历史 Rank 60%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 427,739 股

📆 11-13 Forward Structure
存量OI: C 92.7k / P 163.7k，今日变化ΔOI: C +14.4k / P +27.7k，平值价格ATM: C $3.05 / P $2.67 ｜ ATM IV 23.4%，净 delta 敞口 539k shares
Top ΔOI: P 264 +4,590 ｜ P 269 +4,376 ｜ P 256 +4,105
仓位参考: Max Pain 278 ｜ Call Wall 302（+8.2%，弱）（OI 13.7k） ｜ Put Wall 265（-5.0%，弱）（OI 14.1k）
量化解读： 存量 Put 重｜ATM IV 23.4%｜历史 Rank 60%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 正 538,654 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/IWM_morning.json