# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $757.88 ｜ QQQ $688.17
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（1D）ATM IV 159.3% vs 11-20 112.7%（差 +46.6pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔵 **期限 OI 集中**: 12-04 70P ΔOI +1,578 占该期限总 OI 14.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 154.69 → 今开 119.88（-22.5%） | 较昨收变动（含盘初走势） ｜ 今日高 132.69 ｜ 低 118.81

Options: P/C成交量 0.51 | OI比 0.54 | ATM IV 159.3% | Skew -4.8pp | Term 0.60 | ExpMove ±7.3%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±7.3% ｜ 11-20（8D）±13.4% ｜ 11-27（15D）±14.6% ｜ 12-04（22D）±17.8%
   ⇒ IV–VIX Spread: +140.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,660,539 | GEX Change vs 上次快照 -17,284,185 | Flip: Primary Flip: 135.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 581 / LOW 109 / INVALID 210
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 135.98（全链重定价，覆盖 98%）
最近结构参考: Flip 136（现价低于该位 7.1%）
量化视角： 负 Gamma（1066万，无历史分位）｜由正转负（1728万）｜现价位于 Flip 下方 7.09%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 146（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 136（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 180.0C — Vol 15,105 | 最新价 $2.87 | OI 2709→10230 (ΔOI +7521张) | ΔOI/Volume 49.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7521张（+277.6% vs前日OI），连续性待观察（方向未知）
11-13 177.5C — Vol 8,210 | 最新价 $3.30 | OI 1085→6739 (ΔOI +5654张) | ΔOI/Volume 68.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5654张（+521.1% vs前日OI），连续性待观察（方向未知）
11-13 200.0C — Vol 11,980 | 最新价 $0.92 | OI 5201→8431 (ΔOI +3230张) | ΔOI/Volume 27.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3230张（+62.1% vs前日OI），连续性待观察（方向未知）
11-13 165.0C — Vol 6,773 | 最新价 $6.35 | OI 1512→4694 (ΔOI +3182张) | ΔOI/Volume 47.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3182张（+210.4% vs前日OI），连续性待观察（方向未知）
11-13 170.0C — Vol 10,164 | 最新价 $4.90 | OI 2917→5587 (ΔOI +2670张) | ΔOI/Volume 26.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2670张（+91.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 22,257 张（Put 0 / Call 22,257），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +38.6k / P +16.2k ｜ Activity HIGH ｜ 1D
11-20  C +9.8k / P +5.3k ｜ Activity HIGH ｜ 8D
11-27  C +3.0k / P +2.7k ｜ Activity HIGH ｜ 15D
12-04  C +0.5k / P +1.6k ｜ Activity HIGH ｜ 22D

📆 11-13 Forward Structure
存量OI: C 121.6k / P 66.2k，今日变化ΔOI: C +38.6k / P +16.2k，平值价格ATM: C $4.55 / P $4.70 ｜ ATM IV 159.3%，净 delta 敞口 -935k shares
仓位参考: Max Pain 146 ｜ Put Wall 130（+2.9%，弱）（OI 4.1k）
量化解读： 存量 Call 重｜ATM IV 159.3%｜历史 Rank 94%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 934,918 股

📆 11-20 Forward Structure
存量OI: C 133.4k / P 114.4k，今日变化ΔOI: C +9.8k / P +5.3k，平值价格ATM: C $8.40 / P $8.55 ｜ ATM IV 112.7%，净 delta 敞口 -81k shares
Top ΔOI: C 165 +1,354 ｜ C 160 +1,086
仓位参考: Max Pain 175 ｜ Put Wall 115（-9.0%，弱）（OI 8.8k）
量化解读： 存量两侧均衡｜ATM IV 112.7%｜历史 Rank 94%（近端代理）｜IV/RV 0.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 80,847 股

📆 11-27 Forward Structure
存量OI: C 17.5k / P 19.6k，今日变化ΔOI: C +3.0k / P +2.7k，平值价格ATM: C $10.50 / P $7.88 ｜ ATM IV 101.1%，净 delta 敞口 -23k shares
仓位参考: Max Pain 185
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 101.1%｜历史 Rank 94%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 23,146 股

📆 12-04 Forward Structure
存量OI: C 4.5k / P 6.6k，今日变化ΔOI: C +0.5k / P +1.6k，平值价格ATM: C $12.20 / P $10.25 ｜ ATM IV 97.6%，净 delta 敞口 -10k shares
仓位参考: Max Pain 155 ｜ Put Wall 115（-9.0%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 97.6%｜历史 Rank 94%（近端代理）｜IV/RV 0.78×（近似）｜净 delta 敞口 负 9,892 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 159.3% vs 11-20 112.7%（差 +46.6pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/NBIS_morning.json