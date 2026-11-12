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
🟡 **近现价集中开仓**: 11-13 755P ΔOI +14,431（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-18 680P ΔOI +10,839 占该期限总 OI 10.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 753.98 → 收盘 757.12（+0.4%） ｜ 今日高 763.03 ｜ 低 753.70 ｜ 昨收 759.81 → 收盘 757.12（-0.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 1.05 | OI比 1.42 | ATM IV 19.6% | Skew -1.5pp | Term 0.75 | ExpMove ±0.8%（近端） | Rank 83%
量化视角： IV 历史高位（Rank 83%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.42×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 40% ｜ P/C OI(近端) 18%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 40%）｜近端持仓结构中性（P/C OI 分位 18%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-13（1D）±0.8% ｜ 11-16（4D）±1.1% ｜ 11-17（5D）±1.3% ｜ 11-18（6D）±1.6%
   ⇒ IV–VIX Spread: +0.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -698,819,252 | GEX Change vs 上次快照 45,316,825 | Flip: Primary Flip: 762.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3018 / LOW 439 / INVALID 1851
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 762.01（全链重定价，覆盖 95%）
最近结构参考: Flip 762（现价低于该位 0.6%）
量化视角： 负 Gamma（6.99亿，历史分位 40%，中性区）｜负 Gamma 缓解（+4532万）｜现价位于 Flip 下方 0.64%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 757（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 762（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +27.4k / P +50.7k ｜ Activity HIGH ｜ 1D
11-16  C +8.4k / P +30.0k ｜ Activity HIGH ｜ 4D
11-17  C +0.4k / P +6.5k ｜ Activity HIGH ｜ 5D
11-18  C +8.3k / P +34.6k ｜ Activity HIGH ｜ 6D

📆 11-13 Forward Structure
存量OI: C 392.3k / P 594.1k，今日变化ΔOI: C +27.4k / P +50.7k，平值价格ATM: C $3.35 / P $2.30 ｜ ATM IV 17.6%，净 delta 敞口 -3.1M shares
Top ΔOI: P 755 +14,431 ｜ C 770 +8,954 ｜ P 763 +8,259
仓位参考: Max Pain 758 ｜ Call Wall 776（+2.5%，弱）（OI 20.9k） ｜ Put Wall 760（+0.4%，弱）（OI 34.9k）
量化解读： 存量 Put 重｜ATM IV 17.6%｜历史 Rank 83%（近端代理）｜IV/RV 0.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,113,060 股

📆 11-16 Forward Structure
存量OI: C 90.2k / P 111.0k，今日变化ΔOI: C +8.4k / P +30.0k，平值价格ATM: C $4.64 / P $3.52 ｜ ATM IV 12.8%，净 delta 敞口 -1.8M shares
Top ΔOI: P 763 +19,902 ｜ P 758 +2,280 ｜ C 775 +1,372
仓位参考: Max Pain 763 ｜ Call Wall 770（+1.7%）（OI 6.9k） ｜ Put Wall 763（+0.8%）（OI 20.1k）
量化解读： 存量 Put 重｜ATM IV 12.8%｜历史 Rank 83%（近端代理）｜IV/RV 0.58×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,779,830 股

📆 11-17 Forward Structure
存量OI: C 36.0k / P 38.7k，今日变化ΔOI: C +0.4k / P +6.5k，平值价格ATM: C $5.61 / P $4.39 ｜ ATM IV 14.0%，净 delta 敞口 -101k shares
Top ΔOI: C 782 -2,359 ｜ P 742 +668
仓位参考: Max Pain 750 ｜ Call Wall 774（+2.2%，弱）（OI 1.7k） ｜ Put Wall 750（-0.9%，弱）（OI 2.0k）
量化解读： 存量两侧均衡｜ATM IV 14.0%｜历史 Rank 83%（近端代理）｜IV/RV 0.63×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 101,006 股

📆 11-18 Forward Structure
存量OI: C 38.1k / P 67.6k，今日变化ΔOI: C +8.3k / P +34.6k，平值价格ATM: C $6.51 / P $5.51 ｜ ATM IV 15.0%，净 delta 敞口 -170k shares
Top ΔOI: P 680 +10,839 ｜ P 650 +6,775
仓位参考: Max Pain 753 ｜ Call Wall 764（+0.9%，弱）（OI 1.7k） ｜ Put Wall 740（-2.3%，弱）（OI 7.4k）
量化解读： 存量 Put 重｜ATM IV 15.0%｜历史 Rank 83%（近端代理）｜IV/RV 0.68×（近似）｜净 delta 敞口 负 169,584 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/SPY_evening.json