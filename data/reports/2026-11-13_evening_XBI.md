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
🟡 **近现价集中开仓**: 11-20 145C ΔOI +1,000（距现价 -3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 151.24 → 收盘 150.55（-0.5%） ｜ 今日高 151.29 ｜ 低 148.17 ｜ 昨收 151.20 → 收盘 150.55（-0.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 0.36 | OI比 0.80 | ATM IV 60.3% | Skew 22.9pp | Term 0.52 | ExpMove ±3.6%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜保护溢价显著（Skew 22.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（7D）±3.6% ｜ 11-27（14D）±5.1% ｜ 12-04（21D）±3.6% ｜ 12-11（28D）±3.5%
   ⇒ IV–VIX Spread: +41.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,876,490 | GEX Change vs 上次快照 6,832,092 | Flip: Primary Flip: 152.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 409 / LOW 167 / INVALID 346
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 152.94（全链重定价，覆盖 90%）
最近结构参考: Flip 153（现价低于该位 1.6%）
量化视角： 负 Gamma（988万，无历史分位）｜负 Gamma 缓解（+683万）｜现价位于 Flip 下方 1.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 153（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +1.4k / P +0.8k ｜ Activity HIGH ｜ 7D
11-27  C +51 / P +1.0k ｜ Activity HIGH ｜ 14D
12-04  C +21 / P +15 ｜ Activity MEDIUM △ ｜ 21D
12-11  C +18 / P +8 ｜ Activity MEDIUM △ ｜ 28D

📆 11-20 Forward Structure
存量OI: C 26.1k / P 57.3k，今日变化ΔOI: C +1.4k / P +0.8k，平值价格ATM: C $2.62 / P $2.82 ｜ ATM IV 32.9%，净 delta 敞口 84k shares
Top ΔOI: C 145 +1,000 ｜ P 145 +364 ｜ C 155 -300
仓位参考: Max Pain 153 ｜ Call Wall 160（+6.3%，弱）（OI 2.7k） ｜ Put Wall 145（-3.7%，弱）（OI 6.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 32.9%｜历史 Rank 99%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 84,264 股

📆 11-27 Forward Structure
存量OI: C 1.2k / P 2.9k，今日变化ΔOI: C +51 / P +1.0k，平值价格ATM: C $3.70 / P $3.95 ｜ ATM IV 31.6%，净 delta 敞口 -20k shares
Top ΔOI: P 147 +303 ｜ P 137 +300 ｜ P 145 +202
仓位参考: Max Pain 158 ｜ Call Wall 152.5（+1.3%，弱）（OI 0.1k） ｜ Put Wall 147（-2.4%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 31.6%｜历史 Rank 99%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 负 19,991 股

12-04（MEDIUM △）Top ΔOI: 152C +20 ｜ 141P +5
12-04（MEDIUM △）仓位参考: Max Pain 161 ｜ Call Wall 160（+6.3%，弱）（OI 22） ｜ Put Wall 159（+5.6%，弱）（OI 80）

12-11（MEDIUM △）Top ΔOI: 161C +10 ｜ 145C +5
12-11（MEDIUM △）仓位参考: Max Pain 150 ｜ Call Wall 154（+2.3%，弱）（OI 84） ｜ Put Wall 143（-5.0%，弱）（OI 0.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/XBI_evening.json