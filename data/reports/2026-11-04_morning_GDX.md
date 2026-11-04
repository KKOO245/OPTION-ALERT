# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.99 ｜ QQQ $691.95
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔵 **期限 OI 集中**: 11-09 83C ΔOI +271 占该期限总 OI 13.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 77.60 → 今开 81.92（+5.6%） | 较昨收变动（含盘初走势） ｜ 今日高 83.23 ｜ 低 81.56

Options: P/C成交量 0.23 | OI比 0.74 | ATM IV 66.3% | Skew -6.5pp | Term 0.61 | ExpMove ±3.5%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.61，近月 IV 高于远月）｜Put 保护异常便宜（Skew -6.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±3.5% ｜ 11-09（5D）±3.7% ｜ 11-11（7D）±2.2% ｜ 11-13（9D）±6.3%
   ⇒ IV–VIX Spread: +49.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 49,482,133 | GEX Change vs 上次快照 35,475,031 | Flip: Primary Flip: 77.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 508 / LOW 134 / INVALID 570
结构观察区: Primary Flip 77.18（全链重定价，覆盖 95%）
Call Wall 81（弱结构｜现价高于该位 2.0%）
最近结构参考: Call Wall 81（现价高于该位 2.0%）
量化视角： 正 Gamma（4948万，无历史分位）｜正 Gamma 增强（+3548万）｜现价位于 Flip 上方 7.08%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 78（MaxPain，仅结算参考） / 81（Call Wall，弱结构）。
• Gamma 区域：切换参考 77（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 70.0P — Vol 1,018 | 最新价 $0.83 | OI 888→1603 (ΔOI +715张) | ΔOI/Volume 70.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增715张（+80.5% vs前日OI），连续性待观察（方向未知）
11-20 75.0P — Vol 1,007 | 最新价 $1.84 | OI 12153→12845 (ΔOI +692张) | ΔOI/Volume 68.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增692张（+5.7% vs前日OI），连续性待观察（方向未知）
11-20 80.0C — Vol 968 | 最新价 $2.04 | OI 1386→1998 (ΔOI +612张) | ΔOI/Volume 63.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增612张（+44.2% vs前日OI），连续性待观察（方向未知）
11-06 78.0P — Vol 670 | 最新价 $1.70 | OI 1635→2076 (ΔOI +441张) | ΔOI/Volume 65.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增441张（+27.0% vs前日OI），连续性待观察（方向未知）
11-20 95.0C — Vol 482 | 最新价 $0.08 | OI 10636→11047 (ΔOI +411张) | ΔOI/Volume 85.3% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增411张（+3.9% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,871 张（Put 1,848 / Call 1,023），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 9.9k / P 7.3k，今日成交量: C 3.5k / P 0.8k，平值价格ATM: C $0.31 / P $1.04 ｜ ATM IV 66.3%，预期波动 ±1.6%，Max Pain 78
Top ΔOI: C 83 +281 ｜ P 75 +228 ｜ C 79 +178

📆 Forward Expiration Structure

11-06  C +1.3k / P +0.6k ｜ Activity HIGH ｜ 2D
11-09  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 5D
11-11  C +0.1k / P +68 ｜ Activity MEDIUM △ ｜ 7D
11-13  C +0.2k / P +0.5k ｜ Activity MEDIUM △ ｜ 9D

📆 11-06 Forward Structure
存量OI: C 95.0k / P 30.9k，今日变化ΔOI: C +1.3k / P +0.6k，平值价格ATM: C $1.63 / P $1.24 ｜ ATM IV 46.0%，净 delta 敞口 97k shares
Top ΔOI: P 78 +441 ｜ C 83 +350 ｜ C 82 +252
仓位参考: Max Pain 78 ｜ Call Wall 81（-2.0%，弱）（OI 22.7k） ｜ Put Wall 80（-3.2%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 46.0%｜历史 Rank 97%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 96,766 股

11-09（MEDIUM △）Top ΔOI: 83C +271 ｜ 82C +82
11-09（MEDIUM △）仓位参考: Max Pain 78 ｜ Call Wall 83（+0.4%）（OI 0.4k） ｜ Put Wall 78（-5.6%，弱）（OI 85）

11-11（MEDIUM △）Top ΔOI: 83C +62 ｜ 75P +25
11-11（MEDIUM △）仓位参考: Max Pain 78 ｜ Call Wall 85（+2.8%）（OI 1.9k）

11-13（MEDIUM △）Top ΔOI: 79P +220
11-13（MEDIUM △）仓位参考: Max Pain 82 ｜ Call Wall 84.5（+2.2%，弱）（OI 0.6k） ｜ Put Wall 80（-3.2%，弱）（OI 0.8k）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 46.0% vs 11-09 39.6%（差 +6.4pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/GDX_morning.json