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
🟡 **近现价集中开仓**: 11-04 77P ΔOI +5,353（距现价 -1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-04 77P ΔOI +5,353 占该期限总 OI 33.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 79.15 → 今开 78.94（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 79.05 ｜ 低 78.02

Options: P/C成交量 0.95 | OI比 0.80 | ATM IV 66.3% | Skew -1.3pp | Term 0.66 | ExpMove ±3.0%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-04（1D）±3.0% ｜ 11-06（3D）±5.4% ｜ 11-09（6D）±5.8% ｜ 11-11（8D）±4.6%
   ⇒ IV–VIX Spread: +45.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,834,324 | GEX Change vs 上次快照 -13,031,489 | Flip: Primary Flip: 76.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 483 / LOW 113 / INVALID 558
结构观察区: Primary Flip 76.82（全链重定价，覆盖 99%）
Call Wall 81（弱结构｜现价低于该位 3.6%）
最近结构参考: Flip 77（现价高于该位 1.6%）
量化视角： 正 Gamma（1483万，无历史分位）｜正 Gamma 减弱（1303万）｜现价位于 Flip 上方 1.64%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 78（MaxPain，仅结算参考）；上方 81（Call Wall，弱结构）。
• Gamma 区域：切换参考 77（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-04 77.0P — Vol 5,386 | 最新价 $0.54 | OI 81→5434 (ΔOI +5353张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5353张（+6608.6% vs前日OI），连续性待观察（方向未知）
11-04 84.0C — Vol 3,773 | 最新价 $0.12 | OI 242→2698 (ΔOI +2456张) | ΔOI/Volume 65.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2456张（+1014.9% vs前日OI），连续性待观察（方向未知）
11-11 85.0C — Vol 1,868 | 最新价 $0.60 | OI 14→1882 (ΔOI +1868张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1868张（+13342.9% vs前日OI），连续性待观察（方向未知）
11-06 80.0C — Vol 2,134 | 最新价 $1.54 | OI 1289→2498 (ΔOI +1209张) | ΔOI/Volume 56.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1209张（+93.8% vs前日OI），连续性待观察（方向未知）
11-06 78.0P — Vol 1,345 | 最新价 $1.23 | OI 558→1635 (ΔOI +1077张) | ΔOI/Volume 80.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1077张（+193.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,963 张（Put 6,430 / Call 5,533），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-04  C +3.4k / P +6.2k ｜ Activity HIGH ｜ 1D
11-06  C +3.6k / P +1.3k ｜ Activity MEDIUM △ ｜ 3D
11-09  C +0.4k / P +0.2k ｜ Activity MEDIUM △ ｜ 6D
11-11  C +1.9k / P -12 ｜ Activity HIGH ｜ 8D

📆 11-04 Forward Structure
存量OI: C 9.0k / P 7.2k，今日变化ΔOI: C +3.4k / P +6.2k，平值价格ATM: C $1.29 / P $1.03 ｜ ATM IV 66.3%，净 delta 敞口 -211k shares
Top ΔOI: P 77 +5,353 ｜ C 84 +2,456 ｜ P 78 +518
仓位参考: Max Pain 78 ｜ Call Wall 81（+3.7%，弱）（OI 2.7k） ｜ Put Wall 77（-1.4%）（OI 5.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.3%｜历史 Rank 97%（近端代理）｜IV/RV 1.58×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 211,416 股

11-06（MEDIUM △）Top ΔOI: 80C +1,209 ｜ 78P +1,077
11-06（MEDIUM △）仓位参考: Max Pain 78 ｜ Call Wall 81（+3.7%，弱）（OI 22.8k） ｜ Put Wall 75（-3.9%，弱）（OI 4.3k）

11-09（MEDIUM △）Top ΔOI: 84C +141 ｜ 85C +123
11-09（MEDIUM △）仓位参考: Max Pain 78 ｜ Call Wall 78（-0.1%，弱）（OI 0.1k） ｜ Put Wall 78（-0.1%，弱）（OI 80）

📆 11-11 Forward Structure
存量OI: C 2.5k / P 1.3k，今日变化ΔOI: C +1.9k / P -12，平值价格ATM: C $2.58 / P $1.03 ｜ ATM IV 48.2%，净 delta 敞口 29k shares
Top ΔOI: C 85 +1,868 ｜ C 77 +26 ｜ P 82 -19
仓位参考: Max Pain 78 ｜ Put Wall 77（-1.4%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 48.2%｜历史 Rank 97%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 29,014 股

📅 事件差分（观察，非因果）: 11-04（1D）ATM IV 66.3% vs 11-06 59.2%（差 +7.1pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/GDX_morning.json