# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $760.66 ｜ QQQ $698.90
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.4（fear）
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
🟡 **近现价集中开仓**: 11-06 11C ΔOI +121（距现价 -3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 11.65 → 今开 11.80（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 12.14 ｜ 低 11.55

Options: P/C成交量 0.69 | OI比 0.65 | ATM IV 83.0% | Skew -0.1pp | Term 0.92 | ExpMove ±11.0%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.65×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±11.0% ｜ 11-13（11D）±17.9% ｜ 11-20（18D）±12.2% ｜ 11-27（25D）±25.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -286,751 | GEX Change vs 上次快照 -84,885 | Flip: Primary Flip: 12.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 159 / LOW 68 / INVALID 173
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 12.54（全链重定价，覆盖 94%）
Put Wall 12（弱结构｜现价低于该位 1.2%）
最近结构参考: Put Wall 12（现价低于该位 1.2%）
量化视角： 负 Gamma（29万，无历史分位）｜负 Gamma 加深（8万）｜现价位于 Flip 下方 5.41%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 12（Put Wall，弱结构） / 13（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 13（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 9.0P — Vol 156 | 最新价 $0.10 | OI 15→171 (ΔOI +156张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增156张（+1040.0% vs前日OI），连续性待观察（方向未知）
11-06 11.5C — Vol 171 | 最新价 $0.53 | OI 33→154 (ΔOI +121张) | ΔOI/Volume 70.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增121张（+366.7% vs前日OI），连续性待观察（方向未知）
11-06 11.5P — Vol 101 | 最新价 $0.52 | OI 278→379 (ΔOI +101张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增101张（+36.3% vs前日OI），连续性待观察（方向未知）
11-13 13.0P — Vol 73 | 最新价 $1.75 | OI 68→140 (ΔOI +72张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增72张（+105.9% vs前日OI），连续性待观察（方向未知）
11-06 12.0C — Vol 127 | 最新价 $0.37 | OI 24→94 (ΔOI +70张) | ΔOI/Volume 55.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增70张（+291.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 520 张（Put 329 / Call 191），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.2k / P +0.2k ｜ Activity HIGH ｜ 4D
11-13  C +11 / P +89 ｜ Activity HIGH ｜ 11D
11-20  C -22 / P +0.2k ｜ Activity HIGH ｜ 18D
11-27  C +55 / P +55 ｜ Activity HIGH ｜ 25D

📆 11-06 Forward Structure
存量OI: C 2.5k / P 1.6k，今日变化ΔOI: C +0.2k / P +0.2k，平值价格ATM: C $0.37 / P $0.93 ｜ ATM IV 83.0%，净 delta 敞口 -1k shares
Top ΔOI: C 11 +121 ｜ P 11 +101 ｜ C 12 +70
仓位参考: Max Pain 13 ｜ Call Wall 13（+9.6%，弱）（OI 0.3k） ｜ Put Wall 11.5（-3.0%）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 83.0%｜历史 Rank 16%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,436 股

📆 11-13 Forward Structure
存量OI: C 0.9k / P 0.5k，今日变化ΔOI: C +11 / P +89，平值价格ATM: C $1.10 / P $1.02 ｜ ATM IV 74.1%，净 delta 敞口 -6k shares
Top ΔOI: P 13 +72 ｜ P 11 +9 ｜ C 13 +6
仓位参考: Max Pain 14 ｜ Put Wall 13（+9.6%）（OI 0.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.1%｜历史 Rank 16%（近端代理）｜IV/RV 1.23×（近似）｜净 delta 敞口 负 5,917 股

📆 11-20 Forward Structure
存量OI: C 4.1k / P 1.7k，今日变化ΔOI: C -22 / P +0.2k，平值价格ATM: C $0.64 / P $0.81 ｜ ATM IV 67.5%，净 delta 敞口 -885 shares
Top ΔOI: P 11 +38
仓位参考: Max Pain 15 ｜ Put Wall 12（+1.2%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 67.5%｜历史 Rank 16%（近端代理）｜IV/RV 1.12×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 885 股

📆 11-27 Forward Structure
存量OI: C 0.4k / P 0.7k，今日变化ΔOI: C +55 / P +55，平值价格ATM: C $1.80 / P $1.25 ｜ ATM IV 76.2%，净 delta 敞口 -962 shares
Top ΔOI: C 13 +70
仓位参考: Max Pain 15 ｜ Call Wall 13（+9.6%）（OI 0.1k） ｜ Put Wall 12.5（+5.4%）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 76.2%｜历史 Rank 16%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 负 962 股

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 83.0% vs 11-13 74.1%（差 +8.9pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/NNE_morning.json