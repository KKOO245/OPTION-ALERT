# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $774.46 ｜ QQQ $754.50
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　⏰ 今日
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 250C ΔOI +1,502（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 249.87 → 今开 242.21（-3.1%） | 较昨收变动（含盘初走势） ｜ 今日高 243.62 ｜ 低 235.70

Options: P/C成交量 1.30 | OI比 1.00 | ATM IV 79.2% | Skew -2.5pp | Term 0.92 | ExpMove ±5.0%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -2.5pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.30×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.00×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（2D）±5.0% ｜ 10-16（9D）±9.2% ｜ 10-23（16D）±11.9% ｜ 10-30（23D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,256,905 | GEX Change vs 上次快照 -14,810,062 | Flip: Primary Flip: 234.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 516 / LOW 39 / INVALID 129
结构观察区: Primary Flip 234.82（全链重定价，覆盖 100%）
Put Wall 220（弱结构｜现价高于该位 8.8%）
最近结构参考: Flip 235（现价高于该位 2.0%）
量化视角： 正 Gamma（726万，无历史分位）｜正 Gamma 减弱（1481万）｜现价位于 Flip 上方 1.95%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构）；上方 240（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 235（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 225.0P — Vol 10,374 | 最新价 $0.62 | OI 3183→9118 (ΔOI +5935张) | ΔOI/Volume 57.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5935张（+186.5% vs前日OI），连续性待观察（方向未知）
10-16 270.0C — Vol 10,721 | 最新价 $5.55 | OI 6150→10072 (ΔOI +3922张) | ΔOI/Volume 36.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3922张（+63.8% vs前日OI），连续性待观察（方向未知）
10-30 280.0C — Vol 3,275 | 最新价 $8.97 | OI 462→2975 (ΔOI +2513张) | ΔOI/Volume 76.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2513张（+543.9% vs前日OI），连续性待观察（方向未知）
10-09 260.0C — Vol 13,838 | 最新价 $3.53 | OI 2462→4078 (ΔOI +1616张) | ΔOI/Volume 11.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1616张（+65.6% vs前日OI），连续性待观察（方向未知）
10-16 250.0C — Vol 8,518 | 最新价 $12.30 | OI 5610→7112 (ΔOI +1502张) | ΔOI/Volume 17.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1502张（+26.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,488 张（Put 5,935 / Call 9,553），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +7.0k / P +9.8k ｜ Activity HIGH ｜ 2D
10-16  C +8.2k / P +4.8k ｜ Activity HIGH ｜ 9D
10-23  C +1.2k / P +59 ｜ Activity MEDIUM △ ｜ 16D
10-30  C +2.1k / P -0.4k ｜ Activity MEDIUM △ ｜ 23D

📆 10-09 Forward Structure
存量OI: C 53.9k / P 53.8k，今日变化ΔOI: C +7.0k / P +9.8k，平值价格ATM: C $5.67 / P $6.25 ｜ ATM IV 79.2%，净 delta 敞口 -584k shares
Top ΔOI: P 225 +5,935 ｜ C 260 +1,616
仓位参考: Max Pain 240 ｜ Call Wall 260（+8.6%，弱）（OI 4.1k） ｜ Put Wall 225（-6.0%）（OI 9.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.2%｜历史 Rank 10%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 583,615 股

📆 10-16 Forward Structure
存量OI: C 91.1k / P 100.6k，今日变化ΔOI: C +8.2k / P +4.8k，平值价格ATM: C $10.75 / P $11.15 ｜ ATM IV 71.2%，净 delta 敞口 -59k shares
Top ΔOI: C 270 +3,922 ｜ C 250 +1,502
仓位参考: Max Pain 225 ｜ Call Wall 250（+4.4%，弱）（OI 7.1k） ｜ Put Wall 220（-8.1%，弱）（OI 5.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 71.2%｜历史 Rank 10%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 59,029 股

10-23（MEDIUM △）Top ΔOI: 270C +567 ｜ 240C -274
10-23（MEDIUM △）仓位参考: Max Pain 225 ｜ Call Wall 220（-8.1%，弱）（OI 0.9k） ｜ Put Wall 225（-6.0%，弱）（OI 0.5k）

10-30（MEDIUM △）Top ΔOI: 290C -2,639 ｜ 280C +2,513
10-30（MEDIUM △）仓位参考: Max Pain 235 ｜ Put Wall 220（-8.1%，弱）（OI 0.9k）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 79.2% vs 10-16 71.2%（差 +8.0pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/NBIS_morning.json