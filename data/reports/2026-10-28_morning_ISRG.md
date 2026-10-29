# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 430P ΔOI +18（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 445.88 → 今开 441.42（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 447.96 ｜ 低 437.51

Options: P/C成交量 0.00 | OI比 0.90 | ATM IV 47.5% | Skew 6.4pp | Term 0.67 | ExpMove ±2.8%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价显著（Skew 6.4pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.00×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（2D）±2.8% ｜ 11-06（9D）±2.9% ｜ 11-13（16D）±3.5% ｜ 11-20（23D）±7.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,831,994 | GEX Change vs 上次快照 -315,563 | Flip: Primary Flip: 418.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 291 / LOW 166 / INVALID 527
结构观察区: Primary Flip 418.71（全链重定价，覆盖 95%）
Call Wall 420（弱结构｜现价高于该位 5.4%）
最近结构参考: Call Wall 420（现价高于该位 5.4%）
量化视角： 正 Gamma（183万，无历史分位）｜正 Gamma 减弱（32万）｜现价位于 Flip 上方 5.74%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 435（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 419（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 420.0P — Vol 165 | 最新价 $2.30 | OI 41→165 (ΔOI +124张) | ΔOI/Volume 75.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增124张（+302.4% vs前日OI），连续性待观察（方向未知）
11-06 450.0C — Vol 43 | 最新价 $9.30 | OI 53→88 (ΔOI +35张) | ΔOI/Volume 81.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35张（+66.0% vs前日OI），连续性待观察（方向未知）
11-06 390.0P — Vol 102 | 最新价 $0.20 | OI 49→76 (ΔOI +27张) | ΔOI/Volume 26.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27张（+55.1% vs前日OI），连续性待观察（方向未知）
10-30 425.0P — Vol 43 | 最新价 $1.01 | OI 101→126 (ΔOI +25张) | ΔOI/Volume 58.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增25张（+24.8% vs前日OI），连续性待观察（方向未知）
10-30 430.0P — Vol 30 | 最新价 $1.41 | OI 52→70 (ΔOI +18张) | ΔOI/Volume 60.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18张（+34.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 229 张（Put 194 / Call 35），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +28 / P +68 ｜ Activity LOW ｜ 2D
11-06  C +46 / P +0.2k ｜ Activity MEDIUM △ ｜ 9D
11-13  C +6 / P -46 ｜ Activity LOW ｜ 16D
11-20  C +37 / P +22 ｜ Activity LOW ｜ 23D

📆 10-30 Forward Structure
存量OI: C 2.4k / P 2.2k，今日变化ΔOI: C +28 / P +68，平值价格ATM: C $8.20 / P $4.20 ｜ ATM IV 47.5%，净 delta 敞口 -1k shares
Top ΔOI: P 425 +25 ｜ P 430 +18 ｜ C 475 +16
仓位参考: Max Pain 435 ｜ Call Wall 450（+1.6%，弱）（OI 0.2k） ｜ Put Wall 455（+2.8%）（OI 0.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 47.5%｜历史 Rank 79%（近端代理）｜IV/RV 2.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,417 股

11-06（MEDIUM △）Top ΔOI: 420P +124 ｜ 450C +35
11-06（MEDIUM △）仓位参考: Max Pain 428 ｜ Call Wall 430（-2.9%，弱）（OI 0.1k） ｜ Put Wall 420（-5.1%，弱）（OI 0.2k）

11-13（Activity LOW）仓位参考: Max Pain 430 ｜ Call Wall 440（-0.6%，弱）（OI 0.1k） ｜ Put Wall 420（-5.1%，弱）（OI 81）

11-20（Activity LOW）仓位参考: Max Pain 400 ｜ Call Wall 420（-5.1%，弱）（OI 0.8k） ｜ Put Wall 410（-7.4%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 47.5% vs 11-06 38.4%（差 +9.2pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/ISRG_morning.json