# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $765.98 ｜ QQQ $715.34
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
🔴 **事件差分**: 10-30（1D）ATM IV 109.9% vs 11-06 92.7%（差 +17.2pp），覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 175P ΔOI +1,155（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 182.34 → 今开 173.15（-5.0%） | 较昨收变动（含盘初走势） ｜ 今日高 175.60 ｜ 低 169.42

Options: P/C成交量 0.51 | OI比 0.57 | ATM IV 109.9% | Skew -1.4pp | Term 0.85 | ExpMove ±5.1%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.57）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±5.1% ｜ 11-06（8D）±11.4% ｜ 11-13（15D）±15.7% ｜ 11-20（22D）±19.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,739,354 | GEX Change vs 上次快照 -8,186,638 | Flip: Primary Flip: 170.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 602 / LOW 69 / INVALID 183
结构观察区: Primary Flip 170.76（全链重定价，覆盖 99%）
最近结构参考: Flip 171（现价高于该位 1.4%）
量化视角： 正 Gamma（274万，无历史分位）｜正 Gamma 减弱（819万）｜现价位于 Flip 上方 1.44%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 175（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 171（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 175.0P — Vol 2,313 | 最新价 $2.96 | OI 876→2031 (ΔOI +1155张) | ΔOI/Volume 49.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1155张（+131.8% vs前日OI），连续性待观察（方向未知）
10-30 172.5P — Vol 2,749 | 最新价 $2.27 | OI 543→1690 (ΔOI +1147张) | ΔOI/Volume 41.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1147张（+211.2% vs前日OI），连续性待观察（方向未知）
11-13 230.0C — Vol 1,135 | 最新价 $3.55 | OI 1086→2087 (ΔOI +1001张) | ΔOI/Volume 88.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1001张（+92.2% vs前日OI），连续性待观察（方向未知）
10-30 177.5P — Vol 2,248 | 最新价 $3.93 | OI 88→1041 (ΔOI +953张) | ΔOI/Volume 42.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增953张（+1083.0% vs前日OI），连续性待观察（方向未知）
10-30 190.0C — Vol 8,283 | 最新价 $3.34 | OI 4464→5313 (ΔOI +849张) | ΔOI/Volume 10.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增849张（+19.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,105 张（Put 3,255 / Call 1,850），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +3.5k / P +5.0k ｜ Activity HIGH ｜ 1D
11-06  C +2.4k / P +1.9k ｜ Activity HIGH ｜ 8D
11-13  C +1.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 15D
11-20  C +0.4k / P +76 ｜ Activity MEDIUM △ ｜ 22D

📆 10-30 Forward Structure
存量OI: C 96.3k / P 54.9k，今日变化ΔOI: C +3.5k / P +5.0k，平值价格ATM: C $5.00 / P $3.88 ｜ ATM IV 109.9%，净 delta 敞口 -89k shares
Top ΔOI: P 175 +1,155 ｜ P 172 +1,147 ｜ P 177 +953
仓位参考: Max Pain 175 ｜ Call Wall 190（+9.7%，弱）（OI 5.3k） ｜ Put Wall 160（-7.6%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 109.9%｜历史 Rank 60%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 89,119 股

📆 11-06 Forward Structure
存量OI: C 48.4k / P 31.2k，今日变化ΔOI: C +2.4k / P +1.9k，平值价格ATM: C $10.13 / P $9.68 ｜ ATM IV 92.7%，净 delta 敞口 18k shares
Top ΔOI: C 185 +799 ｜ C 190 +637
仓位参考: Max Pain 190 ｜ Call Wall 170（-1.9%，弱）（OI 2.3k） ｜ Put Wall 170（-1.9%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 92.7%｜历史 Rank 60%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 17,938 股

11-13（MEDIUM △）Top ΔOI: 230C +1,001
11-13（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 175（+1.0%，弱）（OI 1.1k） ｜ Put Wall 165（-4.7%，弱）（OI 1.4k）

11-20（MEDIUM △）Top ΔOI: 145P -280 ｜ 220C +235
11-20（MEDIUM △）仓位参考: Max Pain 195 ｜ Call Wall 180（+3.9%，弱）（OI 5.5k） ｜ Put Wall 180（+3.9%，弱）（OI 3.2k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 109.9% vs 11-06 92.7%（差 +17.2pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/NBIS_morning.json