# 期权晚报 2026-11-17（快照 16:40 ET）

📊 市场环境

SPY $732.44 ｜ QQQ $656.95
VIX 25.46 ↑11.1%（5D +30.8%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **Vol Regime 升档**: ELEVATED → STRESS（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-18 275P ΔOI -1,217（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-23 270P ΔOI +12,177 占该期限总 OI 35.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## IWM

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
IWM: 今开 272.03 → 收盘 269.05（-1.1%） ｜ 今日高 273.04 ｜ 低 267.87 ｜ 昨收 272.94 → 收盘 269.05（-1.4%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-20，窗口结束前不做对错判定）

Options: P/C成交量 1.31 | OI比 1.09 | ATM IV 30.4% | Skew 2.2pp | Term 0.77 | ExpMove ±1.2%（近端） | Rank 67%
量化视角： IV 中性（Rank 67%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价中性（Skew 2.2pp）｜当日成交偏 Put（P/C量 1.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.31×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.09×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-18（1D）±1.2% ｜ 11-19（2D）±1.8% ｜ 11-20（3D）±2.1% ｜ 11-23（6D）±2.6%
   ⇒ IV–VIX Spread: +4.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,825,296,208 | GEX Change vs 上次快照 -215,186,029 | Flip: Primary Flip: 281.98（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 1136 / LOW 270 / INVALID 1142
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 281.98（全链重定价，覆盖 93%）
Put Wall 270（弱结构｜现价低于该位 0.4%）
最近结构参考: Put Wall 270（现价低于该位 0.4%）
量化视角： 负 Gamma（18.25亿，无历史分位）｜负 Gamma 加深（2.15亿）｜现价位于 Flip 下方 4.59%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 270（Put Wall，弱结构） / 275（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 282（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-18  C +5.3k / P +2.7k ｜ Activity HIGH ｜ 1D
11-19  C +1.3k / P +2.5k ｜ Activity HIGH ｜ 2D
11-20  C +6.7k / P -37.0k ｜ Activity MEDIUM △ ｜ 3D
11-23  C +7.0k / P +15.5k ｜ Activity HIGH ｜ 6D

📆 11-18 Forward Structure
存量OI: C 21.5k / P 20.7k，今日变化ΔOI: C +5.3k / P +2.7k，平值价格ATM: C $1.71 / P $1.66 ｜ ATM IV 29.6%，净 delta 敞口 -9k shares
Top ΔOI: P 275 -1,217 ｜ P 267 +1,212 ｜ C 275 +1,126
仓位参考: Max Pain 276 ｜ Call Wall 278（+3.3%，弱）（OI 2.2k） ｜ Put Wall 275（+2.2%）（OI 3.2k）
量化解读： 存量两侧均衡｜ATM IV 29.6%｜历史 Rank 67%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,793 股

📆 11-19 Forward Structure
存量OI: C 15.1k / P 27.0k，今日变化ΔOI: C +1.3k / P +2.5k，平值价格ATM: C $2.40 / P $2.46 ｜ ATM IV 29.9%，净 delta 敞口 -94k shares
Top ΔOI: P 270 +553 ｜ P 271 +458 ｜ P 267 +358
仓位参考: Max Pain 278 ｜ Call Wall 287（+6.7%）（OI 3.4k） ｜ Put Wall 272（+1.1%，弱）（OI 3.9k）
量化解读： 存量 Put 重｜ATM IV 29.9%｜历史 Rank 67%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 94,188 股

11-20（MEDIUM △）Top ΔOI: 268P -26,781 ｜ 264P +16,566
11-20（MEDIUM △）仓位参考: Max Pain 279 ｜ Call Wall 285（+5.9%，弱）（OI 51.5k） ｜ Put Wall 265（-1.5%，弱）（OI 138.3k）

📆 11-23 Forward Structure
存量OI: C 12.7k / P 21.7k，今日变化ΔOI: C +7.0k / P +15.5k，平值价格ATM: C $3.63 / P $3.34 ｜ ATM IV 24.9%，净 delta 敞口 -741k shares
Top ΔOI: P 270 +12,177 ｜ C 278 +1,090 ｜ C 282 +1,085
仓位参考: Max Pain 277 ｜ Call Wall 282（+4.8%，弱）（OI 1.5k） ｜ Put Wall 270（+0.4%）（OI 12.4k）
量化解读： 存量 Put 重｜ATM IV 24.9%｜历史 Rank 67%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 负 741,081 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/IWM_evening.json