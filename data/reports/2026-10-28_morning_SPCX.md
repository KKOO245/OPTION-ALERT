# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-30 ATM IV 62.0% vs 11-02 48.7%（差 +13.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 150P ΔOI +6,044（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 148.58 → 今开 147.29（-0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 147.57 ｜ 低 142.13

Options: P/C成交量 0.62 | OI比 0.80 | ATM IV 83.0% | Skew 1.0pp | Term 0.60 | ExpMove ±3.9%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价薄（Skew 1.0pp）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±3.9% ｜ 11-02（5D）±4.7% ｜ 11-04（7D）±5.6% ｜ 11-06（9D）±6.8%
   ⇒ IV–VIX Spread: +65.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -47,275,240 | GEX Change vs 上次快照 -50,845,695 | Flip: Primary Flip: 147.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 805 / LOW 159 / INVALID 600
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 147.05（全链重定价，覆盖 98%）
Put Wall 135（弱结构｜现价高于该位 6.4%）
最近结构参考: Flip 147（现价低于该位 2.3%）
量化视角： 负 Gamma（4728万，无历史分位）｜由正转负（5085万）｜现价位于 Flip 下方 2.34%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Put Wall，弱结构）；上方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 150.0P — Vol 12,227 | 最新价 $3.75 | OI 14277→20321 (ΔOI +6044张) | ΔOI/Volume 49.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6044张（+42.3% vs前日OI），连续性待观察（方向未知）
10-30 160.0C — Vol 20,847 | 最新价 $0.32 | OI 39941→44937 (ΔOI +4996张) | ΔOI/Volume 24.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4996张（+12.5% vs前日OI），连续性待观察（方向未知）
10-28 155.0C — Vol 54,461 | 最新价 $0.22 | OI 8260→13088 (ΔOI +4828张) | ΔOI/Volume 8.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4828张（+58.5% vs前日OI），连续性待观察（方向未知）
10-28 152.5C — Vol 37,864 | 最新价 $0.53 | OI 3381→7681 (ΔOI +4300张) | ΔOI/Volume 11.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4300张（+127.2% vs前日OI），连续性待观察（方向未知）
11-06 140.0P — Vol 5,181 | 最新价 $1.76 | OI 7108→10408 (ΔOI +3300张) | ΔOI/Volume 63.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3300张（+46.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,468 张（Put 9,344 / Call 14,124），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 58.5k / P 46.7k，今日成交量: C 76.4k / P 47.7k，平值价格ATM: C $1.02 / P $1.59 ｜ ATM IV 83.0%，预期波动 ±1.8%，Max Pain 150
Top ΔOI: C 155 +4,828 ｜ C 152 +4,300 ｜ P 150 +2,009

📆 Forward Expiration Structure

10-30  C +17.6k / P +10.9k ｜ Activity HIGH ｜ 2D
11-02  C +3.4k / P +3.7k ｜ Activity HIGH ｜ 5D
11-04  C +0.8k / P +1.6k ｜ Activity HIGH ｜ 7D
11-06  C +11.9k / P +9.1k ｜ Activity HIGH ｜ 9D

📆 10-30 Forward Structure
存量OI: C 275.5k / P 194.2k，今日变化ΔOI: C +17.6k / P +10.9k，平值价格ATM: C $2.55 / P $3.05 ｜ ATM IV 62.0%，净 delta 敞口 -635k shares
Top ΔOI: P 150 +6,044 ｜ C 155 +3,130
仓位参考: Max Pain 150 ｜ Call Wall 155（+7.9%，弱）（OI 20.8k） ｜ Put Wall 150（+4.4%）（OI 20.3k）
量化解读： 存量 Call 重｜ATM IV 62.0%｜历史 Rank 95%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 635,306 股

📆 11-02 Forward Structure
存量OI: C 20.2k / P 11.8k，今日变化ΔOI: C +3.4k / P +3.7k，平值价格ATM: C $3.15 / P $3.60 ｜ ATM IV 48.7%，净 delta 敞口 -165k shares
Top ΔOI: P 145 +2,401 ｜ C 150 +727 ｜ C 152 +656
仓位参考: Max Pain 148 ｜ Call Wall 152.5（+6.2%，弱）（OI 2.1k） ｜ Put Wall 145（+1.0%）（OI 2.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.7%｜历史 Rank 95%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 165,292 股

📆 11-04 Forward Structure
存量OI: C 7.7k / P 4.7k，今日变化ΔOI: C +0.8k / P +1.6k，平值价格ATM: C $4.00 / P $4.02 ｜ ATM IV 51.7%，净 delta 敞口 -49k shares
Top ΔOI: P 135 +572 ｜ P 149 +310 ｜ C 152 +222
仓位参考: Max Pain 150 ｜ Call Wall 155（+7.9%，弱）（OI 0.8k） ｜ Put Wall 135（-6.0%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 51.7%｜历史 Rank 95%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 负 49,079 股

📆 11-06 Forward Structure
存量OI: C 108.7k / P 75.9k，今日变化ΔOI: C +11.9k / P +9.1k，平值价格ATM: C $4.75 / P $5.00 ｜ ATM IV 52.8%，净 delta 敞口 -137k shares
Top ΔOI: P 140 +3,300 ｜ C 165 +2,617
仓位参考: Max Pain 150 ｜ Put Wall 140（-2.5%，弱）（OI 10.4k）
量化解读： 存量 Call 重｜ATM IV 52.8%｜历史 Rank 95%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 负 137,395 股

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 62.0% vs 11-02 48.7%（差 +13.3pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/SPCX_morning.json