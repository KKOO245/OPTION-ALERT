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
🔴 **事件差分**: 10-02（1D）ATM IV 107.3% vs 10-09 71.0%（差 +36.3pp），覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-02 16C ΔOI +48（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 15.87 → 收盘 15.73（-0.9%） ｜ 今日高 16.15 ｜ 低 15.52 ｜ 昨收 15.85 → 收盘 15.73（-0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.47 | OI比 0.40 | ATM IV 107.3% | Skew -1.1pp | Term 0.67 | ExpMove ±6.4%（近端） | Rank 49%
量化视角： IV 中性（Rank 49%）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±6.4% ｜ 10-09（8D）±7.6% ｜ 10-16（15D）±12.7% ｜ 10-23（22D）±13.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 332,094 | GEX Change vs 上次快照 34,605 | Flip: Primary Flip: 15.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 200 / LOW 101 / INVALID 135
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 15.49（全链重定价，覆盖 84%）
Put Wall 15（现价高于该位 4.9%）
最近结构参考: Flip 15（现价高于该位 1.5%）
量化视角： 正 Gamma（33万，无历史分位）｜正 Gamma 增强（+3万）｜现价位于 Flip 上方 1.52%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0.3k / P -19 ｜ Activity MEDIUM △ ｜ 1D
10-09  C +0.1k / P +34 ｜ Activity MEDIUM △ ｜ 8D
10-16  C +26 / P -0.1k ｜ Activity MEDIUM △ ｜ 15D
10-23  C +1 / P +13 ｜ Activity LOW ｜ 22D

📆 10-02 Forward Structure
存量OI: C 5.8k / P 2.3k，今日变化ΔOI: C +0.3k / P -19，平值价格ATM: C $0.70 / P $0.30 ｜ ATM IV 107.3%，净 delta 敞口 6k shares
Top ΔOI: C 17 +190 ｜ C 16 +48
仓位参考: Max Pain 17 ｜ Call Wall 17（+8.1%，弱）（OI 0.6k） ｜ Put Wall 15.5（-1.5%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 107.3%｜历史 Rank 49%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,254 股

10-09（MEDIUM △）Top ΔOI: 15P +24
10-09（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 15（-4.6%）（OI 0.4k）

10-16（MEDIUM △）Top ΔOI: 23P -202 ｜ 15P +50
10-16（MEDIUM △）仓位参考: Max Pain 19 ｜ Put Wall 15（-4.6%，弱）（OI 0.8k）

10-23（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 16（+1.7%）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 107.3% vs 10-09 71.0%（差 +36.3pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/NNE_evening.json