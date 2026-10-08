# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $775.90 ｜ QQQ $755.88
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 380C ΔOI +3,559（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
TSLA  昨收 377.81 → 今开 374.12（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 375.96 ｜ 低 371.55

Options: P/C成交量 1.10 | OI比 1.05 | ATM IV 38.9% | Skew -0.9pp | Term 1.12 | ExpMove ±1.8%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构正常（Term 1.12）｜Put 保护异常便宜（Skew -0.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.10×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.05×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（1D）±1.8% ｜ 10-12（4D）±2.6% ｜ 10-14（6D）±3.5% ｜ 10-16（8D）±4.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 67,591,650 | GEX Change vs 上次快照 -48,680,306 | Flip: Primary Flip: 364.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1085 / LOW 126 / INVALID 513
结构观察区: Primary Flip 364.65（全链重定价，覆盖 99%）
Call Wall 400（现价低于该位 7.0%）
最近结构参考: Flip 365（现价高于该位 2.0%）
量化视角： 正 Gamma（6759万，无历史分位）｜正 Gamma 减弱（4868万）｜现价位于 Flip 上方 1.98%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 370（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 365（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 380.0C — Vol 34,075 | 最新价 $3.21 | OI 7574→11133 (ΔOI +3559张) | ΔOI/Volume 10.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3559张（+47.0% vs前日OI），连续性待观察（方向未知）
10-12 310.0P — Vol 3,005 | 最新价 $0.08 | OI 42→3037 (ΔOI +2995张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2995张（+7130.9% vs前日OI），连续性待观察（方向未知）
10-09 377.5P — Vol 19,227 | 最新价 $3.95 | OI 2867→5854 (ΔOI +2987张) | ΔOI/Volume 15.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2987张（+104.2% vs前日OI），连续性待观察（方向未知）
10-09 385.0C — Vol 18,542 | 最新价 $1.65 | OI 8826→11441 (ΔOI +2615张) | ΔOI/Volume 14.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2615张（+29.6% vs前日OI），连续性待观察（方向未知）
10-09 375.0C — Vol 20,009 | 最新价 $5.81 | OI 8458→10817 (ΔOI +2359张) | ΔOI/Volume 11.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2359张（+27.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 14,515 张（Put 5,982 / Call 8,533），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +20.5k / P +13.5k ｜ Activity HIGH ｜ 1D
10-12  C +5.1k / P +6.5k ｜ Activity HIGH ｜ 4D
10-14  C +1.8k / P +1.4k ｜ Activity HIGH ｜ 6D
10-16  C +9.6k / P +7.0k ｜ Activity HIGH ｜ 8D

📆 10-09 Forward Structure
存量OI: C 214.8k / P 225.3k，今日变化ΔOI: C +20.5k / P +13.5k，平值价格ATM: C $3.45 / P $3.39 ｜ ATM IV 38.9%，净 delta 敞口 -269k shares
Top ΔOI: C 380 +3,559 ｜ P 377 +2,987 ｜ C 385 +2,615
仓位参考: Max Pain 370 ｜ Call Wall 400（+7.6%）（OI 23.8k） ｜ Put Wall 370（-0.5%，弱）（OI 8.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 38.9%｜历史 Rank 8%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 负 268,875 股

📆 10-12 Forward Structure
存量OI: C 22.9k / P 22.7k，今日变化ΔOI: C +5.1k / P +6.5k，平值价格ATM: C $4.75 / P $4.76 ｜ ATM IV 29.5%，净 delta 敞口 -48k shares
Top ΔOI: C 405 +1,071 ｜ C 400 +735
仓位参考: Max Pain 372 ｜ Call Wall 400（+7.6%，弱）（OI 2.4k） ｜ Put Wall 370（-0.5%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 29.5%｜历史 Rank 8%（近端代理）｜IV/RV 1.04×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 48,264 股

📆 10-14 Forward Structure
存量OI: C 8.3k / P 6.7k，今日变化ΔOI: C +1.8k / P +1.4k，平值价格ATM: C $6.52 / P $6.55 ｜ ATM IV 33.5%，净 delta 敞口 3k shares
Top ΔOI: C 400 +380 ｜ C 405 +174 ｜ C 377 +162
仓位参考: Max Pain 370 ｜ Call Wall 400（+7.6%）（OI 1.4k） ｜ Put Wall 370（-0.5%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 33.5%｜历史 Rank 8%（近端代理）｜IV/RV 1.18×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 3,023 股

📆 10-16 Forward Structure
存量OI: C 315.8k / P 290.1k，今日变化ΔOI: C +9.6k / P +7.0k，平值价格ATM: C $8.90 / P $8.70 ｜ ATM IV 39.0%，净 delta 敞口 -87k shares
Top ΔOI: C 385 +2,003 ｜ P 340 +1,785 ｜ P 375 +1,541
仓位参考: Max Pain 370 ｜ Call Wall 400（+7.6%）（OI 23.3k） ｜ Put Wall 380（+2.2%，弱）（OI 14.7k）
量化解读： 存量两侧均衡｜ATM IV 39.0%｜历史 Rank 8%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 负 87,183 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 38.9% vs 10-12 29.5%（差 +9.5pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/TSLA_morning.json