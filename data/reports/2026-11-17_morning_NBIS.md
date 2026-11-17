# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $734.92 ｜ QQQ $656.95
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（3D）ATM IV 153.3% vs 11-27 117.2%（差 +36.1pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-20 115C ΔOI +3,893（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 107.13 → 今开 108.93（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 111.90 ｜ 低 107.66

Options: P/C成交量 0.45 | OI比 0.59 | ATM IV 153.3% | Skew 6.6pp | Term 0.70 | ExpMove ±11.9%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 6.6pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（3D）±11.9% ｜ 11-27（10D）±15.2% ｜ 12-04（17D）±19.2% ｜ 12-11（24D）±25.0%
   ⇒ IV–VIX Spread: +130.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,803,727 | GEX Change vs 上次快照 4,056,445 | Flip: Primary Flip: 116.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 636 / LOW 62 / INVALID 108
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 116.85（全链重定价，覆盖 100%）
Put Wall 100（弱结构｜现价高于该位 10.4%）
最近结构参考: Flip 117（现价低于该位 5.5%）
量化视角： 负 Gamma（380万，无历史分位）｜负 Gamma 缓解（+406万）｜现价位于 Flip 下方 5.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall，弱结构）；上方 130（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 117（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 115.0C — Vol 6,724 | 最新价 $3.40 | OI 1340→5233 (ΔOI +3893张) | ΔOI/Volume 57.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3893张（+290.5% vs前日OI），连续性待观察（方向未知）
11-20 125.0C — Vol 5,357 | 最新价 $1.36 | OI 3950→7385 (ΔOI +3435张) | ΔOI/Volume 64.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3435张（+87.0% vs前日OI），连续性待观察（方向未知）
11-20 107.0P — Vol 3,725 | 最新价 $6.50 | OI 0→3137 (ΔOI +3137张) | ΔOI/Volume 84.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3137张（前日OI缺失），连续性待观察（方向未知）
12-18 80.0P — Vol 3,785 | 最新价 $3.80 | OI 2721→5698 (ΔOI +2977张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2977张（+109.4% vs前日OI），连续性待观察（方向未知）
11-27 150.0C — Vol 3,723 | 最新价 $0.45 | OI 3087→5054 (ΔOI +1967张) | ΔOI/Volume 52.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1967张（+63.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,409 张（Put 6,114 / Call 9,295），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +19.3k / P -3.9k ｜ Activity HIGH ｜ 3D
11-27  C +6.4k / P -0.3k ｜ Activity HIGH ｜ 10D
12-04  C +0.9k / P +0.1k ｜ Activity MEDIUM △ ｜ 17D
12-11  C +0.8k / P +0.5k ｜ Activity MEDIUM △ ｜ 24D

📆 11-20 Forward Structure
存量OI: C 187.7k / P 110.1k，今日变化ΔOI: C +19.3k / P -3.9k，平值价格ATM: C $7.15 / P $6.00 ｜ ATM IV 153.3%，净 delta 敞口 1.6M shares
Top ΔOI: C 115 +3,893 ｜ C 125 +3,435 ｜ P 107 +3,137
仓位参考: Max Pain 130 ｜ Call Wall 120（+8.7%，弱）（OI 5.6k） ｜ Put Wall 115（+4.2%，弱）（OI 9.9k）
量化解读： 存量 Call 重｜ATM IV 153.3%｜历史 Rank 92%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,589,872 股

📆 11-27 Forward Structure
存量OI: C 35.3k / P 18.7k，今日变化ΔOI: C +6.4k / P -0.3k，平值价格ATM: C $8.79 / P $8.04 ｜ ATM IV 117.2%，净 delta 敞口 237k shares
Top ΔOI: C 150 +1,967 ｜ C 107 +768 ｜ C 110 +754
仓位参考: Max Pain 132 ｜ Call Wall 110（-0.4%，弱）（OI 1.3k） ｜ Put Wall 100（-9.4%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 117.2%｜历史 Rank 92%（近端代理）｜IV/RV 0.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 237,133 股

12-04（MEDIUM △）Top ΔOI: 120C +106
12-04（MEDIUM △）仓位参考: Max Pain 130 ｜ Call Wall 120（+8.7%，弱）（OI 0.8k） ｜ Put Wall 100（-9.4%，弱）（OI 0.8k）

12-11（MEDIUM △）Top ΔOI: 120C +212 ｜ 90P +196
12-11（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 120（+8.7%，弱）（OI 0.5k） ｜ Put Wall 100（-9.4%，弱）（OI 1.3k）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 153.3% vs 11-27 117.2%（差 +36.1pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/NBIS_morning.json