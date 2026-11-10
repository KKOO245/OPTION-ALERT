# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（4D）ATM IV 203.7% vs 11-20 150.0%（差 +53.7pp），覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 135P ΔOI +688（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 129.49 → 今开 131.15（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 139.33 ｜ 低 128.51

Options: P/C成交量 0.59 | OI比 0.58 | ATM IV 203.7% | Skew 15.4pp | Term 0.58 | ExpMove ±17.4%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.58，近月 IV 高于远月）｜保护溢价显著（Skew 15.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±17.4% ｜ 11-20（11D）±21.6% ｜ 11-27（18D）±11.3% ｜ 12-04（25D）±25.0%
   ⇒ IV–VIX Spread: +182.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,115,663 | GEX Change vs 上次快照 1,124,992 | Flip: Primary Flip: 144.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 583 / LOW 49 / INVALID 248
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 144.81（全链重定价，覆盖 100%）
Put Wall 150（弱结构｜现价低于该位 8.9%）
最近结构参考: Flip 145（现价低于该位 5.6%）
量化视角： 负 Gamma（312万，无历史分位）｜负 Gamma 缓解（+112万）｜现价位于 Flip 下方 5.63%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall，弱结构） / 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 145（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 187.5C — Vol 2,510 | 最新价 $0.80 | OI 210→2639 (ΔOI +2429张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2429张（+1156.7% vs前日OI），连续性待观察（方向未知）
11-13 145.0C — Vol 1,839 | 最新价 $6.50 | OI 286→1420 (ΔOI +1134张) | ΔOI/Volume 61.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1134张（+396.5% vs前日OI），连续性待观察（方向未知）
11-13 114.0P — Vol 964 | 最新价 $6.20 | OI 120→927 (ΔOI +807张) | ΔOI/Volume 83.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增807张（+672.5% vs前日OI），连续性待观察（方向未知）
11-13 140.0C — Vol 1,619 | 最新价 $7.85 | OI 483→1287 (ΔOI +804张) | ΔOI/Volume 49.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增804张（+166.5% vs前日OI），连续性待观察（方向未知）
11-13 60.0P — Vol 877 | 最新价 $0.10 | OI 0→777 (ΔOI +777张) | ΔOI/Volume 88.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增777张（前日OI缺失），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,951 张（Put 1,584 / Call 4,367），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +8.5k / P +5.2k ｜ Activity HIGH ｜ 4D
11-20  C -2.3k / P +0.2k ｜ Activity HIGH ｜ 11D
11-27  C +0.8k / P +0.1k ｜ Activity MEDIUM △ ｜ 18D
12-04  C +0.4k / P +0.7k ｜ Activity HIGH ｜ 25D

📆 11-13 Forward Structure
存量OI: C 59.9k / P 34.5k，今日变化ΔOI: C +8.5k / P +5.2k，平值价格ATM: C $11.45 / P $12.30 ｜ ATM IV 203.7%，净 delta 敞口 151k shares
Top ΔOI: C 187 +2,429 ｜ C 145 +1,134 ｜ P 114 +807
仓位参考: Max Pain 155 ｜ Call Wall 150（+9.8%，弱）（OI 2.5k） ｜ Put Wall 130（-4.9%）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 203.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 151,052 股

📆 11-20 Forward Structure
存量OI: C 117.0k / P 110.8k，今日变化ΔOI: C -2.3k / P +0.2k，平值价格ATM: C $14.70 / P $14.80 ｜ ATM IV 150.0%，净 delta 敞口 42k shares
Top ΔOI: C 210 -3,002 ｜ P 135 +688
仓位参考: Max Pain 175 ｜ Put Wall 150（+9.8%，弱）（OI 6.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 150.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 42,231 股

11-27（MEDIUM △）Top ΔOI: 180C +304 ｜ 170C +215
11-27（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 150（+9.8%，弱）（OI 0.9k） ｜ Put Wall 150（+9.8%，弱）（OI 0.7k）

📆 12-04 Forward Structure
存量OI: C 3.4k / P 4.7k，今日变化ΔOI: C +0.4k / P +0.7k，平值价格ATM: C $18.00 / P $16.18 ｜ ATM IV 121.9%，净 delta 敞口 -10k shares
Top ΔOI: P 115 +373 ｜ C 150 +155
仓位参考: Max Pain 155 ｜ Call Wall 150（+9.8%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 121.9%｜历史 Rank 100%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 负 9,617 股

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 203.7% vs 11-20 150.0%（差 +53.7pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/NBIS_morning.json