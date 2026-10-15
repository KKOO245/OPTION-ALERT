# 期权晚报 2026-10-15（快照 16:40 ET）

📊 市场环境

SPY $771.79 ｜ QQQ $728.00
VIX 16.46 ↓2.4%（5D +6.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 740C ΔOI +13,699（距现价 +1.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 718.54 → 收盘 728.00（+1.3%） ｜ 今日高 729.43 ｜ 低 715.43 ｜ 昨收 728.95 → 收盘 728.00（-0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.98 | OI比 1.50 | ATM IV 18.9% | Skew -0.0pp | Term 1.06 | ExpMove ±0.9%（近端） | Rank 54%
量化视角： IV 中性（Rank 54%）｜期限结构正常（Term 1.06）｜Put 保护异常便宜（Skew -0.0pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.50×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 7% ｜ P/C OI(近端) 38%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 7%）｜近端持仓结构中性（P/C OI 分位 38%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-16（1D）±0.9% ｜ 10-19（4D）±1.3% ｜ 10-20（5D）±1.6% ｜ 10-21（6D）±1.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -939,512,632 | GEX Change vs 上次快照 425,077,208 | Flip: Primary Flip: 739.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2943 / LOW 411 / INVALID 1604
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 739.34（全链重定价，覆盖 94%）
最近结构参考: Flip 739（现价低于该位 1.5%）
量化视角： 负 Gamma（9.40亿，历史分位偏负区，比 93% 的交易日更负）｜负 Gamma 缓解（+4.25亿）｜现价位于 Flip 下方 1.53%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 734（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 739（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +48.8k / P +12.6k ｜ Activity HIGH ｜ 1D
10-19  C +18.4k / P +12.2k ｜ Activity HIGH ｜ 4D
10-20  C +14.2k / P +8.9k ｜ Activity HIGH ｜ 5D
10-21  C +7.8k / P +10.9k ｜ Activity HIGH ｜ 6D

📆 10-16 Forward Structure
存量OI: C 782.5k / P 1312.7k，今日变化ΔOI: C +48.8k / P +12.6k，平值价格ATM: C $3.24 / P $3.39 ｜ ATM IV 21.7%，净 delta 敞口 4.0M shares
Top ΔOI: C 740 +13,699 ｜ C 735 +10,967
仓位参考: Max Pain 732 ｜ Call Wall 740（+1.6%，弱）（OI 38.4k） ｜ Put Wall 740（+1.6%，弱）（OI 27.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 21.7%｜历史 Rank 54%（近端代理）｜IV/RV 1.76×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,011,069 股

📆 10-19 Forward Structure
存量OI: C 54.8k / P 86.7k，今日变化ΔOI: C +18.4k / P +12.2k，平值价格ATM: C $4.83 / P $4.89 ｜ ATM IV 15.9%，净 delta 敞口 279k shares
Top ΔOI: C 753 +3,822 ｜ P 720 +3,173 ｜ P 728 +3,028
仓位参考: Max Pain 740 ｜ Call Wall 740（+1.6%，弱）（OI 2.3k） ｜ Put Wall 720（-1.1%，弱）（OI 6.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 15.9%｜历史 Rank 54%（近端代理）｜IV/RV 1.29×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 279,103 股

📆 10-20 Forward Structure
存量OI: C 41.3k / P 46.1k，今日变化ΔOI: C +14.2k / P +8.9k，平值价格ATM: C $5.72 / P $5.79 ｜ ATM IV 16.8%，净 delta 敞口 279k shares
Top ΔOI: C 733 +4,176 ｜ C 740 +1,815
仓位参考: Max Pain 733 ｜ Call Wall 749（+2.9%）（OI 9.2k） ｜ Put Wall 726（-0.3%，弱）（OI 2.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 16.8%｜历史 Rank 54%（近端代理）｜IV/RV 1.36×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 278,823 股

📆 10-21 Forward Structure
存量OI: C 23.6k / P 33.9k，今日变化ΔOI: C +7.8k / P +10.9k，平值价格ATM: C $6.68 / P $6.71 ｜ ATM IV 17.7%，净 delta 敞口 78k shares
Top ΔOI: C 749 +1,263
仓位参考: Max Pain 740 ｜ Call Wall 749（+2.9%）（OI 2.0k） ｜ Put Wall 710（-2.5%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 17.7%｜历史 Rank 54%（近端代理）｜IV/RV 1.44×（近似）｜净 delta 敞口 正 77,751 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 21.7% vs 10-19 15.9%（差 +5.8pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/QQQ_evening.json