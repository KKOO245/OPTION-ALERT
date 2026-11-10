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
🟡 **近现价集中开仓**: 11-11 747P ΔOI +2,763（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-12 744P ΔOI +18,981 占该期限总 OI 11.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 747.94 → 收盘 749.92（+0.3%） ｜ 今日高 752.14 ｜ 低 744.87 ｜ 昨收 752.69 → 收盘 749.92（-0.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-17，窗口结束前不做对错判定）

Options: P/C成交量 1.18 | OI比 1.59 | ATM IV 18.9% | Skew 1.3pp | Term 0.83 | ExpMove ±0.7%（近端） | Rank 81%
量化视角： IV 历史高位（Rank 81%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价薄（Skew 1.3pp）｜当日成交偏 Put（P/C量 1.18）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.18×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.59×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 31% ｜ P/C OI(近端) 30%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 31%）｜近端持仓结构中性（P/C OI 分位 30%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-11（1D）±0.7% ｜ 11-12（2D）±1.0% ｜ 11-13（3D）±0.1% ｜ 11-16（6D）±1.5%
   ⇒ IV–VIX Spread: -0.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,116,332,957 | GEX Change vs 上次快照 -165,055,368 | Flip: Primary Flip: 759.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3288 / LOW 325 / INVALID 1699
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 759.77（全链重定价，覆盖 95%）
最近结构参考: Flip 760（现价低于该位 1.3%）
量化视角： 负 Gamma（11.16亿，历史分位 31%，中性区）｜负 Gamma 加深（1.65亿）｜现价位于 Flip 下方 1.30%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 749（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 760（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-11  C +14.8k / P +34.1k ｜ Activity HIGH ｜ 1D
11-12  C +11.3k / P +37.8k ｜ Activity HIGH ｜ 2D
11-13  C +32.0k / P +12.6k ｜ Activity HIGH ｜ 3D
11-16  C +19.8k / P +23.1k ｜ Activity HIGH ｜ 6D

📆 11-11 Forward Structure
存量OI: C 91.1k / P 114.5k，今日变化ΔOI: C +14.8k / P +34.1k，平值价格ATM: C $2.79 / P $2.20 ｜ ATM IV 15.8%，净 delta 敞口 -609k shares
Top ΔOI: P 747 +2,763 ｜ P 740 +2,696 ｜ P 753 +2,528
仓位参考: Max Pain 750 ｜ Call Wall 770（+2.7%，弱）（OI 7.2k） ｜ Put Wall 740（-1.3%，弱）（OI 5.4k）
量化解读： 存量 Put 重｜ATM IV 15.8%｜历史 Rank 81%（近端代理）｜IV/RV 0.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 609,033 股

📆 11-12 Forward Structure
存量OI: C 66.7k / P 96.2k，今日变化ΔOI: C +11.3k / P +37.8k，平值价格ATM: C $4.07 / P $3.38 ｜ ATM IV 16.7%，净 delta 敞口 -794k shares
Top ΔOI: P 744 +18,981 ｜ P 730 +7,285 ｜ C 789 +1,973
仓位参考: Max Pain 750 ｜ Call Wall 770（+2.7%，弱）（OI 2.8k） ｜ Put Wall 744（-0.8%）（OI 19.2k）
量化解读： 存量 Put 重｜ATM IV 16.7%｜历史 Rank 81%（近端代理）｜IV/RV 0.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 794,232 股

📆 11-13 Forward Structure
存量OI: C 316.7k / P 500.9k，今日变化ΔOI: C +32.0k / P +12.6k，平值价格ATM: C $0.62 / P $0.00 ｜ ATM IV 0.0%，净 delta 敞口 -816k shares
Top ΔOI: P 715 -47,746 ｜ P 730 -43,226
仓位参考: Max Pain 753 ｜ Call Wall 760（+1.3%，弱）（OI 13.3k） ｜ Put Wall 745（-0.7%，弱）（OI 29.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜净 delta 敞口 负 816,058 股

📆 11-16 Forward Structure
存量OI: C 64.6k / P 65.4k，今日变化ΔOI: C +19.8k / P +23.1k，平值价格ATM: C $6.01 / P $5.00 ｜ ATM IV 14.2%，净 delta 敞口 -133k shares
Top ΔOI: C 794 +2,992 ｜ C 770 +2,777 ｜ C 795 +2,555
仓位参考: Max Pain 750 ｜ Call Wall 770（+2.7%）（OI 6.5k） ｜ Put Wall 740（-1.3%，弱）（OI 3.8k）
量化解读： 存量两侧均衡｜ATM IV 14.2%｜历史 Rank 81%（近端代理）｜IV/RV 0.66×（近似）｜净 delta 敞口 负 132,573 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/SPY_evening.json