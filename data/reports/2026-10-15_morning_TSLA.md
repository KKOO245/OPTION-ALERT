# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $767.19 ｜ QQQ $720.38
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🔴 **事件差分**: 10-16（1D）ATM IV 64.6% vs 10-19 40.6%（差 +24.1pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 365P ΔOI +3,782（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 367.16 → 今开 360.58（-1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 360.58 ｜ 低 355.23

Options: P/C成交量 0.80 | OI比 0.95 | ATM IV 64.7% | Skew 0.3pp | Term 0.70 | ExpMove ±3.1%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价薄（Skew 0.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±3.1% ｜ 10-19（4D）±3.5% ｜ 10-23（8D）±7.4% ｜ 10-26（11D）±7.7%
   ⇒ IV–VIX Spread: +47.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -32,193,593 | GEX Change vs 上次快照 -33,666,256 | Flip: Primary Flip: 362.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1169 / LOW 148 / INVALID 541
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 362.43（全链重定价，覆盖 99%）
最近结构参考: Flip 362（现价低于该位 1.8%）
量化视角： 负 Gamma（3219万，无历史分位）｜由正转负（3367万）｜现价位于 Flip 下方 1.82%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 370（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 362（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 435.0C — Vol 8,791 | 最新价 $0.06 | OI 3630→8715 (ΔOI +5085张) | ΔOI/Volume 57.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5085张（+140.1% vs前日OI），连续性待观察（方向未知）
10-19 250.0P — Vol 4,429 | 最新价 $0.05 | OI 106→4351 (ΔOI +4245张) | ΔOI/Volume 95.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4245张（+4004.7% vs前日OI），连续性待观察（方向未知）
10-16 432.5C — Vol 4,277 | 最新价 $0.06 | OI 126→4141 (ΔOI +4015张) | ΔOI/Volume 93.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4015张（+3186.5% vs前日OI），连续性待观察（方向未知）
10-16 365.0P — Vol 26,922 | 最新价 $4.85 | OI 6229→10011 (ΔOI +3782张) | ΔOI/Volume 14.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3782张（+60.7% vs前日OI），连续性待观察（方向未知）
10-19 290.0P — Vol 3,013 | 最新价 $0.09 | OI 93→3042 (ΔOI +2949张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2949张（+3171.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 20,076 张（Put 10,976 / Call 9,100），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +32.6k / P +12.3k ｜ Activity HIGH ｜ 1D
10-19  C +11.9k / P +14.7k ｜ Activity HIGH ｜ 4D
10-23  C +11.4k / P +5.5k ｜ Activity HIGH ｜ 8D
10-26  C +1.0k / P +1.1k ｜ Activity HIGH ｜ 11D

📆 10-16 Forward Structure
存量OI: C 436.7k / P 414.7k，今日变化ΔOI: C +32.6k / P +12.3k，平值价格ATM: C $6.27 / P $4.65 ｜ ATM IV 64.6%，净 delta 敞口 -280k shares
Top ΔOI: P 365 +3,782
仓位参考: Max Pain 370 ｜ Call Wall 380（+6.8%，弱）（OI 18.3k） ｜ Put Wall 380（+6.8%，弱）（OI 15.2k）
量化解读： 存量两侧均衡｜ATM IV 64.6%｜历史 Rank 78%（近端代理）｜IV/RV 2.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 279,943 股

📆 10-19 Forward Structure
存量OI: C 38.9k / P 25.3k，今日变化ΔOI: C +11.9k / P +14.7k，平值价格ATM: C $7.07 / P $5.40 ｜ ATM IV 40.6%，净 delta 敞口 -45k shares
Top ΔOI: C 367 +1,587
仓位参考: Max Pain 370 ｜ Call Wall 390（+9.6%，弱）（OI 2.4k） ｜ Put Wall 365（+2.6%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.6%｜历史 Rank 78%（近端代理）｜IV/RV 1.44×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 45,347 股

📆 10-23 Forward Structure
存量OI: C 84.4k / P 55.5k，今日变化ΔOI: C +11.4k / P +5.5k，平值价格ATM: C $14.18 / P $12.28 ｜ ATM IV 61.8%，净 delta 敞口 12k shares
Top ΔOI: C 395 +1,890 ｜ P 365 +988
仓位参考: Max Pain 370 ｜ Call Wall 390（+9.6%，弱）（OI 5.8k） ｜ Put Wall 360（+1.2%，弱）（OI 3.2k）
量化解读： 存量 Call 重｜ATM IV 61.8%｜历史 Rank 78%（近端代理）｜IV/RV 2.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 12,186 股

📆 10-26 Forward Structure
存量OI: C 2.7k / P 3.9k，今日变化ΔOI: C +1.0k / P +1.1k，平值价格ATM: C $14.55 / P $13.00 ｜ ATM IV 55.4%，净 delta 敞口 -18k shares
Top ΔOI: P 367 +370 ｜ C 360 +203
仓位参考: Max Pain 368 ｜ Call Wall 380（+6.8%，弱）（OI 0.4k） ｜ Put Wall 367.5（+3.3%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 55.4%｜历史 Rank 78%（近端代理）｜IV/RV 1.97×（近似）｜净 delta 敞口 负 18,313 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 64.6% vs 10-19 40.6%（差 +24.1pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/TSLA_morning.json