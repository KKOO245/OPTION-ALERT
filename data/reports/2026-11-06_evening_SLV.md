# 期权晚报 2026-11-06（快照 16:40 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
VIX 25.64 ↓9.0%（5D +32.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-09 45P ΔOI +438（距现价 -4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-09 44P ΔOI +5,433 占该期限总 OI 18.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 46.37 → 收盘 46.87（+1.1%） ｜ 今日高 47.13 ｜ 低 46.35 ｜ 昨收 46.93 → 收盘 46.87（-0.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 0.68 | OI比 0.34 | ATM IV 51.8% | Skew 99.2pp | Term 0.77 | ExpMove ±2.2%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价显著（Skew 99.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-09（3D）±2.2% ｜ 11-11（5D）±3.9% ｜ 11-13（7D）±4.7% ｜ 11-16（10D）±5.2%
   ⇒ IV–VIX Spread: +26.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 27,881,449 | GEX Change vs 上次快照 -10,820,106 | Flip: Primary Flip: 45.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 691 / LOW 112 / INVALID 361
结构观察区: Primary Flip 45.75（全链重定价，覆盖 88%）
最近结构参考: Flip 46（现价高于该位 2.4%）
量化视角： 正 Gamma（2788万，无历史分位）｜正 Gamma 减弱（1082万）｜现价位于 Flip 上方 2.44%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 47（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 46（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-09  C +1.8k / P +7.2k ｜ Activity HIGH ｜ 3D
11-11  C +2.2k / P +3.7k ｜ Activity HIGH ｜ 5D
11-13  C +3.6k / P +3.8k ｜ Activity HIGH ｜ 7D
11-16  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 10D

📆 11-09 Forward Structure
存量OI: C 11.4k / P 17.8k，今日变化ΔOI: C +1.8k / P +7.2k，平值价格ATM: C $0.47 / P $0.58 ｜ ATM IV 31.3%，净 delta 敞口 -63k shares
Top ΔOI: P 44 +5,433 ｜ C 50 +648 ｜ P 45 +438
仓位参考: Max Pain 46 ｜ Call Wall 50（+6.7%）（OI 2.4k） ｜ Put Wall 44.5（-5.1%）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 31.3%｜历史 Rank 85%（近端代理）｜IV/RV 0.68×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 63,188 股

📆 11-11 Forward Structure
存量OI: C 15.0k / P 10.0k，今日变化ΔOI: C +2.2k / P +3.7k，平值价格ATM: C $0.85 / P $0.96 ｜ ATM IV 40.8%，净 delta 敞口 -5k shares
Top ΔOI: C 49 +551
仓位参考: Max Pain 46 ｜ Call Wall 51（+8.8%）（OI 2.9k） ｜ Put Wall 44（-6.1%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.8%｜历史 Rank 85%（近端代理）｜IV/RV 0.88×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,486 股

📆 11-13 Forward Structure
存量OI: C 58.4k / P 32.7k，今日变化ΔOI: C +3.6k / P +3.8k，平值价格ATM: C $1.04 / P $1.14 ｜ ATM IV 42.3%，净 delta 敞口 4k shares
Top ΔOI: C 51 +1,402 ｜ C 48 +854
仓位参考: Max Pain 48 ｜ Call Wall 50（+6.7%，弱）（OI 7.0k） ｜ Put Wall 45（-4.0%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.3%｜历史 Rank 85%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,012 股

📆 11-16 Forward Structure
存量OI: C 3.0k / P 1.2k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $1.17 / P $1.27 ｜ ATM IV 39.1%，净 delta 敞口 4k shares
Top ΔOI: C 48 +192 ｜ P 45 +126 ｜ P 43 +82
仓位参考: Max Pain 46 ｜ Call Wall 51（+8.8%）（OI 1.1k） ｜ Put Wall 45（-4.0%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 39.1%｜历史 Rank 85%（近端代理）｜IV/RV 0.85×（近似）｜净 delta 敞口 正 4,375 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/SLV_evening.json