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
🟡 **近现价集中开仓**: 11-06 12P ΔOI +19（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 12.16 → 今开 12.40（+2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 12.45 ｜ 低 11.95

Options: P/C成交量 1.85 | OI比 0.22 | ATM IV 74.2% | Skew -3.3pp | Term 1.00 | ExpMove ±8.0%（近端） | Rank 6%
量化视角： IV 历史低位（Rank 6%，期权偏便宜）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -3.3pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.22）+ 当日成交偏 Put（P/C量 1.85）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.85×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.22×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（4D）±8.0% ｜ 11-06（11D）±18.4% ｜ 11-13（18D）±3.3% ｜ 11-20（25D）±30.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 143,809 | GEX Change vs 上次快照 -125,436 | Flip: Primary Flip: 11.60（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 109 / LOW 74 / INVALID 217
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 11.60（全链重定价，覆盖 86%）
Put Wall 12（弱结构｜现价高于该位 2.0%）
最近结构参考: Put Wall 12（现价高于该位 2.0%）
量化视角： 正 Gamma（14万，无历史分位）｜正 Gamma 减弱（13万）｜现价位于 Flip 上方 5.52%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 12（Put Wall，弱结构）；上方 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 12（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 14.0P — Vol 64 | 最新价 $1.75 | OI 402→464 (ΔOI +62张) | ΔOI/Volume 96.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增62张（+15.4% vs前日OI），连续性待观察（方向未知）
11-06 11.5P — Vol 60 | 最新价 $0.40 | OI 0→60 (ΔOI +60张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增60张（前日OI缺失），值得跟踪（方向未知）
11-13 13.5C — Vol 100 | 最新价 $0.45 | OI 51→105 (ΔOI +54张) | ΔOI/Volume 54.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54张（+105.9% vs前日OI），连续性待观察（方向未知）
10-30 13.5P — Vol 43 | 最新价 $1.41 | OI 186→229 (ΔOI +43张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43张（+23.1% vs前日OI），连续性待观察（方向未知）
10-30 11.0P — Vol 39 | 最新价 $0.10 | OI 20→59 (ΔOI +39张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增39张（+195.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 258 张（Put 204 / Call 54），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +84 / P +0.1k ｜ Activity HIGH ｜ 4D
11-06  C +25 / P +87 ｜ Activity HIGH ｜ 11D
11-13  C +58 / P +1 ｜ Activity HIGH ｜ 18D
11-20  C +16 / P +19 ｜ Activity MEDIUM △ ｜ 25D

📆 10-30 Forward Structure
存量OI: C 7.2k / P 1.6k，今日变化ΔOI: C +84 / P +0.1k，平值价格ATM: C $0.58 / P $0.40 ｜ ATM IV 74.2%，净 delta 敞口 -6k shares
仓位参考: Max Pain 14 ｜ Put Wall 12（-2.0%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.2%｜历史 Rank 6%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,744 股

📆 11-06 Forward Structure
存量OI: C 1.6k / P 0.6k，今日变化ΔOI: C +25 / P +87，平值价格ATM: C $1.65 / P $0.60 ｜ ATM IV 72.4%，净 delta 敞口 -2k shares
Top ΔOI: P 11 +60 ｜ P 12 +19
仓位参考: Max Pain 16 ｜ Put Wall 13（+6.2%，弱）（OI 78）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.4%｜历史 Rank 6%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 负 2,483 股

📆 11-13 Forward Structure
存量OI: C 0.8k / P 0.4k，今日变化ΔOI: C +58 / P +1，平值价格ATM: C $0.00 / P $0.40 ｜ ATM IV 73.4%，净 delta 敞口 2k shares
Top ΔOI: P 13 -2
仓位参考: Max Pain 14 ｜ Put Wall 13（+6.2%，弱）（OI 68）
量化解读： 存量 Call 重｜ATM IV 73.4%｜历史 Rank 6%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,798 股

11-20（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 12（-2.0%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/NNE_morning.json