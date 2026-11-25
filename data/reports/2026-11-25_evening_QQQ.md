# 期权晚报 2026-11-25（快照 16:40 ET）

📊 市场环境

SPY $716.70 ｜ QQQ $633.93
VIX 28.29 ↑7.3%（5D +15.2%） ｜ Vol Regime: STRESS
CNN 恐惧贪婪 15.2（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-25

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-25 08:30　【高】Personal Spending MoM　预测 0.4 ｜ 实际 0.3 ｜ 前值 0.6　✅ 今日已公布
- 周三 11-25 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.7 ｜ 前值 0.3　✅ 今日已公布
- 周三 11-25 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 3.5 ｜ 实际 4.3 ｜ 前值 1.5　✅ 今日已公布
- 周三 11-25 08:30　【高】耐用品订单 Orders MoM　预测 0.6 ｜ 实际 0.2 ｜ 前值 1.8　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 650C ΔOI +6,870（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 617.10 → 收盘 633.93（+2.7%） ｜ 今日高 634.89 ｜ 低 607.76 ｜ 昨收 638.10 → 收盘 633.93（-0.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-12-02，窗口结束前不做对错判定）

Options: P/C成交量 1.07 | OI比 0.91 | ATM IV 57.9% | Skew 9.2pp | Term 0.59 | ExpMove ±2.1%（近端） | Rank 99%
量化视角： IV 历史高位（Rank 99%，期权偏贵）｜期限结构倒挂（Term 0.59，近月 IV 高于远月）｜保护溢价显著（Skew 9.2pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.07×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 27% ｜ P/C OI(近端) 3%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 27%）｜近端持仓极端 Call 重（P/C OI 分位 3%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-27（2D）±2.1% ｜ 11-30（5D）±3.2% ｜ 12-01（6D）±4.0% ｜ 12-02（7D）±4.3%
   ⇒ IV–VIX Spread: +29.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -363,324,333 | GEX Change vs 上次快照 233,043,523 | Flip: Primary Flip: 650.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 3057 / LOW 603 / INVALID 2086
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 650.93（全链重定价，覆盖 94%）
最近结构参考: Flip 651（现价低于该位 2.6%）
量化视角： 负 Gamma（3.63亿，历史分位 27%，中性区）｜负 Gamma 缓解（+2.33亿）｜现价位于 Flip 下方 2.61%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 638（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 651（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-27  C +24.6k / P +6.7k ｜ Activity MEDIUM △ ｜ 2D
11-30  C +22.9k / P -1.2k ｜ Activity HIGH ｜ 5D
12-01  C +8.5k / P +4.9k ｜ Activity HIGH ｜ 6D
12-02  C +9.9k / P +10.8k ｜ Activity HIGH ｜ 7D

📆 11-27 Forward Structure
存量OI: C 291.5k / P 263.7k，今日变化ΔOI: C +24.6k / P +6.7k，平值价格ATM: C $6.32 / P $6.91 ｜ ATM IV 36.5%，净 delta 敞口 2.8M shares
Top ΔOI: P 690 -9,361 ｜ P 680 -9,316 ｜ C 650 +6,870
仓位参考: Max Pain 644 ｜ Call Wall 650（+2.5%，弱）（OI 11.3k） ｜ Put Wall 640（+1.0%，弱）（OI 14.9k）
量化解读： 存量两侧均衡｜ATM IV 36.5%｜历史 Rank 99%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 正 2,822,472 股

📆 11-30 Forward Structure
存量OI: C 358.8k / P 344.8k，今日变化ΔOI: C +22.9k / P -1.2k，平值价格ATM: C $10.24 / P $10.04 ｜ ATM IV 35.0%，净 delta 敞口 1.9M shares
Top ΔOI: P 575 +7,861 ｜ P 690 -6,681 ｜ C 650 +5,412
仓位参考: Max Pain 660 ｜ Call Wall 650（+2.5%，弱）（OI 19.2k） ｜ Put Wall 650（+2.5%，弱）（OI 19.8k）
量化解读： 存量两侧均衡｜ATM IV 35.0%｜历史 Rank 99%（近端代理）｜IV/RV 0.75×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,908,853 股

📆 12-01 Forward Structure
存量OI: C 29.4k / P 46.0k，今日变化ΔOI: C +8.5k / P +4.9k，平值价格ATM: C $12.64 / P $12.48 ｜ ATM IV 37.4%，净 delta 敞口 43k shares
Top ΔOI: C 684 +1,315 ｜ P 585 +1,276
仓位参考: Max Pain 640 ｜ Call Wall 630（-0.6%，弱）（OI 1.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 37.4%｜历史 Rank 99%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 正 43,211 股

📆 12-02 Forward Structure
存量OI: C 21.3k / P 19.4k，今日变化ΔOI: C +9.9k / P +10.8k，平值价格ATM: C $13.48 / P $13.91 ｜ ATM IV 38.3%，净 delta 敞口 38k shares
Top ΔOI: P 510 +3,296 ｜ P 575 +2,106 ｜ C 660 +1,914
仓位参考: Max Pain 643 ｜ Call Wall 650（+2.5%，弱）（OI 1.3k） ｜ Put Wall 620（-2.2%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 38.3%｜历史 Rank 99%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 正 38,312 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol STRESS（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-25/QQQ_evening.json