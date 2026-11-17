# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **事件差分**: 11-20 ATM IV 89.7% vs 11-27 76.9%（差 +12.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 11.11 → 今开 10.71（-3.6%） | 较昨收变动（含盘初走势） ｜ 今日高 10.96 ｜ 低 10.41

Options: P/C成交量 0.40 | OI比 0.33 | ATM IV 89.7% | Skew 3.9pp | Term 0.97 | ExpMove ±9.4%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 0.97）｜保护溢价中性（Skew 3.9pp）｜存量 Call 偏重（OI比 0.33）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±9.4% ｜ 11-27（11D）±12.0% ｜ 12-04（18D）±5.0% ｜ 12-11（25D）±20.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 917,373 | GEX Change vs 上次快照 -203,739 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 157 / LOW 61 / INVALID 146
结构观察区: NO_CROSS
Put Wall 10（弱结构｜现价高于该位 9.0%）
最近结构参考: Put Wall 10（现价高于该位 9.0%）
量化视角： 正 Gamma（92万，无历史分位）｜正 Gamma 减弱（20万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 10（Put Wall，弱结构）；上方 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 13.0C — Vol 103 | 最新价 $0.05 | OI 174→234 (ΔOI +60张) | ΔOI/Volume 58.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增60张（+34.5% vs前日OI），连续性待观察（方向未知）
11-27 10.0P — Vol 53 | 最新价 $0.23 | OI 94→141 (ΔOI +47张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增47张（+50.0% vs前日OI），连续性待观察（方向未知）
12-18 11.0C — Vol 47 | 最新价 $1.20 | OI 110→157 (ΔOI +47张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增47张（+42.7% vs前日OI），连续性待观察（方向未知）
11-20 11.5C — Vol 61 | 最新价 $0.30 | OI 177→220 (ΔOI +43张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43张（+24.3% vs前日OI），连续性待观察（方向未知）
12-18 11.0P — Vol 50 | 最新价 $1.09 | OI 98→141 (ΔOI +43张) | ΔOI/Volume 86.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增43张（+43.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 240 张（Put 90 / Call 150），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +0.1k / P +45 ｜ Activity MEDIUM △ ｜ 4D
11-27  C +17 / P +76 ｜ Activity HIGH ｜ 11D
12-04  C +5 / P +0 ｜ Activity MEDIUM △ ｜ 18D
12-11  C -9 / P +0 ｜ Activity MEDIUM △ ｜ 25D

📆 11-20 Forward Structure
存量OI: C 6.4k / P 2.1k，今日变化ΔOI: C +0.1k / P +45，平值价格ATM: C $0.59 / P $0.43 ｜ ATM IV 89.7%，净 delta 敞口 1k shares
Top ΔOI: C 11 +43
仓位参考: Max Pain 12 ｜ Call Wall 10（-8.3%，弱）（OI 0.2k） ｜ Put Wall 11（+0.9%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 89.7%｜历史 Rank 24%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,002 股

📆 11-27 Forward Structure
存量OI: C 4.8k / P 0.7k，今日变化ΔOI: C +17 / P +76，平值价格ATM: C $0.70 / P $0.61 ｜ ATM IV 76.9%，净 delta 敞口 -2k shares
Top ΔOI: P 10 +47 ｜ P 11 +27 ｜ C 11 +8
仓位参考: Max Pain 12 ｜ Put Wall 10（-8.3%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 76.9%｜历史 Rank 24%（近端代理）｜IV/RV 0.79×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,945 股

12-04（MEDIUM △）仓位参考: Max Pain 13

12-11（MEDIUM △）Top ΔOI: 11C -1
12-11（MEDIUM △）仓位参考: Max Pain 12 ｜ Call Wall 10（-8.3%，弱）（OI 33） ｜ Put Wall 11（+0.9%，弱）（OI 13）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 89.7% vs 11-27 76.9%（差 +12.7pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/NNE_morning.json