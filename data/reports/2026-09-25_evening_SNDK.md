# 期权晚报 2026-09-25（快照 16:40 ET）

📊 市场环境

SPY $771.35 ｜ QQQ $744.50
VIX 14.87 ↓5.1%（5D +0.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 0 ｜ 前值 0.9　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 1750C ΔOI +84（距现价 -1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 1672.8）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,791.80 → 收盘 1,777.80（-0.8%） ｜ 今日高 1815.00 ｜ 低 1742.95 ｜ 昨收 1,753.62 → 收盘 1,777.80（+1.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.53 | OI比 0.98 | ATM IV 64.0% | Skew -5.4pp | Term 1.09 | ExpMove ±7.8%（近端） | Rank 19%
量化视角： IV 历史低位（Rank 19%，期权偏便宜）｜期限结构正常（Term 1.09）｜Put 保护异常便宜（Skew -5.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（7D）±7.8% ｜ 10-09（14D）±10.8% ｜ 10-16（21D）±13.3% ｜ 10-23（28D）±15.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,438,999 | GEX Change vs 上次快照 -193,853 | Flip: Candidates 1672.78 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 76%（带内） ｜ IV 有效性: VALID 1754 / LOW 452 / INVALID 1240
结构观察区: ≈1673（全链重定价，覆盖 76%，CONDITIONAL）
最近结构参考: Flip 1673（现价高于该位 6.3%）
量化视角： 正 Gamma（944万，无历史分位）｜正 Gamma 减弱（19万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,750（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1673（全链重定价，覆盖 76%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +1.5k / P +3.5k ｜ Activity HIGH ｜ 7D
10-09  C +0.9k / P +0.6k ｜ Activity HIGH ｜ 14D
10-16  C +1.2k / P +1.0k ｜ Activity HIGH ｜ 21D
10-23  C +0.3k / P +0.5k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 25.5k / P 23.5k，今日变化ΔOI: C +1.5k / P +3.5k，平值价格ATM: C $68.49 / P $69.98 ｜ ATM IV 69.8%，净 delta 敞口 -149k shares
Top ΔOI: C 1600 -2,493 ｜ C 2000 +650 ｜ P 1550 +393
仓位参考: Max Pain 1,690 ｜ Call Wall 1900（+6.9%，弱）（OI 1.3k） ｜ Put Wall 1700（-4.4%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 69.8%｜历史 Rank 19%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 149,169 股

📆 10-09 Forward Structure
存量OI: C 9.1k / P 7.8k，今日变化ΔOI: C +0.9k / P +0.6k，平值价格ATM: C $96.41 / P $94.72 ｜ ATM IV 68.4%，净 delta 敞口 18k shares
Top ΔOI: P 1550 +117 ｜ C 1750 +84 ｜ C 1900 +61
仓位参考: Max Pain 1,570 ｜ Put Wall 1690（-4.9%，弱）（OI 0.2k）
量化解读： 存量两侧均衡｜ATM IV 68.4%｜历史 Rank 19%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 正 17,975 股

📆 10-16 Forward Structure
存量OI: C 36.4k / P 44.7k，今日变化ΔOI: C +1.2k / P +1.0k，平值价格ATM: C $118.10 / P $117.69 ｜ ATM IV 69.3%，净 delta 敞口 17k shares
Top ΔOI: C 2500 +174 ｜ P 1580 +151
仓位参考: Max Pain 1,640 ｜ Call Wall 1800（+1.2%，弱）（OI 1.2k） ｜ Put Wall 1700（-4.4%，弱）（OI 1.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 69.3%｜历史 Rank 19%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 正 16,986 股

📆 10-23 Forward Structure
存量OI: C 3.7k / P 5.9k，今日变化ΔOI: C +0.3k / P +0.5k，平值价格ATM: C $136.00 / P $135.09 ｜ ATM IV 69.8%，净 delta 敞口 -372 shares
Top ΔOI: P 1540 +81 ｜ P 1500 +48 ｜ C 2370 +46
仓位参考: Max Pain 1,750 ｜ Call Wall 1840（+3.5%，弱）（OI 0.2k） ｜ Put Wall 1650（-7.2%，弱）（OI 0.1k）
量化解读： 存量 Put 重｜ATM IV 69.8%｜历史 Rank 19%（近端代理）｜IV/RV 0.95×（近似）｜净 delta 敞口 负 372 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/SNDK_evening.json