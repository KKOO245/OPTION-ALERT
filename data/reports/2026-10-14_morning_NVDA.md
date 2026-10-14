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
🟡 **近现价集中开仓**: 10-19 225C ΔOI +1,430（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 228.52 → 今开 225.60（-1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 226.00 ｜ 低 224.24

Options: P/C成交量 0.83 | OI比 0.91 | ATM IV 45.0% | Skew 0.5pp | Term 0.70 | ExpMove ±2.4%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价薄（Skew 0.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±2.4% ｜ 10-19（5D）±2.8% ｜ 10-21（7D）±3.5% ｜ 10-23（9D）±4.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 296,708,216 | GEX Change vs 上次快照 -105,889,264 | Flip: Primary Flip: 217.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 749 / LOW 227 / INVALID 586
结构观察区: Primary Flip 217.96（全链重定价，覆盖 96%）
Put Wall 220（弱结构｜现价高于该位 2.2%） | Call Wall 240（弱结构｜现价低于该位 6.3%）
最近结构参考: Put Wall 220（现价高于该位 2.2%）
量化视角： 正 Gamma（2.97亿，无历史分位）｜正 Gamma 减弱（1.06亿）｜现价位于 Flip 上方 3.17%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构）；上方 228（MaxPain，仅结算参考） / 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 218（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 237.5C — Vol 23,464 | 最新价 $0.46 | OI 41979→53026 (ΔOI +11047张) | ΔOI/Volume 47.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11047张（+26.3% vs前日OI），连续性待观察（方向未知）
10-14 190.0P — Vol 13,195 | 最新价 $0.01 | OI 2040→12045 (ΔOI +10005张) | ΔOI/Volume 75.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10005张（+490.4% vs前日OI），连续性待观察（方向未知）
10-14 235.0C — Vol 39,521 | 最新价 $0.17 | OI 9707→19136 (ΔOI +9429张) | ΔOI/Volume 23.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9429张（+97.1% vs前日OI），连续性待观察（方向未知）
10-16 235.0C — Vol 40,335 | 最新价 $0.83 | OI 76512→84763 (ΔOI +8251张) | ΔOI/Volume 20.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8251张（+10.8% vs前日OI），连续性待观察（方向未知）
10-14 230.0C — Vol 85,613 | 最新价 $1.19 | OI 9993→17357 (ΔOI +7364张) | ΔOI/Volume 8.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7364张（+73.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 46,096 张（Put 10,005 / Call 36,091），跨 2 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 154.9k / P 141.7k，今日成交量: C 106.6k / P 89.0k，平值价格ATM: C $0.89 / P $1.31 ｜ ATM IV 45.0%，预期波动 ±1.0%，Max Pain 228
Top ΔOI: P 190 +10,005 ｜ C 235 +9,429 ｜ C 230 +7,364

📆 Forward Expiration Structure

10-16  C +32.8k / P +12.7k ｜ Activity HIGH ｜ 2D
10-19  C +11.4k / P +3.5k ｜ Activity HIGH ｜ 5D
10-21  C +11.7k / P +6.1k ｜ Activity HIGH ｜ 7D
10-23  C +10.6k / P +5.6k ｜ Activity HIGH ｜ 9D

📆 10-16 Forward Structure
存量OI: C 1076.0k / P 829.4k，今日变化ΔOI: C +32.8k / P +12.7k，平值价格ATM: C $2.58 / P $2.86 ｜ ATM IV 38.5%，净 delta 敞口 238k shares
Top ΔOI: C 237 +11,047 ｜ C 235 +8,251 ｜ C 240 +4,380
仓位参考: Max Pain 220 ｜ Call Wall 220（-2.2%，弱）（OI 99.0k） ｜ Put Wall 220（-2.2%，弱）（OI 68.0k）
量化解读： 存量 Call 重｜ATM IV 38.5%｜历史 Rank 58%（近端代理）｜IV/RV 2.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 237,953 股

📆 10-19 Forward Structure
存量OI: C 48.7k / P 18.4k，今日变化ΔOI: C +11.4k / P +3.5k，平值价格ATM: C $3.05 / P $3.15 ｜ ATM IV 29.3%，净 delta 敞口 164k shares
Top ΔOI: C 242 +2,160 ｜ C 245 +1,433 ｜ C 225 +1,430
仓位参考: Max Pain 230 ｜ Call Wall 235（+4.5%，弱）（OI 4.1k） ｜ Put Wall 230（+2.3%）（OI 4.3k）
量化解读： 存量 Call 重｜ATM IV 29.3%｜历史 Rank 58%（近端代理）｜IV/RV 1.57×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 164,018 股

📆 10-21 Forward Structure
存量OI: C 21.7k / P 12.6k，今日变化ΔOI: C +11.7k / P +6.1k，平值价格ATM: C $3.85 / P $3.98 ｜ ATM IV 30.7%，净 delta 敞口 7k shares
Top ΔOI: P 220 +3,051 ｜ C 240 +3,047 ｜ C 230 +2,673
仓位参考: Max Pain 228 ｜ Call Wall 240（+6.7%）（OI 6.7k） ｜ Put Wall 220（-2.2%）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 30.7%｜历史 Rank 58%（近端代理）｜IV/RV 1.65×（近似）｜净 delta 敞口 正 7,201 股

📆 10-23 Forward Structure
存量OI: C 169.7k / P 134.8k，今日变化ΔOI: C +10.6k / P +5.6k，平值价格ATM: C $4.50 / P $4.54 ｜ ATM IV 31.6%，净 delta 敞口 45k shares
Top ΔOI: C 227 +1,364
仓位参考: Max Pain 228 ｜ Call Wall 240（+6.7%）（OI 60.1k） ｜ Put Wall 205（-8.8%，弱）（OI 10.7k）
量化解读： 存量 Call 重｜ATM IV 31.6%｜历史 Rank 58%（近端代理）｜IV/RV 1.70×（近似）｜净 delta 敞口 正 44,721 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 38.5% vs 10-19 29.3%（差 +9.2pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/NVDA_morning.json