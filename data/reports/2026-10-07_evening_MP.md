# 期权晚报 2026-10-07（快照 16:40 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $757.73
VIX 15.08 ↑0.5%（5D -7.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 44P ΔOI +1,505（距现价 -5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 44P ΔOI +1,505 占该期限总 OI 18.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 47.00 → 收盘 46.31（-1.5%） ｜ 今日高 47.01 ｜ 低 45.58 ｜ 昨收 48.53 → 收盘 46.31（-4.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-12，窗口结束前不做对错判定）

Options: P/C成交量 0.64 | OI比 0.77 | ATM IV 62.7% | Skew 3.9pp | Term 0.94 | ExpMove ±4.0%（近端） | Rank 42%
量化视角： IV 中性（Rank 42%）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 3.9pp）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±4.0% ｜ 10-16（9D）±6.6% ｜ 10-23（16D）±9.2% ｜ 10-30（23D）±10.8%
   ⇒ IV–VIX Spread: +47.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,795,987 | GEX Change vs 上次快照 -141,566 | Flip: Primary Flip: 47.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 289 / LOW 54 / INVALID 93
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 47.69（全链重定价，覆盖 98%）
Put Wall 45（现价高于该位 2.9%） | Call Wall 50（弱结构｜现价低于该位 7.4%）
最近结构参考: Flip 48（现价低于该位 2.9%）
量化视角： 负 Gamma（380万，无历史分位）｜负 Gamma 加深（14万）｜现价位于 Flip 下方 2.89%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall）；上方 48（MaxPain，仅结算参考） / 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.8k / P -0.1k ｜ Activity HIGH ｜ 2D
10-16  C +0.7k / P +91 ｜ Activity HIGH ｜ 9D
10-23  C +0.5k / P +22 ｜ Activity MEDIUM △ ｜ 16D
10-30  C +0.3k / P +1.5k ｜ Activity HIGH ｜ 23D

📆 10-09 Forward Structure
存量OI: C 11.7k / P 9.1k，今日变化ΔOI: C +0.8k / P -0.1k，平值价格ATM: C $0.65 / P $1.19 ｜ ATM IV 62.7%，净 delta 敞口 4k shares
Top ΔOI: C 50 +429
仓位参考: Max Pain 48 ｜ Call Wall 50（+8.0%，弱）（OI 2.2k） ｜ Put Wall 47（+1.5%）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 62.7%｜历史 Rank 42%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,441 股

📆 10-16 Forward Structure
存量OI: C 20.3k / P 16.6k，今日变化ΔOI: C +0.7k / P +91，平值价格ATM: C $1.31 / P $1.75 ｜ ATM IV 53.2%，净 delta 敞口 5k shares
Top ΔOI: C 50 +133 ｜ P 48 +113
仓位参考: Max Pain 50 ｜ Call Wall 50（+8.0%，弱）（OI 4.2k） ｜ Put Wall 45（-2.8%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 53.2%｜历史 Rank 42%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 正 4,573 股

10-23（MEDIUM △）Top ΔOI: 47C +72
10-23（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+8.0%，弱）（OI 0.2k） ｜ Put Wall 45（-2.8%，弱）（OI 0.2k）

📆 10-30 Forward Structure
存量OI: C 4.7k / P 3.6k，今日变化ΔOI: C +0.3k / P +1.5k，平值价格ATM: C $2.65 / P $2.34 ｜ ATM IV 53.8%，净 delta 敞口 -42k shares
Top ΔOI: P 44 +1,505
仓位参考: Max Pain 48 ｜ Call Wall 50（+8.0%，弱）（OI 0.3k） ｜ Put Wall 44（-5.0%）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 53.8%｜历史 Rank 42%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 41,620 股

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 62.7% vs 10-16 53.2%（差 +9.5pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/MP_evening.json