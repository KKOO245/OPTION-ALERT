# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $769.11 ｜ QQQ $721.50
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 29.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 151P ΔOI +2,915（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-06 151P ΔOI +460 占该期限总 OI 12.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 153.24 → 今开 153.37（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 155.78 ｜ 低 153.13

Options: P/C成交量 0.48 | OI比 1.36 | ATM IV 39.9% | Skew 8.7pp | Term 0.82 | ExpMove ±2.7%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 8.7pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.36×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±2.7% ｜ 10-30（9D）±4.5% ｜ 11-06（16D）±6.1% ｜ 11-13（23D）±8.8%
   ⇒ IV–VIX Spread: +22.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,861,433 | GEX Change vs 上次快照 -10,388,973 | Flip: Primary Flip: 162.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 358 / LOW 80 / INVALID 336
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 162.66（全链重定价，覆盖 88%）
Call Wall 155（现价低于该位 0.6%）
最近结构参考: Call Wall 155（现价低于该位 0.6%）
量化视角： 负 Gamma（1486万，无历史分位）｜负 Gamma 加深（1039万）｜现价位于 Flip 下方 5.30%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 148（MaxPain，仅结算参考）；上方 155（Call Wall）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 151.0P — Vol 3,022 | 最新价 $0.78 | OI 95→3010 (ΔOI +2915张) | ΔOI/Volume 96.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2915张（+3068.4% vs前日OI），连续性待观察（方向未知）
10-30 148.0P — Vol 2,723 | 最新价 $1.42 | OI 177→2345 (ΔOI +2168张) | ΔOI/Volume 79.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2168张（+1224.9% vs前日OI），连续性待观察（方向未知）
10-23 152.0P — Vol 1,143 | 最新价 $1.44 | OI 18→1147 (ΔOI +1129张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1129张（+6272.2% vs前日OI），连续性待观察（方向未知）
11-20 160.0C — Vol 1,169 | 最新价 $3.14 | OI 911→1805 (ΔOI +894张) | ΔOI/Volume 76.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增894张（+98.1% vs前日OI），连续性待观察（方向未知）
10-30 145.0P — Vol 1,025 | 最新价 $0.88 | OI 379→1256 (ΔOI +877张) | ΔOI/Volume 85.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增877张（+231.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,983 张（Put 7,089 / Call 894），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C -1.7k / P +2.8k ｜ Activity MEDIUM △ ｜ 2D
10-30  C +0.9k / P +3.8k ｜ Activity MEDIUM △ ｜ 9D
11-06  C +22 / P +0.5k ｜ Activity MEDIUM △ ｜ 16D
11-13  C +0.1k / P -0.2k ｜ Activity MEDIUM △ ｜ 23D

📆 10-23 Forward Structure
存量OI: C 17.3k / P 23.6k，今日变化ΔOI: C -1.7k / P +2.8k，平值价格ATM: C $2.02 / P $2.15 ｜ ATM IV 39.9%，净 delta 敞口 -244k shares
Top ΔOI: P 151 +2,915 ｜ P 146 -1,155 ｜ P 152 +1,129
仓位参考: Max Pain 148 ｜ Call Wall 148（-3.9%，弱）（OI 3.0k） ｜ Put Wall 151（-2.0%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 39.9%｜历史 Rank 83%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 243,587 股

10-30（MEDIUM △）Top ΔOI: 148P +2,168 ｜ 145P +877
10-30（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 155（+0.6%）（OI 1.7k） ｜ Put Wall 150（-2.6%，弱）（OI 7.3k）

11-06（MEDIUM △）Top ΔOI: 151P +460 ｜ 154C -113
11-06（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 155（+0.6%）（OI 0.3k） ｜ Put Wall 151（-2.0%，弱）（OI 0.6k）

11-13（MEDIUM △）Top ΔOI: 140P -271 ｜ 160C +26
11-13（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 160（+3.9%，弱）（OI 45） ｜ Put Wall 153（-0.7%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/XBI_morning.json