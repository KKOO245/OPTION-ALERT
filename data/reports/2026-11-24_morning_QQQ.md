# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $717.83 ｜ QQQ $637.01
VIX 27.25 ↑2.4%（5D +7.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 11-25 619P ΔOI +4,655（距现价 -3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 651.03 → 今开 640.02（-1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 643.47 ｜ 低 635.86

Options: P/C成交量 1.00 | OI比 1.55 | ATM IV 56.4% | Skew 6.0pp | Term 0.56 | ExpMove ±2.3%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜保护溢价显著（Skew 6.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.55×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 30% ｜ P/C OI(近端) 43%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 30%）｜近端持仓结构中性（P/C OI 分位 43%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-25（1D）±2.3% ｜ 11-27（3D）±2.9% ｜ 11-30（6D）±3.5% ｜ 12-01（7D）±3.9%
   ⇒ IV–VIX Spread: +29.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -307,460,705 | GEX Change vs 上次快照 -220,605,354 | Flip: Primary Flip: 653.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 3352 / LOW 405 / INVALID 1889
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 653.40（全链重定价，覆盖 94%）
最近结构参考: Flip 653（现价低于该位 1.9%）
量化视角： 负 Gamma（3.07亿，历史分位 30%，中性区）｜负 Gamma 加深（2.21亿）｜现价位于 Flip 下方 1.88%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 650（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 653（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 565.0P — Vol 37,241 | 最新价 $4.31 | OI 8178→41663 (ΔOI +33485张) | ΔOI/Volume 89.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33485张（+409.4% vs前日OI），连续性待观察（方向未知）
12-18 540.0P — Vol 36,432 | 最新价 $2.66 | OI 19455→51144 (ΔOI +31689张) | ΔOI/Volume 87.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31689张（+162.9% vs前日OI），连续性待观察（方向未知）
12-18 590.0P — Vol 43,244 | 最新价 $6.66 | OI 31672→62908 (ΔOI +31236张) | ΔOI/Volume 72.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31236张（+98.6% vs前日OI），连续性待观察（方向未知）
12-18 635.0P — Vol 36,307 | 最新价 $15.80 | OI 8559→39656 (ΔOI +31097张) | ΔOI/Volume 85.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31097张（+363.3% vs前日OI），连续性待观察（方向未知）
11-27 550.0P — Vol 29,120 | 最新价 $0.18 | OI 3782→31483 (ΔOI +27701张) | ΔOI/Volume 95.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增27701张（+732.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 155,208 张（Put 155,208 / Call 0），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $93M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 131.9k / P 204.6k，今日成交量: C 471.2k / P 470.5k，平值价格ATM: C $3.74 / P $4.10 ｜ ATM IV 56.4%，预期波动 ±1.2%，Max Pain 650
Top ΔOI: P 505 +7,942 ｜ P 640 +7,785 ｜ P 510 +6,618

📆 Forward Expiration Structure

11-25  C +8.7k / P +46.5k ｜ Activity HIGH ｜ 1D
11-27  C +32.2k / P +80.8k ｜ Activity HIGH ｜ 3D
11-30  C +37.5k / P +39.8k ｜ Activity MEDIUM △ ｜ 6D
12-01  C +1.9k / P +5.3k ｜ Activity HIGH ｜ 7D

📆 11-25 Forward Structure
存量OI: C 101.4k / P 101.0k，今日变化ΔOI: C +8.7k / P +46.5k，平值价格ATM: C $7.10 / P $7.49 ｜ ATM IV 48.2%，净 delta 敞口 -877k shares
Top ΔOI: P 605 +15,315 ｜ P 619 +4,655
仓位参考: Max Pain 642 ｜ Call Wall 650（+1.4%，弱）（OI 5.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 48.2%｜历史 Rank 99%（近端代理）｜IV/RV 1.04×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 876,529 股

📆 11-27 Forward Structure
存量OI: C 266.9k / P 257.1k，今日变化ΔOI: C +32.2k / P +80.8k，平值价格ATM: C $9.00 / P $9.26 ｜ ATM IV 38.3%，净 delta 敞口 -1.5M shares
Top ΔOI: P 550 +27,701 ｜ C 700 +15,529
仓位参考: Max Pain 654 ｜ Put Wall 640（-0.2%，弱）（OI 15.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.3%｜历史 Rank 99%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,474,436 股

11-30（MEDIUM △）Top ΔOI: 540P +11,169 ｜ 500P +11,167
11-30（MEDIUM △）仓位参考: Max Pain 670 ｜ Call Wall 650（+1.4%，弱）（OI 13.8k） ｜ Put Wall 650（+1.4%，弱）（OI 21.3k）

📆 12-01 Forward Structure
存量OI: C 20.8k / P 41.1k，今日变化ΔOI: C +1.9k / P +5.3k，平值价格ATM: C $12.80 / P $12.20 ｜ ATM IV 34.4%，净 delta 敞口 -158k shares
Top ΔOI: C 630 -1,140 ｜ C 650 +420
仓位参考: Max Pain 642 ｜ Call Wall 630（-1.7%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 34.4%｜历史 Rank 99%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 负 157,669 股

📅 事件差分（观察，非因果）: 11-25（1D）ATM IV 48.2% vs 11-27 38.3%（差 +9.9pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/QQQ_morning.json