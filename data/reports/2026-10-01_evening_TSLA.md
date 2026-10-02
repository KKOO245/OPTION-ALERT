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
🔴 **事件差分**: 10-02（1D）ATM IV 59.7% vs 10-05 38.5%（差 +21.2pp），覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 356.81 → 收盘 354.11（-0.8%） ｜ 今日高 359.79 ｜ 低 353.80 ｜ 昨收 354.81 → 收盘 354.11（-0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.56 | OI比 0.99 | ATM IV 59.7% | Skew -2.0pp | Term 0.76 | ExpMove ±2.5%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.5% ｜ 10-05（4D）±3.2% ｜ 10-07（6D）±4.1% ｜ 10-09（8D）±4.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 50,163,505 | GEX Change vs 上次快照 -1,763,284 | Flip: Primary Flip: 348.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1210 / LOW 122 / INVALID 528
结构观察区: Primary Flip 348.27（全链重定价，覆盖 99%）
最近结构参考: Flip 348（现价高于该位 1.7%）
量化视角： 正 Gamma（5016万，无历史分位）｜正 Gamma 减弱（176万）｜现价位于 Flip 上方 1.68%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 360（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 348（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-05  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-07  C +0 / P +0 ｜ Activity LOW ｜ 6D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 10-02 Forward Structure
存量OI: C 275.3k / P 273.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.15 / P $4.75 ｜ ATM IV 59.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 360 ｜ Call Wall 360（+1.7%，弱）（OI 17.5k） ｜ Put Wall 350（-1.2%，弱）（OI 7.3k）
量化解读： 存量两侧均衡｜ATM IV 59.7%｜历史 Rank 71%（近端代理）｜IV/RV 2.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-05（Activity LOW）仓位参考: Max Pain 355 ｜ Call Wall 377.5（+6.6%）（OI 15.8k） ｜ Put Wall 325（-8.2%，弱）（OI 1.3k）

10-07（Activity LOW）仓位参考: Max Pain 355 ｜ Call Wall 375（+5.9%，弱）（OI 1.1k） ｜ Put Wall 360（+1.7%，弱）（OI 0.5k）

10-09（Activity LOW）仓位参考: Max Pain 355 ｜ Call Wall 370（+4.5%，弱）（OI 3.7k） ｜ Put Wall 350（-1.2%，弱）（OI 2.3k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 59.7% vs 10-05 38.5%（差 +21.2pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/TSLA_evening.json