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
🔴 **事件差分**: 11-06（3D）ATM IV 118.9% vs 11-13 99.7%（差 +19.2pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-13 222C ΔOI -120（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 210.33 → 收盘 214.01（+1.7%） ｜ 今日高 220.50 ｜ 低 208.20 ｜ 昨收 196.25 → 收盘 214.01（+9.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 0.45 | OI比 0.71 | ATM IV 118.9% | Skew 5.1pp | Term 0.75 | ExpMove ±8.7%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜保护溢价中性（Skew 5.1pp）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±8.7% ｜ 11-13（10D）±13.2% ｜ 11-20（17D）±16.4% ｜ 11-27（24D）±18.2%
   ⇒ IV–VIX Spread: +98.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -688,140 | GEX Change vs 上次快照 -1,484,597 | Flip: Primary Flip: 216.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 557 / LOW 81 / INVALID 208
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 216.07（全链重定价，覆盖 100%）
Put Wall 200（现价高于该位 7.0%）
最近结构参考: Flip 216（现价低于该位 1.0%）
量化视角： 负 Gamma（69万，无历史分位）｜由正转负（148万）｜现价位于 Flip 下方 0.95%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 215（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 216（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +12.8k / P +3.3k ｜ Activity HIGH ｜ 3D
11-13  C +0.7k / P +0.9k ｜ Activity HIGH ｜ 10D
11-20  C +0.7k / P +41 ｜ Activity MEDIUM △ ｜ 17D
11-27  C +0.7k / P +0.5k ｜ Activity HIGH ｜ 24D

📆 11-06 Forward Structure
存量OI: C 43.2k / P 30.8k，今日变化ΔOI: C +12.8k / P +3.3k，平值价格ATM: C $8.84 / P $9.68 ｜ ATM IV 118.9%，净 delta 敞口 352k shares
Top ΔOI: C 240 +1,509 ｜ C 235 +1,298 ｜ C 225 +1,212
仓位参考: Max Pain 215 ｜ Call Wall 225（+5.1%，弱）（OI 2.8k） ｜ Put Wall 200（-6.5%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 118.9%｜历史 Rank 76%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 351,780 股

📆 11-13 Forward Structure
存量OI: C 12.1k / P 11.2k，今日变化ΔOI: C +0.7k / P +0.9k，平值价格ATM: C $13.83 / P $14.50 ｜ ATM IV 99.7%，净 delta 敞口 -831 shares
Top ΔOI: P 192 +316 ｜ P 305 -143 ｜ C 222 -120
仓位参考: Max Pain 235 ｜ Call Wall 222.5（+4.0%，弱）（OI 0.6k） ｜ Put Wall 200（-6.5%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 99.7%｜历史 Rank 76%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 831 股

11-20（MEDIUM △）Top ΔOI: 175P -164 ｜ 200C +144
11-20（MEDIUM △）仓位参考: Max Pain 230 ｜ Call Wall 200（-6.5%，弱）（OI 2.2k） ｜ Put Wall 200（-6.5%，弱）（OI 5.9k）

📆 11-27 Forward Structure
存量OI: C 6.1k / P 9.0k，今日变化ΔOI: C +0.7k / P +0.5k，平值价格ATM: C $19.10 / P $19.91 ｜ ATM IV 88.8%，净 delta 敞口 5k shares
Top ΔOI: C 265 +325 ｜ P 210 +267 ｜ C 215 +183
仓位参考: Max Pain 225 ｜ Call Wall 225（+5.1%，弱）（OI 0.5k） ｜ Put Wall 200（-6.5%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 88.8%｜历史 Rank 76%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 4,957 股

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 118.9% vs 11-13 99.7%（差 +19.2pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/BE_evening.json