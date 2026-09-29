# 期权晨报 2026-09-29（快照 10:20 ET）

📊 市场环境

SPY $764.73 ｜ QQQ $737.93
VIX 15.96 ↓0.7%（5D +12.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 580C ΔOI +501（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 560.79 → 今开 569.87（+1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 572.67 ｜ 低 565.30

Options: P/C成交量 1.34 | OI比 1.57 | ATM IV 44.6% | Skew -0.1pp | Term 0.87 | ExpMove ±3.5%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.1pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.34×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.57×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±3.5% ｜ 10-09（10D）±6.3% ｜ 10-16（17D）±6.8% ｜ 10-23（24D）±3.8%
   ⇒ IV–VIX Spread: +28.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,147,331 | GEX Change vs 上次快照 2,970,614 | Flip: Primary Flip: 559.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 570 / LOW 243 / INVALID 739
结构观察区: Primary Flip 559.69（全链重定价，覆盖 96%）
Call Wall 600（现价低于该位 4.9%）
最近结构参考: Flip 560（现价高于该位 2.0%）
量化视角： 正 Gamma（615万，无历史分位）｜正 Gamma 增强（+297万）｜现价位于 Flip 上方 1.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 542（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 560（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 580.0C — Vol 507 | 最新价 $10.70 | OI 920→1421 (ΔOI +501张) | ΔOI/Volume 98.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增501张（+54.5% vs前日OI），连续性待观察（方向未知）
10-16 535.0P — Vol 506 | 最新价 $7.80 | OI 870→1367 (ΔOI +497张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增497张（+57.1% vs前日OI），连续性待观察（方向未知）
10-16 590.0C — Vol 315 | 最新价 $7.28 | OI 793→1066 (ΔOI +273张) | ΔOI/Volume 86.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增273张（+34.4% vs前日OI），连续性待观察（方向未知）
10-16 400.0P — Vol 355 | 最新价 $0.20 | OI 6323→6557 (ΔOI +234张) | ΔOI/Volume 65.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增234张（+3.7% vs前日OI），值得跟踪（方向未知）
10-02 465.0P — Vol 207 | 最新价 $0.20 | OI 118→321 (ΔOI +203张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增203张（+172.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,708 张（Put 934 / Call 774），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.9k / P +0.7k ｜ Activity MEDIUM △ ｜ 3D
10-09  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 10D
10-16  C +1.0k / P +1.1k ｜ Activity MEDIUM △ ｜ 17D
10-23  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 24D

📆 10-02 Forward Structure
存量OI: C 16.3k / P 25.6k，今日变化ΔOI: C +0.9k / P +0.7k，平值价格ATM: C $9.80 / P $10.20 ｜ ATM IV 44.6%，净 delta 敞口 30k shares
Top ΔOI: C 575 +201
仓位参考: Max Pain 542 ｜ Call Wall 542.5（-5.0%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 44.6%｜历史 Rank 80%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 30,355 股

10-09（MEDIUM △）Top ΔOI: 580P +100 ｜ 550C +68
10-09（MEDIUM △）仓位参考: Max Pain 525 ｜ Call Wall 537.5（-5.8%，弱）（OI 0.4k） ｜ Put Wall 540（-5.4%，弱）（OI 0.1k）

10-16（MEDIUM △）Top ΔOI: 580C +501 ｜ 535P +497
10-16（MEDIUM △）仓位参考: Max Pain 530 ｜ Call Wall 600（+5.1%）（OI 9.4k）

10-23（MEDIUM △）Top ΔOI: 555P +54
10-23（MEDIUM △）仓位参考: Max Pain 525 ｜ Call Wall 570（-0.1%，弱）（OI 95）

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 44.6% vs 10-09 37.6%（差 +7.0pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/SOXX_morning.json