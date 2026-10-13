# 期权晨报 2026-10-13（快照 10:20 ET）

📊 市场环境

SPY $777.90 ｜ QQQ $743.57
VIX 15.31 ↑0.7%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 14P ΔOI +158（距现价 +0.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 14.29 → 今开 13.81（-3.4%） | 较昨收变动（含盘初走势） ｜ 今日高 14.19 ｜ 低 13.71

Options: P/C成交量 0.79 | OI比 0.20 | ATM IV 79.4% | Skew 0.2pp | Term 0.78 | ExpMove ±6.6%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价薄（Skew 0.2pp）｜存量 Call 偏重（OI比 0.20）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.20×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（3D）±6.6% ｜ 10-23（10D）±9.7% ｜ 10-30（17D）±24.1% ｜ 11-06（24D）±18.5%
   ⇒ IV–VIX Spread: +64.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 8,171 | GEX Change vs 上次快照 -57,660 | Flip: Primary Flip: 13.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 149 / LOW 96 / INVALID 159
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 13.91（全链重定价，覆盖 95%）
Put Wall 14（弱结构｜现价低于该位 0.6%）
最近结构参考: Flip 14（现价高于该位 0.1%）
量化视角： 正 Gamma（1万，无历史分位）｜正 Gamma 减弱（6万）｜现价位于 Flip 上方 0.10%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall，弱结构） / 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 15.0C — Vol 432 | 最新价 $0.20 | OI 83→310 (ΔOI +227张) | ΔOI/Volume 52.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增227张（+273.5% vs前日OI），连续性待观察（方向未知）
10-23 14.0P — Vol 613 | 最新价 $0.50 | OI 451→609 (ΔOI +158张) | ΔOI/Volume 25.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增158张（+35.0% vs前日OI），连续性待观察（方向未知）
11-13 14.5C — Vol 140 | 最新价 $1.15 | OI 4→143 (ΔOI +139张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增139张（+3475.0% vs前日OI），连续性待观察（方向未知）
10-16 15.5C — Vol 137 | 最新价 $0.14 | OI 79→207 (ΔOI +128张) | ΔOI/Volume 93.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增128张（+162.0% vs前日OI），连续性待观察（方向未知）
10-16 14.5C — Vol 133 | 最新价 $0.37 | OI 7→108 (ΔOI +101张) | ΔOI/Volume 75.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增101张（+1442.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 753 张（Put 158 / Call 595），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.5k / P -1.0k ｜ Activity MEDIUM △ ｜ 3D
10-23  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 10D
10-30  C +57 / P +18 ｜ Activity MEDIUM △ ｜ 17D
11-06  C +18 / P +42 ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 22.4k / P 4.6k，今日变化ΔOI: C +0.5k / P -1.0k，平值价格ATM: C $0.65 / P $0.27 ｜ ATM IV 79.4%，净 delta 敞口 119k shares
Top ΔOI: P 20 -327 ｜ P 18 -282 ｜ C 15 +227
仓位参考: Max Pain 17 ｜ Put Wall 15（+7.8%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 79.4%｜历史 Rank 10%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 119,041 股

10-23（MEDIUM △）Top ΔOI: 14P +158 ｜ 14C +51
10-23（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 14（+0.6%）（OI 0.6k）

10-30（MEDIUM △）Top ΔOI: 13P +13
10-30（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 14（+0.6%）（OI 0.3k）

11-06（MEDIUM △）Top ΔOI: 15P +10
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 15（+7.8%，弱）（OI 29）

📅 事件差分（观察，非因果）: 10-16（3D）ATM IV 79.4% vs 10-23 69.9%（差 +9.5pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=50 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=50）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/NNE_morning.json