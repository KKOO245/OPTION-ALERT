# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $734.92 ｜ QQQ $656.95
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **事件差分**: 11-20（3D）ATM IV 77.6% vs 11-27 59.2%（差 +18.4pp），覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 12-04 155P ΔOI -850（距现价 -3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 160.39 → 今开 159.97（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 162.59 ｜ 低 158.31

Options: P/C成交量 0.44 | OI比 0.84 | ATM IV 77.6% | Skew 7.3pp | Term 0.71 | ExpMove ±6.0%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价显著（Skew 7.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（3D）±6.0% ｜ 11-27（10D）±7.9% ｜ 12-04（17D）±10.0% ｜ 12-11（24D）±11.8%
   ⇒ IV–VIX Spread: +54.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,053,358 | GEX Change vs 上次快照 5,983,514 | Flip: Primary Flip: 161.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 442 / LOW 169 / INVALID 187
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 161.88（全链重定价，覆盖 100%）
最近结构参考: Flip 162（现价低于该位 1.3%）
量化视角： 负 Gamma（805万，无历史分位）｜负 Gamma 缓解（+598万）｜现价位于 Flip 下方 1.34%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 170（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 162（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 180.0C — Vol 14,521 | 最新价 $0.36 | OI 15959→24509 (ΔOI +8550张) | ΔOI/Volume 58.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8550张（+53.6% vs前日OI），连续性待观察（方向未知）
11-20 177.5C — Vol 9,538 | 最新价 $0.54 | OI 13256→19511 (ΔOI +6255张) | ΔOI/Volume 65.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6255张（+47.2% vs前日OI），连续性待观察（方向未知）
11-27 150.0P — Vol 3,686 | 最新价 $3.10 | OI 3402→6072 (ΔOI +2670张) | ΔOI/Volume 72.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2670张（+78.5% vs前日OI），连续性待观察（方向未知）
11-20 100.0P — Vol 3,259 | 最新价 $0.04 | OI 8416→10294 (ΔOI +1878张) | ΔOI/Volume 57.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1878张（+22.3% vs前日OI），连续性待观察（方向未知）
12-18 140.0P — Vol 4,117 | 最新价 $3.43 | OI 19830→21528 (ΔOI +1698张) | ΔOI/Volume 41.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1698张（+8.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 21,051 张（Put 6,246 / Call 14,805），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +20.7k / P -4.8k ｜ Activity HIGH ｜ 3D
11-27  C +2.4k / P +5.1k ｜ Activity MEDIUM △ ｜ 10D
12-04  C +1.1k / P -0.3k ｜ Activity MEDIUM △ ｜ 17D
12-11  C +0.2k / P +0.6k ｜ Activity MEDIUM △ ｜ 24D

📆 11-20 Forward Structure
存量OI: C 240.8k / P 202.6k，今日变化ΔOI: C +20.7k / P -4.8k，平值价格ATM: C $4.70 / P $4.80 ｜ ATM IV 77.6%，净 delta 敞口 950k shares
Top ΔOI: C 180 +8,550 ｜ C 177 +6,255 ｜ P 200 -4,433
仓位参考: Max Pain 170 ｜ Call Wall 175（+9.6%，弱）（OI 11.7k） ｜ Put Wall 150（-6.1%，弱）（OI 8.7k）
量化解读： 存量 Call 重｜ATM IV 77.6%｜历史 Rank 91%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 949,926 股

11-27（MEDIUM △）Top ΔOI: 150P +2,670 ｜ 149P +553
11-27（MEDIUM △）仓位参考: Max Pain 172 ｜ Call Wall 175（+9.6%，弱）（OI 0.8k） ｜ Put Wall 150（-6.1%，弱）（OI 6.1k）

12-04（MEDIUM △）Top ΔOI: 155P -850
12-04（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 175（+9.6%，弱）（OI 0.9k） ｜ Put Wall 155（-3.0%，弱）（OI 2.2k）

12-11（MEDIUM △）Top ΔOI: 145P +87 ｜ 150P +70
12-11（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 175（+9.6%，弱）（OI 0.6k） ｜ Put Wall 150（-6.1%，弱）（OI 1.2k）

📅 事件差分（观察，非因果）: 11-20（3D）ATM IV 77.6% vs 11-27 59.2%（差 +18.4pp）——覆盖 零售销售 MoM、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/PLTR_morning.json