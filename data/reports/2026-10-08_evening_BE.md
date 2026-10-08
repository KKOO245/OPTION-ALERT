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
🟡 **事件差分**: 10-09 ATM IV 83.2% vs 10-16 69.6%（差 +13.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 275P ΔOI +689（距现价 +0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 283.83 → 收盘 272.82（-3.9%） ｜ 今日高 286.95 ｜ 低 264.50 ｜ 昨收 291.29 → 收盘 272.82（-6.3%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-13，窗口结束前不做对错判定）

Options: P/C成交量 0.65 | OI比 1.17 | ATM IV 83.2% | Skew 0.3pp | Term 0.98 | ExpMove ±3.5%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构正常（Term 0.98）｜保护溢价薄（Skew 0.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.65×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.5% ｜ 10-16（8D）±8.3% ｜ 10-23（15D）±12.3% ｜ 10-30（22D）±15.7%
   ⇒ IV–VIX Spread: +67.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,302,694 | GEX Change vs 上次快照 -3,176,084 | Flip: Primary Flip: 280.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 566 / LOW 105 / INVALID 199
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 280.82（全链重定价，覆盖 98%）
Call Wall 300（弱结构｜现价低于该位 9.1%）
最近结构参考: Flip 281（现价低于该位 2.8%）
量化视角： 负 Gamma（730万，无历史分位）｜负 Gamma 加深（318万）｜现价位于 Flip 下方 2.85%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 282（MaxPain，仅结算参考） / 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 281（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.8k / P +2.4k ｜ Activity HIGH ｜ 1D
10-16  C +0.9k / P +2.0k ｜ Activity MEDIUM △ ｜ 8D
10-23  C +0.6k / P +1.1k ｜ Activity HIGH ｜ 15D
10-30  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 36.3k / P 42.4k，今日变化ΔOI: C +0.8k / P +2.4k，平值价格ATM: C $4.95 / P $4.54 ｜ ATM IV 83.2%，净 delta 敞口 -100k shares
Top ΔOI: P 275 +689 ｜ P 270 +386 ｜ C 290 +364
仓位参考: Max Pain 282 ｜ Call Wall 300（+10.0%，弱）（OI 3.1k） ｜ Put Wall 280（+2.6%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 83.2%｜历史 Rank 42%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 99,538 股

10-16（MEDIUM △）Top ΔOI: 270C -579 ｜ 270P +566
10-16（MEDIUM △）仓位参考: Max Pain 270 ｜ Call Wall 270（-1.0%，弱）（OI 7.0k） ｜ Put Wall 260（-4.7%，弱）（OI 4.3k）

📆 10-23 Forward Structure
存量OI: C 14.5k / P 16.7k，今日变化ΔOI: C +0.6k / P +1.1k，平值价格ATM: C $15.65 / P $17.84 ｜ ATM IV 69.8%，净 delta 敞口 -23k shares
仓位参考: Max Pain 270 ｜ Call Wall 300（+10.0%，弱）（OI 1.1k） ｜ Put Wall 250（-8.4%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 69.8%｜历史 Rank 42%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 23,415 股

10-30（MEDIUM △）Top ΔOI: 250P +100 ｜ 260P +65
10-30（MEDIUM △）仓位参考: Max Pain 285 ｜ Call Wall 300（+10.0%，弱）（OI 1.4k） ｜ Put Wall 285（+4.5%，弱）（OI 1.8k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 83.2% vs 10-16 69.6%（差 +13.5pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/BE_evening.json