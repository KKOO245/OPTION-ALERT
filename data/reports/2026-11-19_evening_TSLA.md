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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-25 382P ΔOI +711（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 389.90 → 收盘 374.41（-4.0%） ｜ 今日高 393.60 ｜ 低 370.81 ｜ 昨收 383.72 → 收盘 374.41（-2.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 0.58 | OI比 1.40 | ATM IV 71.1% | Skew 9.0pp | Term 0.42 | ExpMove ±0.3%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.42，近月 IV 高于远月）｜保护溢价显著（Skew 9.0pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.40×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±0.3% ｜ 11-23（4D）±4.4% ｜ 11-25（6D）±5.6% ｜ 11-27（8D）±0.0%
   ⇒ IV–VIX Spread: +42.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,250,994 | GEX Change vs 上次快照 -62,490,671 | Flip: Primary Flip: 374.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1300 / LOW 310 / INVALID 828
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 374.91（全链重定价，覆盖 99%）
Call Wall 400（弱结构｜现价低于该位 6.4%）
最近结构参考: Flip 375（现价低于该位 0.1%）
量化视角： 负 Gamma（225万，无历史分位）｜由正转负（6249万）｜现价位于 Flip 下方 0.13%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 378（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 375（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +12.2k / P +16.4k ｜ Activity MEDIUM △ ｜ 1D
11-23  C +2.3k / P +4.8k ｜ Activity HIGH ｜ 4D
11-25  C +1.2k / P +2.6k ｜ Activity HIGH ｜ 6D
11-27  C +3.4k / P +3.5k ｜ Activity HIGH ｜ 8D

📆 11-20 Forward Structure
存量OI: C 375.5k / P 524.6k，今日变化ΔOI: C +12.2k / P +16.4k，平值价格ATM: C $0.65 / P $0.42 ｜ ATM IV 0.0%，净 delta 敞口 -166k shares
Top ΔOI: C 405 +3,016 ｜ C 400 +2,452
仓位参考: Max Pain 378 ｜ Call Wall 400（+6.8%，弱）（OI 28.8k）
量化解读： 存量 Put 重｜净 delta 敞口 负 166,110 股

📆 11-23 Forward Structure
存量OI: C 26.3k / P 16.8k，今日变化ΔOI: C +2.3k / P +4.8k，平值价格ATM: C $7.92 / P $8.65 ｜ ATM IV 52.1%，净 delta 敞口 -48k shares
Top ΔOI: P 312 +3,002 ｜ C 410 +546
仓位参考: Max Pain 385 ｜ Put Wall 357.5（-4.5%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.1%｜历史 Rank 84%（近端代理）｜IV/RV 0.94×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 47,850 股

📆 11-25 Forward Structure
存量OI: C 5.0k / P 7.3k，今日变化ΔOI: C +1.2k / P +2.6k，平值价格ATM: C $10.05 / P $10.92 ｜ ATM IV 54.8%，净 delta 敞口 -97k shares
Top ΔOI: P 382 +711 ｜ P 385 +563 ｜ P 345 +256
仓位参考: Max Pain 385 ｜ Call Wall 400（+6.8%，弱）（OI 0.6k） ｜ Put Wall 382.5（+2.2%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜ATM IV 54.8%｜历史 Rank 84%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 负 96,943 股

📆 11-27 Forward Structure
存量OI: C 65.4k / P 60.3k，今日变化ΔOI: C +3.4k / P +3.5k，平值价格ATM: C $0.00 / P $0.00 ｜ ATM IV 0.0%，净 delta 敞口 -16k shares
仓位参考: Max Pain 375 ｜ Call Wall 410（+9.5%）（OI 9.4k） ｜ Put Wall 350（-6.5%，弱）（OI 2.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜净 delta 敞口 负 16,194 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/TSLA_evening.json