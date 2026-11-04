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
🟡 **事件差分**: 11-06 ATM IV 52.5% vs 11-09 41.1%（差 +11.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-09 207P ΔOI +2,070（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 206.69 → 今开 203.58（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 206.79 ｜ 低 200.94

Options: P/C成交量 0.59 | OI比 1.12 | ATM IV 63.4% | Skew 3.9pp | Term 0.73 | ExpMove ±3.3%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价中性（Skew 3.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.12×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（2D）±3.3% ｜ 11-09（5D）±3.9% ｜ 11-11（7D）±4.8% ｜ 11-13（9D）±5.5%
   ⇒ IV–VIX Spread: +46.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 92,441,905 | GEX Change vs 上次快照 -31,485,199 | Flip: Primary Flip: 203.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 710 / LOW 170 / INVALID 630
结构观察区: Primary Flip 203.00（全链重定价，覆盖 98%）
Put Wall 200（弱结构｜现价高于该位 2.9%）
最近结构参考: Flip 203（现价高于该位 1.3%）
量化视角： 正 Gamma（9244万，无历史分位）｜正 Gamma 减弱（3149万）｜现价位于 Flip 上方 1.33%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 208（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 203（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-04 215.0C — Vol 55,619 | 最新价 $0.32 | OI 6339→15885 (ΔOI +9546张) | ΔOI/Volume 17.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9546张（+150.6% vs前日OI），连续性待观察（方向未知）
11-06 242.5C — Vol 13,013 | 最新价 $0.01 | OI 1023→9241 (ΔOI +8218张) | ΔOI/Volume 63.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8218张（+803.3% vs前日OI），连续性待观察（方向未知）
11-04 200.0P — Vol 43,616 | 最新价 $0.60 | OI 8748→15239 (ΔOI +6491张) | ΔOI/Volume 14.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6491张（+74.2% vs前日OI），连续性待观察（方向未知）
11-04 180.0P — Vol 8,308 | 最新价 $0.01 | OI 3594→10025 (ΔOI +6431张) | ΔOI/Volume 77.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6431张（+178.9% vs前日OI），连续性待观察（方向未知）
11-04 212.5C — Vol 64,438 | 最新价 $0.69 | OI 6974→12016 (ΔOI +5042张) | ΔOI/Volume 7.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5042张（+72.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 35,728 张（Put 12,922 / Call 22,806），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 111.3k / P 124.4k，今日成交量: C 201.2k / P 118.0k，平值价格ATM: C $1.71 / P $1.15 ｜ ATM IV 63.4%，预期波动 ±1.4%，Max Pain 208
Top ΔOI: C 215 +9,546 ｜ P 200 +6,491 ｜ P 180 +6,431

📆 Forward Expiration Structure

11-06  C +32.4k / P +17.4k ｜ Activity HIGH ｜ 2D
11-09  C +4.4k / P +4.8k ｜ Activity HIGH ｜ 5D
11-11  C +2.2k / P +5.1k ｜ Activity HIGH ｜ 7D
11-13  C +8.3k / P +9.3k ｜ Activity HIGH ｜ 9D

📆 11-06 Forward Structure
存量OI: C 403.0k / P 292.6k，今日变化ΔOI: C +32.4k / P +17.4k，平值价格ATM: C $3.75 / P $3.08 ｜ ATM IV 52.5%，净 delta 敞口 27k shares
Top ΔOI: C 220 +4,560 ｜ C 222 +4,112
仓位参考: Max Pain 208 ｜ Call Wall 220（+6.9%，弱）（OI 55.4k） ｜ Put Wall 200（-2.8%，弱）（OI 21.9k）
量化解读： 存量 Call 重｜ATM IV 52.5%｜历史 Rank 88%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,501 股

📆 11-09 Forward Structure
存量OI: C 16.0k / P 17.0k，今日变化ΔOI: C +4.4k / P +4.8k，平值价格ATM: C $4.40 / P $3.70 ｜ ATM IV 41.1%，净 delta 敞口 -91k shares
Top ΔOI: P 207 +2,070 ｜ C 222 +952 ｜ P 190 +872
仓位参考: Max Pain 208 ｜ Call Wall 220（+6.9%，弱）（OI 2.2k） ｜ Put Wall 207.5（+0.9%，弱）（OI 2.5k）
量化解读： 存量两侧均衡｜ATM IV 41.1%｜历史 Rank 88%（近端代理）｜IV/RV 1.32×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 91,082 股

📆 11-11 Forward Structure
存量OI: C 9.1k / P 17.3k，今日变化ΔOI: C +2.2k / P +5.1k，平值价格ATM: C $5.25 / P $4.60 ｜ ATM IV 42.5%，净 delta 敞口 -48k shares
Top ΔOI: P 192 +1,227 ｜ P 202 +759
仓位参考: Max Pain 210 ｜ Call Wall 220（+6.9%）（OI 2.4k） ｜ Put Wall 190（-7.6%）（OI 4.9k）
量化解读： 存量 Put 重｜ATM IV 42.5%｜历史 Rank 88%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 负 48,019 股

📆 11-13 Forward Structure
存量OI: C 170.8k / P 183.6k，今日变化ΔOI: C +8.3k / P +9.3k，平值价格ATM: C $6.12 / P $5.25 ｜ ATM IV 43.3%，净 delta 敞口 -59k shares
Top ΔOI: C 215 +2,527 ｜ P 185 +1,529 ｜ C 220 +1,406
仓位参考: Max Pain 215 ｜ Call Wall 220（+6.9%，弱）（OI 14.2k） ｜ Put Wall 200（-2.8%，弱）（OI 15.1k）
量化解读： 存量两侧均衡｜ATM IV 43.3%｜历史 Rank 88%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 负 58,851 股

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 52.5% vs 11-09 41.1%（差 +11.4pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/NVDA_morning.json