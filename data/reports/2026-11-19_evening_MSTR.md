# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $645.04
VIX 28.44 ↑15.8%（5D +52.1%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 12-04 85P ΔOI +1,573（距现价 -1.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 93.11 → 收盘 86.13（-7.5%） ｜ 今日高 93.82 ｜ 低 86.02 ｜ 昨收 90.32 → 收盘 86.13（-4.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 1.40 | OI比 0.63 | ATM IV 130.9% | Skew 11.9pp | Term 0.73 | ExpMove ±5.5%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价显著（Skew 11.9pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.63）+ 当日成交偏 Put（P/C量 1.40）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.40×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±5.5% ｜ 11-27（8D）±11.2% ｜ 12-04（15D）±15.5% ｜ 12-11（22D）±18.9%
   ⇒ IV–VIX Spread: +102.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -38,218,933 | GEX Change vs 上次快照 -564,451 | Flip: Primary Flip: 96.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 488 / LOW 273 / INVALID 379
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 96.52（全链重定价，覆盖 94%）
Put Wall 90（弱结构｜现价低于该位 4.3%）
最近结构参考: Put Wall 90（现价低于该位 4.3%）
量化视角： 负 Gamma（3822万，无历史分位）｜负 Gamma 加深（56万）｜现价位于 Flip 下方 10.76%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 90（Put Wall，弱结构） / 107（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 97（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C -41.7k / P -9.9k ｜ Activity HIGH ｜ 1D
11-27  C +44.9k / P +10.9k ｜ Activity HIGH ｜ 8D
12-04  C +2.9k / P +9.8k ｜ Activity HIGH ｜ 15D
12-11  C +0.7k / P +1.9k ｜ Activity HIGH ｜ 22D

📆 11-20 Forward Structure
存量OI: C 283.6k / P 178.2k，今日变化ΔOI: C -41.7k / P -9.9k，平值价格ATM: C $2.49 / P $2.28 ｜ ATM IV 130.9%，净 delta 敞口 1.7M shares
仓位参考: Max Pain 107 ｜ Put Wall 90（+4.5%，弱）（OI 14.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 130.9%｜历史 Rank 94%（近端代理）｜IV/RV 1.94×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,716,304 股

📆 11-27 Forward Structure
存量OI: C 88.2k / P 102.5k，今日变化ΔOI: C +44.9k / P +10.9k，平值价格ATM: C $5.00 / P $4.65 ｜ ATM IV 96.0%，净 delta 敞口 780k shares
Top ΔOI: C 98 +8,550 ｜ C 103 +7,725 ｜ C 97 +5,420
仓位参考: Max Pain 98 ｜ Put Wall 90（+4.5%）（OI 15.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 96.0%｜历史 Rank 94%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 779,892 股

📆 12-04 Forward Structure
存量OI: C 23.5k / P 59.6k，今日变化ΔOI: C +2.9k / P +9.8k，平值价格ATM: C $7.00 / P $6.33 ｜ ATM IV 96.6%，净 delta 敞口 119k shares
Top ΔOI: P 85 +1,573 ｜ P 92 +1,571 ｜ C 98 +1,389
仓位参考: Max Pain 120 ｜ Put Wall 85（-1.3%）（OI 7.0k）
量化解读： 存量 Put 重｜ATM IV 96.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 119,430 股

📆 12-11 Forward Structure
存量OI: C 7.8k / P 37.6k，今日变化ΔOI: C +0.7k / P +1.9k，平值价格ATM: C $9.00 / P $7.31 ｜ ATM IV 95.2%，净 delta 敞口 191k shares
Top ΔOI: P 160 -1,105 ｜ P 155 -988 ｜ P 65 +788
仓位参考: Max Pain 135 ｜ Put Wall 80（-7.1%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜ATM IV 95.2%｜历史 Rank 94%（近端代理）｜IV/RV 1.41×（近似）｜净 delta 敞口 正 190,776 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/MSTR_evening.json