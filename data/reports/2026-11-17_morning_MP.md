# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $737.42 ｜ QQQ $nan
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🟡 **事件差分**: 11-20 ATM IV 84.3% vs 11-27 73.9%（差 +10.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🔵 **期限 OI 集中**: 12-11 50C ΔOI +695 占该期限总 OI 31.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 36.09 → 今开 36.75（+1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 37.09 ｜ 低 35.60

Options: P/C成交量 0.15 | OI比 0.47 | ATM IV 84.3% | Skew -0.2pp | Term 0.79 | ExpMove ±6.0%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.15×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（3D）±6.0% ｜ 11-27（10D）±9.8% ｜ 12-04（17D）±12.0% ｜ 12-11（24D）±15.9%
   ⇒ IV–VIX Spread: +61.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,830,721 | GEX Change vs 上次快照 555,667 | Flip: Primary Flip: 34.10（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 241 / LOW 71 / INVALID 126
结构观察区: Primary Flip 34.10（全链重定价，覆盖 100%）
Put Wall 35（现价高于该位 3.2%）
最近结构参考: Put Wall 35（现价高于该位 3.2%）
量化视角： 正 Gamma（383万，无历史分位）｜正 Gamma 增强（+56万）｜现价位于 Flip 上方 5.91%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 40（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 34（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 45.0C — Vol 855 | 最新价 $0.12 | OI 347→1151 (ΔOI +804张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增804张（+231.7% vs前日OI），连续性待观察（方向未知）
12-11 50.0C — Vol 695 | 最新价 $0.16 | OI 39→734 (ΔOI +695张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增695张（+1782.0% vs前日OI），连续性待观察（方向未知）
12-18 40.0C — Vol 1,278 | 最新价 $1.53 | OI 16729→17178 (ΔOI +449张) | ΔOI/Volume 35.1% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增449张（+2.7% vs前日OI），值得跟踪（方向未知）
11-20 38.5C — Vol 428 | 最新价 $0.49 | OI 193→583 (ΔOI +390张) | ΔOI/Volume 91.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增390张（+202.1% vs前日OI），连续性待观察（方向未知）
11-20 40.0C — Vol 726 | 最新价 $0.26 | OI 1989→2260 (ΔOI +271张) | ΔOI/Volume 37.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增271张（+13.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,609 张（Put 0 / Call 2,609），跨 4 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +1.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 3D
11-27  C +1.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 10D
12-04  C +53 / P +0.3k ｜ Activity MEDIUM △ ｜ 17D
12-11  C +0.7k / P +90 ｜ Activity HIGH ｜ 24D

📆 11-20 Forward Structure
存量OI: C 29.6k / P 14.0k，今日变化ΔOI: C +1.4k / P +0.2k，平值价格ATM: C $1.37 / P $0.80 ｜ ATM IV 84.3%，净 delta 敞口 32k shares
Top ΔOI: C 38 +390
仓位参考: Max Pain 40 ｜ Call Wall 39.5（+9.4%，弱）（OI 1.7k） ｜ Put Wall 35（-3.1%）（OI 4.0k）
量化解读： 存量 Call 重｜ATM IV 84.3%｜历史 Rank 78%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 31,937 股

11-27（MEDIUM △）Top ΔOI: 42P -142
11-27（MEDIUM △）仓位参考: Max Pain 40 ｜ Put Wall 33（-8.6%）（OI 2.5k）

12-04（MEDIUM △）Top ΔOI: 42P +232 ｜ 36P +27
12-04（MEDIUM △）仓位参考: Max Pain 39 ｜ Call Wall 35（-3.1%）（OI 0.5k） ｜ Put Wall 34（-5.8%，弱）（OI 0.2k）

📆 12-11 Forward Structure
存量OI: C 1.4k / P 0.8k，今日变化ΔOI: C +0.7k / P +90，平值价格ATM: C $3.40 / P $2.36 ｜ ATM IV 67.7%，净 delta 敞口 284 shares
Top ΔOI: P 34 +12
仓位参考: Max Pain 42 ｜ Put Wall 34（-5.8%，弱）（OI 42）
量化解读： 存量 Call 重｜ATM IV 67.7%｜历史 Rank 78%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 正 284 股

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 84.3% vs 11-27 73.9%（差 +10.4pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/MP_morning.json