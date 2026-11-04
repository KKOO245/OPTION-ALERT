# 期权晚报 2026-11-04（快照 16:40 ET）

📊 市场环境

SPY $766.81 ｜ QQQ $691.95
VIX 16.61 ↓20.3%（5D -1.8%） ｜ Vol Regime: NORMAL
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
🔴 **事件差分**: 11-06（2D）ATM IV 102.1% vs 11-13 86.0%（差 +16.1pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,079.00 → 收盘 1,037.40（-3.9%） ｜ 今日高 1120.22 ｜ 低 1014.02 ｜ 昨收 1,126.52 → 收盘 1,037.40（-7.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-09，窗口结束前不做对错判定）

Options: P/C成交量 0.77 | OI比 0.70 | ATM IV 102.1% | Skew -1.9pp | Term 0.77 | ExpMove ±6.1%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±6.1% ｜ 11-13（9D）±11.1% ｜ 11-20（16D）±14.5% ｜ 11-27（23D）±16.0%
   ⇒ IV–VIX Spread: +85.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,978,558 | GEX Change vs 上次快照 -3,025,550 | Flip: Primary Flip: 1115.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1623 / LOW 620 / INVALID 997
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1115.42（全链重定价，覆盖 100%）
Put Wall 1,000（弱结构｜现价高于该位 3.7%）
最近结构参考: Put Wall 1000（现价高于该位 3.7%）
量化视角： 负 Gamma（498万，无历史分位）｜负 Gamma 加深（303万）｜现价位于 Flip 下方 6.99%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,000（Put Wall，弱结构）；上方 1,190（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1115（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +6.2k / P +1.6k ｜ Activity HIGH ｜ 2D
11-13  C +2.8k / P +0.4k ｜ Activity HIGH ｜ 9D
11-20  C +2.4k / P +0.2k ｜ Activity HIGH ｜ 16D
11-27  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 23D

📆 11-06 Forward Structure
存量OI: C 44.5k / P 30.9k，今日变化ΔOI: C +6.2k / P +1.6k，平值价格ATM: C $33.00 / P $29.95 ｜ ATM IV 102.1%，净 delta 敞口 21k shares
Top ΔOI: C 1300 +839 ｜ P 1100 -436
仓位参考: Max Pain 1,190 ｜ Put Wall 1000（-3.6%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 102.1%｜历史 Rank 58%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 20,748 股

📆 11-13 Forward Structure
存量OI: C 15.6k / P 9.8k，今日变化ΔOI: C +2.8k / P +0.4k，平值价格ATM: C $58.38 / P $56.64 ｜ ATM IV 86.0%，净 delta 敞口 21k shares
Top ΔOI: C 1150 +193
仓位参考: Max Pain 1,250 ｜ Call Wall 1120（+8.0%，弱）（OI 0.3k） ｜ Put Wall 1100（+6.0%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 86.0%｜历史 Rank 58%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 21,451 股

📆 11-20 Forward Structure
存量OI: C 54.0k / P 54.6k，今日变化ΔOI: C +2.4k / P +0.2k，平值价格ATM: C $72.82 / P $77.60 ｜ ATM IV 82.8%，净 delta 敞口 83k shares
Top ΔOI: C 1150 +832 ｜ P 950 +408 ｜ C 1480 +354
仓位参考: Max Pain 1,390 ｜ Call Wall 1000（-3.6%，弱）（OI 0.6k） ｜ Put Wall 1000（-3.6%，弱）（OI 2.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 82.8%｜历史 Rank 58%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 83,467 股

📆 11-27 Forward Structure
存量OI: C 13.2k / P 8.1k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $83.00 / P $83.01 ｜ ATM IV 80.7%，净 delta 敞口 3k shares
Top ΔOI: C 1200 +72
仓位参考: Max Pain 1,270
量化解读： 存量 Call 重｜ATM IV 80.7%｜历史 Rank 58%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 2,673 股

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 102.1% vs 11-13 86.0%（差 +16.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=83 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=83）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/SNDK_evening.json