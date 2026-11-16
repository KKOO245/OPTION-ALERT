# 期权晨报 2026-11-16（快照 10:20 ET）

📊 市场环境

SPY $740.36 ｜ QQQ $661.75
VIX 21.57 ↑11.8%（5D +8.3%） ｜ Vol Regime: ELEVATED
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
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **事件差分**: 11-20 ATM IV 71.3% vs 11-27 57.3%（差 +14.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🔵 **期限 OI 集中**: 11-27 85P ΔOI +6,448 占该期限总 OI 12.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 167.99 → 今开 165.74（-1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 166.09 ｜ 低 161.10

Options: P/C成交量 1.00 | OI比 0.94 | ATM IV 71.3% | Skew 7.9pp | Term 0.74 | ExpMove ±6.4%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价显著（Skew 7.9pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（4D）±6.4% ｜ 11-27（11D）±8.0% ｜ 12-04（18D）±10.3% ｜ 12-11（25D）±11.4%
   ⇒ IV–VIX Spread: +49.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 2,457,206 | GEX Change vs 上次快照 1,557,255 | Flip: Primary Flip: 162.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 436 / LOW 165 / INVALID 197
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 162.81（全链重定价，覆盖 97%）
最近结构参考: Flip 163（现价高于该位 0.5%）
量化视角： 正 Gamma（246万，无历史分位）｜正 Gamma 增强（+156万）｜现价位于 Flip 上方 0.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 163（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 177.5C — Vol 13,316 | 最新价 $1.68 | OI 6308→13256 (ΔOI +6948张) | ΔOI/Volume 52.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6948张（+110.2% vs前日OI），连续性待观察（方向未知）
11-20 172.5C — Vol 8,486 | 最新价 $3.20 | OI 1310→7959 (ΔOI +6649张) | ΔOI/Volume 78.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6649张（+507.6% vs前日OI），连续性待观察（方向未知）
11-27 85.0P — Vol 6,513 | 最新价 $0.01 | OI 61→6509 (ΔOI +6448张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6448张（+10570.5% vs前日OI），连续性待观察（方向未知）
11-20 95.0P — Vol 5,609 | 最新价 $0.02 | OI 1873→7018 (ΔOI +5145张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5145张（+274.7% vs前日OI），连续性待观察（方向未知）
11-20 180.0C — Vol 10,563 | 最新价 $1.15 | OI 11925→15959 (ΔOI +4034张) | ΔOI/Volume 38.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4034张（+33.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 29,224 张（Put 11,593 / Call 17,631），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +25.2k / P +14.3k ｜ Activity MEDIUM △ ｜ 4D
11-27  C +1.6k / P +8.7k ｜ Activity HIGH ｜ 11D
12-04  C +73 / P +0.3k ｜ Activity MEDIUM △ ｜ 18D
12-11  C +6 / P +1.3k ｜ Activity MEDIUM △ ｜ 25D

📆 11-20 Forward Structure
存量OI: C 220.2k / P 207.4k，今日变化ΔOI: C +25.2k / P +14.3k，平值价格ATM: C $5.65 / P $4.75 ｜ ATM IV 71.3%，净 delta 敞口 411k shares
Top ΔOI: C 177 +6,948 ｜ C 172 +6,649
仓位参考: Max Pain 170 ｜ Call Wall 177.5（+8.5%，弱）（OI 13.3k） ｜ Put Wall 155（-5.3%，弱）（OI 8.8k）
量化解读： 存量两侧均衡｜ATM IV 71.3%｜历史 Rank 89%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 411,025 股

📆 11-27 Forward Structure
存量OI: C 20.6k / P 30.5k，今日变化ΔOI: C +1.6k / P +8.7k，平值价格ATM: C $7.75 / P $5.30 ｜ ATM IV 57.3%，净 delta 敞口 -12k shares
Top ΔOI: P 145 +1,651 ｜ C 187 +1,048
仓位参考: Max Pain 172 ｜ Call Wall 175（+7.0%，弱）（OI 0.7k） ｜ Put Wall 150（-8.3%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 57.3%｜历史 Rank 89%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 11,806 股

12-04（MEDIUM △）Top ΔOI: 165P +120 ｜ 155P -59
12-04（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 175（+7.0%，弱）（OI 0.9k） ｜ Put Wall 155（-5.3%）（OI 3.1k）

12-11（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 175（+7.0%，弱）（OI 0.6k） ｜ Put Wall 150（-8.3%，弱）（OI 1.1k）

📅 事件差分（观察，非因果）: 11-20（4D）ATM IV 71.3% vs 11-27 57.3%（差 +14.0pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/PLTR_morning.json