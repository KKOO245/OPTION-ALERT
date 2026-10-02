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


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 186.07 → 收盘 189.29（+1.7%） ｜ 今日高 192.30 ｜ 低 185.88 ｜ 昨收 186.41 → 收盘 189.29（+1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.16 | OI比 0.58 | ATM IV 68.0% | Skew -7.4pp | Term 0.95 | ExpMove ±2.9%（近端） | Rank 27%
量化视角： IV 中性（Rank 27%）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -7.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.16×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.9% ｜ 10-09（8D）±6.9% ｜ 10-16（15D）±9.5% ｜ 10-23（22D）±11.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,327,260 | GEX Change vs 上次快照 2,018,927 | Flip: Primary Flip: 183.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 509 / LOW 140 / INVALID 243
结构观察区: Primary Flip 183.56（全链重定价，覆盖 99%）
Call Wall 202（弱结构｜现价低于该位 6.5%）
最近结构参考: Flip 184（现价高于该位 3.1%）
量化视角： 正 Gamma（1433万，无历史分位）｜正 Gamma 增强（+202万）｜现价位于 Flip 上方 3.12%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 190（MaxPain，仅结算参考） / 202（Call Wall，弱结构）。
• Gamma 区域：切换参考 184（全链重定价，覆盖 99%）。
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
存量OI: C 78.0k / P 45.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.41 / P $3.05 ｜ ATM IV 68.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 190 ｜ Call Wall 202.5（+7.0%，弱）（OI 16.1k） ｜ Put Wall 180（-4.9%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 68.0%｜历史 Rank 27%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-09（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 200（+5.7%）（OI 2.9k）

10-16（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 200（+5.7%，弱）（OI 6.4k） ｜ Put Wall 200（+5.7%，弱）（OI 3.9k）

10-23（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 190（+0.4%，弱）（OI 0.5k） ｜ Put Wall 192.5（+1.7%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 68.0% vs 10-09 58.7%（差 +9.4pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/COIN_evening.json