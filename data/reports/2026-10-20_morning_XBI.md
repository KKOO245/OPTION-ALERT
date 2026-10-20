# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $769.68 ｜ QQQ $718.15
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 146P ΔOI +1,802（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 147.86 → 今开 148.03（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 151.64 ｜ 低 147.76

Options: P/C成交量 0.23 | OI比 1.10 | ATM IV 41.0% | Skew 15.4pp | Term 0.80 | ExpMove ±5.8%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 15.4pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.10×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±5.8% ｜ 10-30（10D）±5.7% ｜ 11-06（17D）±7.9% ｜ 11-13（24D）±9.4%
   ⇒ IV–VIX Spread: +22.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -12,712,201 | GEX Change vs 上次快照 9,668,467 | Flip: Primary Flip: 163.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 350 / LOW 90 / INVALID 334
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.06（全链重定价，覆盖 91%）
Call Wall 155（现价低于该位 2.8%）
最近结构参考: Call Wall 155（现价低于该位 2.8%）
量化视角： 负 Gamma（1271万，无历史分位）｜负 Gamma 缓解（+967万）｜现价位于 Flip 下方 7.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 146（MaxPain，仅结算参考）；上方 155（Call Wall）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 146.0P — Vol 2,005 | 最新价 $1.31 | OI 270→2072 (ΔOI +1802张) | ΔOI/Volume 89.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1802张（+667.4% vs前日OI），连续性待观察（方向未知）
10-30 140.0P — Vol 3,080 | 最新价 $1.00 | OI 18780→19775 (ΔOI +995张) | ΔOI/Volume 32.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增995张（+5.3% vs前日OI），连续性待观察（方向未知）
10-23 155.0C — Vol 1,334 | 最新价 $0.25 | OI 1734→2501 (ΔOI +767张) | ΔOI/Volume 57.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增767张（+44.2% vs前日OI），连续性待观察（方向未知）
10-30 143.0P — Vol 713 | 最新价 $1.50 | OI 247→902 (ΔOI +655张) | ΔOI/Volume 91.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增655张（+265.2% vs前日OI），连续性待观察（方向未知）
10-23 156.0C — Vol 1,050 | 最新价 $0.17 | OI 100→744 (ΔOI +644张) | ΔOI/Volume 61.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增644张（+644.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,863 张（Put 3,452 / Call 1,411），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +1.6k / P +2.5k ｜ Activity MEDIUM △ ｜ 3D
10-30  C +0.6k / P +1.8k ｜ Activity MEDIUM △ ｜ 10D
11-06  C +0.1k / P +33 ｜ Activity MEDIUM △ ｜ 17D
11-13  C +95 / P +86 ｜ Activity MEDIUM △ ｜ 24D

📆 10-23 Forward Structure
存量OI: C 19.0k / P 20.8k，今日变化ΔOI: C +1.6k / P +2.5k，平值价格ATM: C $1.72 / P $6.99 ｜ ATM IV 41.0%，净 delta 敞口 -28k shares
Top ΔOI: P 146 +1,802 ｜ C 155 +767 ｜ C 156 +644
仓位参考: Max Pain 146 ｜ Call Wall 148（-1.8%，弱）（OI 3.0k） ｜ Put Wall 144（-4.4%，弱）（OI 3.1k）
量化解读： 存量两侧均衡｜ATM IV 41.0%｜历史 Rank 87%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 27,809 股

10-30（MEDIUM △）Top ΔOI: 140P +995 ｜ 143P +655
10-30（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 155（+2.9%）（OI 1.7k） ｜ Put Wall 150（-0.5%，弱）（OI 6.5k）

11-06（MEDIUM △）Top ΔOI: 140P +60 ｜ 159C +44
11-06（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 155（+2.9%，弱）（OI 0.3k） ｜ Put Wall 145（-3.8%，弱）（OI 0.4k）

11-13（MEDIUM △）Top ΔOI: 120C +59 ｜ 137P +32
11-13（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 154（+2.2%，弱）（OI 21） ｜ Put Wall 153（+1.5%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/XBI_morning.json