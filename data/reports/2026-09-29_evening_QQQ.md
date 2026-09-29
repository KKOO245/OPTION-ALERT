# 期权晚报 2026-09-29（快照 16:40 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $737.93
VIX 16.04 ↓0.2%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-30 736P ΔOI +9,844（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-05 660P ΔOI +11,559 占该期限总 OI 10.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 740.17 → 收盘 737.93（-0.3%） ｜ 今日高 740.58 ｜ 低 735.34 ｜ 昨收 736.53 → 收盘 737.93（+0.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.01 | OI比 1.90 | ATM IV 13.5% | Skew 1.0pp | Term 1.43 | ExpMove ±0.8%（近端） | Rank 21%
量化视角： IV 历史低位（Rank 21%，期权偏便宜）｜期限结构正常偏陡（Term 1.43）｜保护溢价薄（Skew 1.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.90×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 45% ｜ P/C OI(近端) 70%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 45%）｜近端持仓结构中性（P/C OI 分位 70%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-30（1D）±0.8% ｜ 10-01（2D）±1.2% ｜ 10-02（3D）±1.5% ｜ 10-05（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -91,274,337 | GEX Change vs 上次快照 56,326,281 | Flip: Primary Flip: 739.12（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2912 / LOW 484 / INVALID 1868
结构观察区: Primary Flip 739.12（全链重定价，覆盖 94%）
Put Wall 730（弱结构｜现价高于该位 1.1%） | Call Wall 760（现价低于该位 2.9%）
最近结构参考: Flip 739（现价低于该位 0.2%）
量化视角： 负 Gamma（9127万，历史分位 45%，中性区）｜负 Gamma 缓解（+5633万）｜现价位于 Flip 下方 0.16%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 730（Put Wall，弱结构） / 736（MaxPain，仅结算参考）；上方 760（Call Wall）。
• Gamma 区域：切换参考 739（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-30  C +17.0k / P +42.7k ｜ Activity HIGH ｜ 1D
10-01  C +10.2k / P +12.5k ｜ Activity HIGH ｜ 2D
10-02  C +28.6k / P +58.6k ｜ Activity HIGH ｜ 3D
10-05  C +7.5k / P +58.9k ｜ Activity HIGH ｜ 6D

📆 09-30 Forward Structure
存量OI: C 330.4k / P 588.3k，今日变化ΔOI: C +17.0k / P +42.7k，平值价格ATM: C $3.35 / P $2.95 ｜ ATM IV 20.2%，净 delta 敞口 -604k shares
Top ΔOI: P 736 +9,844
仓位参考: Max Pain 726 ｜ Call Wall 726（-1.6%）（OI 35.6k） ｜ Put Wall 730（-1.1%，弱）（OI 46.5k）
量化解读： 存量 Put 重｜ATM IV 20.2%｜历史 Rank 21%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 603,831 股

📆 10-01 Forward Structure
存量OI: C 48.5k / P 64.4k，今日变化ΔOI: C +10.2k / P +12.5k，平值价格ATM: C $4.84 / P $4.27 ｜ ATM IV 20.6%，净 delta 敞口 102k shares
Top ΔOI: C 747 +1,297 ｜ C 755 +1,164 ｜ C 736 +1,100
仓位参考: Max Pain 739 ｜ Call Wall 740（+0.3%）（OI 6.2k） ｜ Put Wall 740（+0.3%，弱）（OI 4.7k）
量化解读： 存量 Put 重｜ATM IV 20.6%｜历史 Rank 21%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 101,635 股

📆 10-02 Forward Structure
存量OI: C 226.1k / P 442.3k，今日变化ΔOI: C +28.6k / P +58.6k，平值价格ATM: C $6.02 / P $5.23 ｜ ATM IV 20.8%，净 delta 敞口 433k shares
Top ΔOI: P 650 +18,527 ｜ P 705 +4,177 ｜ C 750 +4,144
仓位参考: Max Pain 730 ｜ Call Wall 725（-1.8%）（OI 34.3k） ｜ Put Wall 730（-1.1%，弱）（OI 51.2k）
量化解读： 存量 Put 重｜ATM IV 20.8%｜历史 Rank 21%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 433,186 股

📆 10-05 Forward Structure
存量OI: C 25.7k / P 83.1k，今日变化ΔOI: C +7.5k / P +58.9k，平值价格ATM: C $7.03 / P $6.28 ｜ ATM IV 17.3%，净 delta 敞口 -29k shares
Top ΔOI: P 660 +11,559
仓位参考: Max Pain 739 ｜ Call Wall 755（+2.3%）（OI 8.2k）
量化解读： 存量 Put 重｜ATM IV 17.3%｜历史 Rank 21%（近端代理）｜IV/RV 1.17×（近似）｜净 delta 敞口 负 28,668 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/QQQ_evening.json