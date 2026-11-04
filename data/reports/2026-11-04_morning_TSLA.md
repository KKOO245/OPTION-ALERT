# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.05 ｜ QQQ $697.41
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.0（fear）
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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 11-06 ATM IV 58.0% vs 11-09 45.1%（差 +12.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 385P ΔOI +1,243（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 398.50 → 今开 379.80（-4.7%） | 较昨收变动（含盘初走势） ｜ 今日高 389.65 ｜ 低 375.50

Options: P/C成交量 0.63 | OI比 1.18 | ATM IV 75.4% | Skew 5.4pp | Term 0.57 | ExpMove ±3.7%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜保护溢价中性（Skew 5.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.18×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（2D）±3.7% ｜ 11-09（5D）±4.3% ｜ 11-11（7D）±5.3% ｜ 11-13（9D）±6.0%
   ⇒ IV–VIX Spread: +58.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,384,907 | GEX Change vs 上次快照 -63,174,469 | Flip: Primary Flip: 386.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1379 / LOW 153 / INVALID 822
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 386.73（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价低于该位 3.8%）
最近结构参考: Flip 387（现价低于该位 0.5%）
量化视角： 负 Gamma（1038万，无历史分位）｜由正转负（6317万）｜现价位于 Flip 下方 0.50%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 400（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 387（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-04 300.0P — Vol 4,400 | 最新价 $0.01 | OI 2475→6634 (ΔOI +4159张) | ΔOI/Volume 94.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4159张（+168.0% vs前日OI），连续性待观察（方向未知）
11-04 402.5C — Vol 23,982 | 最新价 $3.70 | OI 1800→5692 (ΔOI +3892张) | ΔOI/Volume 16.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3892张（+216.2% vs前日OI），连续性待观察（方向未知）
11-06 470.0C — Vol 4,256 | 最新价 $0.04 | OI 1240→4750 (ΔOI +3510张) | ΔOI/Volume 82.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3510张（+283.1% vs前日OI），连续性待观察（方向未知）
11-04 380.0P — Vol 16,733 | 最新价 $0.83 | OI 2106→5244 (ΔOI +3138张) | ΔOI/Volume 18.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3138张（+149.0% vs前日OI），连续性待观察（方向未知）
11-04 410.0C — Vol 34,058 | 最新价 $1.49 | OI 2162→4481 (ΔOI +2319张) | ΔOI/Volume 6.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2319张（+107.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 17,018 张（Put 7,297 / Call 9,721），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 72.8k / P 86.0k，今日成交量: C 198.8k / P 125.1k，平值价格ATM: C $3.53 / P $2.79 ｜ ATM IV 75.4%，预期波动 ±1.6%，Max Pain 400
Top ΔOI: P 300 +4,159 ｜ C 402 +3,892 ｜ P 380 +3,138

📆 Forward Expiration Structure

11-06  C +12.0k / P +6.3k ｜ Activity HIGH ｜ 2D
11-09  C +6.5k / P +5.7k ｜ Activity HIGH ｜ 5D
11-11  C +2.4k / P +1.3k ｜ Activity HIGH ｜ 7D
11-13  C +4.4k / P +4.4k ｜ Activity HIGH ｜ 9D

📆 11-06 Forward Structure
存量OI: C 170.3k / P 258.9k，今日变化ΔOI: C +12.0k / P +6.3k，平值价格ATM: C $7.55 / P $6.53 ｜ ATM IV 58.0%，净 delta 敞口 -33k shares
Top ΔOI: P 385 +1,243 ｜ C 400 +1,066
仓位参考: Max Pain 395 ｜ Call Wall 410（+6.5%，弱）（OI 10.8k） ｜ Put Wall 380（-1.2%，弱）（OI 10.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 58.0%｜历史 Rank 88%（近端代理）｜IV/RV 1.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 32,746 股

📆 11-09 Forward Structure
存量OI: C 20.1k / P 15.3k，今日变化ΔOI: C +6.5k / P +5.7k，平值价格ATM: C $8.70 / P $7.95 ｜ ATM IV 45.1%，净 delta 敞口 -25k shares
Top ΔOI: C 420 +609
仓位参考: Max Pain 400 ｜ Call Wall 420（+9.1%）（OI 2.4k） ｜ Put Wall 380（-1.2%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 45.1%｜历史 Rank 88%（近端代理）｜IV/RV 1.38×（近似）｜净 delta 敞口 负 25,251 股

📆 11-11 Forward Structure
存量OI: C 10.0k / P 5.5k，今日变化ΔOI: C +2.4k / P +1.3k，平值价格ATM: C $11.10 / P $9.35 ｜ ATM IV 46.8%，净 delta 敞口 -8k shares
Top ΔOI: C 410 +484 ｜ P 355 +435
仓位参考: Max Pain 400 ｜ Call Wall 410（+6.5%，弱）（OI 1.1k） ｜ Put Wall 405（+5.2%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 46.8%｜历史 Rank 88%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 负 8,225 股

📆 11-13 Forward Structure
存量OI: C 51.2k / P 37.1k，今日变化ΔOI: C +4.4k / P +4.4k，平值价格ATM: C $12.30 / P $10.59 ｜ ATM IV 47.1%，净 delta 敞口 -42k shares
Top ΔOI: C 407 +1,310
仓位参考: Max Pain 380 ｜ Call Wall 420（+9.1%，弱）（OI 2.1k） ｜ Put Wall 350（-9.0%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 47.1%｜历史 Rank 88%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 负 41,792 股

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 58.0% vs 11-09 45.1%（差 +12.9pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=83 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=83）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/TSLA_morning.json