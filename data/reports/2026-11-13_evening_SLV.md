# 期权晚报 2026-11-13（快照 16:40 ET）

📊 市场环境

SPY $754.37 ｜ QQQ $679.89
VIX 19.30 ↑3.2%（5D -24.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-18 46C ΔOI +680（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-18 49C ΔOI +2,891 占该期限总 OI 14.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 44.78 → 收盘 44.13（-1.5%） ｜ 今日高 45.17 ｜ 低 43.97 ｜ 昨收 45.12 → 收盘 44.13（-2.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 0.94 | OI比 0.49 | ATM IV 40.5% | Skew 45.1pp | Term 1.00 | ExpMove ±2.2%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构正常（Term 1.00）｜保护溢价显著（Skew 45.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.49）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.94×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.49×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-16（3D）±2.2% ｜ 11-18（5D）±3.6% ｜ 11-20（7D）±4.6% ｜ 11-23（10D）±5.0%
   ⇒ IV–VIX Spread: +21.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,850,086 | GEX Change vs 上次快照 -16,482,206 | Flip: Primary Flip: 44.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 626 / LOW 153 / INVALID 425
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 44.67（全链重定价，覆盖 92%）
Put Wall 40（弱结构｜现价高于该位 10.3%）
最近结构参考: Flip 45（现价低于该位 1.2%）
量化视角： 负 Gamma（1485万，无历史分位）｜由正转负（1648万）｜现价位于 Flip 下方 1.20%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 40（Put Wall，弱结构）；上方 46（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 45（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-16  C +3.4k / P +2.1k ｜ Activity HIGH ｜ 3D
11-18  C +6.2k / P +1.4k ｜ Activity HIGH ｜ 5D
11-20  C -8.2k / P -4.8k ｜ Activity HIGH ｜ 7D
11-23  C +2.0k / P +0.2k ｜ Activity HIGH ｜ 10D

📆 11-16 Forward Structure
存量OI: C 14.7k / P 6.6k，今日变化ΔOI: C +3.4k / P +2.1k，平值价格ATM: C $0.55 / P $0.42 ｜ ATM IV 30.4%，净 delta 敞口 2k shares
Top ΔOI: C 48 +1,070 ｜ P 40 +970 ｜ C 48 +726
仓位参考: Max Pain 46 ｜ Call Wall 48（+8.8%，弱）（OI 2.2k） ｜ Put Wall 40（-9.4%）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 30.4%｜历史 Rank 66%（近端代理）｜IV/RV 0.71×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,861 股

📆 11-18 Forward Structure
存量OI: C 11.2k / P 8.7k，今日变化ΔOI: C +6.2k / P +1.4k，平值价格ATM: C $0.86 / P $0.72 ｜ ATM IV 39.1%，净 delta 敞口 21k shares
Top ΔOI: C 46 +680
仓位参考: Max Pain 46 ｜ Put Wall 44.5（+0.8%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 39.1%｜历史 Rank 66%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 21,379 股

📆 11-20 Forward Structure
存量OI: C 572.9k / P 147.1k，今日变化ΔOI: C -8.2k / P -4.8k，平值价格ATM: C $1.10 / P $0.92 ｜ ATM IV 41.5%，净 delta 敞口 647k shares
Top ΔOI: P 55 -2,339 ｜ P 54 -1,706
仓位参考: Max Pain 50 ｜ Put Wall 40（-9.4%，弱）（OI 13.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.5%｜历史 Rank 66%（近端代理）｜IV/RV 0.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 647,176 股

📆 11-23 Forward Structure
存量OI: C 6.4k / P 0.9k，今日变化ΔOI: C +2.0k / P +0.2k，平值价格ATM: C $1.16 / P $1.03 ｜ ATM IV 38.6%，净 delta 敞口 33k shares
Top ΔOI: C 46 +1,857 ｜ C 45 +44
仓位参考: Max Pain 45 ｜ Call Wall 47.5（+7.6%）（OI 3.0k） ｜ Put Wall 48（+8.8%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜ATM IV 38.6%｜历史 Rank 66%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 33,284 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/SLV_evening.json