# 期权晚报 2026-10-06（快照 21:00 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 156.87 → 收盘 150.90（-3.8%） ｜ 今日高 157.47 ｜ 低 149.68 ｜ 昨收 156.19 → 收盘 150.90（-3.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-09，窗口结束前不做对错判定）

Options: P/C成交量 1.01 | OI比 2.54 | ATM IV 38.8% | Skew 3.7pp | Term 0.84 | ExpMove ±2.7%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价中性（Skew 3.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.54×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±2.7% ｜ 10-16（10D）±4.5% ｜ 10-23（17D）±6.0% ｜ 10-30（24D）±3.2%
   ⇒ IV–VIX Spread: +23.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -52,042,901 | GEX Change vs 上次快照 -6,350,131 | Flip: Primary Flip: 165.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 327 / LOW 90 / INVALID 317
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 165.47（全链重定价，覆盖 95%）
Put Wall 150（现价高于该位 0.6%）
最近结构参考: Put Wall 150（现价高于该位 0.6%）
量化视角： 负 Gamma（5204万，无历史分位）｜负 Gamma 加深（635万）｜现价位于 Flip 下方 8.81%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall）；上方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 10D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 10-09 Forward Structure
存量OI: C 4.3k / P 10.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.95 / P $2.19 ｜ ATM IV 38.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 155 ｜ Call Wall 145（-3.9%）（OI 1.0k） ｜ Put Wall 148（-1.9%，弱）（OI 3.3k）
量化解读： 存量 Put 重｜ATM IV 38.8%｜历史 Rank 80%（近端代理）｜IV/RV 1.58×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-16（Activity LOW）仓位参考: Max Pain 160 ｜ Put Wall 150（-0.6%）（OI 22.6k）

10-23（Activity LOW）仓位参考: Max Pain 155 ｜ Call Wall 154（+2.1%，弱）（OI 84） ｜ Put Wall 153（+1.4%，弱）（OI 0.4k）

10-30（Activity LOW）仓位参考: Max Pain 156 ｜ Call Wall 159（+5.4%，弱）（OI 0.4k） ｜ Put Wall 150（-0.6%，弱）（OI 7.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/XBI_evening.json