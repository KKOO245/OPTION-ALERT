# 期权晚报 2026-11-23（快照 16:40 ET）

📊 市场环境

SPY $722.29 ｜ QQQ $651.03
VIX 26.62 ↓25.8%（5D +16.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.4 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 109C ΔOI +4,357（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 12-11 65P ΔOI +1,027 占该期限总 OI 12.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 109.56 → 收盘 108.78（-0.7%） ｜ 今日高 111.40 ｜ 低 107.20 ｜ 昨收 101.97 → 收盘 108.78（+6.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.69 | OI比 0.57 | ATM IV 80.7% | Skew 8.7pp | Term 0.90 | ExpMove ±6.6%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜保护溢价显著（Skew 8.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.57）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.69×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.57×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±6.6% ｜ 12-04（11D）±10.7% ｜ 12-11（18D）±13.7% ｜ 12-18（25D）±15.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,399,557 | GEX Change vs 上次快照 521,358 | Flip: Primary Flip: 103.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 374 / LOW 219 / INVALID 395
结构观察区: Primary Flip 103.69（全链重定价，覆盖 100%）
Put Wall 110（弱结构｜现价低于该位 1.1%）
最近结构参考: Put Wall 110（现价低于该位 1.1%）
量化视角： 正 Gamma（840万，无历史分位）｜正 Gamma 增强（+52万）｜现价位于 Flip 上方 4.91%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 110（Put Wall，弱结构） / 110（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 104（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 109.0C — Vol 625 | 最新价 $3.40 | OI 6→4363 (ΔOI +4357张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4357张（+72616.7% vs前日OI），连续性待观察（方向未知）
11-27 114.0C — Vol 792 | 最新价 $1.56 | OI 3705→7109 (ΔOI +3404张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3404张（+91.9% vs前日OI），连续性待观察（方向未知）
11-27 110.0C — Vol 1,135 | 最新价 $3.00 | OI 253→2600 (ΔOI +2347张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2347张（+927.7% vs前日OI），连续性待观察（方向未知）
11-27 100.0P — Vol 957 | 最新价 $0.92 | OI 1309→2817 (ΔOI +1508张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1508张（+115.2% vs前日OI），连续性待观察（方向未知）
11-27 95.0P — Vol 162 | 最新价 $0.41 | OI 196→1518 (ΔOI +1322张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1322张（+674.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 12,938 张（Put 2,830 / Call 10,108），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +16.4k / P +11.5k ｜ Activity HIGH ｜ 4D
12-04  C +0.6k / P +1.4k ｜ Activity HIGH ｜ 11D
12-11  C +0.4k / P +1.2k ｜ Activity HIGH ｜ 18D
12-18  C +3.6k / P -0.5k ｜ Activity HIGH ｜ 25D

📆 11-27 Forward Structure
存量OI: C 57.1k / P 32.3k，今日变化ΔOI: C +16.4k / P +11.5k，平值价格ATM: C $3.40 / P $3.77 ｜ ATM IV 80.7%，净 delta 敞口 487k shares
Top ΔOI: C 109 +4,357 ｜ C 114 +3,404 ｜ C 110 +2,347
仓位参考: Max Pain 110 ｜ Call Wall 114（+4.8%，弱）（OI 7.1k） ｜ Put Wall 100（-8.1%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 80.7%｜历史 Rank 61%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 487,116 股

📆 12-04 Forward Structure
存量OI: C 10.5k / P 13.7k，今日变化ΔOI: C +0.6k / P +1.4k，平值价格ATM: C $5.55 / P $6.11 ｜ ATM IV 80.8%，净 delta 敞口 9k shares
Top ΔOI: P 102 +122
仓位参考: Max Pain 133 ｜ Put Wall 100（-8.1%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜ATM IV 80.8%｜历史 Rank 61%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,647 股

📆 12-11 Forward Structure
存量OI: C 3.6k / P 4.9k，今日变化ΔOI: C +0.4k / P +1.2k，平值价格ATM: C $7.35 / P $7.50 ｜ ATM IV 80.6%，净 delta 敞口 12k shares
Top ΔOI: C 110 +115
仓位参考: Max Pain 130 ｜ Call Wall 110（+1.1%，弱）（OI 0.2k） ｜ Put Wall 100（-8.1%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 80.6%｜历史 Rank 61%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 11,851 股

📆 12-18 Forward Structure
存量OI: C 138.8k / P 54.3k，今日变化ΔOI: C +3.6k / P -0.5k，平值价格ATM: C $8.70 / P $8.55 ｜ ATM IV 77.2%，净 delta 敞口 74k shares
Top ΔOI: P 80 -798
仓位参考: Max Pain 135 ｜ Put Wall 110（+1.1%）（OI 7.9k）
量化解读： 存量 Call 重｜ATM IV 77.2%｜历史 Rank 61%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 73,772 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/COIN_evening.json