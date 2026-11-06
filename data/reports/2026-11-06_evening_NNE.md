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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🔵 **期限 OI 集中**: 12-04 9P ΔOI +140 占该期限总 OI 28.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 10.25 → 收盘 11.11（+8.4%） ｜ 今日高 11.28 ｜ 低 9.90 ｜ 昨收 9.64 → 收盘 11.11（+15.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 1.45 | OI比 0.31 | ATM IV 240.7% | Skew 11.9pp | Term 0.34 | ExpMove ±10.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.34，近月 IV 高于远月）｜保护溢价显著（Skew 11.9pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.31）+ 当日成交偏 Put（P/C量 1.45）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.45×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±10.2% ｜ 11-20（14D）±13.5% ｜ 11-27（21D）±24.5% ｜ 12-04（28D）±4.5%
   ⇒ IV–VIX Spread: +215.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 718,176 | GEX Change vs 上次快照 -62,761 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 156 / LOW 65 / INVALID 189
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 11（现价高于该位 1.0%）
最近结构参考: Put Wall 11（现价高于该位 1.0%）
量化视角： 正 Gamma（72万，无历史分位）｜正 Gamma 减弱（6万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall）；上方 12（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +29 / P +0.3k ｜ Activity MEDIUM △ ｜ 7D
11-20  C +11 / P +0.2k ｜ Activity MEDIUM △ ｜ 14D
11-27  C -4 / P -16 ｜ Activity LOW ｜ 21D
12-04  C +17 / P +0.1k ｜ Activity HIGH ｜ 28D

📆 11-13 Forward Structure
存量OI: C 1.4k / P 1.2k，今日变化ΔOI: C +29 / P +0.3k，平值价格ATM: C $0.58 / P $0.55 ｜ ATM IV 87.4%，净 delta 敞口 4k shares
仓位参考: Max Pain 12 ｜ Call Wall 12（+8.0%，弱）（OI 0.1k） ｜ Put Wall 11（-1.0%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 87.4%｜历史 Rank 100%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,577 股

11-20（MEDIUM △）Top ΔOI: 11P +187 ｜ 10P +186
11-20（MEDIUM △）仓位参考: Max Pain 15 ｜ Put Wall 10（-10.0%，弱）（OI 0.3k）

11-27（Activity LOW）仓位参考: Max Pain 12

📆 12-04 Forward Structure
存量OI: C 0.1k / P 0.4k，今日变化ΔOI: C +17 / P +0.1k，平值价格ATM: C $0.00 / P $0.50 ｜ ATM IV 83.0%，净 delta 敞口 -915 shares
Top ΔOI: C 12 +6
仓位参考: Max Pain 14 ｜ Call Wall 10（-10.0%，弱）（OI 6）
量化解读： 存量 Put 重｜ATM IV 83.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 负 915 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/NNE_evening.json