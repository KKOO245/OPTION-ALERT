# 期权晚报 2026-11-04（快照 16:40 ET）

📊 市场环境

SPY $766.81 ｜ QQQ $691.95
VIX 16.61 ↓20.3%（5D -1.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **事件差分**: 11-06 ATM IV 65.9% vs 11-13 54.4%（差 +11.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 180C ΔOI +4,200（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 165.08 → 收盘 171.70（+4.0%） ｜ 今日高 177.43 ｜ 低 164.60 ｜ 昨收 175.40 → 收盘 171.70（-2.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.59 | OI比 1.04 | ATM IV 65.9% | Skew 2.8pp | Term 0.76 | ExpMove ±4.0%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价中性（Skew 2.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.04×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-06（2D）±4.0% ｜ 11-13（9D）±6.8% ｜ 11-20（16D）±9.5% ｜ 11-27（23D）±9.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -12,599,571 | GEX Change vs 上次快照 -9,835,232 | Flip: Primary Flip: 174.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 544 / LOW 140 / INVALID 222
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 174.99（全链重定价，覆盖 100%）
最近结构参考: Flip 175（现价低于该位 1.9%）
量化视角： 负 Gamma（1260万，无历史分位）｜负 Gamma 加深（984万）｜现价位于 Flip 下方 1.88%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 182（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 175（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +21.0k / P -6.4k ｜ Activity HIGH ｜ 2D
11-13  C +9.0k / P +6.3k ｜ Activity HIGH ｜ 9D
11-20  C +7.1k / P +1.6k ｜ Activity HIGH ｜ 16D
11-27  C +1.9k / P +0.6k ｜ Activity HIGH ｜ 23D

📆 11-06 Forward Structure
存量OI: C 193.5k / P 201.1k，今日变化ΔOI: C +21.0k / P -6.4k，平值价格ATM: C $2.99 / P $3.80 ｜ ATM IV 65.9%，净 delta 敞口 853k shares
Top ΔOI: C 180 +4,200 ｜ C 175 +2,328
仓位参考: Max Pain 182 ｜ Call Wall 187.5（+9.2%，弱）（OI 13.3k） ｜ Put Wall 170（-1.0%，弱）（OI 7.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 65.9%｜历史 Rank 90%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 853,171 股

📆 11-13 Forward Structure
存量OI: C 37.8k / P 33.7k，今日变化ΔOI: C +9.0k / P +6.3k，平值价格ATM: C $5.60 / P $6.15 ｜ ATM IV 54.4%，净 delta 敞口 105k shares
Top ΔOI: C 200 +1,784 ｜ C 175 +1,013 ｜ C 187 +690
仓位参考: Max Pain 182 ｜ Call Wall 187.5（+9.2%，弱）（OI 1.4k） ｜ Put Wall 155（-9.7%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜ATM IV 54.4%｜历史 Rank 90%（近端代理）｜IV/RV 1.18×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 105,466 股

📆 11-20 Forward Structure
存量OI: C 177.5k / P 177.9k，今日变化ΔOI: C +7.1k / P +1.6k，平值价格ATM: C $7.85 / P $8.45 ｜ ATM IV 52.2%，净 delta 敞口 158k shares
Top ΔOI: C 205 +4,347 ｜ P 150 +1,525
仓位参考: Max Pain 175 ｜ Call Wall 165（-3.9%，弱）（OI 11.8k） ｜ Put Wall 180（+4.8%，弱）（OI 10.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 52.2%｜历史 Rank 90%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 158,235 股

📆 11-27 Forward Structure
存量OI: C 13.5k / P 14.8k，今日变化ΔOI: C +1.9k / P +0.6k，平值价格ATM: C $9.66 / P $7.40 ｜ ATM IV 49.8%，净 delta 敞口 62k shares
仓位参考: Max Pain 185 ｜ Call Wall 185（+7.7%，弱）（OI 0.5k） ｜ Put Wall 180（+4.8%，弱）（OI 1.3k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 49.8%｜历史 Rank 90%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 62,251 股

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 65.9% vs 11-13 54.4%（差 +11.4pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/PLTR_evening.json