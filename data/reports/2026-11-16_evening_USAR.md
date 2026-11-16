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
🔴 **事件差分**: 11-20（4D）ATM IV 119.9% vs 11-27 102.4%（差 +17.5pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 12-04 9C ΔOI +580 占该期限总 OI 12.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 7.66 → 收盘 7.13（-6.9%） ｜ 今日高 7.75 ｜ 低 7.11 ｜ 昨收 8.16 → 收盘 7.13（-12.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 0.42 | OI比 0.60 | ATM IV 119.9% | Skew 5.3pp | Term 0.85 | ExpMove ±10.4%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价中性（Skew 5.3pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±10.4% ｜ 11-27（11D）±13.5% ｜ 12-04（18D）±21.9% ｜ 12-11（25D）±21.0%
   ⇒ IV–VIX Spread: +97.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -363,592 | GEX Change vs 上次快照 -56,840 | Flip: Primary Flip: 7.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 163 / LOW 91 / INVALID 142
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 7.30（全链重定价，覆盖 100%）
最近结构参考: Flip 7（现价低于该位 2.3%）
量化视角： 负 Gamma（36万，无历史分位）｜负 Gamma 加深（6万）｜现价位于 Flip 下方 2.32%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 7（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 8.0P — Vol 800 | 最新价 $1.40 | OI 9143→10191 (ΔOI +1048张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1048张（+11.5% vs前日OI），值得跟踪（方向未知）
11-20 10.5C — Vol 39 | 最新价 $0.02 | OI 1774→2702 (ΔOI +928张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增928张（+52.3% vs前日OI），连续性待观察（方向未知）
12-04 9.0C — Vol 63 | 最新价 $0.15 | OI 157→737 (ΔOI +580张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增580张（+369.4% vs前日OI），连续性待观察（方向未知）
11-27 12.0C — Vol 1 | 最新价 $0.01 | OI 308→484 (ΔOI +176张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增176张（+57.1% vs前日OI），值得跟踪（方向未知）
11-20 8.5C — Vol 2,587 | 最新价 $0.05 | OI 2528→2680 (ΔOI +152张) | ΔOI/Volume 5.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增152张（+6.0% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,884 张（Put 1,048 / Call 1,836），跨 4 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +1.5k / P -1.5k ｜ Activity HIGH ｜ 4D
11-27  C +0.4k / P +46 ｜ Activity MEDIUM △ ｜ 11D
12-04  C +0.7k / P +3 ｜ Activity HIGH ｜ 18D
12-11  C +33 / P +45 ｜ Activity LOW ｜ 25D

📆 11-20 Forward Structure
存量OI: C 52.4k / P 31.4k，今日变化ΔOI: C +1.5k / P -1.5k，平值价格ATM: C $0.44 / P $0.30 ｜ ATM IV 119.9%，净 delta 敞口 148k shares
Top ΔOI: P 8 -1,273 ｜ P 10 -429
仓位参考: Max Pain 10 ｜ Put Wall 7（-1.8%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 119.9%｜历史 Rank 58%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 148,240 股

11-27（MEDIUM △）Top ΔOI: 7P +47
11-27（MEDIUM △）仓位参考: Max Pain 8 ｜ Put Wall 7（-1.8%，弱）（OI 0.4k）

📆 12-04 Forward Structure
存量OI: C 3.3k / P 1.6k，今日变化ΔOI: C +0.7k / P +3，平值价格ATM: C $1.02 / P $0.54 ｜ ATM IV 100.5%，净 delta 敞口 16k shares
Top ΔOI: C 7 +49
仓位参考: Max Pain 9 ｜ Put Wall 7（-1.8%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 100.5%｜历史 Rank 58%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 15,935 股

12-11（Activity LOW）仓位参考: Max Pain 10 ｜ Call Wall 7.5（+5.2%，弱）（OI 97） ｜ Put Wall 7.5（+5.2%，弱）（OI 83）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 119.9% vs 11-27 102.4%（差 +17.5pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/USAR_evening.json