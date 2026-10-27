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


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 373.20 → 收盘 391.62（+4.9%） ｜ 今日高 397.27 ｜ 低 383.73 ｜ 昨收 372.22 → 收盘 391.62（+5.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.88 | OI比 1.18 | ATM IV 43.0% | Skew 1.3pp | Term 0.90 | ExpMove ±2.6%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构正常（Term 0.90）｜保护溢价薄（Skew 1.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.88×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.18×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-28（2D）±2.6% ｜ 10-30（4D）±3.7% ｜ 11-02（7D）±4.1% ｜ 11-04（9D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 98,623,561 | GEX Change vs 上次快照 2,598,745 | Flip: Primary Flip: 363.55（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1180 / LOW 75 / INVALID 703
结构观察区: Primary Flip 363.55（全链重定价，覆盖 100%）
Call Wall 400（现价低于该位 2.1%）
最近结构参考: Call Wall 400（现价低于该位 2.1%）
量化视角： 正 Gamma（9862万，无历史分位）｜正 Gamma 增强（+260万）｜现价位于 Flip 上方 7.72%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 375（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 364（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 230.0P — Vol 2,019 | 最新价 $0.02 | OI 2752→21935 (ΔOI +19183张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19183张（+697.1% vs前日OI），连续性待观察（方向未知）
10-30 140.0P — Vol 120 | 最新价 $0.01 | OI 804→14512 (ΔOI +13708张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13708张（+1705.0% vs前日OI），连续性待观察（方向未知）
11-06 210.0P — Vol 3,174 | 最新价 $0.04 | OI 176→7055 (ΔOI +6879张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6879张（+3908.5% vs前日OI），连续性待观察（方向未知）
11-20 380.0C — Vol 1,875 | 最新价 $23.00 | OI 5422→10009 (ΔOI +4587张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4587张（+84.6% vs前日OI），连续性待观察（方向未知）
10-30 382.5C — Vol 1,763 | 最新价 $12.76 | OI 715→5281 (ΔOI +4566张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4566张（+638.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 48,923 张（Put 39,770 / Call 9,153），跨 3 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 10-28 Forward Structure
存量OI: C 21.6k / P 25.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.65 / P $5.44 ｜ ATM IV 43.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 375 ｜ Call Wall 375（-4.2%，弱）（OI 2.2k） ｜ Put Wall 385（-1.7%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 43.0%｜历史 Rank 18%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 372 ｜ Call Wall 400（+2.1%，弱）（OI 13.1k）

11-02（Activity LOW）仓位参考: Max Pain 378 ｜ Put Wall 380（-3.0%，弱）（OI 0.5k）

11-04（Activity LOW）仓位参考: Max Pain 380 ｜ Call Wall 400（+2.1%）（OI 0.4k） ｜ Put Wall 385（-1.7%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/TSLA_evening.json