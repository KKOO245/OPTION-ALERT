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
🟡 **近现价集中开仓**: 11-09 710P ΔOI +33,497（距现价 -3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-09 710P ΔOI +33,497 占该期限总 OI 10.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 734.82 → 收盘 735.29（+0.1%） ｜ 今日高 742.21 ｜ 低 734.58 ｜ 昨收 733.00 → 收盘 735.29（+0.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 1.05 | OI比 0.98 | ATM IV 22.9% | Skew -1.4pp | Term 0.88 | ExpMove ±1.3%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 26% ｜ P/C OI(近端) 2%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 26%）｜近端持仓极端 Call 重（P/C OI 分位 2%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-09（3D）±1.3% ｜ 11-10（4D）±1.8% ｜ 11-11（5D）±2.1% ｜ 11-12（6D）±2.3%
   ⇒ IV–VIX Spread: -2.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,377,720,135 | GEX Change vs 上次快照 -134,340,381 | Flip: Primary Flip: 760.31（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 3002 / LOW 376 / INVALID 1416
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 760.31（全链重定价，覆盖 89%）
最近结构参考: Flip 760（现价低于该位 3.3%）
量化视角： 负 Gamma（13.78亿，历史分位 26%，中性区）｜负 Gamma 加深（1.34亿）｜现价位于 Flip 下方 3.29%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 745（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 760（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-09  C +61.1k / P +111.5k ｜ Activity HIGH ｜ 3D
11-10  C +55.1k / P +11.6k ｜ Activity HIGH ｜ 4D
11-11  C +33.1k / P +19.9k ｜ Activity HIGH ｜ 5D
11-12  C +25.2k / P +23.8k ｜ Activity HIGH ｜ 6D

📆 11-09 Forward Structure
存量OI: C 111.3k / P 208.6k，今日变化ΔOI: C +61.1k / P +111.5k，平值价格ATM: C $5.26 / P $4.25 ｜ ATM IV 17.8%，净 delta 敞口 443k shares
Top ΔOI: P 710 +33,497 ｜ P 725 +33,465 ｜ P 675 +8,712
仓位参考: Max Pain 747 ｜ Call Wall 750（+2.0%，弱）（OI 5.1k） ｜ Put Wall 725（-1.4%，弱）（OI 35.8k）
量化解读： 存量 Put 重｜ATM IV 17.8%｜历史 Rank 91%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 443,343 股

📆 11-10 Forward Structure
存量OI: C 109.1k / P 77.0k，今日变化ΔOI: C +55.1k / P +11.6k，平值价格ATM: C $7.18 / P $5.92 ｜ ATM IV 21.1%，净 delta 敞口 3.1M shares
Top ΔOI: C 740 +11,226 ｜ P 734 +9,701 ｜ C 750 +7,999
仓位参考: Max Pain 741 ｜ Call Wall 740（+0.6%，弱）（OI 11.3k） ｜ Put Wall 734（-0.2%）（OI 9.9k）
量化解读： 存量 Call 重｜ATM IV 21.1%｜历史 Rank 91%（近端代理）｜IV/RV 1.05×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 3,069,603 股

📆 11-11 Forward Structure
存量OI: C 58.5k / P 73.1k，今日变化ΔOI: C +33.1k / P +19.9k，平值价格ATM: C $8.30 / P $7.09 ｜ ATM IV 22.2%，净 delta 敞口 625k shares
Top ΔOI: P 700 +3,161 ｜ C 788 +3,056 ｜ P 725 +2,294
仓位参考: Max Pain 750 ｜ Call Wall 738（+0.4%，弱）（OI 1.8k） ｜ Put Wall 720（-2.1%，弱）（OI 6.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 22.2%｜历史 Rank 91%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 624,617 股

📆 11-12 Forward Structure
存量OI: C 48.5k / P 50.3k，今日变化ΔOI: C +25.2k / P +23.8k，平值价格ATM: C $9.30 / P $7.92 ｜ ATM IV 22.8%，净 delta 敞口 151k shares
Top ΔOI: P 690 +2,702 ｜ P 701 +2,157 ｜ P 700 +1,748
仓位参考: Max Pain 750 ｜ Call Wall 750（+2.0%，弱）（OI 2.1k） ｜ Put Wall 715（-2.8%）（OI 4.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 22.8%｜历史 Rank 91%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 正 151,391 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/SPY_evening.json