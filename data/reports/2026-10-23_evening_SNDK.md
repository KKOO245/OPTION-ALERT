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
🟡 **近现价集中开仓**: 10-30 1300C ΔOI +539（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 1340.2）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,269.00 → 收盘 1,238.03（-2.4%） ｜ 今日高 1299.99 ｜ 低 1228.89 ｜ 昨收 1,260.93 → 收盘 1,238.03（-1.8%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-28，窗口结束前不做对错判定）

Options: P/C成交量 0.87 | OI比 0.70 | ATM IV 110.0% | Skew -2.2pp | Term 0.69 | ExpMove ±10.8%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.70）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.87×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（7D）±10.8% ｜ 11-06（14D）±13.4% ｜ 11-13（21D）±16.2% ｜ 11-20（28D）±17.0%
   ⇒ IV–VIX Spread: +90.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,531,617 | GEX Change vs 上次快照 -2,604,807 | Flip: Candidates 1340.20 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 75%（带内） ｜ IV 有效性: VALID 1757 / LOW 456 / INVALID 1345
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈1340（全链重定价，覆盖 75%，CONDITIONAL）
Put Wall 1,200（弱结构｜现价高于该位 3.2%）
最近结构参考: Put Wall 1200（现价高于该位 3.2%）
量化视角： 负 Gamma（453万，无历史分位）｜负 Gamma 加深（260万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,200（Put Wall，弱结构）；上方 1,325（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1340（全链重定价，覆盖 75%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +3.1k / P +2.6k ｜ Activity HIGH ｜ 7D
11-06  C +1.1k / P +0.7k ｜ Activity HIGH ｜ 14D
11-13  C +0.2k / P +0.4k ｜ Activity HIGH ｜ 21D
11-20  C +4.1k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 10-30 Forward Structure
存量OI: C 31.3k / P 21.2k，今日变化ΔOI: C +3.1k / P +2.6k，平值价格ATM: C $66.40 / P $67.50 ｜ ATM IV 97.8%，净 delta 敞口 62k shares
Top ΔOI: P 750 +1,010 ｜ C 1300 +539 ｜ P 900 +258
仓位参考: Max Pain 1,425 ｜ Call Wall 1300（+5.0%，弱）（OI 1.0k） ｜ Put Wall 1350（+9.0%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 97.8%｜历史 Rank 70%（近端代理）｜IV/RV 1.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 62,410 股

📆 11-06 Forward Structure
存量OI: C 11.1k / P 8.2k，今日变化ΔOI: C +1.1k / P +0.7k，平值价格ATM: C $82.93 / P $83.03 ｜ ATM IV 85.5%，净 delta 敞口 6k shares
Top ΔOI: P 1240 +197 ｜ C 1700 +142
仓位参考: Max Pain 1,465 ｜ Call Wall 1350（+9.0%，弱）（OI 0.1k） ｜ Put Wall 1200（-3.1%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 85.5%｜历史 Rank 70%（近端代理）｜IV/RV 1.51×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,692 股

📆 11-13 Forward Structure
存量OI: C 4.8k / P 4.6k，今日变化ΔOI: C +0.2k / P +0.4k，平值价格ATM: C $107.00 / P $94.22 ｜ ATM IV 79.0%，净 delta 敞口 -4k shares
Top ΔOI: P 900 +117 ｜ P 1500 +94 ｜ P 990 -61
仓位参考: Max Pain 1,500 ｜ Call Wall 1320（+6.6%，弱）（OI 86） ｜ Put Wall 1300（+5.0%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 79.0%｜历史 Rank 70%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 3,923 股

📆 11-20 Forward Structure
存量OI: C 43.5k / P 48.5k，今日变化ΔOI: C +4.1k / P +0.2k，平值价格ATM: C $108.70 / P $102.10 ｜ ATM IV 76.2%，净 delta 敞口 154k shares
Top ΔOI: C 1500 +2,140 ｜ P 1000 +465 ｜ C 1000 +450
仓位参考: Max Pain 1,500 ｜ Put Wall 1200（-3.1%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 76.2%｜历史 Rank 70%（近端代理）｜IV/RV 1.35×（近似）｜净 delta 敞口 正 153,964 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-23/SNDK_evening.json