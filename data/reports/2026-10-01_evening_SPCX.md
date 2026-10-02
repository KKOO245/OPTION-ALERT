# 期权晚报 2026-10-01（快照 21:00 ET）

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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 150.45 → 收盘 148.07（-1.6%） ｜ 今日高 153.78 ｜ 低 146.03 ｜ 昨收 150.86 → 收盘 148.07（-1.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-06，窗口结束前不做对错判定）

Options: P/C成交量 0.62 | OI比 1.02 | ATM IV 47.4% | Skew 0.1pp | Term 0.89 | ExpMove ±2.0%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价薄（Skew 0.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.02×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.0% ｜ 10-09（8D）±4.8% ｜ 10-16（15D）±6.5% ｜ 10-23（22D）±7.3%
   ⇒ IV–VIX Spread: +31.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,049,419 | GEX Change vs 上次快照 -75,229,488 | Flip: Primary Flip: 148.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 534 / LOW 102 / INVALID 286
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 148.11（全链重定价，覆盖 100%）
Call Wall 160（现价低于该位 7.5%）
最近结构参考: Flip 148（现价低于该位 0.0%）
量化视角： 负 Gamma（105万，无历史分位）｜由正转负（7523万）｜现价位于 Flip 下方 0.03%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（MaxPain，仅结算参考） / 160（Call Wall）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 8D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 15D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 10-02 Forward Structure
存量OI: C 205.0k / P 208.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.55 / P $1.46 ｜ ATM IV 47.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 150 ｜ Call Wall 160（+8.1%，弱）（OI 24.9k） ｜ Put Wall 140（-5.5%，弱）（OI 18.8k）
量化解读： 存量两侧均衡｜ATM IV 47.3%｜历史 Rank 16%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-09（Activity LOW）仓位参考: Max Pain 150 ｜ Call Wall 160（+8.1%，弱）（OI 6.7k） ｜ Put Wall 135（-8.8%，弱）（OI 5.5k）

10-16（Activity LOW）仓位参考: Max Pain 143 ｜ Call Wall 160（+8.1%）（OI 42.7k） ｜ Put Wall 135（-8.8%，弱）（OI 30.3k）

10-23（Activity LOW）仓位参考: Max Pain 148 ｜ Call Wall 150（+1.3%，弱）（OI 3.5k） ｜ Put Wall 140（-5.5%）（OI 4.1k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 47.3% vs 10-09 40.6%（差 +6.8pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=39 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=39）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/SPCX_evening.json