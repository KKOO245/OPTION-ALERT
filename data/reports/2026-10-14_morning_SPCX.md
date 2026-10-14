# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $769.08 ｜ QQQ $728.95
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.4（fear）
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
🟡 **事件差分**: 10-16 ATM IV 54.5% vs 10-19 42.9%（差 +11.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 157C ΔOI +4,473（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 156.54 → 今开 154.96（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 155.44 ｜ 低 151.99

Options: P/C成交量 0.73 | OI比 0.47 | ATM IV 67.8% | Skew 1.9pp | Term 0.77 | ExpMove ±3.5%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±3.5% ｜ 10-19（5D）±4.2% ｜ 10-21（7D）±4.9% ｜ 10-23（9D）±5.8%
   ⇒ IV–VIX Spread: +51.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 6,735,054 | GEX Change vs 上次快照 2,781,922 | Flip: Primary Flip: 152.83（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 747 / LOW 182 / INVALID 547
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 152.83（全链重定价，覆盖 96%）
最近结构参考: Flip 153（现价高于该位 0.3%）
量化视角： 正 Gamma（674万，无历史分位）｜正 Gamma 增强（+278万）｜现价位于 Flip 上方 0.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 160（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 190.0C — Vol 21,188 | 最新价 $0.37 | OI 30885→42494 (ΔOI +11609张) | ΔOI/Volume 54.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11609张（+37.6% vs前日OI），连续性待观察（方向未知）
10-16 165.0C — Vol 38,420 | 最新价 $0.55 | OI 22709→33087 (ΔOI +10378张) | ΔOI/Volume 27.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10378张（+45.7% vs前日OI），连续性待观察（方向未知）
10-14 160.0C — Vol 55,315 | 最新价 $0.60 | OI 941→10851 (ΔOI +9910张) | ΔOI/Volume 17.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9910张（+1053.1% vs前日OI），连续性待观察（方向未知）
10-14 165.0C — Vol 25,223 | 最新价 $0.12 | OI 4096→10063 (ΔOI +5967张) | ΔOI/Volume 23.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5967张（+145.7% vs前日OI），连续性待观察（方向未知）
10-14 162.5C — Vol 27,200 | 最新价 $0.26 | OI 3430→8616 (ΔOI +5186张) | ΔOI/Volume 19.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5186张（+151.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 43,050 张（Put 0 / Call 43,050），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 60.6k / P 28.2k，今日成交量: C 50.8k / P 37.2k，平值价格ATM: C $1.56 / P $0.77 ｜ ATM IV 67.8%，预期波动 ±1.5%，Max Pain 160
Top ΔOI: C 160 +9,910 ｜ C 165 +5,967 ｜ C 162 +5,186

📆 Forward Expiration Structure

10-16  C +11.5k / P -0.3k ｜ Activity HIGH ｜ 2D
10-19  C +10.9k / P +3.3k ｜ Activity HIGH ｜ 5D
10-21  C +5.8k / P +2.9k ｜ Activity HIGH ｜ 7D
10-23  C +9.5k / P +5.4k ｜ Activity HIGH ｜ 9D

📆 10-16 Forward Structure
存量OI: C 409.3k / P 414.6k，今日变化ΔOI: C +11.5k / P -0.3k，平值价格ATM: C $3.19 / P $2.13 ｜ ATM IV 54.5%，净 delta 敞口 527k shares
Top ΔOI: C 165 +10,378 ｜ C 157 +4,473
仓位参考: Max Pain 150 ｜ Call Wall 165（+7.6%，弱）（OI 33.1k） ｜ Put Wall 150（-2.2%，弱）（OI 25.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 54.5%｜历史 Rank 88%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 526,634 股

📆 10-19 Forward Structure
存量OI: C 26.3k / P 9.2k，今日变化ΔOI: C +10.9k / P +3.3k，平值价格ATM: C $3.71 / P $2.67 ｜ ATM IV 42.9%，净 delta 敞口 9k shares
Top ΔOI: C 157 +2,552 ｜ C 162 +2,296
仓位参考: Max Pain 160 ｜ Call Wall 157.5（+2.7%，弱）（OI 2.6k） ｜ Put Wall 162.5（+6.0%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 42.9%｜历史 Rank 88%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 8,824 股

📆 10-21 Forward Structure
存量OI: C 10.2k / P 5.5k，今日变化ΔOI: C +5.8k / P +2.9k，平值价格ATM: C $4.15 / P $3.30 ｜ ATM IV 44.2%，净 delta 敞口 5k shares
Top ΔOI: C 162 +1,686 ｜ P 147 +1,416
仓位参考: Max Pain 160 ｜ Call Wall 162.5（+6.0%，弱）（OI 1.8k） ｜ Put Wall 147（-4.1%）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 44.2%｜历史 Rank 88%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 5,011 股

📆 10-23 Forward Structure
存量OI: C 56.6k / P 65.7k，今日变化ΔOI: C +9.5k / P +5.4k，平值价格ATM: C $4.85 / P $4.04 ｜ ATM IV 46.6%，净 delta 敞口 -58k shares
Top ΔOI: C 160 +2,377 ｜ C 165 +1,736 ｜ P 200 +1,575
仓位参考: Max Pain 158 ｜ Call Wall 165（+7.6%，弱）（OI 5.3k） ｜ Put Wall 140（-8.7%，弱）（OI 6.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.6%｜历史 Rank 88%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 负 57,590 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 54.5% vs 10-19 42.9%（差 +11.6pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/SPCX_morning.json