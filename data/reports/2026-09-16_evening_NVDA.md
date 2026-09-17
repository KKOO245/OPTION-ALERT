# 期权晚报 2026-09-16（快照 21:12 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 17.71 ↑3.0%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 214.14 → 收盘 213.90（-0.1%） ｜ 今日高 216.76 ｜ 低 212.50 ｜ 昨收 212.17 → 收盘 213.90（+0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.69 | OI比 0.84 | ATM IV 37.7% | Skew 4.0pp | Term 0.88 | ExpMove ±2.3%（近端） | Rank 27%
量化视角： IV 中性（Rank 27%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（2D）±2.3% ｜ 09-21（5D）±2.9% ｜ 09-23（7D）±3.6% ｜ 09-25（9D）±4.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 189,684,141 | GEX Change vs 上次快照 -222,910,444 | Flip: Primary Flip: 209.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 673 / LOW 201 / INVALID 528
结构观察区: Primary Flip 209.64（全链重定价，覆盖 99%）
Put Wall 200（现价高于该位 6.9%） | Call Wall 220（弱结构｜现价低于该位 2.8%）
最近结构参考: Flip 210（现价高于该位 2.0%）
量化视角： 正 Gamma（1.90亿，无历史分位）｜正 Gamma 减弱（2.23亿）｜现价位于 Flip 上方 2.03%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall） / 205（MaxPain，仅结算参考）；上方 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-18 Forward Structure
存量OI: C 1345.5k / P 1124.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.90 / P $2.95 ｜ ATM IV 37.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 205 ｜ Call Wall 230（+7.5%，弱）（OI 95.5k） ｜ Put Wall 200（-6.5%，弱）（OI 58.9k）
量化解读： 存量 Call 重｜ATM IV 37.7%｜历史 Rank 27%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-21（Activity LOW）仓位参考: Max Pain 212 ｜ Call Wall 230（+7.5%，弱）（OI 5.4k） ｜ Put Wall 200（-6.5%，弱）（OI 7.1k）

09-23（Activity LOW）仓位参考: Max Pain 215 ｜ Call Wall 230（+7.5%）（OI 8.8k） ｜ Put Wall 195（-8.8%）（OI 2.8k）

09-25（Activity LOW）仓位参考: Max Pain 218 ｜ Call Wall 220（+2.9%）（OI 35.2k） ｜ Put Wall 210（-1.8%，弱）（OI 17.4k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 37.7% vs 09-21 30.3%（差 +7.3pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/NVDA_evening.json