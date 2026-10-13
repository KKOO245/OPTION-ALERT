# 期权晚报 2026-10-13（快照 16:40 ET）

📊 市场环境

SPY $778.01 ｜ QQQ $743.57
VIX 15.27 ↑0.4%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **事件差分**: 10-16 ATM IV 74.9% vs 10-23 64.2%（差 +10.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-23 1500C ΔOI +1,018（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,405.75 → 收盘 1,482.33（+5.4%） ｜ 今日高 1484.00 ｜ 低 1403.16 ｜ 昨收 1,487.33 → 收盘 1,482.33（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.56 | OI比 0.99 | ATM IV 74.9% | Skew 0.6pp | Term 0.91 | ExpMove ±5.4%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 0.91）｜保护溢价薄（Skew 0.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.99×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±5.4% ｜ 10-23（10D）±8.5% ｜ 10-30（17D）±12.6% ｜ 11-06（24D）±15.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,746,290 | GEX Change vs 上次快照 3,810,699 | Flip: Primary Flip: 1559.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1920 / LOW 434 / INVALID 854
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1559.75（全链重定价，覆盖 100%）
最近结构参考: Flip 1560（现价低于该位 5.0%）
量化视角： 负 Gamma（675万，无历史分位）｜负 Gamma 缓解（+381万）｜现价位于 Flip 下方 4.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,600（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1560（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +13.2k / P +3.4k ｜ Activity HIGH ｜ 3D
10-23  C +4.4k / P +1.6k ｜ Activity HIGH ｜ 10D
10-30  C +2.5k / P +0.6k ｜ Activity HIGH ｜ 17D
11-06  C +0.8k / P +0.6k ｜ Activity HIGH ｜ 24D

📆 10-16 Forward Structure
存量OI: C 69.6k / P 69.2k，今日变化ΔOI: C +13.2k / P +3.4k，平值价格ATM: C $41.18 / P $38.80 ｜ ATM IV 74.9%，净 delta 敞口 379k shares
Top ΔOI: C 1700 +1,780 ｜ C 1600 +1,154 ｜ P 1400 +981
仓位参考: Max Pain 1,600 ｜ Call Wall 1600（+7.9%，弱）（OI 2.5k） ｜ Put Wall 1400（-5.6%，弱）（OI 3.4k）
量化解读： 存量两侧均衡｜ATM IV 74.9%｜历史 Rank 32%（近端代理）｜IV/RV 1.57×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 378,560 股

📆 10-23 Forward Structure
存量OI: C 18.7k / P 16.0k，今日变化ΔOI: C +4.4k / P +1.6k，平值价格ATM: C $64.60 / P $61.40 ｜ ATM IV 64.2%，净 delta 敞口 118k shares
Top ΔOI: C 1500 +1,018 ｜ C 1550 +241
仓位参考: Max Pain 1,600 ｜ Call Wall 1500（+1.2%，弱）（OI 1.1k） ｜ Put Wall 1500（+1.2%）（OI 1.0k）
量化解读： 存量两侧均衡｜ATM IV 64.2%｜历史 Rank 32%（近端代理）｜IV/RV 1.34×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 118,330 股

📆 10-30 Forward Structure
存量OI: C 11.6k / P 12.5k，今日变化ΔOI: C +2.5k / P +0.6k，平值价格ATM: C $95.92 / P $91.28 ｜ ATM IV 73.2%，净 delta 敞口 55k shares
Top ΔOI: C 1500 +409 ｜ C 2040 +267 ｜ C 2000 +265
仓位参考: Max Pain 1,650 ｜ Call Wall 1500（+1.2%，弱）（OI 0.6k） ｜ Put Wall 1500（+1.2%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 73.2%｜历史 Rank 32%（近端代理）｜IV/RV 1.53×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 54,832 股

📆 11-06 Forward Structure
存量OI: C 4.3k / P 5.0k，今日变化ΔOI: C +0.8k / P +0.6k，平值价格ATM: C $110.00 / P $120.25 ｜ ATM IV 70.7%，净 delta 敞口 4k shares
Top ΔOI: C 1650 +244 ｜ P 1500 +92
仓位参考: Max Pain 1,640 ｜ Call Wall 1560（+5.2%，弱）（OI 0.1k） ｜ Put Wall 1400（-5.6%）（OI 0.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 70.7%｜历史 Rank 32%（近端代理）｜IV/RV 1.48×（近似）｜净 delta 敞口 正 4,367 股

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 74.9% vs 10-23 64.2%（差 +10.7pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/SNDK_evening.json