# 期权晚报 2026-11-20（快照 16:40 ET）

📊 市场环境

SPY $689.81 ｜ QQQ $608.45
VIX 35.89 ↑26.2%（5D +86.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 9.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔵 **期限 OI 集中**: 11-27 290C ΔOI +5,391 占该期限总 OI 12.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 162.02 → 收盘 142.39（-12.1%） ｜ 今日高 163.38 ｜ 低 140.69 ｜ 昨收 168.11 → 收盘 142.39（-15.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 1.05 | OI比 0.66 | ATM IV 250.8% | Skew 32.1pp | Term 0.49 | ExpMove ±15.5%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.49，近月 IV 高于远月）｜保护溢价显著（Skew 32.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.66）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.05×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±15.5% ｜ 12-04（14D）±20.1% ｜ 12-11（21D）±23.3% ｜ 12-18（28D）±26.5%
   ⇒ IV–VIX Spread: +214.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,359,580 | GEX Change vs 上次快照 3,992,784 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 424 / LOW 86 / INVALID 412
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: NO_CROSS
Put Wall 150（弱结构｜现价低于该位 5.1%）
最近结构参考: Put Wall 150（现价低于该位 5.1%）
量化视角： 负 Gamma（936万，无历史分位）｜负 Gamma 缓解（+399万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 150（Put Wall，弱结构） / 180（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 440.0P — Vol 10 | 最新价 $243.95 | OI 0→11 (ΔOI +11张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增11张（量数据缺失），以日内换手为主
12-18 430.0P — Vol 5 | 最新价 $246.70 | OI 0→7 (ΔOI +7张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增7张（量数据缺失），以日内换手为主
12-18 470.0P — Vol 2 | 最新价 $265.09 | OI 0→2 (ΔOI +2张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增2张（前日OI缺失），值得跟踪（方向未知）
12-18 490.0P — Vol 0 | 最新价 $234.73 | OI 0→1 (ΔOI +1张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增1张（量数据缺失），以日内换手为主
量化视角： 4 个事件合计 ΔOI ≈ 21 张（Put 21 / Call 0），跨 1 个期限｜有实质成本保护 4 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +9.4k / P +2.6k ｜ Activity HIGH ｜ 7D（新行权价 C 0.2k / P 10）
12-04  C +0.7k / P +48 ｜ Activity HIGH ｜ 14D（新行权价 C 0.3k / P 0.3k）
12-11  C +0.2k / P +79 ｜ Activity MEDIUM △ ｜ 21D（新行权价 C 4）
12-18  C +1.4k / P +1.5k ｜ Activity MEDIUM △ ｜ 28D

📆 11-27 Forward Structure
存量OI: C 26.8k / P 16.0k，今日变化ΔOI: C +9.4k / P +2.6k（新行权价 C 0.2k / P 10），平值价格ATM: C $11.05 / P $11.05 ｜ ATM IV 137.8%，净 delta 敞口 -111k shares
Top ΔOI: P 110 +603 ｜ P 152 +523
仓位参考: Max Pain 190 ｜ Put Wall 140（-1.7%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 137.8%｜历史 Rank 100%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 110,900 股

📆 12-04 Forward Structure
存量OI: C 10.0k / P 8.3k，今日变化ΔOI: C +0.7k / P +48（新行权价 C 0.3k / P 0.3k），平值价格ATM: C $14.80 / P $13.85 ｜ ATM IV 132.2%，净 delta 敞口 9k shares
仓位参考: Max Pain 200 ｜ Put Wall 140（-1.7%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 132.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,436 股

12-11（MEDIUM △）仓位参考: Max Pain 205 ｜ Put Wall 150（+5.3%，弱）（OI 0.3k）

12-18（MEDIUM △）Top ΔOI: 170C +535 ｜ 120P +328
12-18（MEDIUM △）仓位参考: Max Pain 210 ｜ Put Wall 150（+5.3%，弱）（OI 6.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location ? | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/BE_evening.json