# 期权晚报 2026-11-27（快照 16:40 ET）

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

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 87.5）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 89.67 → 收盘 89.46（-0.2%） ｜ 今日高 89.88 ｜ 低 83.88 ｜ 昨收 84.99 → 收盘 89.46（+5.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.61 | OI比 0.31 | ATM IV 89.2% | Skew 25.5pp | Term 1.35 | ExpMove ±14.5%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常偏陡（Term 1.35）｜保护溢价显著（Skew 25.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±14.5% ｜ 12-11（14D）±22.2% ｜ 12-18（21D）±25.4% ｜ 12-24（27D）±26.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,417,384 | GEX Change vs 上次快照 -2,505,214 | Flip: Candidates 87.50 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 76%（带内） ｜ IV 有效性: VALID 521 / LOW 92 / INVALID 427
结构观察区: ≈88（全链重定价，覆盖 76%，CONDITIONAL）
最近结构参考: Flip 88（现价高于该位 2.2%）
量化视角： 正 Gamma（142万，无历史分位）｜正 Gamma 减弱（251万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 90（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 88（全链重定价，覆盖 76%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

12-04  C +6.7k / P +6.7k ｜ Activity HIGH ｜ 7D
12-11  C +1.9k / P +0.4k ｜ Activity HIGH ｜ 14D
12-18  C +6.6k / P +0.6k ｜ Activity MEDIUM △ ｜ 21D
12-24  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 27D

📆 12-04 Forward Structure
存量OI: C 36.7k / P 23.4k，今日变化ΔOI: C +6.7k / P +6.7k，平值价格ATM: C $6.60 / P $6.35 ｜ ATM IV 128.1%，净 delta 敞口 250k shares
Top ΔOI: C 100 +846
仓位参考: Max Pain 93 ｜ Call Wall 90（+0.6%，弱）（OI 1.2k） ｜ Put Wall 90（+0.6%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 128.1%｜历史 Rank 24%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 249,904 股

📆 12-11 Forward Structure
存量OI: C 13.2k / P 14.0k，今日变化ΔOI: C +1.9k / P +0.4k，平值价格ATM: C $8.45 / P $11.42 ｜ ATM IV 126.8%，净 delta 敞口 90k shares
Top ΔOI: C 80 +358 ｜ C 100 +220 ｜ C 90 +181
仓位参考: Max Pain 100 ｜ Call Wall 90（+0.6%，弱）（OI 0.5k） ｜ Put Wall 85（-5.0%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 126.8%｜历史 Rank 24%（近端代理）｜IV/RV 0.80×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 89,679 股

12-18（MEDIUM △）Top ΔOI: 180P -1,895 ｜ 100C +1,764
12-18（MEDIUM △）仓位参考: Max Pain 135 ｜ Put Wall 90（+0.6%，弱）（OI 4.1k）

📆 12-24 Forward Structure
存量OI: C 8.2k / P 5.0k，今日变化ΔOI: C +0.7k / P +0.2k，平值价格ATM: C $11.40 / P $12.71 ｜ ATM IV 120.3%，净 delta 敞口 22k shares
Top ΔOI: C 95 +99
仓位参考: Max Pain 115 ｜ Put Wall 90（+0.6%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 120.3%｜历史 Rank 24%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 正 21,641 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/NBIS_evening.json