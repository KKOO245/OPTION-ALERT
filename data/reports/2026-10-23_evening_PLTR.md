# 期权晚报 2026-10-23（快照 16:40 ET）

📊 市场环境

SPY $759.97 ｜ QQQ $704.40
VIX 19.45 ↑2.2%（5D -2.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 21.0（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 205C ΔOI +2,613（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 195.02 → 收盘 196.75（+0.9%） ｜ 今日高 197.49 ｜ 低 190.57 ｜ 昨收 196.19 → 收盘 196.75（+0.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-30，窗口结束前不做对错判定）

Options: P/C成交量 0.67 | OI比 0.94 | ATM IV 62.3% | Skew 8.4pp | Term 1.06 | ExpMove ±5.4%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构正常（Term 1.06）｜保护溢价显著（Skew 8.4pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.94×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（7D）±5.4% ｜ 11-06（14D）±12.4% ｜ 11-13（21D）±13.7% ｜ 11-20（28D）±14.6%
   ⇒ IV–VIX Spread: +42.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 39,942,279 | GEX Change vs 上次快照 -5,965,519 | Flip: Primary Flip: 183.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 579 / LOW 72 / INVALID 299
结构观察区: Primary Flip 183.70（全链重定价，覆盖 82%）
Put Wall 180（弱结构｜现价高于该位 9.3%） | Call Wall 200（弱结构｜现价低于该位 1.6%）
最近结构参考: Call Wall 200（现价低于该位 1.6%）
量化视角： 正 Gamma（3994万，无历史分位）｜正 Gamma 减弱（597万）｜现价位于 Flip 上方 7.10%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构） / 192（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 184（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +8.2k / P +6.9k ｜ Activity HIGH ｜ 7D
11-06  C +0.8k / P +1.3k ｜ Activity MEDIUM △ ｜ 14D
11-13  C +0.5k / P +1.1k ｜ Activity HIGH ｜ 21D
11-20  C +2.7k / P +1.7k ｜ Activity HIGH ｜ 28D

📆 10-30 Forward Structure
存量OI: C 65.0k / P 86.9k，今日变化ΔOI: C +8.2k / P +6.9k，平值价格ATM: C $5.05 / P $5.61 ｜ ATM IV 48.1%，净 delta 敞口 149k shares
Top ΔOI: C 212 +2,760 ｜ C 205 +2,613
仓位参考: Max Pain 190 ｜ Call Wall 205（+4.2%，弱）（OI 6.6k） ｜ Put Wall 190（-3.4%，弱）（OI 6.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 48.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.06×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 149,154 股

11-06（MEDIUM △）Top ΔOI: 180P +601 ｜ 195C +170
11-06（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 215（+9.3%，弱）（OI 2.1k） ｜ Put Wall 190（-3.4%，弱）（OI 3.1k）

📆 11-13 Forward Structure
存量OI: C 12.1k / P 15.8k，今日变化ΔOI: C +0.5k / P +1.1k，平值价格ATM: C $12.81 / P $14.22 ｜ ATM IV 71.1%，净 delta 敞口 -269 shares
Top ΔOI: P 165 +162
仓位参考: Max Pain 195 ｜ Call Wall 210（+6.7%，弱）（OI 1.2k） ｜ Put Wall 180（-8.5%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 71.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.57×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 269 股

📆 11-20 Forward Structure
存量OI: C 160.1k / P 165.8k，今日变化ΔOI: C +2.7k / P +1.7k，平值价格ATM: C $13.68 / P $15.05 ｜ ATM IV 66.0%，净 delta 敞口 29k shares
Top ΔOI: C 190 +413 ｜ P 197 +290
仓位参考: Max Pain 175 ｜ Call Wall 200（+1.7%，弱）（OI 13.0k） ｜ Put Wall 185（-6.0%，弱）（OI 10.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 66.0%｜历史 Rank 94%（近端代理）｜IV/RV 1.46×（近似）｜净 delta 敞口 正 28,854 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/PLTR_evening.json