# 期权晚报 2026-11-10（快照 16:40 ET）

📊 市场环境

SPY $749.92 ｜ QQQ $674.76
VIX 19.46 ↓2.3%（5D -6.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **事件差分**: 11-11（1D）ATM IV 47.5% vs 11-13 0.0%（差 +47.5pp），覆盖 Core Inflation Rate MoM、Inflation Rate MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 11-16 450C ΔOI +4,921 占该期限总 OI 15.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 370.54 → 收盘 379.78（+2.5%） ｜ 今日高 380.00 ｜ 低 370.43 ｜ 昨收 378.05 → 收盘 379.78（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.78 | OI比 1.21 | ATM IV 47.5% | Skew 4.6pp | Term 0.67 | ExpMove ±2.0%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构倒挂（Term 0.67，近月 IV 高于远月）｜保护溢价中性（Skew 4.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.21×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-11（1D）±2.0% ｜ 11-13（3D）±0.0% ｜ 11-16（6D）±4.3% ｜ 11-18（8D）±5.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 66,830,608 | GEX Change vs 上次快照 8,850,926 | Flip: Primary Flip: 364.27（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1294 / LOW 205 / INVALID 1089
结构观察区: Primary Flip 364.27（全链重定价，覆盖 99%）
Call Wall 400（现价低于该位 5.1%）
最近结构参考: Flip 364（现价高于该位 4.3%）
量化视角： 正 Gamma（6683万，无历史分位）｜正 Gamma 增强（+885万）｜现价位于 Flip 上方 4.26%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 372（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 364（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-11  C +15.6k / P +29.9k ｜ Activity HIGH ｜ 1D
11-13  C +28.8k / P +35.5k ｜ Activity HIGH ｜ 3D
11-16  C +9.3k / P +4.2k ｜ Activity HIGH ｜ 6D
11-18  C +1.2k / P +1.6k ｜ Activity HIGH ｜ 8D

📆 11-11 Forward Structure
存量OI: C 45.9k / P 55.7k，今日变化ΔOI: C +15.6k / P +29.9k，平值价格ATM: C $3.65 / P $4.00 ｜ ATM IV 47.5%，净 delta 敞口 -36k shares
Top ΔOI: P 345 +7,290 ｜ C 400 +2,228 ｜ P 350 +1,684
仓位参考: Max Pain 372 ｜ Call Wall 400（+5.3%，弱）（OI 4.1k） ｜ Put Wall 345（-9.2%）（OI 7.7k）
量化解读： 存量 Put 重｜ATM IV 47.5%｜历史 Rank 34%（近端代理）｜IV/RV 0.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 36,097 股

📆 11-13 Forward Structure
存量OI: C 152.8k / P 223.3k，今日变化ΔOI: C +28.8k / P +35.5k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 0.0%，净 delta 敞口 117k shares
Top ΔOI: C 400 +5,493
仓位参考: Max Pain 362 ｜ Call Wall 400（+5.3%，弱）（OI 11.7k）
量化解读： 存量 Put 重｜净 delta 敞口 正 116,904 股

📆 11-16 Forward Structure
存量OI: C 21.2k / P 10.3k，今日变化ΔOI: C +9.3k / P +4.2k，平值价格ATM: C $8.10 / P $8.20 ｜ ATM IV 41.8%，净 delta 敞口 19k shares
仓位参考: Max Pain 370 ｜ Call Wall 400（+5.3%，弱）（OI 1.2k） ｜ Put Wall 380（+0.1%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 41.8%｜历史 Rank 34%（近端代理）｜IV/RV 0.72×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 18,630 股

📆 11-18 Forward Structure
存量OI: C 5.8k / P 5.1k，今日变化ΔOI: C +1.2k / P +1.6k，平值价格ATM: C $10.10 / P $10.32 ｜ ATM IV 46.1%，净 delta 敞口 -30k shares
Top ΔOI: C 400 +198 ｜ C 410 +195 ｜ P 360 +130
仓位参考: Max Pain 368 ｜ Call Wall 400（+5.3%，弱）（OI 0.4k） ｜ Put Wall 350（-7.8%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 46.1%｜历史 Rank 34%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 负 29,789 股

📅 事件差分（观察，非因果）: 11-11（1D）ATM IV 47.5% vs 11-13 0.0%（差 +47.5pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/TSLA_evening.json