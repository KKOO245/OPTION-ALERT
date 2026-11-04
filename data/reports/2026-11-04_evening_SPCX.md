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
🟡 **事件差分**: 11-06 ATM IV 69.0% vs 11-09 55.0%（差 +14.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-09 130P ΔOI +369（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 133.27 → 收盘 135.92（+2.0%） ｜ 今日高 140.50 ｜ 低 133.14 ｜ 昨收 141.31 → 收盘 135.92（-3.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.10 | OI比 1.49 | ATM IV 55.9% | Skew 0.7pp | Term 0.97 | ExpMove ±4.1%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构正常（Term 0.97）｜保护溢价薄（Skew 0.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.10×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.49×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±4.1% ｜ 11-09（5D）±5.1% ｜ 11-11（7D）±6.4% ｜ 11-13（9D）±7.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -84,193,510 | GEX Change vs 上次快照 -13,283,824 | Flip: Primary Flip: 142.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 676 / LOW 191 / INVALID 647
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 142.69（全链重定价，覆盖 92%）
Put Wall 135（弱结构｜现价高于该位 0.7%）
最近结构参考: Put Wall 135（现价高于该位 0.7%）
量化视角： 负 Gamma（8419万，无历史分位）｜负 Gamma 加深（1328万）｜现价位于 Flip 下方 4.75%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（Put Wall，弱结构）；上方 141（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 143（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +5.2k / P +15.4k ｜ Activity HIGH ｜ 2D
11-09  C +2.6k / P +2.7k ｜ Activity HIGH ｜ 5D
11-11  C +0.9k / P +1.3k ｜ Activity HIGH ｜ 7D
11-13  C +3.7k / P +3.3k ｜ Activity HIGH ｜ 9D

📆 11-06 Forward Structure
存量OI: C 249.3k / P 183.2k，今日变化ΔOI: C +5.2k / P +15.4k，平值价格ATM: C $2.75 / P $2.85 ｜ ATM IV 69.0%，净 delta 敞口 -374k shares
Top ΔOI: C 150 +4,153 ｜ P 125 +3,289
仓位参考: Max Pain 144 ｜ Call Wall 140（+3.0%，弱）（OI 9.2k） ｜ Put Wall 135（-0.7%，弱）（OI 22.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 69.0%｜历史 Rank 52%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 373,783 股

📆 11-09 Forward Structure
存量OI: C 9.6k / P 7.6k，今日变化ΔOI: C +2.6k / P +2.7k，平值价格ATM: C $3.41 / P $3.48 ｜ ATM IV 55.0%，净 delta 敞口 -62k shares
Top ΔOI: C 145 +426 ｜ P 130 +369
仓位参考: Max Pain 142 ｜ Call Wall 145（+6.7%，弱）（OI 1.1k） ｜ Put Wall 135（-0.7%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 55.0%｜历史 Rank 52%（近端代理）｜IV/RV 0.97×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 62,185 股

📆 11-11 Forward Structure
存量OI: C 3.6k / P 3.3k，今日变化ΔOI: C +0.9k / P +1.3k，平值价格ATM: C $4.36 / P $4.35 ｜ ATM IV 58.2%，净 delta 敞口 -29k shares
Top ΔOI: P 125 +306 ｜ P 130 +304 ｜ P 133 +202
仓位参考: Max Pain 142 ｜ Call Wall 145（+6.7%，弱）（OI 0.3k） ｜ Put Wall 130（-4.4%，弱）（OI 0.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 58.2%｜历史 Rank 52%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 负 28,711 股

📆 11-13 Forward Structure
存量OI: C 72.3k / P 59.8k，今日变化ΔOI: C +3.7k / P +3.3k，平值价格ATM: C $5.10 / P $5.05 ｜ ATM IV 59.5%，净 delta 敞口 -11k shares
Top ΔOI: P 125 -2,447
仓位参考: Max Pain 147 ｜ Call Wall 147（+8.2%，弱）（OI 2.6k） ｜ Put Wall 140（+3.0%，弱）（OI 3.7k）
量化解读： 存量 Call 重｜ATM IV 59.5%｜历史 Rank 52%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 10,736 股

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 69.0% vs 11-09 55.0%（差 +14.0pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/SPCX_evening.json