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
🟡 **近现价集中开仓**: 11-27 135P ΔOI -192（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 146.28 → 收盘 137.95（-5.7%） ｜ 今日高 148.59 ｜ 低 137.66 ｜ 昨收 141.85 → 收盘 137.95（-2.7%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-24，窗口结束前不做对错判定）

Options: P/C成交量 2.18 | OI比 1.68 | ATM IV 109.8% | Skew 28.5pp | Term 0.56 | ExpMove ±4.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.56，近月 IV 高于远月）｜保护溢价显著（Skew 28.5pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.18）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.18×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.68×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±4.2% ｜ 11-27（8D）±3.7% ｜ 12-04（15D）±8.1% ｜ 12-11（22D）±5.8%
   ⇒ IV–VIX Spread: +81.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -59,744,296 | GEX Change vs 上次快照 -18,387,627 | Flip: Primary Flip: 147.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 85%（带内） ｜ IV 有效性: VALID 547 / LOW 396 / INVALID 683
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 147.86（全链重定价，覆盖 85%）
最近结构参考: Flip 148（现价低于该位 6.7%）
量化视角： 负 Gamma（5974万，无历史分位）｜负 Gamma 加深（1839万）｜现价位于 Flip 下方 6.70%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 85%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C -0.3k / P -17.4k ｜ Activity HIGH ｜ 1D
11-27  C +0.4k / P -1.2k ｜ Activity HIGH ｜ 8D
12-04  C -1.2k / P -0.1k ｜ Activity MEDIUM △ ｜ 15D
12-11  C +0.1k / P +75 ｜ Activity MEDIUM △ ｜ 22D

📆 11-20 Forward Structure
存量OI: C 201.6k / P 339.2k，今日变化ΔOI: C -0.3k / P -17.4k，平值价格ATM: C $3.35 / P $2.42 ｜ ATM IV 109.8%，净 delta 敞口 1.4M shares
Top ΔOI: P 166 -3,307 ｜ P 171 -2,448
仓位参考: Max Pain 155 ｜ Call Wall 145（+5.1%，弱）（OI 6.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 109.8%｜历史 Rank 100%（近端代理）｜IV/RV 0.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,402,831 股

📆 11-27 Forward Structure
存量OI: C 41.7k / P 30.1k，今日变化ΔOI: C +0.4k / P -1.2k，平值价格ATM: C $0.00 / P $5.10 ｜ ATM IV 77.9%，净 delta 敞口 123k shares
Top ΔOI: P 163 -203 ｜ P 135 -192
仓位参考: Max Pain 160 ｜ Put Wall 146.67（+6.3%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 77.9%｜历史 Rank 100%（近端代理）｜IV/RV 0.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 122,795 股

12-04（MEDIUM △）Top ΔOI: 140P -151
12-04（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 145（+5.1%，弱）（OI 1.2k） ｜ Put Wall 140（+1.5%，弱）（OI 5.1k）

12-11（MEDIUM △）Top ΔOI: 150C +88 ｜ 125P +51
12-11（MEDIUM △）仓位参考: Max Pain 147 ｜ Call Wall 143.33（+3.9%，弱）（OI 0.1k） ｜ Put Wall 140（+1.5%）（OI 0.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=104 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=104）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/SOXX_evening.json