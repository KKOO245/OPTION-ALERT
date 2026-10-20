# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 38.31 → 收盘 39.05（+1.9%） ｜ 今日高 40.16 ｜ 低 37.94 ｜ 昨收 38.95 → 收盘 39.05（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.89 | OI比 0.93 | ATM IV 66.1% | Skew -1.0pp | Term 1.00 | ExpMove ±4.9%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -1.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±4.9% ｜ 10-30（10D）±7.9% ｜ 11-06（17D）±14.0% ｜ 11-13（24D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,810,900 | GEX Change vs 上次快照 29,966 | Flip: Primary Flip: 41.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 280 / LOW 67 / INVALID 177
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 41.15（全链重定价，覆盖 98%）
Put Wall 40（弱结构｜现价低于该位 2.4%）
最近结构参考: Put Wall 40（现价低于该位 2.4%）
量化视角： 负 Gamma（281万，无历史分位）｜负 Gamma 缓解（+3万）｜现价位于 Flip 下方 5.11%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall，弱结构） / 42（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 41（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +2.8k / P -39 ｜ Activity HIGH ｜ 3D
10-30  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 10D
11-06  C +0.3k / P +0.1k ｜ Activity HIGH ｜ 17D
11-13  C +0.2k / P -38 ｜ Activity MEDIUM △ ｜ 24D

📆 10-23 Forward Structure
存量OI: C 9.1k / P 8.5k，今日变化ΔOI: C +2.8k / P -39，平值价格ATM: C $1.03 / P $0.90 ｜ ATM IV 66.1%，净 delta 敞口 98k shares
Top ΔOI: C 42 +766 ｜ P 42 -356
仓位参考: Max Pain 42 ｜ Call Wall 42（+7.6%，弱）（OI 1.0k） ｜ Put Wall 36.5（-6.5%）（OI 2.7k）
量化解读： 存量两侧均衡｜ATM IV 66.1%｜历史 Rank 50%（近端代理）｜IV/RV 1.34×（近似）｜净 delta 敞口 正 98,177 股

📆 10-30 Forward Structure
存量OI: C 7.2k / P 6.6k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $1.72 / P $1.35 ｜ ATM IV 61.8%，净 delta 敞口 -17k shares
Top ΔOI: P 42 +209 ｜ P 42 +137
仓位参考: Max Pain 45 ｜ Put Wall 42（+7.6%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 61.8%｜历史 Rank 50%（近端代理）｜IV/RV 1.25×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 16,686 股

📆 11-06 Forward Structure
存量OI: C 5.4k / P 3.6k，今日变化ΔOI: C +0.3k / P +0.1k，平值价格ATM: C $3.38 / P $2.10 ｜ ATM IV 71.1%，净 delta 敞口 -677 shares
仓位参考: Max Pain 43 ｜ Call Wall 40（+2.4%，弱）（OI 0.3k） ｜ Put Wall 38（-2.7%）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 71.1%｜历史 Rank 50%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 677 股

11-13（MEDIUM △）Top ΔOI: 39P -87
11-13（MEDIUM △）仓位参考: Max Pain 48 ｜ Put Wall 39（-0.1%）（OI 0.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/MP_evening.json