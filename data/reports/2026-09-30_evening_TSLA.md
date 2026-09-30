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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-02 ATM IV 50.1% vs 10-05 38.5%（差 +11.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-02 365C ΔOI +4,159（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 351.79 → 收盘 354.81（+0.9%） ｜ 今日高 355.22 ｜ 低 345.88 ｜ 昨收 352.84 → 收盘 354.81（+0.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.85 | OI比 0.55 | ATM IV 24.2% | Skew 2.1pp | Term 1.89 | ExpMove ±3.0%（近端） | Rank 50%
量化视角： IV 中性（Rank 50%）｜期限结构正常偏陡（Term 1.89）｜保护溢价中性（Skew 2.1pp）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.85×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-02（2D）±3.0% ｜ 10-05（5D）±3.6% ｜ 10-07（7D）±4.4% ｜ 10-09（9D）±5.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 57,453,780 | GEX Change vs 上次快照 68,172,087 | Flip: Primary Flip: 346.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 1106 / LOW 161 / INVALID 709
结构观察区: Primary Flip 346.81（全链重定价，覆盖 90%）
最近结构参考: Flip 347（现价高于该位 2.3%）
量化视角： 正 Gamma（5745万，无历史分位）｜由负转正（+6817万）｜现价位于 Flip 上方 2.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 355（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 347（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +31.6k / P +11.9k ｜ Activity HIGH ｜ 2D
10-05  C +6.5k / P +1.4k ｜ Activity HIGH ｜ 5D
10-07  C +2.8k / P +1.2k ｜ Activity HIGH ｜ 7D
10-09  C +6.2k / P +6.1k ｜ Activity HIGH ｜ 9D

📆 10-02 Forward Structure
存量OI: C 246.5k / P 254.1k，今日变化ΔOI: C +31.6k / P +11.9k，平值价格ATM: C $5.25 / P $5.40 ｜ ATM IV 50.1%，净 delta 敞口 349k shares
Top ΔOI: C 365 +4,159 ｜ C 370 +2,946
仓位参考: Max Pain 360 ｜ Call Wall 390（+9.9%，弱）（OI 16.6k） ｜ Put Wall 350（-1.4%，弱）（OI 7.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 50.1%｜历史 Rank 50%（近端代理）｜IV/RV 1.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 349,367 股

📆 10-05 Forward Structure
存量OI: C 35.1k / P 15.9k，今日变化ΔOI: C +6.5k / P +1.4k，平值价格ATM: C $6.40 / P $6.49 ｜ ATM IV 38.5%，净 delta 敞口 102k shares
Top ΔOI: C 420 +5,866 ｜ C 390 -3,941 ｜ C 375 +677
仓位参考: Max Pain 360 ｜ Call Wall 390（+9.9%，弱）（OI 6.4k） ｜ Put Wall 325（-8.4%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 38.5%｜历史 Rank 50%（近端代理）｜IV/RV 1.41×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 101,661 股

📆 10-07 Forward Structure
存量OI: C 9.1k / P 3.2k，今日变化ΔOI: C +2.8k / P +1.2k，平值价格ATM: C $7.79 / P $7.75 ｜ ATM IV 40.1%，净 delta 敞口 40k shares
Top ΔOI: C 355 +389 ｜ C 365 +288 ｜ C 380 +250
仓位参考: Max Pain 360 ｜ Call Wall 375（+5.7%，弱）（OI 1.1k） ｜ Put Wall 360（+1.5%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 40.1%｜历史 Rank 50%（近端代理）｜IV/RV 1.46×（近似）｜净 delta 敞口 正 39,672 股

📆 10-09 Forward Structure
存量OI: C 59.7k / P 46.2k，今日变化ΔOI: C +6.2k / P +6.1k，平值价格ATM: C $9.23 / P $8.95 ｜ ATM IV 40.8%，净 delta 敞口 125k shares
仓位参考: Max Pain 360 ｜ Call Wall 370（+4.3%，弱）（OI 3.7k） ｜ Put Wall 350（-1.4%，弱）（OI 1.8k）
量化解读： 存量 Call 重｜ATM IV 40.8%｜历史 Rank 50%（近端代理）｜IV/RV 1.49×（近似）｜净 delta 敞口 正 124,515 股

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 50.1% vs 10-05 38.5%（差 +11.6pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/TSLA_evening.json