# 期权晚报 2026-10-22（快照 16:40 ET）

📊 市场环境

SPY $763.96 ｜ QQQ $704.47
VIX 19.03 ↑14.1%（5D +15.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 19.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 714P ΔOI +4,383（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 713.68 → 收盘 704.47（-1.3%） ｜ 今日高 715.43 ｜ 低 701.90 ｜ 昨收 725.20 → 收盘 704.47（-2.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 0.87 | OI比 1.33 | ATM IV 29.3% | Skew 2.7pp | Term 0.87 | ExpMove ±1.4%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.87，近月 IV 高于远月）｜保护溢价中性（Skew 2.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.87×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.33×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 3% ｜ P/C OI(近端) 23%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 3%）｜近端持仓结构中性（P/C OI 分位 23%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-23（1D）±1.4% ｜ 10-26（4D）±2.1% ｜ 10-27（5D）±2.4% ｜ 10-28（6D）±2.9%
   ⇒ IV–VIX Spread: +10.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,187,284,641 | GEX Change vs 上次快照 -147,377,442 | Flip: Primary Flip: 733.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3212 / LOW 315 / INVALID 1623
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 733.16（全链重定价，覆盖 96%）
Put Wall 700（弱结构｜现价高于该位 0.6%）
最近结构参考: Put Wall 700（现价高于该位 0.6%）
量化视角： 负 Gamma（11.87亿，历史分位偏负区，比 97% 的交易日更负）｜负 Gamma 加深（1.47亿）｜现价位于 Flip 下方 3.91%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 722（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 733（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +2.3k / P +45.8k ｜ Activity MEDIUM △ ｜ 1D
10-26  C +12.4k / P +29.6k ｜ Activity HIGH ｜ 4D
10-27  C +11.8k / P +23.9k ｜ Activity HIGH ｜ 5D
10-28  C +6.4k / P +10.0k ｜ Activity HIGH ｜ 6D

📆 10-23 Forward Structure
存量OI: C 278.5k / P 466.4k，今日变化ΔOI: C +2.3k / P +45.8k，平值价格ATM: C $5.53 / P $4.60 ｜ ATM IV 34.2%，净 delta 敞口 -1.5M shares
Top ΔOI: P 714 +4,383
仓位参考: Max Pain 726 ｜ Call Wall 725（+2.9%，弱）（OI 5.5k） ｜ Put Wall 710（+0.8%，弱）（OI 46.6k）
量化解读： 存量 Put 重｜ATM IV 34.2%｜历史 Rank 89%（近端代理）｜IV/RV 2.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,462,521 股

📆 10-26 Forward Structure
存量OI: C 46.4k / P 87.1k，今日变化ΔOI: C +12.4k / P +29.6k，平值价格ATM: C $8.05 / P $7.06 ｜ ATM IV 25.1%，净 delta 敞口 -1.4M shares
Top ΔOI: P 722 +12,433 ｜ C 736 +2,874
仓位参考: Max Pain 725 ｜ Call Wall 722（+2.5%，弱）（OI 1.1k） ｜ Put Wall 722（+2.5%）（OI 12.8k）
量化解读： 存量 Put 重｜ATM IV 25.1%｜历史 Rank 89%（近端代理）｜IV/RV 1.64×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,373,678 股

📆 10-27 Forward Structure
存量OI: C 39.4k / P 62.2k，今日变化ΔOI: C +11.8k / P +23.9k，平值价格ATM: C $9.09 / P $8.05 ｜ ATM IV 26.2%，净 delta 敞口 -173k shares
Top ΔOI: P 630 +8,774 ｜ C 742 +7,299 ｜ P 640 +6,511
仓位参考: Max Pain 728 ｜ Put Wall 722（+2.5%，弱）（OI 1.9k）
量化解读： 存量 Put 重｜ATM IV 26.2%｜历史 Rank 89%（近端代理）｜IV/RV 1.71×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 172,941 股

📆 10-28 Forward Structure
存量OI: C 20.7k / P 26.3k，今日变化ΔOI: C +6.4k / P +10.0k，平值价格ATM: C $10.81 / P $9.64 ｜ ATM IV 28.1%，净 delta 敞口 -470k shares
Top ΔOI: P 720 +2,619 ｜ C 729 +994 ｜ C 750 +944
仓位参考: Max Pain 723 ｜ Call Wall 725（+2.9%，弱）（OI 0.7k） ｜ Put Wall 720（+2.2%）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 28.1%｜历史 Rank 89%（近端代理）｜IV/RV 1.83×（近似）｜净 delta 敞口 负 469,671 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=61 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=61）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-22/QQQ_evening.json