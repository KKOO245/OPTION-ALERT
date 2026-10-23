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
🟡 **近现价集中开仓**: 10-26 215C ΔOI +4,281（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 210.94 → 收盘 210.96（+0.0%） ｜ 今日高 213.85 ｜ 低 210.18 ｜ 昨收 212.21 → 收盘 210.96（-0.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-30，窗口结束前不做对错判定）

Options: P/C成交量 0.51 | OI比 0.78 | ATM IV 59.8% | Skew -0.5pp | Term 0.73 | ExpMove ±2.2%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.78）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.51×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-26（3D）±2.2% ｜ 10-28（5D）±3.5% ｜ 10-30（7D）±4.3% ｜ 11-02（10D）±4.7%
   ⇒ IV–VIX Spread: +40.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 20,284,070 | GEX Change vs 上次快照 -94,456,059 | Flip: Primary Flip: 209.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 699 / LOW 206 / INVALID 557
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 209.93（全链重定价，覆盖 88%）
Put Wall 200（弱结构｜现价高于该位 5.5%） | Call Wall 230（弱结构｜现价低于该位 8.3%）
最近结构参考: Flip 210（现价高于该位 0.5%）
量化视角： 正 Gamma（2028万，无历史分位）｜正 Gamma 减弱（9446万）｜现价位于 Flip 上方 0.49%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 215（MaxPain，仅结算参考） / 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 210（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-26  C +19.1k / P +8.3k ｜ Activity HIGH ｜ 3D
10-28  C +15.4k / P +5.0k ｜ Activity HIGH ｜ 5D
10-30  C +63.1k / P +17.8k ｜ Activity HIGH ｜ 7D
11-02  C +2.8k / P +1.3k ｜ Activity HIGH ｜ 10D

📆 10-26 Forward Structure
存量OI: C 61.5k / P 45.6k，今日变化ΔOI: C +19.1k / P +8.3k，平值价格ATM: C $2.79 / P $1.77 ｜ ATM IV 29.2%，净 delta 敞口 276k shares
Top ΔOI: C 215 +4,281 ｜ C 217 +4,057 ｜ C 220 +2,744
仓位参考: Max Pain 215 ｜ Call Wall 225（+6.7%，弱）（OI 7.0k） ｜ Put Wall 200（-5.2%）（OI 10.1k）
量化解读： 存量 Call 重｜ATM IV 29.2%｜历史 Rank 85%（近端代理）｜IV/RV 1.02×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 276,320 股

📆 10-28 Forward Structure
存量OI: C 34.3k / P 22.0k，今日变化ΔOI: C +15.4k / P +5.0k，平值价格ATM: C $4.20 / P $3.10 ｜ ATM IV 37.3%，净 delta 敞口 223k shares
Top ΔOI: C 217 +3,377 ｜ C 215 +2,650 ｜ C 220 +2,370
仓位参考: Max Pain 215 ｜ Call Wall 230（+9.0%，弱）（OI 5.9k） ｜ Put Wall 215（+1.9%）（OI 3.5k）
量化解读： 存量 Call 重｜ATM IV 37.3%｜历史 Rank 85%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 222,768 股

📆 10-30 Forward Structure
存量OI: C 272.4k / P 211.3k，今日变化ΔOI: C +63.1k / P +17.8k，平值价格ATM: C $5.07 / P $3.95 ｜ ATM IV 38.3%，净 delta 敞口 1.3M shares
Top ΔOI: C 225 +21,035 ｜ C 217 +20,898 ｜ C 220 +4,957
仓位参考: Max Pain 218 ｜ Call Wall 225（+6.7%，弱）（OI 32.3k） ｜ Put Wall 210（-0.5%，弱）（OI 19.1k）
量化解读： 存量 Call 重｜ATM IV 38.3%｜历史 Rank 85%（近端代理）｜IV/RV 1.34×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,299,992 股

📆 11-02 Forward Structure
存量OI: C 7.3k / P 2.7k，今日变化ΔOI: C +2.8k / P +1.3k，平值价格ATM: C $5.70 / P $4.30 ｜ ATM IV 35.7%，净 delta 敞口 49k shares
Top ΔOI: C 220 +862 ｜ C 215 +352 ｜ C 225 +325
仓位参考: Max Pain 212 ｜ Call Wall 230（+9.0%，弱）（OI 2.0k） ｜ Put Wall 200（-5.2%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 35.7%｜历史 Rank 85%（近端代理）｜IV/RV 1.25×（近似）｜净 delta 敞口 正 48,899 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/NVDA_evening.json