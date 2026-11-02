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
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 11.80 → 收盘 10.96（-7.1%） ｜ 今日高 12.14 ｜ 低 10.88 ｜ 昨收 11.65 → 收盘 10.96（-5.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-05，窗口结束前不做对错判定）

Options: P/C成交量 0.29 | OI比 0.65 | ATM IV 91.8% | Skew -3.5pp | Term 0.83 | ExpMove ±7.5%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±7.5% ｜ 11-13（11D）±11.2% ｜ 11-20（18D）±27.8% ｜ 11-27（25D）±29.6%
   ⇒ IV–VIX Spread: +70.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -91,911 | GEX Change vs 上次快照 194,839 | Flip: Primary Flip: 11.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 90 / LOW 73 / INVALID 237
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 11.42（全链重定价，覆盖 91%）
Put Wall 12（弱结构｜现价低于该位 8.7%）
最近结构参考: Flip 11（现价低于该位 4.0%）
量化视角： 负 Gamma（9万，无历史分位）｜负 Gamma 缓解（+19万）｜现价位于 Flip 下方 4.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 12（Put Wall，弱结构） / 13（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 9.0P — Vol 156（Yahoo补） | 最新价 $0.10 | OI 15→171 (ΔOI +156张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增156张（+1040.0% vs前日OI），连续性待观察（方向未知）
11-06 11.5C — Vol 74 | 最新价 $0.23 | OI 33→154 (ΔOI +121张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增121张（+366.7% vs前日OI），值得跟踪（方向未知）
11-06 11.5P — Vol 52 | 最新价 $0.60 | OI 278→379 (ΔOI +101张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增101张（+36.3% vs前日OI），值得跟踪（方向未知）
11-13 13.0P — Vol 6 | 最新价 $1.89 | OI 68→140 (ΔOI +72张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增72张（+105.9% vs前日OI），值得跟踪（方向未知）
11-06 12.0C — Vol 146 | 最新价 $0.10 | OI 24→94 (ΔOI +70张) | ΔOI/Volume 48.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增70张（+291.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 520 张（Put 329 / Call 191），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.2k / P +0.2k ｜ Activity HIGH ｜ 4D
11-13  C +11 / P +89 ｜ Activity MEDIUM △ ｜ 11D
11-20  C -22 / P +0.2k ｜ Activity HIGH ｜ 18D
11-27  C +55 / P +55 ｜ Activity MEDIUM △ ｜ 25D

📆 11-06 Forward Structure
存量OI: C 2.5k / P 1.6k，今日变化ΔOI: C +0.2k / P +0.2k，平值价格ATM: C $0.40 / P $0.42 ｜ ATM IV 91.8%，净 delta 敞口 -10k shares
Top ΔOI: C 11 +121 ｜ P 11 +101 ｜ C 12 +70
仓位参考: Max Pain 13 ｜ Put Wall 11.5（+4.9%）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 91.8%｜历史 Rank 29%（近端代理）｜IV/RV 1.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,875 股

11-13（MEDIUM △）Top ΔOI: 11P +9
11-13（MEDIUM △）仓位参考: Max Pain 14 ｜ Put Wall 11（+0.4%，弱）（OI 64）

📆 11-20 Forward Structure
存量OI: C 4.1k / P 1.7k，今日变化ΔOI: C -22 / P +0.2k，平值价格ATM: C $2.40 / P $0.65 ｜ ATM IV 80.6%，净 delta 敞口 -2k shares
Top ΔOI: P 11 +38
仓位参考: Max Pain 15 ｜ Put Wall 12（+9.5%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 80.6%｜历史 Rank 29%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,771 股

11-27（MEDIUM △）仓位参考: Max Pain 15

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 91.8% vs 11-13 83.5%（差 +8.3pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/NNE_evening.json