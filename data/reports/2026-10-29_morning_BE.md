# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $765.72 ｜ QQQ $715.34
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 10-30（1D）ATM IV 101.4% vs 11-06 84.6%（差 +16.8pp），覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 225C ΔOI +856（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 228.08 → 今开 221.00（-3.1%） | 较昨收变动（含盘初走势） ｜ 今日高 229.50 ｜ 低 219.01

Options: P/C成交量 0.73 | OI比 0.74 | ATM IV 101.4% | Skew -0.1pp | Term 0.76 | ExpMove ±4.9%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±4.9% ｜ 11-06（8D）±10.3% ｜ 11-13（15D）±13.8% ｜ 11-20（22D）±15.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,183,431 | GEX Change vs 上次快照 -4,064,047 | Flip: Primary Flip: 218.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 567 / LOW 131 / INVALID 240
结构观察区: Primary Flip 218.01（全链重定价，覆盖 95%）
最近结构参考: Flip 218（现价高于该位 3.5%）
量化视角： 正 Gamma（518万，无历史分位）｜正 Gamma 减弱（406万）｜现价位于 Flip 上方 3.50%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 215（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 218（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 245.0C — Vol 1,952 | 最新价 $1.49 | OI 854→1768 (ΔOI +914张) | ΔOI/Volume 46.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增914张（+107.0% vs前日OI），连续性待观察（方向未知）
10-30 225.0C — Vol 3,572 | 最新价 $8.10 | OI 1485→2341 (ΔOI +856张) | ΔOI/Volume 24.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增856张（+57.6% vs前日OI），连续性待观察（方向未知）
10-30 232.5P — Vol 1,012 | 最新价 $8.55 | OI 211→938 (ΔOI +727张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增727张（+344.6% vs前日OI），连续性待观察（方向未知）
10-30 255.0C — Vol 1,623 | 最新价 $0.55 | OI 1065→1694 (ΔOI +629张) | ΔOI/Volume 38.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增629张（+59.1% vs前日OI），连续性待观察（方向未知）
10-30 235.0C — Vol 2,560 | 最新价 $3.74 | OI 1740→2292 (ΔOI +552张) | ΔOI/Volume 21.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增552张（+31.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,678 张（Put 727 / Call 2,951），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +2.6k / P +2.1k ｜ Activity HIGH ｜ 1D
11-06  C +0.6k / P +1.5k ｜ Activity HIGH ｜ 8D
11-13  C +1.0k / P +0.2k ｜ Activity MEDIUM △ ｜ 15D
11-20  C -0.2k / P +1.3k ｜ Activity HIGH ｜ 22D

📆 10-30 Forward Structure
存量OI: C 68.2k / P 50.4k，今日变化ΔOI: C +2.6k / P +2.1k，平值价格ATM: C $5.87 / P $5.20 ｜ ATM IV 101.4%，净 delta 敞口 -78k shares
Top ΔOI: C 245 +914 ｜ C 225 +856 ｜ P 232 +727
仓位参考: Max Pain 215 ｜ Call Wall 240（+6.4%，弱）（OI 4.0k） ｜ Put Wall 210（-6.9%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 101.4%｜历史 Rank 63%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 77,882 股

📆 11-06 Forward Structure
存量OI: C 19.7k / P 19.2k，今日变化ΔOI: C +0.6k / P +1.5k，平值价格ATM: C $11.84 / P $11.40 ｜ ATM IV 84.6%，净 delta 敞口 -31k shares
Top ΔOI: P 235 -286
仓位参考: Max Pain 230 ｜ Call Wall 225（-0.3%，弱）（OI 1.4k） ｜ Put Wall 235（+4.2%，弱）（OI 1.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 84.6%｜历史 Rank 63%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 31,180 股

11-13（MEDIUM △）Top ΔOI: 225C +68 ｜ 222C +44
11-13（MEDIUM △）仓位参考: Max Pain 240 ｜ Call Wall 240（+6.4%，弱）（OI 0.6k） ｜ Put Wall 240（+6.4%，弱）（OI 0.5k）

📆 11-20 Forward Structure
存量OI: C 59.6k / P 71.1k，今日变化ΔOI: C -0.2k / P +1.3k，平值价格ATM: C $18.45 / P $17.10 ｜ ATM IV 80.4%，净 delta 敞口 -36k shares
Top ΔOI: P 165 +452 ｜ P 230 +264 ｜ P 205 +233
仓位参考: Max Pain 230 ｜ Call Wall 240（+6.4%，弱）（OI 2.9k） ｜ Put Wall 220（-2.5%，弱）（OI 3.7k）
量化解读： 存量 Put 重｜ATM IV 80.4%｜历史 Rank 63%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 负 35,553 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 101.4% vs 11-06 84.6%（差 +16.8pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/BE_morning.json