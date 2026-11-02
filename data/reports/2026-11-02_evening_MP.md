# 期权晚报 2026-11-02（快照 16:40 ET）

📊 市场环境

SPY $752.10 ｜ QQQ $681.09
VIX 21.15 ↑8.9%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　⏰ 今日
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🔴 **事件差分**: 11-06（4D）ATM IV 99.9% vs 11-13 78.5%（差 +21.3pp），覆盖 ISM 制造业 PMI、Midterm Elections 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 38P ΔOI +559（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 40.19 → 收盘 38.35（-4.6%） ｜ 今日高 40.87 ｜ 低 38.13 ｜ 昨收 39.57 → 收盘 38.35（-3.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-09，窗口结束前不做对错判定）

Options: P/C成交量 0.25 | OI比 0.50 | ATM IV 99.9% | Skew -4.4pp | Term 0.66 | ExpMove ±8.5%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.25×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±8.5% ｜ 11-13（11D）±16.5% ｜ 11-20（18D）±12.9% ｜ 11-27（25D）±13.8%
   ⇒ IV–VIX Spread: +78.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,115,566 | GEX Change vs 上次快照 -1,280,471 | Flip: Primary Flip: 36.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 280 / LOW 33 / INVALID 155
结构观察区: Primary Flip 36.37（全链重定价，覆盖 100%）
Put Wall 35（弱结构｜现价高于该位 9.6%）
最近结构参考: Flip 36（现价高于该位 5.4%）
量化视角： 正 Gamma（112万，无历史分位）｜正 Gamma 减弱（128万）｜现价位于 Flip 上方 5.43%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall，弱结构）；上方 42（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 36（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 48.0C — Vol 14 | 最新价 $0.20 | OI 108→857 (ΔOI +749张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增749张（+693.5% vs前日OI），连续性待观察（方向未知）
11-06 38.0P — Vol 60 | 最新价 $1.39 | OI 862→1421 (ΔOI +559张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增559张（+64.8% vs前日OI），连续性待观察（方向未知）
11-06 45.0C — Vol 388 | 最新价 $0.19 | OI 1765→1971 (ΔOI +206张) | ΔOI/Volume 53.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增206张（+11.7% vs前日OI），连续性待观察（方向未知）
11-06 42.0C — Vol 253 | 最新价 $0.49 | OI 464→663 (ΔOI +199张) | ΔOI/Volume 78.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增199张（+42.9% vs前日OI），连续性待观察（方向未知）
11-13 39.0P — Vol 114 | 最新价 $2.35 | OI 497→625 (ΔOI +128张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增128张（+25.8% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,841 张（Put 687 / Call 1,154），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +1.0k / P +0.8k ｜ Activity HIGH ｜ 4D
11-13  C +0.8k / P +0.4k ｜ Activity HIGH ｜ 11D
11-20  C +29 / P +0.1k ｜ Activity MEDIUM △ ｜ 18D
11-27  C +71 / P +24 ｜ Activity MEDIUM △ ｜ 25D

📆 11-06 Forward Structure
存量OI: C 11.0k / P 5.5k，今日变化ΔOI: C +1.0k / P +0.8k，平值价格ATM: C $1.57 / P $1.70 ｜ ATM IV 99.9%，净 delta 敞口 -9k shares
Top ΔOI: P 38 +559 ｜ C 42 +199
仓位参考: Max Pain 42 ｜ Call Wall 42（+9.5%，弱）（OI 0.7k） ｜ Put Wall 38（-0.9%）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 99.9%｜历史 Rank 93%（近端代理）｜IV/RV 1.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,388 股

📆 11-13 Forward Structure
存量OI: C 4.8k / P 2.3k，今日变化ΔOI: C +0.8k / P +0.4k，平值价格ATM: C $4.54 / P $1.80 ｜ ATM IV 78.5%，净 delta 敞口 -8k shares
Top ΔOI: P 39 +128 ｜ P 35 +56
仓位参考: Max Pain 40 ｜ Call Wall 40（+4.3%，弱）（OI 0.8k） ｜ Put Wall 39（+1.7%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 78.5%｜历史 Rank 93%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,166 股

11-20（MEDIUM △）Top ΔOI: 38P +16 ｜ 37P +15
11-20（MEDIUM △）仓位参考: Max Pain 45 ｜ Call Wall 40（+4.3%，弱）（OI 0.9k） ｜ Put Wall 35（-8.7%，弱）（OI 1.7k）

11-27（MEDIUM △）仓位参考: Max Pain 44 ｜ Put Wall 38（-0.9%，弱）（OI 68）

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 99.9% vs 11-13 78.5%（差 +21.3pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/MP_evening.json