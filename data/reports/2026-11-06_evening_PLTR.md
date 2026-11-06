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
🟡 **近现价集中开仓**: 11-13 165C ΔOI +7,714（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 158.75 → 收盘 160.38（+1.0%） ｜ 今日高 163.97 ｜ 低 157.24 ｜ 昨收 154.99 → 收盘 160.38（+3.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-13，窗口结束前不做对错判定）

Options: P/C成交量 0.82 | OI比 0.82 | ATM IV 81.5% | Skew 8.7pp | Term 0.69 | ExpMove ±6.9%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜保护溢价显著（Skew 8.7pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（7D）±6.9% ｜ 11-20（14D）±9.5% ｜ 11-27（21D）±10.8% ｜ 12-04（28D）±12.4%
   ⇒ IV–VIX Spread: +55.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,788,820 | GEX Change vs 上次快照 -5,640,351 | Flip: Primary Flip: 162.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 469 / LOW 111 / INVALID 360
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 162.15（全链重定价，覆盖 84%）
最近结构参考: Flip 162（现价低于该位 1.1%）
量化视角： 负 Gamma（279万，无历史分位）｜由正转负（564万）｜现价位于 Flip 下方 1.09%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 165（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 162（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +27.3k / P +6.0k ｜ Activity HIGH ｜ 7D
11-20  C +1.4k / P -0.6k ｜ Activity MEDIUM △ ｜ 14D
11-27  C +0.9k / P +2.4k ｜ Activity HIGH ｜ 21D
12-04  C +0.7k / P +0.5k ｜ Activity HIGH ｜ 28D

📆 11-13 Forward Structure
存量OI: C 70.2k / P 43.2k，今日变化ΔOI: C +27.3k / P +6.0k，平值价格ATM: C $5.81 / P $5.27 ｜ ATM IV 62.5%，净 delta 敞口 1.1M shares
Top ΔOI: C 165 +7,714 ｜ C 160 +6,924
仓位参考: Max Pain 162 ｜ Call Wall 165（+2.9%，弱）（OI 8.0k） ｜ Put Wall 155（-3.4%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 62.5%｜历史 Rank 92%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,122,647 股

11-20（MEDIUM △）Top ΔOI: 175C +2,203 ｜ 150P -1,725
11-20（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 165（+2.9%，弱）（OI 12.3k） ｜ Put Wall 170（+6.0%，弱）（OI 8.1k）

📆 11-27 Forward Structure
存量OI: C 15.8k / P 17.3k，今日变化ΔOI: C +0.9k / P +2.4k，平值价格ATM: C $9.17 / P $8.15 ｜ ATM IV 57.2%，净 delta 敞口 25k shares
Top ΔOI: P 115 +1,209 ｜ P 150 +867
仓位参考: Max Pain 180 ｜ Call Wall 160（-0.2%，弱）（OI 0.6k） ｜ Put Wall 150（-6.5%，弱）（OI 1.7k）
量化解读： 存量两侧均衡｜ATM IV 57.2%｜历史 Rank 92%（近端代理）｜IV/RV 1.01×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 25,146 股

📆 12-04 Forward Structure
存量OI: C 13.6k / P 8.5k，今日变化ΔOI: C +0.7k / P +0.5k，平值价格ATM: C $10.20 / P $9.63 ｜ ATM IV 55.8%，净 delta 敞口 29k shares
Top ΔOI: C 180 +208 ｜ C 175 +148
仓位参考: Max Pain 175 ｜ Call Wall 175（+9.1%，弱）（OI 0.8k） ｜ Put Wall 150（-6.5%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 55.8%｜历史 Rank 92%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 29,407 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/PLTR_evening.json