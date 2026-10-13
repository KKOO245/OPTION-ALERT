# 期权晚报 2026-10-12（快照 21:00 ET）

📊 市场环境

SPY $778.10 ｜ QQQ $746.04
VIX 15.21 ↑2.5%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 45.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.96 ｜ 实际 待公布 ｜ 前值 3.98
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.7 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MP: 今开 45.65 → 收盘 43.36（-5.0%） ｜ 今日高 45.96 ｜ 低 43.17 ｜ 昨收 46.14 → 收盘 43.36（-6.0%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-15，窗口结束前不做对错判定）

Options: P/C成交量 1.29 | OI比 0.91 | ATM IV 58.3% | Skew 1.3pp | Term 1.05 | ExpMove ±4.8%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构正常（Term 1.05）｜保护溢价薄（Skew 1.3pp）｜当日成交偏 Put（P/C量 1.29）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.29×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.91×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（4D）±4.8% ｜ 10-23（11D）±7.4% ｜ 10-30（18D）±9.7% ｜ 11-06（25D）±13.0%
   ⇒ IV–VIX Spread: +43.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,234,127 | GEX Change vs 上次快照 -1,920,704 | Flip: Primary Flip: 47.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 248 / LOW 45 / INVALID 111
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 47.15（全链重定价，覆盖 100%）
Put Wall 45（现价低于该位 3.6%）
最近结构参考: Put Wall 45（现价低于该位 3.6%）
量化视角： 负 Gamma（523万，无历史分位）｜负 Gamma 加深（192万）｜现价位于 Flip 下方 8.04%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 45（Put Wall） / 50（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 47（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 11D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-16 Forward Structure
存量OI: C 21.6k / P 19.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.90 / P $1.17 ｜ ATM IV 58.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 50 ｜ Put Wall 45（+3.8%，弱）（OI 4.9k）
量化解读： 存量两侧均衡｜ATM IV 58.3%｜历史 Rank 34%（近端代理）｜IV/RV 1.14×（近似）｜净 delta 敞口 正 0 股

10-23（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 47（+8.4%，弱）（OI 0.1k） ｜ Put Wall 45（+3.8%，弱）（OI 0.3k）

10-30（Activity LOW）仓位参考: Max Pain 49 ｜ Put Wall 44（+1.5%）（OI 1.6k）

11-06（Activity LOW）仓位参考: Max Pain 47 ｜ Call Wall 47（+8.4%，弱）（OI 0.3k） ｜ Put Wall 41（-5.4%）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-16（4D）ATM IV 58.3% vs 10-23 51.9%（差 +6.4pp）——覆盖 成屋销售、Core Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=50 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=50）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-12/MP_evening.json