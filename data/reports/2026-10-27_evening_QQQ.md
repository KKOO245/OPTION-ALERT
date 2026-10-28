# 期权晚报 2026-10-27（快照 21:00 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $nan
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 715.10 → 收盘 721.25（+0.9%） ｜ 今日高 722.86 ｜ 低 713.59 ｜ 昨收 712.20 → 收盘 721.25（+1.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-03，窗口结束前不做对错判定）

Options: P/C成交量 1.24 | OI比 1.57 | ATM IV 24.5% | Skew 4.1pp | Term 0.88 | ExpMove ±1.0%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 4.1pp）｜当日成交偏 Put（P/C量 1.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.57×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 32% ｜ P/C OI(近端) 45%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 32%）｜近端持仓结构中性（P/C OI 分位 45%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-28（1D）±1.0% ｜ 10-29（2D）±1.6% ｜ 10-30（3D）±1.9% ｜ 11-02（6D）±2.2%
   ⇒ IV–VIX Spread: +7.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -277,277,258 | GEX Change vs 上次快照 179,338,723 | Flip: Primary Flip: 727.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2858 / LOW 246 / INVALID 1132
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 727.21（全链重定价，覆盖 99%）
最近结构参考: Flip 727（现价低于该位 0.8%）
量化视角： 负 Gamma（2.77亿，历史分位 32%，中性区）｜负 Gamma 缓解（+1.79亿）｜现价位于 Flip 下方 0.82%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 715（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 727（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-28  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-29  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-28 Forward Structure
存量OI: C 63.0k / P 98.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.69 / P $3.74 ｜ ATM IV 24.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 715 ｜ Call Wall 715（-0.9%，弱）（OI 4.1k） ｜ Put Wall 710（-1.6%，弱）（OI 4.6k）
量化解读： 存量 Put 重｜ATM IV 24.5%｜历史 Rank 78%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-29（Activity LOW）仓位参考: Max Pain 717 ｜ Call Wall 725（+0.5%，弱）（OI 2.3k） ｜ Put Wall 705（-2.3%，弱）（OI 2.0k）

10-30（Activity LOW）仓位参考: Max Pain 722 ｜ Call Wall 740（+2.6%，弱）（OI 21.4k） ｜ Put Wall 700（-2.9%，弱）（OI 44.5k）

11-02（Activity LOW）仓位参考: Max Pain 714 ｜ Call Wall 740（+2.6%）（OI 15.7k） ｜ Put Wall 710（-1.6%，弱）（OI 1.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/QQQ_evening.json