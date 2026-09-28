# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $767.62 ｜ QQQ $737.24
VIX 15.89 ↑6.9%（5D +6.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.24 ｜ 实际 待公布 ｜ 前值 7.271
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 54.9 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 84 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 10-02 280P ΔOI +1,155（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 288.70 → 今开 282.51（-2.1%） | 较昨收变动（含盘初走势） ｜ 今日高 286.26 ｜ 低 265.65

Options: P/C成交量 0.81 | OI比 0.98 | ATM IV 86.6% | Skew -3.0pp | Term 0.98 | ExpMove ±7.5%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -3.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（4D）±7.5% ｜ 10-09（11D）±11.0% ｜ 10-16（18D）±14.0% ｜ 10-23（25D）±16.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,046,534 | GEX Change vs 上次快照 -4,965,460 | Flip: Primary Flip: 257.54（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 624 / LOW 65 / INVALID 159
结构观察区: Primary Flip 257.54（全链重定价，覆盖 100%）
Call Wall 270（弱结构｜现价低于该位 0.4%）
最近结构参考: Call Wall 270（现价低于该位 0.4%）
量化视角： 正 Gamma（505万，无历史分位）｜正 Gamma 减弱（497万）｜现价位于 Flip 上方 4.45%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 270（MaxPain，仅结算参考） / 270（Call Wall，弱结构）。
• Gamma 区域：切换参考 258（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 150.0P — Vol 2,789 | 最新价 $0.06 | OI 1632→3922 (ΔOI +2290张) | ΔOI/Volume 82.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2290张（+140.3% vs前日OI），连续性待观察（方向未知）
10-02 290.0C — Vol 2,729 | 最新价 $11.50 | OI 1231→2416 (ΔOI +1185张) | ΔOI/Volume 43.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1185张（+96.3% vs前日OI），连续性待观察（方向未知）
10-02 280.0P — Vol 2,355 | 最新价 $7.94 | OI 182→1337 (ΔOI +1155张) | ΔOI/Volume 49.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1155张（+634.6% vs前日OI），连续性待观察（方向未知）
10-02 210.0P — Vol 1,465 | 最新价 $0.09 | OI 812→1926 (ΔOI +1114张) | ΔOI/Volume 76.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1114张（+137.2% vs前日OI），连续性待观察（方向未知）
10-09 350.0C — Vol 2,325 | 最新价 $2.70 | OI 124→1077 (ΔOI +953张) | ΔOI/Volume 41.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增953张（+768.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,697 张（Put 4,559 / Call 2,138），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +9.1k / P +6.3k ｜ Activity HIGH ｜ 4D
10-09  C +2.1k / P +0.5k ｜ Activity HIGH ｜ 11D
10-16  C +0.3k / P +1.6k ｜ Activity HIGH ｜ 18D
10-23  C +27 / P -0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 10-02 Forward Structure
存量OI: C 34.4k / P 33.7k，今日变化ΔOI: C +9.1k / P +6.3k，平值价格ATM: C $9.80 / P $10.24 ｜ ATM IV 86.6%，净 delta 敞口 -152k shares
Top ΔOI: C 290 +1,185 ｜ P 280 +1,155
仓位参考: Max Pain 270 ｜ Call Wall 270（+0.4%，弱）（OI 3.0k） ｜ Put Wall 260（-3.3%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜ATM IV 86.6%｜历史 Rank 48%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 152,198 股

📆 10-09 Forward Structure
存量OI: C 7.6k / P 11.0k，今日变化ΔOI: C +2.1k / P +0.5k，平值价格ATM: C $15.00 / P $14.50 ｜ ATM IV 77.5%，净 delta 敞口 -4k shares
Top ΔOI: C 350 +953 ｜ P 240 -180
仓位参考: Max Pain 265 ｜ Call Wall 295（+9.7%，弱）（OI 0.5k） ｜ Put Wall 245（-8.9%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.5%｜历史 Rank 48%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,667 股

📆 10-16 Forward Structure
存量OI: C 68.1k / P 74.5k，今日变化ΔOI: C +0.3k / P +1.6k，平值价格ATM: C $18.87 / P $18.73 ｜ ATM IV 77.3%，净 delta 敞口 -68k shares
Top ΔOI: C 300 -564 ｜ C 315 +522
仓位参考: Max Pain 258 ｜ Call Wall 280（+4.1%，弱）（OI 8.3k） ｜ Put Wall 260（-3.3%，弱）（OI 3.8k）
量化解读： 存量两侧均衡｜ATM IV 77.3%｜历史 Rank 48%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 67,924 股

10-23（MEDIUM △）Top ΔOI: 300C -466
10-23（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 270（+0.4%，弱）（OI 0.7k） ｜ Put Wall 250（-7.1%，弱）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 86.6% vs 10-09 77.5%（差 +9.1pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/BE_morning.json