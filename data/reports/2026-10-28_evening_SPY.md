# 期权晚报 2026-10-28（快照 21:00 ET）

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
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 771.43 → 收盘 772.31（+0.1%） ｜ 今日高 773.35 ｜ 低 769.25 ｜ 昨收 769.66 → 收盘 772.31（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.96 | OI比 2.26 | ATM IV 16.3% | Skew 2.4pp | Term 0.83 | ExpMove ±0.7%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 2.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.96×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.26×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 53% ｜ P/C OI(近端) 78%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 53%）｜近端持仓结构中性（P/C OI 分位 78%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-29（1D）±0.7% ｜ 10-30（2D）±0.9% ｜ 11-02（5D）±1.1% ｜ 11-03（6D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -149,168,235 | GEX Change vs 上次快照 286,735,174 | Flip: Primary Flip: 773.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2717 / LOW 333 / INVALID 1206
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 773.34（全链重定价，覆盖 94%）
最近结构参考: Flip 773（现价低于该位 0.1%）
量化视角： 负 Gamma（1.49亿，历史分位 53%，中性区）｜负 Gamma 缓解（+2.87亿）｜现价位于 Flip 下方 0.13%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 768（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 773（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-29  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 5D
11-03  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-29 Forward Structure
存量OI: C 57.9k / P 130.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.61 / P $2.67 ｜ ATM IV 16.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 768 ｜ Call Wall 790（+2.3%）（OI 4.8k） ｜ Put Wall 758（-1.9%，弱）（OI 16.1k）
量化解读： 存量 Put 重｜ATM IV 16.3%｜历史 Rank 71%（近端代理）｜IV/RV 1.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 765 ｜ Call Wall 780（+1.0%，弱）（OI 29.1k） ｜ Put Wall 750（-2.9%，弱）（OI 68.6k）

11-02（Activity LOW）仓位参考: Max Pain 767 ｜ Call Wall 775（+0.3%，弱）（OI 1.4k） ｜ Put Wall 750（-2.9%）（OI 7.3k）

11-03（Activity LOW）仓位参考: Max Pain 768 ｜ Call Wall 770（-0.3%，弱）（OI 0.9k） ｜ Put Wall 755（-2.2%，弱）（OI 1.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/SPY_evening.json