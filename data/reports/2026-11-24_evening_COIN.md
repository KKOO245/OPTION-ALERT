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


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 107.49 → 收盘 102.35（-4.8%） ｜ 今日高 107.49 ｜ 低 101.91 ｜ 昨收 108.78 → 收盘 102.35（-5.9%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 0.54 | OI比 0.58 | ATM IV 80.7% | Skew 7.2pp | Term 1.00 | ExpMove ±5.8%（近端） | Rank 61%
量化视角： IV 中性（Rank 61%）｜期限结构正常（Term 1.00）｜保护溢价显著（Skew 7.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.58）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±5.8% ｜ 12-04（10D）±11.2% ｜ 12-11（17D）±11.5% ｜ 12-18（24D）±16.4%
   ⇒ IV–VIX Spread: +54.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,924,175 | GEX Change vs 上次快照 -6,993,926 | Flip: Primary Flip: 103.72（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 410 / LOW 213 / INVALID 365
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 103.72（全链重定价，覆盖 98%）
Put Wall 110（弱结构｜现价低于该位 7.0%）
最近结构参考: Flip 104（现价低于该位 1.3%）
量化视角： 负 Gamma（292万，无历史分位）｜由正转负（699万）｜现价位于 Flip 下方 1.32%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 110（Put Wall，弱结构） / 110（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 104（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +5.9k / P +4.1k ｜ Activity HIGH ｜ 3D
12-04  C +2.6k / P +5.1k ｜ Activity HIGH ｜ 10D
12-11  C +0.7k / P +2.1k ｜ Activity HIGH ｜ 17D
12-18  C +5.4k / P +1.3k ｜ Activity HIGH ｜ 24D

📆 11-27 Forward Structure
存量OI: C 63.0k / P 36.4k，今日变化ΔOI: C +5.9k / P +4.1k，平值价格ATM: C $3.15 / P $2.75 ｜ ATM IV 80.7%，净 delta 敞口 -23k shares
仓位参考: Max Pain 110 ｜ Call Wall 112（+9.4%，弱）（OI 5.4k） ｜ Put Wall 100（-2.3%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 80.7%｜历史 Rank 61%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 22,682 股

📆 12-04 Forward Structure
存量OI: C 13.1k / P 18.8k，今日变化ΔOI: C +2.6k / P +5.1k，平值价格ATM: C $6.52 / P $4.93 ｜ ATM IV 82.4%，净 delta 敞口 -161k shares
Top ΔOI: P 113 +1,551 ｜ P 97 +1,513
仓位参考: Max Pain 125 ｜ Put Wall 97（-5.2%，弱）（OI 1.5k）
量化解读： 存量 Put 重｜ATM IV 82.4%｜历史 Rank 61%（近端代理）｜IV/RV 1.24×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 161,307 股

📆 12-11 Forward Structure
存量OI: C 4.3k / P 7.1k，今日变化ΔOI: C +0.7k / P +2.1k，平值价格ATM: C $7.60 / P $4.21 ｜ ATM IV 80.3%，净 delta 敞口 -12k shares
仓位参考: Max Pain 125 ｜ Call Wall 110（+7.5%，弱）（OI 0.3k） ｜ Put Wall 100（-2.3%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 80.3%｜历史 Rank 61%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 11,637 股

📆 12-18 Forward Structure
存量OI: C 144.2k / P 55.6k，今日变化ΔOI: C +5.4k / P +1.3k，平值价格ATM: C $8.90 / P $7.85 ｜ ATM IV 77.5%，净 delta 敞口 95k shares
Top ΔOI: C 150 +2,002 ｜ C 130 +669
仓位参考: Max Pain 130 ｜ Put Wall 110（+7.5%）（OI 7.9k）
量化解读： 存量 Call 重｜ATM IV 77.5%｜历史 Rank 61%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 正 95,309 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/COIN_evening.json