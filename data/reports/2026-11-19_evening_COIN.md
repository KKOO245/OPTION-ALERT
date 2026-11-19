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
🟡 **近现价集中开仓**: 11-27 114C ΔOI +3,565（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 114.43 → 收盘 108.87（-4.9%） ｜ 今日高 115.54 ｜ 低 108.80 ｜ 昨收 110.51 → 收盘 108.87（-1.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 3.01 | OI比 0.44 | ATM IV 97.2% | Skew 8.0pp | Term 0.76 | ExpMove ±3.8%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价显著（Skew 8.0pp，Put 明显贵于 Call）｜⚠️ 重点观察：存量 Call 重（OI比 0.44）+ 当日成交偏 Put（P/C量 3.01）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 3.01×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±3.8% ｜ 11-27（8D）±8.7% ｜ 12-04（15D）±5.9% ｜ 12-11（22D）±14.7%
   ⇒ IV–VIX Spread: +68.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -7,633,334 | GEX Change vs 上次快照 -2,191,705 | Flip: Primary Flip: 113.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 304 / LOW 246 / INVALID 476
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 113.52（全链重定价，覆盖 91%）
Put Wall 110（弱结构｜现价低于该位 1.0%）
最近结构参考: Put Wall 110（现价低于该位 1.0%）
量化视角： 负 Gamma（763万，无历史分位）｜负 Gamma 加深（219万）｜现价位于 Flip 下方 4.10%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 110（Put Wall，弱结构） / 130（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 114（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C -3.1k / P -3.4k ｜ Activity HIGH ｜ 1D
11-27  C +12.2k / P +1.6k ｜ Activity HIGH ｜ 8D
12-04  C +0.9k / P +1.2k ｜ Activity HIGH ｜ 15D
12-11  C +0.3k / P +0.6k ｜ Activity HIGH ｜ 22D

📆 11-20 Forward Structure
存量OI: C 135.6k / P 60.3k，今日变化ΔOI: C -3.1k / P -3.4k，平值价格ATM: C $2.24 / P $1.85 ｜ ATM IV 97.2%，净 delta 敞口 598k shares
Top ΔOI: P 140 -2,316
仓位参考: Max Pain 130 ｜ Put Wall 105（-3.6%，弱）（OI 6.5k）
量化解读： 存量 Call 重｜ATM IV 97.2%｜历史 Rank 85%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 597,838 股

📆 11-27 Forward Structure
存量OI: C 24.4k / P 11.5k，今日变化ΔOI: C +12.2k / P +1.6k，平值价格ATM: C $5.20 / P $4.30 ｜ ATM IV 77.8%，净 delta 敞口 290k shares
Top ΔOI: C 114 +3,565 ｜ C 118 +3,521 ｜ C 120 +2,247
仓位参考: Max Pain 115 ｜ Call Wall 118（+8.4%，弱）（OI 3.6k） ｜ Put Wall 100（-8.1%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜ATM IV 77.8%｜历史 Rank 85%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 290,221 股

📆 12-04 Forward Structure
存量OI: C 9.2k / P 12.8k，今日变化ΔOI: C +0.9k / P +1.2k，平值价格ATM: C $0.00 / P $6.43 ｜ ATM IV 73.9%，净 delta 敞口 -5k shares
Top ΔOI: P 100 +613
仓位参考: Max Pain 135 ｜ Put Wall 100（-8.1%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 73.9%｜历史 Rank 85%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 负 5,434 股

📆 12-11 Forward Structure
存量OI: C 3.0k / P 3.4k，今日变化ΔOI: C +0.3k / P +0.6k，平值价格ATM: C $8.11 / P $7.88 ｜ ATM IV 74.7%，净 delta 敞口 -11k shares
Top ΔOI: P 100 +333 ｜ C 110 +95 ｜ P 115 +81
仓位参考: Max Pain 135 ｜ Call Wall 110（+1.0%，弱）（OI 0.1k） ｜ Put Wall 100（-8.1%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 74.7%｜历史 Rank 85%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 负 11,016 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/COIN_evening.json