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
🔵 **Flip 状态**: CONDITIONAL（Candidates: 39.9）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 38.14 → 收盘 38.30（+0.4%） ｜ 今日高 38.87 ｜ 低 37.11 ｜ 昨收 38.56 → 收盘 38.30（-0.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-30，窗口结束前不做对错判定）

Options: P/C成交量 0.66 | OI比 0.59 | ATM IV 99.0% | Skew -28.6pp | Term 0.65 | ExpMove ±6.3%（近端） | Rank 92%
量化视角： IV 历史高位（Rank 92%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜Put 保护异常便宜（Skew -28.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±6.3% ｜ 11-06（14D）±10.5% ｜ 11-13（21D）±12.0% ｜ 11-20（28D）±14.6%
   ⇒ IV–VIX Spread: +79.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,355,396 | GEX Change vs 上次快照 174,984 | Flip: Candidates 39.89 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 68%（带内） ｜ IV 有效性: VALID 280 / LOW 64 / INVALID 198
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈40（全链重定价，覆盖 68%，CONDITIONAL）
Put Wall 40（弱结构｜现价低于该位 4.3%）
最近结构参考: Flip 40（现价低于该位 4.0%）
量化视角： 负 Gamma（136万，无历史分位）｜负 Gamma 缓解（+17万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall，弱结构） / 40（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 40（全链重定价，覆盖 68%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0.5k / P +24 ｜ Activity HIGH ｜ 7D
11-06  C +0.9k / P +0.4k ｜ Activity MEDIUM △ ｜ 14D
11-13  C -25 / P +46 ｜ Activity MEDIUM △ ｜ 21D
11-20  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 28D

📆 10-30 Forward Structure
存量OI: C 8.8k / P 7.0k，今日变化ΔOI: C +0.5k / P +24，平值价格ATM: C $1.16 / P $1.27 ｜ ATM IV 57.6%，净 delta 敞口 32k shares
Top ΔOI: P 37 +126 ｜ P 50 -75 ｜ P 38 +66
仓位参考: Max Pain 44 ｜ Call Wall 42（+9.7%，弱）（OI 0.5k） ｜ Put Wall 37（-3.4%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 57.6%｜历史 Rank 92%（近端代理）｜IV/RV 1.20×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 31,987 股

11-06（MEDIUM △）Top ΔOI: 42P +129
11-06（MEDIUM △）仓位参考: Max Pain 43 ｜ Call Wall 40（+4.4%，弱）（OI 0.3k） ｜ Put Wall 38（-0.8%）（OI 0.9k）

11-13（MEDIUM △）Top ΔOI: 36P +20
11-13（MEDIUM △）仓位参考: Max Pain 42 ｜ Call Wall 35（-8.6%，弱）（OI 0.5k） ｜ Put Wall 39（+1.8%）（OI 0.7k）

11-20（MEDIUM △）Top ΔOI: 38C +253
11-20（MEDIUM △）仓位参考: Max Pain 45 ｜ Call Wall 40（+4.4%，弱）（OI 1.0k） ｜ Put Wall 40（+4.4%，弱）（OI 1.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/MP_evening.json