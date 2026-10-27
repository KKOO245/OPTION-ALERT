# 期权晚报 2026-10-27（快照 16:40 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $721.25
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.7（fear）
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

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 500C ΔOI +968（距现价 -2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 510C ΔOI +9,615 占该期限总 OI 30.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 500.24 → 收盘 511.06（+2.2%） ｜ 今日高 513.16 ｜ 低 498.41 ｜ 昨收 491.83 → 收盘 511.06（+3.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-03，窗口结束前不做对错判定）

Options: P/C成交量 1.32 | OI比 5.97 | ATM IV 50.9% | Skew 1.2pp | Term 0.81 | ExpMove ±3.9%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜当日成交偏 Put（P/C量 1.32）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.32×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 5.97×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±3.9% ｜ 11-06（10D）±5.9% ｜ 11-13（17D）±7.5% ｜ 11-20（24D）±8.7%
   ⇒ IV–VIX Spread: +33.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,917,676 | GEX Change vs 上次快照 10,065,764 | Flip: Primary Flip: 518.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 501 / LOW 334 / INVALID 757
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 518.62（全链重定价，覆盖 92%）
Call Wall 510（现价高于该位 0.2%）
最近结构参考: Call Wall 510（现价高于该位 0.2%）
量化视角： 负 Gamma（692万，无历史分位）｜负 Gamma 缓解（+1007万）｜现价位于 Flip 下方 1.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 508（MaxPain，仅结算参考） / 510（Call Wall）。
• Gamma 区域：切换参考 519（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 345.0P — Vol 25,030（Yahoo补） | 最新价 $0.15 | OI 147→25147 (ΔOI +25000张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25000张（+17006.8% vs前日OI），连续性待观察（方向未知）
11-20 530.0C — Vol 22 | 最新价 $9.20 | OI 487→3051 (ΔOI +2564张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2564张（+526.5% vs前日OI），连续性待观察（方向未知）
11-20 505.0C — Vol 183 | 最新价 $18.20 | OI 478→2596 (ΔOI +2118张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2118张（+443.1% vs前日OI），连续性待观察（方向未知）
11-20 430.0P — Vol 421 | 最新价 $4.36 | OI 1768→3872 (ΔOI +2104张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2104张（+119.0% vs前日OI），连续性待观察（方向未知）
10-30 500.0C — Vol 1,427 | 最新价 $6.93 | OI 2897→3743 (ΔOI +846张) | ΔOI/Volume 59.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增846张（+29.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 32,632 张（Put 27,104 / Call 5,528），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +1.9k / P +37 ｜ Activity HIGH ｜ 3D
11-06  C +1.2k / P +0.7k ｜ Activity HIGH ｜ 10D
11-13  C +9.4k / P +0.1k ｜ Activity HIGH ｜ 17D
11-20  C +1.9k / P +5.8k ｜ Activity HIGH ｜ 24D

📆 10-30 Forward Structure
存量OI: C 29.2k / P 174.2k，今日变化ΔOI: C +1.9k / P +37，平值价格ATM: C $11.88 / P $7.90 ｜ ATM IV 50.9%，净 delta 敞口 156k shares
Top ΔOI: C 500 +968 ｜ C 490 +194 ｜ C 480 +193
仓位参考: Max Pain 508 ｜ Call Wall 500（-2.2%）（OI 4.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.9%｜历史 Rank 86%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 156,073 股

📆 11-06 Forward Structure
存量OI: C 7.7k / P 7.6k，今日变化ΔOI: C +1.2k / P +0.7k，平值价格ATM: C $15.45 / P $14.50 ｜ ATM IV 42.9%，净 delta 敞口 57k shares
Top ΔOI: C 505 +1,065 ｜ P 465 +401 ｜ P 485 +130
仓位参考: Max Pain 505 ｜ Call Wall 505（-1.2%，弱）（OI 1.2k） ｜ Put Wall 495（-3.1%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 42.9%｜历史 Rank 86%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 57,008 股

📆 11-13 Forward Structure
存量OI: C 24.4k / P 6.9k，今日变化ΔOI: C +9.4k / P +0.1k，平值价格ATM: C $19.90 / P $18.69 ｜ ATM IV 43.4%，净 delta 敞口 363k shares
Top ΔOI: C 510 +9,615 ｜ C 520 -3,723 ｜ C 560 +3,196
仓位参考: Max Pain 510 ｜ Call Wall 510（-0.2%，弱）（OI 9.6k）
量化解读： 存量 Call 重｜ATM IV 43.4%｜历史 Rank 86%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 363,341 股

📆 11-20 Forward Structure
存量OI: C 35.9k / P 64.5k，今日变化ΔOI: C +1.9k / P +5.8k，平值价格ATM: C $23.23 / P $21.28 ｜ ATM IV 41.4%，净 delta 敞口 -1k shares
Top ΔOI: P 455 +4,715 ｜ C 500 +1,059 ｜ C 517 +420
仓位参考: Max Pain 530 ｜ Call Wall 530（+3.7%，弱）（OI 3.1k） ｜ Put Wall 490（-4.1%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 41.4%｜历史 Rank 86%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 负 1,452 股

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 50.9% vs 11-06 42.9%（差 +8.1pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/SOXX_evening.json