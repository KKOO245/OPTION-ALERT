# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $769.48 ｜ QQQ $716.05
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-30 ATM IV 47.6% vs 11-02 35.8%（差 +11.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 49C ΔOI +2,364（距现价 +3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 49.06 → 今开 47.23（-3.7%） | 较昨收变动（含盘初走势） ｜ 今日高 47.42 ｜ 低 46.93

Options: P/C成交量 0.45 | OI比 0.39 | ATM IV 47.6% | Skew 3.3pp | Term 0.83 | ExpMove ±2.3%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜存量 Call 偏重（OI比 0.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.3% ｜ 11-02（4D）±3.2% ｜ 11-04（6D）±4.4% ｜ 11-06（8D）±5.2%
   ⇒ IV–VIX Spread: +30.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -20,760,890 | GEX Change vs 上次快照 -23,337,345 | Flip: Primary Flip: 48.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 709 / LOW 103 / INVALID 280
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 48.02（全链重定价，覆盖 99%）
Put Wall 50（弱结构｜现价低于该位 5.5%）
最近结构参考: Flip 48（现价低于该位 1.6%）
量化视角： 负 Gamma（2076万，无历史分位）｜由正转负（2334万）｜现价位于 Flip 下方 1.61%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 31.0P — Vol 4,500 | 最新价 $0.03 | OI 13→4505 (ΔOI +4492张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4492张（+34553.8% vs前日OI），连续性待观察（方向未知）
11-20 50.0C — Vol 7,246 | 最新价 $1.50 | OI 5730→9701 (ΔOI +3971张) | ΔOI/Volume 54.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3971张（+69.3% vs前日OI），连续性待观察（方向未知）
11-06 50.0C — Vol 5,401 | 最新价 $0.83 | OI 1108→4016 (ΔOI +2908张) | ΔOI/Volume 53.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2908张（+262.4% vs前日OI），连续性待观察（方向未知）
10-30 49.0C — Vol 5,511 | 最新价 $0.70 | OI 1063→3427 (ΔOI +2364张) | ΔOI/Volume 42.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2364张（+222.4% vs前日OI），连续性待观察（方向未知）
10-30 49.5C — Vol 4,346 | 最新价 $0.47 | OI 1024→3068 (ΔOI +2044张) | ΔOI/Volume 47.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2044张（+199.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,779 张（Put 4,492 / Call 11,287），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +10.2k / P +1.4k ｜ Activity HIGH ｜ 1D
11-02  C +3.8k / P +1.9k ｜ Activity HIGH ｜ 4D
11-04  C +1.9k / P +1.7k ｜ Activity HIGH ｜ 6D
11-06  C +4.6k / P -0.3k ｜ Activity MEDIUM △ ｜ 8D

📆 10-30 Forward Structure
存量OI: C 101.6k / P 39.5k，今日变化ΔOI: C +10.2k / P +1.4k，平值价格ATM: C $0.70 / P $0.39 ｜ ATM IV 47.6%，净 delta 敞口 188k shares
Top ΔOI: C 49 +2,364 ｜ C 49 +2,044 ｜ C 48 +1,348
仓位参考: Max Pain 50 ｜ Call Wall 50（+5.8%，弱）（OI 5.7k） ｜ Put Wall 45（-4.8%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 47.6%｜历史 Rank 80%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 187,984 股

📆 11-02 Forward Structure
存量OI: C 7.9k / P 7.6k，今日变化ΔOI: C +3.8k / P +1.9k，平值价格ATM: C $0.92 / P $0.59 ｜ ATM IV 35.8%，净 delta 敞口 -19k shares
Top ΔOI: C 50 +1,546 ｜ C 49 +753 ｜ P 48 +508
仓位参考: Max Pain 49 ｜ Call Wall 50（+5.8%）（OI 2.2k） ｜ Put Wall 47.5（+0.5%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 35.8%｜历史 Rank 80%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 19,173 股

📆 11-04 Forward Structure
存量OI: C 12.3k / P 5.9k，今日变化ΔOI: C +1.9k / P +1.7k，平值价格ATM: C $1.18 / P $0.92 ｜ ATM IV 41.6%，净 delta 敞口 -28k shares
Top ΔOI: P 44 +502
仓位参考: Max Pain 48 ｜ Call Wall 51.5（+9.0%，弱）（OI 3.1k） ｜ Put Wall 44（-6.9%）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 41.6%｜历史 Rank 80%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 负 28,390 股

11-06（MEDIUM △）Top ΔOI: 50C +2,908 ｜ 49C +524
11-06（MEDIUM △）仓位参考: Max Pain 51 ｜ Put Wall 43（-9.0%，弱）（OI 3.0k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 47.6% vs 11-02 35.8%（差 +11.8pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/SLV_morning.json