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
🟡 **近现价集中开仓**: 10-12 230C ΔOI +4,181（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 250C ΔOI +8,883 占该期限总 OI 30.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 233.88 → 收盘 229.28（-2.0%） ｜ 今日高 233.89 ｜ 低 229.11 ｜ 昨收 230.48 → 收盘 229.28（-0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.53 | OI比 1.11 | ATM IV 27.5% | Skew 15.2pp | Term 1.08 | ExpMove ±1.4%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常（Term 1.08）｜保护溢价显著（Skew 15.2pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.11×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-12（3D）±1.4% ｜ 10-14（5D）±2.5% ｜ 10-16（7D）±3.2% ｜ 10-19（10D）±3.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 324,575,140 | GEX Change vs 上次快照 34,510,973 | Flip: Primary Flip: 215.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 83%（带内） ｜ IV 有效性: VALID 672 / LOW 182 / INVALID 586
结构观察区: Primary Flip 215.46（全链重定价，覆盖 83%）
Put Wall 220（弱结构｜现价高于该位 4.2%） | Call Wall 240（弱结构｜现价低于该位 4.5%）
最近结构参考: Put Wall 220（现价高于该位 4.2%）
量化视角： 正 Gamma（3.25亿，无历史分位）｜正 Gamma 增强（+3451万）｜现价位于 Flip 上方 6.41%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 220（Put Wall，弱结构）；上方 230（MaxPain，仅结算参考） / 240（Call Wall，弱结构）。
• Gamma 区域：切换参考 215（全链重定价，覆盖 83%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-12  C +16.1k / P +21.6k ｜ Activity HIGH ｜ 3D
10-14  C +13.6k / P +5.4k ｜ Activity HIGH ｜ 5D
10-16  C +38.3k / P +32.0k ｜ Activity MEDIUM △ ｜ 7D
10-19  C +19.9k / P +1.3k ｜ Activity HIGH ｜ 10D

📆 10-12 Forward Structure
存量OI: C 55.0k / P 54.9k，今日变化ΔOI: C +16.1k / P +21.6k，平值价格ATM: C $1.30 / P $1.90 ｜ ATM IV 19.1%，净 delta 敞口 62k shares
Top ΔOI: C 230 +4,181 ｜ C 232 +3,378
仓位参考: Max Pain 232 ｜ Call Wall 240（+4.7%，弱）（OI 7.3k） ｜ Put Wall 220（-4.0%，弱）（OI 4.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 19.1%｜历史 Rank 5%（近端代理）｜IV/RV 0.90×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 61,734 股

📆 10-14 Forward Structure
存量OI: C 32.6k / P 16.0k，今日变化ΔOI: C +13.6k / P +5.4k，平值价格ATM: C $2.60 / P $3.15 ｜ ATM IV 26.9%，净 delta 敞口 83k shares
Top ΔOI: C 250 +2,532 ｜ C 240 +2,208 ｜ C 245 +2,062
仓位参考: Max Pain 232 ｜ Call Wall 250（+9.0%，弱）（OI 5.3k） ｜ Put Wall 237.5（+3.6%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 26.9%｜历史 Rank 5%（近端代理）｜IV/RV 1.27×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 83,420 股

10-16（MEDIUM △）Top ΔOI: 242C +14,860 ｜ 235C +9,853
10-16（MEDIUM △）仓位参考: Max Pain 215 ｜ Call Wall 220（-4.0%，弱）（OI 99.2k） ｜ Put Wall 220（-4.0%，弱）（OI 54.8k）

📆 10-19 Forward Structure
存量OI: C 24.4k / P 4.3k，今日变化ΔOI: C +19.9k / P +1.3k，平值价格ATM: C $3.80 / P $4.30 ｜ ATM IV 26.5%，净 delta 敞口 102k shares
Top ΔOI: C 250 +8,883 ｜ C 247 +8,776 ｜ C 235 +480
仓位参考: Max Pain 235 ｜ Call Wall 250（+9.0%，弱）（OI 9.4k） ｜ Put Wall 220（-4.0%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 26.5%｜历史 Rank 5%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 102,209 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/NVDA_evening.json