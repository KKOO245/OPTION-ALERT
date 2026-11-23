# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.39 ｜ QQQ $651.03
VIX 27.37 ↓23.7%（5D +19.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.4 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-25 370C ΔOI +1,057（距现价 -4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 120P ΔOI +66,217 占该期限总 OI 22.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 345.82 → 今开 374.84（+8.4%） | 较昨收变动（含盘初走势） ｜ 今日高 392.53 ｜ 低 371.99

Options: P/C成交量 0.39 | OI比 0.97 | ATM IV 96.2% | Skew 11.2pp | Term 0.54 | ExpMove ±4.5%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.54，近月 IV 高于远月）｜保护溢价显著（Skew 11.2pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-25（2D）±4.5% ｜ 11-27（4D）±0.0% ｜ 11-30（7D）±6.0% ｜ 12-02（9D）±7.1%
   ⇒ IV–VIX Spread: +68.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 62,885,994 | GEX Change vs 上次快照 91,150,406 | Flip: Primary Flip: 360.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1089 / LOW 283 / INVALID 1006
结构观察区: Primary Flip 360.57（全链重定价，覆盖 97%）
Call Wall 400（弱结构｜现价低于该位 2.7%）
最近结构参考: Call Wall 400（现价低于该位 2.7%）
量化视角： 正 Gamma（6289万，无历史分位）｜由负转正（+9115万）｜现价位于 Flip 上方 7.94%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 360（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 361（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 120.0P — Vol 66,221 | 最新价 $0.01 | OI 2233→68450 (ΔOI +66217张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增66217张（+2965.4% vs前日OI），连续性待观察（方向未知）
11-23 250.0P — Vol 19,119 | 最新价 $0.06 | OI 22→18997 (ΔOI +18975张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18975张（+86250.0% vs前日OI），连续性待观察（方向未知）
11-27 130.0P — Vol 17,214 | 最新价 $0.01 | OI 350→17272 (ΔOI +16922张) | ΔOI/Volume 98.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16922张（+4834.9% vs前日OI），连续性待观察（方向未知）
11-27 200.0P — Vol 13,108 | 最新价 $0.13 | OI 5031→14921 (ΔOI +9890张) | ΔOI/Volume 75.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9890张（+196.6% vs前日OI），连续性待观察（方向未知）
11-30 420.0C — Vol 8,449 | 最新价 $0.20 | OI 3290→11309 (ΔOI +8019张) | ΔOI/Volume 94.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8019张（+243.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 120,023 张（Put 112,004 / Call 8,019），跨 3 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 53.1k / P 51.6k，今日成交量: C 201.6k / P 78.5k，平值价格ATM: C $4.05 / P $3.95 ｜ ATM IV 96.2%，预期波动 ±2.1%，Max Pain 360
Top ΔOI: P 250 +18,975 ｜ C 377 +2,825 ｜ C 440 -2,699

📆 Forward Expiration Structure

11-25  C +5.9k / P +4.4k ｜ Activity HIGH ｜ 2D
11-27  C +30.9k / P +113.1k ｜ Activity HIGH ｜ 4D
11-30  C +10.7k / P +4.9k ｜ Activity HIGH ｜ 7D
12-02  C +1.4k / P +1.2k ｜ Activity HIGH ｜ 9D

📆 11-25 Forward Structure
存量OI: C 13.8k / P 13.6k，今日变化ΔOI: C +5.9k / P +4.4k，平值价格ATM: C $8.80 / P $8.50 ｜ ATM IV 70.5%，净 delta 敞口 390k shares
Top ΔOI: C 370 +1,057 ｜ C 375 +624
仓位参考: Max Pain 372 ｜ Call Wall 400（+2.8%，弱）（OI 1.2k） ｜ Put Wall 382.5（-1.7%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 70.5%｜历史 Rank 95%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 390,481 股

📆 11-27 Forward Structure
存量OI: C 118.0k / P 179.5k，今日变化ΔOI: C +30.9k / P +113.1k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 75.8%，净 delta 敞口 2.1M shares
Top ΔOI: P 120 +66,217
仓位参考: Max Pain 362 ｜ Call Wall 410（+5.3%，弱）（OI 9.8k）
量化解读： 存量 Put 重｜ATM IV 75.8%｜历史 Rank 95%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,077,353 股

📆 11-30 Forward Structure
存量OI: C 17.7k / P 9.6k，今日变化ΔOI: C +10.7k / P +4.9k，平值价格ATM: C $11.45 / P $12.05 ｜ ATM IV 51.4%，净 delta 敞口 60k shares
Top ΔOI: C 420 +8,019 ｜ P 395 +1,511 ｜ P 392 +1,488
仓位参考: Max Pain 395 ｜ Call Wall 420（+7.9%）（OI 11.3k） ｜ Put Wall 395（+1.5%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 51.4%｜历史 Rank 95%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 60,311 股

📆 12-02 Forward Structure
存量OI: C 3.1k / P 2.4k，今日变化ΔOI: C +1.4k / P +1.2k，平值价格ATM: C $13.60 / P $13.90 ｜ ATM IV 54.7%，净 delta 敞口 79k shares
Top ΔOI: C 372 +442 ｜ C 400 +247
仓位参考: Max Pain 372 ｜ Call Wall 400（+2.8%，弱）（OI 0.5k） ｜ Put Wall 360（-7.5%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 54.7%｜历史 Rank 95%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 79,288 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/TSLA_morning.json