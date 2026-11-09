# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $748.41 ｜ QQQ $674.64
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.1（fear）
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
🟡 **近现价集中开仓**: 11-20 150P ΔOI -6,806（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 101P ΔOI +120,790 占该期限总 OI 37.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 136.53 → 今开 138.58（+1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 144.60 ｜ 低 137.97

Options: P/C成交量 0.56 | OI比 2.02 | ATM IV 68.5% | Skew 9.9pp | Term 0.81 | ExpMove ±5.9%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 9.9pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.02×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±5.9% ｜ 11-20（11D）±10.2% ｜ 11-27（18D）±0.0% ｜ 12-04（25D）±0.0%
   ⇒ IV–VIX Spread: +47.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -75,944,169 | GEX Change vs 上次快照 -193,305 | Flip: Primary Flip: 158.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 533 / LOW 438 / INVALID 833
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 158.33（全链重定价，覆盖 100%）
最近结构参考: Flip 158（现价低于该位 9.7%）
量化视角： 负 Gamma（7594万，无历史分位）｜负 Gamma 加深（19万）｜现价位于 Flip 下方 9.69%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 153（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 158（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 101.67P — Vol 433,620 | 最新价 $0.27 | OI 434→121224 (ΔOI +120790张) | ΔOI/Volume 27.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增120790张（+27831.8% vs前日OI），连续性待观察（方向未知）
11-20 135.0P — Vol 13,212 | 最新价 $6.50 | OI 2818→7404 (ΔOI +4586张) | ΔOI/Volume 34.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4586张（+162.7% vs前日OI），连续性待观察（方向未知）
11-20 145.0C — Vol 5,354 | 最新价 $3.30 | OI 692→5153 (ΔOI +4461张) | ΔOI/Volume 83.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4461张（+644.6% vs前日OI），连续性待观察（方向未知）
11-20 150.0C — Vol 6,990 | 最新价 $1.98 | OI 637→4871 (ΔOI +4234张) | ΔOI/Volume 60.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4234张（+664.7% vs前日OI），连续性待观察（方向未知）
11-20 115.0P — Vol 4,861 | 最新价 $1.48 | OI 2696→6382 (ΔOI +3686张) | ΔOI/Volume 75.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3686张（+136.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 137,757 张（Put 129,062 / Call 8,695），跨 2 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +3.6k / P +87.7k ｜ Activity HIGH ｜ 4D
11-20  C +11.8k / P -16.1k ｜ Activity MEDIUM △ ｜ 11D
11-27  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
12-04  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 25D

📆 11-13 Forward Structure
存量OI: C 106.6k / P 215.5k，今日变化ΔOI: C +3.6k / P +87.7k，平值价格ATM: C $4.20 / P $4.20 ｜ ATM IV 68.5%，净 delta 敞口 229k shares
Top ΔOI: P 101 +120,790 ｜ P 125 -21,742 ｜ P 110 -16,610
仓位参考: Max Pain 153
量化解读： 存量 Put 重｜ATM IV 68.5%｜历史 Rank 96%（近端代理）｜IV/RV 0.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 228,622 股

11-20（MEDIUM △）Top ΔOI: 133P -11,368 ｜ 150P -6,806
11-20（MEDIUM △）仓位参考: Max Pain 163 ｜ Put Wall 150（+4.9%，弱）（OI 21.2k）

11-27（MEDIUM △）Top ΔOI: 150C +330 ｜ 130P +148
11-27（MEDIUM △）仓位参考: Max Pain 162 ｜ Put Wall 146.67（+2.6%，弱）（OI 3.2k）

12-04（MEDIUM △）Top ΔOI: 150C +242 ｜ 155C +131
12-04（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 150（+4.9%，弱）（OI 0.3k） ｜ Put Wall 148.33（+3.7%，弱）（OI 0.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/SOXX_morning.json