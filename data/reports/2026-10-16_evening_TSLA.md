# 期权晚报 2026-10-16（快照 16:40 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $709.80
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-26 347P ΔOI +819（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 420C ΔOI +664 占该期限总 OI 11.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 369.04 → 收盘 354.72（-3.9%） ｜ 今日高 370.58 ｜ 低 349.33 ｜ 昨收 362.44 → 收盘 354.72（-2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.61 | OI比 0.91 | ATM IV 27.9% | Skew -4.7pp | Term 1.72 | ExpMove ±2.5%（近端） | Rank 3%
量化视角： IV 历史低位（Rank 3%，期权偏便宜）｜期限结构正常偏陡（Term 1.72）｜Put 保护异常便宜（Skew -4.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-19（3D）±2.5% ｜ 10-23（7D）±7.4% ｜ 10-26（10D）±7.8% ｜ 10-28（12D）±8.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 4,439,401 | GEX Change vs 上次快照 -48,406,441 | Flip: Candidates 353.30 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 77%（带内） ｜ IV 有效性: VALID 1131 / LOW 94 / INVALID 633
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈353（全链重定价，覆盖 77%，CONDITIONAL）
最近结构参考: Flip 353（现价高于该位 0.4%）
量化视角： 正 Gamma（444万，无历史分位）｜正 Gamma 减弱（4841万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 370（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 353（全链重定价，覆盖 77%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +34.4k / P +10.4k ｜ Activity HIGH ｜ 3D
10-23  C +13.8k / P +11.9k ｜ Activity HIGH ｜ 7D
10-26  C +2.2k / P +2.7k ｜ Activity HIGH ｜ 10D
10-28  C +1.9k / P +0.4k ｜ Activity HIGH ｜ 12D

📆 10-19 Forward Structure
存量OI: C 73.3k / P 35.8k，今日变化ΔOI: C +34.4k / P +10.4k，平值价格ATM: C $4.20 / P $4.53 ｜ ATM IV 34.0%，净 delta 敞口 -21k shares
Top ΔOI: C 410 +5,710 ｜ C 390 +2,331
仓位参考: Max Pain 365 ｜ Call Wall 390（+9.9%，弱）（OI 4.7k） ｜ Put Wall 360（+1.5%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 34.0%｜历史 Rank 3%（近端代理）｜IV/RV 1.21×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 21,014 股

📆 10-23 Forward Structure
存量OI: C 98.2k / P 67.4k，今日变化ΔOI: C +13.8k / P +11.9k，平值价格ATM: C $13.20 / P $13.17 ｜ ATM IV 66.8%，净 delta 敞口 -108k shares
Top ΔOI: C 400 +1,142
仓位参考: Max Pain 370 ｜ Call Wall 390（+9.9%，弱）（OI 6.3k） ｜ Put Wall 350（-1.3%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 66.8%｜历史 Rank 3%（近端代理）｜IV/RV 2.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 108,213 股

📆 10-26 Forward Structure
存量OI: C 5.0k / P 6.6k，今日变化ΔOI: C +2.2k / P +2.7k，平值价格ATM: C $13.80 / P $13.70 ｜ ATM IV 59.1%，净 delta 敞口 -42k shares
Top ΔOI: P 347 +819 ｜ P 335 +467 ｜ C 400 +411
仓位参考: Max Pain 368 ｜ Call Wall 380（+7.1%，弱）（OI 0.4k） ｜ Put Wall 347.5（-2.0%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜ATM IV 59.1%｜历史 Rank 3%（近端代理）｜IV/RV 2.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 41,567 股

📆 10-28 Forward Structure
存量OI: C 3.4k / P 2.3k，今日变化ΔOI: C +1.9k / P +0.4k，平值价格ATM: C $15.00 / P $16.00 ｜ ATM IV 58.0%，净 delta 敞口 16k shares
Top ΔOI: C 420 +664 ｜ C 400 +334
仓位参考: Max Pain 365 ｜ Call Wall 357.5（+0.8%，弱）（OI 0.2k） ｜ Put Wall 375（+5.7%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 58.0%｜历史 Rank 3%（近端代理）｜IV/RV 2.07×（近似）｜净 delta 敞口 正 16,441 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/TSLA_evening.json