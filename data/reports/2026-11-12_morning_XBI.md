# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $756.94 ｜ QQQ $685.63
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-13 148P ΔOI +1,722（距现价 -2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 148P ΔOI +1,722 占该期限总 OI 10.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 156.31 → 今开 154.35（-1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 154.42 ｜ 低 150.58

Options: P/C成交量 0.42 | OI比 1.43 | ATM IV 46.3% | Skew -3.3pp | Term 0.75 | ExpMove ±4.5%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.43×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±4.5% ｜ 11-20（8D）±6.1% ｜ 11-27（15D）±8.5% ｜ 12-04（22D）±0.0%
   ⇒ IV–VIX Spread: +27.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,119,585 | GEX Change vs 上次快照 -22,188,937 | Flip: Primary Flip: 153.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 483 / LOW 143 / INVALID 296
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 153.20（全链重定价，覆盖 96%）
最近结构参考: Flip 153（现价低于该位 1.1%）
量化视角： 负 Gamma（812万，无历史分位）｜由正转负（2219万）｜现价位于 Flip 下方 1.14%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 148.0P — Vol 1,898 | 最新价 $0.07 | OI 471→2193 (ΔOI +1722张) | ΔOI/Volume 90.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1722张（+365.6% vs前日OI），连续性待观察（方向未知）
11-13 145.0P — Vol 439 | 最新价 $0.07 | OI 106→529 (ΔOI +423张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增423张（+399.1% vs前日OI），连续性待观察（方向未知）
11-13 174.0C — Vol 178 | 最新价 $0.05 | OI 24→202 (ΔOI +178张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增178张（+741.7% vs前日OI），连续性待观察（方向未知）
11-13 162.5C — Vol 211 | 最新价 $0.25 | OI 114→280 (ΔOI +166张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增166张（+145.6% vs前日OI），连续性待观察（方向未知）
11-13 161.0C — Vol 145 | 最新价 $0.55 | OI 119→236 (ΔOI +117张) | ΔOI/Volume 80.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增117张（+98.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,606 张（Put 2,145 / Call 461），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.5k / P +2.1k ｜ Activity HIGH ｜ 1D
11-20  C -57 / P -0.4k ｜ Activity MEDIUM △ ｜ 8D
11-27  C +15 / P +8 ｜ Activity LOW ｜ 15D
12-04  C +12 / P -26 ｜ Activity MEDIUM △ ｜ 22D

📆 11-13 Forward Structure
存量OI: C 6.6k / P 9.5k，今日变化ΔOI: C +0.5k / P +2.1k，平值价格ATM: C $6.11 / P $0.75 ｜ ATM IV 46.3%，净 delta 敞口 -35k shares
Top ΔOI: P 148 +1,722 ｜ P 145 +423
仓位参考: Max Pain 150 ｜ Call Wall 160（+5.6%，弱）（OI 1.2k） ｜ Put Wall 148（-2.3%，弱）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 46.3%｜历史 Rank 95%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 34,583 股

11-20（MEDIUM △）Top ΔOI: 150P -243 ｜ 165C -106
11-20（MEDIUM △）仓位参考: Max Pain 154 ｜ Call Wall 160（+5.6%，弱）（OI 2.5k） ｜ Put Wall 145（-4.3%，弱）（OI 6.2k）

11-27（Activity LOW）仓位参考: Max Pain 158 ｜ Call Wall 152.5（+0.7%，弱）（OI 0.1k） ｜ Put Wall 156（+3.0%）（OI 0.2k）

12-04（MEDIUM △）Top ΔOI: 153P -13 ｜ 161P -13
12-04（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 161（+6.3%，弱）（OI 41） ｜ Put Wall 159（+5.0%，弱）（OI 80）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 46.3% vs 11-20 39.1%（差 +7.2pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/XBI_morning.json