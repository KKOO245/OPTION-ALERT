# 期权晚报 2026-10-28（快照 16:40 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
VIX 16.91 ↓3.5%（5D +1.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 441.42 → 收盘 444.18（+0.6%） ｜ 今日高 449.97 ｜ 低 437.51 ｜ 昨收 445.88 → 收盘 444.18（-0.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.38 | OI比 0.90 | ATM IV 37.4% | Skew 1.3pp | Term 0.84 | ExpMove ±2.4%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价薄（Skew 1.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（2D）±2.4% ｜ 11-06（9D）±2.6% ｜ 11-13（16D）±6.6% ｜ 11-20（23D）±6.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,881,822 | GEX Change vs 上次快照 49,829 | Flip: Primary Flip: 419.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 245 / LOW 200 / INVALID 539
结构观察区: Primary Flip 419.13（全链重定价，覆盖 90%）
Call Wall 420（弱结构｜现价高于该位 5.8%）
最近结构参考: Call Wall 420（现价高于该位 5.8%）
量化视角： 正 Gamma（188万，无历史分位）｜正 Gamma 增强（+5万）｜现价位于 Flip 上方 5.98%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 435（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 419（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +28 / P +68 ｜ Activity MEDIUM △ ｜ 2D
11-06  C +46 / P +0.2k ｜ Activity MEDIUM △ ｜ 9D
11-13  C +6 / P -46 ｜ Activity MEDIUM △ ｜ 16D
11-20  C +37 / P +22 ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 2.4k / P 2.2k，今日变化ΔOI: C +28 / P +68，平值价格ATM: C $6.82 / P $4.00 ｜ ATM IV 37.4%，净 delta 敞口 -1k shares
Top ΔOI: P 425 +25 ｜ P 430 +18 ｜ C 475 +16
仓位参考: Max Pain 435 ｜ Call Wall 450（+1.3%，弱）（OI 0.2k） ｜ Put Wall 455（+2.4%）（OI 0.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 37.4%｜历史 Rank 30%（近端代理）｜IV/RV 1.65×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,171 股

11-06（MEDIUM △）Top ΔOI: 420P +124 ｜ 450C +35
11-06（MEDIUM △）仓位参考: Max Pain 428 ｜ Call Wall 430（-3.2%，弱）（OI 0.1k） ｜ Put Wall 420（-5.4%，弱）（OI 0.2k）

11-13（MEDIUM △）Top ΔOI: 410P -28 ｜ 415P -20
11-13（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 440（-0.9%，弱）（OI 0.1k） ｜ Put Wall 420（-5.4%，弱）（OI 81）

11-20（MEDIUM △）Top ΔOI: 420P +14
11-20（MEDIUM △）仓位参考: Max Pain 400 ｜ Call Wall 420（-5.4%，弱）（OI 0.8k） ｜ Put Wall 410（-7.7%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/ISRG_evening.json