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
🟡 **近现价集中开仓**: 10-05 377C ΔOI -7,933（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-05 420C ΔOI +9,983 占该期限总 OI 10.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 360.08 → 收盘 370.59（+2.9%） ｜ 今日高 374.60 ｜ 低 359.41 ｜ 昨收 354.11 → 收盘 370.59（+4.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.80 | OI比 0.98 | ATM IV 23.9% | Skew -6.4pp | Term 1.82 | ExpMove ±1.8%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常偏陡（Term 1.82）｜Put 保护异常便宜（Skew -6.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-05（3D）±1.8% ｜ 10-07（5D）±3.0% ｜ 10-09（7D）±3.8% ｜ 10-12（10D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 165,178,065 | GEX Change vs 上次快照 -14,652,208 | Flip: Primary Flip: 345.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 1058 / LOW 149 / INVALID 653
结构观察区: Primary Flip 345.88（全链重定价，覆盖 83%）
Call Wall 400（弱结构｜现价低于该位 7.4%）
最近结构参考: Flip 346（现价高于该位 7.1%）
量化视角： 正 Gamma（1.65亿，无历史分位）｜正 Gamma 减弱（1465万）｜现价位于 Flip 上方 7.14%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 358（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 346（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-05  C +12.8k / P +5.4k ｜ Activity HIGH ｜ 3D
10-07  C +2.7k / P +2.1k ｜ Activity HIGH ｜ 5D
10-09  C +18.8k / P +24.7k ｜ Activity HIGH ｜ 7D
10-12  C +1.0k / P +3.0k ｜ Activity HIGH ｜ 10D

📆 10-05 Forward Structure
存量OI: C 69.7k / P 29.7k，今日变化ΔOI: C +12.8k / P +5.4k，平值价格ATM: C $3.70 / P $3.05 ｜ ATM IV 24.6%，净 delta 敞口 230k shares
Top ΔOI: C 420 +9,983 ｜ C 377 -7,933
仓位参考: Max Pain 355 ｜ Call Wall 377.5（+1.9%，弱）（OI 7.8k） ｜ Put Wall 350（-5.6%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 24.6%｜历史 Rank 50%（近端代理）｜IV/RV 1.06×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 229,995 股

📆 10-07 Forward Structure
存量OI: C 14.3k / P 7.5k，今日变化ΔOI: C +2.7k / P +2.1k，平值价格ATM: C $6.00 / P $5.19 ｜ ATM IV 32.0%，净 delta 敞口 125k shares
Top ΔOI: C 370 +514 ｜ C 357 +476 ｜ P 357 +328
仓位参考: Max Pain 355 ｜ Call Wall 370（-0.2%，弱）（OI 1.4k） ｜ Put Wall 347.5（-6.2%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 32.0%｜历史 Rank 50%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 正 124,579 股

📆 10-09 Forward Structure
存量OI: C 90.6k / P 83.7k，今日变化ΔOI: C +18.8k / P +24.7k，平值价格ATM: C $7.50 / P $6.60 ｜ ATM IV 34.7%，净 delta 敞口 702k shares
Top ΔOI: C 375 +4,231 ｜ C 362 +4,017
仓位参考: Max Pain 355 ｜ Call Wall 375（+1.2%，弱）（OI 7.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.7%｜历史 Rank 50%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 701,869 股

📆 10-12 Forward Structure
存量OI: C 6.0k / P 5.1k，今日变化ΔOI: C +1.0k / P +3.0k，平值价格ATM: C $8.29 / P $7.41 ｜ ATM IV 32.2%，净 delta 敞口 32k shares
Top ΔOI: C 360 +133
仓位参考: Max Pain 352 ｜ Call Wall 370（-0.2%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.2%｜历史 Rank 50%（近端代理）｜IV/RV 1.38×（近似）｜净 delta 敞口 正 31,973 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/TSLA_evening.json