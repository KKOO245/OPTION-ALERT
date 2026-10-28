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


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 48.50 → 收盘 49.16（+1.4%） ｜ 今日高 49.24 ｜ 低 48.48 ｜ 昨收 48.66 → 收盘 49.16（+1.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-03，窗口结束前不做对错判定）

Options: P/C成交量 0.42 | OI比 0.69 | ATM IV 48.6% | Skew 3.9pp | Term 0.76 | ExpMove ±2.0%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价中性（Skew 3.9pp）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-28（1D）±2.0% ｜ 10-30（3D）±3.2% ｜ 11-02（6D）±3.7% ｜ 11-04（8D）±4.5%
   ⇒ IV–VIX Spread: +31.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,423,351 | GEX Change vs 上次快照 8,119,905 | Flip: Primary Flip: 48.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 728 / LOW 108 / INVALID 356
结构观察区: Primary Flip 48.88（全链重定价，覆盖 98%）
Put Wall 50（弱结构｜现价低于该位 1.7%）
最近结构参考: Flip 49（现价高于该位 0.6%）
量化视角： 正 Gamma（842万，无历史分位）｜正 Gamma 增强（+812万）｜现价位于 Flip 上方 0.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 49（MaxPain，仅结算参考）；上方 50（Put Wall，弱结构）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-28  C +0 / P +0 ｜ Activity LOW ｜ 1D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 6D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 10-28 Forward Structure
存量OI: C 25.5k / P 17.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.59 / P $0.42 ｜ ATM IV 48.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 49 ｜ Call Wall 50（+1.7%）（OI 6.4k） ｜ Put Wall 45.5（-7.4%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 48.6%｜历史 Rank 81%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 51 ｜ Call Wall 52.5（+6.8%，弱）（OI 3.5k） ｜ Put Wall 45（-8.5%，弱）（OI 4.2k）

11-02（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 50.5（+2.7%，弱）（OI 0.5k） ｜ Put Wall 47.5（-3.4%）（OI 0.6k）

11-04（Activity LOW）仓位参考: Max Pain 48 ｜ Call Wall 51.5（+4.8%）（OI 3.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/SLV_evening.json