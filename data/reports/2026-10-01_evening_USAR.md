# 期权晚报 2026-10-01（快照 16:40 ET）

📊 市场环境

SPY $763.99 ｜ QQQ $742.03
VIX 16.39 ↑0.3%（5D +4.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 82.4% vs 10-09 67.5%（差 +14.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 14.09 → 收盘 13.80（-2.0%） ｜ 今日高 14.20 ｜ 低 13.47 ｜ 昨收 14.08 → 收盘 13.80（-2.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-06，窗口结束前不做对错判定）

Options: P/C成交量 2.56 | OI比 0.43 | ATM IV 82.4% | Skew -2.4pp | Term 0.78 | ExpMove ±3.3%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.4pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.43）+ 当日成交偏 Put（P/C量 2.56）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.56×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.43×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±3.3% ｜ 10-09（8D）±7.6% ｜ 10-16（15D）±11.2% ｜ 10-23（22D）±13.3%
   ⇒ IV–VIX Spread: +66.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,787,572 | GEX Change N/A | Flip: Primary Flip: 14.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 215 / LOW 80 / INVALID 109
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 14.16（全链重定价，覆盖 96%）
Put Wall 15（弱结构｜现价低于该位 8.0%）
最近结构参考: Flip 14（现价低于该位 2.5%）
量化视角： 负 Gamma（179万，无历史分位）｜现价位于 Flip 下方 2.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（Put Wall，弱结构） / 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +1.3k / P -0.5k ｜ Activity HIGH ｜ 1D
10-09  C +0.9k / P +0.2k ｜ Activity HIGH ｜ 8D
10-16  C +5.5k / P +0.3k ｜ Activity MEDIUM △ ｜ 15D
10-23  C +0.1k / P -2 ｜ Activity MEDIUM △ ｜ 22D

📆 10-02 Forward Structure
存量OI: C 26.7k / P 11.5k，今日变化ΔOI: C +1.3k / P -0.5k，平值价格ATM: C $0.14 / P $0.32 ｜ ATM IV 82.4%，净 delta 敞口 60k shares
Top ΔOI: P 16 -420 ｜ C 15 +383
仓位参考: Max Pain 16 ｜ Call Wall 15（+8.7%，弱）（OI 2.0k） ｜ Put Wall 14（+1.4%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 82.4%｜历史 Rank 10%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 60,438 股

📆 10-09 Forward Structure
存量OI: C 10.3k / P 6.5k，今日变化ΔOI: C +0.9k / P +0.2k，平值价格ATM: C $0.42 / P $0.63 ｜ ATM IV 67.5%，净 delta 敞口 6k shares
Top ΔOI: C 15 +214
仓位参考: Max Pain 16 ｜ Call Wall 15（+8.7%，弱）（OI 0.9k） ｜ Put Wall 14（+1.4%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 67.5%｜历史 Rank 10%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,848 股

10-16（MEDIUM △）Top ΔOI: 16C +4,770 ｜ 14C +206
10-16（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 15（+8.7%）（OI 5.6k）

10-23（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 15（+8.7%，弱）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 82.4% vs 10-09 67.5%（差 +14.9pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=38 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=38）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/USAR_evening.json