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
🔴 **事件差分**: 11-06（1D）ATM IV 102.3% vs 11-13 77.4%（差 +24.8pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 144C ΔOI +747（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 151.50 → 今开 149.00（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 151.58 ｜ 低 138.69

Options: P/C成交量 1.63 | OI比 0.72 | ATM IV 102.3% | Skew 6.9pp | Term 0.67 | ExpMove ±5.0%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价显著（Skew 6.9pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.72）+ 当日成交偏 Put（P/C量 1.63）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.63×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±5.0% ｜ 11-13（8D）±9.4% ｜ 11-20（15D）±11.7% ｜ 11-27（22D）±16.2%
   ⇒ IV–VIX Spread: +81.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,081,901 | GEX Change vs 上次快照 -8,526,188 | Flip: Primary Flip: 135.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 414 / LOW 173 / INVALID 263
结构观察区: Primary Flip 135.25（全链重定价，覆盖 100%）
最近结构参考: Flip 135（现价高于该位 4.3%）
量化视角： 正 Gamma（1908万，无历史分位）｜正 Gamma 减弱（853万）｜现价位于 Flip 上方 4.26%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 142（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 135（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 75.0P — Vol 1,858 | 最新价 $0.03 | OI 16→1859 (ΔOI +1843张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1843张（+11518.8% vs前日OI），连续性待观察（方向未知）
11-27 85.0P — Vol 1,811 | 最新价 $0.21 | OI 14→1450 (ΔOI +1436张) | ΔOI/Volume 79.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1436张（+10257.1% vs前日OI），连续性待观察（方向未知）
11-20 120.0P — Vol 1,714 | 最新价 $0.66 | OI 4614→5941 (ΔOI +1327张) | ΔOI/Volume 77.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1327张（+28.8% vs前日OI），连续性待观察（方向未知）
11-06 160.0C — Vol 4,025 | 最新价 $0.99 | OI 2414→3423 (ΔOI +1009张) | ΔOI/Volume 25.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1009张（+41.8% vs前日OI），连续性待观察（方向未知）
11-20 90.0P — Vol 1,099 | 最新价 $0.13 | OI 2923→3824 (ΔOI +901张) | ΔOI/Volume 82.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增901张（+30.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,516 张（Put 5,507 / Call 1,009），跨 4 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +2.4k / P -0.3k ｜ Activity HIGH ｜ 1D
11-13  C +1.3k / P +4.9k ｜ Activity HIGH ｜ 8D
11-20  C +0.5k / P +3.5k ｜ Activity HIGH ｜ 15D
11-27  C +0.1k / P +2.5k ｜ Activity HIGH ｜ 22D

📆 11-06 Forward Structure
存量OI: C 75.2k / P 53.9k，今日变化ΔOI: C +2.4k / P -0.3k，平值价格ATM: C $3.65 / P $3.40 ｜ ATM IV 102.3%，净 delta 敞口 -52k shares
Top ΔOI: C 144 +747
仓位参考: Max Pain 142 ｜ Call Wall 148（+5.0%，弱）（OI 8.5k） ｜ Put Wall 130（-7.8%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 102.3%｜历史 Rank 87%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 52,274 股

📆 11-13 Forward Structure
存量OI: C 14.5k / P 24.4k，今日变化ΔOI: C +1.3k / P +4.9k，平值价格ATM: C $6.50 / P $6.74 ｜ ATM IV 77.4%，净 delta 敞口 -61k shares
Top ΔOI: P 146 +406
仓位参考: Max Pain 155 ｜ Call Wall 150（+6.4%，弱）（OI 0.7k） ｜ Put Wall 155（+9.9%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 77.4%｜历史 Rank 87%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 61,115 股

📆 11-20 Forward Structure
存量OI: C 73.7k / P 60.8k，今日变化ΔOI: C +0.5k / P +3.5k，平值价格ATM: C $8.90 / P $7.55 ｜ ATM IV 74.4%，净 delta 敞口 -7k shares
Top ΔOI: P 120 +1,327
仓位参考: Max Pain 170 ｜ Put Wall 140（-0.7%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.4%｜历史 Rank 87%（近端代理）｜IV/RV 1.12×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 7,012 股

📆 11-27 Forward Structure
存量OI: C 3.7k / P 7.7k，今日变化ΔOI: C +0.1k / P +2.5k，平值价格ATM: C $17.50 / P $5.37 ｜ ATM IV 70.0%，净 delta 敞口 -3k shares
仓位参考: Max Pain 160 ｜ Call Wall 155（+9.9%，弱）（OI 0.2k） ｜ Put Wall 140（-0.7%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 70.0%｜历史 Rank 87%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 2,645 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 102.3% vs 11-13 77.4%（差 +24.8pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/COIN_morning.json