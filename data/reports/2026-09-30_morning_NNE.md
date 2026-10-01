# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $nan
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 10-02（2D）ATM IV 86.0% vs 10-09 68.9%（差 +17.1pp），覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-02 17C ΔOI +197（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 15.79 → 今开 16.00（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 16.55 ｜ 低 15.85

Options: P/C成交量 0.53 | OI比 0.42 | ATM IV 86.0% | Skew -0.1pp | Term 0.88 | ExpMove ±7.6%（近端） | Rank 15%
量化视角： IV 历史低位（Rank 15%，期权偏便宜）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±7.6% ｜ 10-09（9D）±10.5% ｜ 10-16（16D）±11.4% ｜ 10-23（23D）±17.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,474,993 | GEX Change vs 上次快照 1,285,407 | Flip: Primary Flip: 15.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 210 / LOW 86 / INVALID 140
结构观察区: Primary Flip 15.55（全链重定价，覆盖 94%）
Put Wall 15（弱结构｜现价高于该位 10.0%）
最近结构参考: Flip 16（现价高于该位 6.1%）
量化视角： 正 Gamma（147万，无历史分位）｜正 Gamma 增强（+129万）｜现价位于 Flip 上方 6.12%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 17.0C — Vol 203 | 最新价 $0.10 | OI 250→447 (ΔOI +197张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增197张（+78.8% vs前日OI），连续性待观察（方向未知）
10-02 17.5C — Vol 114 | 最新价 $0.08 | OI 275→381 (ΔOI +106张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增106张（+38.5% vs前日OI），连续性待观察（方向未知）
10-09 15.0P — Vol 69 | 最新价 $0.40 | OI 326→395 (ΔOI +69张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增69张（+21.2% vs前日OI），连续性待观察（方向未知）
10-09 15.5P — Vol 70 | 最新价 $0.65 | OI 87→148 (ΔOI +61张) | ΔOI/Volume 87.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增61张（+70.1% vs前日OI），连续性待观察（方向未知）
10-23 18.0C — Vol 83 | 最新价 $0.55 | OI 76→130 (ΔOI +54张) | ΔOI/Volume 65.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54张（+71.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 487 张（Put 130 / Call 357），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.4k / P -26 ｜ Activity HIGH ｜ 2D
10-09  C +40 / P +0.2k ｜ Activity HIGH ｜ 9D
10-16  C +88 / P -67 ｜ Activity MEDIUM △ ｜ 16D
10-23  C +44 / P +5 ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 5.5k / P 2.3k，今日变化ΔOI: C +0.4k / P -26，平值价格ATM: C $0.25 / P $1.00 ｜ ATM IV 86.0%，净 delta 敞口 14k shares
Top ΔOI: C 17 +197 ｜ C 17 +106 ｜ C 16 +47
仓位参考: Max Pain 17 ｜ Call Wall 18（+9.1%，弱）（OI 0.7k） ｜ Put Wall 15.5（-6.1%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 86.0%｜历史 Rank 15%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 13,746 股

📆 10-09 Forward Structure
存量OI: C 5.1k / P 1.5k，今日变化ΔOI: C +40 / P +0.2k，平值价格ATM: C $0.65 / P $1.09 ｜ ATM IV 68.9%，净 delta 敞口 -5k shares
Top ΔOI: P 15 +69 ｜ P 15 +61
仓位参考: Max Pain 18 ｜ Put Wall 15（-9.1%）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 68.9%｜历史 Rank 15%（近端代理）｜IV/RV 0.94×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 5,022 股

10-16（MEDIUM △）Top ΔOI: 26P -63 ｜ 16C +40
10-16（MEDIUM △）仓位参考: Max Pain 20 ｜ Put Wall 15（-9.1%，弱）（OI 0.8k）

10-23（MEDIUM △）Top ΔOI: 18C +54 ｜ 17C +10
10-23（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（-3.0%）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 86.0% vs 10-09 68.9%（差 +17.1pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/NNE_morning.json