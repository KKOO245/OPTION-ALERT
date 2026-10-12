# 期权晚报 2026-10-12（快照 16:40 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 540P ΔOI +1,261（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 552.67 → 收盘 544.85（-1.4%） ｜ 今日高 552.75 ｜ 低 543.34 ｜ 昨收 559.40 → 收盘 544.85（-2.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-15，窗口结束前不做对错判定）

Options: P/C成交量 1.66 | OI比 2.75 | ATM IV 34.5% | Skew 2.0pp | Term 1.08 | ExpMove ±3.2%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构正常（Term 1.08）｜保护溢价中性（Skew 2.0pp）｜当日成交偏 Put（P/C量 1.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.66×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.75×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-16（4D）±3.2% ｜ 10-23（11D）±4.8% ｜ 10-30（18D）±6.5% ｜ 11-06（25D）±7.7%
   ⇒ IV–VIX Spread: +19.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -22,496,259 | GEX Change vs 上次快照 -1,931,587 | Flip: Primary Flip: 567.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 652 / LOW 280 / INVALID 674
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 567.08（全链重定价，覆盖 95%）
最近结构参考: Flip 567（现价低于该位 3.9%）
量化视角： 负 Gamma（2250万，无历史分位）｜负 Gamma 加深（193万）｜现价位于 Flip 下方 3.92%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 540（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 567（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 470.0P — Vol 1 | 最新价 $1.45 | OI 48→2050 (ΔOI +2002张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2002张（+4170.8% vs前日OI），连续性待观察（方向未知）
10-16 540.0P — Vol 882 | 最新价 $6.13 | OI 1668→2929 (ΔOI +1261张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1261张（+75.6% vs前日OI），连续性待观察（方向未知）
10-23 500.0P — Vol 283 | 最新价 $2.06 | OI 1463→2429 (ΔOI +966张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增966张（+66.0% vs前日OI），连续性待观察（方向未知）
10-16 560.0P — Vol 90 | 最新价 $17.75 | OI 250→806 (ΔOI +556张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增556张（+222.4% vs前日OI），连续性待观察（方向未知）
10-16 545.0P — Vol 87 | 最新价 $8.60 | OI 76→555 (ΔOI +479张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增479张（+630.3% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,264 张（Put 5,264 / Call 0），跨 3 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +1.4k / P +2.5k ｜ Activity HIGH ｜ 4D
10-23  C +0.1k / P +1.3k ｜ Activity HIGH ｜ 11D
10-30  C +6 / P +2.5k ｜ Activity HIGH ｜ 18D
11-06  C +16 / P +0.1k ｜ Activity MEDIUM △ ｜ 25D

📆 10-16 Forward Structure
存量OI: C 38.9k / P 107.2k，今日变化ΔOI: C +1.4k / P +2.5k，平值价格ATM: C $9.05 / P $8.60 ｜ ATM IV 34.5%，净 delta 敞口 -106k shares
Top ΔOI: P 540 +1,261 ｜ P 560 +556
仓位参考: Max Pain 540 ｜ Call Wall 550（+0.9%，弱）（OI 2.2k） ｜ Put Wall 520（-4.6%，弱）（OI 7.2k）
量化解读： 存量 Put 重｜ATM IV 34.5%｜历史 Rank 54%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 106,240 股

📆 10-23 Forward Structure
存量OI: C 1.7k / P 10.4k，今日变化ΔOI: C +0.1k / P +1.3k，平值价格ATM: C $12.90 / P $13.10 ｜ ATM IV 34.1%，净 delta 敞口 -26k shares
Top ΔOI: P 500 +966 ｜ P 565 +64 ｜ P 560 -49
仓位参考: Max Pain 565 ｜ Call Wall 525（-3.6%，弱）（OI 0.1k） ｜ Put Wall 510（-6.4%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 34.1%｜历史 Rank 54%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 26,122 股

📆 10-30 Forward Structure
存量OI: C 6.0k / P 30.0k，今日变化ΔOI: C +6 / P +2.5k，平值价格ATM: C $18.20 / P $17.00 ｜ ATM IV 36.0%，净 delta 敞口 -35k shares
Top ΔOI: P 470 +2,002 ｜ P 575 +199
仓位参考: Max Pain 570 ｜ Put Wall 550（+0.9%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜ATM IV 36.0%｜历史 Rank 54%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 34,741 股

11-06（MEDIUM △）Top ΔOI: 567C -59
11-06（MEDIUM △）仓位参考: Max Pain 568 ｜ Call Wall 567.5（+4.2%，弱）（OI 0.2k） ｜ Put Wall 565（+3.7%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=45 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=45）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/SOXX_evening.json