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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 12.25 → 收盘 12.34（+0.7%） ｜ 今日高 12.75 ｜ 低 12.08 ｜ 昨收 11.86 → 收盘 12.34（+4.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.20 | OI比 0.22 | ATM IV 85.7% | Skew 10.4pp | Term 0.85 | ExpMove ±6.7%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价显著（Skew 10.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.22）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.20×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.22×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±6.7% ｜ 11-06（10D）±12.5% ｜ 11-13（17D）±14.5% ｜ 11-20（24D）±16.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 183,746 | GEX Change vs 上次快照 -234,463 | Flip: Primary Flip: 11.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 149 / LOW 78 / INVALID 181
结构观察区: Primary Flip 11.91（全链重定价，覆盖 98%）
Put Wall 12（弱结构｜现价高于该位 2.8%）
最近结构参考: Put Wall 12（现价高于该位 2.8%）
量化视角： 正 Gamma（18万，无历史分位）｜正 Gamma 减弱（23万）｜现价位于 Flip 上方 3.59%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 12（Put Wall，弱结构）；上方 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 12（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 14.0P — Vol 21 | 最新价 $2.12 | OI 402→464 (ΔOI +62张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增62张（+15.4% vs前日OI），值得跟踪（方向未知）
11-06 11.5P — Vol 4 | 最新价 $0.45 | OI 0→60 (ΔOI +60张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增60张（量数据缺失），以日内换手为主
11-13 13.5C — Vol 100（Yahoo补） | 最新价 $0.45 | OI 51→105 (ΔOI +54张) | ΔOI/Volume 54.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增54张（+105.9% vs前日OI），连续性待观察（方向未知）
10-30 13.5P — Vol 45 | 最新价 $1.35 | OI 186→229 (ΔOI +43张) | ΔOI/Volume 95.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43张（+23.1% vs前日OI），连续性待观察（方向未知）
10-30 11.0P — Vol 56 | 最新价 $0.10 | OI 20→59 (ΔOI +39张) | ΔOI/Volume 69.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增39张（+195.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 258 张（Put 204 / Call 54），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.6k / P +0.1k ｜ Activity HIGH ｜ 3D
11-06  C +28 / P +0.1k ｜ Activity MEDIUM △ ｜ 10D
11-13  C +37 / P +30 ｜ Activity MEDIUM △ ｜ 17D
11-20  C +19 / P +29 ｜ Activity LOW ｜ 24D

📆 10-30 Forward Structure
存量OI: C 7.8k / P 1.7k，今日变化ΔOI: C +0.6k / P +0.1k，平值价格ATM: C $0.45 / P $0.38 ｜ ATM IV 85.7%，净 delta 敞口 26k shares
Top ΔOI: C 13 +310 ｜ C 12 +195 ｜ C 13 +96
仓位参考: Max Pain 14 ｜ Put Wall 12（-2.8%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 85.7%｜历史 Rank 20%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,370 股

11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（+5.3%，弱）（OI 78）

11-13（MEDIUM △）Top ΔOI: 11P +26 ｜ 11C +19
11-13（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 13.5（+9.4%，弱）（OI 0.1k） ｜ Put Wall 13（+5.3%，弱）（OI 68）

11-20（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 12（-2.8%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 85.7% vs 11-06 77.9%（差 +7.8pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/NNE_evening.json