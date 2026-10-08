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
🟡 **近现价集中开仓**: 10-23 13C ΔOI +125（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 13.02 → 收盘 12.63（-3.0%） ｜ 今日高 13.29 ｜ 低 12.42 ｜ 昨收 13.23 → 收盘 12.63（-4.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-13，窗口结束前不做对错判定）

Options: P/C成交量 1.22 | OI比 0.30 | ATM IV 61.6% | Skew -6.6pp | Term 1.16 | ExpMove ±3.1%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构正常偏陡（Term 1.16）｜Put 保护异常便宜（Skew -6.6pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.30）+ 当日成交偏 Put（P/C量 1.22）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.22×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.1% ｜ 10-16（8D）±7.1% ｜ 10-23（15D）±11.3% ｜ 10-30（22D）±13.6%
   ⇒ IV–VIX Spread: +46.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,077,488 | GEX Change vs 上次快照 291,003 | Flip: Primary Flip: 13.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 180 / LOW 82 / INVALID 134
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 13.22（全链重定价，覆盖 91%）
最近结构参考: Flip 13（现价低于该位 4.5%）
量化视角： 负 Gamma（208万，无历史分位）｜负 Gamma 缓解（+29万）｜现价位于 Flip 下方 4.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 13（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.3k / P -1.7k ｜ Activity HIGH ｜ 1D
10-16  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 8D
10-23  C +0.6k / P -0.4k ｜ Activity HIGH ｜ 15D
10-30  C +35 / P +0.4k ｜ Activity HIGH ｜ 22D

📆 10-09 Forward Structure
存量OI: C 19.2k / P 5.8k，今日变化ΔOI: C +0.3k / P -1.7k，平值价格ATM: C $0.24 / P $0.15 ｜ ATM IV 61.6%，净 delta 敞口 177k shares
Top ΔOI: P 16 -1,010 ｜ P 15 -294
仓位参考: Max Pain 14 ｜ Put Wall 13（+2.9%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 61.6%｜历史 Rank 100%（近端代理）｜IV/RV 1.20×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 177,159 股

10-16（MEDIUM △）Top ΔOI: 13P +447 ｜ 18P -250
10-16（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（+2.9%，弱）（OI 1.6k）

📆 10-23 Forward Structure
存量OI: C 11.5k / P 5.4k，今日变化ΔOI: C +0.6k / P -0.4k，平值价格ATM: C $0.78 / P $0.65 ｜ ATM IV 65.3%，净 delta 敞口 55k shares
Top ΔOI: P 16 -255 ｜ P 17 -153 ｜ C 13 +125
仓位参考: Max Pain 16 ｜ Put Wall 13.5（+6.9%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 65.3%｜历史 Rank 100%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 正 54,506 股

📆 10-30 Forward Structure
存量OI: C 6.4k / P 8.5k，今日变化ΔOI: C +35 / P +0.4k，平值价格ATM: C $0.93 / P $0.79 ｜ ATM IV 67.2%，净 delta 敞口 -8k shares
Top ΔOI: P 12 +239
仓位参考: Max Pain 16 ｜ Put Wall 12.5（-1.0%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 67.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.31×（近似）｜净 delta 敞口 负 7,983 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/USAR_evening.json