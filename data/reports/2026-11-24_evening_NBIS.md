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
🟡 **近现价集中开仓**: 12-04 90P ΔOI +731（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 94.62 → 收盘 87.31（-7.7%） ｜ 今日高 95.28 ｜ 低 84.30 ｜ 昨收 97.80 → 收盘 87.31（-10.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-27，窗口结束前不做对错判定）

Options: P/C成交量 0.56 | OI比 0.40 | ATM IV 139.3% | Skew 14.2pp | Term 0.93 | ExpMove ±9.8%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构正常（Term 0.93）｜保护溢价显著（Skew 14.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.40×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-27（3D）±9.8% ｜ 12-04（10D）±18.5% ｜ 12-11（17D）±24.2% ｜ 12-18（24D）±26.7%
   ⇒ IV–VIX Spread: +112.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,810,326 | GEX Change vs 上次快照 -1,968,508 | Flip: Primary Flip: 93.44（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 666 / LOW 118 / INVALID 170
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 93.44（全链重定价，覆盖 100%）
Put Wall 80（弱结构｜现价高于该位 9.1%）
最近结构参考: Flip 93（现价低于该位 6.6%）
量化视角： 负 Gamma（481万，无历史分位）｜负 Gamma 加深（197万）｜现价位于 Flip 下方 6.56%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 100（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 93（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +28.5k / P +11.2k ｜ Activity HIGH ｜ 3D
12-04  C +4.8k / P +4.2k ｜ Activity HIGH ｜ 10D
12-11  C +2.1k / P +2.1k ｜ Activity HIGH ｜ 17D
12-18  C +5.9k / P +11.7k ｜ Activity HIGH ｜ 24D

📆 11-27 Forward Structure
存量OI: C 92.8k / P 37.4k，今日变化ΔOI: C +28.5k / P +11.2k，平值价格ATM: C $4.45 / P $4.15 ｜ ATM IV 139.3%，净 delta 敞口 -665k shares
Top ΔOI: C 110 +4,317 ｜ C 102 +2,072
仓位参考: Max Pain 100 ｜ Put Wall 80（-8.4%）（OI 4.7k）
量化解读： 存量 Call 重｜ATM IV 139.3%｜历史 Rank 82%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 664,863 股

📆 12-04 Forward Structure
存量OI: C 27.2k / P 15.2k，今日变化ΔOI: C +4.8k / P +4.2k，平值价格ATM: C $8.40 / P $7.78 ｜ ATM IV 139.2%，净 delta 敞口 -140k shares
Top ΔOI: C 100 +978 ｜ P 90 +731
仓位参考: Max Pain 100 ｜ Put Wall 90（+3.1%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 139.2%｜历史 Rank 82%（近端代理）｜IV/RV 0.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 139,509 股

📆 12-11 Forward Structure
存量OI: C 10.5k / P 13.0k，今日变化ΔOI: C +2.1k / P +2.1k，平值价格ATM: C $10.40 / P $10.75 ｜ ATM IV 129.2%，净 delta 敞口 -61k shares
Top ΔOI: C 120 +404 ｜ C 110 +391 ｜ P 95 +349
仓位参考: Max Pain 115 ｜ Call Wall 90（+3.1%，弱）（OI 0.3k） ｜ Put Wall 85（-2.6%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 129.2%｜历史 Rank 82%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 60,777 股

📆 12-18 Forward Structure
存量OI: C 143.2k / P 109.6k，今日变化ΔOI: C +5.9k / P +11.7k，平值价格ATM: C $11.90 / P $11.40 ｜ ATM IV 135.8%，净 delta 敞口 -284k shares
Top ΔOI: C 150 +2,097 ｜ P 80 +1,272 ｜ P 95 +1,129
仓位参考: Max Pain 145 ｜ Put Wall 80（-8.4%，弱）（OI 7.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 135.8%｜历史 Rank 82%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 负 283,666 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=107 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=107）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/NBIS_evening.json