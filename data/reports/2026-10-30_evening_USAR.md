# 期权晚报 2026-10-30（快照 21:00 ET）

📊 市场环境

SPY $755.72 ｜ QQQ $690.49
VIX 19.42 ↑12.9%（5D -0.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 9.88 → 收盘 9.62（-2.6%） ｜ 今日高 10.04 ｜ 低 9.19 ｜ 昨收 10.52 → 收盘 9.62（-8.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-04，窗口结束前不做对错判定）

Options: P/C成交量 0.22 | OI比 0.63 | ATM IV 84.5% | Skew -6.1pp | Term 1.05 | ExpMove ±10.6%（近端） | Rank 16%
量化视角： IV 历史低位（Rank 16%，期权偏便宜）｜期限结构正常（Term 1.05）｜Put 保护异常便宜（Skew -6.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.22×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（7D）±10.6% ｜ 11-13（14D）±17.3% ｜ 11-20（21D）±17.5% ｜ 11-27（28D）±18.6%
   ⇒ IV–VIX Spread: +65.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -550,264 | GEX Change vs 上次快照 -3,790,829 | Flip: Primary Flip: 9.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 198 / LOW 53 / INVALID 85
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 9.92（全链重定价，覆盖 100%）
Put Wall 10（弱结构｜现价低于该位 3.8%）
最近结构参考: Flip 10（现价低于该位 3.0%）
量化视角： 负 Gamma（55万，无历史分位）｜由正转负（379万）｜现价位于 Flip 下方 3.05%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 10（Put Wall，弱结构） / 10（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 10（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 11-06 Forward Structure
存量OI: C 8.8k / P 5.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.52 / P $0.50 ｜ ATM IV 84.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 10 ｜ Call Wall 10（+4.0%，弱）（OI 0.8k） ｜ Put Wall 9（-6.4%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 84.5%｜历史 Rank 16%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 0 股

11-13（Activity LOW）仓位参考: Max Pain 10 ｜ Call Wall 9（-6.4%，弱）（OI 0.6k） ｜ Put Wall 9（-6.4%，弱）（OI 0.4k）

11-20（Activity LOW）仓位参考: Max Pain 13 ｜ Call Wall 9.5（-1.2%，弱）（OI 1.4k） ｜ Put Wall 10（+4.0%，弱）（OI 6.3k）

11-27（Activity LOW）仓位参考: Max Pain 10 ｜ Call Wall 10（+4.0%）（OI 1.6k） ｜ Put Wall 9.5（-1.2%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=69 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=69）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-30/USAR_evening.json