# 期权晚报 2026-11-03（快照 16:41 ET）

📊 市场环境

SPY $754.35 ｜ QQQ $685.28
VIX 20.83 ↓1.5%（5D +18.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-04 274P ΔOI +16,541（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-04 274P ΔOI +16,541 占该期限总 OI 19.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 279.84 → 收盘 279.79（-0.0%） ｜ 今日高 281.99 ｜ 低 279.34 ｜ 昨收 279.14 → 收盘 279.79（+0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.01 | OI比 0.81 | ATM IV 18.2% | Skew 4.1pp | Term 1.15 | ExpMove ±1.5%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常（Term 1.15）｜保护溢价中性（Skew 4.1pp）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-04（1D）±1.5% ｜ 11-05（2D）±1.9% ｜ 11-06（3D）±2.2% ｜ 11-09（6D）±2.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -497,655,670 | GEX Change vs 上次快照 -33,544,720 | Flip: Primary Flip: 286.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1287 / LOW 131 / INVALID 944
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 286.27（全链重定价，覆盖 98%）
Put Wall 270（弱结构｜现价高于该位 3.6%） | Call Wall 285（弱结构｜现价低于该位 1.8%）
最近结构参考: Call Wall 285（现价低于该位 1.8%）
量化视角： 负 Gamma（4.98亿，无历史分位）｜负 Gamma 加深（3354万）｜现价位于 Flip 下方 2.26%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构）；上方 280（MaxPain，仅结算参考） / 285（Call Wall，弱结构）。
• Gamma 区域：切换参考 286（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-04  C +19.1k / P +18.4k ｜ Activity HIGH ｜ 1D
11-05  C +3.5k / P +1.2k ｜ Activity HIGH ｜ 2D
11-06  C +13.5k / P +20.1k ｜ Activity HIGH ｜ 3D
11-09  C +8.4k / P +7.9k ｜ Activity HIGH ｜ 6D

📆 11-04 Forward Structure
存量OI: C 40.5k / P 45.8k，今日变化ΔOI: C +19.1k / P +18.4k，平值价格ATM: C $1.89 / P $2.36 ｜ ATM IV 36.4%，净 delta 敞口 -152k shares
Top ΔOI: P 274 +16,541 ｜ C 287 +9,161 ｜ C 288 +4,145
仓位参考: Max Pain 280 ｜ Call Wall 288（+2.9%，弱）（OI 10.3k） ｜ Put Wall 274（-2.1%）（OI 17.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 36.4%｜历史 Rank 28%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 152,078 股

📆 11-05 Forward Structure
存量OI: C 10.8k / P 18.7k，今日变化ΔOI: C +3.5k / P +1.2k，平值价格ATM: C $2.53 / P $2.77 ｜ ATM IV 31.1%，净 delta 敞口 16k shares
Top ΔOI: C 286 +2,850 ｜ P 268 +240 ｜ P 280 +193
仓位参考: Max Pain 280 ｜ Call Wall 286（+2.2%）（OI 3.0k） ｜ Put Wall 260（-7.1%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 31.1%｜历史 Rank 28%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 15,639 股

📆 11-06 Forward Structure
存量OI: C 118.5k / P 274.6k，今日变化ΔOI: C +13.5k / P +20.1k，平值价格ATM: C $2.93 / P $3.26 ｜ ATM IV 30.6%，净 delta 敞口 -1.2M shares
Top ΔOI: P 277 +29,350 ｜ P 267 -20,907 ｜ C 289 +4,964
仓位参考: Max Pain 280 ｜ Call Wall 285（+1.9%，弱）（OI 13.0k） ｜ Put Wall 277（-1.0%，弱）（OI 33.0k）
量化解读： 存量 Put 重｜ATM IV 30.6%｜历史 Rank 28%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,166,529 股

📆 11-09 Forward Structure
存量OI: C 13.0k / P 17.3k，今日变化ΔOI: C +8.4k / P +7.9k，平值价格ATM: C $3.39 / P $3.58 ｜ ATM IV 24.2%，净 delta 敞口 -6k shares
Top ΔOI: C 285 +7,175 ｜ P 275 +2,567 ｜ P 268 +939
仓位参考: Max Pain 280 ｜ Call Wall 285（+1.9%）（OI 7.2k） ｜ Put Wall 275（-1.7%）（OI 3.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 24.2%｜历史 Rank 28%（近端代理）｜净 delta 敞口 负 5,734 股

📅 事件差分（观察，非因果）: 11-04（1D）ATM IV 36.4% vs 11-05 31.1%（差 +5.3pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/IWM_evening.json