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
🟡 **近现价集中开仓**: 10-02 190P ΔOI +1,769（距现价 -0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 190.18 → 收盘 190.04（-0.1%） ｜ 今日高 191.80 ｜ 低 186.60 ｜ 昨收 187.05 → 收盘 190.04（+1.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.38 | OI比 0.64 | ATM IV 46.5% | Skew -1.0pp | Term 0.95 | ExpMove ±1.9%（近端） | Rank 23%
量化视角： IV 历史低位（Rank 23%，期权偏便宜）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -1.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±1.9% ｜ 10-09（8D）±4.9% ｜ 10-16（15D）±6.9% ｜ 10-23（22D）±8.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 59,089,516 | GEX Change vs 上次快照 -6,700,433 | Flip: Primary Flip: 183.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 558 / LOW 123 / INVALID 155
结构观察区: Primary Flip 183.66（全链重定价，覆盖 100%）
Call Wall 200（现价低于该位 5.0%）
最近结构参考: Flip 184（现价高于该位 3.5%）
量化视角： 正 Gamma（5909万，无历史分位）｜正 Gamma 减弱（670万）｜现价位于 Flip 上方 3.47%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）；上方 200（Call Wall）。
• Gamma 区域：切换参考 184（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +4 / P +3.4k ｜ Activity MEDIUM △ ｜ 1D
10-09  C +5.9k / P +2.0k ｜ Activity HIGH ｜ 8D
10-16  C +2.6k / P +0.6k ｜ Activity MEDIUM △ ｜ 15D
10-23  C +0.5k / P +0.6k ｜ Activity HIGH ｜ 22D

📆 10-02 Forward Structure
存量OI: C 132.3k / P 85.2k，今日变化ΔOI: C +4 / P +3.4k，平值价格ATM: C $1.87 / P $1.81 ｜ ATM IV 46.5%，净 delta 敞口 -115k shares
Top ΔOI: P 190 +1,769 ｜ P 187 +1,681 ｜ C 207 -1,068
仓位参考: Max Pain 185 ｜ Call Wall 200（+5.2%）（OI 25.7k） ｜ Put Wall 185（-2.7%，弱）（OI 7.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 46.5%｜历史 Rank 23%（近端代理）｜IV/RV 1.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 115,366 股

📆 10-09 Forward Structure
存量OI: C 36.6k / P 44.9k，今日变化ΔOI: C +5.9k / P +2.0k，平值价格ATM: C $4.75 / P $4.55 ｜ ATM IV 41.6%，净 delta 敞口 169k shares
Top ΔOI: C 190 +1,258 ｜ C 187 +1,212 ｜ C 202 +648
仓位参考: Max Pain 185 ｜ Call Wall 200（+5.2%）（OI 5.0k） ｜ Put Wall 190（-0.0%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.6%｜历史 Rank 23%（近端代理）｜IV/RV 1.59×（近似）｜净 delta 敞口 正 169,468 股

10-16（MEDIUM △）Top ΔOI: 190C +1,001 ｜ 175P +476
10-16（MEDIUM △）仓位参考: Max Pain 168 ｜ Call Wall 200（+5.2%，弱）（OI 15.3k） ｜ Put Wall 175（-7.9%，弱）（OI 8.3k）

📆 10-23 Forward Structure
存量OI: C 20.9k / P 14.2k，今日变化ΔOI: C +0.5k / P +0.6k，平值价格ATM: C $8.45 / P $7.65 ｜ ATM IV 42.8%，净 delta 敞口 12k shares
Top ΔOI: C 190 +75
仓位参考: Max Pain 180 ｜ Call Wall 180（-5.3%）（OI 4.6k） ｜ Put Wall 175（-7.9%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.8%｜历史 Rank 23%（近端代理）｜IV/RV 1.63×（近似）｜净 delta 敞口 正 11,955 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/PLTR_evening.json