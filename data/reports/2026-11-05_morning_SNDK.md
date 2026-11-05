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
🔴 **事件差分**: 11-06（1D）ATM IV 149.1% vs 11-13 107.7%（差 +41.4pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 900P ΔOI +706（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,037.40 → 今开 962.25（-7.2%） | 较昨收变动（含盘初走势） ｜ 今日高 967.99 ｜ 低 854.38

Options: P/C成交量 1.37 | OI比 0.62 | ATM IV 149.1% | Skew 12.0pp | Term 0.61 | ExpMove ±7.2%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜保护溢价显著（Skew 12.0pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.62）+ 当日成交偏 Put（P/C量 1.37）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.37×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±7.2% ｜ 11-13（8D）±13.2% ｜ 11-20（15D）±16.7% ｜ 11-27（22D）±18.4%
   ⇒ IV–VIX Spread: +128.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,845,159 | GEX Change vs 上次快照 -713,130 | Flip: Primary Flip: 1017.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1573 / LOW 609 / INVALID 1206
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1017.21（全链重定价，覆盖 100%）
最近结构参考: Flip 1017（现价低于该位 12.0%）
量化视角： 负 Gamma（685万，无历史分位）｜负 Gamma 加深（71万）｜现价位于 Flip 下方 11.99%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,120（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1017（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 1150.0C — Vol 3,944 | 最新价 $4.30 | OI 585→1851 (ΔOI +1266张) | ΔOI/Volume 32.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1266张（+216.4% vs前日OI），连续性待观察（方向未知）
11-20 800.0P — Vol 1,625 | 最新价 $9.73 | OI 481→1650 (ΔOI +1169张) | ΔOI/Volume 71.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1169张（+243.0% vs前日OI），连续性待观察（方向未知）
11-06 1130.0C — Vol 1,409 | 最新价 $6.20 | OI 333→1156 (ΔOI +823张) | ΔOI/Volume 58.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增823张（+247.2% vs前日OI），连续性待观察（方向未知）
11-13 820.0P — Vol 852 | 最新价 $5.34 | OI 109→837 (ΔOI +728张) | ΔOI/Volume 85.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增728张（+667.9% vs前日OI），连续性待观察（方向未知）
11-06 900.0P — Vol 2,933 | 最新价 $1.41 | OI 1511→2217 (ΔOI +706张) | ΔOI/Volume 24.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增706张（+46.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,692 张（Put 2,603 / Call 2,089），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +7.7k / P +1.2k ｜ Activity HIGH ｜ 1D
11-13  C +3.7k / P +2.1k ｜ Activity HIGH ｜ 8D
11-20  C +3.4k / P -1.5k ｜ Activity HIGH ｜ 15D
11-27  C +0.6k / P +0.3k ｜ Activity HIGH ｜ 22D

📆 11-06 Forward Structure
存量OI: C 52.2k / P 32.1k，今日变化ΔOI: C +7.7k / P +1.2k，平值价格ATM: C $28.70 / P $35.27 ｜ ATM IV 149.1%，净 delta 敞口 165k shares
Top ΔOI: P 900 +706
仓位参考: Max Pain 1,120 ｜ Put Wall 900（+0.5%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 149.1%｜历史 Rank 91%（近端代理）｜IV/RV 1.70×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 164,893 股

📆 11-13 Forward Structure
存量OI: C 19.3k / P 11.8k，今日变化ΔOI: C +3.7k / P +2.1k，平值价格ATM: C $60.35 / P $57.60 ｜ ATM IV 107.7%，净 delta 敞口 -20k shares
Top ΔOI: P 820 +728 ｜ C 1300 +447
仓位参考: Max Pain 1,185 ｜ Put Wall 820（-8.4%）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 107.7%｜历史 Rank 91%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 19,658 股

📆 11-20 Forward Structure
存量OI: C 57.4k / P 53.2k，今日变化ΔOI: C +3.4k / P -1.5k，平值价格ATM: C $73.50 / P $76.00 ｜ ATM IV 102.3%，净 delta 敞口 394k shares
Top ΔOI: P 1780 -1,234 ｜ P 800 +1,169 ｜ P 1800 -890
仓位参考: Max Pain 1,300 ｜ Put Wall 950（+6.1%，弱）（OI 1.7k）
量化解读： 存量两侧均衡｜ATM IV 102.3%｜历史 Rank 91%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 393,908 股

📆 11-27 Forward Structure
存量OI: C 13.8k / P 8.4k，今日变化ΔOI: C +0.6k / P +0.3k，平值价格ATM: C $81.93 / P $82.90 ｜ ATM IV 95.9%，净 delta 敞口 7k shares
Top ΔOI: P 1200 -98 ｜ P 870 +87
仓位参考: Max Pain 1,270
量化解读： 存量 Call 重｜ATM IV 95.9%｜历史 Rank 91%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 7,057 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 149.1% vs 11-13 107.7%（差 +41.4pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/SNDK_morning.json