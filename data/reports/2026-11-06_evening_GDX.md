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
🟡 **近现价集中开仓**: 11-09 87C ΔOI +1,119（距现价 -0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-09 87C ΔOI +1,119 占该期限总 OI 21.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 84.39 → 收盘 87.60（+3.8%） ｜ 今日高 87.60 ｜ 低 84.01 ｜ 昨收 85.75 → 收盘 87.60（+2.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 0.08 | OI比 0.46 | ATM IV 55.9% | Skew 14.9pp | Term 0.80 | ExpMove ±2.4%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 14.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.08×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-09（3D）±2.4% ｜ 11-11（5D）±4.1% ｜ 11-13（7D）±5.2% ｜ 11-16（10D）±5.7%
   ⇒ IV–VIX Spread: +30.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 16,244,489 | GEX Change vs 上次快照 -9,488,078 | Flip: Candidates 85.03 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 70%（带内） ｜ IV 有效性: VALID 476 / LOW 124 / INVALID 540
结构观察区: ≈85（全链重定价，覆盖 70%，CONDITIONAL）
最近结构参考: Flip 85（现价高于该位 3.0%）
量化视角： 正 Gamma（1624万，无历史分位）｜正 Gamma 减弱（949万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 78（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 70%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-09  C +1.2k / P +0.8k ｜ Activity HIGH ｜ 3D
11-11  C +0.2k / P +52 ｜ Activity MEDIUM △ ｜ 5D
11-13  C +16.8k / P +1.0k ｜ Activity HIGH ｜ 7D
11-16  C +0.2k / P +0.2k ｜ Activity MEDIUM △ ｜ 10D

📆 11-09 Forward Structure
存量OI: C 2.9k / P 2.3k，今日变化ΔOI: C +1.2k / P +0.8k，平值价格ATM: C $0.82 / P $1.32 ｜ ATM IV 32.9%，净 delta 敞口 55k shares
Top ΔOI: C 87 +1,119 ｜ P 84 +270 ｜ P 87 +201
仓位参考: Max Pain 83 ｜ Call Wall 87（-0.7%）（OI 1.2k） ｜ Put Wall 84（-4.1%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 32.9%｜历史 Rank 89%（近端代理）｜IV/RV 0.61×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 55,285 股

11-11（MEDIUM △）Top ΔOI: 88C +75 ｜ 87C +45
11-11（MEDIUM △）仓位参考: Max Pain 78 ｜ Call Wall 85（-3.0%）（OI 2.2k）

📆 11-13 Forward Structure
存量OI: C 29.0k / P 24.2k，今日变化ΔOI: C +16.8k / P +1.0k，平值价格ATM: C $2.12 / P $2.39 ｜ ATM IV 46.2%，净 delta 敞口 616k shares
Top ΔOI: C 92 +5,024 ｜ C 89 +4,823 ｜ C 88 +2,655
仓位参考: Max Pain 82 ｜ Call Wall 92（+5.0%，弱）（OI 5.2k） ｜ Put Wall 82（-6.4%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 46.2%｜历史 Rank 89%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 615,605 股

11-16（MEDIUM △）Top ΔOI: 87C +138 ｜ 80P +61
11-16（MEDIUM △）仓位参考: Max Pain 82 ｜ Call Wall 88（+0.5%，弱）（OI 0.1k） ｜ Put Wall 86（-1.8%，弱）（OI 51）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/GDX_evening.json