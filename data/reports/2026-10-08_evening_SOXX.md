# 期权晚报 2026-10-08（快照 16:40 ET）

📊 市场环境

SPY $773.93 ｜ QQQ $747.58
VIX 15.41 ↑2.2%（5D -6.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 572P ΔOI +755（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 573.00 → 收盘 563.28（-1.7%） ｜ 今日高 579.25 ｜ 低 555.82 ｜ 昨收 582.82 → 收盘 563.28（-3.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-13，窗口结束前不做对错判定）

Options: P/C成交量 1.54 | OI比 2.05 | ATM IV 40.4% | Skew 8.0pp | Term 0.95 | ExpMove ±3.9%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构正常（Term 0.95）｜保护溢价显著（Skew 8.0pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 1.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.54×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.05×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.9% ｜ 10-16（8D）±4.7% ｜ 10-23（15D）±6.3% ｜ 10-30（22D）±7.4%
   ⇒ IV–VIX Spread: +25.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -12,430,917 | GEX Change vs 上次快照 -5,465,310 | Flip: Primary Flip: 580.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 549 / LOW 285 / INVALID 712
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 580.71（全链重定价，覆盖 96%）
最近结构参考: Flip 581（现价低于该位 3.0%）
量化视角： 负 Gamma（1243万，无历史分位）｜负 Gamma 加深（547万）｜现价位于 Flip 下方 3.00%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 570（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 581（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.3k / P +1.1k ｜ Activity HIGH ｜ 1D
10-16  C -2.2k / P +1.5k ｜ Activity HIGH ｜ 8D
10-23  C -11 / P +0.4k ｜ Activity MEDIUM △ ｜ 15D
10-30  C +0.2k / P +0.7k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 5.9k / P 12.2k，今日变化ΔOI: C +0.3k / P +1.1k，平值价格ATM: C $17.90 / P $4.00 ｜ ATM IV 40.4%，净 delta 敞口 -25k shares
Top ΔOI: P 572 +755 ｜ P 577 -310 ｜ C 600 +164
仓位参考: Max Pain 570 ｜ Call Wall 537.5（-4.6%，弱）（OI 0.4k） ｜ Put Wall 555（-1.5%）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 40.4%｜历史 Rank 71%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 25,359 股

📆 10-16 Forward Structure
存量OI: C 37.9k / P 100.8k，今日变化ΔOI: C -2.2k / P +1.5k，平值价格ATM: C $13.50 / P $12.75 ｜ ATM IV 37.0%，净 delta 敞口 -81k shares
Top ΔOI: C 600 -1,716 ｜ P 550 +1,417 ｜ P 540 +846
仓位参考: Max Pain 535 ｜ Call Wall 550（-2.4%，弱）（OI 2.2k） ｜ Put Wall 530（-5.9%，弱）（OI 4.8k）
量化解读： 存量 Put 重｜ATM IV 37.0%｜历史 Rank 71%（近端代理）｜IV/RV 1.41×（近似）｜净 delta 敞口 负 80,681 股

10-23（MEDIUM △）Top ΔOI: 567P +198 ｜ 565P +136
10-23（MEDIUM △）仓位参考: Max Pain 560 ｜ Call Wall 555（-1.5%，弱）（OI 91）

10-30（MEDIUM △）Top ΔOI: 520P +490 ｜ 610C +201
10-30（MEDIUM △）仓位参考: Max Pain 560 ｜ Put Wall 550（-2.4%，弱）（OI 3.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/SOXX_evening.json