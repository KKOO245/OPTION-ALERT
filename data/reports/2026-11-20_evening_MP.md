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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-27 34P ΔOI +792（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 35.94 → 收盘 33.95（-5.5%） ｜ 今日高 37.59 ｜ 低 33.57 ｜ 昨收 36.66 → 收盘 33.95（-7.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 0.75 | OI比 0.35 | ATM IV 135.2% | Skew 15.8pp | Term 0.53 | ExpMove ±8.9%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价显著（Skew 15.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.75×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±8.9% ｜ 12-04（14D）±11.2% ｜ 12-11（21D）±3.9% ｜ 12-18（28D）±16.6%
   ⇒ IV–VIX Spread: +99.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,988,858 | GEX Change vs 上次快照 -889,228 | Flip: Primary Flip: 32.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 216 / LOW 84 / INVALID 172
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 32.45（全链重定价，覆盖 95%）
Put Wall 35（现价低于该位 3.0%）
最近结构参考: Put Wall 35（现价低于该位 3.0%）
量化视角： 正 Gamma（199万，无历史分位）｜正 Gamma 减弱（89万）｜现价位于 Flip 上方 4.61%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 35（Put Wall） / 37（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 32（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 105.0P — Vol 1 | 最新价 $45.50 | OI 0→1 (ΔOI +1张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增1张（前日OI缺失），值得跟踪（方向未知）
量化视角： 1 个事件合计 ΔOI ≈ 1 张（Put 1 / Call 0），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +0.3k / P +0.9k ｜ Activity MEDIUM △ ｜ 7D（新行权价 C 17 / P 12）
12-04  C +75 / P +40 ｜ Activity MEDIUM △ ｜ 14D（新行权价 C 0.1k / P 51）
12-11  C -0.2k / P +19 ｜ Activity MEDIUM △ ｜ 21D（新行权价 P 4）
12-18  C -0.2k / P -1.7k ｜ Activity MEDIUM △ ｜ 28D

📆 11-27 Forward Structure
存量OI: C 12.0k / P 5.8k，今日变化ΔOI: C +0.3k / P +0.9k（新行权价 C 17 / P 12），平值价格ATM: C $2.52 / P $0.50 ｜ ATM IV 87.6%，净 delta 敞口 -25k shares
Top ΔOI: P 34 +792
仓位参考: Max Pain 38 ｜ Put Wall 33（-2.8%）（OI 2.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 87.6%｜历史 Rank 98%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 25,006 股

12-04（MEDIUM △）Top ΔOI: 37C +19 ｜ 35P +15
12-04（MEDIUM △）仓位参考: Max Pain 38 ｜ Call Wall 35（+3.1%）（OI 0.5k） ｜ Put Wall 34（+0.1%，弱）（OI 0.2k）

12-11（MEDIUM △）Top ΔOI: 38C -268
12-11（MEDIUM △）仓位参考: Max Pain 38 ｜ Call Wall 36（+6.0%，弱）（OI 0.2k）

12-18（MEDIUM △）Top ΔOI: 60P -1,674
12-18（MEDIUM △）仓位参考: Max Pain 40 ｜ Put Wall 35（+3.1%，弱）（OI 6.0k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/MP_evening.json