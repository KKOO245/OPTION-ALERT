# 期权晚报 2026-11-04（快照 16:40 ET）

📊 市场环境

SPY $766.81 ｜ QQQ $691.95
VIX 16.61 ↓20.3%（5D -1.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-05 670P ΔOI +9,854（距现价 -3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-10 710C ΔOI +7,094 占该期限总 OI 14.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 688.44 → 收盘 691.95（+0.5%） ｜ 今日高 701.45 ｜ 低 687.90 ｜ 昨收 685.28 → 收盘 691.95（+1.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-11，窗口结束前不做对错判定）

Options: P/C成交量 1.09 | OI比 1.89 | ATM IV 29.1% | Skew 2.4pp | Term 0.78 | ExpMove ±1.1%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价中性（Skew 2.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.09×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.89×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 14% ｜ P/C OI(近端) 70%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 14%）｜近端持仓结构中性（P/C OI 分位 70%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-05（1D）±1.1% ｜ 11-06（2D）±1.7% ｜ 11-09（5D）±2.0% ｜ 11-10（6D）±2.5%
   ⇒ IV–VIX Spread: +12.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -683,791,176 | GEX Change vs 上次快照 -234,974,872 | Flip: Primary Flip: 711.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 2759 / LOW 302 / INVALID 1509
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 711.53（全链重定价，覆盖 93%）
Put Wall 680（弱结构｜现价高于该位 1.8%）
最近结构参考: Put Wall 680（现价高于该位 1.8%）
量化视角： 负 Gamma（6.84亿，历史分位偏负区，比 86% 的交易日更负）｜负 Gamma 加深（2.35亿）｜现价位于 Flip 下方 2.75%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 680（Put Wall，弱结构）；上方 692（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 712（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-05  C +17.4k / P +32.2k ｜ Activity HIGH ｜ 1D
11-06  C +36.8k / P +72.0k ｜ Activity HIGH ｜ 2D
11-09  C +5.1k / P +14.4k ｜ Activity HIGH ｜ 5D
11-10  C +17.4k / P +6.9k ｜ Activity HIGH ｜ 6D

📆 11-05 Forward Structure
存量OI: C 55.9k / P 60.4k，今日变化ΔOI: C +17.4k / P +32.2k，平值价格ATM: C $4.55 / P $3.23 ｜ ATM IV 26.4%，净 delta 敞口 295k shares
Top ΔOI: P 670 +9,854 ｜ P 680 +1,760
仓位参考: Max Pain 693 ｜ Call Wall 710（+2.6%，弱）（OI 4.7k） ｜ Put Wall 680（-1.7%，弱）（OI 3.0k）
量化解读： 存量两侧均衡｜ATM IV 26.4%｜历史 Rank 88%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 295,093 股

📆 11-06 Forward Structure
存量OI: C 414.8k / P 603.4k，今日变化ΔOI: C +36.8k / P +72.0k，平值价格ATM: C $6.58 / P $4.90 ｜ ATM IV 28.0%，净 delta 敞口 505k shares
Top ΔOI: P 668 +11,661 ｜ P 672 +7,155
仓位参考: Max Pain 713 ｜ Call Wall 700（+1.2%，弱）（OI 18.3k） ｜ Put Wall 675（-2.4%，弱）（OI 46.2k）
量化解读： 存量 Put 重｜ATM IV 28.0%｜历史 Rank 88%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 504,619 股

📆 11-09 Forward Structure
存量OI: C 27.8k / P 43.0k，今日变化ΔOI: C +5.1k / P +14.4k，平值价格ATM: C $7.45 / P $6.55 ｜ ATM IV 21.9%，净 delta 敞口 10k shares
Top ΔOI: P 640 +4,558 ｜ P 685 +3,042 ｜ P 630 +2,864
仓位参考: Max Pain 700 ｜ Call Wall 705（+1.9%，弱）（OI 1.8k） ｜ Put Wall 685（-1.0%，弱）（OI 4.1k）
量化解读： 存量 Put 重｜ATM IV 21.9%｜历史 Rank 88%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 10,225 股

📆 11-10 Forward Structure
存量OI: C 34.4k / P 15.0k，今日变化ΔOI: C +17.4k / P +6.9k，平值价格ATM: C $8.72 / P $8.28 ｜ ATM IV 23.0%，净 delta 敞口 175k shares
Top ΔOI: C 710 +7,094 ｜ C 720 +6,574 ｜ P 671 +1,310
仓位参考: Max Pain 691 ｜ Call Wall 710（+2.6%，弱）（OI 8.3k） ｜ Put Wall 686（-0.9%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 23.0%｜历史 Rank 88%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 175,353 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/QQQ_evening.json