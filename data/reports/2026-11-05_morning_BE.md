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
🔴 **事件差分**: 11-06（1D）ATM IV 167.1% vs 11-13 121.9%（差 +45.2pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 167C ΔOI -1,050（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 200.40 → 今开 188.00（-6.2%） | 较昨收变动（含盘初走势） ｜ 今日高 188.80 ｜ 低 164.03

Options: P/C成交量 0.66 | OI比 0.62 | ATM IV 167.1% | Skew 13.7pp | Term 0.59 | ExpMove ±7.8%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜保护溢价显著（Skew 13.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±7.8% ｜ 11-13（8D）±14.7% ｜ 11-20（15D）±18.7% ｜ 11-27（22D）±20.3%
   ⇒ IV–VIX Spread: +146.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,823,126 | GEX Change vs 上次快照 -2,316,098 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 514 / LOW 127 / INVALID 257
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
量化视角： 负 Gamma（982万，无历史分位）｜负 Gamma 加深（232万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 210（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 210.0C — Vol 3,977 | 最新价 $3.43 | OI 836→1876 (ΔOI +1040张) | ΔOI/Volume 26.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1040张（+124.4% vs前日OI），连续性待观察（方向未知）
11-06 220.0C — Vol 4,013 | 最新价 $1.38 | OI 1946→2922 (ΔOI +976张) | ΔOI/Volume 24.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增976张（+50.1% vs前日OI），连续性待观察（方向未知）
11-06 200.0C — Vol 4,288 | 最新价 $7.44 | OI 1513→2267 (ΔOI +754张) | ΔOI/Volume 17.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增754张（+49.8% vs前日OI），连续性待观察（方向未知）
11-20 220.0C — Vol 2,042 | 最新价 $8.77 | OI 2585→3170 (ΔOI +585张) | ΔOI/Volume 28.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增585张（+22.6% vs前日OI），连续性待观察（方向未知）
11-20 300.0C — Vol 1,149 | 最新价 $0.39 | OI 4716→5227 (ΔOI +511张) | ΔOI/Volume 44.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增511张（+10.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,866 张（Put 0 / Call 3,866），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +5.5k / P +0.4k ｜ Activity HIGH ｜ 1D
11-13  C +1.7k / P +1.8k ｜ Activity HIGH ｜ 8D
11-20  C +2.2k / P -41 ｜ Activity HIGH ｜ 15D
11-27  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 11-06 Forward Structure
存量OI: C 54.7k / P 33.7k，今日变化ΔOI: C +5.5k / P +0.4k，平值价格ATM: C $6.70 / P $6.45 ｜ ATM IV 167.1%，净 delta 敞口 -31k shares
Top ΔOI: C 167 -1,050
仓位参考: Max Pain 210 ｜ Call Wall 175（+3.2%，弱）（OI 1.4k） ｜ Put Wall 180（+6.1%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 167.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.76×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 31,193 股

📆 11-13 Forward Structure
存量OI: C 15.0k / P 14.3k，今日变化ΔOI: C +1.7k / P +1.8k，平值价格ATM: C $13.35 / P $11.54 ｜ ATM IV 121.9%，净 delta 敞口 -61k shares
Top ΔOI: C 195 +338 ｜ P 155 +260
仓位参考: Max Pain 228 ｜ Put Wall 160（-5.7%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 121.9%｜历史 Rank 94%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 61,347 股

📆 11-20 Forward Structure
存量OI: C 65.3k / P 75.4k，今日变化ΔOI: C +2.2k / P -41，平值价格ATM: C $16.20 / P $15.55 ｜ ATM IV 111.6%，净 delta 敞口 86k shares
Top ΔOI: P 205 -1,050 ｜ C 220 +585
仓位参考: Max Pain 228 ｜ Call Wall 180（+6.1%，弱）（OI 1.2k） ｜ Put Wall 170（+0.2%，弱）（OI 4.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 111.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 86,256 股

11-27（MEDIUM △）Top ΔOI: 200P +132 ｜ 210P +101
11-27（MEDIUM △）仓位参考: Max Pain 225

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 167.1% vs 11-13 121.9%（差 +45.2pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/BE_morning.json