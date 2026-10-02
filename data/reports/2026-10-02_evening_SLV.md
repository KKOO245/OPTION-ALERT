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
🟡 **近现价集中开仓**: 10-05 57C ΔOI +438（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-12 54P ΔOI +2,083 占该期限总 OI 37.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 55.46 → 收盘 54.74（-1.3%） ｜ 今日高 55.67 ｜ 低 53.90 ｜ 昨收 55.02 → 收盘 54.74（-0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.62 | OI比 0.44 | ATM IV 34.1% | Skew -32.9pp | Term 0.95 | ExpMove ±1.6%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -32.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-05（3D）±1.6% ｜ 10-07（5D）±2.6% ｜ 10-09（7D）±3.2% ｜ 10-12（10D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 17,365,332 | GEX Change vs 上次快照 -34,972,665 | Flip: Primary Flip: 53.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 660 / LOW 128 / INVALID 422
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 53.99（全链重定价，覆盖 87%）
Put Wall 50（弱结构｜现价高于该位 9.5%） | Call Wall 60（弱结构｜现价低于该位 8.8%）
最近结构参考: Flip 54（现价高于该位 1.4%）
量化视角： 正 Gamma（1737万，无历史分位）｜正 Gamma 减弱（3497万）｜现价位于 Flip 上方 1.38%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 55（MaxPain，仅结算参考） / 60（Call Wall，弱结构）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-05  C +1.5k / P +0.7k ｜ Activity HIGH ｜ 3D
10-07  C +1.8k / P +2.3k ｜ Activity HIGH ｜ 5D
10-09  C +5.3k / P +0.7k ｜ Activity HIGH ｜ 7D
10-12  C +0.2k / P +3.3k ｜ Activity HIGH ｜ 10D

📆 10-05 Forward Structure
存量OI: C 9.9k / P 7.2k，今日变化ΔOI: C +1.5k / P +0.7k，平值价格ATM: C $0.55 / P $0.34 ｜ ATM IV 22.6%，净 delta 敞口 37k shares
Top ΔOI: C 57 +438 ｜ P 59 -405 ｜ C 55 +394
仓位参考: Max Pain 56 ｜ Call Wall 60（+9.6%，弱）（OI 1.2k） ｜ Put Wall 52（-5.0%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 22.6%｜历史 Rank 54%（近端代理）｜IV/RV 0.58×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 36,946 股

📆 10-07 Forward Structure
存量OI: C 18.5k / P 7.3k，今日变化ΔOI: C +1.8k / P +2.3k，平值价格ATM: C $0.84 / P $0.58 ｜ ATM IV 28.1%，净 delta 敞口 17k shares
Top ΔOI: P 52 +1,475 ｜ C 55 +625 ｜ C 57 +357
仓位参考: Max Pain 56 ｜ Call Wall 58（+6.0%，弱）（OI 3.0k） ｜ Put Wall 52（-5.0%）（OI 1.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 28.1%｜历史 Rank 54%（近端代理）｜IV/RV 0.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 17,335 股

📆 10-09 Forward Structure
存量OI: C 73.5k / P 18.4k，今日变化ΔOI: C +5.3k / P +0.7k，平值价格ATM: C $0.99 / P $0.77 ｜ ATM IV 30.0%，净 delta 敞口 105k shares
Top ΔOI: C 55 +1,230 ｜ C 58 +621
仓位参考: Max Pain 56 ｜ Call Wall 60（+9.6%，弱）（OI 4.6k） ｜ Put Wall 55（+0.5%，弱）（OI 2.7k）
量化解读： 存量 Call 重｜ATM IV 30.0%｜历史 Rank 54%（近端代理）｜IV/RV 0.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 104,711 股

📆 10-12 Forward Structure
存量OI: C 1.7k / P 3.9k，今日变化ΔOI: C +0.2k / P +3.3k，平值价格ATM: C $1.05 / P $0.96 ｜ ATM IV 27.7%，净 delta 敞口 -111k shares
Top ΔOI: P 54 +2,083 ｜ P 52 +868 ｜ P 55 +241
仓位参考: Max Pain 55 ｜ Call Wall 58（+6.0%，弱）（OI 0.4k） ｜ Put Wall 54（-1.4%）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 27.7%｜历史 Rank 54%（近端代理）｜IV/RV 0.71×（近似）｜净 delta 敞口 负 111,342 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/SLV_evening.json