# 期权晚报 2026-09-15（快照 16:40 ET）

📊 市场环境

SPY $757.39 ｜ QQQ $704.54
VIX 17.20 ↑0.6%（5D +9.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：无更新，来源自 2026-09-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,569.71 → 收盘 1,530.90（-2.5%） ｜ 今日高 1579.99 ｜ 低 1509.14 ｜ 昨收 1,551.99 → 收盘 1,530.90（-1.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.80 | OI比 1.16 | ATM IV 62.9% | Skew -1.4pp | Term 1.07 | ExpMove ±5.3% | Rank 19%
量化视角： IV 历史低位（Rank 19%，期权偏便宜）｜期限结构正常（Term 1.07）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.16×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) nan | GEX Change vs 上次快照 nan | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: VALID 2064 / LOW 466 / INVALID 217
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 1,500（弱结构｜现价高于该位 2.1%）
最近结构参考: Put Wall 1500（现价高于该位 2.1%）
量化视角： 正 Gamma（nan万，无历史分位）｜GEX 变化（nan万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,500（Put Wall，弱结构） / 1,500（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 1400.0P — Vol 2,602 | 最新价 $4.60 | OI 2028→4093 (ΔOI +2065张) | ΔOI/Volume 79.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2065张（+101.8% vs前日OI），连续性待观察（方向未知）
09-18 1750.0C — Vol 2,674 | 最新价 $2.05 | OI 1729→3451 (ΔOI +1722张) | ΔOI/Volume 64.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1722张（+99.6% vs前日OI），连续性待观察（方向未知）
10-16 1460.0P — Vol 24 | 最新价 $85.00 | OI 184→925 (ΔOI +741张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增741张（+402.7% vs前日OI），连续性待观察（方向未知）
09-18 1120.0P — Vol 2 | 最新价 $0.11 | OI 287→953 (ΔOI +666张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增666张（+232.1% vs前日OI），连续性待观察（方向未知）
09-18 2000.0C — Vol 862 | 最新价 $0.20 | OI 3024→3658 (ΔOI +634张) | ΔOI/Volume 73.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增634张（+21.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,828 张（Put 3,472 / Call 2,356），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $7M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-15/SNDK_evening.json