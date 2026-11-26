# 期权晨报 2026-11-25（快照 10:20 ET）

📊 市场环境

SPY $720.30 ｜ QQQ $633.93
VIX 31.62 ↑19.9%（5D +28.8%） ｜ Vol Regime: STRESS
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
🟡 **近现价集中开仓**: 11-27 75P ΔOI +6,673（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 77.95 → 今开 71.32（-8.5%） | 较昨收变动（含盘初走势） ｜ 今日高 72.60 ｜ 低 68.93

Options: P/C成交量 1.00 | OI比 0.44 | ATM IV 141.2% | Skew 12.9pp | Term 0.91 | ExpMove ±8.5%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构正常（Term 0.91）｜保护溢价显著（Skew 12.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（2D）±8.5% ｜ 12-04（9D）±17.7% ｜ 12-11（16D）±22.5% ｜ 12-18（23D）±25.7%
   ⇒ IV–VIX Spread: +109.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -36,452,682 | GEX Change vs 上次快照 -2,415,239 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1086 / LOW 964 / INVALID 3920
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 75（现价低于该位 4.5%）
最近结构参考: Put Wall 75（现价低于该位 4.5%）
量化视角： 负 Gamma（3645万，无历史分位）｜负 Gamma 加深（242万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 75（Put Wall） / 90（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 75.0P — Vol 16,118 | 最新价 $2.30 | OI 3980→10653 (ΔOI +6673张) | ΔOI/Volume 41.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6673张（+167.7% vs前日OI），连续性待观察（方向未知）
11-27 60.0P — Vol 1,404 | 最新价 $0.10 | OI 921→5548 (ΔOI +4627张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4627张（+502.4% vs前日OI），连续性待观察（方向未知）
11-27 65.0P — Vol 5,847 | 最新价 $0.38 | OI 809→5377 (ΔOI +4568张) | ΔOI/Volume 78.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4568张（+564.6% vs前日OI），连续性待观察（方向未知）
12-18 70.0P — Vol 3,972 | 最新价 $5.75 | OI 5323→8302 (ΔOI +2979张) | ΔOI/Volume 75.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2979张（+56.0% vs前日OI），连续性待观察（方向未知）
12-18 100.0C — Vol 5,177 | 最新价 $2.58 | OI 5111→7708 (ΔOI +2597张) | ΔOI/Volume 50.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2597张（+50.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 21,444 张（Put 18,847 / Call 2,597），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +11.2k / P +3.4k ｜ Activity HIGH ｜ 2D
12-04  C +7.6k / P -1.2k ｜ Activity MEDIUM △ ｜ 9D
12-11  C +1.2k / P -0.3k ｜ Activity HIGH ｜ 16D
12-18  C +7.1k / P -15.7k ｜ Activity MEDIUM △ ｜ 23D

📆 11-27 Forward Structure
存量OI: C 308.6k / P 135.1k，今日变化ΔOI: C +11.2k / P +3.4k，平值价格ATM: C $3.10 / P $2.99 ｜ ATM IV 141.2%，净 delta 敞口 1.6M shares
Top ΔOI: P 75 +6,673 ｜ P 60 +4,627 ｜ P 65 +4,568
仓位参考: Max Pain 90 ｜ Put Wall 75（+4.7%）（OI 10.7k）
量化解读： 存量 Call 重｜ATM IV 141.2%｜历史 Rank 88%（近端代理）｜IV/RV 0.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,555,269 股

12-04（MEDIUM △）Top ΔOI: 100C +1,557 ｜ 85C +833
12-04（MEDIUM △）仓位参考: Max Pain 100 ｜ Put Wall 71.25（-0.5%，弱）（OI 2.8k）

📆 12-11 Forward Structure
存量OI: C 61.0k / P 44.0k，今日变化ΔOI: C +1.2k / P -0.3k，平值价格ATM: C $8.50 / P $7.60 ｜ ATM IV 133.1%，净 delta 敞口 168k shares
Top ΔOI: P 57 +715 ｜ P 106 -672
仓位参考: Max Pain 102 ｜ Call Wall 70（-2.2%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 133.1%｜历史 Rank 88%（近端代理）｜IV/RV 0.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 168,071 股

12-18（MEDIUM △）Top ΔOI: 156P -4,277 ｜ 162P -3,835
12-18（MEDIUM △）仓位参考: Max Pain 111 ｜ Put Wall 75（+4.7%，弱）（OI 44.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/SNDK_morning.json