# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $722.55 ｜ QQQ $657.00
VIX 27.37 ↓23.7%（5D +19.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 19.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.4 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-25 40C ΔOI +4,085（距现价 +2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-02 42C ΔOI -1,192 占该期限总 OI 10.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 36.97 → 今开 39.86（+7.8%） | 较昨收变动（含盘初走势） ｜ 今日高 39.91 ｜ 低 39.12

Options: P/C成交量 1.12 | OI比 0.34 | ATM IV 75.0% | Skew 3.1pp | Term 0.66 | ExpMove ±4.1%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价中性（Skew 3.1pp）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.12×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-25（2D）±4.1% ｜ 11-27（4D）±4.7% ｜ 11-30（7D）±5.5% ｜ 12-02（9D）±6.6%
   ⇒ IV–VIX Spread: +47.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 17,140,590 | GEX Change vs 上次快照 31,353,489 | Flip: Primary Flip: 38.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 745 / LOW 223 / INVALID 652
结构观察区: Primary Flip 38.53（全链重定价，覆盖 98%）
Put Wall 40（弱结构｜现价低于该位 1.4%）
最近结构参考: Put Wall 40（现价低于该位 1.4%）
量化视角： 正 Gamma（1714万，无历史分位）｜由负转正（+3135万）｜现价位于 Flip 上方 2.33%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 38（MaxPain，仅结算参考）；上方 40（Put Wall，弱结构）。
• Gamma 区域：切换参考 39（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-23 41.0C — Vol 4,861 | 最新价 $0.02 | OI 2644→7089 (ΔOI +4445张) | ΔOI/Volume 91.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4445张（+168.1% vs前日OI），连续性待观察（方向未知）
11-27 40.0C — Vol 7,668 | 最新价 $0.25 | OI 1901→6136 (ΔOI +4235张) | ΔOI/Volume 55.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4235张（+222.8% vs前日OI），连续性待观察（方向未知）
11-25 40.5C — Vol 4,831 | 最新价 $0.14 | OI 397→4482 (ΔOI +4085张) | ΔOI/Volume 84.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4085张（+1029.0% vs前日OI），连续性待观察（方向未知）
12-18 35.0P — Vol 5,692 | 最新价 $1.54 | OI 10243→13699 (ΔOI +3456张) | ΔOI/Volume 60.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3456张（+33.7% vs前日OI），连续性待观察（方向未知）
12-04 40.0C — Vol 4,035 | 最新价 $0.57 | OI 444→3570 (ΔOI +3126张) | ΔOI/Volume 77.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3126张（+704.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 19,347 张（Put 3,456 / Call 15,891），跨 5 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 41.1k / P 14.1k，今日成交量: C 7.3k / P 8.2k，平值价格ATM: C $0.26 / P $0.38 ｜ ATM IV 75.0%，预期波动 ±1.6%，Max Pain 38
Top ΔOI: C 41 +4,445 ｜ P 36 +1,733 ｜ P 35 +1,524

📆 Forward Expiration Structure

11-25  C +7.7k / P +3.0k ｜ Activity HIGH ｜ 2D
11-27  C +14.8k / P +7.1k ｜ Activity HIGH ｜ 4D
11-30  C +2.6k / P +3.3k ｜ Activity HIGH ｜ 7D
12-02  C +0.3k / P +0.8k ｜ Activity HIGH ｜ 9D

📆 11-25 Forward Structure
存量OI: C 28.6k / P 13.2k，今日变化ΔOI: C +7.7k / P +3.0k，平值价格ATM: C $0.79 / P $0.84 ｜ ATM IV 65.6%，净 delta 敞口 325k shares
Top ΔOI: C 40 +4,085 ｜ C 40 +773 ｜ P 36 +701
仓位参考: Max Pain 40 ｜ Call Wall 40.5（+2.7%，弱）（OI 4.5k） ｜ Put Wall 39（-1.1%）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 65.6%｜历史 Rank 95%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 324,814 股

📆 11-27 Forward Structure
存量OI: C 109.1k / P 41.2k，今日变化ΔOI: C +14.8k / P +7.1k，平值价格ATM: C $0.89 / P $0.97 ｜ ATM IV 57.0%，净 delta 敞口 567k shares
Top ΔOI: C 40 +4,235 ｜ C 41 +2,395
仓位参考: Max Pain 41 ｜ Call Wall 40（+1.4%，弱）（OI 6.1k） ｜ Put Wall 40（+1.4%）（OI 9.3k）
量化解读： 存量 Call 重｜ATM IV 57.0%｜历史 Rank 95%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 566,754 股

📆 11-30 Forward Structure
存量OI: C 25.4k / P 10.0k，今日变化ΔOI: C +2.6k / P +3.3k，平值价格ATM: C $1.04 / P $1.14 ｜ ATM IV 48.9%，净 delta 敞口 90k shares
Top ΔOI: C 40 +1,630 ｜ P 37 +605
仓位参考: Max Pain 40 ｜ Put Wall 39（-1.1%）（OI 4.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.9%｜历史 Rank 95%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 89,894 股

📆 12-02 Forward Structure
存量OI: C 8.0k / P 2.9k，今日变化ΔOI: C +0.3k / P +0.8k，平值价格ATM: C $1.24 / P $1.35 ｜ ATM IV 50.8%，净 delta 敞口 13k shares
Top ΔOI: C 42 -1,192 ｜ P 37 +285
仓位参考: Max Pain 40 ｜ Call Wall 42（+6.5%）（OI 5.1k） ｜ Put Wall 39（-1.1%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 50.8%｜历史 Rank 95%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 13,461 股

📅 事件差分（观察，非因果）: 11-25（2D）ATM IV 65.6% vs 11-27 57.0%（差 +8.6pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/SLV_morning.json