# 期权晚报 2026-11-06（快照 21:00 ET）

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

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 191.14 → 收盘 186.64（-2.4%） ｜ 今日高 194.90 ｜ 低 185.22 ｜ 昨收 181.60 → 收盘 186.64（+2.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-11，窗口结束前不做对错判定）

Options: P/C成交量 1.01 | OI比 0.86 | ATM IV 49.8% | Skew 7.5pp | Term 0.85 | ExpMove ±3.7%（近端） | Rank 72%
量化视角： IV 中性（Rank 72%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价显著（Skew 7.5pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.86×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-09（3D）±3.7% ｜ 11-11（5D）±5.6% ｜ 11-13（7D）±6.8% ｜ 11-16（10D）±7.3%
   ⇒ IV–VIX Spread: +24.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -27,231,655 | GEX Change vs 上次快照 -103,648,919 | Flip: Primary Flip: 189.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 694 / LOW 126 / INVALID 666
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 189.79（全链重定价，覆盖 100%）
Put Wall 190（弱结构｜现价低于该位 1.8%）
最近结构参考: Flip 190（现价低于该位 1.7%）
量化视角： 负 Gamma（2723万，无历史分位）｜由正转负（1.04亿）｜现价位于 Flip 下方 1.66%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 190（Put Wall，弱结构） / 192（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 190（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-09  C +0 / P +0 ｜ Activity LOW ｜ 3D
11-11  C +0 / P +0 ｜ Activity LOW ｜ 5D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-16  C +0 / P +0 ｜ Activity LOW ｜ 10D

📆 11-09 Forward Structure
存量OI: C 51.6k / P 44.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.05 / P $3.81 ｜ ATM IV 49.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 192 ｜ Call Wall 200（+7.2%，弱）（OI 4.2k） ｜ Put Wall 180（-3.6%，弱）（OI 5.3k）
量化解读： 存量两侧均衡｜ATM IV 49.8%｜历史 Rank 72%（近端代理）｜IV/RV 1.10×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-11（Activity LOW）仓位参考: Max Pain 192 ｜ Call Wall 195（+4.5%，弱）（OI 4.1k） ｜ Put Wall 170（-8.9%，弱）（OI 3.5k）

11-13（Activity LOW）仓位参考: Max Pain 198 ｜ Call Wall 197.5（+5.8%，弱）（OI 18.1k） ｜ Put Wall 205（+9.8%，弱）（OI 12.5k）

11-16（Activity LOW）仓位参考: Max Pain 190 ｜ Call Wall 205（+9.8%，弱）（OI 1.4k） ｜ Put Wall 175（-6.2%，弱）（OI 0.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/NVDA_evening.json