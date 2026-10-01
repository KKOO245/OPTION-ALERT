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
🔴 **事件差分**: 10-02（1D）ATM IV 45.2% vs 10-09 29.7%（差 +15.5pp），覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-09 400P ΔOI +11（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📦 月度归档提醒：上个月的数据归档已上传 GitHub Releases，请在 D:\git\Option Alert-数据储存 下载解压保存（以后仓库做月度清理时，归档就是完整副本）。


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 409.05 → 收盘 401.24（-1.9%） ｜ 今日高 410.52 ｜ 低 399.25 ｜ 昨收 406.63 → 收盘 401.24（-1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.30 | OI比 1.60 | ATM IV 45.2% | Skew 17.6pp | Term 0.98 | ExpMove ±2.0%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构正常（Term 0.98）｜保护溢价显著（Skew 17.6pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.30×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.60×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.0% ｜ 10-09（8D）±4.0% ｜ 10-16（15D）±4.7% ｜ 10-23（22D）±9.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,153,640 | GEX Change vs 上次快照 -410,715 | Flip: Primary Flip: 389.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 262 / LOW 176 / INVALID 424
结构观察区: Primary Flip 389.98（全链重定价，覆盖 93%）
Call Wall 420（弱结构｜现价低于该位 4.5%）
最近结构参考: Flip 390（现价高于该位 2.9%）
量化视角： 正 Gamma（215万，无历史分位）｜正 Gamma 减弱（41万）｜现价位于 Flip 上方 2.89%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 390（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +5 / P +70 ｜ Activity MEDIUM △ ｜ 1D
10-09  C +31 / P +67 ｜ Activity HIGH ｜ 8D
10-16  C +20 / P +0.1k ｜ Activity MEDIUM △ ｜ 15D
10-23  C +18 / P +12 ｜ Activity MEDIUM △ ｜ 22D

📆 10-02 Forward Structure
存量OI: C 2.2k / P 3.5k，今日变化ΔOI: C +5 / P +70，平值价格ATM: C $5.40 / P $2.50 ｜ ATM IV 45.2%，净 delta 敞口 -5k shares
Top ΔOI: C 425 +22 ｜ P 410 +13 ｜ P 397 +11
仓位参考: Max Pain 395 ｜ Call Wall 410（+2.2%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 45.2%｜历史 Rank 77%（近端代理）｜IV/RV 1.67×（近似）｜净 delta 敞口 负 4,600 股

📆 10-09 Forward Structure
存量OI: C 1.2k / P 0.4k，今日变化ΔOI: C +31 / P +67，平值价格ATM: C $8.30 / P $7.60 ｜ ATM IV 29.7%，净 delta 敞口 -3k shares
Top ΔOI: P 417 +20 ｜ P 400 +11 ｜ P 420 +11
仓位参考: Max Pain 380 ｜ Call Wall 420（+4.7%，弱）（OI 0.1k） ｜ Put Wall 417.5（+4.1%，弱）（OI 21）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 29.7%｜历史 Rank 77%（近端代理）｜IV/RV 1.09×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 3,198 股

10-16（MEDIUM △）Top ΔOI: 420C +34 ｜ 410P +21
10-16（MEDIUM △）仓位参考: Max Pain 390 ｜ Call Wall 400（-0.3%，弱）（OI 0.9k） ｜ Put Wall 380（-5.3%，弱）（OI 0.6k）

10-23（MEDIUM △）Top ΔOI: 410C +14 ｜ 375P +10
10-23（MEDIUM △）仓位参考: Max Pain 415 ｜ Call Wall 425（+5.9%）（OI 0.5k） ｜ Put Wall 415（+3.4%）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 45.2% vs 10-09 29.7%（差 +15.5pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/ISRG_evening.json