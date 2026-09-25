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
🟡 **近现价集中开仓**: 10-09 200C ΔOI +947（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 166.1）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 199.30 → 收盘 195.11（-2.1%） ｜ 今日高 199.75 ｜ 低 192.58 ｜ 昨收 199.21 → 收盘 195.11（-2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.28 | OI比 0.52 | ATM IV 41.1% | Skew -4.1pp | Term 1.43 | ExpMove ±6.6%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常偏陡（Term 1.43）｜Put 保护异常便宜（Skew -4.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（7D）±6.6% ｜ 10-09（14D）±9.9% ｜ 10-16（21D）±11.7% ｜ 10-23（28D）±13.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 22,280,392 | GEX Change vs 上次快照 -8,898,959 | Flip: Candidates 166.15 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 467 / LOW 126 / INVALID 319
结构观察区: ≈166（全链重定价，覆盖 78%，CONDITIONAL）
最近结构参考: Flip 166（现价高于该位 17.4%）
量化视角： 正 Gamma（2228万，无历史分位）｜正 Gamma 减弱（890万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 78%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +5.6k / P +2.5k ｜ Activity HIGH ｜ 7D
10-09  C +1.2k / P +2.2k ｜ Activity HIGH ｜ 14D
10-16  C +1.1k / P +0.5k ｜ Activity MEDIUM △ ｜ 21D
10-23  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 28D

📆 10-02 Forward Structure
存量OI: C 27.7k / P 35.6k，今日变化ΔOI: C +5.6k / P +2.5k，平值价格ATM: C $6.63 / P $6.29 ｜ ATM IV 59.8%，净 delta 敞口 42k shares
Top ΔOI: C 217 +1,302 ｜ C 207 +1,256 ｜ C 210 +775
仓位参考: Max Pain 190 ｜ Call Wall 210（+7.6%，弱）（OI 1.6k） ｜ Put Wall 190（-2.6%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 59.8%｜历史 Rank 50%（近端代理）｜IV/RV 0.70×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 42,313 股

📆 10-09 Forward Structure
存量OI: C 6.5k / P 14.2k，今日变化ΔOI: C +1.2k / P +2.2k，平值价格ATM: C $9.75 / P $9.65 ｜ ATM IV 63.8%，净 delta 敞口 42k shares
Top ΔOI: C 200 +947 ｜ P 197 +101
仓位参考: Max Pain 188 ｜ Call Wall 200（+2.5%）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 63.8%｜历史 Rank 50%（近端代理）｜IV/RV 0.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,531 股

10-16（MEDIUM △）Top ΔOI: 190P +673 ｜ 195P -230
10-16（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 200（+2.5%，弱）（OI 6.1k） ｜ Put Wall 200（+2.5%，弱）（OI 3.9k）

📆 10-23 Forward Structure
存量OI: C 4.2k / P 3.7k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $13.40 / P $12.63 ｜ ATM IV 58.7%，净 delta 敞口 1k shares
仓位参考: Max Pain 185 ｜ Call Wall 210（+7.6%，弱）（OI 0.2k） ｜ Put Wall 190（-2.6%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.7%｜历史 Rank 50%（近端代理）｜IV/RV 0.69×（近似）｜净 delta 敞口 正 1,453 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-25/COIN_evening.json