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
🟡 **近现价集中开仓**: 11-16 160P ΔOI +6,723（距现价 -1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 169.89 → 收盘 162.85（-4.1%） ｜ 今日高 170.00 ｜ 低 158.39 ｜ 昨收 166.19 → 收盘 162.85（-2.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-18，窗口结束前不做对错判定）

Options: P/C成交量 0.90 | OI比 0.75 | ATM IV 54.5% | Skew -12.9pp | Term 1.10 | ExpMove ±3.7%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构正常（Term 1.10）｜Put 保护异常便宜（Skew -12.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-16（3D）±3.7% ｜ 11-18（5D）±8.6% ｜ 11-20（7D）±9.6% ｜ 11-23（10D）±10.1%
   ⇒ IV–VIX Spread: +35.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -24,309,000 | GEX Change vs 上次快照 -15,766,367 | Flip: Primary Flip: 164.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 1203 / LOW 252 / INVALID 765
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 164.53（全链重定价，覆盖 91%）
Put Wall 150（弱结构｜现价高于该位 8.6%）
最近结构参考: Flip 165（现价低于该位 1.0%）
量化视角： 负 Gamma（2431万，无历史分位）｜负 Gamma 加深（1577万）｜现价位于 Flip 下方 1.02%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall，弱结构）；上方 168（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 165（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-16  C +52.9k / P +64.1k ｜ Activity HIGH ｜ 3D
11-18  C +43.4k / P +36.9k ｜ Activity HIGH ｜ 5D
11-20  C +132.2k / P +79.7k ｜ Activity HIGH ｜ 7D
11-23  C +10.2k / P +3.8k ｜ Activity HIGH ｜ 10D

📆 11-16 Forward Structure
存量OI: C 175.2k / P 121.0k，今日变化ΔOI: C +52.9k / P +64.1k，平值价格ATM: C $3.15 / P $2.82 ｜ ATM IV 50.1%，净 delta 敞口 783k shares
Top ΔOI: P 150 +10,305 ｜ P 160 +6,723
仓位参考: Max Pain 168 ｜ Call Wall 170（+4.4%，弱）（OI 9.0k） ｜ Put Wall 150（-7.9%，弱）（OI 13.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 50.1%｜历史 Rank 79%（近端代理）｜IV/RV 0.94×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 783,178 股

📆 11-18 Forward Structure
存量OI: C 130.6k / P 87.3k，今日变化ΔOI: C +43.4k / P +36.9k，平值价格ATM: C $7.10 / P $6.90 ｜ ATM IV 92.3%，净 delta 敞口 580k shares
Top ΔOI: C 180 +9,361 ｜ P 150 +7,905 ｜ C 170 +3,644
仓位参考: Max Pain 170 ｜ Call Wall 175（+7.5%，弱）（OI 9.4k） ｜ Put Wall 150（-7.9%）（OI 10.4k）
量化解读： 存量 Call 重｜ATM IV 92.3%｜历史 Rank 79%（近端代理）｜IV/RV 1.73×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 579,947 股

📆 11-20 Forward Structure
存量OI: C 1271.1k / P 841.9k，今日变化ΔOI: C +132.2k / P +79.7k，平值价格ATM: C $8.05 / P $7.65 ｜ ATM IV 87.6%，净 delta 敞口 4.5M shares
Top ΔOI: C 172 +22,378 ｜ C 180 +22,298 ｜ C 177 +19,285
仓位参考: Max Pain 190 ｜ Call Wall 175（+7.5%，弱）（OI 35.8k） ｜ Put Wall 150（-7.9%，弱）（OI 42.1k）
量化解读： 存量 Call 重｜ATM IV 87.6%｜历史 Rank 79%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,535,462 股

📆 11-23 Forward Structure
存量OI: C 29.0k / P 16.6k，今日变化ΔOI: C +10.2k / P +3.8k，平值价格ATM: C $8.40 / P $8.07 ｜ ATM IV 76.4%，净 delta 敞口 216k shares
Top ΔOI: C 165 +1,331 ｜ C 160 +1,121 ｜ C 180 +996
仓位参考: Max Pain 168 ｜ Call Wall 170（+4.4%，弱）（OI 2.1k） ｜ Put Wall 150（-7.9%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 76.4%｜历史 Rank 79%（近端代理）｜IV/RV 1.43×（近似）｜净 delta 敞口 正 216,432 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-13/NVDA_evening.json