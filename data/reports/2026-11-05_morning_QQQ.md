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
🟡 **事件差分**: 11-06 ATM IV 45.4% vs 11-09 31.2%（差 +14.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 691P ΔOI +14,339（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 691.95 → 今开 683.17（-1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 683.64 ｜ 低 660.85

Options: P/C成交量 1.15 | OI比 1.12 | ATM IV 57.8% | Skew 1.1pp | Term 0.48 | ExpMove ±2.1%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.48，近月 IV 高于远月）｜保护溢价薄（Skew 1.1pp）｜当日成交偏 Put（P/C量 1.15）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.15×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 9% ｜ P/C OI(近端) 11%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 9%）｜近端持仓结构中性（P/C OI 分位 11%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-06（1D）±2.1% ｜ 11-09（4D）±2.8% ｜ 11-10（5D）±3.2% ｜ 11-11（6D）±3.4%
   ⇒ IV–VIX Spread: +36.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -878,368,146 | GEX Change vs 上次快照 -162,062,241 | Flip: Primary Flip: 700.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 2856 / LOW 204 / INVALID 1506
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 700.32（全链重定价，覆盖 93%）
Put Wall 680（弱结构｜现价低于该位 2.1%）
最近结构参考: Put Wall 680（现价低于该位 2.1%）
量化视角： 负 Gamma（8.78亿，历史分位偏负区，比 91% 的交易日更负）｜负 Gamma 加深（1.62亿）｜现价位于 Flip 下方 4.93%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 680（Put Wall，弱结构） / 694（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 700（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 705.0C — Vol 41,427 | 最新价 $1.30 | OI 6697→29663 (ΔOI +22966张) | ΔOI/Volume 55.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22966张（+342.9% vs前日OI），连续性待观察（方向未知）
11-06 691.0P — Vol 20,246 | 最新价 $4.58 | OI 17527→31866 (ΔOI +14339张) | ΔOI/Volume 70.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14339张（+81.8% vs前日OI），连续性待观察（方向未知）
11-20 710.0C — Vol 19,634 | 最新价 $6.15 | OI 18911→28792 (ΔOI +9881张) | ΔOI/Volume 50.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9881张（+52.2% vs前日OI），连续性待观察（方向未知）
11-05 700.0C — Vol 72,779 | 最新价 $1.07 | OI 4128→13596 (ΔOI +9468张) | ΔOI/Volume 13.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9468张（+229.4% vs前日OI），连续性待观察（方向未知）
11-09 635.0P — Vol 9,170 | 最新价 $0.08 | OI 902→9441 (ΔOI +8539张) | ΔOI/Volume 93.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8539张（+946.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 65,193 张（Put 22,878 / Call 42,315），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $7M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 120.7k / P 135.6k，今日成交量: C 644.9k / P 744.1k，平值价格ATM: C $3.80 / P $4.52 ｜ ATM IV 57.8%，预期波动 ±1.3%，Max Pain 694
Top ΔOI: C 700 +9,468 ｜ P 693 +4,966 ｜ C 705 +4,934

📆 Forward Expiration Structure

11-06  C +53.3k / P +15.7k ｜ Activity HIGH ｜ 1D
11-09  C +13.5k / P +44.5k ｜ Activity HIGH ｜ 4D
11-10  C +5.8k / P +5.3k ｜ Activity HIGH ｜ 5D
11-11  C +6.1k / P +8.3k ｜ Activity HIGH ｜ 6D

📆 11-06 Forward Structure
存量OI: C 468.0k / P 619.0k，今日变化ΔOI: C +53.3k / P +15.7k，平值价格ATM: C $6.82 / P $7.40 ｜ ATM IV 45.4%，净 delta 敞口 413k shares
Top ΔOI: C 705 +22,966 ｜ P 691 +14,339 ｜ C 713 +8,490
仓位参考: Max Pain 710 ｜ Put Wall 675（+1.4%，弱）（OI 48.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.4%｜历史 Rank 100%（近端代理）｜IV/RV 2.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 413,181 股

📆 11-09 Forward Structure
存量OI: C 41.3k / P 87.5k，今日变化ΔOI: C +13.5k / P +44.5k，平值价格ATM: C $8.97 / P $9.44 ｜ ATM IV 31.2%，净 delta 敞口 -630k shares
Top ΔOI: P 635 +8,539 ｜ C 700 +5,713
仓位参考: Max Pain 695 ｜ Put Wall 685（+2.9%，弱）（OI 6.6k）
量化解读： 存量 Put 重｜ATM IV 31.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 负 630,302 股

📆 11-10 Forward Structure
存量OI: C 40.2k / P 20.3k，今日变化ΔOI: C +5.8k / P +5.3k，平值价格ATM: C $10.61 / P $10.44 ｜ ATM IV 32.4%，净 delta 敞口 -211k shares
Top ΔOI: C 708 +752 ｜ P 635 -530
仓位参考: Max Pain 695 ｜ Put Wall 671（+0.8%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 32.4%｜历史 Rank 100%（近端代理）｜IV/RV 1.42×（近似）｜净 delta 敞口 负 210,633 股

📆 11-11 Forward Structure
存量OI: C 21.9k / P 17.4k，今日变化ΔOI: C +6.1k / P +8.3k，平值价格ATM: C $11.55 / P $11.30 ｜ ATM IV 32.6%，净 delta 敞口 -395k shares
Top ΔOI: C 715 +1,230 ｜ P 674 +787
仓位参考: Max Pain 695 ｜ Put Wall 676（+1.5%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 负 395,217 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 45.4% vs 11-09 31.2%（差 +14.2pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/QQQ_morning.json