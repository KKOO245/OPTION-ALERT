# 期权晚报 2026-10-26（快照 21:54 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 18.39 ↓5.5%（5D -0.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：无更新，来源自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 9.52 → 收盘 8.91（-6.4%） ｜ 今日高 9.32 ｜ 低 8.89 ｜ 昨收 9.33 → 收盘 8.91（-4.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-29，窗口结束前不做对错判定）

Options: P/C成交量 0.36 | OI比 0.46 | ATM IV 88.0% | Skew 3.5pp | Term 0.98 | ExpMove ±7.4%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常（Term 0.98）｜保护溢价中性（Skew 3.5pp）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（4D）±7.4% ｜ 11-06（11D）±12.5% ｜ 11-13（18D）±17.4% ｜ 11-20（25D）±20.0%
   ⇒ IV–VIX Spread: +69.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,891,689 | GEX Change vs 上次快照 -131,524 | Flip: Primary Flip: 9.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 167 / LOW 75 / INVALID 174
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 9.84（全链重定价，覆盖 98%）
最近结构参考: Flip 10（现价低于该位 9.5%）
量化视角： 负 Gamma（289万，无历史分位）｜负 Gamma 加深（13万）｜现价位于 Flip 下方 9.47%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 11（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 9.0P — Vol 1,562 | 最新价 $0.89 | OI 888→1747 (ΔOI +859张) | ΔOI/Volume 55.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增859张（+96.7% vs前日OI），连续性待观察（方向未知）
10-30 9.5P — Vol 525 | 最新价 $0.63 | OI 182→758 (ΔOI +576张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增576张（+316.5% vs前日OI），连续性待观察（方向未知）
11-20 9.0C — Vol 854 | 最新价 $0.89 | OI 55→501 (ΔOI +446张) | ΔOI/Volume 52.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增446张（+810.9% vs前日OI），连续性待观察（方向未知）
11-20 9.5C — Vol 871 | 最新价 $0.66 | OI 390→703 (ΔOI +313张) | ΔOI/Volume 35.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增313张（+80.3% vs前日OI），连续性待观察（方向未知）
11-13 10.0C — Vol 74 | 最新价 $0.43 | OI 94→365 (ΔOI +271张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增271张（+288.3% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,465 张（Put 1,435 / Call 1,030），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-30 Forward Structure
存量OI: C 20.0k / P 9.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.29 / P $0.37 ｜ ATM IV 88.0%，净 delta 敞口 0 shares
仓位参考: Max Pain 11 ｜ Put Wall 9（+1.0%）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 88.0%｜历史 Rank 20%（近端代理）｜IV/RV 1.50×（近似）｜净 delta 敞口 正 0 股

11-06（Activity LOW）仓位参考: Max Pain 12 ｜ Put Wall 9（+1.0%）（OI 1.5k）

11-13（Activity LOW）仓位参考: Max Pain 12 ｜ Call Wall 9.5（+6.6%，弱）（OI 0.1k） ｜ Put Wall 9（+1.0%，弱）（OI 0.1k）

11-20（Activity LOW）仓位参考: Max Pain 14 ｜ Put Wall 9（+1.0%，弱）（OI 1.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=67 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=67）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/USAR_evening.json