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
🔴 **事件差分**: 11-06（3D）ATM IV 97.8% vs 11-13 82.7%（差 +15.1pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 131.18 → 收盘 135.63（+3.4%） ｜ 今日高 138.41 ｜ 低 131.09 ｜ 昨收 130.76 → 收盘 135.63（+3.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.55 | OI比 0.62 | ATM IV 97.8% | Skew 1.0pp | Term 0.76 | ExpMove ±7.1%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价薄（Skew 1.0pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±7.1% ｜ 11-13（10D）±11.0% ｜ 11-20（17D）±13.7% ｜ 11-27（24D）±15.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 64,450,580 | GEX Change vs 上次快照 4,130,350 | Flip: Primary Flip: 120.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 543 / LOW 95 / INVALID 202
结构观察区: Primary Flip 120.68（全链重定价，覆盖 100%）
Call Wall 135（现价高于该位 0.5%）
最近结构参考: Call Wall 135（现价高于该位 0.5%）
量化视角： 正 Gamma（6445万，无历史分位）｜正 Gamma 增强（+413万）｜现价位于 Flip 上方 12.39%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（MaxPain，仅结算参考） / 135（Call Wall）。
• Gamma 区域：切换参考 121（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +9.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 3D
11-13  C +2.6k / P +6.9k ｜ Activity HIGH ｜ 10D
11-20  C +1.6k / P +3.1k ｜ Activity MEDIUM △ ｜ 17D
11-27  C +1.1k / P +3.0k ｜ Activity HIGH ｜ 24D

📆 11-06 Forward Structure
存量OI: C 228.8k / P 141.1k，今日变化ΔOI: C +9.2k / P +0.1k，平值价格ATM: C $4.69 / P $4.95 ｜ ATM IV 97.8%，净 delta 敞口 365k shares
仓位参考: Max Pain 135 ｜ Call Wall 136（+0.3%，弱）（OI 24.3k） ｜ Put Wall 125（-7.8%，弱）（OI 6.5k）
量化解读： 存量 Call 重｜ATM IV 97.8%｜历史 Rank 78%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 365,363 股

📆 11-13 Forward Structure
存量OI: C 24.0k / P 66.5k，今日变化ΔOI: C +2.6k / P +6.9k，平值价格ATM: C $7.41 / P $7.49 ｜ ATM IV 82.7%，净 delta 敞口 -36k shares
Top ΔOI: P 115 +1,352 ｜ P 125 +1,315
仓位参考: Max Pain 155 ｜ Call Wall 144（+6.2%，弱）（OI 0.8k） ｜ Put Wall 125（-7.8%，弱）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 82.7%｜历史 Rank 78%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 35,951 股

11-20（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 135（-0.5%）（OI 42.8k） ｜ Put Wall 130（-4.2%，弱）（OI 5.0k）

📆 11-27 Forward Structure
存量OI: C 11.8k / P 24.1k，今日变化ΔOI: C +1.1k / P +3.0k，平值价格ATM: C $10.56 / P $9.79 ｜ ATM IV 75.2%，净 delta 敞口 -48k shares
Top ΔOI: P 125 +866 ｜ P 105 +502
仓位参考: Max Pain 155 ｜ Call Wall 145（+6.9%，弱）（OI 0.9k） ｜ Put Wall 140（+3.2%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜ATM IV 75.2%｜历史 Rank 78%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 负 47,908 股

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 97.8% vs 11-13 82.7%（差 +15.1pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/MSTR_evening.json