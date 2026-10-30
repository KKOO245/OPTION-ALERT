# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 10-30（1D）ATM IV 50.2% vs 11-02 34.9%（差 +15.3pp），覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-02 80P ΔOI +56（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 83.95 → 今开 81.82（-2.5%） | 较昨收变动（含盘初走势） ｜ 今日高 81.75 ｜ 低 80.97

Options: P/C成交量 0.42 | OI比 0.25 | ATM IV 50.2% | Skew 6.8pp | Term 0.80 | ExpMove ±2.4%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 6.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.25×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.4% ｜ 11-02（4D）±2.8% ｜ 11-04（6D）±4.4% ｜ 11-06（8D）±5.6%
   ⇒ IV–VIX Spread: +33.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 54,660,260 | GEX Change vs 上次快照 -32,575,525 | Flip: Primary Flip: 79.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 508 / LOW 148 / INVALID 464
结构观察区: Primary Flip 79.69（全链重定价，覆盖 94%）
Put Wall 80（弱结构｜现价高于该位 2.0%） | Call Wall 85（弱结构｜现价低于该位 4.0%）
最近结构参考: Put Wall 80（现价高于该位 2.0%）
量化视角： 正 Gamma（5466万，无历史分位）｜正 Gamma 减弱（3258万）｜现价位于 Flip 上方 2.42%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构） / 81（MaxPain，仅结算参考）；上方 85（Call Wall，弱结构）。
• Gamma 区域：切换参考 80（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 85.0C — Vol 3,044 | 最新价 $0.79 | OI 28135→29756 (ΔOI +1621张) | ΔOI/Volume 53.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1621张（+5.8% vs前日OI），连续性待观察（方向未知）
11-06 95.0C — Vol 751 | 最新价 $0.16 | OI 398→1119 (ΔOI +721张) | ΔOI/Volume 96.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增721张（+181.2% vs前日OI），连续性待观察（方向未知）
10-30 80.0P — Vol 809 | 最新价 $0.16 | OI 1685→1955 (ΔOI +270张) | ΔOI/Volume 33.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增270张（+16.0% vs前日OI），连续性待观察（方向未知）
10-30 84.0C — Vol 472 | 最新价 $1.25 | OI 10208→10477 (ΔOI +269张) | ΔOI/Volume 57.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增269张（+2.6% vs前日OI），值得跟踪（方向未知）
11-13 78.0P — Vol 340 | 最新价 $0.90 | OI 393→633 (ΔOI +240张) | ΔOI/Volume 70.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增240张（+61.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,121 张（Put 510 / Call 2,611），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +1.6k / P +0.2k ｜ Activity MEDIUM △ ｜ 1D
11-02  C +0.1k / P +0.4k ｜ Activity MEDIUM △ ｜ 4D
11-04  C +17 / P +12 ｜ Activity LOW ｜ 6D
11-06  C +0.2k / P -22 ｜ Activity LOW ｜ 8D

📆 10-30 Forward Structure
存量OI: C 136.8k / P 33.9k，今日变化ΔOI: C +1.6k / P +0.2k，平值价格ATM: C $0.74 / P $1.23 ｜ ATM IV 50.2%，净 delta 敞口 18k shares
Top ΔOI: C 85 +1,621 ｜ C 87 -538 ｜ P 80 +270
仓位参考: Max Pain 81 ｜ Call Wall 85（+4.1%）（OI 29.8k） ｜ Put Wall 79（-3.2%，弱）（OI 3.7k）
量化解读： 存量 Call 重｜ATM IV 50.2%｜历史 Rank 82%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,236 股

11-02（MEDIUM △）Top ΔOI: 76P +150 ｜ 80P +56
11-02（MEDIUM △）仓位参考: Max Pain 84 ｜ Call Wall 86（+5.4%）（OI 0.8k） ｜ Put Wall 81（-0.8%，弱）（OI 0.3k）

11-04（Activity LOW）仓位参考: Max Pain 82 ｜ Call Wall 83（+1.7%，弱）（OI 0.2k） ｜ Put Wall 79（-3.2%）（OI 57）

11-06（Activity LOW）仓位参考: Max Pain 85 ｜ Call Wall 85（+4.1%）（OI 2.4k） ｜ Put Wall 80（-2.0%，弱）（OI 2.3k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 50.2% vs 11-02 34.9%（差 +15.3pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/GDX_morning.json