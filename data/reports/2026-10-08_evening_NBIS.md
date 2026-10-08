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
🟡 **事件差分**: 10-09 ATM IV 83.2% vs 10-16 71.5%（差 +11.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 225P ΔOI -3,202（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 233.13 → 收盘 219.71（-5.8%） ｜ 今日高 234.15 ｜ 低 217.73 ｜ 昨收 237.15 → 收盘 219.71（-7.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-13，窗口结束前不做对错判定）

Options: P/C成交量 0.56 | OI比 0.86 | ATM IV 83.2% | Skew 2.0pp | Term 0.85 | ExpMove ±3.5%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价薄（Skew 2.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.5% ｜ 10-16（8D）±8.5% ｜ 10-23（15D）±11.6% ｜ 10-30（22D）±13.9%
   ⇒ IV–VIX Spread: +67.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -18,497,680 | GEX Change vs 上次快照 -5,276,382 | Flip: Primary Flip: 230.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 503 / LOW 45 / INVALID 144
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 230.39（全链重定价，覆盖 97%）
Put Wall 220（弱结构｜现价低于该位 0.1%）
最近结构参考: Put Wall 220（现价低于该位 0.1%）
量化视角： 负 Gamma（1850万，无历史分位）｜负 Gamma 加深（528万）｜现价位于 Flip 下方 4.64%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 220（Put Wall，弱结构） / 238（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 230（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +4.7k / P -3.3k ｜ Activity HIGH ｜ 1D
10-16  C +4.8k / P +5.2k ｜ Activity HIGH ｜ 8D
10-23  C +2.4k / P +1.4k ｜ Activity HIGH ｜ 15D
10-30  C +0.9k / P +2.5k ｜ Activity HIGH ｜ 22D

📆 10-09 Forward Structure
存量OI: C 58.7k / P 50.5k，今日变化ΔOI: C +4.7k / P -3.3k，平值价格ATM: C $3.81 / P $3.85 ｜ ATM IV 83.2%，净 delta 敞口 302k shares
Top ΔOI: P 225 -3,202 ｜ C 237 +938
仓位参考: Max Pain 238 ｜ Call Wall 240（+9.2%，弱）（OI 3.4k） ｜ Put Wall 225（+2.4%，弱）（OI 5.9k）
量化解读： 存量两侧均衡｜ATM IV 83.2%｜历史 Rank 14%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 301,687 股

📆 10-16 Forward Structure
存量OI: C 95.9k / P 105.7k，今日变化ΔOI: C +4.8k / P +5.2k，平值价格ATM: C $9.40 / P $9.30 ｜ ATM IV 71.5%，净 delta 敞口 -111k shares
Top ΔOI: C 270 -2,275 ｜ C 250 +2,201 ｜ P 220 +1,917
仓位参考: Max Pain 228 ｜ Call Wall 240（+9.2%，弱）（OI 6.0k） ｜ Put Wall 220（+0.1%，弱）（OI 7.8k）
量化解读： 存量两侧均衡｜ATM IV 71.5%｜历史 Rank 14%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 110,549 股

📆 10-23 Forward Structure
存量OI: C 15.2k / P 11.8k，今日变化ΔOI: C +2.4k / P +1.4k，平值价格ATM: C $12.97 / P $12.48 ｜ ATM IV 70.4%，净 delta 敞口 21k shares
Top ΔOI: C 240 +638 ｜ C 245 +557 ｜ C 255 +398
仓位参考: Max Pain 225 ｜ Call Wall 240（+9.2%，弱）（OI 1.0k） ｜ Put Wall 200（-9.0%）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 70.4%｜历史 Rank 14%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 20,704 股

📆 10-30 Forward Structure
存量OI: C 18.3k / P 15.3k，今日变化ΔOI: C +0.9k / P +2.5k，平值价格ATM: C $15.48 / P $15.00 ｜ ATM IV 70.9%，净 delta 敞口 -49k shares
Top ΔOI: P 200 +715 ｜ C 300 +712 ｜ C 320 -550
仓位参考: Max Pain 235 ｜ Call Wall 235（+7.0%，弱）（OI 0.6k） ｜ Put Wall 200（-9.0%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.9%｜历史 Rank 14%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 负 49,154 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 83.2% vs 10-16 71.5%（差 +11.8pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/NBIS_evening.json