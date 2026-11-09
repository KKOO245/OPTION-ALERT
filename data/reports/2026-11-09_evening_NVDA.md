# 期权晚报 2026-11-09（快照 16:40 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
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
🟡 **近现价集中开仓**: 11-11 180P ΔOI +2,077（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 173.04 → 收盘 178.67（+3.3%） ｜ 今日高 179.91 ｜ 低 170.24 ｜ 昨收 186.64 → 收盘 178.67（-4.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-16，窗口结束前不做对错判定）

Options: P/C成交量 0.95 | OI比 0.90 | ATM IV 63.4% | Skew 5.8pp | Term 0.90 | ExpMove ±4.4%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜保护溢价中性（Skew 5.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-11（2D）±4.4% ｜ 11-13（4D）±5.6% ｜ 11-16（7D）±6.4% ｜ 11-18（9D）±9.7%
   ⇒ IV–VIX Spread: +43.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -91,464,073 | GEX Change vs 上次快照 3,552,932 | Flip: Primary Flip: 185.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1087 / LOW 227 / INVALID 760
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 185.76（全链重定价，覆盖 97%）
最近结构参考: Flip 186（现价低于该位 3.8%）
量化视角： 负 Gamma（9146万，无历史分位）｜负 Gamma 缓解（+355万）｜现价位于 Flip 下方 3.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 190（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 186（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 200.0C — Vol 50,313 | 最新价 $0.29 | OI 8773→40207 (ΔOI +31434张) | ΔOI/Volume 62.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31434张（+358.3% vs前日OI），连续性待观察（方向未知）
11-13 207.5C — Vol 6,000 | 最新价 $0.13 | OI 3800→33407 (ΔOI +29607张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29607张（+779.1% vs前日OI），连续性待观察（方向未知）
11-13 80.0P — Vol 618 | 最新价 $0.01 | OI 788→24257 (ΔOI +23469张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23469张（+2978.3% vs前日OI），连续性待观察（方向未知）
11-13 95.0P — Vol 1,119 | 最新价 $0.01 | OI 2461→23208 (ΔOI +20747张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20747张（+843.0% vs前日OI），连续性待观察（方向未知）
11-13 195.0C — Vol 21,873 | 最新价 $0.54 | OI 10137→27057 (ΔOI +16920张) | ΔOI/Volume 77.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16920张（+166.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 122,177 张（Put 44,216 / Call 77,961），跨 1 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-11  C +10.8k / P +7.5k ｜ Activity HIGH ｜ 2D
11-13  C +133.3k / P +102.2k ｜ Activity HIGH ｜ 4D
11-16  C +6.8k / P +4.3k ｜ Activity HIGH ｜ 7D
11-18  C +10.6k / P +6.2k ｜ Activity HIGH ｜ 9D

📆 11-11 Forward Structure
存量OI: C 51.1k / P 48.2k，今日变化ΔOI: C +10.8k / P +7.5k，平值价格ATM: C $4.57 / P $3.35 ｜ ATM IV 74.3%，净 delta 敞口 -242k shares
Top ΔOI: P 180 +2,077
仓位参考: Max Pain 192 ｜ Call Wall 195（+9.1%，弱）（OI 4.6k） ｜ Put Wall 170（-4.9%，弱）（OI 4.3k）
量化解读： 存量两侧均衡｜ATM IV 74.3%｜历史 Rank 87%（近端代理）｜IV/RV 1.51×（近似）｜净 delta 敞口 负 242,318 股

📆 11-13 Forward Structure
存量OI: C 391.3k / P 317.6k，今日变化ΔOI: C +133.3k / P +102.2k，平值价格ATM: C $5.55 / P $4.50 ｜ ATM IV 67.4%，净 delta 敞口 8k shares
Top ΔOI: C 200 +31,434 ｜ C 207 +29,607
仓位参考: Max Pain 195 ｜ Call Wall 195（+9.1%，弱）（OI 27.1k） ｜ Put Wall 165（-7.7%，弱）（OI 19.3k）
量化解读： 存量 Call 重｜ATM IV 67.4%｜历史 Rank 87%（近端代理）｜IV/RV 1.37×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 7,572 股

📆 11-16 Forward Structure
存量OI: C 26.5k / P 12.7k，今日变化ΔOI: C +6.8k / P +4.3k，平值价格ATM: C $6.40 / P $5.05 ｜ ATM IV 57.3%，净 delta 敞口 -176k shares
Top ΔOI: C 200 +1,445 ｜ P 180 +1,243
仓位参考: Max Pain 192 ｜ Put Wall 180（+0.7%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 57.3%｜历史 Rank 87%（近端代理）｜IV/RV 1.17×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 176,115 股

📆 11-18 Forward Structure
存量OI: C 27.2k / P 14.2k，今日变化ΔOI: C +10.6k / P +6.2k，平值价格ATM: C $9.37 / P $7.95 ｜ ATM IV 77.1%，净 delta 敞口 -91k shares
Top ΔOI: C 210 +3,375 ｜ P 160 +2,087 ｜ C 190 +1,517
仓位参考: Max Pain 190 ｜ Call Wall 190（+6.3%，弱）（OI 2.0k） ｜ Put Wall 192.5（+7.7%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 77.1%｜历史 Rank 87%（近端代理）｜IV/RV 1.57×（近似）｜净 delta 敞口 负 90,755 股

📅 事件差分（观察，非因果）: 11-11（2D）ATM IV 74.3% vs 11-13 67.4%（差 +6.9pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate MoM、Inflation Rate YoY
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/NVDA_evening.json