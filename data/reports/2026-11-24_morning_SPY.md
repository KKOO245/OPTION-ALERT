# 期权晨报 2026-11-24（快照 10:20 ET）

📊 市场环境

SPY $717.83 ｜ QQQ $636.95
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
🟡 **近现价集中开仓**: 11-25 735C ΔOI +4,596（距现价 +2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPY  昨收 722.29 → 今开 715.15（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 720.92 ｜ 低 712.14

Options: P/C成交量 0.79 | OI比 1.08 | ATM IV 41.1% | Skew 3.3pp | Term 0.58 | ExpMove ±1.5%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.58，近月 IV 高于远月）｜保护溢价中性（Skew 3.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.79×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.08×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 39% ｜ P/C OI(近端) 3%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 39%）｜近端持仓极端 Call 重（P/C OI 分位 3%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-25（1D）±1.5% ｜ 11-27（3D）±0.0% ｜ 11-30（6D）±2.4% ｜ 12-01（7D）±2.7%
   ⇒ IV–VIX Spread: +13.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -762,396,746 | GEX Change vs 上次快照 -178,075,763 | Flip: Primary Flip: 733.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3307 / LOW 473 / INVALID 1954
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 733.66（全链重定价，覆盖 96%）
最近结构参考: Flip 734（现价低于该位 1.9%）
量化视角： 负 Gamma（7.62亿，历史分位 39%，中性区）｜负 Gamma 加深（1.78亿）｜现价位于 Flip 下方 1.89%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 722（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 734（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-07 700.0P — Vol 34,303 | 最新价 $5.85 | OI 0→33808 (ΔOI +33808张) | ΔOI/Volume 98.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33808张（前日OI缺失），连续性待观察（方向未知）
12-07 675.0P — Vol 34,036 | 最新价 $2.69 | OI 0→33685 (ΔOI +33685张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33685张（前日OI缺失），连续性待观察（方向未知）
12-11 675.0P — Vol 33,969 | 最新价 $3.97 | OI 1758→35069 (ΔOI +33311张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增33311张（+1894.8% vs前日OI），连续性待观察（方向未知）
12-11 700.0P — Vol 36,951 | 最新价 $7.66 | OI 4657→36373 (ΔOI +31716张) | ΔOI/Volume 85.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31716张（+681.0% vs前日OI），连续性待观察（方向未知）
11-30 600.0P — Vol 12,360 | 最新价 $0.13 | OI 2929→13196 (ΔOI +10267张) | ΔOI/Volume 83.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10267张（+350.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 142,787 张（Put 142,787 / Call 0），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $66M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 214.5k / P 231.2k，今日成交量: C 738.5k / P 579.7k，平值价格ATM: C $3.13 / P $3.26 ｜ ATM IV 41.1%，预期波动 ±0.9%，Max Pain 722
Top ΔOI: C 740 +7,318 ｜ P 715 +7,125 ｜ C 730 +6,355

📆 Forward Expiration Structure

11-25  C +23.7k / P +28.6k ｜ Activity HIGH ｜ 1D
11-27  C +0.3k / P -53.1k ｜ Activity MEDIUM △ ｜ 3D
11-30  C +7.7k / P -7.6k ｜ Activity HIGH ｜ 6D
12-01  C +4.1k / P +8.8k ｜ Activity HIGH ｜ 7D

📆 11-25 Forward Structure
存量OI: C 170.2k / P 112.9k，今日变化ΔOI: C +23.7k / P +28.6k，平值价格ATM: C $5.54 / P $5.51 ｜ ATM IV 32.8%，净 delta 敞口 -1.0M shares
Top ΔOI: C 735 +4,596 ｜ C 740 +4,358 ｜ C 739 +3,885
仓位参考: Max Pain 717 ｜ Call Wall 730（+1.4%，弱）（OI 10.0k） ｜ Put Wall 734（+2.0%）（OI 12.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.8%｜历史 Rank 99%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,022,088 股

11-27（MEDIUM △）Top ΔOI: 660P -49,651 ｜ 680P -49,523
11-27（MEDIUM △）仓位参考: Max Pain 725 ｜ Call Wall 730（+1.4%，弱）（OI 13.9k） ｜ Put Wall 700（-2.7%，弱）（OI 34.1k）

📆 11-30 Forward Structure
存量OI: C 345.9k / P 681.6k，今日变化ΔOI: C +7.7k / P -7.6k，平值价格ATM: C $8.75 / P $8.40 ｜ ATM IV 22.8%，净 delta 敞口 -296k shares
Top ΔOI: P 570 -27,877 ｜ P 675 -22,457 ｜ P 600 +10,267
仓位参考: Max Pain 735 ｜ Call Wall 740（+2.8%，弱）（OI 6.8k） ｜ Put Wall 700（-2.7%，弱）（OI 29.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 22.8%｜历史 Rank 99%（近端代理）｜IV/RV 0.73×（近似）｜净 delta 敞口 负 295,791 股

📆 12-01 Forward Structure
存量OI: C 52.5k / P 29.2k，今日变化ΔOI: C +4.1k / P +8.8k，平值价格ATM: C $9.83 / P $9.55 ｜ ATM IV 23.5%，净 delta 敞口 -182k shares
Top ΔOI: P 703 +3,929 ｜ C 760 +605
仓位参考: Max Pain 722 ｜ Call Wall 740（+2.8%，弱）（OI 0.9k） ｜ Put Wall 703（-2.3%）（OI 4.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 23.5%｜历史 Rank 99%（近端代理）｜IV/RV 0.75×（近似）｜净 delta 敞口 负 182,450 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/SPY_morning.json