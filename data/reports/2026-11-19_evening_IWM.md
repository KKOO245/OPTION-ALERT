# 期权晚报 2026-11-19（快照 16:40 ET）

📊 市场环境

SPY $715.87 ｜ QQQ $nan
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
🟡 **近现价集中开仓**: 11-20 263P ΔOI +15,988（距现价 -0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 271.08 → 收盘 264.22（-2.5%） ｜ 今日高 271.80 ｜ 低 263.81 ｜ 昨收 270.12 → 收盘 264.22（-2.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 1.44 | OI比 1.86 | ATM IV 45.2% | Skew -5.8pp | Term 0.56 | ExpMove ±1.5%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.8pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.44）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.44×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.86×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±1.5% ｜ 11-23（4D）±2.1% ｜ 11-24（5D）±2.5% ｜ 11-25（6D）±2.9%
   ⇒ IV–VIX Spread: +16.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,344,487,376 | GEX Change vs 上次快照 -212,207,289 | Flip: Primary Flip: 278.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 1104 / LOW 279 / INVALID 1233
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 278.96（全链重定价，覆盖 91%）
Put Wall 265（弱结构｜现价低于该位 0.3%）
最近结构参考: Put Wall 265（现价低于该位 0.3%）
量化视角： 负 Gamma（23.44亿，无历史分位）｜负 Gamma 加深（2.12亿）｜现价位于 Flip 下方 5.28%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 265（Put Wall，弱结构） / 272（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 279（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +20.3k / P -33.6k ｜ Activity HIGH ｜ 1D
11-23  C +7.0k / P +2.2k ｜ Activity HIGH ｜ 4D
11-24  C +2.5k / P +2.4k ｜ Activity HIGH ｜ 5D
11-25  C +3.6k / P +9.2k ｜ Activity HIGH ｜ 6D

📆 11-20 Forward Structure
存量OI: C 605.8k / P 1402.9k，今日变化ΔOI: C +20.3k / P -33.6k，平值价格ATM: C $2.12 / P $1.94 ｜ ATM IV 36.6%，净 delta 敞口 3.0M shares
Top ΔOI: P 263 +15,988 ｜ C 277 +10,746 ｜ P 270 -10,029
仓位参考: Max Pain 276 ｜ Call Wall 285（+7.9%，弱）（OI 50.6k） ｜ Put Wall 265（+0.3%，弱）（OI 127.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 36.6%｜历史 Rank 96%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 3,046,225 股

📆 11-23 Forward Structure
存量OI: C 23.5k / P 28.1k，今日变化ΔOI: C +7.0k / P +2.2k，平值价格ATM: C $2.91 / P $2.70 ｜ ATM IV 25.6%，净 delta 敞口 -45k shares
Top ΔOI: C 281 +2,550 ｜ C 270 +2,095 ｜ P 265 +1,212
仓位参考: Max Pain 271 ｜ Call Wall 281（+6.4%，弱）（OI 3.5k） ｜ Put Wall 270（+2.2%）（OI 12.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 25.6%｜历史 Rank 96%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 45,495 股

📆 11-24 Forward Structure
存量OI: C 8.9k / P 14.0k，今日变化ΔOI: C +2.5k / P +2.4k，平值价格ATM: C $3.47 / P $3.25 ｜ ATM IV 26.8%，净 delta 敞口 -70k shares
Top ΔOI: P 255 +1,258 ｜ P 265 +718 ｜ C 274 +582
仓位参考: Max Pain 274 ｜ Call Wall 275（+4.1%，弱）（OI 1.3k） ｜ Put Wall 270（+2.2%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 26.8%｜历史 Rank 96%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 69,542 股

📆 11-25 Forward Structure
存量OI: C 12.4k / P 15.1k，今日变化ΔOI: C +3.6k / P +9.2k，平值价格ATM: C $3.85 / P $3.73 ｜ ATM IV 27.3%，净 delta 敞口 -353k shares
Top ΔOI: P 255 +2,162 ｜ P 265 +1,920 ｜ C 272 +1,080
仓位参考: Max Pain 272 ｜ Call Wall 277（+4.8%，弱）（OI 4.2k） ｜ Put Wall 255（-3.5%，弱）（OI 2.3k）
量化解读： 存量 Put 重｜ATM IV 27.3%｜历史 Rank 96%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 负 352,719 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/IWM_evening.json