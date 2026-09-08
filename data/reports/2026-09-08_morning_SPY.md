# 期权晨报 2026-09-08（快照 10:49 ET）

📊 市场环境

SPY $765.79 ｜ QQQ $718.36
VIX 15.51 ↑1.4%（5D -5.1%） ｜ Vol Regime: NORMAL
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


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 770.19 → 今开 769.07（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 769.70 ｜ 低 765.99

Options: P/C成交量 1.46 | OI比 2.40 | ATM IV 12.8% | Skew 1.2pp | Term 0.99 | ExpMove ±0.5%（近端） | Rank 49%
量化视角： IV 中性（Rank 49%）｜期限结构正常（Term 0.99）｜保护溢价薄（Skew 1.2pp）｜当日成交偏 Put（P/C量 1.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.46×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.40×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 35% ｜ P/C OI(近端) 84%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 35%）｜近端持仓结构中性（P/C OI 分位 84%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-09（1D）±0.5% ｜ 09-10（2D）±0.7% ｜ 09-11（3D）±1.0% ｜ 09-14（6D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -951,952,165 | GEX Change vs 上次快照 -696,748,832 | Flip: Primary Flip: 771.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 2833 / LOW 344 / INVALID 1311
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 771.73（全链重定价，覆盖 98%）
Call Wall 800（弱结构｜现价低于该位 4.2%）
最近结构参考: Flip 772（现价低于该位 0.7%）
量化视角： 负 Gamma（9.52亿，历史分位 35%，中性区）｜负 Gamma 加深（6.97亿）｜现价位于 Flip 下方 0.68%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 770（MaxPain，仅结算参考） / 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 772（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-09  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-10  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-11  C +0 / P +0 ｜ Activity LOW ｜ 3D
09-14  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-09 Forward Structure
存量OI:      C 62.7k / P 86.0k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 2.55 / P 1.60
隐含波动率 ATM IV:  11.4%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 768（结算参考） ｜ Call Wall 785（+2.4%）（OI 5.1k） ｜ Put Wall 710（-7.4%，弱）（OI 8.1k）
量化解读： 存量 Put 重｜ATM IV 11.4%｜历史 Rank 49%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-10（Activity LOW）仓位参考: Max Pain 768（结算参考） ｜ Call Wall 770（+0.5%，弱）（OI 3.7k） ｜ Put Wall 695（-9.3%，弱）（OI 8.0k）

09-11（Activity LOW）仓位参考: Max Pain 769（结算参考） ｜ Call Wall 777（+1.4%，弱）（OI 17.8k） ｜ Put Wall 760（-0.8%）（OI 55.3k）

09-14（Activity LOW）仓位参考: Max Pain 770（结算参考） ｜ Call Wall 800（+4.4%，弱）（OI 5.5k） ｜ Put Wall 755（-1.5%，弱）（OI 2.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-08/SPY_morning.json