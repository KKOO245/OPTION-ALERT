# 期权晚报 2026-10-12（快照 16:40 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-14 385C ΔOI +1,615（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-14 315P ΔOI +4,661 占该期限总 OI 11.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 382.61 → 收盘 378.03（-1.2%） ｜ 今日高 382.61 ｜ 低 377.58 ｜ 昨收 382.70 → 收盘 378.03（-1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.78 | OI比 0.69 | ATM IV 16.0% | Skew -30.9pp | Term 2.61 | ExpMove ±2.1%（近端） | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 2.61）｜Put 保护异常便宜（Skew -30.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.69）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-14（2D）±2.1% ｜ 10-16（4D）±3.6% ｜ 10-19（7D）±4.0% ｜ 10-23（11D）±7.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 52,464,333 | GEX Change vs 上次快照 -28,866,863 | Flip: Primary Flip: 366.02（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 1137 / LOW 147 / INVALID 586
结构观察区: Primary Flip 366.02（全链重定价，覆盖 93%）
Call Wall 400（现价低于该位 5.5%）
最近结构参考: Flip 366（现价高于该位 3.3%）
量化视角： 正 Gamma（5246万，无历史分位）｜正 Gamma 减弱（2887万）｜现价位于 Flip 上方 3.28%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 380（MaxPain，仅结算参考） / 400（Call Wall）。
• Gamma 区域：切换参考 366（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 140.0P — Vol 23,000（Yahoo补） | 最新价 $0.01 | OI 983→23928 (ΔOI +22945张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22945张（+2334.2% vs前日OI），连续性待观察（方向未知）
10-16 235.0P — Vol 7 | 最新价 $0.03 | OI 1285→20195 (ΔOI +18910张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18910张（+1471.6% vs前日OI），连续性待观察（方向未知）
10-16 215.0P — Vol 58 | 最新价 $0.01 | OI 1055→14904 (ΔOI +13849张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13849张（+1312.7% vs前日OI），连续性待观察（方向未知）
量化视角： 3 个事件合计 ΔOI ≈ 55,704 张（Put 55,704 / Call 0），跨 1 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-14  C +8.3k / P +10.7k ｜ Activity HIGH ｜ 2D
10-16  C +32.8k / P +83.7k ｜ Activity HIGH ｜ 4D
10-19  C +7.6k / P +1.6k ｜ Activity HIGH ｜ 7D
10-23  C +6.6k / P +4.4k ｜ Activity HIGH ｜ 11D

📆 10-14 Forward Structure
存量OI: C 19.9k / P 20.5k，今日变化ΔOI: C +8.3k / P +10.7k，平值价格ATM: C $4.31 / P $3.73 ｜ ATM IV 35.9%，净 delta 敞口 -138k shares
Top ΔOI: C 385 +1,615 ｜ C 390 +1,472
仓位参考: Max Pain 378 ｜ Call Wall 400（+5.8%，弱）（OI 3.1k） ｜ Put Wall 370（-2.1%，弱）（OI 1.4k）
量化解读： 存量两侧均衡｜ATM IV 35.9%｜历史 Rank 0%（近端代理）｜IV/RV 1.26×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 138,350 股

📆 10-16 Forward Structure
存量OI: C 369.2k / P 378.2k，今日变化ΔOI: C +32.8k / P +83.7k，平值价格ATM: C $7.25 / P $6.38 ｜ ATM IV 42.8%，净 delta 敞口 38k shares
Top ΔOI: P 235 +18,910
仓位参考: Max Pain 370 ｜ Call Wall 400（+5.8%，弱）（OI 24.3k） ｜ Put Wall 380（+0.5%，弱）（OI 15.4k）
量化解读： 存量两侧均衡｜ATM IV 42.8%｜历史 Rank 0%（近端代理）｜IV/RV 1.50×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 37,751 股

📆 10-19 Forward Structure
存量OI: C 14.3k / P 4.7k，今日变化ΔOI: C +7.6k / P +1.6k，平值价格ATM: C $7.90 / P $7.05 ｜ ATM IV 35.8%，净 delta 敞口 -34k shares
Top ΔOI: C 415 +185
仓位参考: Max Pain 378 ｜ Call Wall 400（+5.8%，弱）（OI 1.7k） ｜ Put Wall 360（-4.8%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 35.8%｜历史 Rank 0%（近端代理）｜IV/RV 1.26×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 34,228 股

📆 10-23 Forward Structure
存量OI: C 62.6k / P 42.8k，今日变化ΔOI: C +6.6k / P +4.4k，平值价格ATM: C $14.20 / P $12.95 ｜ ATM IV 51.5%，净 delta 敞口 87k shares
Top ΔOI: C 180 +828 ｜ C 410 +692
仓位参考: Max Pain 370 ｜ Call Wall 400（+5.8%，弱）（OI 5.4k） ｜ Put Wall 360（-4.8%，弱）（OI 2.4k）
量化解读： 存量 Call 重｜ATM IV 51.5%｜历史 Rank 0%（近端代理）｜IV/RV 1.81×（近似）｜净 delta 敞口 正 87,045 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/TSLA_evening.json