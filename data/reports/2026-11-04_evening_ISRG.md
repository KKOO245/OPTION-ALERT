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
🟡 **近现价集中开仓**: 11-06 480C ΔOI +24（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 458.99 → 收盘 482.10（+5.0%） ｜ 今日高 485.85 ｜ 低 453.69 ｜ 昨收 440.75 → 收盘 482.10（+9.4%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-11-09，窗口结束前不做对错判定）

Options: P/C成交量 0.47 | OI比 0.62 | ATM IV 42.2% | Skew 12.9pp | Term 0.79 | ExpMove ±2.5%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价显著（Skew 12.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±2.5% ｜ 11-13（9D）±4.5% ｜ 11-20（16D）±5.9% ｜ 11-27（23D）±6.9%
   ⇒ IV–VIX Spread: +25.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,821,448 | GEX Change vs 上次快照 -350,717 | Flip: Primary Flip: 415.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 231 / LOW 169 / INVALID 512
结构观察区: Primary Flip 415.70（全链重定价，覆盖 88%）
最近结构参考: Flip 416（现价高于该位 16.0%）
量化视角： 正 Gamma（282万，无历史分位）｜正 Gamma 减弱（35万）｜现价位于 Flip 上方 15.97%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 430（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 416（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0.1k / P +19 ｜ Activity MEDIUM △ ｜ 2D
11-13  C +7 / P +76 ｜ Activity HIGH ｜ 9D
11-20  C +22 / P +60 ｜ Activity MEDIUM △ ｜ 16D
11-27  C +2 / P +3 ｜ Activity LOW ｜ 23D

📆 11-06 Forward Structure
存量OI: C 2.6k / P 1.6k，今日变化ΔOI: C +0.1k / P +19，平值价格ATM: C $6.00 / P $6.00 ｜ ATM IV 42.2%，净 delta 敞口 10k shares
Top ΔOI: C 480 +24 ｜ C 465 +23 ｜ C 460 +16
仓位参考: Max Pain 430 ｜ Call Wall 445（-7.7%）（OI 0.5k） ｜ Put Wall 450（-6.7%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 42.2%｜历史 Rank 65%（近端代理）｜IV/RV 1.65×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,982 股

📆 11-13 Forward Structure
存量OI: C 1.0k / P 1.0k，今日变化ΔOI: C +7 / P +76，平值价格ATM: C $11.71 / P $10.09 ｜ ATM IV 37.1%，净 delta 敞口 543 shares
仓位参考: Max Pain 425 ｜ Call Wall 440（-8.7%，弱）（OI 0.1k） ｜ Put Wall 435（-9.8%，弱）（OI 55）
量化解读： 存量两侧均衡｜ATM IV 37.1%｜历史 Rank 65%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 543 股

11-20（MEDIUM △）Top ΔOI: 455C +27 ｜ 440P +24
11-20（MEDIUM △）仓位参考: Max Pain 405 ｜ Call Wall 530（+9.9%，弱）（OI 0.7k）

11-27（Activity LOW）仓位参考: Max Pain 425 ｜ Call Wall 460（-4.6%，弱）（OI 43）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 42.2% vs 11-13 37.1%（差 +5.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/ISRG_evening.json