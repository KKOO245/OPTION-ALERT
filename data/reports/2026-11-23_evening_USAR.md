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
🟡 **近现价集中开仓**: 11-27 7C ΔOI +769（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-27 7C ΔOI +2,842 占该期限总 OI 10.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 7.12 → 收盘 7.02（-1.4%） ｜ 今日高 7.19 ｜ 低 6.60 ｜ 昨收 6.27 → 收盘 7.02（+12.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.19 | OI比 0.23 | ATM IV 122.1% | Skew 20.8pp | Term 0.87 | ExpMove ±10.5%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价显著（Skew 20.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.23×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±10.5% ｜ 12-04（11D）±15.2% ｜ 12-11（18D）±21.1% ｜ 12-18（25D）±23.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,835,988 | GEX Change vs 上次快照 399,383 | Flip: Primary Flip: 6.36（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 217 / LOW 90 / INVALID 109
结构观察区: Primary Flip 6.36（全链重定价，覆盖 100%）
最近结构参考: Flip 6（现价高于该位 10.3%）
量化视角： 正 Gamma（184万，无历史分位）｜正 Gamma 增强（+40万）｜现价位于 Flip 上方 10.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 8（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 6（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 10.0C — Vol 290 | 最新价 $0.13 | OI 4105→20412 (ΔOI +16307张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16307张（+397.2% vs前日OI），连续性待观察（方向未知）
12-18 10.0P — Vol 105 | 最新价 $3.30 | OI 3387→19658 (ΔOI +16271张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16271张（+480.4% vs前日OI），连续性待观察（方向未知）
11-27 7.5C — Vol 1,363 | 最新价 $0.15 | OI 778→3620 (ΔOI +2842张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2842张（+365.3% vs前日OI），连续性待观察（方向未知）
11-27 7.0C — Vol 1,575 | 最新价 $0.35 | OI 894→1663 (ΔOI +769张) | ΔOI/Volume 48.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增769张（+86.0% vs前日OI），连续性待观察（方向未知）
11-27 6.5P — Vol 902 | 最新价 $0.17 | OI 264→868 (ΔOI +604张) | ΔOI/Volume 67.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增604张（+228.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,793 张（Put 16,875 / Call 19,918），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +3.9k / P +1.1k ｜ Activity HIGH ｜ 4D
12-04  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 11D
12-11  C -1 / P +84 ｜ Activity HIGH ｜ 18D
12-18  C +16.6k / P +16.4k ｜ Activity HIGH ｜ 25D

📆 11-27 Forward Structure
存量OI: C 22.7k / P 5.2k，今日变化ΔOI: C +3.9k / P +1.1k，平值价格ATM: C $0.35 / P $0.39 ｜ ATM IV 122.1%，净 delta 敞口 137k shares
Top ΔOI: C 7 +2,842 ｜ C 7 +769 ｜ P 6 +604
仓位参考: Max Pain 8 ｜ Call Wall 7.5（+6.8%，弱）（OI 3.6k） ｜ Put Wall 6.5（-7.4%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 122.1%｜历史 Rank 60%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 136,726 股

12-04（MEDIUM △）Top ΔOI: 6P +62
12-04（MEDIUM △）仓位参考: Max Pain 8 ｜ Call Wall 7.5（+6.8%，弱）（OI 0.3k） ｜ Put Wall 7（-0.3%）（OI 0.6k）

📆 12-11 Forward Structure
存量OI: C 5.4k / P 1.3k，今日变化ΔOI: C -1 / P +84，平值价格ATM: C $0.75 / P $0.73 ｜ ATM IV 111.5%，净 delta 敞口 -865 shares
仓位参考: Max Pain 8 ｜ Put Wall 7.5（+6.8%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 111.5%｜历史 Rank 60%（近端代理）｜IV/RV 1.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 865 股

📆 12-18 Forward Structure
存量OI: C 106.3k / P 77.7k，今日变化ΔOI: C +16.6k / P +16.4k，平值价格ATM: C $0.79 / P $0.84 ｜ ATM IV 111.1%，净 delta 敞口 -1.1M shares
Top ΔOI: C 10 +16,307 ｜ P 10 +16,271 ｜ C 7 +178
仓位参考: Max Pain 10 ｜ Put Wall 7（-0.3%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 111.1%｜历史 Rank 60%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 1,133,462 股

📅 事件差分（观察，非因果）: 11-27（4D）ATM IV 122.1% vs 12-04 112.2%（差 +9.9pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/USAR_evening.json