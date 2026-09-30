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
🟡 **近现价集中开仓**: 10-02 192C ΔOI +2,367（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 187.93 → 收盘 187.05（-0.5%） ｜ 今日高 190.99 ｜ 低 187.00 ｜ 昨收 186.97 → 收盘 187.05（+0.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.41 | OI比 0.62 | ATM IV 49.0% | Skew 2.3pp | Term 0.91 | ExpMove ±2.9%（近端） | Rank 26%
量化视角： IV 中性（Rank 26%）｜期限结构正常（Term 0.91）｜保护溢价中性（Skew 2.3pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±2.9% ｜ 10-09（9D）±5.5% ｜ 10-16（16D）±7.3% ｜ 10-23（23D）±8.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 38,670,416 | GEX Change vs 上次快照 -22,641,775 | Flip: Primary Flip: 181.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 572 / LOW 118 / INVALID 146
结构观察区: Primary Flip 181.15（全链重定价，覆盖 100%）
Put Wall 170（弱结构｜现价高于该位 10.0%） | Call Wall 200（现价低于该位 6.5%）
最近结构参考: Flip 181（现价高于该位 3.3%）
量化视角： 正 Gamma（3867万，无历史分位）｜正 Gamma 减弱（2264万）｜现价位于 Flip 上方 3.26%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 185（MaxPain，仅结算参考）；上方 200（Call Wall）。
• Gamma 区域：切换参考 181（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +3.7k / P +2.6k ｜ Activity MEDIUM △ ｜ 2D
10-09  C +2.1k / P +2.6k ｜ Activity HIGH ｜ 9D
10-16  C -1.4k / P +77 ｜ Activity MEDIUM △ ｜ 16D
10-23  C +0.7k / P +1.4k ｜ Activity HIGH ｜ 23D

📆 10-02 Forward Structure
存量OI: C 132.3k / P 81.8k，今日变化ΔOI: C +3.7k / P +2.6k，平值价格ATM: C $2.57 / P $2.83 ｜ ATM IV 49.0%，净 delta 敞口 -28k shares
Top ΔOI: C 192 +2,367 ｜ P 185 +1,386 ｜ P 177 -1,308
仓位参考: Max Pain 185 ｜ Call Wall 200（+6.9%）（OI 25.9k） ｜ Put Wall 177.5（-5.1%，弱）（OI 7.4k）
量化解读： 存量 Call 重｜ATM IV 49.0%｜历史 Rank 26%（近端代理）｜IV/RV 1.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 28,015 股

📆 10-09 Forward Structure
存量OI: C 30.8k / P 42.8k，今日变化ΔOI: C +2.1k / P +2.6k，平值价格ATM: C $5.10 / P $5.15 ｜ ATM IV 44.0%，净 delta 敞口 41k shares
Top ΔOI: P 165 +1,911 ｜ C 200 +885
仓位参考: Max Pain 185 ｜ Call Wall 200（+6.9%，弱）（OI 4.6k） ｜ Put Wall 190（+1.6%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 44.0%｜历史 Rank 26%（近端代理）｜IV/RV 1.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 40,583 股

10-16（MEDIUM △）Top ΔOI: 210C -1,168 ｜ 200C +595
10-16（MEDIUM △）仓位参考: Max Pain 165 ｜ Call Wall 200（+6.9%，弱）（OI 15.0k） ｜ Put Wall 170（-9.1%，弱）（OI 14.8k）

📆 10-23 Forward Structure
存量OI: C 20.4k / P 13.6k，今日变化ΔOI: C +0.7k / P +1.4k，平值价格ATM: C $8.31 / P $8.01 ｜ ATM IV 43.9%，净 delta 敞口 2k shares
仓位参考: Max Pain 180 ｜ Call Wall 180（-3.8%）（OI 4.6k） ｜ Put Wall 175（-6.4%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 43.9%｜历史 Rank 26%（近端代理）｜IV/RV 1.68×（近似）｜净 delta 敞口 正 1,976 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/PLTR_evening.json