# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $766.09 ｜ QQQ $715.15
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.3（fear）
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
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 144P ΔOI +177（距现价 -4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 150.47 → 今开 150.35（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 151.61 ｜ 低 149.37

Options: P/C成交量 0.78 | OI比 5.43 | ATM IV 44.6% | Skew 1.9pp | Term 0.73 | ExpMove ±3.4%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价薄（Skew 1.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 5.43×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±3.4% ｜ 11-06（10D）±4.4% ｜ 11-13（17D）±5.9% ｜ 11-20（24D）±7.6%
   ⇒ IV–VIX Spread: +26.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -24,931,389 | GEX Change vs 上次快照 -2,646,068 | Flip: Primary Flip: 158.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 340 / LOW 80 / INVALID 350
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 158.25（全链重定价，覆盖 93%）
最近结构参考: Flip 158（现价低于该位 5.0%）
量化视角： 负 Gamma（2493万，无历史分位）｜负 Gamma 加深（265万）｜现价位于 Flip 下方 4.98%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 158（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 145.0P — Vol 2,017 | 最新价 $2.97 | OI 7406→9279 (ΔOI +1873张) | ΔOI/Volume 92.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1873张（+25.3% vs前日OI），连续性待观察（方向未知）
11-20 133.0P — Vol 2,004 | 最新价 $0.62 | OI 6481→7859 (ΔOI +1378张) | ΔOI/Volume 68.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1378张（+21.3% vs前日OI），连续性待观察（方向未知）
11-06 145.0P — Vol 208 | 最新价 $1.70 | OI 637→835 (ΔOI +198张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增198张（+31.1% vs前日OI），连续性待观察（方向未知）
10-30 144.0P — Vol 178 | 最新价 $0.52 | OI 111→288 (ΔOI +177张) | ΔOI/Volume 99.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增177张（+159.5% vs前日OI），连续性待观察（方向未知）
11-27 135.0P — Vol 139 | 最新价 $1.05 | OI 8→147 (ΔOI +139张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增139张（+1737.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,765 张（Put 3,765 / Call 0），跨 4 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.3k / P -0.3k ｜ Activity LOW ｜ 3D
11-06  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 10D
11-13  C -2 / P +64 ｜ Activity LOW ｜ 17D
11-20  C +0.1k / P +3.4k ｜ Activity HIGH ｜ 24D

📆 10-30 Forward Structure
存量OI: C 10.0k / P 54.4k，今日变化ΔOI: C +0.3k / P -0.3k，平值价格ATM: C $2.61 / P $2.55 ｜ ATM IV 44.6%，净 delta 敞口 15k shares
Top ΔOI: P 142 -493 ｜ P 150 -206 ｜ P 144 +177
仓位参考: Max Pain 150 ｜ Call Wall 155（+3.1%，弱）（OI 2.1k） ｜ Put Wall 150（-0.2%，弱）（OI 9.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.6%｜历史 Rank 93%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 15,081 股

11-06（MEDIUM △）Top ΔOI: 145P +198 ｜ 147P +122
11-06（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 154（+2.4%，弱）（OI 0.2k） ｜ Put Wall 145（-3.6%）（OI 0.8k）

11-13（Activity LOW）仓位参考: Max Pain 153 ｜ Call Wall 160（+6.4%）（OI 0.4k） ｜ Put Wall 153（+1.7%，弱）（OI 0.4k）

📆 11-20 Forward Structure
存量OI: C 19.8k / P 37.5k，今日变化ΔOI: C +0.1k / P +3.4k，平值价格ATM: C $6.00 / P $5.45 ｜ ATM IV 35.2%，净 delta 敞口 -74k shares
Top ΔOI: P 145 +1,873 ｜ P 133 +1,378 ｜ P 159 +110
仓位参考: Max Pain 154 ｜ Call Wall 160（+6.4%，弱）（OI 1.9k） ｜ Put Wall 145（-3.6%，弱）（OI 9.3k）
量化解读： 存量 Put 重｜ATM IV 35.2%｜历史 Rank 93%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 负 73,663 股

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 44.6% vs 11-06 36.9%（差 +7.7pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/XBI_morning.json