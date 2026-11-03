# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $755.34 ｜ QQQ $685.28
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（3D）ATM IV 95.5% vs 11-13 77.8%（差 +17.7pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 137.83 → 今开 138.32（+0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 145.80 ｜ 低 137.89

Options: P/C成交量 0.41 | OI比 0.72 | ATM IV 95.5% | Skew 2.6pp | Term 0.73 | ExpMove ±7.2%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价中性（Skew 2.6pp）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±7.2% ｜ 11-13（10D）±11.5% ｜ 11-20（17D）±13.0% ｜ 11-27（24D）±15.0%
   ⇒ IV–VIX Spread: +74.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 15,357,132 | GEX Change vs 上次快照 6,563,543 | Flip: Primary Flip: 131.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 436 / LOW 152 / INVALID 262
结构观察区: Primary Flip 131.62（全链重定价，覆盖 100%）
最近结构参考: Flip 132（现价高于该位 9.8%）
量化视角： 正 Gamma（1536万，无历史分位）｜正 Gamma 增强（+656万）｜现价位于 Flip 上方 9.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 125.0P — Vol 3,086 | 最新价 $1.35 | OI 1028→3074 (ΔOI +2046张) | ΔOI/Volume 66.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2046张（+199.0% vs前日OI），连续性待观察（方向未知）
11-20 120.0P — Vol 1,809 | 最新价 $2.85 | OI 1323→2778 (ΔOI +1455张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1455张（+110.0% vs前日OI），连续性待观察（方向未知）
11-27 50.0P — Vol 803 | 最新价 $0.02 | OI 0→803 (ΔOI +803张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增803张（前日OI缺失），连续性待观察（方向未知）
11-20 45.0P — Vol 804 | 最新价 $0.02 | OI 27→828 (ΔOI +801张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增801张（+2966.7% vs前日OI），连续性待观察（方向未知）
11-06 160.0C — Vol 1,375 | 最新价 $0.41 | OI 856→1595 (ΔOI +739张) | ΔOI/Volume 53.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增739张（+86.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,844 张（Put 5,105 / Call 739），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +5.3k / P +2.8k ｜ Activity MEDIUM △ ｜ 3D
11-13  C +1.1k / P +0.6k ｜ Activity HIGH ｜ 10D
11-20  C -0.2k / P +2.2k ｜ Activity MEDIUM △ ｜ 17D
11-27  C +0.5k / P +1.6k ｜ Activity HIGH ｜ 24D

📆 11-06 Forward Structure
存量OI: C 67.9k / P 48.7k，今日变化ΔOI: C +5.3k / P +2.8k，平值价格ATM: C $4.97 / P $5.45 ｜ ATM IV 95.5%，净 delta 敞口 203k shares
Top ΔOI: P 125 +2,046 ｜ C 160 +739 ｜ C 157 +604
仓位参考: Max Pain 141 ｜ Call Wall 148（+2.4%，弱）（OI 8.4k）
量化解读： 存量 Call 重｜ATM IV 95.5%｜历史 Rank 84%（近端代理）｜IV/RV 1.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 202,958 股

📆 11-13 Forward Structure
存量OI: C 11.5k / P 18.3k，今日变化ΔOI: C +1.1k / P +0.6k，平值价格ATM: C $7.35 / P $9.25 ｜ ATM IV 77.8%，净 delta 敞口 44k shares
Top ΔOI: C 160 +236
仓位参考: Max Pain 160 ｜ Call Wall 150（+3.8%，弱）（OI 0.6k） ｜ Put Wall 155（+7.3%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.8%｜历史 Rank 84%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 43,774 股

11-20（MEDIUM △）Top ΔOI: 120P +1,455
11-20（MEDIUM △）仓位参考: Max Pain 170 ｜ Put Wall 140（-3.1%，弱）（OI 3.3k）

📆 11-27 Forward Structure
存量OI: C 3.5k / P 4.9k，今日变化ΔOI: C +0.5k / P +1.6k，平值价格ATM: C $10.50 / P $11.14 ｜ ATM IV 71.0%，净 delta 敞口 10k shares
仓位参考: Max Pain 155 ｜ Call Wall 155（+7.3%，弱）（OI 0.2k） ｜ Put Wall 140（-3.1%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 71.0%｜历史 Rank 84%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 正 9,558 股

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 95.5% vs 11-13 77.8%（差 +17.7pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/COIN_morning.json