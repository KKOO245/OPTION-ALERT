# 期权晚报 2026-09-08（快照 16:40 ET）

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


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 530.96 → 收盘 528.40（-0.5%） ｜ 今日高 534.28 ｜ 低 525.49 ｜ 昨收 519.86 → 收盘 528.40（+1.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-15，窗口结束前不做对错判定）

Options: P/C成交量 2.69 | OI比 1.26 | ATM IV 44.5% | Skew 2.8pp | Term 0.92 | ExpMove ±3.4%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构正常（Term 0.92）｜保护溢价中性（Skew 2.8pp）｜当日成交偏 Put（P/C量 2.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.69×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.26×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-11（3D）±3.4% ｜ 09-18（10D）±5.5% ｜ 09-25（17D）±8.5% ｜ 10-02（24D）±5.6%
   ⇒ IV–VIX Spread: +28.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,334,637 | GEX Change vs 上次快照 -363,238 | Flip: Primary Flip: 527.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 583 / LOW 323 / INVALID 674
结构观察区: Primary Flip 527.26（全链重定价，覆盖 99%）
Call Wall 575（弱结构｜现价低于该位 8.1%）
最近结构参考: Flip 527（现价高于该位 0.2%）
量化视角： 正 Gamma（133万，无历史分位）｜正 Gamma 减弱（36万）｜现价位于 Flip 上方 0.22%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 508（MaxPain，仅结算参考）；上方 575（Call Wall，弱结构）。
• Gamma 区域：切换参考 527（全链重定价，覆盖 99%）。
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
存量OI:      C 13.0k / P 16.5k
今日变化ΔOI: C +0 / P +0
平值价格ATM:  C 9.95 / P 7.94
隐含波动率 ATM IV:  44.5%
净 delta 敞口变化 ΔOI Δ Exposure*: 0 shares
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）
该期限仓位参考（Wall 同墙位口径，Max Pain 仅结算参考）: Max Pain 508（结算参考） ｜ Call Wall 530（+0.3%）（OI 3.2k） ｜ Put Wall 500（-5.4%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 44.5%｜历史 Rank 79%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股（方向不可观测）——方向不可观测，观察点，非方向信号

09-18（Activity LOW）仓位参考: Max Pain 525（结算参考） ｜ Call Wall 575（+8.8%，弱）（OI 15.9k）

09-25（Activity LOW）仓位参考: Max Pain 545（结算参考） ｜ Call Wall 580（+9.8%，弱）（OI 1.9k）

10-02（Activity LOW）仓位参考: Max Pain 520（结算参考）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-08/SOXX_evening.json