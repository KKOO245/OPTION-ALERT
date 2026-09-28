# 期权晨报 2026-09-28（快照 10:20 ET）

📊 市场环境

SPY $767.62 ｜ QQQ $737.23
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
🟡 **近现价集中开仓**: 10-02 162C ΔOI +29,297（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 158.61 → 今开 157.90（-0.4%） | 较昨收变动（含盘初走势） ｜ 今日高 159.75 ｜ 低 156.33

Options: P/C成交量 1.08 | OI比 0.82 | ATM IV 73.4% | Skew -6.4pp | Term 0.90 | ExpMove ±6.5%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构正常（Term 0.90）｜Put 保护异常便宜（Skew -6.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.08×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（4D）±6.5% ｜ 10-09（11D）±9.2% ｜ 10-16（18D）±11.7% ｜ 10-23（25D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 60,291,767 | GEX Change vs 上次快照 45,451,222 | Flip: Primary Flip: 143.43（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 819 / LOW 41 / INVALID 172
结构观察区: Primary Flip 143.43（全链重定价，覆盖 100%）
Call Wall 170（弱结构｜现价低于该位 6.4%）
最近结构参考: Call Wall 170（现价低于该位 6.4%）
量化视角： 正 Gamma（6029万，无历史分位）｜正 Gamma 增强（+4545万）｜现价位于 Flip 上方 10.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 143（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 170.0C — Vol 51,657 | 最新价 $2.20 | OI 5891→44186 (ΔOI +38295张) | ΔOI/Volume 74.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38295张（+650.1% vs前日OI），连续性待观察（方向未知）
10-02 162.5C — Vol 32,928 | 最新价 $4.10 | OI 663→29960 (ΔOI +29297张) | ΔOI/Volume 89.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增29297张（+4418.9% vs前日OI），连续性待观察（方向未知）
10-02 165.0C — Vol 33,249 | 最新价 $3.35 | OI 2079→30103 (ΔOI +28024张) | ΔOI/Volume 84.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增28024张（+1348.0% vs前日OI），连续性待观察（方向未知）
10-02 100.0P — Vol 23,790 | 最新价 $0.04 | OI 5279→28774 (ΔOI +23495张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23495张（+445.1% vs前日OI），连续性待观察（方向未知）
10-02 172.5C — Vol 19,655 | 最新价 $1.75 | OI 4624→21572 (ΔOI +16948张) | ΔOI/Volume 86.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16948张（+366.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 136,059 张（Put 23,495 / Call 112,564），跨 1 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +131.2k / P +68.5k ｜ Activity HIGH ｜ 4D
10-09  C +6.4k / P +2.4k ｜ Activity HIGH ｜ 11D
10-16  C +7.6k / P -0.9k ｜ Activity HIGH ｜ 18D
10-23  C +0.9k / P +3.2k ｜ Activity MEDIUM △ ｜ 25D

📆 10-02 Forward Structure
存量OI: C 229.9k / P 187.6k，今日变化ΔOI: C +131.2k / P +68.5k，平值价格ATM: C $4.50 / P $5.80 ｜ ATM IV 73.4%，净 delta 敞口 3.8M shares
Top ΔOI: C 170 +38,295 ｜ C 162 +29,297 ｜ C 165 +28,024
仓位参考: Max Pain 155 ｜ Call Wall 170（+6.8%，弱）（OI 44.2k） ｜ Put Wall 150（-5.8%，弱）（OI 12.6k）
量化解读： 存量 Call 重｜ATM IV 73.4%｜历史 Rank 34%（近端代理）｜IV/RV 0.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,764,027 股

📆 10-09 Forward Structure
存量OI: C 37.8k / P 50.0k，今日变化ΔOI: C +6.4k / P +2.4k，平值价格ATM: C $6.85 / P $7.81 ｜ ATM IV 65.2%，净 delta 敞口 263k shares
Top ΔOI: C 165 +3,654 ｜ C 160 -2,062 ｜ C 144 +1,569
仓位参考: Max Pain 144 ｜ Call Wall 144（-9.5%，弱）（OI 5.4k） ｜ Put Wall 155（-2.6%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 65.2%｜历史 Rank 34%（近端代理）｜IV/RV 0.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 262,535 股

📆 10-16 Forward Structure
存量OI: C 171.8k / P 141.4k，今日变化ΔOI: C +7.6k / P -0.9k，平值价格ATM: C $8.80 / P $9.75 ｜ ATM IV 65.0%，净 delta 敞口 38k shares
Top ΔOI: P 115 -2,439 ｜ C 190 +811
仓位参考: Max Pain 120 ｜ Call Wall 155（-2.6%，弱）（OI 10.4k） ｜ Put Wall 160（+0.5%，弱）（OI 4.4k）
量化解读： 存量 Call 重｜ATM IV 65.0%｜历史 Rank 34%（近端代理）｜IV/RV 0.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 37,701 股

10-23（MEDIUM △）Top ΔOI: 162C +380
10-23（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 170（+6.8%，弱）（OI 1.0k） ｜ Put Wall 155（-2.6%，弱）（OI 1.7k）

📅 事件差分（观察，非因果）: 10-02（4D）ATM IV 73.4% vs 10-09 65.2%（差 +8.2pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-28/MSTR_morning.json