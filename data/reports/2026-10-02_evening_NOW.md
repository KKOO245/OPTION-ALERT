# 期权晚报 2026-10-02（快照 16:40 ET）

📊 市场环境

SPY $769.64 ｜ QQQ $749.58
VIX 15.31 ↓6.6%（5D +3.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 140C ΔOI +1,374（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NOW

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NOW: 今开 139.41 → 收盘 134.38（-3.6%） ｜ 今日高 139.57 ｜ 低 133.47 ｜ 昨收 137.76 → 收盘 134.38（-2.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.40 | OI比 0.75 | ATM IV 39.0% | Skew 2.2pp | Term 1.49 | ExpMove ±5.0%（近端） | Rank 0%
量化视角： IV 历史低位（Rank 0%，期权偏便宜）｜期限结构正常偏陡（Term 1.49）｜保护溢价中性（Skew 2.2pp）｜存量 Call 偏重（OI比 0.75）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.40×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.75×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±5.0% ｜ 10-16（14D）±7.4% ｜ 10-23（21D）±9.3% ｜ 10-30（28D）±13.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,912,167 | GEX Change vs 上次快照 -7,587,197 | Flip: Primary Flip: 129.51（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 496 / LOW 63 / INVALID 145
结构观察区: Primary Flip 129.51（全链重定价，覆盖 87%）
Put Wall 125（弱结构｜现价高于该位 7.5%）
最近结构参考: Flip 130（现价高于该位 3.8%）
量化视角： 正 Gamma（991万，无历史分位）｜正 Gamma 减弱（759万）｜现价位于 Flip 上方 3.76%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 125（Put Wall，弱结构） / 132（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 130（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +2.6k / P -25 ｜ Activity HIGH ｜ 7D
10-16  C +0.6k / P -0.3k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +0.4k / P -0.5k ｜ Activity MEDIUM △ ｜ 21D
10-30  C +0.3k / P -46 ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 16.0k / P 11.8k，今日变化ΔOI: C +2.6k / P -25，平值价格ATM: C $3.60 / P $3.10 ｜ ATM IV 44.8%，净 delta 敞口 38k shares
Top ΔOI: C 140 +1,374 ｜ C 145 +433 ｜ C 143 +393
仓位参考: Max Pain 135 ｜ Call Wall 140（+4.2%，弱）（OI 2.0k） ｜ Put Wall 131（-2.5%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 44.8%｜历史 Rank 0%（近端代理）｜IV/RV 1.17×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 38,129 股

10-16（MEDIUM △）Top ΔOI: 142C +652 ｜ 130P -610
10-16（MEDIUM △）仓位参考: Max Pain 130 ｜ Call Wall 140（+4.2%，弱）（OI 5.7k） ｜ Put Wall 125（-7.0%，弱）（OI 5.4k）

10-23（MEDIUM △）仓位参考: Max Pain 134 ｜ Call Wall 134（-0.3%，弱）（OI 1.0k） ｜ Put Wall 122（-9.2%，弱）（OI 3.1k）

📆 10-30 Forward Structure
存量OI: C 5.7k / P 7.6k，今日变化ΔOI: C +0.3k / P -46，平值价格ATM: C $8.96 / P $8.55 ｜ ATM IV 58.2%，净 delta 敞口 4k shares
Top ΔOI: P 140 +56
仓位参考: Max Pain 135 ｜ Call Wall 140（+4.2%，弱）（OI 0.6k） ｜ Put Wall 123（-8.5%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 58.2%｜历史 Rank 0%（近端代理）｜IV/RV 1.52×（近似）｜净 delta 敞口 正 3,927 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/NOW_evening.json