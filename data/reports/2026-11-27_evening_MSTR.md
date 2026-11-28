# 期权晚报 2026-11-27（快照 21:00 ET）

📊 市场环境

SPY $728.32 ｜ QQQ $650.99
VIX 23.81 ↓11.2%（5D -33.7%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 84.57 → 收盘 81.62（-3.5%） ｜ 今日高 84.67 ｜ 低 78.84 ｜ 昨收 79.96 → 收盘 81.62（+2.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-04，窗口结束前不做对错判定）

Options: P/C成交量 0.48 | OI比 0.89 | ATM IV 105.6% | Skew 13.5pp | Term 0.89 | ExpMove ±11.8%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜保护溢价显著（Skew 13.5pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 12-04（7D）±11.8% ｜ 12-11（14D）±16.5% ｜ 12-18（21D）±19.5% ｜ 12-24（27D）±20.6%
   ⇒ IV–VIX Spread: +81.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,830,777 | GEX Change vs 上次快照 -13,204,291 | Flip: Primary Flip: 78.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 507 / LOW 104 / INVALID 277
结构观察区: Primary Flip 78.48（全链重定价，覆盖 100%）
Call Wall 85（弱结构｜现价低于该位 4.0%）
最近结构参考: Call Wall 85（现价低于该位 4.0%）
量化视角： 正 Gamma（583万，无历史分位）｜正 Gamma 减弱（1320万）｜现价位于 Flip 上方 4.00%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 82（MaxPain，仅结算参考） / 85（Call Wall，弱结构）。
• Gamma 区域：切换参考 78（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

12-04  C +0 / P +0 ｜ Activity LOW ｜ 7D
12-11  C +0 / P +0 ｜ Activity LOW ｜ 14D
12-18  C +0 / P +0 ｜ Activity LOW ｜ 21D
12-24  C +0 / P +0 ｜ Activity LOW ｜ 27D

📆 12-04 Forward Structure
存量OI: C 140.0k / P 124.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.65 / P $4.95 ｜ ATM IV 105.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 82 ｜ Call Wall 87（+6.6%，弱）（OI 13.2k） ｜ Put Wall 80（-2.0%，弱）（OI 8.4k）
量化解读： 存量两侧均衡｜ATM IV 105.6%｜历史 Rank 84%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

12-11（Activity LOW）仓位参考: Max Pain 90 ｜ Call Wall 80（-2.0%，弱）（OI 0.6k） ｜ Put Wall 80（-2.0%，弱）（OI 3.6k）

12-18（Activity LOW）仓位参考: Max Pain 105 ｜ Call Wall 85（+4.1%，弱）（OI 9.6k） ｜ Put Wall 80（-2.0%，弱）（OI 9.1k）

12-24（Activity LOW）仓位参考: Max Pain 110 ｜ Call Wall 85（+4.1%，弱）（OI 0.4k） ｜ Put Wall 80（-2.0%，弱）（OI 1.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/MSTR_evening.json