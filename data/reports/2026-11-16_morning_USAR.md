# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $744.62 ｜ QQQ $664.02
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 35.1（fear）
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
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **事件差分**: 11-20 ATM IV 115.5% vs 11-27 105.2%（差 +10.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🔵 **期限 OI 集中**: 12-04 9C ΔOI +580 占该期限总 OI 12.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 8.16 → 今开 7.66（-6.2%） | 较昨收变动（含盘初走势） ｜ 今日高 7.75 ｜ 低 7.40

Options: P/C成交量 0.34 | OI比 0.60 | ATM IV 115.5% | Skew 1.3pp | Term 0.89 | ExpMove ±9.7%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价薄（Skew 1.3pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（4D）±9.7% ｜ 11-27（11D）±15.0% ｜ 12-04（18D）±19.3% ｜ 12-11（25D）±31.3%
   ⇒ IV–VIX Spread: +93.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -306,753 | GEX Change vs 上次快照 -1,033,667 | Flip: Primary Flip: 7.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 186 / LOW 95 / INVALID 115
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 7.70（全链重定价，覆盖 100%）
最近结构参考: Flip 8（现价低于该位 1.3%）
量化视角： 负 Gamma（31万，无历史分位）｜由正转负（103万）｜现价位于 Flip 下方 1.27%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 8（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 8.0P — Vol 1,191 | 最新价 $0.91 | OI 9143→10191 (ΔOI +1048张) | ΔOI/Volume 88.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1048张（+11.5% vs前日OI），连续性待观察（方向未知）
11-20 10.5C — Vol 1,116 | 最新价 $0.05 | OI 1774→2702 (ΔOI +928张) | ΔOI/Volume 83.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增928张（+52.3% vs前日OI），连续性待观察（方向未知）
12-04 9.0C — Vol 587 | 最新价 $0.42 | OI 157→737 (ΔOI +580张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增580张（+369.4% vs前日OI），连续性待观察（方向未知）
11-27 12.0C — Vol 224 | 最新价 $0.03 | OI 308→484 (ΔOI +176张) | ΔOI/Volume 78.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增176张（+57.1% vs前日OI），连续性待观察（方向未知）
11-20 8.5C — Vol 418 | 最新价 $0.29 | OI 2528→2680 (ΔOI +152张) | ΔOI/Volume 36.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增152张（+6.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,884 张（Put 1,048 / Call 1,836），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +1.5k / P -1.5k ｜ Activity MEDIUM △ ｜ 4D
11-27  C +0.4k / P +46 ｜ Activity MEDIUM △ ｜ 11D
12-04  C +0.7k / P +3 ｜ Activity HIGH ｜ 18D
12-11  C +33 / P +45 ｜ Activity MEDIUM △ ｜ 25D

📆 11-20 Forward Structure
存量OI: C 52.4k / P 31.4k，今日变化ΔOI: C +1.5k / P -1.5k，平值价格ATM: C $0.45 / P $0.29 ｜ ATM IV 115.5%，净 delta 敞口 138k shares
Top ΔOI: P 8 -1,273 ｜ P 10 -429
仓位参考: Max Pain 10 ｜ Put Wall 8（+5.2%，弱）（OI 5.6k）
量化解读： 存量 Call 重｜ATM IV 115.5%｜历史 Rank 52%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 138,463 股

11-27（MEDIUM △）Top ΔOI: 7P +47
11-27（MEDIUM △）仓位参考: Max Pain 8 ｜ Call Wall 8（+5.2%，弱）（OI 2.7k） ｜ Put Wall 8（+5.2%，弱）（OI 0.5k）

📆 12-04 Forward Structure
存量OI: C 3.3k / P 1.6k，今日变化ΔOI: C +0.7k / P +3，平值价格ATM: C $0.95 / P $0.52 ｜ ATM IV 102.1%，净 delta 敞口 21k shares
Top ΔOI: C 7 +49
仓位参考: Max Pain 9 ｜ Put Wall 8（+5.2%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 102.1%｜历史 Rank 52%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 正 21,345 股

12-11（MEDIUM △）Top ΔOI: 7P +23 ｜ 7P +8
12-11（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 7.5（-1.4%，弱）（OI 97） ｜ Put Wall 8（+5.2%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 115.5% vs 11-27 105.2%（差 +10.3pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/USAR_morning.json