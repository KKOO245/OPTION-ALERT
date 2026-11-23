# 期权晚报 2026-11-23（快照 16:40 ET）

📊 市场环境

SPY $722.29 ｜ QQQ $651.03
VIX 26.62 ↓25.8%（5D +16.2%） ｜ Vol Regime: STRESS
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
🟡 **事件差分**: 11-25 ATM IV 105.4% vs 11-27 95.1%（差 +10.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 167.04 → 收盘 165.05（-1.2%） ｜ 今日高 171.50 ｜ 低 156.93 ｜ 昨收 125.53 → 收盘 165.05（+31.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-30，窗口结束前不做对错判定）

Options: P/C成交量 0.76 | OI比 0.51 | ATM IV 83.4% | Skew -5.7pp | Term 0.82 | ExpMove ±6.2%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-25（2D）±6.2% ｜ 11-27（4D）±0.3% ｜ 11-30（7D）±8.4% ｜ 12-02（9D）±9.6%
   ⇒ IV–VIX Spread: +56.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 247,178,058 | GEX Change vs 上次快照 -18,203,476 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1226 / LOW 176 / INVALID 988
结构观察区: NO_CROSS
Call Wall 170（弱结构｜现价低于该位 2.9%）
最近结构参考: Call Wall 170（现价低于该位 2.9%）
量化视角： 正 Gamma（2.47亿，无历史分位）｜正 Gamma 减弱（1820万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 137（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 170.0C — Vol 139,740 | 最新价 $9.05 | OI 149816→175759 (ΔOI +25943张) | ΔOI/Volume 18.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25943张（+17.3% vs前日OI），连续性待观察（方向未知）
12-18 160.0C — Vol 53,836 | 最新价 $14.02 | OI 28791→48554 (ΔOI +19763张) | ΔOI/Volume 36.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19763张（+68.6% vs前日OI），连续性待观察（方向未知）
11-27 150.0C — Vol 13,931 | 最新价 $16.75 | OI 4044→18002 (ΔOI +13958张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13958张（+345.1% vs前日OI），连续性待观察（方向未知）
11-27 140.0C — Vol 6,723 | 最新价 $24.70 | OI 612→13863 (ΔOI +13251张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13251张（+2165.2% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 72,915 张（Put 0 / Call 72,915），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-25  C +40.0k / P +37.7k ｜ Activity HIGH ｜ 2D
11-27  C +118.3k / P +82.8k ｜ Activity HIGH ｜ 4D
11-30  C +22.1k / P +7.1k ｜ Activity HIGH ｜ 7D
12-02  C +8.6k / P +2.0k ｜ Activity HIGH ｜ 9D

📆 11-25 Forward Structure
存量OI: C 98.9k / P 63.2k，今日变化ΔOI: C +40.0k / P +37.7k，平值价格ATM: C $5.20 / P $5.00 ｜ ATM IV 105.4%，净 delta 敞口 3.4M shares
Top ΔOI: C 150 +7,036
仓位参考: Max Pain 140 ｜ Call Wall 160（-3.1%，弱）（OI 10.7k）
量化解读： 存量 Call 重｜ATM IV 105.4%｜历史 Rank 93%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,409,672 股

📆 11-27 Forward Structure
存量OI: C 491.9k / P 269.6k，今日变化ΔOI: C +118.3k / P +82.8k，平值价格ATM: C $0.50 / P $0.00 ｜ ATM IV 95.1%，净 delta 敞口 11.1M shares
Top ΔOI: C 150 +13,958 ｜ C 140 +13,251
仓位参考: Max Pain 145 ｜ Call Wall 165（-0.0%，弱）（OI 34.0k） ｜ Put Wall 165（-0.0%，弱）（OI 15.4k）
量化解读： 存量 Call 重｜ATM IV 95.1%｜历史 Rank 93%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,055,862 股

📆 11-30 Forward Structure
存量OI: C 60.9k / P 25.5k，今日变化ΔOI: C +22.1k / P +7.1k，平值价格ATM: C $7.00 / P $6.90 ｜ ATM IV 75.8%，净 delta 敞口 1.8M shares
Top ΔOI: C 150 +8,040 ｜ C 147 +1,947
仓位参考: Max Pain 140 ｜ Call Wall 150（-9.1%）（OI 9.5k） ｜ Put Wall 150（-9.1%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 75.8%｜历史 Rank 93%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 1,823,596 股

📆 12-02 Forward Structure
存量OI: C 29.8k / P 7.1k，今日变化ΔOI: C +8.6k / P +2.0k，平值价格ATM: C $7.85 / P $8.05 ｜ ATM IV 76.8%，净 delta 敞口 592k shares
Top ΔOI: C 180 +1,224 ｜ C 150 +1,013 ｜ C 140 +971
仓位参考: Max Pain 140 ｜ Call Wall 160（-3.1%，弱）（OI 3.3k） ｜ Put Wall 150（-9.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 76.8%｜历史 Rank 93%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 591,980 股

📅 事件差分（观察，非因果）: 11-25（2D）ATM IV 105.4% vs 11-27 95.1%（差 +10.3pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location ? | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/NVDA_evening.json