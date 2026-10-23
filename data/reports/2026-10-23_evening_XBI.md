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
🔵 **Flip 状态**: CONDITIONAL（Candidates: 160.8）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 150.46 → 收盘 149.54（-0.6%） ｜ 今日高 150.70 ｜ 低 147.63 ｜ 昨收 151.64 → 收盘 149.54（-1.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-30，窗口结束前不做对错判定）

Options: P/C成交量 0.42 | OI比 1.38 | ATM IV 63.1% | Skew -2.7pp | Term 0.53 | ExpMove ±4.0%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.38×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±4.0% ｜ 11-06（14D）±11.2% ｜ 11-13（21D）±0.0% ｜ 11-20（28D）±7.5%
   ⇒ IV–VIX Spread: +43.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -28,102,604 | GEX Change vs 上次快照 -77,427 | Flip: Candidates 160.82 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 79%（带内） ｜ IV 有效性: VALID 326 / LOW 95 / INVALID 361
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈161（全链重定价，覆盖 79%，CONDITIONAL）
Put Wall 140（弱结构｜现价高于该位 6.8%）
最近结构参考: Put Wall 140（现价高于该位 6.8%）
量化视角： 负 Gamma（2810万，无历史分位）｜负 Gamma 加深（8万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构） / 148（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 79%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0.2k / P +2 ｜ Activity MEDIUM △ ｜ 7D
11-06  C +0.1k / P +94 ｜ Activity HIGH ｜ 14D
11-13  C +0.2k / P +0 ｜ Activity HIGH ｜ 21D
11-20  C +2.3k / P +81 ｜ Activity MEDIUM △ ｜ 28D

📆 10-30 Forward Structure
存量OI: C 7.4k / P 54.2k，今日变化ΔOI: C +0.2k / P +2，平值价格ATM: C $3.11 / P $2.88 ｜ ATM IV 36.0%，净 delta 敞口 4k shares
Top ΔOI: P 150 -119 ｜ P 152 +110 ｜ C 160 +98
仓位参考: Max Pain 152 ｜ Call Wall 155（+3.7%）（OI 1.8k） ｜ Put Wall 140（-6.4%，弱）（OI 16.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 36.0%｜历史 Rank 99%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,786 股

📆 11-06 Forward Structure
存量OI: C 1.4k / P 2.2k，今日变化ΔOI: C +0.1k / P +94，平值价格ATM: C $11.15 / P $5.56 ｜ ATM IV 34.3%，净 delta 敞口 676 shares
Top ΔOI: P 136 +81 ｜ C 160 +39 ｜ C 162 +31
仓位参考: Max Pain 152 ｜ Call Wall 154（+3.0%，弱）（OI 0.1k） ｜ Put Wall 151（+1.0%）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 34.3%｜历史 Rank 99%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 676 股

📆 11-13 Forward Structure
存量OI: C 0.8k / P 1.5k，今日变化ΔOI: C +0.2k / P +0，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 34.8%，净 delta 敞口 6k shares
Top ΔOI: C 158 +74 ｜ C 157 +53 ｜ C 159 +37
仓位参考: Max Pain 153 ｜ Call Wall 150（+0.3%）（OI 0.2k） ｜ Put Wall 153（+2.3%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 34.8%｜历史 Rank 99%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 6,208 股

11-20（MEDIUM △）Top ΔOI: 165C +1,964
11-20（MEDIUM △）仓位参考: Max Pain 154 ｜ Put Wall 145（-3.0%，弱）（OI 7.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/XBI_evening.json