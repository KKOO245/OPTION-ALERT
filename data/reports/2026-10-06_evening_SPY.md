# 期权晚报 2026-10-06（快照 16:40 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.01 ↓3.3%（5D -6.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-07 742P ΔOI +8,072（距现价 -4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-09 787C ΔOI -200,738 占该期限总 OI 18.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 778.15 → 收盘 779.09（+0.1%） ｜ 今日高 781.62 ｜ 低 777.96 ｜ 昨收 774.83 → 收盘 779.09（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.82 | OI比 0.92 | ATM IV 11.7% | Skew -0.9pp | Term 1.08 | ExpMove ±0.4%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 82% ｜ P/C OI(近端) 1%
量化视角的组合解读： Gamma 异常偏正（GEX 分位 82%）｜近端持仓极端 Call 重（P/C OI 分位 1%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-07（1D）±0.4% ｜ 10-08（2D）±0.6% ｜ 10-09（3D）±0.8% ｜ 10-12（6D）±0.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,365,860,390 | GEX Change vs 上次快照 -113,703,624 | Flip: Primary Flip: 773.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2442 / LOW 424 / INVALID 2102
结构观察区: Primary Flip 773.34（全链重定价，覆盖 94%）
Call Wall 785（现价低于该位 0.8%）
最近结构参考: Flip 773（现价高于该位 0.7%）
量化视角： 正 Gamma（13.66亿，历史分位偏正区，比 82% 的交易日更正）｜正 Gamma 减弱（1.14亿）｜现价位于 Flip 上方 0.74%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 772（MaxPain，仅结算参考）；上方 785（Call Wall）。
• Gamma 区域：切换参考 773（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-07  C +23.1k / P +57.8k ｜ Activity HIGH ｜ 1D
10-08  C +16.8k / P +23.1k ｜ Activity HIGH ｜ 2D
10-09  C -155.9k / P +70.2k ｜ Activity HIGH ｜ 3D
10-12  C +14.4k / P +40.5k ｜ Activity HIGH ｜ 6D

📆 10-07 Forward Structure
存量OI: C 146.6k / P 171.3k，今日变化ΔOI: C +23.1k / P +57.8k，平值价格ATM: C $1.80 / P $1.29 ｜ ATM IV 9.4%，净 delta 敞口 716k shares
Top ΔOI: P 742 +8,072 ｜ P 743 +7,350 ｜ C 782 +4,045
仓位参考: Max Pain 771 ｜ Call Wall 802（+2.9%，弱）（OI 16.9k） ｜ Put Wall 760（-2.5%，弱）（OI 6.9k）
量化解读： 存量两侧均衡｜ATM IV 9.4%｜历史 Rank 40%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 715,843 股

📆 10-08 Forward Structure
存量OI: C 63.6k / P 84.6k，今日变化ΔOI: C +16.8k / P +23.1k，平值价格ATM: C $2.65 / P $2.03 ｜ ATM IV 10.1%，净 delta 敞口 479k shares
Top ΔOI: P 756 +2,333 ｜ P 753 +2,209 ｜ C 781 +2,205
仓位参考: Max Pain 770 ｜ Call Wall 795（+2.0%，弱）（OI 6.5k） ｜ Put Wall 756（-3.0%，弱）（OI 2.9k）
量化解读： 存量 Put 重｜ATM IV 10.1%｜历史 Rank 40%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 479,339 股

📆 10-09 Forward Structure
存量OI: C 499.9k / P 564.5k，今日变化ΔOI: C -155.9k / P +70.2k，平值价格ATM: C $3.43 / P $2.55 ｜ ATM IV 10.4%，净 delta 敞口 -3.2M shares
Top ΔOI: C 787 -200,738 ｜ P 767 +17,914 ｜ C 785 +16,349
仓位参考: Max Pain 770 ｜ Call Wall 785（+0.8%）（OI 125.9k） ｜ Put Wall 767（-1.6%，弱）（OI 64.6k）
量化解读： 存量两侧均衡｜ATM IV 10.4%｜历史 Rank 40%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,169,865 股

📆 10-12 Forward Structure
存量OI: C 37.1k / P 72.3k，今日变化ΔOI: C +14.4k / P +40.5k，平值价格ATM: C $3.97 / P $3.12 ｜ ATM IV 8.9%，净 delta 敞口 255k shares
Top ΔOI: C 793 +2,053
仓位参考: Max Pain 770 ｜ Call Wall 785（+0.8%）（OI 3.1k） ｜ Put Wall 770（-1.2%，弱）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 8.9%｜历史 Rank 40%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 正 254,847 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/SPY_evening.json