# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $766.09 ｜ QQQ $715.30
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
🔴 **事件差分**: 10-30（3D）ATM IV 96.0% vs 11-06 80.9%（差 +15.2pp），覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 145C ΔOI +1,736（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 139.82 → 今开 139.93（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 142.00 ｜ 低 138.69

Options: P/C成交量 0.54 | OI比 0.78 | ATM IV 96.0% | Skew 0.9pp | Term 0.74 | ExpMove ±7.4%（近端） | Rank 76%
量化视角： IV 历史高位（Rank 76%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价薄（Skew 0.9pp）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±7.4% ｜ 11-06（10D）±10.9% ｜ 11-13（17D）±12.9% ｜ 11-20（24D）±15.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,497,582 | GEX Change vs 上次快照 902,684 | Flip: Primary Flip: 134.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 584 / LOW 87 / INVALID 245
结构观察区: Primary Flip 134.38（全链重定价，覆盖 100%）
Call Wall 135（弱结构｜现价高于该位 3.4%）
最近结构参考: Call Wall 135（现价高于该位 3.4%）
量化视角： 正 Gamma（1950万，无历史分位）｜正 Gamma 增强（+90万）｜现价位于 Flip 上方 3.86%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Call Wall，弱结构）；上方 144（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 134（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 145.0C — Vol 6,313 | 最新价 $3.25 | OI 1095→2831 (ΔOI +1736张) | ΔOI/Volume 27.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1736张（+158.5% vs前日OI），连续性待观察（方向未知）
10-30 110.0P — Vol 3,747 | 最新价 $0.20 | OI 5722→7261 (ΔOI +1539张) | ΔOI/Volume 41.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1539张（+26.9% vs前日OI），连续性待观察（方向未知）
10-30 130.0P — Vol 5,278 | 最新价 $1.71 | OI 2952→4423 (ΔOI +1471张) | ΔOI/Volume 27.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1471张（+49.8% vs前日OI），连续性待观察（方向未知）
10-30 100.0P — Vol 3,567 | 最新价 $0.11 | OI 6116→7554 (ΔOI +1438张) | ΔOI/Volume 40.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1438张（+23.5% vs前日OI），连续性待观察（方向未知）
10-30 138.0C — Vol 2,017 | 最新价 $6.37 | OI 117→1465 (ΔOI +1348张) | ΔOI/Volume 66.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1348张（+1152.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,532 张（Put 4,448 / Call 3,084），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +11.3k / P +6.4k ｜ Activity HIGH ｜ 3D
11-06  C +2.3k / P +4.5k ｜ Activity MEDIUM △ ｜ 10D
11-13  C +2.0k / P +2.6k ｜ Activity MEDIUM △ ｜ 17D
11-20  C +1.1k / P +2.6k ｜ Activity HIGH ｜ 24D

📆 10-30 Forward Structure
存量OI: C 220.7k / P 173.2k，今日变化ΔOI: C +11.3k / P +6.4k，平值价格ATM: C $5.04 / P $5.25 ｜ ATM IV 96.0%，净 delta 敞口 425k shares
Top ΔOI: P 120 -2,795 ｜ C 145 +1,736
仓位参考: Max Pain 144 ｜ Call Wall 152.5（+9.3%，弱）（OI 38.6k）
量化解读： 存量 Call 重｜ATM IV 96.0%｜历史 Rank 76%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 425,217 股

11-06（MEDIUM △）Top ΔOI: 115P +583
11-06（MEDIUM △）仓位参考: Max Pain 158 ｜ Call Wall 150（+7.5%，弱）（OI 1.3k） ｜ Put Wall 150（+7.5%，弱）（OI 2.3k）

11-13（MEDIUM △）仓位参考: Max Pain 160 ｜ Put Wall 150（+7.5%，弱）（OI 1.9k）

📆 11-20 Forward Structure
存量OI: C 145.9k / P 108.6k，今日变化ΔOI: C +1.1k / P +2.6k，平值价格ATM: C $10.50 / P $10.95 ｜ ATM IV 74.4%，净 delta 敞口 20k shares
仓位参考: Max Pain 135 ｜ Call Wall 135（-3.3%）（OI 42.4k） ｜ Put Wall 130（-6.9%，弱）（OI 4.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.4%｜历史 Rank 76%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 20,362 股

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 96.0% vs 11-06 80.9%（差 +15.2pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/MSTR_morning.json