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
🟡 **近现价集中开仓**: 11-13 143C ΔOI +377（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 133.00 → 收盘 136.27（+2.5%） ｜ 今日高 138.85 ｜ 低 132.87 ｜ 昨收 132.13 → 收盘 136.27（+3.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.39 | OI比 0.51 | ATM IV 79.0% | Skew 0.4pp | Term 0.88 | ExpMove ±4.8%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±4.8% ｜ 11-20（9D）±8.6% ｜ 11-27（16D）±11.5% ｜ 12-04（23D）±13.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 18,227,558 | GEX Change vs 上次快照 7,816,183 | Flip: Primary Flip: 130.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 435 / LOW 220 / INVALID 333
结构观察区: Primary Flip 130.42（全链重定价，覆盖 98%）
Call Wall 140（弱结构｜现价低于该位 2.7%）
最近结构参考: Call Wall 140（现价低于该位 2.7%）
量化视角： 正 Gamma（1823万，无历史分位）｜正 Gamma 增强（+782万）｜现价位于 Flip 上方 4.48%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 137（MaxPain，仅结算参考） / 140（Call Wall，弱结构）。
• Gamma 区域：切换参考 130（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +2.8k / P +0.8k ｜ Activity MEDIUM △ ｜ 2D
11-20  C +1.9k / P +16 ｜ Activity MEDIUM △ ｜ 9D
11-27  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 16D
12-04  C +0.2k / P +0.4k ｜ Activity HIGH ｜ 23D

📆 11-13 Forward Structure
存量OI: C 72.6k / P 37.3k，今日变化ΔOI: C +2.8k / P +0.8k，平值价格ATM: C $3.41 / P $3.15 ｜ ATM IV 79.0%，净 delta 敞口 150k shares
Top ΔOI: C 147 +491 ｜ C 141 +403 ｜ C 143 +377
仓位参考: Max Pain 137 ｜ Call Wall 147（+7.9%，弱）（OI 9.3k） ｜ Put Wall 135（-0.9%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 79.0%｜历史 Rank 59%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 150,350 股

11-20（MEDIUM △）Top ΔOI: 140C +942
11-20（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 140（+2.7%，弱）（OI 2.7k） ｜ Put Wall 140（+2.7%，弱）（OI 3.4k）

📆 11-27 Forward Structure
存量OI: C 5.7k / P 8.2k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $8.95 / P $6.75 ｜ ATM IV 65.2%，净 delta 敞口 16k shares
Top ΔOI: C 140 +62
仓位参考: Max Pain 145 ｜ Call Wall 140（+2.7%，弱）（OI 0.3k） ｜ Put Wall 130（-4.6%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 65.2%｜历史 Rank 59%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 16,279 股

📆 12-04 Forward Structure
存量OI: C 5.1k / P 7.9k，今日变化ΔOI: C +0.2k / P +0.4k，平值价格ATM: C $10.10 / P $7.70 ｜ ATM IV 67.4%，净 delta 敞口 -11k shares
Top ΔOI: P 135 +410
仓位参考: Max Pain 140 ｜ Call Wall 140（+2.7%）（OI 1.4k） ｜ Put Wall 135（-0.9%）（OI 2.2k）
量化解读： 存量 Put 重｜ATM IV 67.4%｜历史 Rank 59%（近端代理）｜IV/RV 1.02×（近似）｜净 delta 敞口 负 11,061 股

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 79.0% vs 11-20 70.1%（差 +8.9pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/COIN_evening.json