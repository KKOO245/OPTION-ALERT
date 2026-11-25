# 期权晚报 2026-11-25（快照 16:40 ET）

📊 市场环境

SPY $716.70 ｜ QQQ $633.93
VIX 28.29 ↑7.3%（5D +15.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 125C ΔOI +4,967（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 118.46 → 收盘 127.44（+7.6%） ｜ 今日高 128.18 ｜ 低 113.93 ｜ 昨收 125.81 → 收盘 127.44（+1.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-02，窗口结束前不做对错判定）

Options: P/C成交量 0.47 | OI比 0.95 | ATM IV 83.0% | Skew 19.5pp | Term 0.81 | ExpMove ±3.9%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 19.5pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-27（2D）±3.9% ｜ 11-30（5D）±5.7% ｜ 12-02（7D）±7.6% ｜ 12-04（9D）±8.9%
   ⇒ IV–VIX Spread: +54.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -21,320,328 | GEX Change vs 上次快照 32,878,561 | Flip: Primary Flip: 129.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 827 / LOW 190 / INVALID 621
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 129.65（全链重定价，覆盖 95%）
Put Wall 115（弱结构｜现价高于该位 10.8%）
最近结构参考: Flip 130（现价低于该位 1.7%）
量化视角： 负 Gamma（2132万，无历史分位）｜负 Gamma 缓解（+3288万）｜现价位于 Flip 下方 1.70%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 115（Put Wall，弱结构）；上方 130（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 130（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +13.0k / P +0.2k ｜ Activity HIGH ｜ 2D
11-30  C +6.4k / P +3.5k ｜ Activity HIGH ｜ 5D
12-02  C +4.4k / P +1.6k ｜ Activity HIGH ｜ 7D
12-04  C +10.1k / P +25.2k ｜ Activity HIGH ｜ 9D

📆 11-27 Forward Structure
存量OI: C 216.5k / P 101.0k，今日变化ΔOI: C +13.0k / P +0.2k，平值价格ATM: C $2.67 / P $2.30 ｜ ATM IV 67.8%，净 delta 敞口 1.2M shares
Top ΔOI: C 125 +4,967 ｜ C 135 +3,823
仓位参考: Max Pain 133 ｜ Call Wall 140（+9.9%，弱）（OI 9.1k） ｜ Put Wall 120（-5.8%，弱）（OI 7.8k）
量化解读： 存量 Call 重｜ATM IV 67.8%｜历史 Rank 91%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,177,542 股

📆 11-30 Forward Structure
存量OI: C 26.0k / P 15.9k，今日变化ΔOI: C +6.4k / P +3.5k，平值价格ATM: C $3.83 / P $3.45 ｜ ATM IV 61.7%，净 delta 敞口 150k shares
Top ΔOI: C 130 +1,524 ｜ C 126 +747 ｜ C 140 +717
仓位参考: Max Pain 130 ｜ Call Wall 140（+9.9%）（OI 6.4k） ｜ Put Wall 115（-9.8%）（OI 5.2k）
量化解读： 存量 Call 重｜ATM IV 61.7%｜历史 Rank 91%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 150,087 股

📆 12-02 Forward Structure
存量OI: C 10.4k / P 3.6k，今日变化ΔOI: C +4.4k / P +1.6k，平值价格ATM: C $5.00 / P $4.72 ｜ ATM IV 67.6%，净 delta 敞口 81k shares
Top ΔOI: C 135 +860 ｜ P 115 +374
仓位参考: Max Pain 130 ｜ Call Wall 135（+5.9%，弱）（OI 1.0k） ｜ Put Wall 115（-9.8%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 67.6%｜历史 Rank 91%（近端代理）｜IV/RV 1.08×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 81,161 股

📆 12-04 Forward Structure
存量OI: C 115.6k / P 91.5k，今日变化ΔOI: C +10.1k / P +25.2k，平值价格ATM: C $5.95 / P $5.40 ｜ ATM IV 72.2%，净 delta 敞口 22k shares
Top ΔOI: P 115 +5,268 ｜ P 100 +4,670 ｜ P 118 +2,848
仓位参考: Max Pain 137 ｜ Call Wall 137（+7.5%，弱）（OI 10.3k） ｜ Put Wall 140（+9.9%，弱）（OI 11.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.2%｜历史 Rank 91%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 22,454 股

📅 事件差分（观察，非因果）: 11-27（2D）ATM IV 67.8% vs 11-30 61.7%（差 +6.1pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/SPCX_evening.json