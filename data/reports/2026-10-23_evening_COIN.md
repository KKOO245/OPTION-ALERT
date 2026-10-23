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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-06 172C ΔOI +90（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 168.00 → 收盘 164.45（-2.1%） ｜ 今日高 169.84 ｜ 低 163.33 ｜ 昨收 169.09 → 收盘 164.45（-2.7%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-10-28，窗口结束前不做对错判定）

Options: P/C成交量 0.84 | OI比 0.64 | ATM IV 68.1% | Skew 21.1pp | Term 1.06 | ExpMove ±9.5%（近端） | Rank 29%
量化视角： IV 中性（Rank 29%）｜期限结构正常（Term 1.06）｜保护溢价显著（Skew 21.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±9.5% ｜ 11-06（14D）±12.2% ｜ 11-13（21D）±14.0% ｜ 11-20（28D）±15.6%
   ⇒ IV–VIX Spread: +48.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 4,874,603 | GEX Change vs 上次快照 -8,692,132 | Flip: Primary Flip: 151.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 426 / LOW 116 / INVALID 340
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 151.35（全链重定价，覆盖 82%）
Call Wall 170（弱结构｜现价低于该位 3.3%）
最近结构参考: Call Wall 170（现价低于该位 3.3%）
量化视角： 正 Gamma（487万，无历史分位）｜正 Gamma 减弱（869万）｜现价位于 Flip 上方 8.66%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 175（MaxPain，仅结算参考） / 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +14.2k / P +3.0k ｜ Activity HIGH ｜ 7D
11-06  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 14D
11-13  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 21D
11-20  C +0.5k / P +0.9k ｜ Activity HIGH ｜ 28D

📆 10-30 Forward Structure
存量OI: C 34.8k / P 23.0k，今日变化ΔOI: C +14.2k / P +3.0k，平值价格ATM: C $7.64 / P $7.95 ｜ ATM IV 86.2%，净 delta 敞口 288k shares
Top ΔOI: C 175 +3,824 ｜ C 182 +3,552 ｜ C 177 +1,639
仓位参考: Max Pain 175 ｜ Call Wall 175（+6.4%，弱）（OI 4.3k） ｜ Put Wall 150（-8.8%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 86.2%｜历史 Rank 29%（近端代理）｜IV/RV 1.63×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 287,735 股

11-06（MEDIUM △）Top ΔOI: 172C +90 ｜ 180C +55
11-06（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 175（+6.4%，弱）（OI 0.4k）

📆 11-13 Forward Structure
存量OI: C 6.1k / P 7.9k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $11.35 / P $11.66 ｜ ATM IV 72.3%，净 delta 敞口 -6k shares
Top ΔOI: C 180 +139 ｜ P 175 +136 ｜ C 182 +121
仓位参考: Max Pain 178 ｜ Call Wall 177.5（+7.9%）（OI 1.1k） ｜ Put Wall 160（-2.7%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜ATM IV 72.3%｜历史 Rank 29%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 6,394 股

📆 11-20 Forward Structure
存量OI: C 68.3k / P 46.6k，今日变化ΔOI: C +0.5k / P +0.9k，平值价格ATM: C $12.70 / P $12.95 ｜ ATM IV 72.3%，净 delta 敞口 -23k shares
Top ΔOI: P 167 +551 ｜ C 220 +403 ｜ P 140 +196
仓位参考: Max Pain 170 ｜ Call Wall 170（+3.4%）（OI 13.4k） ｜ Put Wall 150（-8.8%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 72.3%｜历史 Rank 29%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 负 22,758 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/COIN_evening.json