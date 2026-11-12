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
🟡 **事件差分**: 11-13 ATM IV 47.4% vs 11-16 35.2%（差 +12.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 44P ΔOI +4,112（距现价 -1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 45.48 → 收盘 45.12（-0.8%） ｜ 今日高 45.58 ｜ 低 44.85 ｜ 昨收 46.65 → 收盘 45.12（-3.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.10 | OI比 0.53 | ATM IV 47.4% | Skew 4.0pp | Term 0.83 | ExpMove ±2.1%（近端） | Rank 79%
量化视角： IV 历史高位（Rank 79%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 4.0pp）｜存量 Call 偏重（OI比 0.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.10×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±2.1% ｜ 11-16（4D）±3.0% ｜ 11-18（6D）±4.2% ｜ 11-20（8D）±4.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,013,388 | GEX Change vs 上次快照 1,672,136 | Flip: Primary Flip: 45.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 628 / LOW 175 / INVALID 401
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 45.47（全链重定价，覆盖 96%）
最近结构参考: Flip 45（现价低于该位 0.8%）
量化视角： 负 Gamma（1301万，无历史分位）｜负 Gamma 缓解（+167万）｜现价位于 Flip 下方 0.78%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 47（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 45（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-13  C +4.1k / P +7.7k ｜ Activity HIGH ｜ 1D
11-16  C +1.2k / P +0.4k ｜ Activity HIGH ｜ 4D
11-18  C +0.4k / P +1.2k ｜ Activity HIGH ｜ 6D
11-20  C -16.5k / P -3.4k ｜ Activity HIGH ｜ 8D

📆 11-13 Forward Structure
存量OI: C 86.5k / P 46.1k，今日变化ΔOI: C +4.1k / P +7.7k，平值价格ATM: C $0.54 / P $0.39 ｜ ATM IV 47.4%，净 delta 敞口 -150k shares
Top ΔOI: P 44 +4,112 ｜ P 45 +1,827 ｜ P 46 +1,598
仓位参考: Max Pain 47 ｜ Call Wall 48（+6.4%，弱）（OI 5.2k） ｜ Put Wall 45（-0.3%，弱）（OI 6.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 47.4%｜历史 Rank 79%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 149,722 股

📆 11-16 Forward Structure
存量OI: C 11.3k / P 4.6k，今日变化ΔOI: C +1.2k / P +0.4k，平值价格ATM: C $0.73 / P $0.62 ｜ ATM IV 35.2%，净 delta 敞口 -18k shares
Top ΔOI: C 48 +354 ｜ C 49 +236 ｜ P 46 +196
仓位参考: Max Pain 47 ｜ Call Wall 48（+6.4%，弱）（OI 1.1k） ｜ Put Wall 46（+2.0%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 35.2%｜历史 Rank 79%（近端代理）｜IV/RV 0.84×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 18,355 股

📆 11-18 Forward Structure
存量OI: C 5.0k / P 7.3k，今日变化ΔOI: C +0.4k / P +1.2k，平值价格ATM: C $1.00 / P $0.88 ｜ ATM IV 40.3%，净 delta 敞口 -43k shares
Top ΔOI: P 45 +366 ｜ P 46 +114
仓位参考: Max Pain 46 ｜ Call Wall 49（+8.6%）（OI 2.0k） ｜ Put Wall 44.5（-1.4%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 40.3%｜历史 Rank 79%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 负 43,393 股

📆 11-20 Forward Structure
存量OI: C 581.1k / P 151.9k，今日变化ΔOI: C -16.5k / P -3.4k，平值价格ATM: C $1.17 / P $1.02 ｜ ATM IV 41.5%，净 delta 敞口 292k shares
Top ΔOI: P 58 -1,270
仓位参考: Max Pain 50 ｜ Put Wall 41（-9.1%，弱）（OI 11.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.5%｜历史 Rank 79%（近端代理）｜IV/RV 0.99×（近似）｜净 delta 敞口 正 292,471 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 47.4% vs 11-16 35.2%（差 +12.2pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/SLV_evening.json