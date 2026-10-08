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
🔴 **事件差分**: 10-09（1D）ATM IV 48.5% vs 10-16 33.3%（差 +15.2pp），覆盖 密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 411.60 → 收盘 415.41（+0.9%） ｜ 今日高 416.72 ｜ 低 407.70 ｜ 昨收 414.52 → 收盘 415.41（+0.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-15，窗口结束前不做对错判定）

Options: P/C成交量 0.60 | OI比 0.50 | ATM IV 48.5% | Skew 7.0pp | Term 0.95 | ExpMove ±1.5%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构正常（Term 0.95）｜保护溢价显著（Skew 7.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±1.5% ｜ 10-16（8D）±3.9% ｜ 10-23（15D）±9.0% ｜ 10-30（22D）±9.6%
   ⇒ IV–VIX Spread: +33.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,182,757 | GEX Change vs 上次快照 1,600,558 | Flip: Primary Flip: 398.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 314 / LOW 143 / INVALID 407
结构观察区: Primary Flip 398.02（全链重定价，覆盖 92%）
Call Wall 420（弱结构｜现价低于该位 1.1%）
最近结构参考: Call Wall 420（现价低于该位 1.1%）
量化视角： 正 Gamma（518万，无历史分位）｜正 Gamma 增强（+160万）｜现价位于 Flip 上方 4.37%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 392（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 398（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 1D
10-16  C +0.1k / P +22 ｜ Activity MEDIUM △ ｜ 8D
10-23  C -5 / P +42 ｜ Activity MEDIUM △ ｜ 15D
10-30  C +23 / P +6 ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 3.3k / P 1.6k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $3.39 / P $3.00 ｜ ATM IV 48.5%，净 delta 敞口 -3k shares
Top ΔOI: C 425 +177 ｜ C 430 +140 ｜ P 397 +130
仓位参考: Max Pain 392 ｜ Call Wall 420（+1.1%，弱）（OI 0.7k） ｜ Put Wall 390（-6.1%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.5%｜历史 Rank 84%（近端代理）｜IV/RV 1.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 2,830 股

10-16（MEDIUM △）Top ΔOI: 430C +39 ｜ 442C +27
10-16（MEDIUM △）仓位参考: Max Pain 390 ｜ Call Wall 400（-3.7%，弱）（OI 0.9k） ｜ Put Wall 380（-8.5%，弱）（OI 0.6k）

10-23（MEDIUM △）Top ΔOI: 445C -38 ｜ 415P +12
10-23（MEDIUM △）仓位参考: Max Pain 415 ｜ Call Wall 425（+2.3%）（OI 0.5k） ｜ Put Wall 415（-0.1%）（OI 0.5k）

10-30（MEDIUM △）Top ΔOI: 380P +8 ｜ 395P -8
10-30（MEDIUM △）仓位参考: Max Pain 390 ｜ Call Wall 450（+8.3%，弱）（OI 75） ｜ Put Wall 375（-9.7%，弱）（OI 52）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 48.5% vs 10-16 33.3%（差 +15.2pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/ISRG_evening.json