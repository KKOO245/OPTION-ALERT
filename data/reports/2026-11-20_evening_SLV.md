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
🟡 **近现价集中开仓**: 11-25 38P ΔOI +698（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 38.8）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 37.97 → 收盘 36.97（-2.6%） ｜ 今日高 38.47 ｜ 低 36.81 ｜ 昨收 39.64 → 收盘 36.97（-6.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 0.77 | OI比 0.15 | ATM IV 99.2% | Skew 8.1pp | Term 0.57 | ExpMove ±4.5%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.57，近月 IV 高于远月）｜保护溢价显著（Skew 8.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.15）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.15×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-23（3D）±4.5% ｜ 11-25（5D）±6.1% ｜ 11-27（7D）±7.2% ｜ 11-30（10D）±7.5%
   ⇒ IV–VIX Spread: +63.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -17,003,755 | GEX Change vs 上次快照 -20,406,405 | Flip: Candidates 38.77 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 79%（带内） ｜ IV 有效性: VALID 569 / LOW 195 / INVALID 572
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈39（全链重定价，覆盖 79%，CONDITIONAL）
Put Wall 40（现价低于该位 7.6%）
最近结构参考: Flip 39（现价低于该位 4.6%）
量化视角： 负 Gamma（1700万，无历史分位）｜由正转负（2041万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 40（Put Wall） / 42（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 39（全链重定价，覆盖 79%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 73.0P — Vol 20 | 最新价 $17.05 | OI 0→19 (ΔOI +19张) | ΔOI/Volume 95.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增19张（前日OI缺失），值得跟踪（方向未知）
量化视角： 1 个事件合计 ΔOI ≈ 19 张（Put 19 / Call 0），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-23  C +6.8k / P +0.2k ｜ Activity HIGH ｜ 3D（新行权价 C 1.5k / P 1.0k）
11-25  C +5.0k / P +1.2k ｜ Activity HIGH ｜ 5D（新行权价 C 0.5k / P 1.9k）
11-27  C +5.8k / P -2.4k ｜ Activity HIGH ｜ 7D（新行权价 C 0.9k / P 6.0k）
11-30  C N/A / P N/A ｜ Activity LOW ｜ 10D（新上架）

📆 11-23 Forward Structure
存量OI: C 27.8k / P 7.6k，今日变化ΔOI: C +6.8k / P +0.2k（新行权价 C 1.5k / P 1.0k），平值价格ATM: C $0.81 / P $0.87 ｜ ATM IV 60.8%，净 delta 敞口 63k shares
仓位参考: Max Pain 40 ｜ Put Wall 40（+8.2%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 60.8%｜历史 Rank 98%（近端代理）｜IV/RV 1.42×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 63,318 股

📆 11-25 Forward Structure
存量OI: C 20.9k / P 10.2k，今日变化ΔOI: C +5.0k / P +1.2k（新行权价 C 0.5k / P 1.9k），平值价格ATM: C $1.16 / P $1.10 ｜ ATM IV 68.1%，净 delta 敞口 -47k shares
Top ΔOI: P 38 +698
仓位参考: Max Pain 42 ｜ Put Wall 39（+5.5%）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 68.1%｜历史 Rank 98%（近端代理）｜IV/RV 1.59×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 46,503 股

📆 11-27 Forward Structure
存量OI: C 94.3k / P 34.1k，今日变化ΔOI: C +5.8k / P -2.4k（新行权价 C 0.9k / P 6.0k），平值价格ATM: C $1.29 / P $1.36 ｜ ATM IV 63.9%，净 delta 敞口 290k shares
Top ΔOI: C 40 +1,239
仓位参考: Max Pain 43 ｜ Call Wall 40（+8.2%，弱）（OI 1.9k） ｜ Put Wall 40（+8.2%）（OI 9.4k）
量化解读： 存量 Call 重｜ATM IV 63.9%｜历史 Rank 98%（近端代理）｜IV/RV 1.49×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 289,665 股

11-30（Activity LOW）仓位参考: Max Pain 41 ｜ Put Wall 39（+5.5%）（OI 4.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-20/SLV_evening.json