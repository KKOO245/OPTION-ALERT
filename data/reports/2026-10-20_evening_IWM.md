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

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 277C ΔOI +9,556（距现价 +0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-21 277C ΔOI +9,556 占该期限总 OI 14.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 271.53 → 收盘 275.78（+1.6%） ｜ 今日高 276.90 ｜ 低 271.29 ｜ 昨收 271.28 → 收盘 275.78（+1.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.99 | OI比 1.34 | ATM IV 11.3% | Skew -1.2pp | Term 1.68 | ExpMove ±0.8%（近端） | Rank — (历史不足)
量化视角： 期限结构正常偏陡（Term 1.68）｜Put 保护异常便宜（Skew -1.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.34×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-21（1D）±0.8% ｜ 10-22（2D）±1.1% ｜ 10-23（3D）±1.4% ｜ 10-26（6D）±1.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -387,154,999 | GEX Change vs 上次快照 185,124,067 | Flip: Primary Flip: 281.61（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1235 / LOW 229 / INVALID 1422
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 281.61（全链重定价，覆盖 98%）
Put Wall 270（弱结构｜现价高于该位 2.1%） | Call Wall 290（弱结构｜现价低于该位 4.9%）
最近结构参考: Flip 282（现价低于该位 2.1%）
量化视角： 负 Gamma（3.87亿，无历史分位）｜负 Gamma 缓解（+1.85亿）｜现价位于 Flip 下方 2.07%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 270（Put Wall，弱结构） / 272（MaxPain，仅结算参考）；上方 290（Call Wall，弱结构）。
• Gamma 区域：切换参考 282（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-21  C +18.0k / P +10.3k ｜ Activity HIGH ｜ 1D
10-22  C +1.0k / P +6.1k ｜ Activity HIGH ｜ 2D
10-23  C +12.0k / P +28.4k ｜ Activity HIGH ｜ 3D
10-26  C +0.9k / P +3.4k ｜ Activity HIGH ｜ 6D

📆 10-21 Forward Structure
存量OI: C 40.4k / P 28.0k，今日变化ΔOI: C +18.0k / P +10.3k，平值价格ATM: C $1.05 / P $1.01 ｜ ATM IV 17.8%，净 delta 敞口 840k shares
Top ΔOI: C 277 +9,556 ｜ C 275 +6,933 ｜ P 260 +4,758
仓位参考: Max Pain 273 ｜ Call Wall 277（+0.4%，弱）（OI 12.2k） ｜ Put Wall 260（-5.7%）（OI 6.9k）
量化解读： 存量 Call 重｜ATM IV 17.8%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 839,667 股

📆 10-22 Forward Structure
存量OI: C 12.3k / P 23.4k，今日变化ΔOI: C +1.0k / P +6.1k，平值价格ATM: C $1.56 / P $1.47 ｜ ATM IV 18.4%，净 delta 敞口 29k shares
Top ΔOI: P 267 +4,305
仓位参考: Max Pain 274 ｜ Call Wall 275（-0.3%）（OI 2.8k） ｜ Put Wall 267（-3.2%）（OI 4.8k）
量化解读： 存量 Put 重｜ATM IV 18.4%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 29,410 股

📆 10-23 Forward Structure
存量OI: C 142.9k / P 176.7k，今日变化ΔOI: C +12.0k / P +28.4k，平值价格ATM: C $1.98 / P $1.85 ｜ ATM IV 19.1%，净 delta 敞口 596k shares
Top ΔOI: P 267 +7,480 ｜ C 276 +4,254
仓位参考: Max Pain 276 ｜ Call Wall 281（+1.9%，弱）（OI 11.6k） ｜ Put Wall 267（-3.2%，弱）（OI 17.8k）
量化解读： 存量 Put 重｜ATM IV 19.1%｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 596,441 股

📆 10-26 Forward Structure
存量OI: C 16.5k / P 15.5k，今日变化ΔOI: C +0.9k / P +3.4k，平值价格ATM: C $2.37 / P $2.33 ｜ ATM IV 16.1%，净 delta 敞口 89k shares
Top ΔOI: C 278 -2,047 ｜ P 262 +761 ｜ C 273 +721
仓位参考: Max Pain 273 ｜ Call Wall 283（+2.6%）（OI 3.4k） ｜ Put Wall 267（-3.2%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 16.1%｜净 delta 敞口 正 88,676 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/IWM_evening.json