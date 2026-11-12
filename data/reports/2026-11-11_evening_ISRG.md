# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 17.49 ↓10.1%（5D +5.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 430P ΔOI +38（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 446.00 → 收盘 449.53（+0.8%） ｜ 今日高 450.99 ｜ 低 443.24 ｜ 昨收 450.04 → 收盘 449.53（-0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.85 | OI比 0.92 | ATM IV 37.2% | Skew 13.4pp | Term 0.84 | ExpMove ±2.6%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价显著（Skew 13.4pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.85×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-13（2D）±2.6% ｜ 11-20（9D）±3.5% ｜ 11-27（16D）±6.8% ｜ 12-04（23D）±5.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 3,362,981 | GEX Change vs 上次快照 585,012 | Flip: Primary Flip: 416.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 329 / LOW 214 / INVALID 461
结构观察区: Primary Flip 416.38（全链重定价，覆盖 93%）
Call Wall 480（弱结构｜现价低于该位 6.3%）
最近结构参考: Call Wall 480（现价低于该位 6.3%）
量化视角： 正 Gamma（336万，无历史分位）｜正 Gamma 增强（+59万）｜现价位于 Flip 上方 7.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 440（MaxPain，仅结算参考）；上方 480（Call Wall，弱结构）。
• Gamma 区域：切换参考 416（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +0.1k / P +57 ｜ Activity HIGH ｜ 2D
11-20  C -98 / P +75 ｜ Activity MEDIUM △ ｜ 9D
11-27  C +54 / P +2 ｜ Activity MEDIUM △ ｜ 16D
12-04  C +2 / P +13 ｜ Activity LOW ｜ 23D

📆 11-13 Forward Structure
存量OI: C 1.7k / P 1.5k，今日变化ΔOI: C +0.1k / P +57，平值价格ATM: C $4.60 / P $7.00 ｜ ATM IV 37.2%，净 delta 敞口 1k shares
Top ΔOI: C 465 +82 ｜ C 460 +47 ｜ P 430 +38
仓位参考: Max Pain 440 ｜ Call Wall 480（+6.8%，弱）（OI 0.2k） ｜ Put Wall 462.5（+2.9%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜ATM IV 37.2%｜历史 Rank 31%（近端代理）｜IV/RV 0.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,052 股

11-20（MEDIUM △）Top ΔOI: 475C -36 ｜ 460P +32
11-20（MEDIUM △）仓位参考: Max Pain 410 ｜ Call Wall 420（-6.6%，弱）（OI 0.8k） ｜ Put Wall 410（-8.8%，弱）（OI 0.5k）

11-27（MEDIUM △）Top ΔOI: 485C +21 ｜ 450C +15
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 430（-4.3%，弱）（OI 64） ｜ Put Wall 410（-8.8%，弱）（OI 42）

12-04（Activity LOW）仓位参考: Max Pain 450 ｜ Call Wall 475（+5.7%，弱）（OI 82） ｜ Put Wall 405（-9.9%，弱）（OI 25）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/ISRG_evening.json