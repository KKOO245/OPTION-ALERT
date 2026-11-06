# 期权晚报 2026-11-06（快照 16:40 ET）

📊 市场环境

SPY $735.29 ｜ QQQ $656.10
VIX 25.64 ↓9.0%（5D +32.0%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 22.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 165 ｜ 前值 60　✅ 今日已公布
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 4.1 ｜ 前值 4.2　✅ 今日已公布
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 51 ｜ 前值 46.3　✅ 今日已公布

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-20 870P ΔOI +1,931（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 883.2）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 数据归档：明天（周六）10:30 自动运行，请保持电脑开机；若未自动运行，手动执行：D:\git\python\python.exe C:\Users\Kody\Documents\Codex\2026-08-17\xian\work\OPTION-ALERT\scripts\archive_eod.py


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 898.27 → 收盘 835.06（-7.0%） ｜ 今日高 912.09 ｜ 低 816.42 ｜ 昨收 806.43 → 收盘 835.06（+3.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-11，窗口结束前不做对错判定）

Options: P/C成交量 0.97 | OI比 0.49 | ATM IV 121.8% | Skew 2.8pp | Term 0.83 | ExpMove ±12.9%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 2.8pp）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.97×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（7D）±12.9% ｜ 11-20（14D）±17.5% ｜ 11-27（21D）±20.0% ｜ 12-04（28D）±22.1%
   ⇒ IV–VIX Spread: +96.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,696,365 | GEX Change vs 上次快照 -2,077,145 | Flip: Candidates 883.20 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 1349 / LOW 504 / INVALID 1895
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈883（全链重定价，覆盖 78%，CONDITIONAL）
Put Wall 800（弱结构｜现价高于该位 4.4%）
最近结构参考: Put Wall 800（现价高于该位 4.4%）
量化视角： 负 Gamma（170万，无历史分位）｜由正转负（208万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 800（Put Wall，弱结构）；上方 925（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 883（全链重定价，覆盖 78%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +9.2k / P +4.8k ｜ Activity HIGH ｜ 7D
11-20  C +9.5k / P -1.8k ｜ Activity HIGH ｜ 14D
11-27  C +1.3k / P +0.4k ｜ Activity HIGH ｜ 21D
12-04  C +1.5k / P +0.4k ｜ Activity HIGH ｜ 28D

📆 11-13 Forward Structure
存量OI: C 28.5k / P 16.7k，今日变化ΔOI: C +9.2k / P +4.8k，平值价格ATM: C $55.10 / P $52.63 ｜ ATM IV 115.1%，净 delta 敞口 172k shares
Top ΔOI: P 700 +1,288 ｜ C 950 +1,044
仓位参考: Max Pain 995 ｜ Call Wall 890（+6.6%，弱）（OI 0.5k） ｜ Put Wall 820（-1.8%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 115.1%｜历史 Rank 80%（近端代理）｜IV/RV 0.96×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 172,206 股

📆 11-20 Forward Structure
存量OI: C 66.9k / P 51.4k，今日变化ΔOI: C +9.5k / P -1.8k，平值价格ATM: C $71.92 / P $73.95 ｜ ATM IV 113.0%，净 delta 敞口 665k shares
Top ΔOI: P 870 +1,931 ｜ P 1680 -1,102 ｜ C 1600 +1,085
仓位参考: Max Pain 1,160 ｜ Call Wall 800（-4.2%，弱）（OI 2.3k） ｜ Put Wall 870（+4.2%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 113.0%｜历史 Rank 80%（近端代理）｜IV/RV 0.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 665,469 股

📆 11-27 Forward Structure
存量OI: C 15.1k / P 8.9k，今日变化ΔOI: C +1.3k / P +0.4k，平值价格ATM: C $82.15 / P $84.75 ｜ ATM IV 104.8%，净 delta 敞口 43k shares
Top ΔOI: C 1000 +154 ｜ P 860 +112 ｜ C 1200 +101
仓位参考: Max Pain 1,200
量化解读： 存量 Call 重｜ATM IV 104.8%｜历史 Rank 80%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 42,863 股

📆 12-04 Forward Structure
存量OI: C 6.2k / P 4.3k，今日变化ΔOI: C +1.5k / P +0.4k，平值价格ATM: C $91.50 / P $93.20 ｜ ATM IV 101.5%，净 delta 敞口 27k shares
Top ΔOI: C 1500 -187 ｜ C 1120 +168 ｜ C 1095 +150
仓位参考: Max Pain 1,095 ｜ Put Wall 820（-1.8%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 101.5%｜历史 Rank 80%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 正 26,881 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-06/SNDK_evening.json