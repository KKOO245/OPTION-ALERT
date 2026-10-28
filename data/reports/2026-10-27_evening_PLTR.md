# 期权晚报 2026-10-27（快照 21:00 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $nan
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 198.02 → 收盘 198.73（+0.4%） ｜ 今日高 201.83 ｜ 低 196.79 ｜ 昨收 198.84 → 收盘 198.73（-0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.54 | OI比 0.97 | ATM IV 51.7% | Skew 2.8pp | Term 1.19 | ExpMove ±3.8%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构正常偏陡（Term 1.19）｜保护溢价中性（Skew 2.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（3D）±3.8% ｜ 11-06（10D）±11.7% ｜ 11-13（17D）±12.6% ｜ 11-20（24D）±13.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 54,694,852 | GEX Change vs 上次快照 10,258,144 | Flip: Primary Flip: 190.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 595 / LOW 87 / INVALID 256
结构观察区: Primary Flip 190.09（全链重定价，覆盖 100%）
Put Wall 180（弱结构｜现价高于该位 10.4%） | Call Wall 200（弱结构｜现价低于该位 0.6%）
最近结构参考: Call Wall 200（现价低于该位 0.6%）
量化视角： 正 Gamma（5469万，无历史分位）｜正 Gamma 增强（+1026万）｜现价位于 Flip 上方 4.55%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构） / 192（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 190（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 10D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 17D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 10-30 Forward Structure
存量OI: C 127.9k / P 124.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.43 / P $3.10 ｜ ATM IV 51.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 192 ｜ Call Wall 200（+0.6%，弱）（OI 15.6k） ｜ Put Wall 180（-9.4%，弱）（OI 9.5k）
量化解读： 存量两侧均衡｜ATM IV 51.7%｜历史 Rank 58%（近端代理）｜IV/RV 1.15×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 192 ｜ Call Wall 215（+8.2%，弱）（OI 3.0k） ｜ Put Wall 190（-4.4%，弱）（OI 3.3k）

11-13（Activity LOW）仓位参考: Max Pain 195 ｜ Call Wall 210（+5.7%，弱）（OI 1.4k） ｜ Put Wall 180（-9.4%，弱）（OI 1.4k）

11-20（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 200（+0.6%，弱）（OI 12.8k） ｜ Put Wall 185（-6.9%，弱）（OI 10.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/PLTR_evening.json