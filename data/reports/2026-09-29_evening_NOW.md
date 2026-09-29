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
🟡 **近现价集中开仓**: 10-02 125P ΔOI +2,567（距现价 -3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 130.83 → 收盘 129.94（-0.7%） ｜ 今日高 132.44 ｜ 低 128.12 ｜ 昨收 131.45 → 收盘 129.94（-1.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-02，窗口结束前不做对错判定）

Options: P/C成交量 0.58 | OI比 0.89 | ATM IV 59.1% | Skew 0.1pp | Term 1.00 | ExpMove ±4.3%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构正常（Term 1.00）｜保护溢价薄（Skew 0.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（3D）±4.3% ｜ 10-09（10D）±7.0% ｜ 10-16（17D）±8.9% ｜ 10-23（24D）±10.8%
   ⇒ IV–VIX Spread: +43.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,425,426 | GEX Change vs 上次快照 -1,959,059 | Flip: Primary Flip: 131.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 554 / LOW 29 / INVALID 113
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 131.91（全链重定价，覆盖 100%）
Put Wall 125（弱结构｜现价高于该位 4.0%）
最近结构参考: Flip 132（现价低于该位 1.5%）
量化视角： 负 Gamma（443万，无历史分位）｜负 Gamma 加深（196万）｜现价位于 Flip 下方 1.49%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 125（Put Wall，弱结构）；上方 134（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 132（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +2.8k / P +5.0k ｜ Activity HIGH ｜ 3D
10-09  C +3.1k / P +1.9k ｜ Activity HIGH ｜ 10D
10-16  C +0.2k / P +1.9k ｜ Activity HIGH ｜ 17D
10-23  C +0.3k / P +3.2k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 27.4k / P 24.3k，今日变化ΔOI: C +2.8k / P +5.0k，平值价格ATM: C $2.87 / P $2.73 ｜ ATM IV 59.1%，净 delta 敞口 5k shares
Top ΔOI: P 125 +2,567 ｜ C 135 +872 ｜ P 121 +786
仓位参考: Max Pain 134 ｜ Call Wall 140（+7.7%，弱）（OI 2.7k） ｜ Put Wall 125（-3.8%）（OI 3.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 59.1%｜历史 Rank 46%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,015 股

📆 10-09 Forward Structure
存量OI: C 14.3k / P 10.3k，今日变化ΔOI: C +3.1k / P +1.9k，平值价格ATM: C $4.59 / P $4.50 ｜ ATM IV 52.1%，净 delta 敞口 1k shares
Top ΔOI: C 150 +2,287 ｜ P 117 +472
仓位参考: Max Pain 135 ｜ Put Wall 120（-7.6%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 52.1%｜历史 Rank 46%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 1,382 股

📆 10-16 Forward Structure
存量OI: C 74.6k / P 62.1k，今日变化ΔOI: C +0.2k / P +1.9k，平值价格ATM: C $5.90 / P $5.66 ｜ ATM IV 51.3%，净 delta 敞口 -17k shares
Top ΔOI: P 125 +1,731
仓位参考: Max Pain 130 ｜ Call Wall 140（+7.7%，弱）（OI 4.6k） ｜ Put Wall 120（-7.6%，弱）（OI 5.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 51.3%｜历史 Rank 46%（近端代理）｜IV/RV 1.27×（近似）｜净 delta 敞口 负 17,106 股

📆 10-23 Forward Structure
存量OI: C 7.7k / P 12.7k，今日变化ΔOI: C +0.3k / P +3.2k，平值价格ATM: C $7.33 / P $6.77 ｜ ATM IV 52.3%，净 delta 敞口 -78k shares
Top ΔOI: P 125 +1,385 ｜ P 120 +573 ｜ P 122 +395
仓位参考: Max Pain 134 ｜ Call Wall 140（+7.7%，弱）（OI 1.0k） ｜ Put Wall 122（-6.1%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 52.3%｜历史 Rank 46%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 负 77,986 股

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 59.1% vs 10-09 52.1%（差 +7.0pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=35 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=35）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/NOW_evening.json