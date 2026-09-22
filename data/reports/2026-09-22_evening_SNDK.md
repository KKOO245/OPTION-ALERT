# 期权晚报 2026-09-22（快照 16:40 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $747.46
VIX 14.21 ↓4.4%（5D -17.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 1800C ΔOI +864（距现价 -4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,758.55 → 收盘 1,887.04（+7.3%） ｜ 今日高 1909.48 ｜ 低 1758.14 ｜ 昨收 1,766.64 → 收盘 1,887.04（+6.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 1.24 | ATM IV 80.7% | Skew -6.4pp | Term 0.95 | ExpMove ±5.8%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -6.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.24×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±5.8% ｜ 10-02（10D）±10.9% ｜ 10-09（17D）±13.8% ｜ 10-16（24D）±15.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,509,147 | GEX Change vs 上次快照 493,215 | Flip: Primary Flip: 1692.20（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2098 / LOW 303 / INVALID 743
结构观察区: Primary Flip 1692.20（全链重定价，覆盖 100%）
Call Wall 2,000（弱结构｜现价低于该位 5.6%）
最近结构参考: Call Wall 2000（现价低于该位 5.6%）
量化视角： 正 Gamma（1151万，无历史分位）｜正 Gamma 增强（+49万）｜现价位于 Flip 上方 11.51%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,700（MaxPain，仅结算参考）；上方 2,000（Call Wall，弱结构）。
• Gamma 区域：切换参考 1692（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +10.2k / P +9.8k ｜ Activity HIGH ｜ 3D
10-02  C +2.2k / P +2.0k ｜ Activity HIGH ｜ 10D
10-09  C +0.7k / P +1.1k ｜ Activity HIGH ｜ 17D
10-16  C +1.9k / P +1.7k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 39.4k / P 48.9k，今日变化ΔOI: C +10.2k / P +9.8k，平值价格ATM: C $56.00 / P $53.21 ｜ ATM IV 80.7%，净 delta 敞口 286k shares
Top ΔOI: C 2000 +2,459 ｜ P 1700 +988 ｜ C 1800 +864
仓位参考: Max Pain 1,700 ｜ Call Wall 2000（+6.0%，弱）（OI 3.7k） ｜ Put Wall 1700（-9.9%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 80.7%｜历史 Rank 35%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 286,289 股

📆 10-02 Forward Structure
存量OI: C 19.7k / P 14.8k，今日变化ΔOI: C +2.2k / P +2.0k，平值价格ATM: C $107.63 / P $98.70 ｜ ATM IV 81.9%，净 delta 敞口 59k shares
Top ΔOI: C 2250 +382 ｜ C 2000 +313
仓位参考: Max Pain 1,600 ｜ Call Wall 2000（+6.0%，弱）（OI 1.0k） ｜ Put Wall 1700（-9.9%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 81.9%｜历史 Rank 35%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 59,311 股

📆 10-09 Forward Structure
存量OI: C 6.6k / P 5.8k，今日变化ΔOI: C +0.7k / P +1.1k，平值价格ATM: C $136.40 / P $123.28 ｜ ATM IV 78.2%，净 delta 敞口 26k shares
Top ΔOI: P 1430 +104 ｜ C 1770 +85
仓位参考: Max Pain 1,500 ｜ Put Wall 1700（-9.9%，弱）（OI 99）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.2%｜历史 Rank 35%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 25,667 股

📆 10-16 Forward Structure
存量OI: C 32.5k / P 41.5k，今日变化ΔOI: C +1.9k / P +1.7k，平值价格ATM: C $154.29 / P $142.30 ｜ ATM IV 77.2%，净 delta 敞口 37k shares
Top ΔOI: C 2000 +527 ｜ C 2100 +308 ｜ P 1160 -255
仓位参考: Max Pain 1,610 ｜ Call Wall 2000（+6.0%，弱）（OI 2.1k） ｜ Put Wall 1700（-9.9%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.2%｜历史 Rank 35%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 正 37,043 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/SNDK_evening.json