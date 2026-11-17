# 期权晚报 2026-11-16（快照 21:00 ET）

📊 市场环境

SPY $739.95 ｜ QQQ $661.75
VIX 22.91 ↑18.7%（5D +15.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.8
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 42.59 → 收盘 42.39（-0.5%） ｜ 今日高 42.92 ｜ 低 42.01 ｜ 昨收 44.13 → 收盘 42.39（-3.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-19，窗口结束前不做对错判定）

Options: P/C成交量 0.46 | OI比 0.54 | ATM IV 52.6% | Skew 6.1pp | Term 0.85 | ExpMove ±3.1%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价显著（Skew 6.1pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-18（2D）±3.1% ｜ 11-20（4D）±4.5% ｜ 11-23（7D）±5.0% ｜ 11-25（9D）±5.9%
   ⇒ IV–VIX Spread: +29.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -37,203,703 | GEX Change vs 上次快照 -9,404,589 | Flip: Primary Flip: 44.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 645 / LOW 122 / INVALID 345
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 44.32（全链重定价，覆盖 99%）
Put Wall 40（弱结构｜现价高于该位 6.0%）
最近结构参考: Flip 44（现价低于该位 4.4%）
量化视角： 负 Gamma（3720万，无历史分位）｜负 Gamma 加深（940万）｜现价位于 Flip 下方 4.36%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 40（Put Wall，弱结构）；上方 45（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 44（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
11-20  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
11-25  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 11-18 Forward Structure
存量OI: C 22.1k / P 12.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.61 / P $0.72 ｜ ATM IV 52.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 45 ｜ Put Wall 40（-5.6%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 52.6%｜历史 Rank 86%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-20（Activity LOW）仓位参考: Max Pain 50 ｜ Put Wall 45（+6.2%，弱）（OI 14.6k）

11-23（Activity LOW）仓位参考: Max Pain 44 ｜ Call Wall 46.5（+9.7%，弱）（OI 1.9k） ｜ Put Wall 40（-5.6%）（OI 0.3k）

11-25（Activity LOW）仓位参考: Max Pain 45 ｜ Call Wall 45（+6.2%，弱）（OI 60） ｜ Put Wall 44.5（+5.0%，弱）（OI 0.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-16/SLV_evening.json