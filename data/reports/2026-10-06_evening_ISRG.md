# 期权晚报 2026-10-06（快照 16:40 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 420C ΔOI +87（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 406.13 → 收盘 404.76（-0.3%） ｜ 今日高 409.29 ｜ 低 402.00 ｜ 昨收 406.48 → 收盘 404.76（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.04 | OI比 0.69 | ATM IV 38.9% | Skew -3.0pp | Term 1.17 | ExpMove ±2.9%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构正常偏陡（Term 1.17）｜Put 保护异常便宜（Skew -3.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.04×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±2.9% ｜ 10-16（10D）±4.4% ｜ 10-23（17D）±8.8% ｜ 10-30（24D）±9.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,753,644 | GEX Change vs 上次快照 165,990 | Flip: Primary Flip: 392.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 287 / LOW 142 / INVALID 407
结构观察区: Primary Flip 392.70（全链重定价，覆盖 92%）
Call Wall 400（弱结构｜现价高于该位 1.2%）
最近结构参考: Call Wall 400（现价高于该位 1.2%）
量化视角： 正 Gamma（175万，无历史分位）｜正 Gamma 增强（+17万）｜现价位于 Flip 上方 3.07%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 390（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 393（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.4k / P +79 ｜ Activity HIGH ｜ 3D
10-16  C +0.1k / P -56 ｜ Activity MEDIUM △ ｜ 10D
10-23  C +52 / P +10 ｜ Activity MEDIUM △ ｜ 17D
10-30  C +53 / P +7 ｜ Activity MEDIUM △ ｜ 24D

📆 10-09 Forward Structure
存量OI: C 1.9k / P 1.3k，今日变化ΔOI: C +0.4k / P +79，平值价格ATM: C $5.83 / P $5.90 ｜ ATM IV 38.9%，净 delta 敞口 8k shares
Top ΔOI: C 420 +87 ｜ C 410 +73 ｜ C 430 +28
仓位参考: Max Pain 390 ｜ Call Wall 420（+3.8%，弱）（OI 0.3k） ｜ Put Wall 370（-8.6%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 38.9%｜历史 Rank 44%（近端代理）｜IV/RV 1.60×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 7,888 股

10-16（MEDIUM △）Top ΔOI: 425C +39
10-16（MEDIUM △）仓位参考: Max Pain 390 ｜ Call Wall 400（-1.2%，弱）（OI 0.9k） ｜ Put Wall 380（-6.1%，弱）（OI 0.6k）

10-23（MEDIUM △）Top ΔOI: 440C +11 ｜ 370P +8
10-23（MEDIUM △）仓位参考: Max Pain 415 ｜ Call Wall 425（+5.0%）（OI 0.5k） ｜ Put Wall 415（+2.5%）（OI 0.5k）

10-30（MEDIUM △）Top ΔOI: 385C +9
10-30（MEDIUM △）仓位参考: Max Pain 380 ｜ Call Wall 375（-7.4%，弱）（OI 59） ｜ Put Wall 375（-7.4%，弱）（OI 52）

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 38.9% vs 10-16 32.5%（差 +6.5pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/ISRG_evening.json