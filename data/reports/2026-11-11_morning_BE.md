# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-13（2D）ATM IV 111.8% vs 11-20 95.0%（差 +16.7pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 185.42 → 今开 199.52（+7.6%） | 较昨收变动（含盘初走势） ｜ 今日高 211.30 ｜ 低 199.48

Options: P/C成交量 0.50 | OI比 0.82 | ATM IV 111.8% | Skew 7.0pp | Term 0.80 | ExpMove ±7.3%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 7.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（2D）±7.3% ｜ 11-20（9D）±12.8% ｜ 11-27（16D）±16.3% ｜ 12-04（23D）±17.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,450,427 | GEX Change vs 上次快照 9,084,136 | Flip: Primary Flip: 203.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 556 / LOW 132 / INVALID 240
结构观察区: Primary Flip 203.93（全链重定价，覆盖 98%）
Put Wall 200（弱结构｜现价高于该位 3.4%）
最近结构参考: Flip 204（现价高于该位 1.4%）
量化视角： 正 Gamma（145万，无历史分位）｜由负转正（+908万）｜现价位于 Flip 上方 1.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构） / 190（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 204（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 250.0C — Vol 2,376 | 最新价 $0.53 | OI 2315→4292 (ΔOI +1977张) | ΔOI/Volume 83.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1977张（+85.4% vs前日OI），连续性待观察（方向未知）
11-20 220.0C — Vol 2,135 | 最新价 $2.43 | OI 3361→4774 (ΔOI +1413张) | ΔOI/Volume 66.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1413张（+42.0% vs前日OI），连续性待观察（方向未知）
11-13 125.0P — Vol 1,051 | 最新价 $0.02 | OI 582→1533 (ΔOI +951张) | ΔOI/Volume 90.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增951张（+163.4% vs前日OI），连续性待观察（方向未知）
11-13 155.0P — Vol 913 | 最新价 $0.64 | OI 1215→1859 (ΔOI +644张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增644张（+53.0% vs前日OI），连续性待观察（方向未知）
11-20 172.5P — Vol 642 | 最新价 $6.75 | OI 1128→1739 (ΔOI +611张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增611张（+54.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,596 张（Put 2,206 / Call 3,390），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +2.1k / P +4.0k ｜ Activity HIGH ｜ 2D
11-20  C +4.6k / P +1.1k ｜ Activity HIGH ｜ 9D
11-27  C +0.5k / P +0.7k ｜ Activity HIGH ｜ 16D
12-04  C +0.3k / P +0.4k ｜ Activity HIGH ｜ 23D

📆 11-13 Forward Structure
存量OI: C 43.4k / P 35.7k，今日变化ΔOI: C +2.1k / P +4.0k，平值价格ATM: C $7.65 / P $7.50 ｜ ATM IV 111.8%，净 delta 敞口 162k shares
Top ΔOI: C 190 +536
仓位参考: Max Pain 190 ｜ Call Wall 220（+6.4%，弱）（OI 2.3k） ｜ Put Wall 190（-8.2%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 111.8%｜历史 Rank 70%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 162,384 股

📆 11-20 Forward Structure
存量OI: C 80.2k / P 81.1k，今日变化ΔOI: C +4.6k / P +1.1k，平值价格ATM: C $12.90 / P $13.50 ｜ ATM IV 95.0%，净 delta 敞口 165k shares
Top ΔOI: C 250 +1,977 ｜ C 220 +1,413 ｜ P 172 +611
仓位参考: Max Pain 215 ｜ Call Wall 220（+6.4%，弱）（OI 4.8k） ｜ Put Wall 200（-3.3%，弱）（OI 5.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 95.0%｜历史 Rank 70%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 165,041 股

📆 11-27 Forward Structure
存量OI: C 9.1k / P 10.9k，今日变化ΔOI: C +0.5k / P +0.7k，平值价格ATM: C $16.95 / P $16.75 ｜ ATM IV 87.7%，净 delta 敞口 15k shares
Top ΔOI: P 185 +355 ｜ P 177 +106
仓位参考: Max Pain 215 ｜ Call Wall 200（-3.3%，弱）（OI 0.7k） ｜ Put Wall 190（-8.2%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜ATM IV 87.7%｜历史 Rank 70%（近端代理）｜IV/RV 0.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,802 股

📆 12-04 Forward Structure
存量OI: C 6.5k / P 7.0k，今日变化ΔOI: C +0.3k / P +0.4k，平值价格ATM: C $18.15 / P $18.96 ｜ ATM IV 86.9%，净 delta 敞口 10k shares
Top ΔOI: P 185 +192 ｜ C 180 +97 ｜ C 200 +66
仓位参考: Max Pain 200 ｜ Call Wall 200（-3.3%，弱）（OI 0.6k） ｜ Put Wall 200（-3.3%）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 86.9%｜历史 Rank 70%（近端代理）｜IV/RV 0.74×（近似）｜净 delta 敞口 正 10,146 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 111.8% vs 11-20 95.0%（差 +16.7pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/BE_morning.json