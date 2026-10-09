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
🟡 **近现价集中开仓**: 10-16 88C ΔOI +11,111（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 92C ΔOI +399 占该期限总 OI 39.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 85.3）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 88.64 → 收盘 89.28（+0.7%） ｜ 今日高 89.63 ｜ 低 88.25 ｜ 昨收 86.72 → 收盘 89.28（+3.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.18 | OI比 0.31 | ATM IV 43.9% | Skew 4.7pp | Term 0.93 | ExpMove ±4.2%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构正常（Term 0.93）｜保护溢价中性（Skew 4.7pp）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.18×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（7D）±4.2% ｜ 10-19（10D）±4.7% ｜ 10-21（12D）±5.6% ｜ 10-23（14D）±5.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 78,106,382 | GEX Change vs 上次快照 -24,575,237 | Flip: Candidates 85.29 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 77%（带内） ｜ IV 有效性: VALID 439 / LOW 128 / INVALID 407
结构观察区: ≈85（全链重定价，覆盖 77%，CONDITIONAL）
Put Wall 85（弱结构｜现价高于该位 5.0%） | Call Wall 90（弱结构｜现价低于该位 0.8%）
最近结构参考: Call Wall 90（现价低于该位 0.8%）
量化视角： 正 Gamma（7811万，无历史分位）｜正 Gamma 减弱（2458万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（Put Wall，弱结构） / 87（MaxPain，仅结算参考）；上方 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 77%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +26.3k / P +5.3k ｜ Activity HIGH ｜ 7D
10-19  C +0.7k / P +12 ｜ Activity HIGH ｜ 10D
10-21  C +25 / P +2.4k ｜ Activity HIGH ｜ 12D
10-23  C +0.8k / P +59 ｜ Activity HIGH ｜ 14D

📆 10-16 Forward Structure
存量OI: C 139.0k / P 114.5k，今日变化ΔOI: C +26.3k / P +5.3k，平值价格ATM: C $1.79 / P $1.95 ｜ ATM IV 37.3%，净 delta 敞口 1.2M shares
Top ΔOI: C 88 +11,111 ｜ C 91 +11,084 ｜ P 81 +3,067
仓位参考: Max Pain 89 ｜ Call Wall 88.5（-0.9%，弱）（OI 11.2k） ｜ Put Wall 90（+0.8%，弱）（OI 10.4k）
量化解读： 存量 Call 重｜ATM IV 37.3%｜历史 Rank 69%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 1,248,550 股

📆 10-19 Forward Structure
存量OI: C 0.9k / P 0.1k，今日变化ΔOI: C +0.7k / P +12，平值价格ATM: C $2.34 / P $1.89 ｜ ATM IV 35.8%，净 delta 敞口 25k shares
Top ΔOI: C 92 +399 ｜ C 90 +230 ｜ C 86 +10
仓位参考: Max Pain 86 ｜ Call Wall 92（+3.0%）（OI 0.4k） ｜ Put Wall 90（+0.8%，弱）（OI 23）
量化解读： 存量 Call 重｜ATM IV 35.8%｜历史 Rank 69%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 25,492 股

📆 10-21 Forward Structure
存量OI: C 0.6k / P 2.5k，今日变化ΔOI: C +25 / P +2.4k，平值价格ATM: C $2.61 / P $2.41 ｜ ATM IV 37.1%，净 delta 敞口 -12k shares
Top ΔOI: P 86 +5
仓位参考: Max Pain 84 ｜ Call Wall 95（+6.4%）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 37.1%｜历史 Rank 69%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 11,723 股

📆 10-23 Forward Structure
存量OI: C 7.7k / P 7.0k，今日变化ΔOI: C +0.8k / P +59，平值价格ATM: C $2.62 / P $2.61 ｜ ATM IV 37.8%，净 delta 敞口 30k shares
Top ΔOI: C 92 +368 ｜ C 90 +190 ｜ C 96 +108
仓位参考: Max Pain 92 ｜ Call Wall 90（+0.8%，弱）（OI 0.6k） ｜ Put Wall 90（+0.8%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜ATM IV 37.8%｜历史 Rank 69%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 29,516 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-09/GDX_evening.json