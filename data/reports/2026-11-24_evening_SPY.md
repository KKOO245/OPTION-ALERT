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
🟡 **近现价集中开仓**: 11-25 735C ΔOI +4,596（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 715.15 → 收盘 718.78（+0.5%） ｜ 今日高 720.92 ｜ 低 712.14 ｜ 昨收 722.29 → 收盘 718.78（-0.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-01，窗口结束前不做对错判定）

Options: P/C成交量 1.25 | OI比 1.08 | ATM IV 30.5% | Skew 2.7pp | Term 0.71 | ExpMove ±1.1%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜保护溢价中性（Skew 2.7pp）｜当日成交偏 Put（P/C量 1.25）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.25×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.08×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 36% ｜ P/C OI(近端) 3%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 36%）｜近端持仓极端 Call 重（P/C OI 分位 3%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-25（1D）±1.1% ｜ 11-27（3D）±1.6% ｜ 11-30（6D）±2.1% ｜ 12-01（7D）±2.4%
   ⇒ IV–VIX Spread: +4.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -858,427,177 | GEX Change vs 上次快照 -96,030,432 | Flip: Primary Flip: 733.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 3069 / LOW 569 / INVALID 2096
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 733.16（全链重定价，覆盖 93%）
最近结构参考: Flip 733（现价低于该位 2.0%）
量化视角： 负 Gamma（8.58亿，历史分位 36%，中性区）｜负 Gamma 加深（9603万）｜现价位于 Flip 下方 1.96%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 722（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 733（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-25  C +23.7k / P +28.6k ｜ Activity HIGH ｜ 1D
11-27  C +0.3k / P -53.1k ｜ Activity HIGH ｜ 3D
11-30  C +7.7k / P -7.6k ｜ Activity MEDIUM △ ｜ 6D
12-01  C +4.1k / P +8.8k ｜ Activity HIGH ｜ 7D

📆 11-25 Forward Structure
存量OI: C 170.2k / P 112.9k，今日变化ΔOI: C +23.7k / P +28.6k，平值价格ATM: C $3.52 / P $4.64 ｜ ATM IV 27.1%，净 delta 敞口 -1.2M shares
Top ΔOI: C 735 +4,596 ｜ C 740 +4,358 ｜ C 739 +3,885
仓位参考: Max Pain 717 ｜ Call Wall 730（+1.6%，弱）（OI 10.0k） ｜ Put Wall 734（+2.1%）（OI 12.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 27.1%｜历史 Rank 96%（近端代理）｜IV/RV 0.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,204,575 股

📆 11-27 Forward Structure
存量OI: C 412.5k / P 355.8k，今日变化ΔOI: C +0.3k / P -53.1k，平值价格ATM: C $5.15 / P $6.13 ｜ ATM IV 22.2%，净 delta 敞口 -1.7M shares
Top ΔOI: P 660 -49,651 ｜ P 680 -49,523 ｜ C 730 -12,450
仓位参考: Max Pain 725 ｜ Call Wall 730（+1.6%，弱）（OI 13.9k） ｜ Put Wall 700（-2.6%，弱）（OI 34.1k）
量化解读： 存量两侧均衡｜ATM IV 22.2%｜历史 Rank 96%（近端代理）｜IV/RV 0.71×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,714,096 股

11-30（MEDIUM △）Top ΔOI: 570P -27,877 ｜ 675P -22,457
11-30（MEDIUM △）仓位参考: Max Pain 735 ｜ Call Wall 740（+3.0%，弱）（OI 6.8k） ｜ Put Wall 700（-2.6%，弱）（OI 29.2k）

📆 12-01 Forward Structure
存量OI: C 52.5k / P 29.2k，今日变化ΔOI: C +4.1k / P +8.8k，平值价格ATM: C $8.43 / P $8.59 ｜ ATM IV 21.4%，净 delta 敞口 -196k shares
Top ΔOI: P 703 +3,929 ｜ C 760 +605
仓位参考: Max Pain 722 ｜ Call Wall 740（+3.0%，弱）（OI 0.9k） ｜ Put Wall 703（-2.2%）（OI 4.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 21.4%｜历史 Rank 96%（近端代理）｜IV/RV 0.69×（近似）｜净 delta 敞口 负 196,303 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-24/SPY_evening.json