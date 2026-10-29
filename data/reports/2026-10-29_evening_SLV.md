# 期权晚报 2026-10-29（快照 16:40 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 17.20 ↑1.7%（5D -9.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 10-30 ATM IV 47.0% vs 11-02 33.5%（差 +13.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 49C ΔOI +2,364（距现价 +3.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-02 50C ΔOI +1,546 占该期限总 OI 10.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 47.23 → 收盘 47.28（+0.1%） ｜ 今日高 47.63 ｜ 低 46.92 ｜ 昨收 49.06 → 收盘 47.28（-3.6%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-11-03，窗口结束前不做对错判定）

Options: P/C成交量 0.90 | OI比 0.39 | ATM IV 47.0% | Skew 6.2pp | Term 0.83 | ExpMove ±2.2%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价显著（Skew 6.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.2% ｜ 11-02（4D）±3.0% ｜ 11-04（6D）±4.3% ｜ 11-06（8D）±5.0%
   ⇒ IV–VIX Spread: +29.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -16,602,341 | GEX Change vs 上次快照 4,158,549 | Flip: Primary Flip: 47.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 679 / LOW 125 / INVALID 288
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 47.91（全链重定价，覆盖 95%）
Put Wall 50（弱结构｜现价低于该位 5.4%）
最近结构参考: Flip 48（现价低于该位 1.3%）
量化视角： 负 Gamma（1660万，无历史分位）｜负 Gamma 缓解（+416万）｜现价位于 Flip 下方 1.30%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +10.2k / P +1.4k ｜ Activity HIGH ｜ 1D
11-02  C +3.8k / P +1.9k ｜ Activity HIGH ｜ 4D
11-04  C +1.9k / P +1.7k ｜ Activity HIGH ｜ 6D
11-06  C +4.6k / P -0.3k ｜ Activity HIGH ｜ 8D

📆 10-30 Forward Structure
存量OI: C 101.6k / P 39.5k，今日变化ΔOI: C +10.2k / P +1.4k，平值价格ATM: C $0.38 / P $0.65 ｜ ATM IV 47.0%，净 delta 敞口 148k shares
Top ΔOI: C 49 +2,364 ｜ C 49 +2,044 ｜ C 48 +1,348
仓位参考: Max Pain 50 ｜ Call Wall 50（+5.8%，弱）（OI 5.7k） ｜ Put Wall 45（-4.8%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 47.0%｜历史 Rank 79%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 148,426 股

📆 11-02 Forward Structure
存量OI: C 7.9k / P 7.6k，今日变化ΔOI: C +3.8k / P +1.9k，平值价格ATM: C $0.59 / P $0.85 ｜ ATM IV 33.5%，净 delta 敞口 -35k shares
Top ΔOI: C 50 +1,546 ｜ C 49 +753 ｜ P 48 +508
仓位参考: Max Pain 49 ｜ Call Wall 50（+5.8%）（OI 2.2k） ｜ Put Wall 47.5（+0.5%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 33.5%｜历史 Rank 79%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 34,828 股

📆 11-04 Forward Structure
存量OI: C 12.3k / P 5.9k，今日变化ΔOI: C +1.9k / P +1.7k，平值价格ATM: C $0.81 / P $1.21 ｜ ATM IV 39.9%，净 delta 敞口 -33k shares
Top ΔOI: P 44 +502
仓位参考: Max Pain 48 ｜ Call Wall 51.5（+8.9%，弱）（OI 3.1k） ｜ Put Wall 44（-6.9%）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 39.9%｜历史 Rank 79%（近端代理）｜IV/RV 1.09×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 33,058 股

📆 11-06 Forward Structure
存量OI: C 109.7k / P 29.6k，今日变化ΔOI: C +4.6k / P -0.3k，平值价格ATM: C $1.07 / P $1.30 ｜ ATM IV 42.1%，净 delta 敞口 115k shares
Top ΔOI: C 50 +2,908 ｜ C 49 +524
仓位参考: Max Pain 51 ｜ Put Wall 43（-9.1%，弱）（OI 3.0k）
量化解读： 存量 Call 重｜ATM IV 42.1%｜历史 Rank 79%（近端代理）｜IV/RV 1.15×（近似）｜净 delta 敞口 正 114,557 股

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 47.0% vs 11-02 33.5%（差 +13.5pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/SLV_evening.json