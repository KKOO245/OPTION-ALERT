# 期权晨报 2026-11-23（快照 10:20 ET）

📊 市场环境

SPY $723.32 ｜ QQQ $651.03
VIX 27.37 ↓23.7%（5D +19.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.4 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🟡 **近现价集中开仓**: 11-25 720C ΔOI +9,020（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 689.81 → 今开 724.33（+5.0%） | 较昨收变动（含盘初走势） ｜ 今日高 725.30 ｜ 低 713.54

Options: P/C成交量 1.02 | OI比 0.97 | ATM IV 48.7% | Skew 5.1pp | Term 0.46 | ExpMove ±1.8%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.46，近月 IV 高于远月）｜保护溢价中性（Skew 5.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.02×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 46% ｜ P/C OI(近端) 2%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 46%）｜近端持仓极端 Call 重（P/C OI 分位 2%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-24（1D）±1.8% ｜ 11-25（2D）±2.2% ｜ 11-27（4D）±2.5% ｜ 11-30（7D）±2.9%
   ⇒ IV–VIX Spread: +21.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -430,691,894 | GEX Change vs 上次快照 690,198,929 | Flip: Primary Flip: 731.84（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3503 / LOW 270 / INVALID 2001
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 731.84（全链重定价，覆盖 99%）
最近结构参考: Flip 732（现价低于该位 1.4%）
量化视角： 负 Gamma（4.31亿，历史分位 46%，中性区）｜负 Gamma 缓解（+6.90亿）｜现价位于 Flip 下方 1.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 706（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 732（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 650.0P — Vol 94,749 | 最新价 $6.65 | OI 7008→91053 (ΔOI +84045张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增84045张（+1199.3% vs前日OI），连续性待观察（方向未知）
11-27 680.0P — Vol 86,314 | 最新价 $8.83 | OI 2410→75231 (ΔOI +72821张) | ΔOI/Volume 84.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增72821张（+3021.6% vs前日OI），连续性待观察（方向未知）
11-27 660.0P — Vol 70,265 | 最新价 $4.64 | OI 4047→68592 (ΔOI +64545张) | ΔOI/Volume 91.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增64545张（+1594.9% vs前日OI），连续性待观察（方向未知）
12-04 675.0P — Vol 140,404 | 最新价 $11.67 | OI 49536→100420 (ΔOI +50884张) | ΔOI/Volume 36.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增50884张（+102.7% vs前日OI），连续性待观察（方向未知）
11-23 605.0P — Vol 37,605 | 最新价 $0.19 | OI 1165→34021 (ΔOI +32856张) | ΔOI/Volume 87.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增32856张（+2820.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 305,151 张（Put 305,151 / Call 0），跨 3 个期限｜有实质成本保护 4 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 289.8k / P 280.5k，今日成交量: C 581.3k / P 591.9k，平值价格ATM: C $3.81 / P $3.83 ｜ ATM IV 48.7%，预期波动 ±1.1%，Max Pain 706
Top ΔOI: P 605 +32,856 ｜ C 700 +14,498 ｜ C 705 +13,478

📆 Forward Expiration Structure

11-24  C +47.5k / P +73.7k ｜ Activity HIGH ｜ 1D
11-25  C +60.5k / P +23.0k ｜ Activity HIGH ｜ 2D
11-27  C +129.0k / P +112.4k ｜ Activity HIGH ｜ 4D
11-30  C +16.8k / P +37.8k ｜ Activity HIGH ｜ 7D

📆 11-24 Forward Structure
存量OI: C 134.8k / P 143.7k，今日变化ΔOI: C +47.5k / P +73.7k，平值价格ATM: C $6.50 / P $6.11 ｜ ATM IV 37.5%，净 delta 敞口 2.8M shares
Top ΔOI: P 677 +6,115
仓位参考: Max Pain 712 ｜ Call Wall 729（+1.0%，弱）（OI 5.1k） ｜ Put Wall 725（+0.4%，弱）（OI 3.8k）
量化解读： 存量两侧均衡｜ATM IV 37.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,807,264 股

📆 11-25 Forward Structure
存量OI: C 146.4k / P 84.3k，今日变化ΔOI: C +60.5k / P +23.0k，平值价格ATM: C $8.04 / P $7.97 ｜ ATM IV 34.3%，净 delta 敞口 3.6M shares
Top ΔOI: C 720 +9,020 ｜ C 695 +6,178 ｜ C 702 +5,054
仓位参考: Max Pain 713 ｜ Call Wall 730（+1.1%，弱）（OI 10.2k） ｜ Put Wall 734（+1.7%）（OI 11.9k）
量化解读： 存量 Call 重｜ATM IV 34.3%｜历史 Rank 100%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,616,376 股

📆 11-27 Forward Structure
存量OI: C 412.2k / P 408.9k，今日变化ΔOI: C +129.0k / P +112.4k，平值价格ATM: C $9.27 / P $8.60 ｜ ATM IV 28.5%，净 delta 敞口 7.8M shares
Top ΔOI: P 680 +72,821 ｜ P 660 +64,545 ｜ P 675 -32,114
仓位参考: Max Pain 722 ｜ Call Wall 730（+1.1%，弱）（OI 26.3k） ｜ Put Wall 730（+1.1%，弱）（OI 19.5k）
量化解读： 存量两侧均衡｜ATM IV 28.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,781,296 股

📆 11-30 Forward Structure
存量OI: C 338.2k / P 689.1k，今日变化ΔOI: C +16.8k / P +37.8k，平值价格ATM: C $10.40 / P $10.31 ｜ ATM IV 25.0%，净 delta 敞口 2.2M shares
Top ΔOI: P 670 +15,128 ｜ P 688 +6,925
仓位参考: Max Pain 735 ｜ Call Wall 740（+2.5%，弱）（OI 5.4k） ｜ Put Wall 727（+0.7%，弱）（OI 23.2k）
量化解读： 存量 Put 重｜ATM IV 25.0%｜历史 Rank 100%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 正 2,209,445 股

📅 事件差分（观察，非因果）: 11-25（2D）ATM IV 34.3% vs 11-27 28.5%（差 +5.8pp）——覆盖 Personal Spending MoM、PCE 物价 Price Index MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-23/SPY_morning.json