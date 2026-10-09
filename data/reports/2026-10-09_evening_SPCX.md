# 期权晚报 2026-10-09（快照 16:40 ET）

📊 市场环境

SPY $778.57 ｜ QQQ $751.27
VIX 14.84 ↓3.7%（5D -3.1%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 45.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 46.3 ｜ 前值 48.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-12 162C ΔOI +3,149（距现价 -0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 165.34 → 收盘 162.57（-1.7%） ｜ 今日高 166.38 ｜ 低 160.61 ｜ 昨收 160.57 → 收盘 162.57（+1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.57 | OI比 1.02 | ATM IV 35.6% | Skew 40.3pp | Term 1.35 | ExpMove ±2.2%（近端） | Rank 1%
量化视角： IV 历史低位（Rank 1%，期权偏便宜）｜期限结构正常偏陡（Term 1.35）｜保护溢价显著（Skew 40.3pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.57×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.02×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-12（3D）±2.2% ｜ 10-14（5D）±3.8% ｜ 10-16（7D）±4.8% ｜ 10-19（10D）±5.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 51,752,589 | GEX Change vs 上次快照 -6,255,251 | Flip: Primary Flip: 157.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 644 / LOW 159 / INVALID 497
结构观察区: Primary Flip 157.00（全链重定价，覆盖 85%）
最近结构参考: Flip 157（现价高于该位 3.5%）
量化视角： 正 Gamma（5175万，无历史分位）｜正 Gamma 减弱（626万）｜现价位于 Flip 上方 3.55%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 162（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 157（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-12  C +10.3k / P +1.4k ｜ Activity HIGH ｜ 3D
10-14  C +4.1k / P +2.8k ｜ Activity HIGH ｜ 5D
10-16  C +9.3k / P +11.6k ｜ Activity MEDIUM △ ｜ 7D
10-19  C -0.8k / P -2 ｜ Activity HIGH ｜ 10D

📆 10-12 Forward Structure
存量OI: C 46.4k / P 20.5k，今日变化ΔOI: C +10.3k / P +1.4k，平值价格ATM: C $1.85 / P $1.79 ｜ ATM IV 30.2%，净 delta 敞口 495k shares
Top ΔOI: C 162 +3,149 ｜ C 165 +2,783 ｜ P 165 -1,424
仓位参考: Max Pain 165 ｜ Call Wall 170（+4.6%，弱）（OI 6.7k） ｜ Put Wall 150（-7.7%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 30.2%｜历史 Rank 1%（近端代理）｜IV/RV 0.63×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 495,336 股

📆 10-14 Forward Structure
存量OI: C 11.3k / P 6.6k，今日变化ΔOI: C +4.1k / P +2.8k，平值价格ATM: C $3.05 / P $3.05 ｜ ATM IV 40.5%，净 delta 敞口 39k shares
Top ΔOI: C 170 +797 ｜ C 167 +673 ｜ C 165 +596
仓位参考: Max Pain 168 ｜ Call Wall 170（+4.6%，弱）（OI 1.7k） ｜ Put Wall 165（+1.5%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 40.5%｜历史 Rank 1%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,242 股

10-16（MEDIUM △）Top ΔOI: 152P +3,414 ｜ 160P +3,067
10-16（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 170（+4.6%，弱）（OI 28.2k） ｜ Put Wall 150（-7.7%，弱）（OI 24.6k）

📆 10-19 Forward Structure
存量OI: C 7.0k / P 4.0k，今日变化ΔOI: C -0.8k / P -2，平值价格ATM: C $4.35 / P $4.03 ｜ ATM IV 40.4%，净 delta 敞口 12k shares
Top ΔOI: C 175 -85
仓位参考: Max Pain 168 ｜ Put Wall 165（+1.5%）（OI 1.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 40.4%｜历史 Rank 1%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 正 12,147 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/SPCX_evening.json