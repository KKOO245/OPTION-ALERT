# 期权晚报 2026-10-22（快照 16:40 ET）

📊 市场环境

SPY $763.96 ｜ QQQ $704.47
VIX 19.03 ↑14.1%（5D +15.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-26 365P ΔOI +1,548（距现价 -2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 455C ΔOI +9,699 占该期限总 OI 12.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 374.03 → 收盘 374.58（+0.1%） ｜ 今日高 388.86 ｜ 低 373.71 ｜ 昨收 386.47 → 收盘 374.58（-3.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.89 | OI比 0.99 | ATM IV 54.2% | Skew 0.5pp | Term 0.74 | ExpMove ±2.3%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价薄（Skew 0.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（1D）±2.3% ｜ 10-26（4D）±3.3% ｜ 10-28（6D）±4.4% ｜ 10-30（8D）±5.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 61,510,561 | GEX Change vs 上次快照 -65,010,448 | Flip: Primary Flip: 365.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1359 / LOW 170 / INVALID 571
结构观察区: Primary Flip 365.12（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 6.4%）
最近结构参考: Flip 365（现价高于该位 2.6%）
量化视角： 正 Gamma（6151万，无历史分位）｜正 Gamma 减弱（6501万）｜现价位于 Flip 上方 2.59%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 365（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +36.3k / P +44.3k ｜ Activity HIGH ｜ 1D
10-26  C +15.6k / P +11.0k ｜ Activity HIGH ｜ 4D
10-28  C +1.7k / P +2.6k ｜ Activity HIGH ｜ 6D
10-30  C +4.1k / P +20.6k ｜ Activity HIGH ｜ 8D

📆 10-23 Forward Structure
存量OI: C 273.3k / P 270.0k，今日变化ΔOI: C +36.3k / P +44.3k，平值价格ATM: C $4.21 / P $4.35 ｜ ATM IV 54.2%，净 delta 敞口 -1.1M shares
Top ΔOI: C 400 +3,507
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.8%，弱）（OI 19.6k） ｜ Put Wall 350（-6.6%，弱）（OI 8.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 54.2%｜历史 Rank 57%（近端代理）｜IV/RV 1.78×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,097,234 股

📆 10-26 Forward Structure
存量OI: C 50.0k / P 29.6k，今日变化ΔOI: C +15.6k / P +11.0k，平值价格ATM: C $6.23 / P $6.17 ｜ ATM IV 39.8%，净 delta 敞口 -260k shares
Top ΔOI: P 365 +1,548
仓位参考: Max Pain 375 ｜ Put Wall 350（-6.6%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 39.8%｜历史 Rank 57%（近端代理）｜IV/RV 1.30×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 260,365 股

📆 10-28 Forward Structure
存量OI: C 9.4k / P 10.7k，今日变化ΔOI: C +1.7k / P +2.6k，平值价格ATM: C $8.28 / P $8.30 ｜ ATM IV 43.0%，净 delta 敞口 -60k shares
Top ΔOI: P 355 +482 ｜ C 410 +331 ｜ P 380 +231
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.8%，弱）（OI 0.9k） ｜ Put Wall 350（-6.6%）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 43.0%｜历史 Rank 57%（近端代理）｜IV/RV 1.41×（近似）｜净 delta 敞口 负 59,729 股

📆 10-30 Forward Structure
存量OI: C 82.7k / P 95.7k，今日变化ΔOI: C +4.1k / P +20.6k，平值价格ATM: C $9.65 / P $9.50 ｜ ATM IV 43.3%，净 delta 敞口 -154k shares
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.8%）（OI 9.2k） ｜ Put Wall 380（+1.4%，弱）（OI 4.0k）
量化解读： 存量两侧均衡｜ATM IV 43.3%｜历史 Rank 57%（近端代理）｜IV/RV 1.42×（近似）｜净 delta 敞口 负 154,111 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/TSLA_evening.json