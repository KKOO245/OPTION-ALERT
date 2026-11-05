# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $732.06 ｜ QQQ $647.05
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **事件差分**: 11-06 ATM IV 31.4% vs 11-09 21.3%（差 +10.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 290C ΔOI +15,289（距现价 +3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
IWM  昨收 284.02 → 今开 283.75（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 284.70 ｜ 低 278.66

Options: P/C成交量 2.19 | OI比 0.87 | ATM IV 38.3% | Skew 1.5pp | Term 0.52 | ExpMove ±1.5%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜当日成交偏 Put（P/C量 2.19）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.19×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.87×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（1D）±1.5% ｜ 11-09（4D）±1.8% ｜ 11-10（5D）±2.2% ｜ 11-11（6D）±2.4%
   ⇒ IV–VIX Spread: +17.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -548,527,095 | GEX Change vs 上次快照 -525,519,555 | Flip: Primary Flip: 285.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1298 / LOW 137 / INVALID 1077
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 285.00（全链重定价，覆盖 98%）
Put Wall 270（弱结构｜现价高于该位 3.8%） | Call Wall 290（弱结构｜现价低于该位 3.3%）
最近结构参考: Flip 285（现价低于该位 1.6%）
量化视角： 负 Gamma（5.49亿，无历史分位）｜负 Gamma 加深（5.26亿）｜现价位于 Flip 下方 1.64%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 283（MaxPain，仅结算参考） / 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 285（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 270.0P — Vol 97,071 | 最新价 $0.81 | OI 165296→201852 (ΔOI +36556张) | ΔOI/Volume 37.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增36556张（+22.1% vs前日OI），连续性待观察（方向未知）
11-06 290.0C — Vol 35,533 | 最新价 $0.15 | OI 10028→25317 (ΔOI +15289张) | ΔOI/Volume 43.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15289张（+152.5% vs前日OI），连续性待观察（方向未知）
11-20 271.0P — Vol 56,804 | 最新价 $0.91 | OI 36892→50468 (ΔOI +13576张) | ΔOI/Volume 23.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13576张（+36.8% vs前日OI），连续性待观察（方向未知）
11-20 272.0P — Vol 64,969 | 最新价 $1.05 | OI 6791→20009 (ΔOI +13218张) | ΔOI/Volume 20.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13218张（+194.6% vs前日OI），连续性待观察（方向未知）
11-20 277.0P — Vol 14,872 | 最新价 $1.88 | OI 35280→45789 (ΔOI +10509张) | ΔOI/Volume 70.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10509张（+29.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 89,148 张（Put 73,859 / Call 15,289），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 43.6k / P 37.9k，今日成交量: C 72.0k / P 158.0k，平值价格ATM: C $1.10 / P $1.23 ｜ ATM IV 38.3%，预期波动 ±0.8%，Max Pain 283
Top ΔOI: P 284 +4,016 ｜ C 284 +3,960 ｜ C 290 +3,919

📆 Forward Expiration Structure

11-06  C +35.2k / P +2.7k ｜ Activity HIGH ｜ 1D
11-09  C +4.5k / P +12.5k ｜ Activity HIGH ｜ 4D
11-10  C +13.6k / P +9.9k ｜ Activity HIGH ｜ 5D
11-11  C +2.8k / P +4.7k ｜ Activity HIGH ｜ 6D

📆 11-06 Forward Structure
存量OI: C 167.9k / P 298.8k，今日变化ΔOI: C +35.2k / P +2.7k，平值价格ATM: C $2.07 / P $2.10 ｜ ATM IV 31.4%，净 delta 敞口 -190k shares
Top ΔOI: C 290 +15,289 ｜ C 288 +5,819 ｜ C 287 +3,241
仓位参考: Max Pain 280 ｜ Call Wall 290（+3.4%）（OI 25.3k） ｜ Put Wall 277（-1.2%，弱）（OI 30.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.4%｜历史 Rank 91%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 189,829 股

📆 11-09 Forward Structure
存量OI: C 23.4k / P 35.9k，今日变化ΔOI: C +4.5k / P +12.5k，平值价格ATM: C $2.62 / P $2.55 ｜ ATM IV 21.3%，净 delta 敞口 -710k shares
Top ΔOI: P 283 +10,229 ｜ P 266 +1,011 ｜ C 293 +677
仓位参考: Max Pain 283 ｜ Call Wall 285（+1.7%）（OI 7.6k） ｜ Put Wall 283（+0.9%）（OI 10.5k）
量化解读： 存量 Put 重｜ATM IV 21.3%｜历史 Rank 91%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 负 710,155 股

📆 11-10 Forward Structure
存量OI: C 19.4k / P 20.1k，今日变化ΔOI: C +13.6k / P +9.9k，平值价格ATM: C $3.26 / P $2.81 ｜ ATM IV 22.4%，净 delta 敞口 -239k shares
Top ΔOI: C 292 +3,987 ｜ C 290 +3,758 ｜ P 282 +1,945
仓位参考: Max Pain 282 ｜ Call Wall 290（+3.4%，弱）（OI 4.2k） ｜ Put Wall 280（-0.1%）（OI 3.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 22.4%｜历史 Rank 91%（近端代理）｜净 delta 敞口 负 239,264 股

📆 11-11 Forward Structure
存量OI: C 10.1k / P 12.4k，今日变化ΔOI: C +2.8k / P +4.7k，平值价格ATM: C $3.63 / P $3.22 ｜ ATM IV 22.6%，净 delta 敞口 -152k shares
Top ΔOI: P 277 +2,332 ｜ C 298 +903 ｜ P 282 +521
仓位参考: Max Pain 282 ｜ Call Wall 286（+2.0%）（OI 3.1k） ｜ Put Wall 277（-1.2%）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 22.6%｜历史 Rank 91%（近端代理）｜净 delta 敞口 负 152,426 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 31.4% vs 11-09 21.3%（差 +10.1pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/IWM_morning.json