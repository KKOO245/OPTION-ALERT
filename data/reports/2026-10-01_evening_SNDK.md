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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,736.19 → 收盘 1,787.69（+3.0%） ｜ 今日高 1802.00 ｜ 低 1708.00 ｜ 昨收 1,739.89 → 收盘 1,787.69（+2.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.55 | OI比 0.80 | ATM IV 69.7% | Skew -2.7pp | Term 1.01 | ExpMove ±2.9%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.9% ｜ 10-09（8D）±7.4% ｜ 10-16（15D）±10.3% ｜ 10-23（22D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,327,484 | GEX Change vs 上次快照 7,833,691 | Flip: Primary Flip: 1710.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1801 / LOW 495 / INVALID 982
结构观察区: Primary Flip 1710.70（全链重定价，覆盖 99%）
最近结构参考: Flip 1711（现价高于该位 4.5%）
量化视角： 正 Gamma（1233万，无历史分位）｜正 Gamma 增强（+783万）｜现价位于 Flip 上方 4.50%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,700（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1711（全链重定价，覆盖 99%）。
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
存量OI: C 51.8k / P 41.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $25.62 / P $26.95 ｜ ATM IV 69.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 1,700 ｜ Call Wall 1900（+6.3%，弱）（OI 3.4k） ｜ Put Wall 1700（-4.9%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 69.7%｜历史 Rank 24%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-09（Activity LOW）仓位参考: Max Pain 1,655 ｜ Call Wall 1900（+6.3%，弱）（OI 0.5k） ｜ Put Wall 1800（+0.7%，弱）（OI 0.8k）

10-16（Activity LOW）仓位参考: Max Pain 1,660 ｜ Call Wall 1900（+6.3%，弱）（OI 1.2k） ｜ Put Wall 1700（-4.9%，弱）（OI 1.2k）

10-23（Activity LOW）仓位参考: Max Pain 1,745 ｜ Call Wall 1840（+2.9%，弱）（OI 0.2k） ｜ Put Wall 1650（-7.7%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 69.7% vs 10-09 61.8%（差 +7.9pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/SNDK_evening.json