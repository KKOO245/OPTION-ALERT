# 期权晨报 2026-11-13（快照 10:20 ET）

📊 市场环境

SPY $750.54 ｜ QQQ $673.40
VIX 19.65 ↑5.1%（5D -23.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔵 **期限 OI 集中**: 11-18 130P ΔOI +7,149 占该期限总 OI 18.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办（详情见今晚晚报）：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 139.94 → 今开 140.17（+0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 142.24 ｜ 低 137.45

Options: P/C成交量 0.47 | OI比 0.77 | ATM IV 95.0% | Skew -2.2pp | Term 0.62 | ExpMove ±5.0%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-16（3D）±5.0% ｜ 11-18（5D）±7.1% ｜ 11-20（7D）±8.5% ｜ 11-23（10D）±8.8%
   ⇒ IV–VIX Spread: +75.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 16,916,483 | GEX Change vs 上次快照 -14,941,764 | Flip: Primary Flip: 137.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 841 / LOW 279 / INVALID 484
结构观察区: Primary Flip 137.13（全链重定价，覆盖 99%）
Put Wall 130（弱结构｜现价高于该位 6.4%）
最近结构参考: Flip 137（现价高于该位 0.9%）
量化视角： 正 Gamma（1692万，无历史分位）｜正 Gamma 减弱（1494万）｜现价位于 Flip 上方 0.89%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（Put Wall，弱结构）；上方 140（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 170.0C — Vol 19,008 | 最新价 $0.41 | OI 30928→46320 (ΔOI +15392张) | ΔOI/Volume 81.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15392张（+49.8% vs前日OI），连续性待观察（方向未知）
11-27 165.0C — Vol 10,134 | 最新价 $0.99 | OI 6472→15953 (ΔOI +9481张) | ΔOI/Volume 93.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9481张（+146.5% vs前日OI），连续性待观察（方向未知）
11-20 175.0C — Vol 8,528 | 最新价 $0.31 | OI 12073→20063 (ΔOI +7990张) | ΔOI/Volume 93.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7990张（+66.2% vs前日OI），连续性待观察（方向未知）
11-18 130.0P — Vol 9,765 | 最新价 $1.66 | OI 417→7566 (ΔOI +7149张) | ΔOI/Volume 73.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7149张（+1714.4% vs前日OI），连续性待观察（方向未知）
11-13 140.0P — Vol 41,964 | 最新价 $2.43 | OI 6482→13520 (ΔOI +7038张) | ΔOI/Volume 16.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7038张（+108.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 47,050 张（Put 14,187 / Call 32,863），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 224.4k / P 173.8k，今日成交量: C 64.1k / P 30.0k，平值价格ATM: C $1.95 / P $0.99 ｜ ATM IV 95.0%，预期波动 ±2.1%，Max Pain 140
Top ΔOI: C 165 -7,621 ｜ P 140 +7,038 ｜ C 150 +3,711

📆 Forward Expiration Structure

11-16  C +8.3k / P +3.3k ｜ Activity HIGH ｜ 3D
11-18  C +3.1k / P +8.6k ｜ Activity HIGH ｜ 5D
11-20  C +33.9k / P +10.1k ｜ Activity MEDIUM △ ｜ 7D
11-23  C +0.3k / P +0.9k ｜ Activity HIGH ｜ 10D

📆 11-16 Forward Structure
存量OI: C 51.2k / P 12.2k，今日变化ΔOI: C +8.3k / P +3.3k，平值价格ATM: C $3.85 / P $3.07 ｜ ATM IV 66.9%，净 delta 敞口 8k shares
Top ΔOI: C 150 +1,564
仓位参考: Max Pain 140 ｜ Call Wall 150（+8.4%，弱）（OI 6.7k） ｜ Put Wall 140（+1.2%）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 66.9%｜历史 Rank 93%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,470 股

📆 11-18 Forward Structure
存量OI: C 14.0k / P 23.9k，今日变化ΔOI: C +3.1k / P +8.6k，平值价格ATM: C $5.15 / P $4.65 ｜ ATM IV 72.4%，净 delta 敞口 -193k shares
Top ΔOI: P 130 +7,149 ｜ C 150 +601
仓位参考: Max Pain 141 ｜ Call Wall 150（+8.4%，弱）（OI 1.6k） ｜ Put Wall 135（-2.4%，弱）（OI 9.9k）
量化解读： 存量 Put 重｜ATM IV 72.4%｜历史 Rank 93%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 193,397 股

11-20（MEDIUM △）Top ΔOI: 170C +15,392 ｜ 175C +7,990
11-20（MEDIUM △）仓位参考: Max Pain 145 ｜ Call Wall 145（+4.8%，弱）（OI 38.5k） ｜ Put Wall 130（-6.0%，弱）（OI 34.9k）

📆 11-23 Forward Structure
存量OI: C 3.6k / P 1.7k，今日变化ΔOI: C +0.3k / P +0.9k，平值价格ATM: C $7.25 / P $5.00 ｜ ATM IV 66.4%，净 delta 敞口 -28k shares
Top ΔOI: P 140 +244 ｜ P 125 +166 ｜ P 138 +163
仓位参考: Max Pain 141 ｜ Call Wall 150（+8.4%）（OI 1.1k） ｜ Put Wall 140（+1.2%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.4%｜历史 Rank 93%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 负 28,134 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/SPCX_morning.json