# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.14 ｜ QQQ $655.56
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
🟡 **近现价集中开仓**: 11-27 157C ΔOI +6,894（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 143.49 → 今开 157.28（+9.6%） | 较昨收变动（含盘初走势） ｜ 今日高 160.27 ｜ 低 154.57

Options: P/C成交量 0.48 | OI比 0.58 | ATM IV 68.3% | Skew 8.0pp | Term 0.86 | ExpMove ±5.9%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价显著（Skew 8.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±5.9% ｜ 12-04（11D）±9.2% ｜ 12-11（18D）±11.7% ｜ 12-18（25D）±12.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,774,601 | GEX Change vs 上次快照 33,469,294 | Flip: Primary Flip: 150.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 448 / LOW 154 / INVALID 306
结构观察区: Primary Flip 150.06（全链重定价，覆盖 100%）
最近结构参考: Flip 150（现价高于该位 4.7%）
量化视角： 正 Gamma（1477万，无历史分位）｜由负转正（+3347万）｜现价位于 Flip 上方 4.70%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 150（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 157.5C — Vol 9,424 | 最新价 $1.07 | OI 614→7508 (ΔOI +6894张) | ΔOI/Volume 73.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6894张（+1122.8% vs前日OI），连续性待观察（方向未知）
11-27 152.5C — Vol 9,004 | 最新价 $2.08 | OI 453→7115 (ΔOI +6662张) | ΔOI/Volume 74.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6662张（+1470.6% vs前日OI），连续性待观察（方向未知）
11-27 155.0C — Vol 16,230 | 最新价 $1.56 | OI 587→6953 (ΔOI +6366张) | ΔOI/Volume 39.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6366张（+1084.5% vs前日OI），连续性待观察（方向未知）
11-27 150.0C — Vol 8,330 | 最新价 $3.05 | OI 271→5232 (ΔOI +4961张) | ΔOI/Volume 59.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4961张（+1830.6% vs前日OI），连续性待观察（方向未知）
12-18 150.0C — Vol 7,289 | 最新价 $7.95 | OI 2117→6879 (ΔOI +4762张) | ΔOI/Volume 65.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4762张（+224.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 29,645 张（Put 0 / Call 29,645），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +26.8k / P +10.4k ｜ Activity HIGH ｜ 4D
12-04  C +2.9k / P +6.1k ｜ Activity HIGH ｜ 11D
12-11  C +0.6k / P +0.8k ｜ Activity HIGH ｜ 18D
12-18  C +4.5k / P -0.2k ｜ Activity HIGH ｜ 25D

📆 11-27 Forward Structure
存量OI: C 85.8k / P 49.8k，今日变化ΔOI: C +26.8k / P +10.4k，平值价格ATM: C $4.43 / P $4.80 ｜ ATM IV 68.3%，净 delta 敞口 1.8M shares
Top ΔOI: C 157 +6,894 ｜ C 152 +6,662 ｜ C 155 +6,366
仓位参考: Max Pain 150 ｜ Call Wall 157.5（+0.2%，弱）（OI 7.5k） ｜ Put Wall 150（-4.5%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 68.3%｜历史 Rank 79%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,782,191 股

📆 12-04 Forward Structure
存量OI: C 24.0k / P 21.1k，今日变化ΔOI: C +2.9k / P +6.1k，平值价格ATM: C $6.90 / P $7.50 ｜ ATM IV 64.8%，净 delta 敞口 98k shares
Top ΔOI: P 139 +1,860 ｜ P 145 +1,085 ｜ C 155 +938
仓位参考: Max Pain 160 ｜ Call Wall 155（-1.3%，弱）（OI 1.2k） ｜ Put Wall 155（-1.3%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 64.8%｜历史 Rank 79%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 98,191 股

📆 12-11 Forward Structure
存量OI: C 10.5k / P 14.2k，今日变化ΔOI: C +0.6k / P +0.8k，平值价格ATM: C $9.10 / P $9.28 ｜ ATM IV 62.9%，净 delta 敞口 29k shares
Top ΔOI: C 170 +320 ｜ C 150 +236
仓位参考: Max Pain 165 ｜ Call Wall 170（+8.2%，弱）（OI 0.9k） ｜ Put Wall 150（-4.5%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 62.9%｜历史 Rank 79%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 28,968 股

📆 12-18 Forward Structure
存量OI: C 264.4k / P 258.2k，今日变化ΔOI: C +4.5k / P -0.2k，平值价格ATM: C $9.21 / P $9.95 ｜ ATM IV 60.1%，净 delta 敞口 445k shares
Top ΔOI: C 150 +4,762 ｜ C 145 +2,071 ｜ P 130 +955
仓位参考: Max Pain 140 ｜ Call Wall 165（+5.0%，弱）（OI 14.2k） ｜ Put Wall 160（+1.8%，弱）（OI 18.9k）
量化解读： 存量两侧均衡｜ATM IV 60.1%｜历史 Rank 79%（近端代理）｜IV/RV 1.00×（近似）｜净 delta 敞口 正 445,252 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/PLTR_morning.json