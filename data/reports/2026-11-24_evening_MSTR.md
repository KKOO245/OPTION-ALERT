# 期权晚报 2026-11-24（快照 16:40 ET）

📊 市场环境

SPY $718.78 ｜ QQQ $638.10
VIX 26.36 ↓1.0%（5D +3.5%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 17.4（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.5
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 待公布 ｜ 前值 1.5
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 1.8

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 12-04 80P ΔOI +1,071（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 82.33 → 收盘 77.55（-5.8%） ｜ 今日高 82.92 ｜ 低 77.32 ｜ 昨收 84.40 → 收盘 77.55（-8.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 0.68 | OI比 0.60 | ATM IV 109.0% | Skew 7.8pp | Term 0.91 | ExpMove ±7.8%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构正常（Term 0.91）｜保护溢价显著（Skew 7.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±7.8% ｜ 12-04（10D）±15.1% ｜ 12-11（17D）±9.2% ｜ 12-18（24D）±21.3%
   ⇒ IV–VIX Spread: +82.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -11,376,186 | GEX Change vs 上次快照 -15,579,587 | Flip: Primary Flip: 80.09（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 533 / LOW 207 / INVALID 288
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 80.09（全链重定价，覆盖 100%）
Put Wall 80（弱结构｜现价低于该位 3.1%）
最近结构参考: Put Wall 80（现价低于该位 3.1%）
量化视角： 负 Gamma（1138万，无历史分位）｜由正转负（1558万）｜现价位于 Flip 下方 3.17%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 80（Put Wall，弱结构） / 86（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 80（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +23.7k / P +5.5k ｜ Activity HIGH ｜ 3D
12-04  C +6.6k / P +7.3k ｜ Activity HIGH ｜ 10D
12-11  C +1.3k / P +2.9k ｜ Activity HIGH ｜ 17D
12-18  C +5.5k / P -0.3k ｜ Activity HIGH ｜ 24D

📆 11-27 Forward Structure
存量OI: C 269.8k / P 161.5k，今日变化ΔOI: C +23.7k / P +5.5k，平值价格ATM: C $2.80 / P $3.23 ｜ ATM IV 109.0%，净 delta 敞口 -118k shares
仓位参考: Max Pain 86 ｜ Call Wall 85（+9.6%，弱）（OI 28.0k） ｜ Put Wall 80（+3.2%，弱）（OI 9.2k）
量化解读： 存量 Call 重｜ATM IV 109.0%｜历史 Rank 86%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 117,597 股

📆 12-04 Forward Structure
存量OI: C 44.0k / P 71.7k，今日变化ΔOI: C +6.6k / P +7.3k，平值价格ATM: C $5.80 / P $5.88 ｜ ATM IV 110.7%，净 delta 敞口 -109k shares
Top ΔOI: P 80 +1,071 ｜ P 67 +851
仓位参考: Max Pain 95 ｜ Call Wall 85（+9.6%，弱）（OI 0.9k） ｜ Put Wall 85（+9.6%，弱）（OI 6.9k）
量化解读： 存量 Put 重｜ATM IV 110.7%｜历史 Rank 86%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 108,601 股

📆 12-11 Forward Structure
存量OI: C 12.0k / P 37.0k，今日变化ΔOI: C +1.3k / P +2.9k，平值价格ATM: C $0.00 / P $7.10 ｜ ATM IV 107.6%，净 delta 敞口 -10k shares
Top ΔOI: P 80 +1,038 ｜ P 60 +733 ｜ P 55 +682
仓位参考: Max Pain 100 ｜ Put Wall 80（+3.2%，弱）（OI 4.2k）
量化解读： 存量 Put 重｜ATM IV 107.6%｜历史 Rank 86%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 9,897 股

📆 12-18 Forward Structure
存量OI: C 245.0k / P 172.1k，今日变化ΔOI: C +5.5k / P -0.3k，平值价格ATM: C $8.50 / P $8.00 ｜ ATM IV 104.6%，净 delta 敞口 304k shares
Top ΔOI: C 150 +4,747 ｜ P 180 -930
仓位参考: Max Pain 120 ｜ Call Wall 85（+9.6%，弱）（OI 9.6k） ｜ Put Wall 80（+3.2%，弱）（OI 9.0k）
量化解读： 存量 Call 重｜ATM IV 104.6%｜历史 Rank 86%（近端代理）｜IV/RV 1.35×（近似）｜净 delta 敞口 正 303,953 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/MSTR_evening.json