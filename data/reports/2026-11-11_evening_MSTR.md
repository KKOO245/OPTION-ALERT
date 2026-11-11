# 期权晚报 2026-11-11（快照 16:40 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $690.38
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
🟡 **事件差分**: 11-13 ATM IV 94.0% vs 11-20 80.2%（差 +13.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 125C ΔOI +1,597（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 120.49 → 收盘 122.35（+1.5%） ｜ 今日高 124.14 ｜ 低 120.21 ｜ 昨收 121.07 → 收盘 122.35（+1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.44 | OI比 0.60 | ATM IV 94.0% | Skew 2.4pp | Term 0.79 | ExpMove ±5.6%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价中性（Skew 2.4pp）｜存量 Call 偏重（OI比 0.60）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.60×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±5.6% ｜ 11-20（9D）±10.1% ｜ 11-27（16D）±12.2% ｜ 12-04（23D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,576,377 | GEX Change vs 上次快照 8,489,534 | Flip: Primary Flip: 120.38（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 531 / LOW 188 / INVALID 263
结构观察区: Primary Flip 120.38（全链重定价，覆盖 100%）
最近结构参考: Flip 120（现价高于该位 1.6%）
量化视角： 正 Gamma（1458万，无历史分位）｜正 Gamma 增强（+849万）｜现价位于 Flip 上方 1.63%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 126（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 120（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +9.0k / P -0.5k ｜ Activity MEDIUM △ ｜ 2D
11-20  C +2.9k / P +8.1k ｜ Activity HIGH ｜ 9D
11-27  C +1.6k / P +5.2k ｜ Activity HIGH ｜ 16D
12-04  C +1.0k / P +5.0k ｜ Activity HIGH ｜ 23D

📆 11-13 Forward Structure
存量OI: C 239.3k / P 144.6k，今日变化ΔOI: C +9.0k / P -0.5k，平值价格ATM: C $3.56 / P $3.28 ｜ ATM IV 94.0%，净 delta 敞口 584k shares
Top ΔOI: C 125 +1,597 ｜ C 123 +1,183
仓位参考: Max Pain 126 ｜ Call Wall 133（+8.7%，弱）（OI 43.8k）
量化解读： 存量 Call 重｜ATM IV 94.0%｜历史 Rank 73%（近端代理）｜IV/RV 1.40×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 584,203 股

📆 11-20 Forward Structure
存量OI: C 167.3k / P 157.8k，今日变化ΔOI: C +2.9k / P +8.1k，平值价格ATM: C $6.40 / P $5.95 ｜ ATM IV 80.2%，净 delta 敞口 121k shares
Top ΔOI: P 105 +1,290
仓位参考: Max Pain 135 ｜ Put Wall 120（-1.9%，弱）（OI 11.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 80.2%｜历史 Rank 73%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 120,548 股

📆 11-27 Forward Structure
存量OI: C 17.2k / P 44.5k，今日变化ΔOI: C +1.6k / P +5.2k，平值价格ATM: C $7.30 / P $7.65 ｜ ATM IV 73.8%，净 delta 敞口 -14k shares
Top ΔOI: P 95 +680
仓位参考: Max Pain 150 ｜ Call Wall 130（+6.3%，弱）（OI 1.0k） ｜ Put Wall 115（-6.0%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜ATM IV 73.8%｜历史 Rank 73%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 负 14,127 股

📆 12-04 Forward Structure
存量OI: C 16.6k / P 27.9k，今日变化ΔOI: C +1.0k / P +5.0k，平值价格ATM: C $10.30 / P $7.60 ｜ ATM IV 73.9%，净 delta 敞口 -92k shares
Top ΔOI: P 90 +684
仓位参考: Max Pain 150 ｜ Put Wall 130（+6.3%，弱）（OI 1.3k）
量化解读： 存量 Put 重｜ATM IV 73.9%｜历史 Rank 73%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 负 92,429 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 94.0% vs 11-20 80.2%（差 +13.8pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/MSTR_evening.json