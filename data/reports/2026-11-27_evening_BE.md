# 期权晚报 2026-11-27（快照 16:40 ET）

📊 市场环境

SPY $728.32 ｜ QQQ $650.99
VIX 23.81 ↓11.2%（5D -33.7%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 12-11 155C ΔOI +780（距现价 -4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 177.5）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull
• 月度备份：把 D:\git\EXTERNAL DATA\OPTION-ALERT-DB\options_eod.db 拷贝到网盘/移动盘保存


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 161.35 → 收盘 163.02（+1.0%） ｜ 今日高 163.15 ｜ 低 153.11 ｜ 昨收 152.89 → 收盘 163.02（+6.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-04，窗口结束前不做对错判定）

Options: P/C成交量 1.00 | OI比 0.61 | ATM IV 125.1% | Skew 2.9pp | Term 0.81 | ExpMove ±12.4%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价中性（Skew 2.9pp）｜存量 Call 偏重（OI比 0.61）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.00×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.61×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 12-04（7D）±12.4% ｜ 12-11（14D）±16.8% ｜ 12-18（21D）±19.9% ｜ 12-24（27D）±22.4%
   ⇒ IV–VIX Spread: +101.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,624,346 | GEX Change vs 上次快照 -977,935 | Flip: Candidates 177.47 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 78%（带内） ｜ IV 有效性: VALID 516 / LOW 100 / INVALID 432
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈177（全链重定价，覆盖 78%，CONDITIONAL）
Put Wall 150（弱结构｜现价高于该位 8.7%）
最近结构参考: Flip 177（现价低于该位 8.1%）
量化视角： 负 Gamma（262万，无历史分位）｜负 Gamma 加深（98万）｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构） / 152（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 177（全链重定价，覆盖 78%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

12-04  C +3.7k / P +3.5k ｜ Activity HIGH ｜ 7D
12-11  C +1.4k / P +0.5k ｜ Activity HIGH ｜ 14D
12-18  C +2.3k / P +1.1k ｜ Activity HIGH ｜ 21D
12-24  C +0.4k / P +0.3k ｜ Activity HIGH ｜ 27D

📆 12-04 Forward Structure
存量OI: C 18.0k / P 19.9k，今日变化ΔOI: C +3.7k / P +3.5k，平值价格ATM: C $10.32 / P $9.87 ｜ ATM IV 110.3%，净 delta 敞口 152k shares
Top ΔOI: P 140 +1,161 ｜ C 150 +558
仓位参考: Max Pain 175 ｜ Call Wall 170（+4.3%，弱）（OI 0.9k） ｜ Put Wall 150（-8.0%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 110.3%｜历史 Rank 79%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 151,567 股

📆 12-11 Forward Structure
存量OI: C 7.1k / P 6.0k，今日变化ΔOI: C +1.4k / P +0.5k，平值价格ATM: C $13.10 / P $14.30 ｜ ATM IV 108.0%，净 delta 敞口 85k shares
Top ΔOI: C 155 +780 ｜ C 145 +195
仓位参考: Max Pain 175 ｜ Call Wall 155（-4.9%）（OI 0.9k） ｜ Put Wall 175（+7.3%）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 108.0%｜历史 Rank 79%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 85,251 股

📆 12-18 Forward Structure
存量OI: C 67.2k / P 78.6k，今日变化ΔOI: C +2.3k / P +1.1k，平值价格ATM: C $16.15 / P $16.35 ｜ ATM IV 105.5%，净 delta 敞口 143k shares
Top ΔOI: C 180 +912 ｜ P 140 +456 ｜ C 140 +422
仓位参考: Max Pain 200 ｜ Call Wall 170（+4.3%，弱）（OI 2.0k） ｜ Put Wall 150（-8.0%，弱）（OI 6.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 105.5%｜历史 Rank 79%（近端代理）｜IV/RV 0.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 142,942 股

📆 12-24 Forward Structure
存量OI: C 4.6k / P 4.6k，今日变化ΔOI: C +0.4k / P +0.3k，平值价格ATM: C $16.25 / P $20.20 ｜ ATM IV 100.8%，净 delta 敞口 15k shares
Top ΔOI: C 180 +168 ｜ P 150 +147 ｜ C 155 +87
仓位参考: Max Pain 170 ｜ Call Wall 160（-1.9%，弱）（OI 0.3k） ｜ Put Wall 150（-8.0%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 100.8%｜历史 Rank 79%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 正 15,340 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-27/BE_evening.json