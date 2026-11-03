# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $753.95 ｜ QQQ $685.78
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
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
🔴 **事件差分**: 11-06（3D）ATM IV 104.6% vs 11-13 86.1%（差 +18.5pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 10.96 → 今开 11.41（+4.1%） | 较昨收变动（含盘初走势） ｜ 今日高 11.83 ｜ 低 11.19

Options: P/C成交量 0.11 | OI比 0.56 | ATM IV 104.6% | Skew 16.7pp | Term 0.74 | ExpMove ±10.9%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 16.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.11×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±10.9% ｜ 11-13（10D）±17.8% ｜ 11-20（17D）±9.2% ｜ 11-27（24D）±5.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 10,448 | GEX Change vs 上次快照 317,917 | Flip: Primary Flip: 11.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 154 / LOW 77 / INVALID 169
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 11.61（全链重定价，覆盖 94%）
Put Wall 12（弱结构｜现价低于该位 3.1%）
最近结构参考: Flip 12（现价高于该位 0.2%）
量化视角： 正 Gamma（1万，无历史分位）｜由负转正（+32万）｜现价位于 Flip 上方 0.20%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 12（Put Wall，弱结构） / 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 12（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 12.5C — Vol 227 | 最新价 $0.05 | OI 47→255 (ΔOI +208张) | ΔOI/Volume 91.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增208张（+442.6% vs前日OI），连续性待观察（方向未知）
11-06 12.0C — Vol 187 | 最新价 $0.11 | OI 94→235 (ΔOI +141张) | ΔOI/Volume 75.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增141张（+150.0% vs前日OI），连续性待观察（方向未知）
11-13 10.5P — Vol 130 | 最新价 $0.40 | OI 0→130 (ΔOI +130张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增130张（前日OI缺失），值得跟踪（方向未知）
11-06 13.0C — Vol 252 | 最新价 $0.03 | OI 285→407 (ΔOI +122张) | ΔOI/Volume 48.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增122张（+42.8% vs前日OI），连续性待观察（方向未知）
11-06 13.5C — Vol 130 | 最新价 $0.05 | OI 152→270 (ΔOI +118张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增118张（+77.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 719 张（Put 130 / Call 589），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 3D
11-13  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 10D
11-20  C -9 / P +5 ｜ Activity LOW ｜ 17D
11-27  C +21 / P -28 ｜ Activity LOW ｜ 24D

📆 11-06 Forward Structure
存量OI: C 3.2k / P 1.8k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $0.50 / P $0.77 ｜ ATM IV 104.6%，净 delta 敞口 16k shares
Top ΔOI: C 12 +208 ｜ C 12 +141
仓位参考: Max Pain 12 ｜ Call Wall 12.5（+7.5%，弱）（OI 0.3k） ｜ Put Wall 11.5（-1.1%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 104.6%｜历史 Rank 50%（近端代理）｜IV/RV 1.71×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,141 股

11-13（MEDIUM △）Top ΔOI: 10P +130 ｜ 12C +56
11-13（MEDIUM △）仓位参考: Max Pain 13 ｜ Call Wall 12.5（+7.5%，弱）（OI 74） ｜ Put Wall 10.5（-9.7%，弱）（OI 0.1k）

11-20（Activity LOW）仓位参考: Max Pain 15 ｜ Put Wall 12（+3.2%，弱）（OI 0.3k）

11-27（Activity LOW）仓位参考: Max Pain 15 ｜ Put Wall 12.5（+7.5%）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 104.6% vs 11-13 86.1%（差 +18.5pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/NNE_morning.json