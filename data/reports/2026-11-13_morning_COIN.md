# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.80 ｜ QQQ $679.89
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 134C ΔOI +8,445（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 130.67 → 今开 127.28（-2.6%） | 较昨收变动（含盘初走势） ｜ 今日高 130.60 ｜ 低 126.57

Options: P/C成交量 0.16 | OI比 0.46 | ATM IV 99.8% | Skew 0.9pp | Term 0.70 | ExpMove ±8.3%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价薄（Skew 0.9pp）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.16×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±8.3% ｜ 11-27（14D）±10.8% ｜ 12-04（21D）±13.3% ｜ 12-11（28D）±15.0%
   ⇒ IV–VIX Spread: +80.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 5,597,508 | GEX Change vs 上次快照 5,873,427 | Flip: Primary Flip: 125.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 380 / LOW 222 / INVALID 390
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 125.59（全链重定价，覆盖 89%）
Call Wall 140（弱结构｜现价低于该位 8.7%）
最近结构参考: Flip 126（现价高于该位 1.8%）
量化视角： 正 Gamma（560万，无历史分位）｜由负转正（+587万）｜现价位于 Flip 上方 1.76%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 135（MaxPain，仅结算参考） / 140（Call Wall，弱结构）。
• Gamma 区域：切换参考 126（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 139.0C — Vol 9,159 | 最新价 $2.46 | OI 135→8895 (ΔOI +8760张) | ΔOI/Volume 95.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8760张（+6488.9% vs前日OI），连续性待观察（方向未知）
11-20 134.0C — Vol 8,562 | 最新价 $4.08 | OI 46→8491 (ΔOI +8445张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8445张（+18358.7% vs前日OI），连续性待观察（方向未知）
11-20 127.0P — Vol 1,046 | 最新价 $3.73 | OI 74→860 (ΔOI +786张) | ΔOI/Volume 75.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增786张（+1062.2% vs前日OI），连续性待观察（方向未知）
11-13 135.0C — Vol 2,341 | 最新价 $0.72 | OI 959→1735 (ΔOI +776张) | ΔOI/Volume 33.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增776张（+80.9% vs前日OI），连续性待观察（方向未知）
11-20 122.0P — Vol 781 | 最新价 $2.11 | OI 577→1134 (ΔOI +557张) | ΔOI/Volume 71.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增557张（+96.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,324 张（Put 1,343 / Call 17,981），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 71.9k / P 33.0k，今日成交量: C 21.6k / P 3.5k，平值价格ATM: C $1.29 / P $1.48 ｜ ATM IV 99.8%，预期波动 ±2.2%，Max Pain 135
Top ΔOI: C 140 -2,148 ｜ P 155 -2,014 ｜ C 146 -868

📆 Forward Expiration Structure

11-20  C +19.2k / P -2.9k ｜ Activity HIGH ｜ 7D
11-27  C +0.8k / P +13 ｜ Activity MEDIUM △ ｜ 14D
12-04  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 21D
12-11  C +0.3k / P -55 ｜ Activity MEDIUM △ ｜ 28D

📆 11-20 Forward Structure
存量OI: C 104.6k / P 59.0k，今日变化ΔOI: C +19.2k / P -2.9k，平值价格ATM: C $5.00 / P $5.60 ｜ ATM IV 72.2%，净 delta 敞口 1.0M shares
Top ΔOI: C 139 +8,760 ｜ C 134 +8,445 ｜ P 175 -2,163
仓位参考: Max Pain 139 ｜ Call Wall 139（+8.8%，弱）（OI 8.9k） ｜ Put Wall 120（-6.1%）（OI 7.4k）
量化解读： 存量 Call 重｜ATM IV 72.2%｜历史 Rank 86%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,007,094 股

11-27（MEDIUM △）Top ΔOI: 138C +219 ｜ 133P +106
11-27（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 140（+9.5%，弱）（OI 0.4k） ｜ Put Wall 120（-6.1%，弱）（OI 0.6k）

📆 12-04 Forward Structure
存量OI: C 5.6k / P 8.7k，今日变化ΔOI: C +0.4k / P +0.4k，平值价格ATM: C $8.20 / P $8.79 ｜ ATM IV 68.6%，净 delta 敞口 -7k shares
Top ΔOI: C 140 +117
仓位参考: Max Pain 140 ｜ Call Wall 140（+9.5%）（OI 1.5k） ｜ Put Wall 135（+5.6%）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 68.6%｜历史 Rank 86%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 负 7,268 股

12-11（MEDIUM △）Top ΔOI: 135C +130 ｜ 130C +39
12-11（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 135（+5.6%）（OI 0.4k） ｜ Put Wall 135（+5.6%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/COIN_morning.json