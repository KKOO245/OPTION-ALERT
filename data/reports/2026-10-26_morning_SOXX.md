# 期权晨报 2026-10-26（快照 09:08 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 19.22 ↓1.2%（5D +4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 500C ΔOI +846（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 345P ΔOI +25,000 占该期限总 OI 12.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 478.20 → 今开 474.74（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 485.04 ｜ 低 473.10

Options: P/C成交量 8.47 | OI比 6.39 | ATM IV 48.8% | Skew 10.4pp | Term 0.88 | ExpMove ±5.3%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价显著（Skew 10.4pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 8.47）——观察点，非方向信号
   ⇒ Put/Call Volume: 8.47×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 6.39×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（4D）±5.3% ｜ 11-06（11D）±7.3% ｜ 11-13（18D）±8.8% ｜ 11-20（25D）±9.8%
   ⇒ IV–VIX Spread: +29.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -32,981,613 | GEX Change vs 上次快照 1,326,124 | Flip: Primary Flip: 526.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 598 / LOW 233 / INVALID 725
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 526.81（全链重定价，覆盖 100%）
最近结构参考: Flip 527（现价低于该位 7.7%）
量化视角： 负 Gamma（3298万，无历史分位）｜负 Gamma 缓解（+133万）｜现价位于 Flip 下方 7.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 520（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 527（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 345.0P — Vol 25,030 | 最新价 $0.15 | OI 147→25147 (ΔOI +25000张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25000张（+17006.8% vs前日OI），连续性待观察（方向未知）
11-20 530.0C — Vol 2,708 | 最新价 $6.48 | OI 487→3051 (ΔOI +2564张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2564张（+526.5% vs前日OI），连续性待观察（方向未知）
11-20 505.0C — Vol 2,148 | 最新价 $12.80 | OI 478→2596 (ΔOI +2118张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2118张（+443.1% vs前日OI），连续性待观察（方向未知）
11-20 430.0P — Vol 2,149 | 最新价 $8.09 | OI 1768→3872 (ΔOI +2104张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2104张（+119.0% vs前日OI），连续性待观察（方向未知）
10-30 500.0C — Vol 1,068 | 最新价 $4.36 | OI 2897→3743 (ΔOI +846张) | ΔOI/Volume 79.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增846张（+29.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 32,632 张（Put 27,104 / Call 5,528），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C -1.7k / P +26.9k ｜ Activity HIGH ｜ 4D
11-06  C +0.8k / P +0.1k ｜ Activity HIGH ｜ 11D
11-13  C +0.7k / P +0.8k ｜ Activity HIGH ｜ 18D
11-20  C +4.9k / P +1.2k ｜ Activity HIGH ｜ 25D

📆 10-30 Forward Structure
存量OI: C 27.3k / P 174.2k，今日变化ΔOI: C -1.7k / P +26.9k，平值价格ATM: C $10.00 / P $16.00 ｜ ATM IV 48.8%，净 delta 敞口 -27k shares
Top ΔOI: P 345 +25,000 ｜ C 525 -3,864 ｜ C 500 +846
仓位参考: Max Pain 520 ｜ Call Wall 500（+2.9%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜ATM IV 48.8%｜历史 Rank 85%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 27,052 股

📆 11-06 Forward Structure
存量OI: C 6.5k / P 6.9k，今日变化ΔOI: C +0.8k / P +0.1k，平值价格ATM: C $15.11 / P $20.35 ｜ ATM IV 47.5%，净 delta 敞口 10k shares
Top ΔOI: C 515 +150 ｜ C 520 +148
仓位参考: Max Pain 515 ｜ Put Wall 455（-6.4%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.5%｜历史 Rank 85%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 10,250 股

📆 11-13 Forward Structure
存量OI: C 15.0k / P 6.8k，今日变化ΔOI: C +0.7k / P +0.8k，平值价格ATM: C $18.25 / P $24.30 ｜ ATM IV 45.5%，净 delta 敞口 -19k shares
Top ΔOI: C 480 +395 ｜ P 485 +388 ｜ P 495 +292
仓位参考: Max Pain 515 ｜ Put Wall 460（-5.3%）（OI 3.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 45.5%｜历史 Rank 85%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 19,185 股

📆 11-20 Forward Structure
存量OI: C 34.0k / P 58.8k，今日变化ΔOI: C +4.9k / P +1.2k，平值价格ATM: C $21.60 / P $26.14 ｜ ATM IV 44.8%，净 delta 敞口 168k shares
Top ΔOI: C 530 +2,564 ｜ C 505 +2,118 ｜ P 430 +2,104
仓位参考: Max Pain 535 ｜ Call Wall 505（+3.9%，弱）（OI 2.6k） ｜ Put Wall 460（-5.3%，弱）（OI 7.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.8%｜历史 Rank 85%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 正 168,121 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/SOXX_morning.json