# 期权晚报 2026-10-29（快照 21:00 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 17.20 ↑1.7%（5D -9.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 768.79 → 收盘 769.36（+0.1%） ｜ 今日高 770.76 ｜ 低 766.62 ｜ 昨收 772.31 → 收盘 769.36（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.20 | OI比 2.47 | ATM IV 14.5% | Skew 2.1pp | Term 0.90 | ExpMove ±0.7%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜当日成交偏 Put（P/C量 1.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.20×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.47×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 41% ｜ P/C OI(近端) 86%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 41%）｜近端持仓结构中性（P/C OI 分位 86%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-30（1D）±0.7% ｜ 11-02（4D）±0.9% ｜ 11-03（5D）±1.1% ｜ 11-04（6D）±1.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -667,478,684 | GEX Change vs 上次快照 121,013,381 | Flip: Primary Flip: 773.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 2600 / LOW 383 / INVALID 1035
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 773.12（全链重定价，覆盖 92%）
最近结构参考: Flip 773（现价低于该位 0.5%）
量化视角： 负 Gamma（6.67亿，历史分位 41%，中性区）｜负 Gamma 缓解（+1.21亿）｜现价位于 Flip 下方 0.49%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 765（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 773（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-03  C +0 / P +0 ｜ Activity LOW ｜ 5D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-30 Forward Structure
存量OI: C 674.7k / P 1666.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.14 / P $4.22 ｜ ATM IV 14.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 765 ｜ Call Wall 780（+1.4%，弱）（OI 27.9k） ｜ Put Wall 750（-2.5%，弱）（OI 67.1k）
量化解读： 存量 Put 重｜ATM IV 14.5%｜历史 Rank 62%（近端代理）｜IV/RV 1.59×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-02（Activity LOW）仓位参考: Max Pain 770 ｜ Call Wall 770（+0.1%，弱）（OI 2.1k） ｜ Put Wall 750（-2.5%，弱）（OI 8.9k）

11-03（Activity LOW）仓位参考: Max Pain 770 ｜ Call Wall 780（+1.4%，弱）（OI 3.3k） ｜ Put Wall 755（-1.9%，弱）（OI 2.9k）

11-04（Activity LOW）仓位参考: Max Pain 769 ｜ Call Wall 771（+0.2%，弱）（OI 1.3k） ｜ Put Wall 767（-0.3%）（OI 29.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/SPY_evening.json