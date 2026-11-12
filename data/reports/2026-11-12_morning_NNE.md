# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $757.88 ｜ QQQ $688.17
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 11P ΔOI +23（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 11.59 → 今开 11.04（-4.7%） | 较昨收变动（含盘初走势） ｜ 今日高 11.44 ｜ 低 10.91

Options: P/C成交量 1.24 | OI比 0.40 | ATM IV 89.6% | Skew 5.7pp | Term 0.94 | ExpMove ±8.5%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 5.7pp）｜⚠️ 重点观察：存量 Call 重（OI比 0.40）+ 当日成交偏 Put（P/C量 1.24）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±8.5% ｜ 11-20（8D）±13.6% ｜ 11-27（15D）±11.7% ｜ 12-04（22D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,093,936 | GEX Change vs 上次快照 -461,834 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 146 / LOW 79 / INVALID 161
结构观察区: NO_CROSS
Put Wall 11（现价高于该位 0.9%）
最近结构参考: Put Wall 11（现价高于该位 0.9%）
量化视角： 正 Gamma（109万，无历史分位）｜正 Gamma 减弱（46万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall）；上方 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 12.5C — Vol 46 | 最新价 $0.07 | OI 466→508 (ΔOI +42张) | ΔOI/Volume 91.3% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增42张（+9.0% vs前日OI），值得跟踪（方向未知）
11-20 12.0P — Vol 42 | 最新价 $0.81 | OI 300→337 (ΔOI +37张) | ΔOI/Volume 88.1% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增37张（+12.3% vs前日OI），值得跟踪（方向未知）
11-13 11.5P — Vol 55 | 最新价 $0.15 | OI 80→103 (ΔOI +23张) | ΔOI/Volume 41.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23张（+28.8% vs前日OI），连续性待观察（方向未知）
11-20 12.5C — Vol 24 | 最新价 $0.25 | OI 100→120 (ΔOI +20张) | ΔOI/Volume 83.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20张（+20.0% vs前日OI），连续性待观察（方向未知）
11-27 13.5C — Vol 19 | 最新价 $0.30 | OI 217→236 (ΔOI +19张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增19张（+8.8% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 141 张（Put 60 / Call 81），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +32 / P +1 ｜ Activity MEDIUM △ ｜ 1D
11-20  C +41 / P -0.2k ｜ Activity HIGH ｜ 8D
11-27  C +43 / P -76 ｜ Activity MEDIUM △ ｜ 15D
12-04  C +3 / P +6 ｜ Activity MEDIUM △ ｜ 22D

📆 11-13 Forward Structure
存量OI: C 3.1k / P 1.2k，今日变化ΔOI: C +32 / P +1，平值价格ATM: C $0.85 / P $0.09 ｜ ATM IV 89.6%，净 delta 敞口 388 shares
Top ΔOI: P 11 +23 ｜ P 12 -16
仓位参考: Max Pain 12 ｜ Call Wall 12（+8.1%，弱）（OI 0.3k） ｜ Put Wall 11（-0.9%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 89.6%｜历史 Rank 24%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 388 股

📆 11-20 Forward Structure
存量OI: C 6.2k / P 2.1k，今日变化ΔOI: C +41 / P -0.2k，平值价格ATM: C $1.23 / P $0.28 ｜ ATM IV 89.1%，净 delta 敞口 9k shares
Top ΔOI: P 11 -146 ｜ P 11 -109 ｜ P 12 +37
仓位参考: Max Pain 12 ｜ Call Wall 12（+8.1%，弱）（OI 0.7k） ｜ Put Wall 12（+8.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 89.1%｜历史 Rank 24%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,809 股

11-27（MEDIUM △）Top ΔOI: 12C +14
11-27（MEDIUM △）仓位参考: Max Pain 12

12-04（MEDIUM △）Top ΔOI: 11P +5
12-04（MEDIUM △）仓位参考: Max Pain 13

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/NNE_morning.json