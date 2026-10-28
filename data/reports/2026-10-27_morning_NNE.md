# 期权晨报 2026-10-27（快照 10:20 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $nan
VIX 18.02 ↓2.0%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.6（fear）
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
🟡 **近现价集中开仓**: 10-30 13C ΔOI +310（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 11.86 → 今开 12.25（+3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 12.75 ｜ 低 12.08

Options: P/C成交量 0.34 | OI比 0.22 | ATM IV 84.4% | Skew 12.0pp | Term 0.90 | ExpMove ±7.7%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜保护溢价显著（Skew 12.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.22）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.22×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±7.7% ｜ 11-06（10D）±11.2% ｜ 11-13（17D）±14.5% ｜ 11-20（24D）±15.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 418,209 | GEX Change vs 上次快照 351,402 | Flip: Primary Flip: 11.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 130 / LOW 82 / INVALID 196
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 11.35（全链重定价，覆盖 86%）
Put Wall 12（弱结构｜现价高于该位 3.2%）
最近结构参考: Put Wall 12（现价高于该位 3.2%）
量化视角： 正 Gamma（42万，无历史分位）｜正 Gamma 增强（+35万）｜现价位于 Flip 上方 9.11%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 12（Put Wall，弱结构）；上方 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 11（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 13.0C — Vol 415 | 最新价 $0.07 | OI 132→442 (ΔOI +310张) | ΔOI/Volume 74.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增310张（+234.8% vs前日OI），连续性待观察（方向未知）
10-30 12.5C — Vol 230 | 最新价 $0.20 | OI 28→223 (ΔOI +195张) | ΔOI/Volume 84.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增195张（+696.4% vs前日OI），连续性待观察（方向未知）
11-06 11.0P — Vol 160 | 最新价 $0.25 | OI 5→165 (ΔOI +160张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增160张（+3200.0% vs前日OI），连续性待观察（方向未知）
10-30 13.5C — Vol 154 | 最新价 $0.01 | OI 202→298 (ΔOI +96张) | ΔOI/Volume 62.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增96张（+47.5% vs前日OI），连续性待观察（方向未知）
10-30 12.0C — Vol 122 | 最新价 $0.35 | OI 26→77 (ΔOI +51张) | ΔOI/Volume 41.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增51张（+196.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 812 张（Put 160 / Call 652），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.6k / P +0.1k ｜ Activity HIGH ｜ 3D
11-06  C +28 / P +0.1k ｜ Activity HIGH ｜ 10D
11-13  C +37 / P +30 ｜ Activity MEDIUM △ ｜ 17D
11-20  C +19 / P +29 ｜ Activity MEDIUM △ ｜ 24D

📆 10-30 Forward Structure
存量OI: C 7.8k / P 1.7k，今日变化ΔOI: C +0.6k / P +0.1k，平值价格ATM: C $0.20 / P $0.75 ｜ ATM IV 84.4%，净 delta 敞口 12k shares
Top ΔOI: C 13 +310 ｜ C 12 +195 ｜ C 13 +96
仓位参考: Max Pain 14 ｜ Put Wall 12（-3.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 84.4%｜历史 Rank 18%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 12,003 股

📆 11-06 Forward Structure
存量OI: C 1.6k / P 0.8k，今日变化ΔOI: C +28 / P +0.1k，平值价格ATM: C $0.45 / P $0.93 ｜ ATM IV 77.4%，净 delta 敞口 -2k shares
仓位参考: Max Pain 16 ｜ Put Wall 13（+5.0%，弱）（OI 78）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 77.4%｜历史 Rank 18%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,238 股

11-13（MEDIUM △）Top ΔOI: 11P +26 ｜ 11C +19
11-13（MEDIUM △）仓位参考: Max Pain 14 ｜ Call Wall 13.5（+9.1%，弱）（OI 0.1k） ｜ Put Wall 13（+5.0%，弱）（OI 68）

11-20（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 12（-3.1%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 84.4% vs 11-06 77.4%（差 +7.0pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/NNE_morning.json