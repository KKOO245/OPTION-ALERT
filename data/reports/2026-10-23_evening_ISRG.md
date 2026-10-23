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
🔵 **Flip 状态**: CONDITIONAL（Candidates: 408.3）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 443.65 → 收盘 452.29（+1.9%） ｜ 今日高 458.45 ｜ 低 442.56 ｜ 昨收 443.85 → 收盘 452.29（+1.9%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-30，窗口结束前不做对错判定）

Options: P/C成交量 0.19 | OI比 0.97 | ATM IV 132.4% | Skew -65.0pp | Term 0.24 | ExpMove ±3.6%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.24，近月 IV 高于远月）｜Put 保护异常便宜（Skew -65.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.19×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（7D）±3.6% ｜ 11-06（14D）±5.2% ｜ 11-13（21D）±10.1% ｜ 11-20（28D）±4.9%
   ⇒ IV–VIX Spread: +112.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,283,182 | GEX Change vs 上次快照 -1,369,643 | Flip: Candidates 408.32 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 71%（带内） ｜ IV 有效性: VALID 255 / LOW 208 / INVALID 537
结构观察区: ≈408（全链重定价，覆盖 71%，CONDITIONAL）
Call Wall 475（弱结构｜现价低于该位 4.8%）
最近结构参考: Call Wall 475（现价低于该位 4.8%）
量化视角： 正 Gamma（428万，无历史分位）｜正 Gamma 减弱（137万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 425（MaxPain，仅结算参考）；上方 475（Call Wall，弱结构）。
• Gamma 区域：切换参考 408（全链重定价，覆盖 71%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C -35 / P +0.1k ｜ Activity HIGH ｜ 7D
11-06  C +44 / P +39 ｜ Activity MEDIUM △ ｜ 14D
11-13  C +43 / P +0.1k ｜ Activity MEDIUM △ ｜ 21D
11-20  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 28D

📆 10-30 Forward Structure
存量OI: C 1.9k / P 1.5k，今日变化ΔOI: C -35 / P +0.1k，平值价格ATM: C $8.40 / P $7.90 ｜ ATM IV 37.8%，净 delta 敞口 -4k shares
Top ΔOI: C 440 -22 ｜ C 485 -19
仓位参考: Max Pain 412 ｜ Call Wall 450（-0.5%，弱）（OI 0.2k） ｜ Put Wall 410（-9.4%，弱）（OI 99）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 37.8%｜历史 Rank 100%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,467 股

11-06（MEDIUM △）Top ΔOI: 430C +16 ｜ 420P +15
11-06（MEDIUM △）仓位参考: Max Pain 425 ｜ Call Wall 430（-4.9%，弱）（OI 0.2k） ｜ Put Wall 450（-0.5%，弱）（OI 64）

11-13（MEDIUM △）Top ΔOI: 415P +34 ｜ 410P +28
11-13（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 435（-3.8%，弱）（OI 0.1k） ｜ Put Wall 420（-7.1%，弱）（OI 80）

11-20（MEDIUM △）Top ΔOI: 440P +75 ｜ 445P +40
11-20（MEDIUM △）仓位参考: Max Pain 395 ｜ Call Wall 420（-7.1%，弱）（OI 0.8k） ｜ Put Wall 410（-9.4%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/ISRG_evening.json