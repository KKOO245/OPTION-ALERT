# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $718.15 ｜ QQQ $638.10
VIX 27.25 ↑2.4%（5D +7.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 12-18 80P ΔOI +1,312（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 87.71 → 今开 82.74（-5.7%） | 较昨收变动（含盘初走势） ｜ 今日高 83.82 ｜ 低 77.12

Options: P/C成交量 0.73 | OI比 0.44 | ATM IV 132.7% | Skew 9.8pp | Term 0.85 | ExpMove ±9.6%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价显著（Skew 9.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±9.6% ｜ 12-04（10D）±17.0% ｜ 12-11（17D）±20.8% ｜ 12-18（24D）±23.7%
   ⇒ IV–VIX Spread: +105.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -20,134,292 | GEX Change vs 上次快照 -1,877,580 | Flip: Primary Flip: 87.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 990 / LOW 954 / INVALID 3960
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 87.21（全链重定价，覆盖 100%）
Put Wall 75（弱结构｜现价高于该位 6.5%）
最近结构参考: Put Wall 75（现价高于该位 6.5%）
量化视角： 负 Gamma（2013万，无历史分位）｜负 Gamma 加深（188万）｜现价位于 Flip 下方 8.38%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 75（Put Wall，弱结构）；上方 98（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 87（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 105.0C — Vol 7,993 | 最新价 $0.42 | OI 1660→4145 (ΔOI +2485张) | ΔOI/Volume 31.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2485张（+149.7% vs前日OI），连续性待观察（方向未知）
12-18 95.0C — Vol 3,713 | 最新价 $7.24 | OI 786→3129 (ΔOI +2343张) | ΔOI/Volume 63.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2343张（+298.1% vs前日OI），连续性待观察（方向未知）
11-27 120.0C — Vol 2,689 | 最新价 $0.08 | OI 1421→3167 (ΔOI +1746张) | ΔOI/Volume 64.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1746张（+122.9% vs前日OI），连续性待观察（方向未知）
11-27 92.5C — Vol 4,525 | 最新价 $2.55 | OI 3612→5337 (ΔOI +1725张) | ΔOI/Volume 38.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1725张（+47.8% vs前日OI），连续性待观察（方向未知）
12-04 100.0C — Vol 4,251 | 最新价 $2.90 | OI 2784→4426 (ΔOI +1642张) | ΔOI/Volume 38.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1642张（+59.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,941 张（Put 0 / Call 9,941），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +12.7k / P +12.1k ｜ Activity HIGH ｜ 3D
12-04  C +0.4k / P +1.3k ｜ Activity HIGH ｜ 10D
12-11  C +1.2k / P +0.5k ｜ Activity HIGH ｜ 17D
12-18  C +4.3k / P -19.8k ｜ Activity HIGH ｜ 24D

📆 11-27 Forward Structure
存量OI: C 297.4k / P 131.6k，今日变化ΔOI: C +12.7k / P +12.1k，平值价格ATM: C $3.80 / P $3.90 ｜ ATM IV 132.7%，净 delta 敞口 -465k shares
Top ΔOI: P 100 -1,971
仓位参考: Max Pain 98 ｜ Put Wall 87.5（+9.5%，弱）（OI 5.2k）
量化解读： 存量 Call 重｜ATM IV 132.7%｜历史 Rank 84%（近端代理）｜IV/RV 0.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 464,974 股

📆 12-04 Forward Structure
存量OI: C 123.9k / P 65.9k，今日变化ΔOI: C +0.4k / P +1.3k，平值价格ATM: C $6.80 / P $6.75 ｜ ATM IV 126.4%，净 delta 敞口 -87k shares
Top ΔOI: C 100 +1,642 ｜ C 85 -1,524 ｜ C 95 -1,446
仓位参考: Max Pain 102 ｜ Call Wall 85（+6.4%，弱）（OI 1.8k） ｜ Put Wall 87.5（+9.5%，弱）（OI 3.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 126.4%｜历史 Rank 84%（近端代理）｜IV/RV 0.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 86,520 股

📆 12-11 Forward Structure
存量OI: C 59.9k / P 44.3k，今日变化ΔOI: C +1.2k / P +0.5k，平值价格ATM: C $8.50 / P $8.10 ｜ ATM IV 121.0%，净 delta 敞口 -3k shares
Top ΔOI: P 82 +293 ｜ C 95 +190
仓位参考: Max Pain 105 ｜ Call Wall 80（+0.1%，弱）（OI 2.0k） ｜ Put Wall 80（+0.1%）（OI 10.6k）
量化解读： 存量 Call 重｜ATM IV 121.0%｜历史 Rank 84%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,310 股

📆 12-18 Forward Structure
存量OI: C 564.8k / P 532.5k，今日变化ΔOI: C +4.3k / P -19.8k，平值价格ATM: C $9.50 / P $9.43 ｜ ATM IV 117.1%，净 delta 敞口 872k shares
Top ΔOI: P 75 -25,030 ｜ C 95 +2,343 ｜ P 80 +1,312
仓位参考: Max Pain 116 ｜ Put Wall 75（-6.1%，弱）（OI 44.0k）
量化解读： 存量两侧均衡｜ATM IV 117.1%｜历史 Rank 84%（近端代理）｜IV/RV 0.15×（近似）｜净 delta 敞口 正 871,532 股

📅 事件差分（观察，非因果）: 11-27（3D）ATM IV 132.7% vs 12-04 126.4%（差 +6.2pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/SNDK_morning.json