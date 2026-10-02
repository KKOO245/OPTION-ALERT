# 期权晚报 2026-10-02（快照 16:40 ET）

📊 市场环境

SPY $769.64 ｜ QQQ $749.58
VIX 15.31 ↓6.6%（5D +3.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 14.08 → 收盘 13.59（-3.5%） ｜ 今日高 14.08 ｜ 低 13.54 ｜ 昨收 13.80 → 收盘 13.59（-1.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-07，窗口结束前不做对错判定）

Options: P/C成交量 0.78 | OI比 0.27 | ATM IV 132.1% | Skew -2.7pp | Term 0.50 | ExpMove ±6.3%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构倒挂（Term 0.50，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.27）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.27×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±6.3% ｜ 10-16（14D）±9.7% ｜ 10-23（21D）±13.0% ｜ 10-30（28D）±14.9%
   ⇒ IV–VIX Spread: +116.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,684,816 | GEX Change vs 上次快照 -2,058,545 | Flip: Primary Flip: 14.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 184 / LOW 63 / INVALID 157
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 14.34（全链重定价，覆盖 82%）
最近结构参考: Flip 14（现价低于该位 5.2%）
量化视角： 负 Gamma（168万，无历史分位）｜由正转负（206万）｜现价位于 Flip 下方 5.22%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 15（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 14（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.5k / P +0.1k ｜ Activity HIGH ｜ 7D
10-16  C -0.5k / P +0.7k ｜ Activity HIGH ｜ 14D
10-23  C -17 / P +0.6k ｜ Activity HIGH ｜ 21D
10-30  C -0.3k / P +0.9k ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 10.8k / P 6.7k，今日变化ΔOI: C +0.5k / P +0.1k，平值价格ATM: C $0.49 / P $0.37 ｜ ATM IV 55.3%，净 delta 敞口 32k shares
Top ΔOI: P 15 -441 ｜ P 13 +368
仓位参考: Max Pain 16 ｜ Put Wall 14（+3.0%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 55.3%｜历史 Rank 67%（近端代理）｜IV/RV 1.01×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 32,344 股

📆 10-16 Forward Structure
存量OI: C 47.0k / P 16.8k，今日变化ΔOI: C -0.5k / P +0.7k，平值价格ATM: C $0.72 / P $0.60 ｜ ATM IV 64.6%，净 delta 敞口 -27k shares
Top ΔOI: P 15 +508 ｜ P 13 +461
仓位参考: Max Pain 16 ｜ Put Wall 14（+3.0%，弱）（OI 2.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 64.6%｜历史 Rank 67%（近端代理）｜IV/RV 1.18×（近似）｜净 delta 敞口 负 27,387 股

📆 10-23 Forward Structure
存量OI: C 9.8k / P 4.3k，今日变化ΔOI: C -17 / P +0.6k，平值价格ATM: C $1.02 / P $0.75 ｜ ATM IV 66.5%，净 delta 敞口 -45k shares
Top ΔOI: P 16 +359 ｜ P 14 +61
仓位参考: Max Pain 17 ｜ Put Wall 14（+3.0%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 66.5%｜历史 Rank 67%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 45,162 股

📆 10-30 Forward Structure
存量OI: C 3.9k / P 6.0k，今日变化ΔOI: C -0.3k / P +0.9k，平值价格ATM: C $1.10 / P $0.93 ｜ ATM IV 65.4%，净 delta 敞口 -30k shares
Top ΔOI: P 12 +425 ｜ P 17 +153
仓位参考: Max Pain 16 ｜ Put Wall 14（+3.0%）（OI 2.5k）
量化解读： 存量 Put 重｜ATM IV 65.4%｜历史 Rank 67%（近端代理）｜IV/RV 1.19×（近似）｜净 delta 敞口 负 30,240 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=39 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=39）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/USAR_evening.json