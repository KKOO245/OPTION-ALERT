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
🟡 **近现价集中开仓**: 09-23 780C ΔOI +13,010（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 774.03 → 收盘 773.38（-0.1%） ｜ 今日高 775.14 ｜ 低 772.59 ｜ 昨收 773.50 → 收盘 773.38（-0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.82 | OI比 1.21 | ATM IV 17.0% | Skew -0.8pp | Term 0.69 | ExpMove ±0.4%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 71% ｜ P/C OI(近端) 7%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 71%）｜近端持仓极端 Call 重（P/C OI 分位 7%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-23（1D）±0.4% ｜ 09-24（2D）±0.6% ｜ 09-25（3D）±0.8% ｜ 09-28（6D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 735,447,887 | GEX Change vs 上次快照 -213,091,095 | Flip: Primary Flip: 769.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2939 / LOW 455 / INVALID 1794
结构观察区: Primary Flip 769.34（全链重定价，覆盖 96%）
Call Wall 785（弱结构｜现价低于该位 1.5%）
最近结构参考: Flip 769（现价高于该位 0.5%）
量化视角： 正 Gamma（7.35亿，历史分位 71%，中性区）｜正 Gamma 减弱（2.13亿）｜现价位于 Flip 上方 0.53%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 770（MaxPain，仅结算参考）；上方 785（Call Wall，弱结构）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-23  C +67.7k / P +58.7k ｜ Activity HIGH ｜ 1D
09-24  C +19.1k / P +15.4k ｜ Activity HIGH ｜ 2D
09-25  C +21.6k / P +60.4k ｜ Activity HIGH ｜ 3D
09-28  C +14.1k / P +27.3k ｜ Activity HIGH ｜ 6D

📆 09-23 Forward Structure
存量OI: C 135.1k / P 124.0k，今日变化ΔOI: C +67.7k / P +58.7k，平值价格ATM: C $1.86 / P $1.21 ｜ ATM IV 9.4%，净 delta 敞口 -316k shares
Top ΔOI: C 780 +13,010 ｜ C 801 +10,694 ｜ P 770 +7,362
仓位参考: Max Pain 770 ｜ Call Wall 780（+0.9%）（OI 16.6k） ｜ Put Wall 770（-0.4%，弱）（OI 7.5k）
量化解读： 存量两侧均衡｜ATM IV 9.4%｜历史 Rank 74%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 316,455 股

📆 09-24 Forward Structure
存量OI: C 62.3k / P 66.7k，今日变化ΔOI: C +19.1k / P +15.4k，平值价格ATM: C $2.64 / P $1.91 ｜ ATM IV 9.8%，净 delta 敞口 65k shares
Top ΔOI: C 778 +2,416 ｜ C 790 +2,346 ｜ C 780 +1,722
仓位参考: Max Pain 764 ｜ Call Wall 771（-0.3%）（OI 5.4k） ｜ Put Wall 752（-2.8%，弱）（OI 3.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 9.8%｜历史 Rank 74%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 64,643 股

📆 09-25 Forward Structure
存量OI: C 284.9k / P 624.2k，今日变化ΔOI: C +21.6k / P +60.4k，平值价格ATM: C $3.40 / P $2.43 ｜ ATM IV 10.2%，净 delta 敞口 -714k shares
Top ΔOI: C 790 -7,980 ｜ P 770 +4,804
仓位参考: Max Pain 766 ｜ Call Wall 772（-0.2%，弱）（OI 30.3k）
量化解读： 存量 Put 重｜ATM IV 10.2%｜历史 Rank 74%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 714,468 股

📆 09-28 Forward Structure
存量OI: C 47.8k / P 68.5k，今日变化ΔOI: C +14.1k / P +27.3k，平值价格ATM: C $4.09 / P $2.94 ｜ ATM IV 8.8%，净 delta 敞口 -17k shares
Top ΔOI: P 770 +3,391
仓位参考: Max Pain 770 ｜ Call Wall 780（+0.9%）（OI 10.8k） ｜ Put Wall 770（-0.4%，弱）（OI 3.5k）
量化解读： 存量 Put 重｜ATM IV 8.8%｜历史 Rank 74%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 负 17,392 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/SPY_evening.json