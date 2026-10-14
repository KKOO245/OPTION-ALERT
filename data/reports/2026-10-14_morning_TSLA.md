# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $773.15 ｜ QQQ $736.46
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-16 ATM IV 51.2% vs 10-19 37.6%（差 +13.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-19 375C ΔOI +602（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 375.23 → 今开 371.15（-1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 371.39 ｜ 低 364.44

Options: P/C成交量 1.50 | OI比 0.76 | ATM IV 48.8% | Skew 0.2pp | Term 0.88 | ExpMove ±3.2%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 0.2pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.76）+ 当日成交偏 Put（P/C量 1.50）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.50×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±3.2% ｜ 10-19（5D）±3.6% ｜ 10-23（9D）±7.1% ｜ 10-26（12D）±7.3%
   ⇒ IV–VIX Spread: +33.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,476,580 | GEX Change vs 上次快照 -58,235,968 | Flip: Primary Flip: 366.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1182 / LOW 169 / INVALID 627
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 366.23（全链重定价，覆盖 96%）
Call Wall 400（现价低于该位 8.7%）
最近结构参考: Flip 366（现价低于该位 0.3%）
量化视角： 负 Gamma（648万，无历史分位）｜由正转负（5824万）｜现价位于 Flip 下方 0.26%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 375（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 366（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-14 380.0C — Vol 52,742 | 最新价 $1.24 | OI 3618→8640 (ΔOI +5022张) | ΔOI/Volume 9.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5022张（+138.8% vs前日OI），连续性待观察（方向未知）
10-14 370.0P — Vol 50,399 | 最新价 $1.03 | OI 2821→7093 (ΔOI +4272张) | ΔOI/Volume 8.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4272张（+151.4% vs前日OI），连续性待观察（方向未知）
10-14 372.5P — Vol 55,565 | 最新价 $1.80 | OI 1444→5056 (ΔOI +3612张) | ΔOI/Volume 6.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3612张（+250.1% vs前日OI），连续性待观察（方向未知）
10-14 405.0C — Vol 4,581 | 最新价 $0.03 | OI 1400→4950 (ΔOI +3550张) | ΔOI/Volume 77.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3550张（+253.6% vs前日OI），连续性待观察（方向未知）
10-14 375.0C — Vol 57,677 | 最新价 $3.14 | OI 1460→3831 (ΔOI +2371张) | ΔOI/Volume 4.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2371张（+162.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,827 张（Put 7,884 / Call 10,943），跨 1 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 75.8k / P 57.6k，今日成交量: C 140.5k / P 209.9k，平值价格ATM: C $2.12 / P $1.75 ｜ ATM IV 48.8%，预期波动 ±1.1%，Max Pain 375
Top ΔOI: C 380 +5,022 ｜ P 370 +4,272 ｜ P 372 +3,612

📆 Forward Expiration Structure

10-16  C +9.0k / P +9.8k ｜ Activity HIGH ｜ 2D
10-19  C +4.7k / P +2.5k ｜ Activity HIGH ｜ 5D
10-23  C +5.7k / P +4.3k ｜ Activity HIGH ｜ 9D
10-26  C +1.0k / P +1.5k ｜ Activity HIGH ｜ 12D

📆 10-16 Forward Structure
存量OI: C 404.1k / P 402.4k，今日变化ΔOI: C +9.0k / P +9.8k，平值价格ATM: C $6.19 / P $5.65 ｜ ATM IV 51.2%，净 delta 敞口 72k shares
Top ΔOI: C 400 +1,711
仓位参考: Max Pain 372 ｜ Call Wall 400（+9.5%，弱）（OI 26.1k） ｜ Put Wall 380（+4.0%，弱）（OI 15.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 51.2%｜历史 Rank 40%（近端代理）｜IV/RV 1.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 72,472 股

📆 10-19 Forward Structure
存量OI: C 27.0k / P 10.6k，今日变化ΔOI: C +4.7k / P +2.5k，平值价格ATM: C $6.95 / P $6.26 ｜ ATM IV 37.6%，净 delta 敞口 -51k shares
Top ΔOI: C 375 +602 ｜ C 390 +573
仓位参考: Max Pain 375 ｜ Call Wall 400（+9.5%，弱）（OI 3.2k） ｜ Put Wall 360（-1.4%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 37.6%｜历史 Rank 40%（近端代理）｜IV/RV 1.39×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 51,365 股

📆 10-23 Forward Structure
存量OI: C 73.0k / P 50.0k，今日变化ΔOI: C +5.7k / P +4.3k，平值价格ATM: C $13.45 / P $12.48 ｜ ATM IV 55.9%，净 delta 敞口 -66k shares
Top ΔOI: C 390 +1,242 ｜ P 375 +792 ｜ P 362 +670
仓位参考: Max Pain 372 ｜ Call Wall 400（+9.5%，弱）（OI 6.3k） ｜ Put Wall 360（-1.4%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 55.9%｜历史 Rank 40%（近端代理）｜IV/RV 2.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 65,568 股

📆 10-26 Forward Structure
存量OI: C 1.7k / P 2.8k，今日变化ΔOI: C +1.0k / P +1.5k，平值价格ATM: C $13.88 / P $12.75 ｜ ATM IV 50.2%，净 delta 敞口 -13k shares
Top ΔOI: P 350 +217
仓位参考: Max Pain 375 ｜ Call Wall 380（+4.0%，弱）（OI 0.3k） ｜ Put Wall 350（-4.2%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜ATM IV 50.2%｜历史 Rank 40%（近端代理）｜IV/RV 1.86×（近似）｜净 delta 敞口 负 13,263 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 51.2% vs 10-19 37.6%（差 +13.6pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/TSLA_morning.json