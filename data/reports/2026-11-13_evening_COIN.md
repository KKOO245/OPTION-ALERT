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
🟡 **近现价集中开仓**: 11-20 134C ΔOI +8,445（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 127.28 → 收盘 127.64（+0.3%） ｜ 今日高 130.60 ｜ 低 125.38 ｜ 昨收 130.67 → 收盘 127.64（-2.3%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 0.56 | OI比 0.46 | ATM IV 69.2% | Skew -11.9pp | Term 0.94 | ExpMove ±7.6%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构正常（Term 0.94）｜Put 保护异常便宜（Skew -11.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±7.6% ｜ 11-27（14D）±10.4% ｜ 12-04（21D）±12.8% ｜ 12-11（28D）±15.3%
   ⇒ IV–VIX Spread: +49.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 966,128 | GEX Change vs 上次快照 -4,631,380 | Flip: Primary Flip: 126.83（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 361 / LOW 219 / INVALID 412
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 126.83（全链重定价，覆盖 84%）
Call Wall 140（弱结构｜现价低于该位 8.8%）
最近结构参考: Flip 127（现价高于该位 0.6%）
量化视角： 正 Gamma（97万，无历史分位）｜正 Gamma 减弱（463万）｜现价位于 Flip 上方 0.65%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 135（MaxPain，仅结算参考） / 140（Call Wall，弱结构）。
• Gamma 区域：切换参考 127（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +19.2k / P -2.9k ｜ Activity HIGH ｜ 7D
11-27  C +0.8k / P +13 ｜ Activity HIGH ｜ 14D
12-04  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 21D
12-11  C +0.3k / P -55 ｜ Activity HIGH ｜ 28D

📆 11-20 Forward Structure
存量OI: C 104.6k / P 59.0k，今日变化ΔOI: C +19.2k / P -2.9k，平值价格ATM: C $4.72 / P $5.01 ｜ ATM IV 69.0%，净 delta 敞口 974k shares
Top ΔOI: C 139 +8,760 ｜ C 134 +8,445 ｜ P 175 -2,163
仓位参考: Max Pain 139 ｜ Call Wall 139（+8.9%，弱）（OI 8.9k） ｜ Put Wall 120（-6.0%）（OI 7.4k）
量化解读： 存量 Call 重｜ATM IV 69.0%｜历史 Rank 30%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 974,473 股

📆 11-27 Forward Structure
存量OI: C 7.0k / P 8.4k，今日变化ΔOI: C +0.8k / P +13，平值价格ATM: C $6.80 / P $6.50 ｜ ATM IV 67.3%，净 delta 敞口 19k shares
Top ΔOI: C 138 +219 ｜ P 133 +106
仓位参考: Max Pain 140 ｜ Call Wall 140（+9.7%，弱）（OI 0.4k） ｜ Put Wall 120（-6.0%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 67.3%｜历史 Rank 30%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 18,737 股

📆 12-04 Forward Structure
存量OI: C 5.6k / P 8.7k，今日变化ΔOI: C +0.4k / P +0.4k，平值价格ATM: C $7.75 / P $8.65 ｜ ATM IV 69.8%，净 delta 敞口 -8k shares
Top ΔOI: C 140 +117
仓位参考: Max Pain 140 ｜ Call Wall 140（+9.7%）（OI 1.5k） ｜ Put Wall 135（+5.8%）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 69.8%｜历史 Rank 30%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 7,697 股

📆 12-11 Forward Structure
存量OI: C 1.9k / P 2.5k，今日变化ΔOI: C +0.3k / P -55，平值价格ATM: C $9.50 / P $10.05 ｜ ATM IV 64.9%，净 delta 敞口 6k shares
Top ΔOI: C 135 +130 ｜ C 130 +39
仓位参考: Max Pain 135 ｜ Call Wall 135（+5.8%）（OI 0.4k） ｜ Put Wall 135（+5.8%，弱）（OI 0.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 64.9%｜历史 Rank 30%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 正 6,244 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/COIN_evening.json