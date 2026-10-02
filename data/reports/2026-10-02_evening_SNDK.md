# 期权晚报 2026-10-02（快照 16:40 ET）

📊 市场环境

SPY $769.64 ｜ QQQ $749.58
VIX 15.31 ↓6.6%（5D +3.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 1690.2）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,773.12 → 收盘 1,719.99（-3.0%） ｜ 今日高 1774.23 ｜ 低 1713.47 ｜ 昨收 1,787.69 → 收盘 1,719.99（-3.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.55 | OI比 0.81 | ATM IV 39.1% | Skew 1.4pp | Term 1.67 | ExpMove ±6.0%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常偏陡（Term 1.67）｜保护溢价薄（Skew 1.4pp）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（7D）±6.0% ｜ 10-16（14D）±8.8% ｜ 10-23（21D）±11.1% ｜ 10-30（28D）±14.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 2,139,598 | GEX Change vs 上次快照 -3,355,472 | Flip: Candidates 1690.15 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 77%（带内） ｜ IV 有效性: VALID 1527 / LOW 484 / INVALID 1267
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈1690（全链重定价，覆盖 77%，CONDITIONAL）
最近结构参考: Flip 1690（现价高于该位 1.8%）
量化视角： 正 Gamma（214万，无历史分位）｜正 Gamma 减弱（336万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,715（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1690（全链重定价，覆盖 77%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +3.0k / P +5.2k ｜ Activity HIGH ｜ 7D
10-16  C +1.1k / P +1.0k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +1.4k / P +0.4k ｜ Activity HIGH ｜ 21D
10-30  C +0.2k / P +0.3k ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 17.4k / P 19.7k，今日变化ΔOI: C +3.0k / P +5.2k，平值价格ATM: C $52.40 / P $51.08 ｜ ATM IV 54.2%，净 delta 敞口 -7k shares
Top ΔOI: C 1900 +380
仓位参考: Max Pain 1,675 ｜ Call Wall 1800（+4.7%，弱）（OI 0.6k） ｜ Put Wall 1800（+4.7%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 54.2%｜历史 Rank 20%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 6,854 股

10-16（MEDIUM △）Top ΔOI: 1670P +206
10-16（MEDIUM △）仓位参考: Max Pain 1,670 ｜ Call Wall 1800（+4.7%，弱）（OI 1.1k） ｜ Put Wall 1600（-7.0%，弱）（OI 1.3k）

📆 10-23 Forward Structure
存量OI: C 6.6k / P 7.9k，今日变化ΔOI: C +1.4k / P +0.4k，平值价格ATM: C $100.50 / P $90.30 ｜ ATM IV 58.0%，净 delta 敞口 18k shares
Top ΔOI: C 2290 +170 ｜ C 1900 +87
仓位参考: Max Pain 1,740 ｜ Call Wall 1800（+4.7%，弱）（OI 0.3k） ｜ Put Wall 1650（-4.1%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 58.0%｜历史 Rank 20%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 18,233 股

📆 10-30 Forward Structure
存量OI: C 4.2k / P 7.4k，今日变化ΔOI: C +0.2k / P +0.3k，平值价格ATM: C $127.30 / P $121.70 ｜ ATM IV 65.2%，净 delta 敞口 -6k shares
Top ΔOI: C 1860 +50 ｜ C 2250 +48 ｜ P 1560 +40
仓位参考: Max Pain 1,725 ｜ Call Wall 1700（-1.2%，弱）（OI 0.1k） ｜ Put Wall 1600（-7.0%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 65.2%｜历史 Rank 20%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 负 6,320 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/SNDK_evening.json