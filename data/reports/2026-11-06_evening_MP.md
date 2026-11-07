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


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 34.93 → 收盘 35.41（+1.4%） ｜ 今日高 35.80 ｜ 低 33.82 ｜ 昨收 33.74 → 收盘 35.41（+4.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.36 | OI比 0.43 | ATM IV 71.9% | Skew 5.6pp | Term 0.94 | ExpMove ±8.8%（近端） | Rank 58%
量化视角： IV 中性（Rank 58%）｜期限结构正常（Term 0.94）｜保护溢价中性（Skew 5.6pp）｜存量 Call 偏重（OI比 0.43）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.43×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±8.8% ｜ 11-20（14D）±10.9% ｜ 11-27（21D）±13.0% ｜ 12-04（28D）±14.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -802,516 | GEX Change vs 上次快照 -2,148,779 | Flip: Primary Flip: 37.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 271 / LOW 45 / INVALID 94
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 37.17（全链重定价，覆盖 100%）
Put Wall 35（现价高于该位 1.2%）
最近结构参考: Put Wall 35（现价高于该位 1.2%）
量化视角： 负 Gamma（80万，无历史分位）｜由正转负（215万）｜现价位于 Flip 下方 4.74%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 35（Put Wall）；上方 39（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 37（全链重定价，覆盖 100%）。
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
存量OI: C 7.7k / P 3.3k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.65 / P $1.45 ｜ ATM IV 71.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 39 ｜ Call Wall 35（-1.2%，弱）（OI 0.6k） ｜ Put Wall 35（-1.2%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 71.9%｜历史 Rank 58%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-20（Activity LOW）仓位参考: Max Pain 44 ｜ Put Wall 35（-1.2%）（OI 3.8k）

11-27（Activity LOW）仓位参考: Max Pain 43 ｜ Put Wall 38（+7.3%，弱）（OI 89）

12-04（Activity LOW）仓位参考: Max Pain 35 ｜ Call Wall 35（-1.2%）（OI 0.5k） ｜ Put Wall 34（-4.0%）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/MP_evening.json