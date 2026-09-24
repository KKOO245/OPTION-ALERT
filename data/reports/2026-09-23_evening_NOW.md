# 期权晚报 2026-09-23（快照 21:00 ET）

📊 市场环境

SPY $767.81 ｜ QQQ $nan
VIX 15.18 ↑2.1%（5D -11.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布　✅ 今日已公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 137.22 → 收盘 140.78（+2.6%） ｜ 今日高 141.54 ｜ 低 136.15 ｜ 昨收 137.00 → 收盘 140.78（+2.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.29 | OI比 0.63 | ATM IV 59.8% | Skew -2.8pp | Term 0.94 | ExpMove ±5.0%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（2D）±5.0% ｜ 10-02（9D）±8.1% ｜ 10-09（16D）±9.8% ｜ 10-16（23D）±10.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 18,899,791 | GEX Change vs 上次快照 9,220,087 | Flip: Primary Flip: 133.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 614 / LOW 36 / INVALID 76
结构观察区: Primary Flip 133.13（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 6.1%）
最近结构参考: Flip 133（现价高于该位 5.7%）
量化视角： 正 Gamma（1890万，无历史分位）｜正 Gamma 增强（+922万）｜现价位于 Flip 上方 5.74%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 136（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 133（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-25 Forward Structure
存量OI: C 30.0k / P 18.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.63 / P $5.40 ｜ ATM IV 59.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 136 ｜ Call Wall 150（+6.5%，弱）（OI 6.1k） ｜ Put Wall 130（-7.7%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 59.8%｜历史 Rank 40%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 132 ｜ Call Wall 150（+6.5%）（OI 2.3k） ｜ Put Wall 130（-7.7%）（OI 1.1k）

10-09（Activity LOW）仓位参考: Max Pain 136 ｜ Call Wall 150（+6.5%）（OI 1.0k） ｜ Put Wall 140（-0.6%，弱）（OI 0.5k）

10-16（Activity LOW）仓位参考: Max Pain 125 ｜ Call Wall 150（+6.5%）（OI 11.2k） ｜ Put Wall 130（-7.7%，弱）（OI 4.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/NOW_evening.json