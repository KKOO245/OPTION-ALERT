# 期权晚报 2026-09-14（快照 16:48 ET）

📊 市场环境

SPY $760.88 ｜ QQQ $709.18
VIX 17.10 ↑8.0%（5D +11.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.9 ｜ 实际 待公布 ｜ 前值 -0.6
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 3.75
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 15.28 → 收盘 15.71（+2.8%） ｜ 今日高 16.07 ｜ 低 15.25 ｜ 昨收 15.56 → 收盘 15.71（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.34 | OI比 0.54 | ATM IV 81.9% | Skew -6.2pp | Term 0.97 | ExpMove ±6.8%（近端） | Rank 4%
量化视角： IV 历史低位（Rank 4%，期权偏便宜）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -6.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（4D）±6.8% ｜ 09-25（11D）±10.5% ｜ 10-02（18D）±13.4% ｜ 10-09（25D）±16.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,841,266 | GEX Change vs 上次快照 2,568,904 | Flip: Primary Flip: 16.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 250 / LOW 84 / INVALID 134
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 16.33（全链重定价，覆盖 95%）
Put Wall 15（弱结构｜现价高于该位 4.7%）
最近结构参考: Flip 16（现价低于该位 3.8%）
量化视角： 负 Gamma（384万，无历史分位）｜负 Gamma 缓解（+257万）｜现价位于 Flip 下方 3.77%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 19（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 21.0C — Vol 78 | 最新价 $0.25 | OI 1538→5011 (ΔOI +3473张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3473张（+225.8% vs前日OI），连续性待观察（方向未知）
09-18 16.5P — Vol 237 | 最新价 $1.00 | OI 723→2176 (ΔOI +1453张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1453张（+201.0% vs前日OI），连续性待观察（方向未知）
09-25 16.5C — Vol 131 | 最新价 $0.56 | OI 55→1086 (ΔOI +1031张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1031张（+1874.5% vs前日OI），连续性待观察（方向未知）
10-16 15.0P — Vol 172 | 最新价 $1.02 | OI 3560→4511 (ΔOI +951张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增951张（+26.7% vs前日OI），连续性待观察（方向未知）
09-18 18.0C — Vol 4,993 | 最新价 $0.05 | OI 6340→7106 (ΔOI +766张) | ΔOI/Volume 15.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增766张（+12.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,674 张（Put 2,404 / Call 5,270），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 4D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 18D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 09-18 Forward Structure
存量OI: C 122.8k / P 66.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.66 / P $0.41 ｜ ATM IV 81.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 19 ｜ Put Wall 15（-4.5%，弱）（OI 9.0k）
量化解读： 存量 Call 重｜ATM IV 81.9%｜历史 Rank 4%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 16 ｜ Call Wall 16.5（+5.0%，弱）（OI 1.1k） ｜ Put Wall 15（-4.5%，弱）（OI 0.9k）

10-02（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 16（+1.8%，弱）（OI 0.5k）

10-09（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 16（+1.8%）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-14/USAR_evening.json