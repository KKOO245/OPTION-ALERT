# 期权晚报 2026-10-19（快照 21:00 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,358.50 → 收盘 1,371.12（+0.9%） ｜ 今日高 1407.00 ｜ 低 1357.64 ｜ 昨收 1,299.30 → 收盘 1,371.12（+5.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.58 | OI比 0.93 | ATM IV 77.4% | Skew 2.1pp | Term 0.95 | ExpMove ±6.5%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 0.95）｜保护溢价中性（Skew 2.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.93×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（4D）±6.5% ｜ 10-30（11D）±12.6% ｜ 11-06（18D）±14.2% ｜ 11-13（25D）±15.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,849,707 | GEX Change vs 上次快照 -417,556 | Flip: Primary Flip: 1421.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1979 / LOW 317 / INVALID 1100
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1421.87（全链重定价，覆盖 100%）
Call Wall 1,500（现价低于该位 8.6%）
最近结构参考: Flip 1422（现价低于该位 3.6%）
量化视角： 负 Gamma（285万，无历史分位）｜负 Gamma 加深（42万）｜现价位于 Flip 下方 3.57%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,465（MaxPain，仅结算参考） / 1,500（Call Wall）。
• Gamma 区域：切换参考 1422（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0 / P +0 ｜ Activity LOW ｜ 4D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 11D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 18D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 25D

📆 10-23 Forward Structure
存量OI: C 36.0k / P 33.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $45.20 / P $43.70 ｜ ATM IV 77.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 1,465 ｜ Call Wall 1500（+9.4%）（OI 2.2k） ｜ Put Wall 1250（-8.8%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 77.4%｜历史 Rank 36%（近端代理）｜IV/RV 1.52×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 1,520 ｜ Call Wall 1500（+9.4%，弱）（OI 1.5k） ｜ Put Wall 1400（+2.1%，弱）（OI 0.6k）

11-06（Activity LOW）仓位参考: Max Pain 1,520 ｜ Call Wall 1400（+2.1%，弱）（OI 0.6k） ｜ Put Wall 1400（+2.1%，弱）（OI 0.4k）

11-13（Activity LOW）仓位参考: Max Pain 1,520 ｜ Call Wall 1480（+7.9%，弱）（OI 0.2k） ｜ Put Wall 1300（-5.2%，弱）（OI 0.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/SNDK_evening.json