# 期权晚报 2026-10-27（快照 16:40 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $721.25
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-28 85C ΔOI +545（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-04 86C ΔOI +81 占该期限总 OI 10.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 81.37 → 收盘 83.19（+2.2%） ｜ 今日高 83.23 ｜ 低 81.04 ｜ 昨收 81.02 → 收盘 83.19（+2.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-03，窗口结束前不做对错判定）

Options: P/C成交量 0.63 | OI比 1.63 | ATM IV 50.6% | Skew 3.7pp | Term 0.77 | ExpMove ±2.5%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价中性（Skew 3.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.63×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.63×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-28（1D）±2.5% ｜ 10-30（3D）±3.5% ｜ 11-02（6D）±3.9% ｜ 11-04（8D）±2.5%
   ⇒ IV–VIX Spread: +33.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 53,785,117 | GEX Change vs 上次快照 15,366,842 | Flip: Primary Flip: 79.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 510 / LOW 136 / INVALID 542
结构观察区: Primary Flip 79.39（全链重定价，覆盖 99%）
Put Wall 80（弱结构｜现价高于该位 4.0%） | Call Wall 85（弱结构｜现价低于该位 2.1%）
最近结构参考: Call Wall 85（现价低于该位 2.1%）
量化视角： 正 Gamma（5379万，无历史分位）｜正 Gamma 增强（+1537万）｜现价位于 Flip 上方 4.79%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 84（MaxPain，仅结算参考） / 85（Call Wall，弱结构）。
• Gamma 区域：切换参考 79（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 82.0C — Vol 606 | 最新价 $1.14 | OI 502→19113 (ΔOI +18611张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18611张（+3707.4% vs前日OI），连续性待观察（方向未知）
10-30 85.0C — Vol 1,299 | 最新价 $0.35 | OI 11174→27547 (ΔOI +16373张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16373张（+146.5% vs前日OI），连续性待观察（方向未知）
10-30 83.0C — Vol 1,134 | 最新价 $0.83 | OI 58→9138 (ΔOI +9080张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9080张（+15655.2% vs前日OI），连续性待观察（方向未知）
10-30 81.0C — Vol 386 | 最新价 $1.62 | OI 73→9151 (ΔOI +9078张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9078张（+12435.6% vs前日OI），连续性待观察（方向未知）
10-30 76.0P — Vol 264 | 最新价 $0.22 | OI 35→4059 (ΔOI +4024张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4024张（+11497.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 57,166 张（Put 4,024 / Call 53,142），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-28  C +1.8k / P +0.6k ｜ Activity HIGH ｜ 1D
10-30  C +2.7k / P +0.1k ｜ Activity HIGH ｜ 3D
11-02  C +0.1k / P +0.1k ｜ Activity MEDIUM △ ｜ 6D
11-04  C +0.1k / P +24 ｜ Activity HIGH ｜ 8D

📆 10-28 Forward Structure
存量OI: C 3.7k / P 6.0k，今日变化ΔOI: C +1.8k / P +0.6k，平值价格ATM: C $0.94 / P $1.10 ｜ ATM IV 50.6%，净 delta 敞口 89k shares
Top ΔOI: P 76 +549 ｜ C 85 +545 ｜ C 81 +323
仓位参考: Max Pain 84 ｜ Call Wall 85（+2.2%，弱）（OI 0.6k） ｜ Put Wall 84（+1.0%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.6%｜历史 Rank 82%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 88,801 股

📆 10-30 Forward Structure
存量OI: C 133.5k / P 33.4k，今日变化ΔOI: C +2.7k / P +0.1k，平值价格ATM: C $1.51 / P $1.36 ｜ ATM IV 47.9%，净 delta 敞口 130k shares
Top ΔOI: C 85 +618 ｜ C 83 +552 ｜ C 84 +358
仓位参考: Max Pain 81 ｜ Call Wall 85（+2.2%，弱）（OI 28.2k） ｜ Put Wall 79（-5.0%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 47.9%｜历史 Rank 82%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 130,354 股

11-02（MEDIUM △）Top ΔOI: 90C +91 ｜ 76P +62
11-02（MEDIUM △）仓位参考: Max Pain 86 ｜ Call Wall 86（+3.4%）（OI 0.5k） ｜ Put Wall 81（-2.6%）（OI 0.3k）

📆 11-04 Forward Structure
存量OI: C 0.7k / P 83，今日变化ΔOI: C +0.1k / P +24，平值价格ATM: C $2.04 / P $0.00 ｜ ATM IV 42.7%，净 delta 敞口 2k shares
Top ΔOI: C 86 +81 ｜ P 86 +10
仓位参考: Max Pain 82 ｜ Call Wall 83（-0.2%，弱）（OI 0.2k） ｜ Put Wall 80（-3.8%，弱）（OI 18）
量化解读： 存量 Call 重｜ATM IV 42.7%｜历史 Rank 82%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 2,227 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/GDX_evening.json