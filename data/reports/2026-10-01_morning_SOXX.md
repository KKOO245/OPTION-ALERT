# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $763.99 ｜ QQQ $742.03
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 45.6% vs 10-09 35.4%（差 +10.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 550P ΔOI +2,004（距现价 -3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 568.64 → 今开 569.19（+0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 572.89 ｜ 低 564.69

Options: P/C成交量 22.81 | OI比 1.81 | ATM IV 45.6% | Skew 2.5pp | Term 0.85 | ExpMove ±2.4%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价中性（Skew 2.5pp）｜当日成交偏 Put（P/C量 22.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 22.81×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.81×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.4% ｜ 10-09（8D）±4.7% ｜ 10-16（15D）±6.3% ｜ 10-23（22D）±7.1%
   ⇒ IV–VIX Spread: +28.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,742,240 | GEX Change vs 上次快照 -3,247,432 | Flip: Primary Flip: 561.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 583 / LOW 284 / INVALID 691
结构观察区: Primary Flip 561.41（全链重定价，覆盖 97%）
Call Wall 600（现价低于该位 5.5%）
最近结构参考: Flip 561（现价高于该位 0.9%）
量化视角： 正 Gamma（574万，无历史分位）｜正 Gamma 减弱（325万）｜现价位于 Flip 上方 0.95%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 550（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 561（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 535.0P — Vol 2,603 | 最新价 $0.55 | OI 99→2553 (ΔOI +2454张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2454张（+2478.8% vs前日OI），连续性待观察（方向未知）
10-02 550.0P — Vol 2,603 | 最新价 $1.26 | OI 1026→3030 (ΔOI +2004张) | ΔOI/Volume 77.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2004张（+195.3% vs前日OI），连续性待观察（方向未知）
10-02 590.0C — Vol 314 | 最新价 $1.30 | OI 200→463 (ΔOI +263张) | ΔOI/Volume 83.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增263张（+131.5% vs前日OI），连续性待观察（方向未知）
10-02 315.0P — Vol 216 | 最新价 $0.11 | OI 327→543 (ΔOI +216张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增216张（+66.1% vs前日OI），连续性待观察（方向未知）
10-02 310.0P — Vol 216 | 最新价 $0.05 | OI 389→605 (ΔOI +216张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增216张（+55.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,153 张（Put 4,890 / Call 263），跨 1 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +0.5k / P +4.5k ｜ Activity MEDIUM △ ｜ 1D
10-09  C +0.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 8D
10-16  C -0.7k / P -2.3k ｜ Activity MEDIUM △ ｜ 15D
10-23  C -2 / P +68 ｜ Activity LOW ｜ 22D

📆 10-02 Forward Structure
存量OI: C 17.0k / P 30.8k，今日变化ΔOI: C +0.5k / P +4.5k，平值价格ATM: C $8.60 / P $5.20 ｜ ATM IV 45.6%，净 delta 敞口 -26k shares
Top ΔOI: P 535 +2,454 ｜ P 550 +2,004 ｜ C 590 +263
仓位参考: Max Pain 550 ｜ Call Wall 542.5（-4.3%，弱）（OI 2.8k） ｜ Put Wall 550（-3.0%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 45.6%｜历史 Rank 81%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 25,842 股

10-09（MEDIUM △）Top ΔOI: 535P +163 ｜ 550P +71
10-09（MEDIUM △）仓位参考: Max Pain 525 ｜ Call Wall 537.5（-5.2%，弱）（OI 0.4k） ｜ Put Wall 550（-3.0%，弱）（OI 0.3k）

10-16（MEDIUM △）Top ΔOI: 465P -1,160
10-16（MEDIUM △）仓位参考: Max Pain 530 ｜ Call Wall 600（+5.9%）（OI 9.1k） ｜ Put Wall 530（-6.5%，弱）（OI 4.8k）

10-23（Activity LOW）仓位参考: Max Pain 528 ｜ Call Wall 570（+0.6%，弱）（OI 82）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 45.6% vs 10-09 35.4%（差 +10.1pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/SOXX_morning.json