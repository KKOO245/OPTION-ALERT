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
🔴 **事件差分**: 11-06（2D）ATM IV 121.1% vs 11-13 101.8%（差 +19.4pp），覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 11-13 210P ΔOI +403（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 205.50 → 收盘 200.40（-2.5%） ｜ 今日高 213.96 ｜ 低 190.60 ｜ 昨收 214.01 → 收盘 200.40（-6.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-09，窗口结束前不做对错判定）

Options: P/C成交量 0.60 | OI比 0.68 | ATM IV 121.1% | Skew 7.1pp | Term 0.72 | ExpMove ±7.2%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价显著（Skew 7.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.68）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.68×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±7.2% ｜ 11-13（9D）±12.9% ｜ 11-20（16D）±16.0% ｜ 11-27（23D）±17.8%
   ⇒ IV–VIX Spread: +104.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,127,741 | GEX Change vs 上次快照 -1,765,080 | Flip: Primary Flip: 212.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 537 / LOW 109 / INVALID 200
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 212.54（全链重定价，覆盖 98%）
Put Wall 200（现价高于该位 0.2%）
最近结构参考: Put Wall 200（现价高于该位 0.2%）
量化视角： 负 Gamma（613万，无历史分位）｜负 Gamma 加深（177万）｜现价位于 Flip 下方 5.71%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall）；上方 215（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 213（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +6.0k / P +2.5k ｜ Activity HIGH ｜ 2D
11-13  C +1.2k / P +1.2k ｜ Activity HIGH ｜ 9D
11-20  C +0.9k / P +3.1k ｜ Activity HIGH ｜ 16D
11-27  C +0.3k / P +48 ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 49.2k / P 33.3k，今日变化ΔOI: C +6.0k / P +2.5k，平值价格ATM: C $7.44 / P $7.00 ｜ ATM IV 121.1%，净 delta 敞口 -50k shares
Top ΔOI: P 175 +728
仓位参考: Max Pain 215 ｜ Call Wall 220（+9.8%，弱）（OI 1.9k） ｜ Put Wall 190（-5.2%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 121.1%｜历史 Rank 78%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 49,824 股

📆 11-13 Forward Structure
存量OI: C 13.3k / P 12.5k，今日变化ΔOI: C +1.2k / P +1.2k，平值价格ATM: C $12.95 / P $12.84 ｜ ATM IV 101.8%，净 delta 敞口 -28k shares
Top ΔOI: P 210 +403 ｜ C 235 +241
仓位参考: Max Pain 232 ｜ Call Wall 220（+9.8%，弱）（OI 0.4k） ｜ Put Wall 210（+4.8%，弱）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 101.8%｜历史 Rank 78%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 27,935 股

📆 11-20 Forward Structure
存量OI: C 63.0k / P 75.5k，今日变化ΔOI: C +0.9k / P +3.1k，平值价格ATM: C $16.30 / P $15.70 ｜ ATM IV 96.4%，净 delta 敞口 -41k shares
Top ΔOI: P 205 +1,506
仓位参考: Max Pain 230 ｜ Call Wall 220（+9.8%，弱）（OI 2.6k） ｜ Put Wall 200（-0.2%，弱）（OI 5.8k）
量化解读： 存量 Put 重｜ATM IV 96.4%｜历史 Rank 78%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 40,913 股

11-27（MEDIUM △）仓位参考: Max Pain 230 ｜ Call Wall 215（+7.3%，弱）（OI 0.3k） ｜ Put Wall 200（-0.2%，弱）（OI 1.6k）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 121.1% vs 11-13 101.8%（差 +19.4pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=83 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=83）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/BE_evening.json