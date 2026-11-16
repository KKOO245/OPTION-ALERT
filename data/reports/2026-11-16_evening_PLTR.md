# 期权晚报 2026-11-16（快照 16:40 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（4D）ATM IV 77.4% vs 11-27 60.9%（差 +16.5pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 11-27 85P ΔOI +6,448 占该期限总 OI 12.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 165.74 → 收盘 160.39（-3.2%） ｜ 今日高 166.09 ｜ 低 158.68 ｜ 昨收 167.99 → 收盘 160.39（-4.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 0.79 | OI比 0.94 | ATM IV 77.4% | Skew 8.0pp | Term 0.72 | ExpMove ±6.5%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价显著（Skew 8.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（4D）±6.5% ｜ 11-27（11D）±8.2% ｜ 12-04（18D）±10.3% ｜ 12-11（25D）±12.0%
   ⇒ IV–VIX Spread: +54.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -12,114,521 | GEX Change vs 上次快照 -14,571,727 | Flip: Primary Flip: 164.62（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 375 / LOW 163 / INVALID 260
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 164.62（全链重定价，覆盖 100%）
最近结构参考: Flip 165（现价低于该位 2.6%）
量化视角： 负 Gamma（1211万，无历史分位）｜由正转负（1457万）｜现价位于 Flip 下方 2.57%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 177.5C — Vol 9,538 | 最新价 $0.54 | OI 6308→13256 (ΔOI +6948张) | ΔOI/Volume 72.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6948张（+110.2% vs前日OI），连续性待观察（方向未知）
11-20 172.5C — Vol 4,373 | 最新价 $1.19 | OI 1310→7959 (ΔOI +6649张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6649张（+507.6% vs前日OI），连续性待观察（方向未知）
11-27 85.0P — Vol 3 | 最新价 $0.01 | OI 61→6509 (ΔOI +6448张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6448张（+10570.5% vs前日OI），连续性待观察（方向未知）
11-20 95.0P — Vol 75 | 最新价 $0.02 | OI 1873→7018 (ΔOI +5145张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5145张（+274.7% vs前日OI），连续性待观察（方向未知）
11-20 180.0C — Vol 14,521 | 最新价 $0.36 | OI 11925→15959 (ΔOI +4034张) | ΔOI/Volume 27.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4034张（+33.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 29,224 张（Put 11,593 / Call 17,631），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +25.2k / P +14.3k ｜ Activity HIGH ｜ 4D
11-27  C +1.6k / P +8.7k ｜ Activity HIGH ｜ 11D
12-04  C +73 / P +0.3k ｜ Activity LOW ｜ 18D
12-11  C +6 / P +1.3k ｜ Activity HIGH ｜ 25D

📆 11-20 Forward Structure
存量OI: C 220.2k / P 207.4k，今日变化ΔOI: C +25.2k / P +14.3k，平值价格ATM: C $5.41 / P $4.93 ｜ ATM IV 77.4%，净 delta 敞口 273k shares
Top ΔOI: C 177 +6,948 ｜ C 172 +6,649
仓位参考: Max Pain 170 ｜ Call Wall 175（+9.1%，弱）（OI 10.7k） ｜ Put Wall 155（-3.4%，弱）（OI 8.8k）
量化解读： 存量两侧均衡｜ATM IV 77.4%｜历史 Rank 91%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 273,327 股

📆 11-27 Forward Structure
存量OI: C 20.6k / P 30.5k，今日变化ΔOI: C +1.6k / P +8.7k，平值价格ATM: C $6.70 / P $6.50 ｜ ATM IV 60.9%，净 delta 敞口 -25k shares
Top ΔOI: P 145 +1,651
仓位参考: Max Pain 172 ｜ Call Wall 175（+9.1%，弱）（OI 0.7k） ｜ Put Wall 150（-6.5%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 60.9%｜历史 Rank 91%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 25,274 股

12-04（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 175（+9.1%，弱）（OI 0.9k） ｜ Put Wall 155（-3.4%）（OI 3.1k）

📆 12-11 Forward Structure
存量OI: C 8.8k / P 10.9k，今日变化ΔOI: C +6 / P +1.3k，平值价格ATM: C $9.95 / P $9.30 ｜ ATM IV 57.6%，净 delta 敞口 -7k shares
仓位参考: Max Pain 170 ｜ Call Wall 175（+9.1%，弱）（OI 0.6k） ｜ Put Wall 150（-6.5%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜ATM IV 57.6%｜历史 Rank 91%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 负 7,387 股

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 77.4% vs 11-27 60.9%（差 +16.5pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/PLTR_evening.json