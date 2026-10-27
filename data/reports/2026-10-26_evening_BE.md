# 期权晚报 2026-10-26（快照 21:54 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 18.39 ↓5.5%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：无更新，来源自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 203.01 → 收盘 203.92（+0.4%） ｜ 今日高 210.86 ｜ 低 192.15 ｜ 昨收 193.30 → 收盘 203.92（+5.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 0.76 | ATM IV 97.2% | Skew -0.5pp | Term 0.81 | ExpMove ±8.2%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（4D）±8.2% ｜ 11-06（11D）±12.1% ｜ 11-13（18D）±15.5% ｜ 11-20（25D）±17.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,721,734 | GEX Change vs 上次快照 1,515,322 | Flip: Primary Flip: 216.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 571 / LOW 71 / INVALID 238
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 216.22（全链重定价，覆盖 100%）
Put Wall 190（弱结构｜现价高于该位 7.3%）
最近结构参考: Flip 216（现价低于该位 5.7%）
量化视角： 负 Gamma（372万，无历史分位）｜负 Gamma 缓解（+152万）｜现价位于 Flip 下方 5.69%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall，弱结构）；上方 215（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 216（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 230.0C — Vol 5,600 | 最新价 $1.45 | OI 1437→3277 (ΔOI +1840张) | ΔOI/Volume 32.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1840张（+128.0% vs前日OI），连续性待观察（方向未知）
10-30 195.0C — Vol 1,238 | 最新价 $13.35 | OI 11→1759 (ΔOI +1748张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1748张（+15890.9% vs前日OI），连续性待观察（方向未知）
10-30 200.0C — Vol 4,934 | 最新价 $9.80 | OI 254→1890 (ΔOI +1636张) | ΔOI/Volume 33.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1636张（+644.1% vs前日OI），连续性待观察（方向未知）
10-30 165.0C — Vol 11 | 最新价 $41.49 | OI 3→1505 (ΔOI +1502张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1502张（+50066.7% vs前日OI），连续性待观察（方向未知）
11-06 200.0C — Vol 502 | 最新价 $13.65 | OI 19→1450 (ΔOI +1431张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1431张（+7531.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,157 张（Put 0 / Call 8,157），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-30 Forward Structure
存量OI: C 52.3k / P 40.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $7.85 / P $8.90 ｜ ATM IV 97.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 215 ｜ Call Wall 220（+7.9%，弱）（OI 3.5k） ｜ Put Wall 190（-6.8%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 97.2%｜历史 Rank 60%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 235 ｜ Call Wall 200（-1.9%，弱）（OI 1.4k） ｜ Put Wall 215（+5.4%，弱）（OI 0.6k）

11-13（Activity LOW）仓位参考: Max Pain 245 ｜ Call Wall 220（+7.9%，弱）（OI 0.3k） ｜ Put Wall 200（-1.9%，弱）（OI 0.6k）

11-20（Activity LOW）仓位参考: Max Pain 235 ｜ Call Wall 220（+7.9%，弱）（OI 1.8k） ｜ Put Wall 200（-1.9%，弱）（OI 5.3k）

📅 事件差分（观察，非因果）: 10-30（4D）ATM IV 97.2% vs 11-06 87.6%（差 +9.6pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/BE_evening.json