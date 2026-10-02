# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $763.99 ｜ QQQ $742.03
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 10-02（1D）ATM IV 48.0% vs 10-09 32.5%（差 +15.5pp），覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-02 163C ΔOI +416（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 140P ΔOI +576 占该期限总 OI 21.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 157.68 → 今开 156.99（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 159.08 ｜ 低 156.49

Options: P/C成交量 0.17 | OI比 2.13 | ATM IV 48.0% | Skew -6.5pp | Term 0.66 | ExpMove ±2.8%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.17×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.13×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.8% ｜ 10-09（8D）±4.3% ｜ 10-16（15D）±5.4% ｜ 10-23（22D）±5.4%
   ⇒ IV–VIX Spread: +30.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -37,174,507 | GEX Change vs 上次快照 -8,231,649 | Flip: Primary Flip: 163.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 363 / LOW 87 / INVALID 314
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.05（全链重定价，覆盖 92%）
Put Wall 150（现价高于该位 4.5%）
最近结构参考: Flip 163（现价低于该位 3.9%）
量化视角： 负 Gamma（3717万，无历史分位）｜负 Gamma 加深（823万）｜现价位于 Flip 下方 3.91%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 156（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 151.0P — Vol 849 | 最新价 $1.37 | OI 130→979 (ΔOI +849张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增849张（+653.1% vs前日OI），连续性待观察（方向未知）
10-23 140.0P — Vol 604 | 最新价 $0.42 | OI 66→642 (ΔOI +576张) | ΔOI/Volume 95.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增576张（+872.7% vs前日OI），连续性待观察（方向未知）
10-02 163.0C — Vol 422 | 最新价 $0.46 | OI 334→750 (ΔOI +416张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增416张（+124.5% vs前日OI），连续性待观察（方向未知）
10-02 166.0C — Vol 312 | 最新价 $0.10 | OI 92→273 (ΔOI +181张) | ΔOI/Volume 58.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增181张（+196.7% vs前日OI），连续性待观察（方向未知）
10-16 163.0C — Vol 188 | 最新价 $2.51 | OI 369→525 (ΔOI +156张) | ΔOI/Volume 83.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增156张（+42.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,178 张（Put 1,425 / Call 753），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.7k / P -5.9k ｜ Activity MEDIUM △ ｜ 1D
10-09  C +37 / P -0.2k ｜ Activity LOW ｜ 8D
10-16  C +0.5k / P +0.6k ｜ Activity MEDIUM △ ｜ 15D
10-23  C +22 / P +0.5k ｜ Activity HIGH ｜ 22D

📆 10-02 Forward Structure
存量OI: C 13.0k / P 27.6k，今日变化ΔOI: C +0.7k / P -5.9k，平值价格ATM: C $2.60 / P $1.71 ｜ ATM IV 48.0%，净 delta 敞口 33k shares
Top ΔOI: P 148 -3,900 ｜ P 145 -1,607 ｜ C 163 +416
仓位参考: Max Pain 156 ｜ Call Wall 162（+3.4%，弱）（OI 1.7k） ｜ Put Wall 148（-5.5%，弱）（OI 6.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.0%｜历史 Rank 96%（近端代理）｜IV/RV 1.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,403 股

10-09（Activity LOW）仓位参考: Max Pain 156 ｜ Call Wall 156（-0.4%，弱）（OI 0.2k） ｜ Put Wall 150（-4.3%，弱）（OI 0.4k）

10-16（MEDIUM △）Top ΔOI: 151P +849 ｜ 154P -334
10-16（MEDIUM △）仓位参考: Max Pain 162 ｜ Call Wall 165（+5.3%，弱）（OI 3.0k） ｜ Put Wall 150（-4.3%）（OI 22.5k）

📆 10-23 Forward Structure
存量OI: C 0.7k / P 2.0k，今日变化ΔOI: C +22 / P +0.5k，平值价格ATM: C $4.45 / P $3.97 ｜ ATM IV 31.9%，净 delta 敞口 -3k shares
Top ΔOI: P 145 -34
仓位参考: Max Pain 156 ｜ Call Wall 155（-1.1%，弱）（OI 78） ｜ Put Wall 153（-2.3%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 31.9%｜历史 Rank 96%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 负 3,450 股

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 48.0% vs 10-09 32.5%（差 +15.5pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/XBI_morning.json