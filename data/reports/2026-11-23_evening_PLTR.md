# 期权晚报 2026-11-23（快照 16:40 ET）

📊 市场环境

SPY $722.29 ｜ QQQ $651.03
VIX 26.62 ↓25.8%（5D +16.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
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
🟡 **近现价集中开仓**: 11-27 157C ΔOI +6,894（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 157.28 → 收盘 159.36（+1.3%） ｜ 今日高 161.17 ｜ 低 154.57 ｜ 昨收 143.49 → 收盘 159.36（+11.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.45 | OI比 0.58 | ATM IV 68.0% | Skew 9.8pp | Term 0.84 | ExpMove ±5.7%（近端） | Rank 78%
量化视角： IV 历史高位（Rank 78%，期权偏贵）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价显著（Skew 9.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±5.7% ｜ 12-04（11D）±8.7% ｜ 12-11（18D）±10.7% ｜ 12-18（25D）±12.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 18,220,675 | GEX Change vs 上次快照 3,446,074 | Flip: Primary Flip: 150.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 460 / LOW 159 / INVALID 289
结构观察区: Primary Flip 150.34（全链重定价，覆盖 100%）
最近结构参考: Flip 150（现价高于该位 6.0%）
量化视角： 正 Gamma（1822万，无历史分位）｜正 Gamma 增强（+345万）｜现价位于 Flip 上方 6.00%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 150（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 157.5C — Vol 3,945 | 最新价 $5.64 | OI 614→7508 (ΔOI +6894张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6894张（+1122.8% vs前日OI），连续性待观察（方向未知）
11-27 152.5C — Vol 956 | 最新价 $9.41 | OI 453→7115 (ΔOI +6662张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6662张（+1470.6% vs前日OI），连续性待观察（方向未知）
11-27 155.0C — Vol 2,307 | 最新价 $7.15 | OI 587→6953 (ΔOI +6366张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6366张（+1084.5% vs前日OI），连续性待观察（方向未知）
11-27 150.0C — Vol 1,091 | 最新价 $11.00 | OI 271→5232 (ΔOI +4961张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4961张（+1830.6% vs前日OI），连续性待观察（方向未知）
12-18 150.0C — Vol 186 | 最新价 $15.98 | OI 2117→6879 (ΔOI +4762张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4762张（+224.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 29,645 张（Put 0 / Call 29,645），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +26.8k / P +10.4k ｜ Activity HIGH ｜ 4D
12-04  C +2.9k / P +6.1k ｜ Activity HIGH ｜ 11D
12-11  C +0.6k / P +0.8k ｜ Activity HIGH ｜ 18D
12-18  C +4.5k / P -0.2k ｜ Activity HIGH ｜ 25D

📆 11-27 Forward Structure
存量OI: C 85.8k / P 49.8k，今日变化ΔOI: C +26.8k / P +10.4k，平值价格ATM: C $4.21 / P $4.80 ｜ ATM IV 68.0%，净 delta 敞口 2.0M shares
Top ΔOI: C 157 +6,894 ｜ C 152 +6,662 ｜ C 155 +6,366
仓位参考: Max Pain 150 ｜ Call Wall 157.5（-1.2%，弱）（OI 7.5k） ｜ Put Wall 150（-5.9%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 68.0%｜历史 Rank 78%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,987,618 股

📆 12-04 Forward Structure
存量OI: C 24.0k / P 21.1k，今日变化ΔOI: C +2.9k / P +6.1k，平值价格ATM: C $6.75 / P $7.05 ｜ ATM IV 62.6%，净 delta 敞口 129k shares
Top ΔOI: P 139 +1,860 ｜ P 145 +1,085 ｜ C 155 +938
仓位参考: Max Pain 160 ｜ Call Wall 175（+9.8%，弱）（OI 1.4k） ｜ Put Wall 155（-2.7%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 62.6%｜历史 Rank 78%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 129,493 股

📆 12-11 Forward Structure
存量OI: C 10.5k / P 14.2k，今日变化ΔOI: C +0.6k / P +0.8k，平值价格ATM: C $8.52 / P $8.46 ｜ ATM IV 60.8%，净 delta 敞口 33k shares
Top ΔOI: C 170 +320 ｜ C 150 +236
仓位参考: Max Pain 165 ｜ Call Wall 170（+6.7%，弱）（OI 0.9k） ｜ Put Wall 150（-5.9%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 60.8%｜历史 Rank 78%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 33,398 股

📆 12-18 Forward Structure
存量OI: C 264.4k / P 258.2k，今日变化ΔOI: C +4.5k / P -0.2k，平值价格ATM: C $9.80 / P $9.80 ｜ ATM IV 59.4%，净 delta 敞口 470k shares
Top ΔOI: C 150 +4,762 ｜ C 145 +2,071 ｜ P 130 +955
仓位参考: Max Pain 140 ｜ Call Wall 165（+3.5%，弱）（OI 14.2k） ｜ Put Wall 160（+0.4%，弱）（OI 18.9k）
量化解读： 存量两侧均衡｜ATM IV 59.4%｜历史 Rank 78%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 470,496 股

📅 事件差分（观察，非因果）: 11-27（4D）ATM IV 68.0% vs 12-04 62.6%（差 +5.4pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/PLTR_evening.json