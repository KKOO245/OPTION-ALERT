# 期权晚报 2026-10-16（快照 21:00 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $nan
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 725.48 → 收盘 709.80（-2.2%） ｜ 今日高 725.94 ｜ 低 707.23 ｜ 昨收 728.00 → 收盘 709.80（-2.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-21，窗口结束前不做对错判定）

Options: P/C成交量 1.13 | OI比 1.48 | ATM IV 19.1% | Skew 7.0pp | Term 1.18 | ExpMove ±1.4%（近端） | Rank 55%
量化视角： IV 中性（Rank 55%）｜期限结构正常偏陡（Term 1.18）｜保护溢价显著（Skew 7.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.13×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.48×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 7% ｜ P/C OI(近端) 37%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 7%）｜近端持仓结构中性（P/C OI 分位 37%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-19（3D）±1.4% ｜ 10-20（4D）±1.8% ｜ 10-21（5D）±2.1% ｜ 10-22（6D）±2.4%
   ⇒ IV–VIX Spread: -0.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -938,531,779 | GEX Change vs 上次快照 342,626,705 | Flip: Primary Flip: 738.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2747 / LOW 190 / INVALID 1323
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 738.33（全链重定价，覆盖 100%）
Put Wall 700（弱结构｜现价高于该位 1.4%）
最近结构参考: Put Wall 700（现价高于该位 1.4%）
量化视角： 负 Gamma（9.39亿，历史分位偏负区，比 93% 的交易日更负）｜负 Gamma 缓解（+3.43亿）｜现价位于 Flip 下方 3.86%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall，弱结构）；上方 730（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 738（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-20  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-21  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-22  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 10-19 Forward Structure
存量OI: C 89.5k / P 132.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.75 / P $5.14 ｜ ATM IV 19.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 730 ｜ Call Wall 725（+2.1%，弱）（OI 2.5k） ｜ Put Wall 700（-1.4%，弱）（OI 8.4k）
量化解读： 存量 Put 重｜ATM IV 19.1%｜历史 Rank 55%（近端代理）｜IV/RV 1.61×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-20（Activity LOW）仓位参考: Max Pain 728 ｜ Put Wall 705（-0.7%，弱）（OI 6.8k）

10-21（Activity LOW）仓位参考: Max Pain 733 ｜ Call Wall 730（+2.8%，弱）（OI 1.0k） ｜ Put Wall 710（+0.0%，弱）（OI 3.5k）

10-22（Activity LOW）仓位参考: Max Pain 727 ｜ Call Wall 710（+0.0%，弱）（OI 1.4k） ｜ Put Wall 705（-0.7%，弱）（OI 3.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/QQQ_evening.json