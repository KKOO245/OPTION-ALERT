# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.96 ｜ QQQ $691.95
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-05 290C ΔOI +13,353（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-05 290C ΔOI +13,353 占该期限总 OI 25.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 279.79 → 今开 284.17（+1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 286.17 ｜ 低 282.86

Options: P/C成交量 1.07 | OI比 1.43 | ATM IV 30.0% | Skew 3.3pp | Term 0.62 | ExpMove ±1.1%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.07×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.43×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-05（1D）±1.1% ｜ 11-06（2D）±1.5% ｜ 11-09（5D）±1.8% ｜ 11-10（6D）±2.2%
   ⇒ IV–VIX Spread: +13.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -134,036,327 | GEX Change vs 上次快照 385,980,608 | Flip: Primary Flip: 284.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1313 / LOW 128 / INVALID 1025
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 284.63（全链重定价，覆盖 99%）
Put Wall 270（弱结构｜现价高于该位 5.0%） | Call Wall 285（弱结构｜现价低于该位 0.6%）
最近结构参考: Flip 285（现价低于该位 0.4%）
量化视角： 负 Gamma（1.34亿，无历史分位）｜负 Gamma 缓解（+3.86亿）｜现价位于 Flip 下方 0.42%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 280（MaxPain，仅结算参考）；上方 285（Call Wall，弱结构）。
• Gamma 区域：切换参考 285（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-05 290.0C — Vol 16,645 | 最新价 $0.12 | OI 983→14336 (ΔOI +13353张) | ΔOI/Volume 80.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13353张（+1358.4% vs前日OI），连续性待观察（方向未知）
11-20 266.0P — Vol 30,960 | 最新价 $1.72 | OI 75041→84913 (ΔOI +9872张) | ΔOI/Volume 31.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9872张（+13.2% vs前日OI），连续性待观察（方向未知）
11-06 247.5P — Vol 7,012 | 最新价 $0.05 | OI 27→7028 (ΔOI +7001张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7001张（+25929.6% vs前日OI），连续性待观察（方向未知）
11-06 245.0P — Vol 6,759 | 最新价 $0.03 | OI 2460→8792 (ΔOI +6332张) | ΔOI/Volume 93.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6332张（+257.4% vs前日OI），连续性待观察（方向未知）
11-04 276.0P — Vol 8,438 | 最新价 $0.85 | OI 979→6905 (ΔOI +5926张) | ΔOI/Volume 70.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5926张（+605.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 42,484 张（Put 29,131 / Call 13,353），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 48.8k / P 69.7k，今日成交量: C 88.6k / P 94.9k，平值价格ATM: C $1.18 / P $0.69 ｜ ATM IV 30.0%，预期波动 ±0.7%，Max Pain 280
Top ΔOI: P 276 +5,926 ｜ C 288 -5,144 ｜ C 287 -3,531

📆 Forward Expiration Structure

11-05  C +20.5k / P +1.7k ｜ Activity HIGH ｜ 1D
11-06  C +14.3k / P +21.6k ｜ Activity HIGH ｜ 2D
11-09  C +5.9k / P +6.1k ｜ Activity HIGH ｜ 5D
11-10  C +1.8k / P +3.8k ｜ Activity HIGH ｜ 6D

📆 11-05 Forward Structure
存量OI: C 31.2k / P 20.5k，今日变化ΔOI: C +20.5k / P +1.7k，平值价格ATM: C $1.83 / P $1.29 ｜ ATM IV 22.8%，净 delta 敞口 222k shares
Top ΔOI: C 290 +13,353 ｜ C 286 +5,208 ｜ P 282 +688
仓位参考: Max Pain 280 ｜ Call Wall 290（+2.3%）（OI 14.3k） ｜ Put Wall 282（-0.5%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 22.8%｜历史 Rank 77%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 222,498 股

📆 11-06 Forward Structure
存量OI: C 132.7k / P 296.2k，今日变化ΔOI: C +14.3k / P +21.6k，平值价格ATM: C $2.42 / P $1.90 ｜ ATM IV 24.2%，净 delta 敞口 111k shares
Top ΔOI: P 275 +5,128
仓位参考: Max Pain 280 ｜ Call Wall 285（+0.6%，弱）（OI 13.4k） ｜ Put Wall 277（-2.3%，弱）（OI 33.0k）
量化解读： 存量 Put 重｜ATM IV 24.2%｜历史 Rank 77%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 110,636 股

📆 11-09 Forward Structure
存量OI: C 18.9k / P 23.4k，今日变化ΔOI: C +5.9k / P +6.1k，平值价格ATM: C $2.80 / P $2.29 ｜ ATM IV 18.7%，净 delta 敞口 31k shares
Top ΔOI: P 265 +2,295 ｜ P 275 +1,452 ｜ C 292 +1,303
仓位参考: Max Pain 280 ｜ Call Wall 285（+0.6%）（OI 7.1k） ｜ Put Wall 275（-3.0%，弱）（OI 4.5k）
量化解读： 存量 Put 重｜ATM IV 18.7%｜历史 Rank 77%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 31,393 股

📆 11-10 Forward Structure
存量OI: C 5.9k / P 10.2k，今日变化ΔOI: C +1.8k / P +3.8k，平值价格ATM: C $3.61 / P $2.74 ｜ ATM IV 19.9%，净 delta 敞口 -7k shares
Top ΔOI: P 277 +555 ｜ P 265 +436 ｜ P 275 +434
仓位参考: Max Pain 281 ｜ Call Wall 287（+1.3%，弱）（OI 0.9k） ｜ Put Wall 280（-1.2%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 19.9%｜历史 Rank 77%（近端代理）｜净 delta 敞口 负 6,737 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/IWM_morning.json