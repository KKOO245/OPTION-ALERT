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
🟡 **近现价集中开仓**: 12-04 88C ΔOI +348（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 80.50 → 收盘 84.99（+5.6%） ｜ 今日高 87.26 ｜ 低 75.60 ｜ 昨收 87.31 → 收盘 84.99（-2.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.72 | OI比 0.33 | ATM IV 122.6% | Skew 7.2pp | Term 1.06 | ExpMove ±7.0%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构正常（Term 1.06）｜保护溢价显著（Skew 7.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±7.0% ｜ 12-04（9D）±17.4% ｜ 12-11（16D）±23.3% ｜ 12-18（23D）±26.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,522,503 | GEX Change vs 上次快照 1,924,456 | Flip: Primary Flip: 88.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 590 / LOW 130 / INVALID 240
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 88.29（全链重定价，覆盖 100%）
Put Wall 80（弱结构｜现价高于该位 6.2%）
最近结构参考: Flip 88（现价低于该位 3.7%）
量化视角： 负 Gamma（352万，无历史分位）｜负 Gamma 缓解（+192万）｜现价位于 Flip 下方 3.74%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 95（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 88（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +9.3k / P -3.9k ｜ Activity HIGH ｜ 2D
12-04  C +2.9k / P +1.5k ｜ Activity HIGH ｜ 9D
12-11  C +0.8k / P +0.6k ｜ Activity HIGH ｜ 16D
12-18  C +1.2k / P +1.8k ｜ Activity MEDIUM △ ｜ 23D

📆 11-27 Forward Structure
存量OI: C 102.1k / P 33.6k，今日变化ΔOI: C +9.3k / P -3.9k，平值价格ATM: C $3.00 / P $2.91 ｜ ATM IV 122.6%，净 delta 敞口 573k shares
Top ΔOI: C 90 +1,403 ｜ P 80 -1,344
仓位参考: Max Pain 95 ｜ Call Wall 90（+5.9%，弱）（OI 1.9k） ｜ Put Wall 80（-5.9%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜ATM IV 122.6%｜历史 Rank 72%（近端代理）｜IV/RV 0.75×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 572,626 股

📆 12-04 Forward Structure
存量OI: C 30.1k / P 16.7k，今日变化ΔOI: C +2.9k / P +1.5k，平值价格ATM: C $7.50 / P $7.25 ｜ ATM IV 139.3%，净 delta 敞口 86k shares
Top ΔOI: C 90 +592 ｜ C 100 +497 ｜ C 88 +348
仓位参考: Max Pain 100 ｜ Call Wall 90（+5.9%，弱）（OI 0.8k） ｜ Put Wall 90（+5.9%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 139.3%｜历史 Rank 72%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 85,568 股

📆 12-11 Forward Structure
存量OI: C 11.3k / P 13.6k，今日变化ΔOI: C +0.8k / P +0.6k，平值价格ATM: C $10.20 / P $9.64 ｜ ATM IV 136.1%，净 delta 敞口 18k shares
Top ΔOI: P 80 +261
仓位参考: Max Pain 110 ｜ Call Wall 90（+5.9%，弱）（OI 0.3k） ｜ Put Wall 85（+0.0%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 136.1%｜历史 Rank 72%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 17,593 股

12-18（MEDIUM △）Top ΔOI: 55P +1,304 ｜ 200P -1,167
12-18（MEDIUM △）仓位参考: Max Pain 140 ｜ Put Wall 80（-5.9%，弱）（OI 8.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/NBIS_evening.json