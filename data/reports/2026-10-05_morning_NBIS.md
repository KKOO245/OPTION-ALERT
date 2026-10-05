# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $771.25 ｜ QQQ $753.47
VIX 15.75 ↑2.9%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 240P ΔOI +896（距现价 +1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 242.81 → 今开 244.03（+0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 244.19 ｜ 低 234.59

Options: P/C成交量 0.93 | OI比 0.69 | ATM IV 75.9% | Skew -0.6pp | Term 1.01 | ExpMove ±6.6%（近端） | Rank 7%
量化视角： IV 历史低位（Rank 7%，期权偏便宜）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±6.6% ｜ 10-16（11D）±10.1% ｜ 10-23（18D）±13.0% ｜ 10-30（25D）±15.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,807,144 | GEX Change vs 上次快照 -1,694,721 | Flip: Primary Flip: 224.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 488 / LOW 22 / INVALID 142
结构观察区: Primary Flip 224.38（全链重定价，覆盖 100%）
最近结构参考: Flip 224（现价高于该位 5.8%）
量化视角： 正 Gamma（981万，无历史分位）｜正 Gamma 减弱（169万）｜现价位于 Flip 上方 5.80%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 224（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 100.0P — Vol 4,550 | 最新价 $0.04 | OI 4159→7755 (ΔOI +3596张) | ΔOI/Volume 79.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3596张（+86.5% vs前日OI），连续性待观察（方向未知）
10-16 270.0C — Vol 4,756 | 最新价 $4.65 | OI 4002→6278 (ΔOI +2276张) | ΔOI/Volume 47.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2276张（+56.9% vs前日OI），连续性待观察（方向未知）
10-16 225.0P — Vol 1,654 | 最新价 $5.64 | OI 316→1806 (ΔOI +1490张) | ΔOI/Volume 90.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1490张（+471.5% vs前日OI），连续性待观察（方向未知）
10-09 270.0C — Vol 2,811 | 最新价 $1.68 | OI 1319→2235 (ΔOI +916张) | ΔOI/Volume 32.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增916张（+69.5% vs前日OI），连续性待观察（方向未知）
10-09 240.0P — Vol 2,635 | 最新价 $7.50 | OI 237→1133 (ΔOI +896张) | ΔOI/Volume 34.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增896张（+378.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,174 张（Put 5,982 / Call 3,192），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +9.3k / P +4.0k ｜ Activity HIGH ｜ 4D
10-16  C +1.0k / P +3.8k ｜ Activity MEDIUM △ ｜ 11D
10-23  C +0.6k / P -0.4k ｜ Activity MEDIUM △ ｜ 18D
10-30  C +0.9k / P -0.1k ｜ Activity HIGH ｜ 25D

📆 10-09 Forward Structure
存量OI: C 41.9k / P 29.0k，今日变化ΔOI: C +9.3k / P +4.0k，平值价格ATM: C $7.93 / P $7.75 ｜ ATM IV 75.9%，净 delta 敞口 -62k shares
Top ΔOI: C 270 +916 ｜ P 240 +896 ｜ C 260 +858
仓位参考: Max Pain 230 ｜ Call Wall 242.5（+2.1%）（OI 7.1k） ｜ Put Wall 220（-7.3%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 75.9%｜历史 Rank 7%（近端代理）｜IV/RV 1.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 61,625 股

10-16（MEDIUM △）Top ΔOI: 270C +2,276 ｜ 225P +1,490
10-16（MEDIUM △）仓位参考: Max Pain 220 ｜ Call Wall 240（+1.1%，弱）（OI 5.3k） ｜ Put Wall 220（-7.3%，弱）（OI 4.7k）

10-23（MEDIUM △）仓位参考: Max Pain 225 ｜ Call Wall 220（-7.3%，弱）（OI 0.9k） ｜ Put Wall 220（-7.3%，弱）（OI 0.5k）

📆 10-30 Forward Structure
存量OI: C 11.2k / P 10.3k，今日变化ΔOI: C +0.9k / P -0.1k，平值价格ATM: C $19.68 / P $16.75 ｜ ATM IV 73.9%，净 delta 敞口 4k shares
Top ΔOI: C 340 +493 ｜ C 295 -193 ｜ C 300 +190
仓位参考: Max Pain 230 ｜ Call Wall 260（+9.5%，弱）（OI 0.5k） ｜ Put Wall 215（-9.4%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 73.9%｜历史 Rank 7%（近端代理）｜IV/RV 1.48×（近似）｜净 delta 敞口 正 4,316 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/NBIS_morning.json