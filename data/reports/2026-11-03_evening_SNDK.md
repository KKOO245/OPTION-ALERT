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

🔍 重点速览
🔴 **事件差分**: 11-06（3D）ATM IV 102.6% vs 11-13 86.2%（差 +16.3pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,106.46 → 收盘 1,126.52（+1.8%） ｜ 今日高 1153.19 ｜ 低 1100.53 ｜ 昨收 1,075.08 → 收盘 1,126.52（+4.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.67 | OI比 0.77 | ATM IV 102.5% | Skew 7.1pp | Term 0.76 | ExpMove ±7.4%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 7.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±7.4% ｜ 11-13（10D）±11.9% ｜ 11-20（17D）±14.9% ｜ 11-27（24D）±16.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,132,255 | GEX Change vs 上次快照 -646,343 | Flip: Primary Flip: 1171.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1775 / LOW 475 / INVALID 990
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1171.51（全链重定价，覆盖 100%）
最近结构参考: Flip 1172（现价低于该位 3.8%）
量化视角： 负 Gamma（213万，无历史分位）｜负 Gamma 加深（65万）｜现价位于 Flip 下方 3.84%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,200（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1172（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +5.9k / P +2.5k ｜ Activity HIGH ｜ 3D
11-13  C +3.6k / P +0.8k ｜ Activity HIGH ｜ 10D
11-20  C +1.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 17D
11-27  C +0.8k / P +0.3k ｜ Activity HIGH ｜ 24D

📆 11-06 Forward Structure
存量OI: C 38.3k / P 29.4k，今日变化ΔOI: C +5.9k / P +2.5k，平值价格ATM: C $42.70 / P $40.87 ｜ ATM IV 102.6%，净 delta 敞口 300k shares
Top ΔOI: C 1300 +542 ｜ P 900 +502
仓位参考: Max Pain 1,200 ｜ Call Wall 1200（+6.5%，弱）（OI 1.1k） ｜ Put Wall 1050（-6.8%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 102.6%｜历史 Rank 59%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 300,367 股

📆 11-13 Forward Structure
存量OI: C 12.8k / P 9.4k，今日变化ΔOI: C +3.6k / P +0.8k，平值价格ATM: C $64.00 / P $69.70 ｜ ATM IV 86.2%，净 delta 敞口 60k shares
Top ΔOI: C 1500 +601
仓位参考: Max Pain 1,295 ｜ Call Wall 1185（+5.2%，弱）（OI 0.3k） ｜ Put Wall 1100（-2.4%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 86.2%｜历史 Rank 59%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 59,551 股

11-20（MEDIUM △）Top ΔOI: 680P +726 ｜ 1200C +533
11-20（MEDIUM △）仓位参考: Max Pain 1,400 ｜ Call Wall 1200（+6.5%，弱）（OI 0.9k） ｜ Put Wall 1200（+6.5%，弱）（OI 1.5k）

📆 11-27 Forward Structure
存量OI: C 12.5k / P 8.0k，今日变化ΔOI: C +0.8k / P +0.3k，平值价格ATM: C $86.00 / P $95.88 ｜ ATM IV 79.7%，净 delta 敞口 16k shares
Top ΔOI: C 1120 +81 ｜ C 1200 +81
仓位参考: Max Pain 1,270 ｜ Put Wall 1150（+2.1%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 79.7%｜历史 Rank 59%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 正 15,703 股

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 102.6% vs 11-13 86.2%（差 +16.3pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/SNDK_evening.json