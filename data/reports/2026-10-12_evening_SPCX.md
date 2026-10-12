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
🟡 **近现价集中开仓**: 10-14 162C ΔOI +2,643（距现价 -0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 164.70 → 收盘 163.42（-0.8%） ｜ 今日高 167.07 ｜ 低 160.85 ｜ 昨收 162.57 → 收盘 163.42（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.42 | OI比 0.48 | ATM IV 47.2% | Skew -15.7pp | Term 1.08 | ExpMove ±2.9%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -15.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-14（2D）±2.9% ｜ 10-16（4D）±4.0% ｜ 10-19（7D）±4.7% ｜ 10-21（9D）±5.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 87,145,894 | GEX Change vs 上次快照 -23,393,791 | Flip: Primary Flip: 155.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 680 / LOW 201 / INVALID 515
结构观察区: Primary Flip 155.37（全链重定价，覆盖 94%）
最近结构参考: Flip 155（现价高于该位 5.2%）
量化视角： 正 Gamma（8715万，无历史分位）｜正 Gamma 减弱（2339万）｜现价位于 Flip 上方 5.18%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 155（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 165.0C — Vol 37,093 | 最新价 $2.63 | OI 14143→17606 (ΔOI +3463张) | ΔOI/Volume 9.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3463张（+24.5% vs前日OI），连续性待观察（方向未知）
10-16 175.0C — Vol 11,801 | 最新价 $0.44 | OI 15750→19201 (ΔOI +3451张) | ΔOI/Volume 29.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3451张（+21.9% vs前日OI），连续性待观察（方向未知）
10-16 162.5C — Vol 10,506 | 最新价 $3.80 | OI 6510→9688 (ΔOI +3178张) | ΔOI/Volume 30.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3178张（+48.8% vs前日OI），连续性待观察（方向未知）
10-16 167.5C — Vol 14,533 | 最新价 $1.70 | OI 4757→7917 (ΔOI +3160张) | ΔOI/Volume 21.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3160张（+66.4% vs前日OI），连续性待观察（方向未知）
量化视角： 4 个事件合计 ΔOI ≈ 13,252 张（Put 0 / Call 13,252），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-14  C +7.7k / P +3.6k ｜ Activity HIGH ｜ 2D
10-16  C +20.6k / P +19.6k ｜ Activity HIGH ｜ 4D
10-19  C +2.1k / P +0.7k ｜ Activity HIGH ｜ 7D
10-21  C +1.2k / P +0.7k ｜ Activity HIGH ｜ 9D

📆 10-14 Forward Structure
存量OI: C 18.9k / P 10.2k，今日变化ΔOI: C +7.7k / P +3.6k，平值价格ATM: C $2.77 / P $1.90 ｜ ATM IV 47.9%，净 delta 敞口 285k shares
Top ΔOI: C 162 +2,643 ｜ C 165 +1,185 ｜ P 160 +964
仓位参考: Max Pain 162 ｜ Call Wall 162.5（-0.6%，弱）（OI 3.1k） ｜ Put Wall 160（-2.1%，弱）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 47.9%｜历史 Rank 18%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 284,996 股

📆 10-16 Forward Structure
存量OI: C 378.7k / P 407.7k，今日变化ΔOI: C +20.6k / P +19.6k，平值价格ATM: C $3.80 / P $2.76 ｜ ATM IV 47.9%，净 delta 敞口 262k shares
Top ΔOI: C 165 +3,463 ｜ C 175 +3,451 ｜ C 162 +3,178
仓位参考: Max Pain 150 ｜ Call Wall 170（+4.0%，弱）（OI 31.0k） ｜ Put Wall 150（-8.2%，弱）（OI 25.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.9%｜历史 Rank 18%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 262,339 股

📆 10-19 Forward Structure
存量OI: C 9.1k / P 4.7k，今日变化ΔOI: C +2.1k / P +0.7k，平值价格ATM: C $4.25 / P $3.40 ｜ ATM IV 41.5%，净 delta 敞口 66k shares
Top ΔOI: C 167 +615 ｜ C 170 +444 ｜ C 160 +347
仓位参考: Max Pain 165 ｜ Call Wall 167.5（+2.5%，弱）（OI 0.9k） ｜ Put Wall 165（+1.0%）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 41.5%｜历史 Rank 18%（近端代理）｜IV/RV 0.87×（近似）｜净 delta 敞口 正 66,064 股

📆 10-21 Forward Structure
存量OI: C 3.9k / P 2.1k，今日变化ΔOI: C +1.2k / P +0.7k，平值价格ATM: C $4.90 / P $4.05 ｜ ATM IV 43.3%，净 delta 敞口 28k shares
Top ΔOI: C 170 +461 ｜ C 165 +154
仓位参考: Max Pain 162 ｜ Call Wall 170（+4.0%）（OI 0.7k） ｜ Put Wall 162.5（-0.6%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 43.3%｜历史 Rank 18%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 27,826 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/SPCX_evening.json