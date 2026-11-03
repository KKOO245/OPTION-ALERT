# 期权晚报 2026-11-03（快照 16:41 ET）

📊 市场环境

SPY $754.35 ｜ QQQ $685.28
VIX 20.83 ↓1.5%（5D +18.9%） ｜ Vol Regime: ELEVATED
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 11.41 → 收盘 11.43（+0.2%） ｜ 今日高 11.83 ｜ 低 11.18 ｜ 昨收 10.96 → 收盘 11.43（+4.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.38 | OI比 0.56 | ATM IV 92.5% | Skew 7.1pp | Term 0.82 | ExpMove ±7.9%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜保护溢价显著（Skew 7.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±7.9% ｜ 11-13（10D）±18.1% ｜ 11-20（17D）±11.3% ｜ 11-27（24D）±13.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,260 | GEX Change vs 上次快照 -19,708 | Flip: Primary Flip: 11.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 130 / LOW 72 / INVALID 198
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 11.45（全链重定价，覆盖 94%）
Put Wall 12（弱结构｜现价低于该位 4.7%）
最近结构参考: Flip 11（现价低于该位 0.2%）
量化视角： 负 Gamma（1万，无历史分位）｜由正转负（2万）｜现价位于 Flip 下方 0.20%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 12（Put Wall，弱结构） / 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 3D
11-13  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 10D
11-20  C -9 / P +5 ｜ Activity LOW ｜ 17D
11-27  C +21 / P -28 ｜ Activity MEDIUM △ ｜ 24D

📆 11-06 Forward Structure
存量OI: C 3.2k / P 1.8k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $0.50 / P $0.40 ｜ ATM IV 92.5%，净 delta 敞口 14k shares
Top ΔOI: C 12 +208 ｜ C 12 +141
仓位参考: Max Pain 12 ｜ Call Wall 12.5（+9.4%，弱）（OI 0.3k） ｜ Put Wall 11.5（+0.6%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 92.5%｜历史 Rank 31%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,627 股

11-13（MEDIUM △）Top ΔOI: 10P +130 ｜ 12C +56
11-13（MEDIUM △）仓位参考: Max Pain 13 ｜ Call Wall 12.5（+9.4%，弱）（OI 74） ｜ Put Wall 10.5（-8.1%，弱）（OI 0.1k）

11-20（Activity LOW）仓位参考: Max Pain 15 ｜ Put Wall 12（+5.0%，弱）（OI 0.3k）

11-27（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 12.5（+9.4%）（OI 0.3k）

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 92.5% vs 11-13 84.6%（差 +7.9pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/NNE_evening.json