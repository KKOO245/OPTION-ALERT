# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $766.09 ｜ QQQ $715.17
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
🔴 **事件差分**: 10-30（3D）ATM IV 126.7% vs 11-06 94.2%（差 +32.5pp），覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,255.58 → 今开 1,267.08（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 1305.00 ｜ 低 1259.00

Options: P/C成交量 0.50 | OI比 0.78 | ATM IV 126.7% | Skew 4.3pp | Term 0.60 | ExpMove ±9.6%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价中性（Skew 4.3pp）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±9.6% ｜ 11-06（10D）±12.6% ｜ 11-13（17D）±16.5% ｜ 11-20（24D）±16.6%
   ⇒ IV–VIX Spread: +108.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,029,621 | GEX Change vs 上次快照 2,871,715 | Flip: Primary Flip: 1324.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1878 / LOW 429 / INVALID 1087
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1324.40（全链重定价，覆盖 100%）
最近结构参考: Flip 1324（现价低于该位 2.0%）
量化视角： 负 Gamma（103万，无历史分位）｜负 Gamma 缓解（+287万）｜现价位于 Flip 下方 1.99%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,370（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1324（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 1400.0C — Vol 1,869 | 最新价 $53.40 | OI 355→1696 (ΔOI +1341张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1341张（+377.8% vs前日OI），连续性待观察（方向未知）
10-30 1500.0C — Vol 4,755 | 最新价 $4.95 | OI 1638→2476 (ΔOI +838张) | ΔOI/Volume 17.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增838张（+51.2% vs前日OI），连续性待观察（方向未知）
10-30 1800.0C — Vol 854 | 最新价 $0.27 | OI 1299→1926 (ΔOI +627张) | ΔOI/Volume 73.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增627张（+48.3% vs前日OI），连续性待观察（方向未知）
10-30 630.0P — Vol 569 | 最新价 $0.10 | OI 69→619 (ΔOI +550张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增550张（+797.1% vs前日OI），连续性待观察（方向未知）
11-20 1500.0C — Vol 916 | 最新价 $31.02 | OI 2136→2632 (ΔOI +496张) | ΔOI/Volume 54.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增496张（+23.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,852 张（Put 550 / Call 3,302），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +7.9k / P +4.9k ｜ Activity HIGH ｜ 3D
11-06  C +1.2k / P +1.6k ｜ Activity MEDIUM △ ｜ 10D
11-13  C +0.5k / P +0.4k ｜ Activity MEDIUM △ ｜ 17D
11-20  C +2.8k / P +0.9k ｜ Activity MEDIUM △ ｜ 24D

📆 10-30 Forward Structure
存量OI: C 44.7k / P 34.7k，今日变化ΔOI: C +7.9k / P +4.9k，平值价格ATM: C $60.00 / P $64.62 ｜ ATM IV 126.7%，净 delta 敞口 206k shares
Top ΔOI: C 1500 +838
仓位参考: Max Pain 1,370 ｜ Call Wall 1400（+7.9%，弱）（OI 1.6k） ｜ Put Wall 1200（-7.6%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 126.7%｜历史 Rank 84%（近端代理）｜IV/RV 2.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 205,739 股

11-06（MEDIUM △）Top ΔOI: 730P +324 ｜ 1000P +233
11-06（MEDIUM △）仓位参考: Max Pain 1,400 ｜ Call Wall 1400（+7.9%，弱）（OI 0.8k） ｜ Put Wall 1200（-7.6%，弱）（OI 0.8k）

11-13（MEDIUM △）Top ΔOI: 1700C +82 ｜ 1300P +53
11-13（MEDIUM △）仓位参考: Max Pain 1,495 ｜ Call Wall 1420（+9.4%，弱）（OI 0.2k） ｜ Put Wall 1300（+0.2%，弱）（OI 0.2k）

11-20（MEDIUM △）Top ΔOI: 1400C +1,341 ｜ 1500C +496
11-20（MEDIUM △）仓位参考: Max Pain 1,490 ｜ Call Wall 1400（+7.9%，弱）（OI 1.7k） ｜ Put Wall 1200（-7.6%，弱）（OI 1.5k）

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 126.7% vs 11-06 94.2%（差 +32.5pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/SNDK_morning.json