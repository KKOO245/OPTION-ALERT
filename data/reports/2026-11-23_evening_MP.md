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
🟡 **近现价集中开仓**: 12-04 34C ΔOI +34（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 36.42 → 收盘 35.54（-2.4%） ｜ 今日高 36.51 ｜ 低 34.27 ｜ 昨收 33.95 → 收盘 35.54（+4.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.11 | OI比 0.51 | ATM IV 79.0% | Skew 8.9pp | Term 0.86 | ExpMove ±6.5%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价显著（Skew 8.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.11×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（4D）±6.5% ｜ 12-04（11D）±10.9% ｜ 12-11（18D）±6.6% ｜ 12-18（25D）±14.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,848,317 | GEX Change N/A | Flip: Primary Flip: 34.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 245 / LOW 63 / INVALID 190
结构观察区: Primary Flip 34.12（全链重定价，覆盖 100%）
Put Wall 35（弱结构｜现价高于该位 1.5%）
最近结构参考: Put Wall 35（现价高于该位 1.5%）
量化视角： 正 Gamma（185万，无历史分位）｜现价位于 Flip 上方 4.17%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall，弱结构）；上方 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 34（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 30.0P — Vol 42 | 最新价 $0.73 | OI 2311→3483 (ΔOI +1172张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1172张（+50.7% vs前日OI），连续性待观察（方向未知）
12-18 25.0P — Vol 4 | 最新价 $0.11 | OI 444→1511 (ΔOI +1067张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1067张（+240.3% vs前日OI），连续性待观察（方向未知）
11-27 30.0P — Vol 1 | 最新价 $0.04 | OI 151→513 (ΔOI +362张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增362张（+239.7% vs前日OI），值得跟踪（方向未知）
12-04 40.0C — Vol 64 | 最新价 $0.45 | OI 329→540 (ΔOI +211张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增211张（+64.1% vs前日OI），值得跟踪（方向未知）
12-11 42.0P — Vol 16 | 最新价 $6.69 | OI 264→472 (ΔOI +208张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增208张（+78.8% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,020 张（Put 2,809 / Call 211），跨 4 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（4 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +0.6k / P +0.7k ｜ Activity HIGH ｜ 4D
12-04  C +0.3k / P +3 ｜ Activity HIGH ｜ 11D
12-11  C +65 / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
12-18  C -12.1k / P +2.2k ｜ Activity MEDIUM △ ｜ 25D

📆 11-27 Forward Structure
存量OI: C 12.6k / P 6.5k，今日变化ΔOI: C +0.6k / P +0.7k，平值价格ATM: C $1.20 / P $1.10 ｜ ATM IV 79.0%，净 delta 敞口 19k shares
Top ΔOI: C 35 +196 ｜ C 39 +106
仓位参考: Max Pain 37 ｜ Put Wall 33（-7.1%）（OI 2.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.0%｜历史 Rank 70%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,753 股

📆 12-04 Forward Structure
存量OI: C 3.1k / P 1.3k，今日变化ΔOI: C +0.3k / P +3，平值价格ATM: C $1.85 / P $2.01 ｜ ATM IV 74.5%，净 delta 敞口 14k shares
Top ΔOI: P 42 -121 ｜ C 34 +34
仓位参考: Max Pain 36 ｜ Call Wall 35（-1.5%，弱）（OI 0.6k） ｜ Put Wall 34（-4.3%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 74.5%｜历史 Rank 70%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,008 股

12-11（MEDIUM △）Top ΔOI: 42P +208
12-11（MEDIUM △）仓位参考: Max Pain 38 ｜ Call Wall 38（+6.9%，弱）（OI 0.8k）

12-18（MEDIUM △）Top ΔOI: 45C -6,019 ｜ 40C -5,620
12-18（MEDIUM △）仓位参考: Max Pain 45 ｜ Put Wall 35（-1.5%，弱）（OI 6.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/MP_evening.json