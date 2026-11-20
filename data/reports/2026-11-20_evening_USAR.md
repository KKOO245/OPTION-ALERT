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
🔵 **Flip 状态**: CONDITIONAL（Candidates: 6.0）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 6.69 → 收盘 6.27（-6.3%） ｜ 今日高 7.09 ｜ 低 6.18 ｜ 昨收 6.87 → 收盘 6.27（-8.7%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 0.83 | OI比 0.41 | ATM IV N/A | Skew 17.2pp | Term N/A | ExpMove ±13.7%（近端） | Rank — (历史不足)
量化视角： 保护溢价显著（Skew 17.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.41×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（7D）±13.7% ｜ 12-04（14D）±20.9% ｜ 12-11（21D）±24.1% ｜ 12-18（28D）±25.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 405,987 | GEX Change vs 上次快照 -1,793,077 | Flip: Candidates 6.00 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 76%（带内） ｜ IV 有效性: VALID 160 / LOW 88 / INVALID 184
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈6（全链重定价，覆盖 76%，CONDITIONAL）
最近结构参考: Flip 6（现价高于该位 4.5%）
量化视角： 正 Gamma（41万，无历史分位）｜正 Gamma 减弱（179万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 9（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 6（全链重定价，覆盖 76%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 31.0P — Vol 1 | 最新价 $11.05 | OI 0→4 (ΔOI +4张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增4张（量数据缺失），以日内换手为主
12-18 34.0P — Vol 8 | 最新价 $13.00 | OI 0→4 (ΔOI +4张) | ΔOI/Volume 50.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增4张（前日OI缺失），值得跟踪（方向未知）
量化视角： 2 个事件合计 ΔOI ≈ 8 张（Put 8 / Call 0），跨 1 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-27  C +0.8k / P +0.1k ｜ Activity MEDIUM △ ｜ 7D（新行权价 C 2 / P 2）
12-04  C +0.3k / P -40 ｜ Activity HIGH ｜ 14D（新行权价 P 6）
12-11  C +60 / P +18 ｜ Activity MEDIUM △ ｜ 21D（新行权价 P 1）
12-18  C +0.3k / P -0.6k ｜ Activity MEDIUM △ ｜ 28D（新行权价 C 1）

📆 11-27 Forward Structure
存量OI: C 18.8k / P 4.1k，今日变化ΔOI: C +0.8k / P +0.1k（新行权价 C 2 / P 2），平值价格ATM: C $0.32 / P $0.54 ｜ ATM IV 124.4%，净 delta 敞口 14k shares
仓位参考: Max Pain 8 ｜ Put Wall 6（-4.3%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 124.4%｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,308 股

📆 12-04 Forward Structure
存量OI: C 3.9k / P 2.1k，今日变化ΔOI: C +0.3k / P -40（新行权价 P 6），平值价格ATM: C $0.55 / P $0.76 ｜ ATM IV 114.0%，净 delta 敞口 15k shares
仓位参考: Max Pain 8 ｜ Put Wall 6（-4.3%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 114.0%｜IV/RV 1.16×（近似）｜净 delta 敞口 正 15,055 股

12-11（MEDIUM △）仓位参考: Max Pain 8 ｜ Put Wall 6（-4.3%，弱）（OI 74）

12-18（MEDIUM △）Top ΔOI: 7P +411 ｜ 19P -402
12-18（MEDIUM △）仓位参考: Max Pain 11

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/USAR_evening.json