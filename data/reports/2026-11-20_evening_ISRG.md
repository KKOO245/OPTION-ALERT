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
🟡 **近现价集中开仓**: 12-11 415C ΔOI +2（距现价 +4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 398.5）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 406.44 → 收盘 399.05（-1.8%） ｜ 今日高 410.00 ｜ 低 397.78 ｜ 昨收 407.24 → 收盘 399.05（-2.0%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 0.99 | OI比 0.88 | ATM IV 125.8% | Skew -38.9pp | Term 0.31 | ExpMove ±5.0%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.31，近月 IV 高于远月）｜Put 保护异常便宜（Skew -38.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.99×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-27（7D）±5.0% ｜ 12-04（14D）±6.9% ｜ 12-11（21D）±2.7% ｜ 12-18（28D）±8.3%
   ⇒ IV–VIX Spread: +89.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 23,796 | GEX Change vs 上次快照 612,162 | Flip: Candidates 398.54 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 69%（带内） ｜ IV 有效性: VALID 203 / LOW 165 / INVALID 640
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈399（全链重定价，覆盖 69%，CONDITIONAL）
最近结构参考: Flip 399（现价高于该位 0.1%）
量化视角： 正 Gamma（2万，无历史分位）｜由负转正（+61万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 399（全链重定价，覆盖 69%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 620.0P — Vol 3 | 最新价 $165.40 | OI 0→9 (ΔOI +9张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增9张（量数据缺失），以日内换手为主
12-18 660.0P — Vol 4 | 最新价 $122.70 | OI 0→4 (ΔOI +4张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增4张（前日OI缺失），值得跟踪（方向未知）
量化视角： 2 个事件合计 ΔOI ≈ 13 张（Put 13 / Call 0），跨 1 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +0.1k / P +13 ｜ Activity HIGH ｜ 7D（新行权价 C 45 / P 22）
12-04  C +60 / P -3 ｜ Activity HIGH ｜ 14D（新行权价 C 38 / P 84）
12-11  C +20 / P +4 ｜ Activity MEDIUM △ ｜ 21D（新行权价 C 1 / P 3）
12-18  C +0.6k / P +50 ｜ Activity MEDIUM △ ｜ 28D

📆 11-27 Forward Structure
存量OI: C 0.9k / P 0.8k，今日变化ΔOI: C +0.1k / P +13（新行权价 C 45 / P 22），平值价格ATM: C $13.02 / P $7.10 ｜ ATM IV 44.2%，净 delta 敞口 3k shares
Top ΔOI: C 420 +71 ｜ P 365 +16
仓位参考: Max Pain 420 ｜ Call Wall 420（+5.2%，弱）（OI 77） ｜ Put Wall 395（-1.0%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 44.2%｜历史 Rank 100%（近端代理）｜IV/RV 1.00×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,998 股

📆 12-04 Forward Structure
存量OI: C 0.6k / P 0.3k，今日变化ΔOI: C +60 / P -3（新行权价 C 38 / P 84），平值价格ATM: C $18.20 / P $9.30 ｜ ATM IV 40.2%，净 delta 敞口 2k shares
Top ΔOI: C 420 +16
仓位参考: Max Pain 430 ｜ Call Wall 420（+5.2%，弱）（OI 21） ｜ Put Wall 405（+1.5%，弱）（OI 25）
量化解读： 存量 Call 重｜ATM IV 40.2%｜历史 Rank 100%（近端代理）｜IV/RV 0.91×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,696 股

12-11（MEDIUM △）Top ΔOI: 425C +13 ｜ 380P +6
12-11（MEDIUM △）仓位参考: Max Pain 440 ｜ Put Wall 435（+9.0%）（OI 36）

12-18（MEDIUM △）Top ΔOI: 435C +137 ｜ 250C +98
12-18（MEDIUM △）仓位参考: Max Pain 410 ｜ Call Wall 400（+0.2%，弱）（OI 1.5k） ｜ Put Wall 420（+5.2%，弱）（OI 0.6k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/ISRG_evening.json