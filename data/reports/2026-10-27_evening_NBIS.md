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
🟡 **事件差分**: 10-30 ATM IV 108.9% vs 11-06 96.9%（差 +11.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 170C ΔOI +889（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 159.23 → 收盘 170.47（+7.1%） ｜ 今日高 171.52 ｜ 低 158.31 ｜ 昨收 153.27 → 收盘 170.47（+11.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.53 | OI比 0.54 | ATM IV 108.9% | Skew 3.3pp | Term 0.88 | ExpMove ±7.9%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（3D）±7.9% ｜ 11-06（10D）±12.8% ｜ 11-13（17D）±18.3% ｜ 11-20（24D）±20.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,569,905 | GEX Change vs 上次快照 1,610,190 | Flip: Primary Flip: 168.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 578 / LOW 47 / INVALID 229
结构观察区: Primary Flip 168.02（全链重定价，覆盖 100%）
最近结构参考: Flip 168（现价高于该位 1.5%）
量化视角： 正 Gamma（157万，无历史分位）｜由负转正（+161万）｜现价位于 Flip 上方 1.46%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 172（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 168（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 225.0P — Vol 103 | 最新价 $61.53 | OI 325→2695 (ΔOI +2370张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2370张（+729.2% vs前日OI），连续性待观察（方向未知）
10-30 235.0C — Vol 337 | 最新价 $0.05 | OI 1204→3315 (ΔOI +2111张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2111张（+175.3% vs前日OI），连续性待观察（方向未知）
11-20 75.0P — Vol 56 | 最新价 $0.30 | OI 3748→5813 (ΔOI +2065张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2065张（+55.1% vs前日OI），连续性待观察（方向未知）
10-30 170.0C — Vol 10,439 | 最新价 $1.80 | OI 1716→3423 (ΔOI +1707张) | ΔOI/Volume 16.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1707张（+99.5% vs前日OI），连续性待观察（方向未知）
11-20 80.0P — Vol 8 | 最新价 $0.47 | OI 357→1862 (ΔOI +1505张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1505张（+421.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,758 张（Put 5,940 / Call 3,818），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +12.2k / P +1.2k ｜ Activity HIGH ｜ 3D
11-06  C +4.7k / P +2.1k ｜ Activity HIGH ｜ 10D
11-13  C +2.1k / P +0.3k ｜ Activity HIGH ｜ 17D
11-20  C +0.7k / P +0.2k ｜ Activity MEDIUM △ ｜ 24D

📆 10-30 Forward Structure
存量OI: C 90.3k / P 48.6k，今日变化ΔOI: C +12.2k / P +1.2k，平值价格ATM: C $7.00 / P $6.40 ｜ ATM IV 108.9%，净 delta 敞口 936k shares
Top ΔOI: C 160 +2,312 ｜ P 230 -1,535 ｜ C 180 +1,285
仓位参考: Max Pain 172 ｜ Call Wall 180（+5.6%，弱）（OI 4.3k） ｜ Put Wall 160（-6.1%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 108.9%｜历史 Rank 59%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 936,366 股

📆 11-06 Forward Structure
存量OI: C 40.9k / P 25.6k，今日变化ΔOI: C +4.7k / P +2.1k，平值价格ATM: C $11.50 / P $10.35 ｜ ATM IV 96.9%，净 delta 敞口 229k shares
Top ΔOI: C 170 +889 ｜ P 140 +575 ｜ C 165 +419
仓位参考: Max Pain 200 ｜ Put Wall 170（-0.3%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 96.9%｜历史 Rank 59%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 正 229,391 股

📆 11-13 Forward Structure
存量OI: C 17.9k / P 17.1k，今日变化ΔOI: C +2.1k / P +0.3k，平值价格ATM: C $16.20 / P $15.07 ｜ ATM IV 104.7%，净 delta 敞口 67k shares
Top ΔOI: C 195 +902 ｜ C 200 +271
仓位参考: Max Pain 190 ｜ Call Wall 175（+2.7%，弱）（OI 1.2k） ｜ Put Wall 165（-3.2%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜ATM IV 104.7%｜历史 Rank 59%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 67,134 股

11-20（MEDIUM △）Top ΔOI: 260C -569 ｜ 150P -529
11-20（MEDIUM △）仓位参考: Max Pain 195 ｜ Call Wall 180（+5.6%，弱）（OI 5.4k） ｜ Put Wall 180（+5.6%，弱）（OI 3.2k）

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 108.9% vs 11-06 96.9%（差 +11.9pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/NBIS_evening.json