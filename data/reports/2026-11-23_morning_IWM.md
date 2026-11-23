# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.32 ｜ QQQ $651.03
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
🟡 **近现价集中开仓**: 11-24 255P ΔOI +5,619（距现价 -3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 256.61 → 今开 266.04（+3.7%） | 较昨收变动（含盘初走势） ｜ 今日高 266.08 ｜ 低 263.00

Options: P/C成交量 1.55 | OI比 1.82 | ATM IV 43.2% | Skew 3.8pp | Term 0.58 | ExpMove ±1.6%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.58，近月 IV 高于远月）｜保护溢价中性（Skew 3.8pp）｜当日成交偏 Put（P/C量 1.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.55×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.82×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-24（1D）±1.6% ｜ 11-25（2D）±2.0% ｜ 11-27（4D）±2.3% ｜ 11-30（7D）±2.9%
   ⇒ IV–VIX Spread: +15.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -889,807,479 | GEX Change vs 上次快照 -119,621,869 | Flip: Primary Flip: 284.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1245 / LOW 279 / INVALID 1198
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 284.75（全链重定价，覆盖 98%）
Put Wall 260（弱结构｜现价高于该位 1.6%）
最近结构参考: Put Wall 260（现价高于该位 1.6%）
量化视角： 负 Gamma（8.90亿，无历史分位）｜负 Gamma 加深（1.20亿）｜现价位于 Flip 下方 7.27%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构）；上方 268（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 285（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 254.0P — Vol 56,755 | 最新价 $5.60 | OI 1744→57841 (ΔOI +56097张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增56097张（+3216.6% vs前日OI），连续性待观察（方向未知）
12-18 249.0P — Vol 48,778 | 最新价 $6.35 | OI 1326→22779 (ΔOI +21453张) | ΔOI/Volume 44.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21453张（+1617.9% vs前日OI），连续性待观察（方向未知）
12-18 245.0P — Vol 59,575 | 最新价 $5.31 | OI 71773→91888 (ΔOI +20115张) | ΔOI/Volume 33.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20115张（+28.0% vs前日OI），连续性待观察（方向未知）
12-18 248.0P — Vol 34,156 | 最新价 $6.11 | OI 2217→19781 (ΔOI +17564张) | ΔOI/Volume 51.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增17564张（+792.2% vs前日OI），连续性待观察（方向未知）
12-18 247.0P — Vol 31,021 | 最新价 $5.86 | OI 2212→16392 (ΔOI +14180张) | ΔOI/Volume 45.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14180张（+641.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 129,409 张（Put 129,409 / Call 0），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $75M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 50.6k / P 92.2k，今日成交量: C 61.7k / P 95.5k，平值价格ATM: C $1.34 / P $1.13 ｜ ATM IV 43.2%，预期波动 ±0.9%，Max Pain 268
Top ΔOI: P 252 +13,418 ｜ P 250 +10,880 ｜ P 247 +8,653

📆 Forward Expiration Structure

11-24  C +6.5k / P +25.4k ｜ Activity HIGH ｜ 1D
11-25  C +6.6k / P +2.7k ｜ Activity HIGH ｜ 2D
11-27  C +17.6k / P +39.2k ｜ Activity HIGH ｜ 4D
11-30  C +2.4k / P +25.4k ｜ Activity HIGH ｜ 7D

📆 11-24 Forward Structure
存量OI: C 17.4k / P 39.1k，今日变化ΔOI: C +6.5k / P +25.4k，平值价格ATM: C $2.17 / P $2.03 ｜ ATM IV 33.5%，净 delta 敞口 119k shares
Top ΔOI: P 255 +5,619 ｜ P 247 +4,714 ｜ P 250 +4,621
仓位参考: Max Pain 269 ｜ Call Wall 271（+2.6%）（OI 2.5k） ｜ Put Wall 255（-3.4%，弱）（OI 7.2k）
量化解读： 存量 Put 重｜ATM IV 33.5%｜历史 Rank 97%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 118,905 股

📆 11-25 Forward Structure
存量OI: C 23.8k / P 38.6k，今日变化ΔOI: C +6.6k / P +2.7k，平值价格ATM: C $2.77 / P $2.57 ｜ ATM IV 31.8%，净 delta 敞口 362k shares
Top ΔOI: P 257 +2,255 ｜ C 267 +1,417 ｜ P 255 +1,079
仓位参考: Max Pain 267 ｜ Call Wall 277（+4.9%，弱）（OI 4.3k） ｜ Put Wall 261（-1.2%，弱）（OI 6.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.8%｜历史 Rank 97%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 361,812 股

📆 11-27 Forward Structure
存量OI: C 96.6k / P 242.8k，今日变化ΔOI: C +17.6k / P +39.2k，平值价格ATM: C $3.19 / P $2.84 ｜ ATM IV 26.8%，净 delta 敞口 477k shares
Top ΔOI: P 250 +11,115 ｜ P 255 +9,320 ｜ C 263 +3,866
仓位参考: Max Pain 275 ｜ Call Wall 275（+4.1%，弱）（OI 6.8k） ｜ Put Wall 270（+2.3%，弱）（OI 35.0k）
量化解读： 存量 Put 重｜ATM IV 26.8%｜历史 Rank 97%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 477,407 股

📆 11-30 Forward Structure
存量OI: C 16.3k / P 54.9k，今日变化ΔOI: C +2.4k / P +25.4k，平值价格ATM: C $3.81 / P $3.81 ｜ ATM IV 24.4%，净 delta 敞口 -99k shares
Top ΔOI: P 250 +6,681 ｜ P 255 +6,381 ｜ P 235 +3,841
仓位参考: Max Pain 269 ｜ Call Wall 276（+4.5%，弱）（OI 3.9k） ｜ Put Wall 255（-3.4%，弱）（OI 10.2k）
量化解读： 存量 Put 重｜ATM IV 24.4%｜历史 Rank 97%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 负 99,056 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/IWM_morning.json