# 期权晚报 2026-09-08（快照 17:30 ET）

📊 市场环境

SPY $765.96 ｜ QQQ $718.36
VIX 15.72 ↑2.8%（5D -3.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 40.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-10 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0
- 周四 09-10 10:00　【高】成屋销售　预测 3.99 ｜ 实际 待公布 ｜ 前值 4.06
- 周五 09-11 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.2
- 周五 09-11 08:30　【高】Inflation Rate MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.1
- 周五 09-11 08:30　【高】Inflation Rate YoY　预测 3.4 ｜ 实际 待公布 ｜ 前值 3.4
- 周五 09-11 08:30　【高】Core Inflation Rate YoY　预测 2.4 ｜ 实际 待公布 ｜ 前值 2.5
- 周五 09-11 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 51 ｜ 实际 待公布 ｜ 前值 51.7

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 160.76 → 收盘 161.93（+0.7%） ｜ 今日高 163.43 ｜ 低 158.79 ｜ 昨收 163.81 → 收盘 161.93（-1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 3.07 | OI比 1.80 | ATM IV 34.9% | Skew -0.3pp | Term 0.82 | ExpMove ±3.2%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.82，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.3pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 3.07）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.07×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.80×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（3D）±3.2% ｜ 09-18（10D）±4.6% ｜ 09-25（17D）±4.6% ｜ 10-02（24D）±2.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -21,774,586 | GEX Change vs 上次快照 -1,778,305 | Flip: Primary Flip: 165.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 405 / LOW 127 / INVALID 320
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 165.68（全链重定价，覆盖 96%）
Put Wall 158（弱结构｜现价高于该位 2.5%） | Call Wall 170（弱结构｜现价低于该位 4.7%）
最近结构参考: Flip 166（现价低于该位 2.3%）
量化视角： 负 Gamma（2177万，无历史分位）｜负 Gamma 加深（178万）｜现价位于 Flip 下方 2.26%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 158（Put Wall，弱结构）；上方 163（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-11  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 10D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 17D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 24D

📆 09-11 Forward Structure
存量OI:      C 8.5k / P 15.4k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 3.20 / P 2.00
隐含波动率 ATM IV:  34.9%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 163（结算参考） ｜ Call Wall 164（+1.3%，弱）（OI 2.0k） ｜ Put Wall 162（+0.0%，弱）（OI 3.8k）
量化解读： 存量 Put 重｜ATM IV 34.9%｜历史 Rank 61%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 158（结算参考） ｜ Call Wall 155（-4.3%，弱）（OI 10.8k） ｜ Put Wall 158（-2.4%，弱）（OI 16.9k）

09-25（Activity LOW）仓位参考: Max Pain 160（结算参考） ｜ Call Wall 167（+3.1%）（OI 1.4k）

10-02（Activity LOW）仓位参考: Max Pain 164（结算参考） ｜ Call Wall 165（+1.9%）（OI 0.2k） ｜ Put Wall 150（-7.4%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-08/XBI_evening.json