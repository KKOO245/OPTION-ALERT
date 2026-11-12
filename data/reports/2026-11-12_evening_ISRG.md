# 期权晚报 2026-11-12（快照 16:40 ET）

📊 市场环境

SPY $757.12 ｜ QQQ $688.17
VIX 18.70 ↑6.9%（5D -33.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-27 445P ΔOI +11（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 448.61 → 收盘 439.89（-1.9%） ｜ 今日高 451.26 ｜ 低 438.44 ｜ 昨收 449.53 → 收盘 439.89（-2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.18 | OI比 0.95 | ATM IV 34.3% | Skew 9.6pp | Term 0.99 | ExpMove ±2.1%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构正常（Term 0.99）｜保护溢价显著（Skew 9.6pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.18×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.95×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（1D）±2.1% ｜ 11-20（8D）±4.0% ｜ 11-27（15D）±5.6% ｜ 12-04（22D）±5.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,036,149 | GEX Change vs 上次快照 391,950 | Flip: Primary Flip: 417.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 261 / LOW 227 / INVALID 522
结构观察区: Primary Flip 417.92（全链重定价，覆盖 89%）
Call Wall 480（弱结构｜现价低于该位 8.4%）
最近结构参考: Flip 418（现价高于该位 5.3%）
量化视角： 正 Gamma（304万，无历史分位）｜正 Gamma 增强（+39万）｜现价位于 Flip 上方 5.26%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 440（MaxPain，仅结算参考） / 480（Call Wall，弱结构）。
• Gamma 区域：切换参考 418（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +28 / P +69 ｜ Activity LOW ｜ 1D
11-20  C -15 / P -52 ｜ Activity MEDIUM △ ｜ 8D
11-27  C +19 / P +15 ｜ Activity MEDIUM △ ｜ 15D
12-04  C -16 / P +4 ｜ Activity MEDIUM △ ｜ 22D

📆 11-13 Forward Structure
存量OI: C 1.7k / P 1.6k，今日变化ΔOI: C +28 / P +69，平值价格ATM: C $5.85 / P $3.50 ｜ ATM IV 34.3%，净 delta 敞口 3k shares
Top ΔOI: P 430 +52 ｜ P 482 -21 ｜ P 440 +15
仓位参考: Max Pain 440 ｜ Call Wall 480（+9.1%，弱）（OI 0.2k） ｜ Put Wall 462.5（+5.1%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 34.3%｜历史 Rank 17%（近端代理）｜IV/RV 0.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,526 股

11-20（MEDIUM △）Top ΔOI: 500P -54 ｜ 450C -19
11-20（MEDIUM △）仓位参考: Max Pain 410 ｜ Call Wall 420（-4.5%，弱）（OI 0.8k） ｜ Put Wall 410（-6.8%，弱）（OI 0.5k）

11-27（MEDIUM △）Top ΔOI: 445P +11 ｜ 435C +6
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 430（-2.2%，弱）（OI 64） ｜ Put Wall 410（-6.8%，弱）（OI 42）

12-04（MEDIUM △）Top ΔOI: 460C -8
12-04（MEDIUM △）仓位参考: Max Pain 450 ｜ Call Wall 475（+8.0%，弱）（OI 82） ｜ Put Wall 405（-7.9%，弱）（OI 25）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/ISRG_evening.json