# 期权晚报 2026-11-25（快照 16:40 ET）

📊 市场环境

SPY $716.70 ｜ QQQ $633.93
VIX 28.29 ↑7.3%（5D +15.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 275P ΔOI -14,600（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 260P ΔOI +2,291 占该期限总 OI 15.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 263.23 → 收盘 268.87（+2.1%） ｜ 今日高 269.77 ｜ 低 260.84 ｜ 昨收 267.14 → 收盘 268.87（+0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.25 | OI比 1.42 | ATM IV 33.2% | Skew 4.0pp | Term 0.72 | ExpMove ±1.2%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜当日成交偏 Put（P/C量 1.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.25×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.42×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±1.2% ｜ 11-30（5D）±1.9% ｜ 12-01（6D）±2.3% ｜ 12-02（7D）±2.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -742,879,415 | GEX Change vs 上次快照 222,092,220 | Flip: Primary Flip: 284.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 1222 / LOW 253 / INVALID 1227
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 284.05（全链重定价，覆盖 96%）
Put Wall 250（弱结构｜现价高于该位 7.5%）
最近结构参考: Flip 284（现价低于该位 5.3%）
量化视角： 负 Gamma（7.43亿，无历史分位）｜负 Gamma 缓解（+2.22亿）｜现价位于 Flip 下方 5.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 250（Put Wall，弱结构） / 267（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 284（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +12.0k / P -15.4k ｜ Activity HIGH ｜ 2D
11-30  C +3.7k / P +14.2k ｜ Activity HIGH ｜ 5D
12-01  C +0.8k / P +1.0k ｜ Activity HIGH ｜ 6D
12-02  C +1.7k / P +3.8k ｜ Activity HIGH ｜ 7D

📆 11-27 Forward Structure
存量OI: C 124.0k / P 224.9k，今日变化ΔOI: C +12.0k / P -15.4k，平值价格ATM: C $1.52 / P $1.72 ｜ ATM IV 20.8%，净 delta 敞口 2.1M shares
Top ΔOI: P 275 -14,600 ｜ P 276 -4,614 ｜ C 276 +3,671
仓位参考: Max Pain 270 ｜ Call Wall 270（+0.4%，弱）（OI 9.8k） ｜ Put Wall 270（+0.4%，弱）（OI 35.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 20.8%｜历史 Rank 70%（近端代理）｜IV/RV 0.69×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,074,970 股

📆 11-30 Forward Structure
存量OI: C 25.3k / P 75.5k，今日变化ΔOI: C +3.7k / P +14.2k，平值价格ATM: C $2.45 / P $2.59 ｜ ATM IV 20.2%，净 delta 敞口 -70k shares
Top ΔOI: P 252 +7,796 ｜ P 261 +3,635 ｜ P 264 +3,467
仓位参考: Max Pain 269 ｜ Call Wall 276（+2.7%，弱）（OI 3.9k） ｜ Put Wall 260（-3.3%，弱）（OI 8.9k）
量化解读： 存量 Put 重｜ATM IV 20.2%｜历史 Rank 70%（近端代理）｜IV/RV 0.67×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 69,933 股

📆 12-01 Forward Structure
存量OI: C 14.5k / P 15.5k，今日变化ΔOI: C +0.8k / P +1.0k，平值价格ATM: C $3.19 / P $3.07 ｜ ATM IV 21.7%，净 delta 敞口 9k shares
Top ΔOI: C 270 +298 ｜ P 247 +232 ｜ P 250 +188
仓位参考: Max Pain 265 ｜ Call Wall 270（+0.4%，弱）（OI 3.4k） ｜ Put Wall 260（-3.3%）（OI 6.0k）
量化解读： 存量两侧均衡｜ATM IV 21.7%｜历史 Rank 70%（近端代理）｜IV/RV 0.72×（近似）｜净 delta 敞口 正 8,523 股

📆 12-02 Forward Structure
存量OI: C 4.1k / P 10.7k，今日变化ΔOI: C +1.7k / P +3.8k，平值价格ATM: C $3.47 / P $3.18 ｜ ATM IV 22.7%，净 delta 敞口 -38k shares
Top ΔOI: P 260 +2,291 ｜ C 273 +431 ｜ C 271 +293
仓位参考: Max Pain 265 ｜ Call Wall 273（+1.5%，弱）（OI 0.6k） ｜ Put Wall 260（-3.3%）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 22.7%｜历史 Rank 70%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 负 37,959 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/IWM_evening.json