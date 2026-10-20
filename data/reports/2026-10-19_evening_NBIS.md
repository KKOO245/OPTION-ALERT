# 期权晚报 2026-10-19（快照 21:00 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **事件差分**: 10-23 ATM IV 101.9% vs 10-30 91.5%（差 +10.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 176.60 → 收盘 170.24（-3.6%） ｜ 今日高 176.69 ｜ 低 166.59 ｜ 昨收 165.47 → 收盘 170.24（+2.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-22，窗口结束前不做对错判定）

Options: P/C成交量 0.66 | OI比 0.72 | ATM IV 101.9% | Skew 3.2pp | Term 0.90 | ExpMove ±8.5%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构倒挂（Term 0.90，近月 IV 高于远月）｜保护溢价中性（Skew 3.2pp）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（4D）±8.5% ｜ 10-30（11D）±12.7% ｜ 11-06（18D）±15.8% ｜ 11-13（25D）±20.1%
   ⇒ IV–VIX Spread: +83.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,786,644 | GEX Change vs 上次快照 521,813 | Flip: Primary Flip: 181.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 497 / LOW 38 / INVALID 205
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 181.73（全链重定价，覆盖 100%）
最近结构参考: Flip 182（现价低于该位 6.3%）
量化视角： 负 Gamma（779万，无历史分位）｜负 Gamma 缓解（+52万）｜现价位于 Flip 下方 6.32%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 190（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 182（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-23 Forward Structure
存量OI: C 85.6k / P 61.5k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $7.50 / P $7.03 ｜ ATM IV 101.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 190 ｜ Call Wall 180（+5.7%，弱）（OI 3.9k） ｜ Put Wall 165（-3.1%，弱）（OI 3.8k）
量化解读： 存量 Call 重｜ATM IV 101.9%｜历史 Rank 48%（近端代理）｜IV/RV 1.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 205 ｜ Put Wall 180（+5.7%，弱）（OI 1.6k）

11-06（Activity LOW）仓位参考: Max Pain 210 ｜ Put Wall 170（-0.1%，弱）（OI 1.5k）

11-13（Activity LOW）仓位参考: Max Pain 210 ｜ Call Wall 180（+5.7%，弱）（OI 0.4k） ｜ Put Wall 165（-3.1%，弱）（OI 1.2k）

📅 事件差分（观察，非因果）: 10-23（4D）ATM IV 101.9% vs 10-30 91.5%（差 +10.3pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=59 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=59）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/NBIS_evening.json