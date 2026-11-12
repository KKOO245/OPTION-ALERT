# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 680P ΔOI +6,545（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-17 707C ΔOI +9,526 占该期限总 OI 12.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 680.21 → 收盘 688.17（+1.2%） ｜ 今日高 694.56 ｜ 低 679.84 ｜ 昨收 690.38 → 收盘 688.17（-0.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 1.01 | OI比 1.29 | ATM IV 34.4% | Skew 4.3pp | Term 0.72 | ExpMove ±1.3%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价中性（Skew 4.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.29×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 39% ｜ P/C OI(近端) 20%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 39%）｜近端持仓结构中性（P/C OI 分位 20%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-13（1D）±1.3% ｜ 11-16（4D）±1.9% ｜ 11-17（5D）±2.3% ｜ 11-18（6D）±2.7%
   ⇒ IV–VIX Spread: +15.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -173,622,317 | GEX Change vs 上次快照 87,076,438 | Flip: Primary Flip: 692.25（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3575 / LOW 528 / INVALID 1815
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 692.25（全链重定价，覆盖 95%）
Put Wall 680（弱结构｜现价高于该位 1.2%） | Call Wall 700（弱结构｜现价低于该位 1.7%）
最近结构参考: Flip 692（现价低于该位 0.6%）
量化视角： 负 Gamma（1.74亿，历史分位 39%，中性区）｜负 Gamma 缓解（+8708万）｜现价位于 Flip 下方 0.59%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 680（Put Wall，弱结构） / 688（MaxPain，仅结算参考）；上方 700（Call Wall，弱结构）。
• Gamma 区域：切换参考 692（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +24.7k / P +45.2k ｜ Activity HIGH ｜ 1D
11-16  C +10.8k / P +21.6k ｜ Activity HIGH ｜ 4D
11-17  C +16.4k / P +17.8k ｜ Activity HIGH ｜ 5D
11-18  C +6.2k / P +30.3k ｜ Activity HIGH ｜ 6D

📆 11-13 Forward Structure
存量OI: C 326.9k / P 455.0k，今日变化ΔOI: C +24.7k / P +45.2k，平值价格ATM: C $5.35 / P $3.81 ｜ ATM IV 31.2%，净 delta 敞口 -1.5M shares
Top ΔOI: P 680 +6,545 ｜ C 710 +5,411 ｜ P 678 +5,289
仓位参考: Max Pain 685 ｜ Call Wall 700（+1.7%，弱）（OI 14.4k） ｜ Put Wall 685（-0.5%，弱）（OI 26.5k）
量化解读： 存量 Put 重｜ATM IV 31.2%｜历史 Rank 93%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,549,762 股

📆 11-16 Forward Structure
存量OI: C 57.0k / P 63.0k，今日变化ΔOI: C +10.8k / P +21.6k，平值价格ATM: C $7.41 / P $5.81 ｜ ATM IV 22.8%，净 delta 敞口 -95k shares
Top ΔOI: C 700 +5,786 ｜ C 720 +2,495
仓位参考: Max Pain 685 ｜ Call Wall 700（+1.7%，弱）（OI 7.4k） ｜ Put Wall 690（+0.3%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 22.8%｜历史 Rank 93%（近端代理）｜IV/RV 0.65×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 94,745 股

📆 11-17 Forward Structure
存量OI: C 38.0k / P 40.4k，今日变化ΔOI: C +16.4k / P +17.8k，平值价格ATM: C $8.98 / P $7.13 ｜ ATM IV 25.1%，净 delta 敞口 109k shares
Top ΔOI: C 707 +9,526
仓位参考: Max Pain 676 ｜ Call Wall 707（+2.7%）（OI 10.3k）
量化解读： 存量两侧均衡｜ATM IV 25.1%｜历史 Rank 93%（近端代理）｜IV/RV 0.71×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 109,113 股

📆 11-18 Forward Structure
存量OI: C 20.9k / P 60.3k，今日变化ΔOI: C +6.2k / P +30.3k，平值价格ATM: C $10.30 / P $8.54 ｜ ATM IV 26.8%，净 delta 敞口 -139k shares
Top ΔOI: P 620 +11,137 ｜ P 600 +7,899 ｜ P 646 +2,315
仓位参考: Max Pain 678 ｜ Call Wall 700（+1.7%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 26.8%｜历史 Rank 93%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 负 138,768 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 31.2% vs 11-16 22.8%（差 +8.4pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/QQQ_evening.json