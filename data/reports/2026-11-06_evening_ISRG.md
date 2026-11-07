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


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 456.49 → 收盘 452.80（-0.8%） ｜ 今日高 463.25 ｜ 低 450.51 ｜ 昨收 468.52 → 收盘 452.80（-3.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.71 | OI比 1.18 | ATM IV 37.2% | Skew 7.5pp | Term 0.98 | ExpMove ±2.7%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常（Term 0.98）｜保护溢价显著（Skew 7.5pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.18×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（7D）±2.7% ｜ 11-20（14D）±5.0% ｜ 11-27（21D）±4.3% ｜ 12-04（28D）±7.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,046,016 | GEX Change vs 上次快照 -685,933 | Flip: Primary Flip: 415.01（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 269 / LOW 119 / INVALID 396
结构观察区: Primary Flip 415.01（全链重定价，覆盖 95%）
Call Wall 420（弱结构｜现价高于该位 7.8%）
最近结构参考: Call Wall 420（现价高于该位 7.8%）
量化视角： 正 Gamma（205万，无历史分位）｜正 Gamma 减弱（69万）｜现价位于 Flip 上方 9.11%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 440（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 415（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-27  C +0 / P +0 ｜ Activity LOW ｜ 21D
12-04  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 11-13 Forward Structure
存量OI: C 1.1k / P 1.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $9.73 / P $2.50 ｜ ATM IV 37.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 440 ｜ Call Wall 440（-2.8%，弱）（OI 0.1k） ｜ Put Wall 462.5（+2.1%，弱）（OI 0.1k）
量化解读： 存量 Put 重｜ATM IV 37.2%｜历史 Rank 29%（近端代理）｜IV/RV 0.89×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-20（Activity LOW）仓位参考: Max Pain 405 ｜ Call Wall 420（-7.2%，弱）（OI 0.8k） ｜ Put Wall 410（-9.5%，弱）（OI 0.5k）

11-27（Activity LOW）仓位参考: Max Pain 430 ｜ Call Wall 430（-5.0%，弱）（OI 64） ｜ Put Wall 410（-9.5%，弱）（OI 42）

12-04（Activity LOW）仓位参考: Max Pain 440 ｜ Call Wall 475（+4.9%）（OI 92） ｜ Put Wall 410（-9.5%，弱）（OI 24）

📅 事件差分（观察，非因果）: 11-13（7D）ATM IV 37.2% vs 11-20 32.0%（差 +5.2pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/ISRG_evening.json