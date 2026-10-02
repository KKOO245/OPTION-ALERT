# 期权晚报 2026-10-02（快照 16:40 ET）

📊 市场环境

SPY $769.64 ｜ QQQ $749.58
VIX 15.31 ↓6.6%（5D +3.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 560P ΔOI +130（距现价 -4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 590.59 → 收盘 588.90（-0.3%） ｜ 今日高 596.44 ｜ 低 587.25 ｜ 昨收 576.33 → 收盘 588.90（+2.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-09，窗口结束前不做对错判定）

Options: P/C成交量 0.55 | OI比 1.79 | ATM IV 99.7% | Skew 42.8pp | Term 0.39 | ExpMove ±3.0%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.39，近月 IV 高于远月）｜保护溢价显著（Skew 42.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.79×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±3.0% ｜ 10-16（14D）±5.1% ｜ 10-23（21D）±7.1% ｜ 10-30（28D）±8.3%
   ⇒ IV–VIX Spread: +84.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,161,030 | GEX Change vs 上次快照 -3,209,462 | Flip: Primary Flip: 561.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 500 / LOW 265 / INVALID 793
结构观察区: Primary Flip 561.01（全链重定价，覆盖 89%）
Call Wall 600（现价低于该位 1.8%）
最近结构参考: Call Wall 600（现价低于该位 1.8%）
量化视角： 正 Gamma（1116万，无历史分位）｜正 Gamma 减弱（321万）｜现价位于 Flip 上方 4.97%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 550（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 561（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +67 / P +0.8k ｜ Activity HIGH ｜ 7D
10-16  C +0.2k / P -26 ｜ Activity MEDIUM △ ｜ 14D
10-23  C +0.2k / P +87 ｜ Activity HIGH ｜ 21D
10-30  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 10-09 Forward Structure
存量OI: C 4.8k / P 4.8k，今日变化ΔOI: C +67 / P +0.8k，平值价格ATM: C $9.10 / P $8.80 ｜ ATM IV 25.7%，净 delta 敞口 -7k shares
Top ΔOI: P 550 +276 ｜ P 560 +130 ｜ P 562 +106
仓位参考: Max Pain 532 ｜ Put Wall 560（-4.9%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜ATM IV 25.7%｜历史 Rank 100%（近端代理）｜IV/RV 0.71×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 6,539 股

10-16（MEDIUM △）Top ΔOI: 570P +158
10-16（MEDIUM △）仓位参考: Max Pain 530 ｜ Call Wall 600（+1.9%）（OI 9.1k）

📆 10-23 Forward Structure
存量OI: C 1.3k / P 5.4k，今日变化ΔOI: C +0.2k / P +87，平值价格ATM: C $21.85 / P $20.11 ｜ ATM IV 35.9%，净 delta 敞口 8k shares
Top ΔOI: C 580 +31 ｜ C 555 +26
仓位参考: Max Pain 530 ｜ Call Wall 610（+3.6%，弱）（OI 0.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 35.9%｜历史 Rank 100%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 7,587 股

10-30（MEDIUM △）Top ΔOI: 555P +76 ｜ 555C +54
10-30（MEDIUM △）仓位参考: Max Pain 555

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/SOXX_evening.json