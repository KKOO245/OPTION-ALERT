# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $777.22 ｜ QQQ $757.73
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 390C ΔOI +2,112（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 380.68 → 今开 378.35（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 382.35 ｜ 低 374.43

Options: P/C成交量 0.95 | OI比 0.66 | ATM IV 47.3% | Skew 0.3pp | Term 0.90 | ExpMove ±2.5%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 0.90）｜保护溢价薄（Skew 0.3pp）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±2.5% ｜ 10-12（5D）±3.0% ｜ 10-14（7D）±3.9% ｜ 10-16（9D）±4.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 135,685,617 | GEX Change vs 上次快照 -26,559,535 | Flip: Primary Flip: 364.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 1164 / LOW 161 / INVALID 517
结构观察区: Primary Flip 364.52（全链重定价，覆盖 98%）
Call Wall 400（现价低于该位 5.8%）
最近结构参考: Flip 365（现价高于该位 3.4%）
量化视角： 正 Gamma（1.36亿，无历史分位）｜正 Gamma 减弱（2656万）｜现价位于 Flip 上方 3.40%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 375（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 365（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-07 385.0C — Vol 100,258 | 最新价 $1.31 | OI 3684→15375 (ΔOI +11691张) | ΔOI/Volume 11.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11691张（+317.4% vs前日OI），连续性待观察（方向未知）
10-07 370.0P — Vol 34,599 | 最新价 $0.31 | OI 5107→13008 (ΔOI +7901张) | ΔOI/Volume 22.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7901张（+154.7% vs前日OI），连续性待观察（方向未知）
10-07 390.0C — Vol 58,783 | 最新价 $0.47 | OI 5013→10914 (ΔOI +5901张) | ΔOI/Volume 10.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5901张（+117.7% vs前日OI），连续性待观察（方向未知）
10-09 430.0C — Vol 5,446 | 最新价 $0.06 | OI 2218→6759 (ΔOI +4541张) | ΔOI/Volume 83.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4541张（+204.7% vs前日OI），连续性待观察（方向未知）
10-07 392.5C — Vol 21,068 | 最新价 $0.28 | OI 1435→5832 (ΔOI +4397张) | ΔOI/Volume 20.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4397张（+306.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 34,431 张（Put 7,901 / Call 26,530），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 108.8k / P 72.3k，今日成交量: C 190.3k / P 181.4k，平值价格ATM: C $1.26 / P $2.81 ｜ ATM IV 47.3%，预期波动 ±1.1%，Max Pain 375
Top ΔOI: C 385 +11,691 ｜ P 370 +7,901 ｜ C 390 +5,901

📆 Forward Expiration Structure

10-09  C +17.0k / P +6.3k ｜ Activity HIGH ｜ 2D
10-12  C +4.0k / P +2.9k ｜ Activity HIGH ｜ 5D
10-14  C +0.8k / P +0.8k ｜ Activity HIGH ｜ 7D
10-16  C +4.2k / P +6.0k ｜ Activity HIGH ｜ 9D

📆 10-09 Forward Structure
存量OI: C 194.4k / P 211.9k，今日变化ΔOI: C +17.0k / P +6.3k，平值价格ATM: C $4.05 / P $5.30 ｜ ATM IV 39.3%，净 delta 敞口 -200k shares
Top ΔOI: P 350 -2,637 ｜ C 390 +2,112
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.1%）（OI 21.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 39.3%｜历史 Rank 32%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 199,512 股

📆 10-12 Forward Structure
存量OI: C 17.8k / P 16.2k，今日变化ΔOI: C +4.0k / P +2.9k，平值价格ATM: C $5.00 / P $6.34 ｜ ATM IV 31.3%，净 delta 敞口 -18k shares
Top ΔOI: C 385 +824 ｜ P 360 +645 ｜ C 400 +351
仓位参考: Max Pain 370 ｜ Call Wall 380（+0.8%，弱）（OI 1.7k） ｜ Put Wall 360（-4.5%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜ATM IV 31.3%｜历史 Rank 32%（近端代理）｜IV/RV 1.10×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 18,126 股

📆 10-14 Forward Structure
存量OI: C 6.5k / P 5.4k，今日变化ΔOI: C +0.8k / P +0.8k，平值价格ATM: C $6.55 / P $8.00 ｜ ATM IV 34.1%，净 delta 敞口 184 shares
Top ΔOI: C 382 +193 ｜ P 380 +127 ｜ P 370 +107
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.1%）（OI 1.0k） ｜ Put Wall 370（-1.8%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 34.1%｜历史 Rank 32%（近端代理）｜IV/RV 1.20×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 184 股

📆 10-16 Forward Structure
存量OI: C 306.2k / P 283.1k，今日变化ΔOI: C +4.2k / P +6.0k，平值价格ATM: C $8.56 / P $9.90 ｜ ATM IV 38.1%，净 delta 敞口 -46k shares
Top ΔOI: P 370 +1,043
仓位参考: Max Pain 370 ｜ Call Wall 400（+6.1%）（OI 23.9k） ｜ Put Wall 380（+0.8%，弱）（OI 14.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.1%｜历史 Rank 32%（近端代理）｜IV/RV 1.34×（近似）｜净 delta 敞口 负 46,227 股

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 39.3% vs 10-12 31.3%（差 +8.0pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/TSLA_morning.json