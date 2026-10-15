# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $770.81 ｜ QQQ $724.05
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🔴 **事件差分**: 10-16（1D）ATM IV 135.0% vs 10-23 93.9%（差 +41.1pp），覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-30 170P ΔOI +502（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 186.01 → 今开 175.48（-5.7%） | 较昨收变动（含盘初走势） ｜ 今日高 176.58 ｜ 低 163.36

Options: P/C成交量 0.81 | OI比 0.74 | ATM IV 135.0% | Skew 14.1pp | Term 0.71 | ExpMove ±6.5%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价显著（Skew 14.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（1D）±6.5% ｜ 10-23（8D）±11.0% ｜ 10-30（15D）±15.4% ｜ 11-06（22D）±18.2%
   ⇒ IV–VIX Spread: +117.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -21,842,305 | GEX Change vs 上次快照 2,172,417 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 540 / LOW 54 / INVALID 188
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
量化视角： 负 Gamma（2184万，无历史分位）｜负 Gamma 缓解（+217万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 210（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 230.0C — Vol 18,998 | 最新价 $0.11 | OI 14221→28905 (ΔOI +14684张) | ΔOI/Volume 77.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14684张（+103.3% vs前日OI），连续性待观察（方向未知）
10-23 200.0C — Vol 8,100 | 最新价 $4.59 | OI 282→4115 (ΔOI +3833张) | ΔOI/Volume 47.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3833张（+1359.2% vs前日OI），连续性待观察（方向未知）
11-06 240.0C — Vol 3,402 | 最新价 $2.50 | OI 1157→4288 (ΔOI +3131张) | ΔOI/Volume 92.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3131张（+270.6% vs前日OI），连续性待观察（方向未知）
10-23 275.0C — Vol 4,617 | 最新价 $0.21 | OI 283→3294 (ΔOI +3011张) | ΔOI/Volume 65.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3011张（+1064.0% vs前日OI），连续性待观察（方向未知）
11-06 230.0C — Vol 3,462 | 最新价 $3.64 | OI 474→3468 (ΔOI +2994张) | ΔOI/Volume 86.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2994张（+631.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 27,653 张（Put 0 / Call 27,653），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +28.9k / P -3.8k ｜ Activity HIGH ｜ 1D
10-23  C +16.4k / P +13.7k ｜ Activity HIGH ｜ 8D
10-30  C +4.2k / P +1.8k ｜ Activity HIGH ｜ 15D
11-06  C +7.9k / P +92 ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 162.4k / P 119.5k，今日变化ΔOI: C +28.9k / P -3.8k，平值价格ATM: C $5.74 / P $5.15 ｜ ATM IV 135.0%，净 delta 敞口 726k shares
Top ΔOI: P 220 -2,906
仓位参考: Max Pain 210 ｜ Put Wall 180（+8.2%，弱）（OI 6.3k）
量化解读： 存量 Call 重｜ATM IV 135.0%｜历史 Rank 84%（近端代理）｜IV/RV 1.90×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 725,568 股

📆 10-23 Forward Structure
存量OI: C 47.3k / P 34.9k，今日变化ΔOI: C +16.4k / P +13.7k，平值价格ATM: C $8.60 / P $9.75 ｜ ATM IV 93.9%，净 delta 敞口 -775k shares
Top ΔOI: C 200 +3,833 ｜ P 220 +2,705
仓位参考: Max Pain 212 ｜ Put Wall 180（+8.2%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 93.9%｜历史 Rank 84%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 774,528 股

📆 10-30 Forward Structure
存量OI: C 30.2k / P 20.8k，今日变化ΔOI: C +4.2k / P +1.8k，平值价格ATM: C $12.32 / P $13.39 ｜ ATM IV 92.1%，净 delta 敞口 -257 shares
Top ΔOI: C 200 +1,171 ｜ P 170 +502
仓位参考: Max Pain 215 ｜ Put Wall 180（+8.2%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 92.1%｜历史 Rank 84%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 负 257 股

📆 11-06 Forward Structure
存量OI: C 19.2k / P 13.5k，今日变化ΔOI: C +7.9k / P +92，平值价格ATM: C $15.39 / P $14.95 ｜ ATM IV 92.8%，净 delta 敞口 118k shares
Top ΔOI: C 240 +3,131 ｜ C 230 +2,994 ｜ P 200 -722
仓位参考: Max Pain 220 ｜ Put Wall 180（+8.2%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 92.8%｜历史 Rank 84%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 正 117,730 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 135.0% vs 10-23 93.9%（差 +41.1pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/NBIS_morning.json