# 期权晚报 2026-10-28（快照 16:40 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 16.91 ↓3.5%（5D +1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 43C ΔOI +522（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 40.92 → 收盘 41.06（+0.3%） ｜ 今日高 41.36 ｜ 低 39.69 ｜ 昨收 40.87 → 收盘 41.06（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.46 | OI比 0.62 | ATM IV 80.7% | Skew 18.7pp | Term 0.83 | ExpMove ±4.9%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价显著（Skew 18.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±4.9% ｜ 11-06（9D）±10.5% ｜ 11-13（16D）±11.7% ｜ 11-20（23D）±13.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,215,122 | GEX Change vs 上次快照 964,677 | Flip: Primary Flip: 38.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 324 / LOW 68 / INVALID 134
结构观察区: Primary Flip 38.89（全链重定价，覆盖 95%）
最近结构参考: Flip 39（现价高于该位 5.6%）
量化视角： 正 Gamma（322万，无历史分位）｜正 Gamma 增强（+96万）｜现价位于 Flip 上方 5.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 41（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 39（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +1.0k / P +0.5k ｜ Activity HIGH ｜ 2D
11-06  C +1.2k / P +41 ｜ Activity MEDIUM △ ｜ 9D
11-13  C +0.2k / P +6 ｜ Activity MEDIUM △ ｜ 16D
11-20  C +0.9k / P +0.8k ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 13.1k / P 8.1k，今日变化ΔOI: C +1.0k / P +0.5k，平值价格ATM: C $0.85 / P $1.16 ｜ ATM IV 80.7%，净 delta 敞口 37k shares
Top ΔOI: C 43 +522 ｜ C 41 +359 ｜ C 41 +218
仓位参考: Max Pain 41 ｜ Call Wall 40（-2.6%，弱）（OI 1.1k） ｜ Put Wall 44（+7.2%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 80.7%｜历史 Rank 73%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,773 股

11-06（MEDIUM △）Top ΔOI: 45C +622 ｜ 42C +141
11-06（MEDIUM △）仓位参考: Max Pain 42 ｜ Call Wall 45（+9.6%，弱）（OI 1.6k） ｜ Put Wall 38（-7.5%）（OI 0.9k）

11-13（MEDIUM △）Top ΔOI: 43C +57 ｜ 42C +34
11-13（MEDIUM △）仓位参考: Max Pain 42 ｜ Put Wall 39（-5.0%）（OI 0.8k）

11-20（MEDIUM △）Top ΔOI: 36P +648 ｜ 45C +434
11-20（MEDIUM △）仓位参考: Max Pain 45 ｜ Call Wall 45（+9.6%，弱）（OI 1.9k） ｜ Put Wall 45（+9.6%，弱）（OI 1.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/MP_evening.json