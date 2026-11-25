# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $701.98 ｜ QQQ $610.77
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 153P ΔOI +2,854（距现价 +0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 153P ΔOI +2,854 占该期限总 OI 13.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 156.82 → 今开 154.54（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 155.30 ｜ 低 151.38

Options: P/C成交量 0.65 | OI比 1.98 | ATM IV 39.7% | Skew 9.6pp | Term 0.95 | ExpMove ±2.1%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构正常（Term 0.95）｜保护溢价显著（Skew 9.6pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.98×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±2.1% ｜ 12-04（9D）±6.5% ｜ 12-11（16D）±4.5% ｜ 12-18（23D）±8.1%
   ⇒ IV–VIX Spread: +8.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -3,268,558 | GEX Change vs 上次快照 -21,831,399 | Flip: Primary Flip: 153.50（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 389 / LOW 142 / INVALID 381
结构观察区: Primary Flip 153.50（全链重定价，覆盖 95%）
最近结构参考: Flip 154（现价低于该位 0.7%）
量化视角： 负 Gamma（327万，无历史分位）｜由正转负（2183万）｜现价位于 Flip 下方 0.70%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 154（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 175.0C — Vol 11,052 | 最新价 $0.85 | OI 30760→40767 (ΔOI +10007张) | ΔOI/Volume 90.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10007张（+32.5% vs前日OI），连续性待观察（方向未知）
12-11 142.0P — Vol 6 | 最新价 $0.90 | OI 15→4004 (ΔOI +3989张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3989张（+26593.3% vs前日OI），连续性待观察（方向未知）
12-18 140.0P — Vol 6,032 | 最新价 $1.08 | OI 4189→7727 (ΔOI +3538张) | ΔOI/Volume 58.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3538张（+84.5% vs前日OI），连续性待观察（方向未知）
11-27 153.0P — Vol 3,191 | 最新价 $0.95 | OI 33→2887 (ΔOI +2854张) | ΔOI/Volume 89.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2854张（+8648.5% vs前日OI），连续性待观察（方向未知）
11-27 152.0P — Vol 2,715 | 最新价 $0.63 | OI 18→2675 (ΔOI +2657张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2657张（+14761.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 23,045 张（Put 13,038 / Call 10,007），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +1.5k / P +7.6k ｜ Activity HIGH ｜ 2D
12-04  C +0.9k / P +3.8k ｜ Activity HIGH ｜ 9D
12-11  C +1.7k / P +15.6k ｜ Activity HIGH ｜ 16D
12-18  C +12.3k / P +10.0k ｜ Activity MEDIUM △ ｜ 23D

📆 11-27 Forward Structure
存量OI: C 7.1k / P 14.2k，今日变化ΔOI: C +1.5k / P +7.6k，平值价格ATM: C $1.70 / P $1.50 ｜ ATM IV 39.7%，净 delta 敞口 -246k shares
Top ΔOI: P 153 +2,854 ｜ P 152 +2,657 ｜ P 142 +526
仓位参考: Max Pain 152 ｜ Call Wall 152（-0.3%，弱）（OI 0.6k） ｜ Put Wall 153（+0.4%，弱）（OI 2.9k）
量化解读： 存量 Put 重｜ATM IV 39.7%｜历史 Rank 80%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 负 245,943 股

📆 12-04 Forward Structure
存量OI: C 1.7k / P 17.7k，今日变化ΔOI: C +0.9k / P +3.8k，平值价格ATM: C $6.34 / P $3.65 ｜ ATM IV 42.2%，净 delta 敞口 -112k shares
Top ΔOI: P 146 +1,995 ｜ P 147 +1,955 ｜ P 138 -1,022
仓位参考: Max Pain 154 ｜ Call Wall 157.5（+3.3%，弱）（OI 0.2k） ｜ Put Wall 146（-4.2%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 42.2%｜历史 Rank 80%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 111,723 股

📆 12-11 Forward Structure
存量OI: C 2.9k / P 16.8k，今日变化ΔOI: C +1.7k / P +15.6k，平值价格ATM: C $3.30 / P $3.55 ｜ ATM IV 39.7%，净 delta 敞口 -185k shares
Top ΔOI: P 142 +3,989 ｜ P 133 +2,086 ｜ P 141 +2,001
仓位参考: Max Pain 150 ｜ Call Wall 147（-3.6%，弱）（OI 1.0k） ｜ Put Wall 150（-1.6%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 39.7%｜历史 Rank 80%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 负 184,905 股

12-18（MEDIUM △）Top ΔOI: 175C +10,007 ｜ 140P +3,538
12-18（MEDIUM △）仓位参考: Max Pain 140

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/XBI_morning.json