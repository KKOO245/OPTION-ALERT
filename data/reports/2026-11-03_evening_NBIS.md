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
🟡 **近现价集中开仓**: 11-06 145P ΔOI +3,239（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 145.46 → 收盘 151.64（+4.2%） ｜ 今日高 152.67 ｜ 低 143.71 ｜ 昨收 141.39 → 收盘 151.64（+7.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 0.46 | OI比 0.56 | ATM IV 143.8% | Skew 9.0pp | Term 0.76 | ExpMove ±10.4%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 9.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.56）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±10.4% ｜ 11-13（10D）±18.6% ｜ 11-20（17D）±21.2% ｜ 11-27（24D）±23.2%
   ⇒ IV–VIX Spread: +123.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,617,543 | GEX Change vs 上次快照 660,916 | Flip: Primary Flip: 156.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 593 / LOW 43 / INVALID 100
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 156.89（全链重定价，覆盖 100%）
最近结构参考: Flip 157（现价低于该位 3.3%）
量化视角： 负 Gamma（262万，无历史分位）｜负 Gamma 缓解（+66万）｜现价位于 Flip 下方 3.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 160（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 157（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +10.7k / P +4.0k ｜ Activity HIGH ｜ 3D
11-13  C +4.5k / P +0.9k ｜ Activity HIGH ｜ 10D
11-20  C +17.1k / P +1.3k ｜ Activity HIGH ｜ 17D
11-27  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 24D

📆 11-06 Forward Structure
存量OI: C 76.0k / P 42.4k，今日变化ΔOI: C +10.7k / P +4.0k，平值价格ATM: C $7.60 / P $8.25 ｜ ATM IV 143.8%，净 delta 敞口 668k shares
Top ΔOI: P 145 +3,239 ｜ C 160 +2,528 ｜ C 150 +1,292
仓位参考: Max Pain 160 ｜ Call Wall 160（+5.5%，弱）（OI 3.7k） ｜ Put Wall 145（-4.4%）（OI 5.2k）
量化解读： 存量 Call 重｜ATM IV 143.8%｜历史 Rank 89%（近端代理）｜IV/RV 1.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 668,444 股

📆 11-13 Forward Structure
存量OI: C 27.6k / P 27.6k，今日变化ΔOI: C +4.5k / P +0.9k，平值价格ATM: C $13.81 / P $14.45 ｜ ATM IV 141.0%，净 delta 敞口 101k shares
Top ΔOI: C 210 +1,755 ｜ C 200 +625 ｜ C 160 +329
仓位参考: Max Pain 195 ｜ Put Wall 150（-1.1%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 141.0%｜历史 Rank 89%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 101,357 股

📆 11-20 Forward Structure
存量OI: C 112.5k / P 110.4k，今日变化ΔOI: C +17.1k / P +1.3k，平值价格ATM: C $15.34 / P $16.80 ｜ ATM IV 124.8%，净 delta 敞口 504k shares
Top ΔOI: C 175 +7,311 ｜ C 210 +6,497 ｜ C 200 +947
仓位参考: Max Pain 180 ｜ Put Wall 150（-1.1%，弱）（OI 7.6k）
量化解读： 存量两侧均衡｜ATM IV 124.8%｜历史 Rank 89%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 504,244 股

📆 11-27 Forward Structure
存量OI: C 10.1k / P 10.0k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $18.55 / P $16.60 ｜ ATM IV 113.0%，净 delta 敞口 12k shares
Top ΔOI: C 200 +125 ｜ C 155 +99
仓位参考: Max Pain 180 ｜ Call Wall 150（-1.1%，弱）（OI 0.6k） ｜ Put Wall 155（+2.2%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜ATM IV 113.0%｜历史 Rank 89%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 正 12,357 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/NBIS_evening.json