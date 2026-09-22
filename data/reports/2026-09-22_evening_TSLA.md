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
🟡 **近现价集中开仓**: 09-23 390C ΔOI +3,131（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 379.07 → 收盘 378.90（-0.0%） ｜ 今日高 380.42 ｜ 低 372.88 ｜ 昨收 375.30 → 收盘 378.90（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.67 | OI比 0.74 | ATM IV 42.4% | Skew -2.5pp | Term 1.06 | ExpMove ±1.8%（近端） | Rank 14%
量化视角： IV 历史低位（Rank 14%，期权偏便宜）｜期限结构正常（Term 1.06）｜Put 保护异常便宜（Skew -2.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-23（1D）±1.8% ｜ 09-25（3D）±3.1% ｜ 09-28（6D）±3.6% ｜ 09-30（8D）±4.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 138,179,162 | GEX Change vs 上次快照 22,223,959 | Flip: Primary Flip: 357.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1250 / LOW 108 / INVALID 478
结构观察区: Primary Flip 357.88（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 5.3%）
最近结构参考: Call Wall 400（现价低于该位 5.3%）
量化视角： 正 Gamma（1.38亿，无历史分位）｜正 Gamma 增强（+2222万）｜现价位于 Flip 上方 5.87%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 358（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-23  C +28.5k / P +18.7k ｜ Activity HIGH ｜ 1D
09-25  C +33.7k / P +23.6k ｜ Activity HIGH ｜ 3D
09-28  C +5.8k / P +3.2k ｜ Activity HIGH ｜ 6D
09-30  C +2.0k / P +1.8k ｜ Activity HIGH ｜ 8D

📆 09-23 Forward Structure
存量OI: C 54.6k / P 40.5k，今日变化ΔOI: C +28.5k / P +18.7k，平值价格ATM: C $2.84 / P $4.00 ｜ ATM IV 42.4%，净 delta 敞口 217k shares
Top ΔOI: C 400 +4,172 ｜ C 410 +3,589 ｜ C 390 +3,131
仓位参考: Max Pain 370 ｜ Call Wall 400（+5.6%，弱）（OI 5.9k） ｜ Put Wall 370（-2.3%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 42.4%｜历史 Rank 14%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 217,410 股

📆 09-25 Forward Structure
存量OI: C 188.9k / P 222.0k，今日变化ΔOI: C +33.7k / P +23.6k，平值价格ATM: C $5.40 / P $6.34 ｜ ATM IV 42.4%，净 delta 敞口 -42k shares
Top ΔOI: C 400 +6,779 ｜ C 395 +4,203
仓位参考: Max Pain 362 ｜ Call Wall 367.5（-3.0%，弱）（OI 16.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.4%｜历史 Rank 14%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 41,530 股

📆 09-28 Forward Structure
存量OI: C 15.4k / P 7.7k，今日变化ΔOI: C +5.8k / P +3.2k，平值价格ATM: C $6.51 / P $7.30 ｜ ATM IV 35.5%，净 delta 敞口 38k shares
Top ΔOI: C 415 +1,067 ｜ C 410 +1,061 ｜ P 375 +776
仓位参考: Max Pain 368 ｜ Call Wall 410（+8.2%，弱）（OI 1.4k） ｜ Put Wall 375（-1.0%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 35.5%｜历史 Rank 14%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 37,608 股

📆 09-30 Forward Structure
存量OI: C 8.5k / P 5.2k，今日变化ΔOI: C +2.0k / P +1.8k，平值价格ATM: C $8.18 / P $8.85 ｜ ATM IV 37.8%，净 delta 敞口 -10k shares
Top ΔOI: P 370 +508 ｜ C 395 +322 ｜ C 390 +282
仓位参考: Max Pain 368 ｜ Call Wall 400（+5.6%，弱）（OI 0.8k） ｜ Put Wall 370（-2.3%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 37.8%｜历史 Rank 14%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 负 10,027 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/TSLA_evening.json