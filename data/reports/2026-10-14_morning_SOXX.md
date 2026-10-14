# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $769.08 ｜ QQQ $728.95
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 540P ΔOI +1,246（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 543.90 → 今开 531.59（-2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 534.42 ｜ 低 528.75

Options: P/C成交量 0.28 | OI比 2.31 | ATM IV 46.0% | Skew 1.2pp | Term 0.83 | ExpMove ±3.0%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价薄（Skew 1.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 2.31×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±3.0% ｜ 10-23（9D）±4.9% ｜ 10-30（16D）±6.5% ｜ 11-06（23D）±8.3%
   ⇒ IV–VIX Spread: +30.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -35,751,562 | GEX Change vs 上次快照 -12,769,657 | Flip: Primary Flip: 559.18（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 644 / LOW 325 / INVALID 649
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 559.18（全链重定价，覆盖 91%）
Put Wall 500（弱结构｜现价高于该位 6.1%）
最近结构参考: Flip 559（现价低于该位 5.1%）
量化视角： 负 Gamma（3575万，无历史分位）｜负 Gamma 加深（1277万）｜现价位于 Flip 下方 5.14%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall，弱结构）；上方 540（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 559（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 580.0C — Vol 2,050 | 最新价 $0.38 | OI 1688→3386 (ΔOI +1698张) | ΔOI/Volume 82.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1698张（+100.6% vs前日OI），连续性待观察（方向未知）
10-30 540.0P — Vol 1,571 | 最新价 $15.80 | OI 897→2143 (ΔOI +1246张) | ΔOI/Volume 79.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1246张（+138.9% vs前日OI），连续性待观察（方向未知）
10-16 600.0C — Vol 2,436 | 最新价 $0.12 | OI 7075→8111 (ΔOI +1036张) | ΔOI/Volume 42.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1036张（+14.6% vs前日OI），连续性待观察（方向未知）
10-16 540.0C — Vol 931 | 最新价 $10.05 | OI 614→1365 (ΔOI +751张) | ΔOI/Volume 80.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增751张（+122.3% vs前日OI），连续性待观察（方向未知）
10-16 545.0C — Vol 848 | 最新价 $7.98 | OI 187→921 (ΔOI +734张) | ΔOI/Volume 86.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增734张（+392.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,465 张（Put 1,246 / Call 4,219），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +5.1k / P -0.7k ｜ Activity HIGH ｜ 2D
10-23  C +0.4k / P +1.1k ｜ Activity MEDIUM △ ｜ 9D
10-30  C +0.5k / P +2.4k ｜ Activity MEDIUM △ ｜ 16D
11-06  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 23D

📆 10-16 Forward Structure
存量OI: C 45.4k / P 105.0k，今日变化ΔOI: C +5.1k / P -0.7k，平值价格ATM: C $9.20 / P $6.80 ｜ ATM IV 46.0%，净 delta 敞口 26k shares
Top ΔOI: C 580 +1,698
仓位参考: Max Pain 540 ｜ Call Wall 550（+3.7%，弱）（OI 2.3k） ｜ Put Wall 530（-0.1%，弱）（OI 5.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 46.0%｜历史 Rank 82%（近端代理）｜IV/RV 1.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,102 股

10-23（MEDIUM △）Top ΔOI: 522P +197 ｜ 555P +188
10-23（MEDIUM △）仓位参考: Max Pain 555 ｜ Call Wall 550（+3.7%）（OI 1.0k） ｜ Put Wall 510（-3.9%，弱）（OI 3.0k）

10-30（MEDIUM △）Top ΔOI: 540P +1,246 ｜ 530P +618
10-30（MEDIUM △）仓位参考: Max Pain 568 ｜ Put Wall 500（-5.7%）（OI 10.7k）

11-06（MEDIUM △）Top ΔOI: 570P +149 ｜ 562C +34
11-06（MEDIUM △）仓位参考: Max Pain 570 ｜ Call Wall 562.5（+6.0%，弱）（OI 0.2k） ｜ Put Wall 500（-5.7%，弱）（OI 94）

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 46.0% vs 10-23 39.9%（差 +6.1pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/SOXX_morning.json