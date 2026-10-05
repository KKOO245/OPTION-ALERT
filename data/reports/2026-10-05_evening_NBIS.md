# 期权晚报 2026-10-05（快照 16:51 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $756.20
VIX 15.52 ↑1.4%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
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
🟡 **近现价集中开仓**: 10-09 240P ΔOI +896（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 244.03 → 收盘 232.57（-4.7%） ｜ 今日高 244.19 ｜ 低 230.51 ｜ 昨收 242.81 → 收盘 232.57（-4.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.62 | OI比 0.69 | ATM IV 73.7% | Skew -4.0pp | Term 0.97 | ExpMove ±6.2%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -4.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（4D）±6.2% ｜ 10-16（11D）±9.4% ｜ 10-23（18D）±12.2% ｜ 10-30（25D）±14.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,779,701 | GEX Change vs 上次快照 -3,027,442 | Flip: Primary Flip: 224.04（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 477 / LOW 25 / INVALID 150
结构观察区: Primary Flip 224.04（全链重定价，覆盖 100%）
最近结构参考: Flip 224（现价高于该位 3.8%）
量化视角： 正 Gamma（678万，无历史分位）｜正 Gamma 减弱（303万）｜现价位于 Flip 上方 3.81%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 230（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 224（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 100.0P — Vol 148 | 最新价 $0.05 | OI 4159→7755 (ΔOI +3596张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3596张（+86.5% vs前日OI），连续性待观察（方向未知）
10-16 270.0C — Vol 4,455 | 最新价 $2.19 | OI 4002→6278 (ΔOI +2276张) | ΔOI/Volume 51.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2276张（+56.9% vs前日OI），连续性待观察（方向未知）
10-16 225.0P — Vol 575 | 最新价 $7.50 | OI 316→1806 (ΔOI +1490张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1490张（+471.5% vs前日OI），连续性待观察（方向未知）
10-09 270.0C — Vol 1,625 | 最新价 $0.45 | OI 1319→2235 (ΔOI +916张) | ΔOI/Volume 56.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增916张（+69.5% vs前日OI），连续性待观察（方向未知）
10-09 240.0P — Vol 590 | 最新价 $10.65 | OI 237→1133 (ΔOI +896张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增896张（+378.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,174 张（Put 5,982 / Call 3,192），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +9.3k / P +4.0k ｜ Activity HIGH ｜ 4D
10-16  C +1.0k / P +3.8k ｜ Activity HIGH ｜ 11D
10-23  C +0.6k / P -0.4k ｜ Activity HIGH ｜ 18D
10-30  C +0.9k / P -0.1k ｜ Activity HIGH ｜ 25D

📆 10-09 Forward Structure
存量OI: C 41.9k / P 29.0k，今日变化ΔOI: C +9.3k / P +4.0k，平值价格ATM: C $7.30 / P $7.10 ｜ ATM IV 73.7%，净 delta 敞口 -129k shares
Top ΔOI: P 240 +896 ｜ C 260 +858
仓位参考: Max Pain 230 ｜ Call Wall 242.5（+4.3%）（OI 7.1k） ｜ Put Wall 220（-5.4%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 73.7%｜历史 Rank 5%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 128,647 股

📆 10-16 Forward Structure
存量OI: C 72.4k / P 91.0k，今日变化ΔOI: C +1.0k / P +3.8k，平值价格ATM: C $11.45 / P $10.32 ｜ ATM IV 69.5%，净 delta 敞口 -120k shares
Top ΔOI: C 270 +2,276 ｜ P 225 +1,490
仓位参考: Max Pain 220 ｜ Call Wall 240（+3.2%，弱）（OI 5.3k） ｜ Put Wall 220（-5.4%，弱）（OI 4.7k）
量化解读： 存量 Put 重｜ATM IV 69.5%｜历史 Rank 5%（近端代理）｜IV/RV 1.39×（近似）｜净 delta 敞口 负 119,938 股

📆 10-23 Forward Structure
存量OI: C 8.7k / P 9.4k，今日变化ΔOI: C +0.6k / P -0.4k，平值价格ATM: C $14.65 / P $13.66 ｜ ATM IV 69.9%，净 delta 敞口 -3k shares
仓位参考: Max Pain 225 ｜ Call Wall 220（-5.4%，弱）（OI 0.9k） ｜ Put Wall 220（-5.4%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 69.9%｜历史 Rank 5%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,929 股

📆 10-30 Forward Structure
存量OI: C 11.2k / P 10.3k，今日变化ΔOI: C +0.9k / P -0.1k，平值价格ATM: C $16.38 / P $18.35 ｜ ATM IV 69.8%，净 delta 敞口 3k shares
Top ΔOI: C 295 -193 ｜ C 300 +190
仓位参考: Max Pain 230 ｜ Put Wall 215（-7.6%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 69.8%｜历史 Rank 5%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 正 2,717 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/NBIS_evening.json