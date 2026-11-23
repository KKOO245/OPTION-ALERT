# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.39 ｜ QQQ $651.03
VIX 27.37 ↓23.7%（5D +19.5%） ｜ Vol Regime: STRESS
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-27 109C ΔOI +4,357（距现价 +0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-11 65P ΔOI +1,027 占该期限总 OI 12.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 101.97 → 今开 109.56（+7.4%） | 较昨收变动（含盘初走势） ｜ 今日高 111.21 ｜ 低 107.20

Options: P/C成交量 0.36 | OI比 0.57 | ATM IV 90.4% | Skew 11.5pp | Term 0.85 | ExpMove ±7.4%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价显著（Skew 11.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.57）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±7.4% ｜ 12-04（11D）±11.4% ｜ 12-11（18D）±0.0% ｜ 12-18（25D）±7.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,878,199 | GEX Change vs 上次快照 7,729,363 | Flip: Primary Flip: 103.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 428 / LOW 201 / INVALID 359
结构观察区: Primary Flip 103.16（全链重定价，覆盖 100%）
Put Wall 110（弱结构｜现价低于该位 1.0%）
最近结构参考: Put Wall 110（现价低于该位 1.0%）
量化视角： 正 Gamma（788万，无历史分位）｜正 Gamma 增强（+773万）｜现价位于 Flip 上方 5.61%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 110（Put Wall，弱结构） / 110（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 103（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 109.0C — Vol 4,494 | 最新价 $2.20 | OI 6→4363 (ΔOI +4357张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4357张（+72616.7% vs前日OI），连续性待观察（方向未知）
11-27 114.0C — Vol 5,259 | 最新价 $1.20 | OI 3705→7109 (ΔOI +3404张) | ΔOI/Volume 64.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3404张（+91.9% vs前日OI），连续性待观察（方向未知）
11-27 110.0C — Vol 2,711 | 最新价 $1.84 | OI 253→2600 (ΔOI +2347张) | ΔOI/Volume 86.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2347张（+927.7% vs前日OI），连续性待观察（方向未知）
11-27 100.0P — Vol 4,748 | 最新价 $4.30 | OI 1309→2817 (ΔOI +1508张) | ΔOI/Volume 31.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1508张（+115.2% vs前日OI），连续性待观察（方向未知）
11-27 95.0P — Vol 1,487 | 最新价 $2.53 | OI 196→1518 (ΔOI +1322张) | ΔOI/Volume 88.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1322张（+674.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,938 张（Put 2,830 / Call 10,108），跨 1 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +16.4k / P +11.5k ｜ Activity HIGH ｜ 4D
12-04  C +0.6k / P +1.4k ｜ Activity HIGH ｜ 11D
12-11  C +0.4k / P +1.2k ｜ Activity HIGH ｜ 18D
12-18  C +3.6k / P -0.5k ｜ Activity HIGH ｜ 25D

📆 11-27 Forward Structure
存量OI: C 57.1k / P 32.3k，今日变化ΔOI: C +16.4k / P +11.5k，平值价格ATM: C $4.05 / P $4.00 ｜ ATM IV 90.4%，净 delta 敞口 503k shares
Top ΔOI: C 109 +4,357 ｜ C 114 +3,404 ｜ C 110 +2,347
仓位参考: Max Pain 110 ｜ Call Wall 114（+4.6%，弱）（OI 7.1k） ｜ Put Wall 100（-8.2%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 90.4%｜历史 Rank 80%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 502,963 股

📆 12-04 Forward Structure
存量OI: C 10.5k / P 13.7k，今日变化ΔOI: C +0.6k / P +1.4k，平值价格ATM: C $6.05 / P $6.35 ｜ ATM IV 82.8%，净 delta 敞口 8k shares
Top ΔOI: P 102 +122
仓位参考: Max Pain 133 ｜ Put Wall 100（-8.2%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 82.8%｜历史 Rank 80%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,019 股

📆 12-11 Forward Structure
存量OI: C 3.6k / P 4.9k，今日变化ΔOI: C +0.4k / P +1.2k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 82.2%，净 delta 敞口 11k shares
Top ΔOI: P 65 +1,027 ｜ C 110 +115
仓位参考: Max Pain 130 ｜ Call Wall 110（+1.0%，弱）（OI 0.2k） ｜ Put Wall 100（-8.2%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 82.2%｜历史 Rank 80%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,470 股

📆 12-18 Forward Structure
存量OI: C 138.8k / P 54.3k，今日变化ΔOI: C +3.6k / P -0.5k，平值价格ATM: C $8.52 / P $0.00 ｜ ATM IV 80.7%，净 delta 敞口 76k shares
Top ΔOI: P 80 -798
仓位参考: Max Pain 135 ｜ Put Wall 110（+1.0%）（OI 7.9k）
量化解读： 存量 Call 重｜ATM IV 80.7%｜历史 Rank 80%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 正 75,938 股

📅 事件差分（观察，非因果）: 11-27（4D）ATM IV 90.4% vs 12-04 82.8%（差 +7.6pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/COIN_morning.json