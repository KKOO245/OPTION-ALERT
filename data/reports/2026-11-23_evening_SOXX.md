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
🟡 **近现价集中开仓**: 11-27 135C ΔOI +9,339（距现价 -3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 130C ΔOI +10,640 占该期限总 OI 10.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 142.18 → 收盘 140.22（-1.4%） ｜ 今日高 142.26 ｜ 低 136.64 ｜ 昨收 123.40 → 收盘 140.22（+13.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-30，窗口结束前不做对错判定）

Options: P/C成交量 0.28 | OI比 0.54 | ATM IV 79.8% | Skew 16.3pp | Term 0.79 | ExpMove ±5.8%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价显著（Skew 16.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±5.8% ｜ 12-04（11D）±9.8% ｜ 12-11（18D）±11.7% ｜ 12-18（25D）±13.5%
   ⇒ IV–VIX Spread: +53.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -476,391 | GEX Change vs 上次快照 405,685 | Flip: Primary Flip: 140.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 592 / LOW 274 / INVALID 626
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 140.51（全链重定价，覆盖 100%）
最近结构参考: Flip 141（现价低于该位 0.2%）
量化视角： 负 Gamma（48万，无历史分位）｜负 Gamma 缓解（+41万）｜现价位于 Flip 下方 0.20%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 141（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 125.0P — Vol 15,684 | 最新价 $4.20 | OI 2699→30975 (ΔOI +28276张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28276张（+1047.7% vs前日OI），连续性待观察（方向未知）
11-27 130.0C — Vol 11,379 | 最新价 $11.50 | OI 33→10673 (ΔOI +10640张) | ΔOI/Volume 93.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10640张（+32242.4% vs前日OI），连续性待观察（方向未知）
11-27 135.0C — Vol 9,596 | 最新价 $7.40 | OI 13→9352 (ΔOI +9339张) | ΔOI/Volume 97.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9339张（+71838.5% vs前日OI），连续性待观察（方向未知）
11-27 130.0P — Vol 4,902 | 最新价 $1.20 | OI 2471→5711 (ΔOI +3240张) | ΔOI/Volume 66.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3240张（+131.1% vs前日OI），连续性待观察（方向未知）
12-18 126.67P — Vol 37 | 最新价 $4.59 | OI 1140→4352 (ΔOI +3212张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3212张（+281.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 54,707 张（Put 34,728 / Call 19,979），跨 2 个期限｜有实质成本保护 3 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +22.8k / P +10.3k ｜ Activity HIGH ｜ 4D
12-04  C +1.5k / P +4.7k ｜ Activity HIGH ｜ 11D
12-11  C +0.2k / P +0.6k ｜ Activity HIGH ｜ 18D
12-18  C +6.7k / P +28.2k ｜ Activity HIGH ｜ 25D

📆 11-27 Forward Structure
存量OI: C 66.9k / P 35.9k，今日变化ΔOI: C +22.8k / P +10.3k，平值价格ATM: C $4.15 / P $3.95 ｜ ATM IV 79.8%，净 delta 敞口 1.6M shares
Top ΔOI: C 130 +10,640 ｜ C 135 +9,339 ｜ P 130 +3,240
仓位参考: Max Pain 135 ｜ Call Wall 135（-3.7%，弱）（OI 9.4k） ｜ Put Wall 146.67（+4.6%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 79.8%｜历史 Rank 98%（近端代理）｜IV/RV 0.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,560,731 股

📆 12-04 Forward Structure
存量OI: C 13.9k / P 28.6k，今日变化ΔOI: C +1.5k / P +4.7k，平值价格ATM: C $6.60 / P $7.12 ｜ ATM IV 70.7%，净 delta 敞口 1k shares
Top ΔOI: P 120 +1,688 ｜ P 125 +868 ｜ P 110 +834
仓位参考: Max Pain 150 ｜ Call Wall 145（+3.4%，弱）（OI 1.5k） ｜ Put Wall 140（-0.2%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 70.7%｜历史 Rank 98%（近端代理）｜IV/RV 0.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,385 股

📆 12-11 Forward Structure
存量OI: C 4.2k / P 4.5k，今日变化ΔOI: C +0.2k / P +0.6k，平值价格ATM: C $8.30 / P $8.08 ｜ ATM IV 65.7%，净 delta 敞口 5k shares
仓位参考: Max Pain 145 ｜ Call Wall 145（+3.4%，弱）（OI 0.2k） ｜ Put Wall 140（-0.2%）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 65.7%｜历史 Rank 98%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,524 股

📆 12-18 Forward Structure
存量OI: C 249.3k / P 198.0k，今日变化ΔOI: C +6.7k / P +28.2k，平值价格ATM: C $9.50 / P $9.45 ｜ ATM IV 64.4%，净 delta 敞口 188k shares
Top ΔOI: P 125 +28,276 ｜ P 150 -8,622 ｜ P 126 +3,212
仓位参考: Max Pain 155 ｜ Put Wall 140（-0.2%，弱）（OI 11.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 64.4%｜历史 Rank 98%（近端代理）｜IV/RV 0.15×（近似）｜净 delta 敞口 正 187,639 股

📅 事件差分（观察，非因果）: 11-27（4D）ATM IV 79.8% vs 12-04 70.7%（差 +9.1pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/SOXX_evening.json