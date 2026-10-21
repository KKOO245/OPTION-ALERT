# 期权晚报 2026-10-21（快照 16:40 ET）

📊 市场环境

SPY $773.09 ｜ QQQ $725.20
VIX 16.68 ↓3.6%（5D -1.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-22 282C ΔOI +12,813（距现价 +2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-22 282C ΔOI +12,813 占该期限总 OI 16.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 276.86 → 收盘 276.48（-0.1%） ｜ 今日高 277.70 ｜ 低 275.30 ｜ 昨收 275.78 → 收盘 276.48（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.86 | OI比 1.00 | ATM IV 14.9% | Skew -0.1pp | Term 1.29 | ExpMove ±0.7%（近端） | Rank — (历史不足)
量化视角： 期限结构正常偏陡（Term 1.29）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-22（1D）±0.7% ｜ 10-23（2D）±1.1% ｜ 10-26（5D）±1.4% ｜ 10-27（6D）±1.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -395,006,903 | GEX Change vs 上次快照 -24,920,907 | Flip: Primary Flip: 279.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 1245 / LOW 237 / INVALID 1392
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 279.39（全链重定价，覆盖 97%）
Put Wall 260（弱结构｜现价高于该位 6.3%） | Call Wall 280（弱结构｜现价低于该位 1.3%）
最近结构参考: Flip 279（现价低于该位 1.0%）
量化视角： 负 Gamma（3.95亿，无历史分位）｜负 Gamma 加深（2492万）｜现价位于 Flip 下方 1.04%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 260（Put Wall，弱结构） / 275（MaxPain，仅结算参考）；上方 280（Call Wall，弱结构）。
• Gamma 区域：切换参考 279（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-22  C +35.9k / P +4.4k ｜ Activity HIGH ｜ 1D
10-23  C +13.3k / P +13.1k ｜ Activity HIGH ｜ 2D
10-26  C +7.7k / P +5.0k ｜ Activity HIGH ｜ 5D
10-27  C +4.3k / P +2.5k ｜ Activity HIGH ｜ 6D

📆 10-22 Forward Structure
存量OI: C 48.3k / P 27.8k，今日变化ΔOI: C +35.9k / P +4.4k，平值价格ATM: C $1.17 / P $0.85 ｜ ATM IV 17.2%，净 delta 敞口 142k shares
Top ΔOI: C 282 +12,813 ｜ C 283 +9,347 ｜ C 280 +9,345
仓位参考: Max Pain 274 ｜ Call Wall 282（+2.0%，弱）（OI 13.2k） ｜ Put Wall 267（-3.4%）（OI 4.8k）
量化解读： 存量 Call 重｜ATM IV 17.2%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 142,183 股

📆 10-23 Forward Structure
存量OI: C 156.2k / P 189.8k，今日变化ΔOI: C +13.3k / P +13.1k，平值价格ATM: C $1.73 / P $1.29 ｜ ATM IV 18.0%，净 delta 敞口 -112k shares
Top ΔOI: P 273 +8,064 ｜ C 278 +5,102 ｜ C 280 +4,592
仓位参考: Max Pain 276 ｜ Call Wall 280（+1.3%，弱）（OI 14.2k） ｜ Put Wall 267（-3.4%，弱）（OI 17.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 18.0%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 112,416 股

📆 10-26 Forward Structure
存量OI: C 24.2k / P 20.5k，今日变化ΔOI: C +7.7k / P +5.0k，平值价格ATM: C $2.21 / P $1.70 ｜ ATM IV 14.8%，净 delta 敞口 115k shares
Top ΔOI: C 280 +2,570 ｜ C 283 +1,681 ｜ C 278 +1,414
仓位参考: Max Pain 274 ｜ Call Wall 283（+2.4%，弱）（OI 5.1k） ｜ Put Wall 267（-3.4%）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 14.8%｜净 delta 敞口 正 115,275 股

📆 10-27 Forward Structure
存量OI: C 16.5k / P 13.7k，今日变化ΔOI: C +4.3k / P +2.5k，平值价格ATM: C $2.50 / P $1.93 ｜ ATM IV 15.5%，净 delta 敞口 64k shares
Top ΔOI: C 282 +1,835 ｜ C 279 +744 ｜ C 285 +584
仓位参考: Max Pain 272 ｜ Call Wall 284（+2.7%）（OI 4.3k） ｜ Put Wall 262（-5.2%）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 15.5%｜净 delta 敞口 正 63,529 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/IWM_evening.json