# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 700P ΔOI +3,501（距现价 -2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 715.19 → 收盘 717.63（+0.3%） ｜ 今日高 722.75 ｜ 低 710.39 ｜ 昨收 718.36 → 收盘 717.63（-0.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 1.14 | OI比 1.58 | ATM IV 28.6% | Skew 2.6pp | Term 0.76 | ExpMove ±1.0%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价中性（Skew 2.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.14×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.58×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 10% ｜ P/C OI(近端) 46%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 10%）｜近端持仓结构中性（P/C OI 分位 46%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-21（1D）±1.0% ｜ 10-22（2D）±1.4% ｜ 10-23（3D）±1.8% ｜ 10-26（6D）±2.1%
   ⇒ IV–VIX Spread: +11.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -810,712,099 | GEX Change vs 上次快照 78,703,716 | Flip: Primary Flip: 733.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2776 / LOW 440 / INVALID 1818
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 733.34（全链重定价，覆盖 96%）
Put Wall 700（弱结构｜现价高于该位 2.5%）
最近结构参考: Flip 733（现价低于该位 2.1%）
量化视角： 负 Gamma（8.11亿，历史分位偏负区，比 90% 的交易日更负）｜负 Gamma 缓解（+7870万）｜现价位于 Flip 下方 2.14%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 720（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 733（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-21  C +17.1k / P +41.1k ｜ Activity HIGH ｜ 1D
10-22  C +7.4k / P +17.2k ｜ Activity HIGH ｜ 2D
10-23  C +5.6k / P +55.9k ｜ Activity HIGH ｜ 3D
10-26  C +5.8k / P +9.8k ｜ Activity HIGH ｜ 6D

📆 10-21 Forward Structure
存量OI: C 74.9k / P 97.8k，今日变化ΔOI: C +17.1k / P +41.1k，平值价格ATM: C $4.02 / P $3.25 ｜ ATM IV 24.0%，净 delta 敞口 -52k shares
Top ΔOI: P 660 +4,745 ｜ P 700 +3,501 ｜ C 720 +3,103
仓位参考: Max Pain 720 ｜ Call Wall 720（+0.3%，弱）（OI 4.4k） ｜ Put Wall 700（-2.5%）（OI 9.3k）
量化解读： 存量 Put 重｜ATM IV 24.0%｜历史 Rank 88%（近端代理）｜IV/RV 1.59×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 51,653 股

📆 10-22 Forward Structure
存量OI: C 35.5k / P 62.9k，今日变化ΔOI: C +7.4k / P +17.2k，平值价格ATM: C $5.66 / P $4.72 ｜ ATM IV 24.3%，净 delta 敞口 -15k shares
Top ΔOI: C 746 +1,091 ｜ C 745 +986
仓位参考: Max Pain 722 ｜ Call Wall 730（+1.7%，弱）（OI 1.8k） ｜ Put Wall 710（-1.1%，弱）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 24.3%｜历史 Rank 88%（近端代理）｜IV/RV 1.61×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 15,404 股

📆 10-23 Forward Structure
存量OI: C 258.5k / P 406.8k，今日变化ΔOI: C +5.6k / P +55.9k，平值价格ATM: C $6.86 / P $5.72 ｜ ATM IV 24.1%，净 delta 敞口 -584k shares
Top ΔOI: P 630 +20,390 ｜ C 740 -6,489 ｜ P 710 +4,068
仓位参考: Max Pain 726 ｜ Call Wall 735（+2.4%）（OI 24.9k） ｜ Put Wall 711（-0.9%，弱）（OI 41.4k）
量化解读： 存量 Put 重｜ATM IV 24.1%｜历史 Rank 88%（近端代理）｜IV/RV 1.59×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 584,261 股

📆 10-26 Forward Structure
存量OI: C 26.0k / P 43.5k，今日变化ΔOI: C +5.8k / P +9.8k，平值价格ATM: C $8.07 / P $6.90 ｜ ATM IV 20.2%，净 delta 敞口 -119k shares
Top ΔOI: P 690 +1,135 ｜ P 700 +840 ｜ P 719 +836
仓位参考: Max Pain 728 ｜ Call Wall 710（-1.1%，弱）（OI 0.7k） ｜ Put Wall 700（-2.5%，弱）（OI 2.6k）
量化解读： 存量 Put 重｜ATM IV 20.2%｜历史 Rank 88%（近端代理）｜IV/RV 1.34×（近似）｜净 delta 敞口 负 118,762 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/QQQ_evening.json