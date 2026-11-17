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
🟡 **近现价集中开仓**: 11-18 718P ΔOI +15,185（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 738.39 → 收盘 732.44（-0.8%） ｜ 今日高 739.76 ｜ 低 727.00 ｜ 昨收 739.95 → 收盘 732.44（-1.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-20，窗口结束前不做对错判定）

Options: P/C成交量 1.40 | OI比 1.10 | ATM IV 85.4% | Skew -0.5pp | Term 0.24 | ExpMove ±1.3%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.24，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.40）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.40×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.10×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 19% ｜ P/C OI(近端) 4%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 19%）｜近端持仓极端 Call 重（P/C OI 分位 4%，历史极低区）｜⚠️ 需重点观察：持仓极端 + Gamma 异常侧组合——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-18（1D）±1.3% ｜ 11-19（2D）±1.7% ｜ 11-20（3D）±2.1% ｜ 11-23（6D）±2.4%
   ⇒ IV–VIX Spread: +60.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,777,554,539 | GEX Change vs 上次快照 -136,375,176 | Flip: Primary Flip: 754.35（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 2908 / LOW 374 / INVALID 1484
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 754.35（全链重定价，覆盖 93%）
最近结构参考: Flip 754（现价低于该位 2.9%）
量化视角： 负 Gamma（17.78亿，历史分位偏负区，比 81% 的交易日更负）｜负 Gamma 加深（1.36亿）｜现价位于 Flip 下方 2.90%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 744（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 754（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-18  C +33.1k / P +38.3k ｜ Activity HIGH ｜ 1D
11-19  C +20.7k / P +18.0k ｜ Activity HIGH ｜ 2D
11-20  C +51.5k / P +26.4k ｜ Activity HIGH ｜ 3D
11-23  C +25.1k / P +20.4k ｜ Activity HIGH ｜ 6D

📆 11-18 Forward Structure
存量OI: C 111.8k / P 133.7k，今日变化ΔOI: C +33.1k / P +38.3k，平值价格ATM: C $4.79 / P $4.48 ｜ ATM IV 30.0%，净 delta 敞口 -434k shares
Top ΔOI: P 718 +15,185 ｜ P 731 -6,533 ｜ P 730 +5,065
仓位参考: Max Pain 748 ｜ Call Wall 750（+2.4%，弱）（OI 3.7k） ｜ Put Wall 718（-2.0%，弱）（OI 15.5k）
量化解读： 存量 Put 重｜ATM IV 30.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.33×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 434,091 股

📆 11-19 Forward Structure
存量OI: C 59.5k / P 86.1k，今日变化ΔOI: C +20.7k / P +18.0k，平值价格ATM: C $6.52 / P $6.07 ｜ ATM IV 29.1%，净 delta 敞口 -205k shares
Top ΔOI: C 764 +1,801 ｜ C 750 +1,402 ｜ P 665 +1,372
仓位参考: Max Pain 750 ｜ Call Wall 750（+2.4%，弱）（OI 2.5k） ｜ Put Wall 750（+2.4%，弱）（OI 2.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 29.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 205,236 股

📆 11-20 Forward Structure
存量OI: C 906.4k / P 2963.6k，今日变化ΔOI: C +51.5k / P +26.4k，平值价格ATM: C $7.88 / P $7.23 ｜ ATM IV 28.3%，净 delta 敞口 939k shares
Top ΔOI: P 770 -9,183 ｜ P 740 +7,474 ｜ P 710 +7,052
仓位参考: Max Pain 755 ｜ Put Wall 725（-1.0%，弱）（OI 71.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 28.3%｜历史 Rank 100%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 938,992 股

📆 11-23 Forward Structure
存量OI: C 45.9k / P 47.6k，今日变化ΔOI: C +25.1k / P +20.4k，平值价格ATM: C $9.19 / P $8.34 ｜ ATM IV 23.3%，净 delta 敞口 -457k shares
Top ΔOI: P 736 +2,807 ｜ P 728 +2,551 ｜ P 719 +2,496
仓位参考: Max Pain 750 ｜ Call Wall 752（+2.7%，弱）（OI 1.7k） ｜ Put Wall 736（+0.5%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 23.3%｜历史 Rank 100%（近端代理）｜IV/RV 1.03×（近似）｜净 delta 敞口 负 457,264 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=98 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=98）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/SPY_evening.json