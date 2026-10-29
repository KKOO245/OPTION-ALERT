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
🔴 **事件差分**: 10-30（2D）ATM IV 111.3% vs 11-06 94.8%（差 +16.5pp），覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 10C ΔOI +2,084（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 10.40 → 今开 10.41（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 10.43 ｜ 低 9.85

Options: P/C成交量 0.78 | OI比 0.37 | ATM IV 111.3% | Skew -8.5pp | Term 0.81 | ExpMove ±6.3%（近端） | Rank 44%
量化视角： IV 中性（Rank 44%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.37）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.37×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±6.3% ｜ 11-06（9D）±12.8% ｜ 11-13（16D）±15.4% ｜ 11-20（23D）±18.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,637,027 | GEX Change vs 上次快照 1,302,801 | Flip: Primary Flip: 9.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 197 / LOW 77 / INVALID 146
结构观察区: Primary Flip 9.29（全链重定价，覆盖 100%）
Put Wall 10（弱结构｜现价低于该位 0.3%）
最近结构参考: Put Wall 10（现价低于该位 0.3%）
量化视角： 正 Gamma（364万，无历史分位）｜正 Gamma 增强（+130万）｜现价位于 Flip 上方 7.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 10.0C — Vol 7,985 | 最新价 $0.63 | OI 3026→5110 (ΔOI +2084张) | ΔOI/Volume 26.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2084张（+68.9% vs前日OI），连续性待观察（方向未知）
10-30 11.0C — Vol 3,452 | 最新价 $0.18 | OI 2936→4748 (ΔOI +1812张) | ΔOI/Volume 52.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1812张（+61.7% vs前日OI），连续性待观察（方向未知）
11-20 13.0C — Vol 1,724 | 最新价 $0.33 | OI 779→2297 (ΔOI +1518张) | ΔOI/Volume 88.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1518张（+194.9% vs前日OI），连续性待观察（方向未知）
10-30 10.0P — Vol 1,892 | 最新价 $0.22 | OI 627→1986 (ΔOI +1359张) | ΔOI/Volume 71.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1359张（+216.8% vs前日OI），连续性待观察（方向未知）
10-30 11.5C — Vol 1,309 | 最新价 $0.09 | OI 2930→3710 (ΔOI +780张) | ΔOI/Volume 59.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增780张（+26.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,553 张（Put 1,359 / Call 6,194），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +5.5k / P +1.5k ｜ Activity HIGH ｜ 2D
11-06  C +1.6k / P +0.1k ｜ Activity HIGH ｜ 9D
11-13  C +1.0k / P +17 ｜ Activity HIGH ｜ 16D
11-20  C +3.9k / P +0.3k ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 29.1k / P 10.8k，今日变化ΔOI: C +5.5k / P +1.5k，平值价格ATM: C $0.32 / P $0.31 ｜ ATM IV 111.3%，净 delta 敞口 122k shares
Top ΔOI: C 10 +2,084 ｜ P 10 +1,359
仓位参考: Max Pain 10 ｜ Call Wall 10（+0.3%，弱）（OI 5.1k） ｜ Put Wall 9（-9.7%）（OI 3.9k）
量化解读： 存量 Call 重｜ATM IV 111.3%｜历史 Rank 44%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 122,219 股

📆 11-06 Forward Structure
存量OI: C 8.1k / P 4.3k，今日变化ΔOI: C +1.6k / P +0.1k，平值价格ATM: C $0.61 / P $0.67 ｜ ATM IV 94.8%，净 delta 敞口 45k shares
Top ΔOI: C 10 +486
仓位参考: Max Pain 10 ｜ Call Wall 10.5（+5.3%，弱）（OI 0.9k） ｜ Put Wall 9（-9.7%）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 94.8%｜历史 Rank 44%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 45,348 股

📆 11-13 Forward Structure
存量OI: C 4.9k / P 2.7k，今日变化ΔOI: C +1.0k / P +17，平值价格ATM: C $0.82 / P $0.72 ｜ ATM IV 99.0%，净 delta 敞口 37k shares
仓位参考: Max Pain 10 ｜ Call Wall 9（-9.7%，弱）（OI 0.6k） ｜ Put Wall 9（-9.7%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 99.0%｜历史 Rank 44%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,606 股

11-20（MEDIUM △）仓位参考: Max Pain 13 ｜ Call Wall 9.5（-4.7%，弱）（OI 1.4k） ｜ Put Wall 10（+0.3%，弱）（OI 6.3k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 111.3% vs 11-06 94.8%（差 +16.5pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/USAR_morning.json