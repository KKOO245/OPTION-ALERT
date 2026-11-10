# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $750.86 ｜ QQQ $674.76
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
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
🔵 **期限 OI 集中**: 11-11 96C ΔOI +2,704 占该期限总 OI 20.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 91.46 → 今开 88.02（-3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 88.99 ｜ 低 86.48

Options: P/C成交量 0.37 | OI比 0.37 | ATM IV 55.9% | Skew 7.8pp | Term 0.81 | ExpMove ±3.3%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 7.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.37）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.37×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-11（1D）±3.3% ｜ 11-13（3D）±4.2% ｜ 11-16（6D）±4.6% ｜ 11-18（8D）±6.5%
   ⇒ IV–VIX Spread: +36.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 62,131,171 | GEX Change vs 上次快照 -23,298,680 | Flip: Primary Flip: 84.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 604 / LOW 162 / INVALID 546
结构观察区: Primary Flip 84.15（全链重定价，覆盖 99%）
最近结构参考: Flip 84（现价高于该位 4.7%）
量化视角： 正 Gamma（6213万，无历史分位）｜正 Gamma 减弱（2330万）｜现价位于 Flip 上方 4.70%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 84（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-11 96.0C — Vol 3,755 | 最新价 $0.16 | OI 0→2704 (ΔOI +2704张) | ΔOI/Volume 72.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2704张（前日OI缺失），连续性待观察（方向未知）
11-20 70.0P — Vol 5,331 | 最新价 $0.03 | OI 24327→25336 (ΔOI +1009张) | ΔOI/Volume 18.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1009张（+4.2% vs前日OI），值得跟踪（方向未知）
11-27 97.0C — Vol 1,028 | 最新价 $1.60 | OI 43→1016 (ΔOI +973张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增973张（+2262.8% vs前日OI），连续性待观察（方向未知）
11-16 94.0C — Vol 846 | 最新价 $0.91 | OI 3→842 (ΔOI +839张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增839张（+27966.7% vs前日OI），连续性待观察（方向未知）
11-20 97.0C — Vol 973 | 最新价 $1.17 | OI 1848→2596 (ΔOI +748张) | ΔOI/Volume 76.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增748张（+40.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,273 张（Put 1,009 / Call 5,264），跨 4 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-11  C +4.3k / P +1.9k ｜ Activity HIGH ｜ 1D
11-13  C +1.1k / P +1.4k ｜ Activity HIGH ｜ 3D
11-16  C +1.1k / P +0.1k ｜ Activity HIGH ｜ 6D
11-18  C +0.2k / P +22 ｜ Activity MEDIUM △ ｜ 8D

📆 11-11 Forward Structure
存量OI: C 9.6k / P 3.6k，今日变化ΔOI: C +4.3k / P +1.9k，平值价格ATM: C $1.17 / P $1.72 ｜ ATM IV 55.9%，净 delta 敞口 -77k shares
Top ΔOI: C 96 +2,704 ｜ C 93 +433 ｜ P 89 +425
仓位参考: Max Pain 85 ｜ Call Wall 85（-3.5%，弱）（OI 2.2k） ｜ Put Wall 89（+1.0%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 55.9%｜历史 Rank 89%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 76,848 股

📆 11-13 Forward Structure
存量OI: C 81.9k / P 34.8k，今日变化ΔOI: C +1.1k / P +1.4k，平值价格ATM: C $1.88 / P $1.79 ｜ ATM IV 54.6%，净 delta 敞口 -73k shares
Top ΔOI: C 95 +654 ｜ P 87 +355 ｜ P 89 +297
仓位参考: Max Pain 84 ｜ Call Wall 88（-0.1%，弱）（OI 13.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 54.6%｜历史 Rank 89%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 73,082 股

📆 11-16 Forward Structure
存量OI: C 1.8k / P 0.7k，今日变化ΔOI: C +1.1k / P +0.1k，平值价格ATM: C $1.52 / P $2.50 ｜ ATM IV 47.0%，净 delta 敞口 15k shares
Top ΔOI: C 94 +839 ｜ C 91 +40
仓位参考: Max Pain 85 ｜ Call Wall 88（-0.1%，弱）（OI 0.2k） ｜ Put Wall 86（-2.4%，弱）（OI 92）
量化解读： 存量 Call 重｜ATM IV 47.0%｜历史 Rank 89%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,671 股

11-18（MEDIUM △）Top ΔOI: 92C +50 ｜ 95C +32
11-18（MEDIUM △）仓位参考: Max Pain 85 ｜ Call Wall 87（-1.3%）（OI 97） ｜ Put Wall 84（-4.7%）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/GDX_morning.json