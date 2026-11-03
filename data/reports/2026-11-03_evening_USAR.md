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
🟡 **近现价集中开仓**: 11-20 9P ΔOI +509（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 8.94 → 收盘 8.71（-2.5%） ｜ 今日高 9.03 ｜ 低 8.57 ｜ 昨收 8.85 → 收盘 8.71（-1.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-06，窗口结束前不做对错判定）

Options: P/C成交量 0.19 | OI比 0.59 | ATM IV 116.6% | Skew -0.2pp | Term 0.84 | ExpMove ±8.3%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±8.3% ｜ 11-13（10D）±14.9% ｜ 11-20（17D）±18.5% ｜ 11-27（24D）±20.0%
   ⇒ IV–VIX Spread: +95.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -875,685 | GEX Change vs 上次快照 -195,752 | Flip: Primary Flip: 9.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 181 / LOW 59 / INVALID 156
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 9.16（全链重定价，覆盖 100%）
最近结构参考: Flip 9（现价低于该位 5.0%）
量化视角： 负 Gamma（88万，无历史分位）｜负 Gamma 加深（20万）｜现价位于 Flip 下方 4.96%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +3.3k / P +2.1k ｜ Activity HIGH ｜ 3D
11-13  C +0.5k / P -28 ｜ Activity HIGH ｜ 10D
11-20  C +1.1k / P +1.1k ｜ Activity HIGH ｜ 17D
11-27  C +25 / P +0.1k ｜ Activity HIGH ｜ 24D

📆 11-06 Forward Structure
存量OI: C 14.0k / P 8.2k，今日变化ΔOI: C +3.3k / P +2.1k，平值价格ATM: C $0.45 / P $0.27 ｜ ATM IV 116.6%，净 delta 敞口 -8k shares
Top ΔOI: P 8 +1,554
仓位参考: Max Pain 10 ｜ Call Wall 9.5（+9.1%，弱）（OI 0.9k） ｜ Put Wall 9（+3.3%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 116.6%｜历史 Rank 53%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 7,953 股

📆 11-13 Forward Structure
存量OI: C 10.2k / P 3.0k，今日变化ΔOI: C +0.5k / P -28，平值价格ATM: C $0.74 / P $0.56 ｜ ATM IV 113.1%，净 delta 敞口 14k shares
Top ΔOI: P 15 -103
仓位参考: Max Pain 10 ｜ Put Wall 9.5（+9.1%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 113.1%｜历史 Rank 53%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,387 股

📆 11-20 Forward Structure
存量OI: C 33.2k / P 28.3k，今日变化ΔOI: C +1.1k / P +1.1k，平值价格ATM: C $0.65 / P $0.96 ｜ ATM IV 106.5%，净 delta 敞口 -35k shares
Top ΔOI: P 9 +509 ｜ P 9 +501
仓位参考: Max Pain 12 ｜ Call Wall 9.5（+9.1%，弱）（OI 1.7k） ｜ Put Wall 9（+3.3%，弱）（OI 3.6k）
量化解读： 存量两侧均衡｜ATM IV 106.5%｜历史 Rank 53%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 35,499 股

📆 11-27 Forward Structure
存量OI: C 4.0k / P 2.5k，今日变化ΔOI: C +25 / P +0.1k，平值价格ATM: C $1.08 / P $0.66 ｜ ATM IV 96.5%，净 delta 敞口 -5k shares
Top ΔOI: P 9 +47 ｜ P 9 +24
仓位参考: Max Pain 10 ｜ Put Wall 9.5（+9.1%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 96.5%｜历史 Rank 53%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 4,947 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=72 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=72）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/USAR_evening.json