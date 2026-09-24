# 期权晚报 2026-09-24（快照 16:40 ET）

📊 市场环境

SPY $767.18 ｜ QQQ $741.10
VIX 15.67 ↑3.2%（5D -11.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-25 736P ΔOI +20,675（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-28 727P ΔOI +30,125 占该期限总 OI 15.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 735.16 → 收盘 741.10（+0.8%） ｜ 今日高 742.65 ｜ 低 734.63 ｜ 昨收 741.21 → 收盘 741.10（-0.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-01，窗口结束前不做对错判定）

Options: P/C成交量 0.84 | OI比 2.15 | ATM IV 25.5% | Skew 0.2pp | Term 0.72 | ExpMove ±0.8%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价薄（Skew 0.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.15×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 57% ｜ P/C OI(近端) 83%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 57%）｜近端持仓结构中性（P/C OI 分位 83%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-25（1D）±0.8% ｜ 09-28（4D）±1.2% ｜ 09-29（5D）±1.4% ｜ 09-30（6D）±1.7%
   ⇒ IV–VIX Spread: +9.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 54,188,818 | GEX Change vs 上次快照 -572,407,654 | Flip: Primary Flip: 740.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3245 / LOW 355 / INVALID 1840
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 740.46（全链重定价，覆盖 95%）
Call Wall 760（弱结构｜现价低于该位 2.5%）
最近结构参考: Flip 740（现价高于该位 0.1%）
量化视角： 正 Gamma（5419万，历史分位 57%，中性区）｜正 Gamma 减弱（5.72亿）｜现价位于 Flip 上方 0.09%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 740（MaxPain，仅结算参考）；上方 760（Call Wall，弱结构）。
• Gamma 区域：切换参考 740（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +53.7k / P +114.2k ｜ Activity HIGH ｜ 1D（新行权价 C 1.1k）
09-28  C +22.7k / P +68.3k ｜ Activity HIGH ｜ 4D（新行权价 C 59）
09-29  C +18.0k / P +42.6k ｜ Activity HIGH ｜ 5D
09-30  C +57.5k / P +30.3k ｜ Activity HIGH ｜ 6D

📆 09-25 Forward Structure
存量OI: C 230.6k / P 552.4k，今日变化ΔOI: C +53.7k / P +114.2k（新行权价 C 1.1k），平值价格ATM: C $2.32 / P $3.40 ｜ ATM IV 18.2%，净 delta 敞口 -2.9M shares
Top ΔOI: P 736 +20,675 ｜ P 730 +10,312 ｜ C 754 +8,964
仓位参考: Max Pain 735 ｜ Call Wall 755（+1.9%）（OI 20.3k） ｜ Put Wall 736（-0.7%，弱）（OI 22.1k）
量化解读： 存量 Put 重｜ATM IV 18.2%｜历史 Rank 80%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,850,997 股

📆 09-28 Forward Structure
存量OI: C 47.8k / P 148.4k，今日变化ΔOI: C +22.7k / P +68.3k（新行权价 C 59），平值价格ATM: C $3.89 / P $4.84 ｜ ATM IV 13.9%，净 delta 敞口 -1.2M shares
Top ΔOI: P 727 +30,125 ｜ P 725 +6,908 ｜ P 735 +5,533
仓位参考: Max Pain 736 ｜ Call Wall 755（+1.9%，弱）（OI 3.5k） ｜ Put Wall 727（-1.9%）（OI 30.3k）
量化解读： 存量 Put 重｜ATM IV 13.9%｜历史 Rank 80%（近端代理）｜IV/RV 0.90×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,185,172 股

📆 09-29 Forward Structure
存量OI: C 30.9k / P 76.4k，今日变化ΔOI: C +18.0k / P +42.6k，平值价格ATM: C $4.70 / P $5.46 ｜ ATM IV 14.9%，净 delta 敞口 -440k shares
Top ΔOI: P 725 +20,052 ｜ C 768 +6,482 ｜ P 670 +3,549
仓位参考: Max Pain 734 ｜ Put Wall 725（-2.2%）（OI 20.3k）
量化解读： 存量 Put 重｜ATM IV 14.9%｜历史 Rank 80%（近端代理）｜IV/RV 0.97×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 440,004 股

📆 09-30 Forward Structure
存量OI: C 343.0k / P 527.4k，今日变化ΔOI: C +57.5k / P +30.3k，平值价格ATM: C $5.99 / P $6.70 ｜ ATM IV 16.5%，净 delta 敞口 128k shares
Top ΔOI: C 726 +34,966 ｜ C 720 -25,906 ｜ P 720 +18,185
仓位参考: Max Pain 721 ｜ Call Wall 726（-2.0%）（OI 45.2k） ｜ Put Wall 720（-2.8%，弱）（OI 51.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.5%｜历史 Rank 80%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 127,605 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/QQQ_evening.json