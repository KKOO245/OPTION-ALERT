# 期权晚报 2026-10-28（快照 16:40 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 16.91 ↓3.5%（5D +1.4%） ｜ Vol Regime: NORMAL
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
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **事件差分**: 10-30（2D）ATM IV 113.5% vs 11-06 95.7%（差 +17.8pp），覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 187C ΔOI +689（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 173.65 → 收盘 182.34（+5.0%） ｜ 今日高 182.72 ｜ 低 168.92 ｜ 昨收 170.47 → 收盘 182.34（+7.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.60 | OI比 0.54 | ATM IV 113.5% | Skew -1.8pp | Term 0.83 | ExpMove ±6.7%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.60×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±6.7% ｜ 11-06（9D）±12.1% ｜ 11-13（16D）±17.3% ｜ 11-20（23D）±19.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,996,120 | GEX Change vs 上次快照 6,584,577 | Flip: Primary Flip: 168.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 631 / LOW 52 / INVALID 171
结构观察区: Primary Flip 168.47（全链重定价，覆盖 100%）
最近结构参考: Flip 168（现价高于该位 8.2%）
量化视角： 正 Gamma（1000万，无历史分位）｜正 Gamma 增强（+658万）｜现价位于 Flip 上方 8.23%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 175（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 168（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +2.5k / P +1.3k ｜ Activity MEDIUM △ ｜ 2D
11-06  C +5.0k / P +3.7k ｜ Activity HIGH ｜ 9D
11-13  C +0.4k / P +0.8k ｜ Activity HIGH ｜ 16D
11-20  C +0.2k / P +2.0k ｜ Activity HIGH ｜ 23D

📆 10-30 Forward Structure
存量OI: C 92.8k / P 49.9k，今日变化ΔOI: C +2.5k / P +1.3k，平值价格ATM: C $6.11 / P $6.10 ｜ ATM IV 113.5%，净 delta 敞口 48k shares
Top ΔOI: C 195 +965 ｜ C 200 +951 ｜ C 187 +689
仓位参考: Max Pain 175 ｜ Call Wall 200（+9.7%，弱）（OI 7.0k） ｜ Put Wall 170（-6.8%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 113.5%｜历史 Rank 65%（近端代理）｜IV/RV 1.28×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 48,346 股

📆 11-06 Forward Structure
存量OI: C 46.0k / P 29.3k，今日变化ΔOI: C +5.0k / P +3.7k，平值价格ATM: C $11.00 / P $10.98 ｜ ATM IV 95.7%，净 delta 敞口 128k shares
Top ΔOI: C 200 +949 ｜ C 170 +895 ｜ P 220 +864
仓位参考: Max Pain 198 ｜ Call Wall 200（+9.7%，弱）（OI 2.5k） ｜ Put Wall 200（+9.7%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜ATM IV 95.7%｜历史 Rank 65%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 127,529 股

📆 11-13 Forward Structure
存量OI: C 18.3k / P 17.9k，今日变化ΔOI: C +0.4k / P +0.8k，平值价格ATM: C $15.37 / P $16.10 ｜ ATM IV 104.4%，净 delta 敞口 -7k shares
Top ΔOI: C 170 +209 ｜ C 165 -137
仓位参考: Max Pain 190 ｜ Call Wall 200（+9.7%，弱）（OI 2.0k） ｜ Put Wall 165（-9.5%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 104.4%｜历史 Rank 65%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 6,574 股

📆 11-20 Forward Structure
存量OI: C 91.5k / P 106.3k，今日变化ΔOI: C +0.2k / P +2.0k，平值价格ATM: C $17.98 / P $17.95 ｜ ATM IV 99.4%，净 delta 敞口 14k shares
Top ΔOI: P 125 +808
仓位参考: Max Pain 195 ｜ Call Wall 200（+9.7%，弱）（OI 6.1k） ｜ Put Wall 200（+9.7%，弱）（OI 4.9k）
量化解读： 存量两侧均衡｜ATM IV 99.4%｜历史 Rank 65%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 13,622 股

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 113.5% vs 11-06 95.7%（差 +17.8pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/NBIS_evening.json