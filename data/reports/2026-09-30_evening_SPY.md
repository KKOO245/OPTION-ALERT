# 期权晚报 2026-09-30（快照 16:40 ET）

📊 市场环境

SPY $762.63 ｜ QQQ $739.77
VIX 16.34 ↑1.9%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-01 775C ΔOI +5,707（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-06 670P ΔOI +8,174 占该期限总 OI 14.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 766.45 → 收盘 762.63（-0.5%） ｜ 今日高 769.41 ｜ 低 762.18 ｜ 昨收 764.20 → 收盘 762.63（-0.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-05，窗口结束前不做对错判定）

Options: P/C成交量 0.95 | OI比 2.60 | ATM IV 25.6% | Skew 2.6pp | Term 0.53 | ExpMove ±0.6%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.53，近月 IV 高于远月）｜保护溢价中性（Skew 2.6pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.60×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 33% ｜ P/C OI(近端) 90%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 33%）｜近端 Put 显著偏重（P/C OI 分位 90%，历史高位区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-01（1D）±0.6% ｜ 10-02（2D）±0.9% ｜ 10-05（5D）±1.1% ｜ 10-06（6D）±1.3%
   ⇒ IV–VIX Spread: +9.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,020,092,699 | GEX Change vs 上次快照 -1,021,861,957 | Flip: Primary Flip: 768.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 2506 / LOW 452 / INVALID 2178
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 768.90（全链重定价，覆盖 87%）
Put Wall 745（弱结构｜现价高于该位 2.4%） | Call Wall 785（现价低于该位 2.8%）
最近结构参考: Flip 769（现价低于该位 0.8%）
量化视角： 负 Gamma（10.20亿，历史分位 33%，中性区）｜由正转负（10.22亿）｜现价位于 Flip 下方 0.82%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 745（Put Wall，弱结构） / 761（MaxPain，仅结算参考）；上方 785（Call Wall）。
• Gamma 区域：切换参考 769（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-01  C +23.7k / P +24.5k ｜ Activity HIGH ｜ 1D
10-02  C +39.5k / P +24.1k ｜ Activity HIGH ｜ 2D
10-05  C +6.4k / P +11.5k ｜ Activity HIGH ｜ 5D
10-06  C +10.5k / P +16.7k ｜ Activity HIGH ｜ 6D

📆 10-01 Forward Structure
存量OI: C 97.0k / P 105.2k，今日变化ΔOI: C +23.7k / P +24.5k，平值价格ATM: C $2.49 / P $2.05 ｜ ATM IV 14.2%，净 delta 敞口 113k shares
Top ΔOI: C 775 +5,707 ｜ P 765 +4,959 ｜ P 732 +2,600
仓位参考: Max Pain 765 ｜ Call Wall 782（+2.5%）（OI 13.6k） ｜ Put Wall 765（+0.3%，弱）（OI 7.5k）
量化解读： 存量两侧均衡｜ATM IV 14.2%｜历史 Rank 94%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 113,049 股

📆 10-02 Forward Structure
存量OI: C 309.9k / P 486.1k，今日变化ΔOI: C +39.5k / P +24.1k，平值价格ATM: C $3.80 / P $3.00 ｜ ATM IV 14.9%，净 delta 敞口 405k shares
Top ΔOI: C 770 +5,850 ｜ P 755 +5,318 ｜ C 775 +4,099
仓位参考: Max Pain 765 ｜ Call Wall 785（+2.9%）（OI 58.6k） ｜ Put Wall 745（-2.3%，弱）（OI 68.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 14.9%｜历史 Rank 94%（近端代理）｜IV/RV 1.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 405,394 股

📆 10-05 Forward Structure
存量OI: C 38.1k / P 65.2k，今日变化ΔOI: C +6.4k / P +11.5k，平值价格ATM: C $4.73 / P $3.80 ｜ ATM IV 11.8%，净 delta 敞口 -5k shares
Top ΔOI: P 755 +3,981 ｜ P 750 +3,942 ｜ C 770 +844
仓位参考: Max Pain 766 ｜ Call Wall 775（+1.6%，弱）（OI 2.1k） ｜ Put Wall 750（-1.7%，弱）（OI 5.5k）
量化解读： 存量 Put 重｜ATM IV 11.8%｜历史 Rank 94%（近端代理）｜IV/RV 1.20×（近似）｜净 delta 敞口 负 5,043 股

📆 10-06 Forward Structure
存量OI: C 25.7k / P 31.6k，今日变化ΔOI: C +10.5k / P +16.7k，平值价格ATM: C $5.17 / P $4.49 ｜ ATM IV 12.1%，净 delta 敞口 93k shares
Top ΔOI: P 715 +980 ｜ C 782 +866
仓位参考: Max Pain 766 ｜ Call Wall 775（+1.6%）（OI 4.0k）
量化解读： 存量 Put 重｜ATM IV 12.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.24×（近似）｜净 delta 敞口 正 93,066 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=35 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=35）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/SPY_evening.json