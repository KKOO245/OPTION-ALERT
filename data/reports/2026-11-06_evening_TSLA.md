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
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 348.92 → 收盘 358.22（+2.7%） ｜ 今日高 363.84 ｜ 低 347.60 ｜ 昨收 343.69 → 收盘 358.22（+4.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.74 | OI比 0.76 | ATM IV 48.9% | Skew 6.9pp | Term 1.05 | ExpMove ±3.6%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 1.05）｜保护溢价显著（Skew 6.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.74×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-09（3D）±3.6% ｜ 11-11（5D）±5.3% ｜ 11-13（7D）±6.5% ｜ 11-16（10D）±7.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,611,161 | GEX Change vs 上次快照 -12,475,009 | Flip: Primary Flip: 354.77（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1227 / LOW 146 / INVALID 887
结构观察区: Primary Flip 354.77（全链重定价，覆盖 100%）
最近结构参考: Flip 355（现价高于该位 1.0%）
量化视角： 正 Gamma（661万，无历史分位）｜正 Gamma 减弱（1248万）｜现价位于 Flip 上方 0.97%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 368（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 355（全链重定价，覆盖 100%）。
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
存量OI: C 46.5k / P 35.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $6.80 / P $6.04 ｜ ATM IV 48.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 368 ｜ Call Wall 380（+6.1%，弱）（OI 3.0k） ｜ Put Wall 380（+6.1%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 48.9%｜历史 Rank 40%（近端代理）｜IV/RV 0.91×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

11-11（Activity LOW）仓位参考: Max Pain 370 ｜ Call Wall 390（+8.9%，弱）（OI 1.7k） ｜ Put Wall 355（-0.9%，弱）（OI 0.6k）

11-13（Activity LOW）仓位参考: Max Pain 360 ｜ Call Wall 377.5（+5.4%，弱）（OI 7.4k） ｜ Put Wall 325（-9.3%，弱）（OI 2.4k）

11-16（Activity LOW）仓位参考: Max Pain 370 ｜ Call Wall 380（+6.1%，弱）（OI 0.5k） ｜ Put Wall 380（+6.1%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/TSLA_evening.json