# 期权晚报 2026-11-10（快照 16:40 ET）

📊 市场环境

SPY $749.92 ｜ QQQ $674.76
VIX 19.46 ↓2.3%（5D -6.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-11 675P ΔOI +6,036（距现价 +0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 672.55 → 收盘 674.76（+0.3%） ｜ 今日高 680.95 ｜ 低 667.05 ｜ 昨收 679.35 → 收盘 674.76（-0.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-17，窗口结束前不做对错判定）

Options: P/C成交量 1.14 | OI比 1.14 | ATM IV 26.2% | Skew -0.0pp | Term 0.96 | ExpMove ±1.2%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.14×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.14×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 23% ｜ P/C OI(近端) 12%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 23%）｜近端持仓结构中性（P/C OI 分位 12%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-11（1D）±1.2% ｜ 11-12（2D）±1.7% ｜ 11-13（3D）±2.2% ｜ 11-16（6D）±2.5%
   ⇒ IV–VIX Spread: +6.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -438,427,708 | GEX Change vs 上次快照 -167,978,009 | Flip: Primary Flip: 687.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3767 / LOW 439 / INVALID 1886
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 687.51（全链重定价，覆盖 96%）
最近结构参考: Flip 688（现价低于该位 1.9%）
量化视角： 负 Gamma（4.38亿，历史分位偏负区，比 77% 的交易日更负）｜负 Gamma 加深（1.68亿）｜现价位于 Flip 下方 1.85%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 675（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 688（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-11  C +16.1k / P +54.8k ｜ Activity HIGH ｜ 1D
11-12  C +6.8k / P +10.1k ｜ Activity HIGH ｜ 2D
11-13  C +38.7k / P +121.7k ｜ Activity HIGH ｜ 3D
11-16  C +13.9k / P +19.2k ｜ Activity HIGH ｜ 6D

📆 11-11 Forward Structure
存量OI: C 66.8k / P 98.7k，今日变化ΔOI: C +16.1k / P +54.8k，平值价格ATM: C $4.10 / P $3.80 ｜ ATM IV 27.7%，净 delta 敞口 -605k shares
Top ΔOI: P 675 +6,036 ｜ P 670 +5,347 ｜ P 650 +4,820
仓位参考: Max Pain 675 ｜ Call Wall 690（+2.3%，弱）（OI 2.8k） ｜ Put Wall 675（+0.0%，弱）（OI 6.7k）
量化解读： 存量 Put 重｜ATM IV 27.7%｜历史 Rank 81%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 605,081 股

📆 11-12 Forward Structure
存量OI: C 52.6k / P 41.0k，今日变化ΔOI: C +6.8k / P +10.1k，平值价格ATM: C $5.99 / P $5.61 ｜ ATM IV 29.0%，净 delta 敞口 -147k shares
Top ΔOI: C 710 +1,555 ｜ P 618 +1,014
仓位参考: Max Pain 672 ｜ Call Wall 685（+1.5%，弱）（OI 1.9k） ｜ Put Wall 670（-0.7%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 29.0%｜历史 Rank 81%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 146,508 股

📆 11-13 Forward Structure
存量OI: C 287.2k / P 383.4k，今日变化ΔOI: C +38.7k / P +121.7k，平值价格ATM: C $7.62 / P $6.93 ｜ ATM IV 29.4%，净 delta 敞口 -600k shares
Top ΔOI: P 570 +24,519 ｜ P 660 +16,911
仓位参考: Max Pain 685 ｜ Call Wall 685（+1.5%，弱）（OI 8.7k） ｜ Put Wall 660（-2.2%，弱）（OI 24.6k）
量化解读： 存量 Put 重｜ATM IV 29.4%｜历史 Rank 81%（近端代理）｜IV/RV 0.85×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 600,311 股

📆 11-16 Forward Structure
存量OI: C 40.2k / P 38.0k，今日变化ΔOI: C +13.9k / P +19.2k，平值价格ATM: C $8.89 / P $8.19 ｜ ATM IV 24.7%，净 delta 敞口 -165k shares
Top ΔOI: C 702 +1,743
仓位参考: Max Pain 677
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 24.7%｜历史 Rank 81%（近端代理）｜IV/RV 0.72×（近似）｜净 delta 敞口 负 165,101 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/QQQ_evening.json