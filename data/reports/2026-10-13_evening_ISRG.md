# 期权晚报 2026-10-13（快照 16:40 ET）

📊 市场环境

SPY $778.01 ｜ QQQ $743.57
VIX 15.27 ↑0.4%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 428.98 → 收盘 422.06（-1.6%） ｜ 今日高 430.00 ｜ 低 416.37 ｜ 昨收 427.64 → 收盘 422.06（-1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.68 | OI比 0.92 | ATM IV 36.6% | Skew 0.7pp | Term 1.19 | ExpMove ±2.9%（近端） | Rank 34%
量化视角： IV 中性（Rank 34%）｜期限结构正常偏陡（Term 1.19）｜保护溢价薄（Skew 0.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.68×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±2.9% ｜ 10-23（10D）±8.2% ｜ 10-30（17D）±0.0% ｜ 11-06（24D）±9.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,980,394 | GEX Change vs 上次快照 416,273 | Flip: Primary Flip: 397.14（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 377 / LOW 152 / INVALID 375
结构观察区: Primary Flip 397.14（全链重定价，覆盖 93%）
Call Wall 420（弱结构｜现价高于该位 0.5%）
最近结构参考: Call Wall 420（现价高于该位 0.5%）
量化视角： 正 Gamma（298万，无历史分位）｜正 Gamma 增强（+42万）｜现价位于 Flip 上方 6.28%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 397（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +0.2k / P +98 ｜ Activity MEDIUM △ ｜ 3D
10-23  C +0.5k / P +86 ｜ Activity HIGH ｜ 10D
10-30  C +26 / P +2 ｜ Activity MEDIUM △ ｜ 17D
11-06  C +7 / P +28 ｜ Activity MEDIUM △ ｜ 24D

📆 10-16 Forward Structure
存量OI: C 11.7k / P 10.7k，今日变化ΔOI: C +0.2k / P +98，平值价格ATM: C $6.60 / P $5.65 ｜ ATM IV 36.6%，净 delta 敞口 740 shares
Top ΔOI: C 445 +81 ｜ C 442 +45 ｜ P 425 +44
仓位参考: Max Pain 395 ｜ Call Wall 400（-5.2%，弱）（OI 0.9k） ｜ Put Wall 380（-10.0%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 36.6%｜历史 Rank 34%（近端代理）｜IV/RV 1.54×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 740 股

📆 10-23 Forward Structure
存量OI: C 2.4k / P 1.7k，今日变化ΔOI: C +0.5k / P +86，平值价格ATM: C $17.75 / P $17.00 ｜ ATM IV 63.4%，净 delta 敞口 6k shares
Top ΔOI: C 460 +194 ｜ P 400 +39
仓位参考: Max Pain 415 ｜ Call Wall 425（+0.7%，弱）（OI 0.5k） ｜ Put Wall 415（-1.7%）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 63.4%｜历史 Rank 34%（近端代理）｜IV/RV 2.66×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,527 股

10-30（MEDIUM △）Top ΔOI: 455C +11 ｜ 430C +5
10-30（MEDIUM △）仓位参考: Max Pain 395 ｜ Call Wall 460（+9.0%，弱）（OI 94） ｜ Put Wall 380（-10.0%，弱）（OI 50）

11-06（MEDIUM △）Top ΔOI: 390P +27 ｜ 425P +5
11-06（MEDIUM △）仓位参考: Max Pain 400 ｜ Call Wall 455（+7.8%，弱）（OI 50） ｜ Put Wall 390（-7.6%）（OI 52）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/ISRG_evening.json