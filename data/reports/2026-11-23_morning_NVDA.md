# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.14 ｜ QQQ $655.58
VIX 27.37 ↓23.7%（5D +19.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 19.0（extreme fear）
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
🔴 **事件差分**: 11-25（2D）ATM IV 114.7% vs 11-27 91.9%（差 +22.8pp），覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 125.53 → 今开 167.04（+33.1%） | 较昨收变动（含盘初走势） ｜ 今日高 170.72 ｜ 低 156.93

Options: P/C成交量 0.57 | OI比 0.51 | ATM IV 184.7% | Skew 1.0pp | Term 0.34 | ExpMove ±7.1%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.34，近月 IV 高于远月）｜保护溢价薄（Skew 1.0pp）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-25（2D）±7.1% ｜ 11-27（4D）±7.9% ｜ 11-30（7D）±8.7% ｜ 12-02（9D）±9.6%
   ⇒ IV–VIX Spread: +157.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 265,381,534 | GEX Change vs 上次快照 337,341,971 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1318 / LOW 248 / INVALID 824
结构观察区: NO_CROSS
Call Wall 170（弱结构｜现价低于该位 2.1%）
最近结构参考: Call Wall 170（现价低于该位 2.1%）
量化视角： 正 Gamma（2.65亿，无历史分位）｜由负转正（+3.37亿）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 137（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 170.0C — Vol 38,587 | 最新价 $0.73 | OI 149816→175759 (ΔOI +25943张) | ΔOI/Volume 67.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25943张（+17.3% vs前日OI），连续性待观察（方向未知）
12-18 160.0C — Vol 49,423 | 最新价 $1.35 | OI 28791→48554 (ΔOI +19763张) | ΔOI/Volume 40.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19763张（+68.6% vs前日OI），连续性待观察（方向未知）
11-27 150.0C — Vol 36,062 | 最新价 $0.72 | OI 4044→18002 (ΔOI +13958张) | ΔOI/Volume 38.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13958张（+345.1% vs前日OI），连续性待观察（方向未知）
11-27 140.0C — Vol 43,244 | 最新价 $2.19 | OI 612→13863 (ΔOI +13251张) | ΔOI/Volume 30.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13251张（+2165.2% vs前日OI），连续性待观察（方向未知）
11-23 150.0C — Vol 46,209 | 最新价 $0.14 | OI 4826→17214 (ΔOI +12388张) | ΔOI/Volume 26.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12388张（+256.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 85,303 张（Put 0 / Call 85,303），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 215.5k / P 110.4k，今日成交量: C 664.2k / P 378.1k，平值价格ATM: C $2.67 / P $4.12 ｜ ATM IV 184.7%，预期波动 ±4.1%，Max Pain 137
Top ΔOI: C 150 +12,388 ｜ C 140 +11,857 ｜ C 145 +8,621

📆 Forward Expiration Structure

11-25  C +40.0k / P +37.7k ｜ Activity HIGH ｜ 2D
11-27  C +118.3k / P +82.8k ｜ Activity HIGH ｜ 4D
11-30  C +22.1k / P +7.1k ｜ Activity HIGH ｜ 7D
12-02  C +8.6k / P +2.0k ｜ Activity HIGH ｜ 9D

📆 11-25 Forward Structure
存量OI: C 98.9k / P 63.2k，今日变化ΔOI: C +40.0k / P +37.7k，平值价格ATM: C $5.35 / P $6.50 ｜ ATM IV 114.7%，净 delta 敞口 3.4M shares
Top ΔOI: C 150 +7,036
仓位参考: Max Pain 140 ｜ Call Wall 160（-3.9%，弱）（OI 10.7k）
量化解读： 存量 Call 重｜ATM IV 114.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,404,188 股

📆 11-27 Forward Structure
存量OI: C 491.9k / P 269.6k，今日变化ΔOI: C +118.3k / P +82.8k，平值价格ATM: C $5.81 / P $7.29 ｜ ATM IV 91.9%，净 delta 敞口 11.1M shares
Top ΔOI: C 150 +13,958 ｜ C 140 +13,251
仓位参考: Max Pain 145 ｜ Call Wall 165（-0.9%，弱）（OI 34.0k） ｜ Put Wall 165（-0.9%，弱）（OI 15.4k）
量化解读： 存量 Call 重｜ATM IV 91.9%｜历史 Rank 100%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,100,721 股

📆 11-30 Forward Structure
存量OI: C 60.9k / P 25.5k，今日变化ΔOI: C +22.1k / P +7.1k，平值价格ATM: C $6.50 / P $7.90 ｜ ATM IV 76.1%，净 delta 敞口 1.9M shares
Top ΔOI: C 150 +8,040 ｜ C 147 +1,947
仓位参考: Max Pain 140 ｜ Call Wall 150（-9.9%）（OI 9.5k） ｜ Put Wall 150（-9.9%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 76.1%｜历史 Rank 100%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,860,027 股

📆 12-02 Forward Structure
存量OI: C 29.8k / P 7.1k，今日变化ΔOI: C +8.6k / P +2.0k，平值价格ATM: C $7.40 / P $8.52 ｜ ATM IV 75.0%，净 delta 敞口 614k shares
Top ΔOI: C 180 +1,224 ｜ C 150 +1,013 ｜ C 140 +971
仓位参考: Max Pain 140 ｜ Call Wall 160（-3.9%，弱）（OI 3.3k） ｜ Put Wall 150（-9.9%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 75.0%｜历史 Rank 100%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 正 613,582 股

📅 事件差分（观察，非因果）: 11-25（2D）ATM IV 114.7% vs 11-27 91.9%（差 +22.8pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location ? | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/NVDA_morning.json