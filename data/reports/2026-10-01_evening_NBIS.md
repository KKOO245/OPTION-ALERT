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
🟡 **近现价集中开仓**: 10-02 235C ΔOI -3,593（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 242C ΔOI +6,208 占该期限总 OI 12.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 236.07 → 收盘 232.28（-1.6%） ｜ 今日高 239.63 ｜ 低 228.47 ｜ 昨收 235.88 → 收盘 232.28（-1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.44 | OI比 0.66 | ATM IV 82.6% | Skew -2.9pp | Term 0.91 | ExpMove ±3.6%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -2.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±3.6% ｜ 10-09（8D）±8.4% ｜ 10-16（15D）±11.6% ｜ 10-23（22D）±14.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,789,510 | GEX Change vs 上次快照 1,728,172 | Flip: Primary Flip: 226.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 522 / LOW 49 / INVALID 127
结构观察区: Primary Flip 226.41（全链重定价，覆盖 98%）
Put Wall 210（弱结构｜现价高于该位 10.6%）
最近结构参考: Flip 226（现价高于该位 2.6%）
量化视角： 正 Gamma（879万，无历史分位）｜正 Gamma 增强（+173万）｜现价位于 Flip 上方 2.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 210（Put Wall，弱结构） / 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 226（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C -0.1k / P -1.9k ｜ Activity MEDIUM △ ｜ 1D
10-09  C +10.1k / P +4.7k ｜ Activity HIGH ｜ 8D
10-16  C +2.6k / P +0.6k ｜ Activity HIGH ｜ 15D
10-23  C +38 / P +16 ｜ Activity LOW ｜ 22D

📆 10-02 Forward Structure
存量OI: C 64.8k / P 42.5k，今日变化ΔOI: C -0.1k / P -1.9k，平值价格ATM: C $4.20 / P $4.25 ｜ ATM IV 82.6%，净 delta 敞口 -153k shares
Top ΔOI: C 235 -3,593 ｜ P 220 -1,778 ｜ P 210 -1,445
仓位参考: Max Pain 230 ｜ Call Wall 250（+7.6%，弱）（OI 6.3k） ｜ Put Wall 210（-9.6%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 82.6%｜历史 Rank 12%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 152,899 股

📆 10-09 Forward Structure
存量OI: C 30.7k / P 21.0k，今日变化ΔOI: C +10.1k / P +4.7k，平值价格ATM: C $9.75 / P $9.86 ｜ ATM IV 73.1%，净 delta 敞口 305k shares
Top ΔOI: C 242 +6,208 ｜ P 220 +2,081 ｜ C 207 +1,824
仓位参考: Max Pain 220 ｜ Call Wall 242.5（+4.4%）（OI 6.4k） ｜ Put Wall 220（-5.3%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 73.1%｜历史 Rank 12%（近端代理）｜IV/RV 1.26×（近似）｜净 delta 敞口 正 305,231 股

📆 10-16 Forward Structure
存量OI: C 68.6k / P 84.3k，今日变化ΔOI: C +2.6k / P +0.6k，平值价格ATM: C $13.70 / P $13.30 ｜ ATM IV 74.1%，净 delta 敞口 53k shares
Top ΔOI: C 250 +1,194 ｜ C 300 +488 ｜ C 245 +285
仓位参考: Max Pain 220 ｜ Call Wall 250（+7.6%，弱）（OI 5.6k） ｜ Put Wall 210（-9.6%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 74.1%｜历史 Rank 12%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 53,003 股

10-23（Activity LOW）仓位参考: Max Pain 230 ｜ Call Wall 240（+3.3%，弱）（OI 0.5k） ｜ Put Wall 210（-9.6%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 82.6% vs 10-09 73.1%（差 +9.4pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/NBIS_evening.json