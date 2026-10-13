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

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 270C ΔOI +827（距现价 +2.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 251.55 → 收盘 263.45（+4.7%） ｜ 今日高 264.09 ｜ 低 248.35 ｜ 昨收 262.28 → 收盘 263.45（+0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.73 | OI比 1.07 | ATM IV 79.2% | Skew 0.9pp | Term 0.99 | ExpMove ±5.8%（近端） | Rank 37%
量化视角： IV 中性（Rank 37%）｜期限结构正常（Term 0.99）｜保护溢价薄（Skew 0.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.07×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（3D）±5.8% ｜ 10-23（10D）±12.1% ｜ 10-30（17D）±14.3% ｜ 11-06（24D）±16.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,660,721 | GEX Change vs 上次快照 3,502,361 | Flip: Primary Flip: 265.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 645 / LOW 85 / INVALID 112
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 265.40（全链重定价，覆盖 99%）
Put Wall 240（弱结构｜现价高于该位 9.8%） | Call Wall 280（弱结构｜现价低于该位 5.9%）
最近结构参考: Flip 265（现价低于该位 0.7%）
量化视角： 负 Gamma（166万，无历史分位）｜负 Gamma 缓解（+350万）｜现价位于 Flip 下方 0.74%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 240（Put Wall，弱结构）；上方 268（MaxPain，仅结算参考） / 280（Call Wall，弱结构）。
• Gamma 区域：切换参考 265（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +7.9k / P +4.0k ｜ Activity HIGH ｜ 3D
10-23  C +2.8k / P +2.7k ｜ Activity HIGH ｜ 10D
10-30  C +1.3k / P +0.7k ｜ Activity HIGH ｜ 17D
11-06  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 24D

📆 10-16 Forward Structure
存量OI: C 96.9k / P 103.6k，今日变化ΔOI: C +7.9k / P +4.0k，平值价格ATM: C $8.05 / P $7.10 ｜ ATM IV 79.2%，净 delta 敞口 242k shares
Top ΔOI: P 250 +1,081 ｜ C 270 +827
仓位参考: Max Pain 268 ｜ Call Wall 270（+2.5%，弱）（OI 7.7k） ｜ Put Wall 260（-1.3%，弱）（OI 5.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 79.2%｜历史 Rank 37%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 242,026 股

📆 10-23 Forward Structure
存量OI: C 19.7k / P 22.2k，今日变化ΔOI: C +2.8k / P +2.7k，平值价格ATM: C $16.13 / P $15.70 ｜ ATM IV 89.7%，净 delta 敞口 -31k shares
Top ΔOI: C 310 +311
仓位参考: Max Pain 270 ｜ Call Wall 280（+6.3%，弱）（OI 1.2k） ｜ Put Wall 250（-5.1%，弱）（OI 1.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 89.7%｜历史 Rank 37%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 30,617 股

📆 10-30 Forward Structure
存量OI: C 12.9k / P 20.7k，今日变化ΔOI: C +1.3k / P +0.7k，平值价格ATM: C $19.38 / P $18.18 ｜ ATM IV 85.3%，净 delta 敞口 36k shares
Top ΔOI: C 320 -506 ｜ C 280 +480 ｜ C 260 +179
仓位参考: Max Pain 280 ｜ Call Wall 280（+6.3%，弱）（OI 1.2k） ｜ Put Wall 240（-8.9%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 85.3%｜历史 Rank 37%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 35,933 股

📆 11-06 Forward Structure
存量OI: C 4.9k / P 11.0k，今日变化ΔOI: C +0.6k / P +0.5k，平值价格ATM: C $21.75 / P $22.30 ｜ ATM IV 80.4%，净 delta 敞口 19k shares
Top ΔOI: C 260 +295 ｜ P 225 +164 ｜ C 280 +142
仓位参考: Max Pain 265 ｜ Call Wall 260（-1.3%，弱）（OI 0.4k） ｜ Put Wall 240（-8.9%，弱）（OI 2.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 80.4%｜历史 Rank 37%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 正 18,918 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/BE_evening.json