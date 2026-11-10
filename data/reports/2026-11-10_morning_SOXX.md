# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $751.28 ｜ QQQ $676.27
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（3D）ATM IV 80.8% vs 11-20 60.3%（差 +20.5pp），覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 146.76 → 今开 144.18（-1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 149.74 ｜ 低 143.13

Options: P/C成交量 1.79 | OI比 2.16 | ATM IV 80.8% | Skew 10.1pp | Term 0.64 | ExpMove ±7.0%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价显著（Skew 10.1pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.79×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.16×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±7.0% ｜ 11-20（10D）±8.2% ｜ 11-27（17D）±6.0% ｜ 12-04（24D）±0.0%
   ⇒ IV–VIX Spread: +60.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -40,354,039 | GEX Change vs 上次快照 35,469,343 | Flip: Primary Flip: 154.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 575 / LOW 414 / INVALID 815
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 154.43（全链重定价，覆盖 99%）
最近结构参考: Flip 154（现价低于该位 3.4%）
量化视角： 负 Gamma（4035万，无历史分位）｜负 Gamma 缓解（+3547万）｜现价位于 Flip 下方 3.44%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 153（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 154（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 105.0P — Vol 30,389 | 最新价 $0.10 | OI 457→30178 (ΔOI +29721张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29721张（+6503.5% vs前日OI），连续性待观察（方向未知）
11-20 140.0P — Vol 16,357 | 最新价 $3.47 | OI 766→15674 (ΔOI +14908张) | ΔOI/Volume 91.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14908张（+1946.2% vs前日OI），连续性待观察（方向未知）
11-20 125.0P — Vol 15,584 | 最新价 $0.85 | OI 7138→17689 (ΔOI +10551张) | ΔOI/Volume 67.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10551张（+147.8% vs前日OI），连续性待观察（方向未知）
11-20 153.33C — Vol 7,636 | 最新价 $3.20 | OI 317→7818 (ΔOI +7501张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7501张（+2366.2% vs前日OI），连续性待观察（方向未知）
11-20 160.0C — Vol 4,485 | 最新价 $1.45 | OI 3084→6617 (ΔOI +3533张) | ΔOI/Volume 78.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3533张（+114.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 66,214 张（Put 55,180 / Call 11,034），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +3.5k / P +22.5k ｜ Activity HIGH ｜ 3D
11-20  C +10.4k / P +2.0k ｜ Activity HIGH ｜ 10D
11-27  C +0.5k / P +1.1k ｜ Activity MEDIUM △ ｜ 17D
12-04  C +1.3k / P +51 ｜ Activity HIGH ｜ 24D

📆 11-13 Forward Structure
存量OI: C 110.1k / P 238.0k，今日变化ΔOI: C +3.5k / P +22.5k，平值价格ATM: C $3.50 / P $7.00 ｜ ATM IV 80.8%，净 delta 敞口 162k shares
Top ΔOI: P 105 +29,721 ｜ P 110 -9,468 ｜ P 138 -4,054
仓位参考: Max Pain 153
量化解读： 存量 Put 重｜ATM IV 80.8%｜历史 Rank 99%（近端代理）｜IV/RV 0.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 162,322 股

📆 11-20 Forward Structure
存量OI: C 199.5k / P 313.6k，今日变化ΔOI: C +10.4k / P +2.0k，平值价格ATM: C $6.45 / P $5.70 ｜ ATM IV 60.3%，净 delta 敞口 36k shares
Top ΔOI: P 140 +14,908 ｜ P 105 -12,672 ｜ P 120 -11,783
仓位参考: Max Pain 162 ｜ Call Wall 153.33（+2.8%，弱）（OI 7.8k） ｜ Put Wall 150（+0.6%，弱）（OI 21.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 60.3%｜历史 Rank 99%（近端代理）｜IV/RV 0.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,435 股

11-27（MEDIUM △）Top ΔOI: 127P +400 ｜ 142P +200
11-27（MEDIUM △）仓位参考: Max Pain 162 ｜ Put Wall 146.67（-1.6%，弱）（OI 3.2k）

📆 12-04 Forward Structure
存量OI: C 5.9k / P 7.9k，今日变化ΔOI: C +1.3k / P +51，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 51.6%，净 delta 敞口 38k shares
Top ΔOI: C 160 +748 ｜ C 148 +227
仓位参考: Max Pain 160 ｜ Call Wall 153.33（+2.8%，弱）（OI 0.3k） ｜ Put Wall 148.33（-0.5%，弱）（OI 0.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 51.6%｜历史 Rank 99%（近端代理）｜IV/RV 0.12×（近似）｜净 delta 敞口 正 38,258 股

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 80.8% vs 11-20 60.3%（差 +20.5pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/SOXX_morning.json