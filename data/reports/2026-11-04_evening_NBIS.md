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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 145.63 → 收盘 141.52（-2.8%） ｜ 今日高 152.88 ｜ 低 140.02 ｜ 昨收 151.64 → 收盘 141.52（-6.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-09，窗口结束前不做对错判定）

Options: P/C成交量 0.37 | OI比 0.53 | ATM IV 131.6% | Skew 4.8pp | Term 0.84 | ExpMove ±7.8%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价中性（Skew 4.8pp）｜存量 Call 偏重（OI比 0.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±7.8% ｜ 11-13（9D）±18.5% ｜ 11-20（16D）±20.8% ｜ 11-27（23D）±22.6%
   ⇒ IV–VIX Spread: +114.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,868,525 | GEX Change vs 上次快照 -2,426,532 | Flip: Primary Flip: 152.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 584 / LOW 60 / INVALID 92
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 152.64（全链重定价，覆盖 100%）
最近结构参考: Flip 153（现价低于该位 7.3%）
量化视角： 负 Gamma（787万，无历史分位）｜负 Gamma 加深（243万）｜现价位于 Flip 下方 7.29%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 160（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +8.3k / P +2.5k ｜ Activity HIGH ｜ 2D
11-13  C +10.2k / P +1.0k ｜ Activity HIGH ｜ 9D
11-20  C +1.8k / P +0.6k ｜ Activity MEDIUM △ ｜ 16D
11-27  C +0.3k / P +11 ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 84.3k / P 44.9k，今日变化ΔOI: C +8.3k / P +2.5k，平值价格ATM: C $5.30 / P $5.74 ｜ ATM IV 131.6%，净 delta 敞口 121k shares
Top ΔOI: P 130 +1,410 ｜ C 150 +1,025
仓位参考: Max Pain 160 ｜ Call Wall 150（+6.0%，弱）（OI 4.0k） ｜ Put Wall 145（+2.5%）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 131.6%｜历史 Rank 82%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 120,946 股

📆 11-13 Forward Structure
存量OI: C 37.8k / P 28.6k，今日变化ΔOI: C +10.2k / P +1.0k，平值价格ATM: C $12.58 / P $13.55 ｜ ATM IV 143.6%，净 delta 敞口 35k shares
Top ΔOI: C 230 +3,285 ｜ C 220 +1,515
仓位参考: Max Pain 190 ｜ Put Wall 130（-8.1%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜ATM IV 143.6%｜历史 Rank 82%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 34,969 股

11-20（MEDIUM △）Top ΔOI: 200C +970 ｜ 130P +373
11-20（MEDIUM △）仓位参考: Max Pain 180 ｜ Put Wall 150（+6.0%，弱）（OI 7.4k）

11-27（MEDIUM △）Top ΔOI: 140P -68 ｜ 165P +39
11-27（MEDIUM △）仓位参考: Max Pain 180 ｜ Call Wall 150（+6.0%，弱）（OI 0.6k） ｜ Put Wall 155（+9.5%，弱）（OI 1.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=83 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=83）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/NBIS_evening.json