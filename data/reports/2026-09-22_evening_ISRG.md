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
🟡 **近现价集中开仓**: 09-25 420C ΔOI +153（距现价 +4.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 403.00 → 收盘 402.09（-0.2%） ｜ 今日高 403.97 ｜ 低 397.72 ｜ 昨收 401.65 → 收盘 402.09（+0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.75 | OI比 0.60 | ATM IV 41.5% | Skew -0.0pp | Term 1.05 | ExpMove ±1.6%（近端） | Rank 53%
量化视角： IV 中性（Rank 53%）｜期限结构正常（Term 1.05）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±1.6% ｜ 10-02（10D）±4.5% ｜ 10-09（17D）±3.4% ｜ 10-16（24D）±6.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,352,160 | GEX Change vs 上次快照 377,258 | Flip: Primary Flip: 384.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 309 / LOW 149 / INVALID 432
结构观察区: Primary Flip 384.53（全链重定价，覆盖 95%）
Call Wall 400（现价高于该位 0.5%）
最近结构参考: Call Wall 400（现价高于该位 0.5%）
量化视角： 正 Gamma（235万，无历史分位）｜正 Gamma 增强（+38万）｜现价位于 Flip 上方 4.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 380（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 385（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 3D
10-02  C +77 / P +0.1k ｜ Activity HIGH ｜ 10D
10-09  C +72 / P +9 ｜ Activity HIGH ｜ 17D
10-16  C +0.9k / P -8 ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 2.4k / P 1.4k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $6.55 / P $0.00 ｜ ATM IV 41.5%，净 delta 敞口 4k shares
Top ΔOI: P 380 +263 ｜ C 420 +153 ｜ C 415 +149
仓位参考: Max Pain 380 ｜ Call Wall 430（+6.9%，弱）（OI 0.3k） ｜ Put Wall 380（-5.5%）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 41.5%｜历史 Rank 53%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,929 股

📆 10-02 Forward Structure
存量OI: C 1.1k / P 3.0k，今日变化ΔOI: C +77 / P +0.1k，平值价格ATM: C $8.60 / P $9.37 ｜ ATM IV 32.7%，净 delta 敞口 280 shares
Top ΔOI: C 410 +28 ｜ P 395 +27
仓位参考: Max Pain 370 ｜ Call Wall 410（+2.0%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 32.7%｜历史 Rank 53%（近端代理）｜期限正常（远月高于近端）｜净 delta 敞口 正 280 股

📆 10-09 Forward Structure
存量OI: C 0.5k / P 0.4k，今日变化ΔOI: C +72 / P +9，平值价格ATM: C $0.00 / P $13.49 ｜ ATM IV 33.8%，净 delta 敞口 1k shares
Top ΔOI: C 430 +43 ｜ C 410 +19 ｜ C 390 -12
仓位参考: Max Pain 380 ｜ Call Wall 380（-5.5%）（OI 0.1k） ｜ Put Wall 385（-4.3%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 33.8%｜历史 Rank 53%（近端代理）｜净 delta 敞口 正 1,234 股

📆 10-16 Forward Structure
存量OI: C 10.1k / P 8.9k，今日变化ΔOI: C +0.9k / P -8，平值价格ATM: C $11.75 / P $14.20 ｜ ATM IV 34.8%，净 delta 敞口 37k shares
Top ΔOI: C 400 +521 ｜ C 405 +65
仓位参考: Max Pain 385 ｜ Call Wall 400（-0.5%）（OI 1.0k） ｜ Put Wall 380（-5.5%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 34.8%｜历史 Rank 53%（近端代理）｜净 delta 敞口 正 37,374 股

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 41.5% vs 10-02 32.7%（差 +8.7pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/ISRG_evening.json