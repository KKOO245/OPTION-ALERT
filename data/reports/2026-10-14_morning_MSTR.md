# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $769.08 ｜ QQQ $728.95
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **事件差分**: 10-16 ATM IV 74.8% vs 10-23 64.6%（差 +10.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-16 149P ΔOI +1,124（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 152.18 → 今开 149.70（-1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 152.18 ｜ 低 145.05

Options: P/C成交量 0.74 | OI比 0.67 | ATM IV 74.8% | Skew -2.8pp | Term 0.89 | ExpMove ±4.6%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±4.6% ｜ 10-23（9D）±8.2% ｜ 10-30（16D）±12.1% ｜ 11-06（23D）±13.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 24,443,283 | GEX Change vs 上次快照 -35,099,721 | Flip: Primary Flip: 144.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 599 / LOW 93 / INVALID 192
结构观察区: Primary Flip 144.07（全链重定价，覆盖 98%）
最近结构参考: Flip 144（现价高于该位 2.3%）
量化视角： 正 Gamma（2444万，无历史分位）｜正 Gamma 减弱（3510万）｜现价位于 Flip 上方 2.34%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 142（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 144（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 145.0P — Vol 2,307 | 最新价 $3.40 | OI 2584→3890 (ΔOI +1306张) | ΔOI/Volume 56.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1306张（+50.5% vs前日OI），连续性待观察（方向未知）
10-16 155.0C — Vol 7,223 | 最新价 $2.88 | OI 20518→21683 (ΔOI +1165张) | ΔOI/Volume 16.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1165张（+5.7% vs前日OI），连续性待观察（方向未知）
10-16 149.0P — Vol 2,036 | 最新价 $2.56 | OI 979→2103 (ΔOI +1124张) | ΔOI/Volume 55.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1124张（+114.8% vs前日OI），连续性待观察（方向未知）
11-13 167.5C — Vol 1,148 | 最新价 $6.25 | OI 73→1076 (ΔOI +1003张) | ΔOI/Volume 87.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1003张（+1374.0% vs前日OI），连续性待观察（方向未知）
10-23 135.0P — Vol 1,399 | 最新价 $1.20 | OI 696→1573 (ΔOI +877张) | ΔOI/Volume 62.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增877张（+126.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,475 张（Put 3,307 / Call 2,168），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +3.9k / P +0.8k ｜ Activity HIGH ｜ 2D
10-23  C +2.2k / P +7.0k ｜ Activity HIGH ｜ 9D
10-30  C +1.0k / P +2.2k ｜ Activity HIGH ｜ 16D
11-06  C +0.4k / P +1.0k ｜ Activity MEDIUM △ ｜ 23D

📆 10-16 Forward Structure
存量OI: C 352.6k / P 234.8k，今日变化ΔOI: C +3.9k / P +0.8k，平值价格ATM: C $3.54 / P $3.30 ｜ ATM IV 74.8%，净 delta 敞口 38k shares
Top ΔOI: C 155 +1,165 ｜ P 149 +1,124 ｜ P 162 -983
仓位参考: Max Pain 142 ｜ Call Wall 157.5（+6.8%，弱）（OI 40.7k） ｜ Put Wall 140（-5.0%，弱）（OI 7.3k）
量化解读： 存量 Call 重｜ATM IV 74.8%｜历史 Rank 38%（近端代理）｜IV/RV 2.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 38,150 股

📆 10-23 Forward Structure
存量OI: C 46.2k / P 96.4k，今日变化ΔOI: C +2.2k / P +7.0k，平值价格ATM: C $6.30 / P $5.80 ｜ ATM IV 64.6%，净 delta 敞口 -181k shares
Top ΔOI: P 145 +1,306 ｜ P 135 +877
仓位参考: Max Pain 158 ｜ Call Wall 160（+8.5%，弱）（OI 2.6k） ｜ Put Wall 160（+8.5%，弱）（OI 6.3k）
量化解读： 存量 Put 重｜ATM IV 64.6%｜历史 Rank 38%（近端代理）｜IV/RV 1.79×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 180,842 股

📆 10-30 Forward Structure
存量OI: C 34.3k / P 53.0k，今日变化ΔOI: C +1.0k / P +2.2k，平值价格ATM: C $10.04 / P $7.75 ｜ ATM IV 67.3%，净 delta 敞口 -11k shares
仓位参考: Max Pain 160 ｜ Call Wall 160（+8.5%，弱）（OI 3.9k） ｜ Put Wall 160（+8.5%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 67.3%｜历史 Rank 38%（近端代理）｜IV/RV 1.86×（近似）｜净 delta 敞口 负 11,037 股

11-06（MEDIUM △）Top ΔOI: 165P -336 ｜ 150P +252
11-06（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 160（+8.5%）（OI 1.8k） ｜ Put Wall 160（+8.5%，弱）（OI 2.9k）

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 74.8% vs 10-23 64.6%（差 +10.2pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/MSTR_morning.json