# 期权晚报 2026-11-09（快照 16:40 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-11 380C ΔOI +652（距现价 +0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 120P ΔOI +53,822 占该期限总 OI 17.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 360.25 → 收盘 378.05（+4.9%） ｜ 今日高 382.20 ｜ 低 360.02 ｜ 昨收 358.22 → 收盘 378.05（+5.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.86 | OI比 0.78 | ATM IV 26.5% | Skew -2.5pp | Term 1.70 | ExpMove ±3.1%（近端） | Rank 2%
量化视角： IV 历史低位（Rank 2%，期权偏便宜）｜期限结构正常偏陡（Term 1.70）｜Put 保护异常便宜（Skew -2.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.86×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-11（2D）±3.1% ｜ 11-13（4D）±4.3% ｜ 11-16（7D）±4.8% ｜ 11-18（9D）±5.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 74,055,637 | GEX Change vs 上次快照 4,495,278 | Flip: Primary Flip: 355.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 1396 / LOW 217 / INVALID 1029
结构观察区: Primary Flip 355.03（全链重定价，覆盖 95%）
Call Wall 400（弱结构｜现价低于该位 5.5%）
最近结构参考: Call Wall 400（现价低于该位 5.5%）
量化视角： 正 Gamma（7406万，无历史分位）｜正 Gamma 增强（+450万）｜现价位于 Flip 上方 6.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 362（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 355（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 120.0P — Vol 2 | 最新价 $0.01 | OI 349→54171 (ΔOI +53822张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增53822张（+15421.8% vs前日OI），连续性待观察（方向未知）
11-13 200.0P — Vol 439 | 最新价 $0.02 | OI 2365→19277 (ΔOI +16912张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16912张（+715.1% vs前日OI），连续性待观察（方向未知）
11-13 180.0P — Vol 406 | 最新价 $0.01 | OI 238→15132 (ΔOI +14894张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14894张（+6258.0% vs前日OI），连续性待观察（方向未知）
11-13 220.0P — Vol 577 | 最新价 $0.04 | OI 1417→15636 (ΔOI +14219张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14219张（+1003.5% vs前日OI），连续性待观察（方向未知）
11-13 380.0C — Vol 7,040 | 最新价 $7.30 | OI 2522→7571 (ΔOI +5049张) | ΔOI/Volume 71.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5049张（+200.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 104,896 张（Put 99,847 / Call 5,049），跨 1 个期限｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-11  C +3.7k / P +7.1k ｜ Activity HIGH ｜ 2D
11-13  C +35.4k / P +128.1k ｜ Activity HIGH ｜ 4D
11-16  C +2.7k / P +1.2k ｜ Activity HIGH ｜ 7D
11-18  C +0.6k / P +0.7k ｜ Activity HIGH ｜ 9D

📆 11-11 Forward Structure
存量OI: C 30.3k / P 25.8k，今日变化ΔOI: C +3.7k / P +7.1k，平值价格ATM: C $6.21 / P $5.50 ｜ ATM IV 52.5%，净 delta 敞口 187k shares
Top ΔOI: C 380 +652
仓位参考: Max Pain 365 ｜ Call Wall 390（+3.2%，弱）（OI 1.9k） ｜ Put Wall 360（-4.8%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.5%｜历史 Rank 2%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 186,660 股

📆 11-13 Forward Structure
存量OI: C 124.1k / P 187.8k，今日变化ΔOI: C +35.4k / P +128.1k，平值价格ATM: C $8.58 / P $7.80 ｜ ATM IV 51.5%，净 delta 敞口 1.7M shares
Top ΔOI: P 120 +53,822
仓位参考: Max Pain 360 ｜ Call Wall 362.5（-4.1%，弱）（OI 7.9k）
量化解读： 存量 Put 重｜ATM IV 51.5%｜历史 Rank 2%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,726,625 股

📆 11-16 Forward Structure
存量OI: C 11.9k / P 6.1k，今日变化ΔOI: C +2.7k / P +1.2k，平值价格ATM: C $9.60 / P $8.65 ｜ ATM IV 44.4%，净 delta 敞口 58k shares
Top ΔOI: C 400 +364
仓位参考: Max Pain 368 ｜ Call Wall 400（+5.8%，弱）（OI 0.8k） ｜ Put Wall 380（+0.5%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 44.4%｜历史 Rank 2%（近端代理）｜IV/RV 0.80×（近似）｜净 delta 敞口 正 58,167 股

📆 11-18 Forward Structure
存量OI: C 4.7k / P 3.5k，今日变化ΔOI: C +0.6k / P +0.7k，平值价格ATM: C $12.00 / P $10.22 ｜ ATM IV 45.4%，净 delta 敞口 27k shares
Top ΔOI: C 387 -150 ｜ C 370 +121
仓位参考: Max Pain 355 ｜ Call Wall 380（+0.5%，弱）（OI 0.3k） ｜ Put Wall 350（-7.4%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 45.4%｜历史 Rank 2%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 正 26,652 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/TSLA_evening.json