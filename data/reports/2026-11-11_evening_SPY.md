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
🟡 **事件差分**: 11-12 ATM IV 13.7% vs 11-13 0.0%（差 +13.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-12 744P ΔOI -6,176（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 756.80 → 收盘 759.81（+0.4%） ｜ 今日高 762.51 ｜ 低 754.91 ｜ 昨收 749.92 → 收盘 759.81（+1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.78 | OI比 1.08 | ATM IV 10.6% | Skew -0.2pp | Term 1.32 | ExpMove ±0.6%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常偏陡（Term 1.32）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.78×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.08×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 58% ｜ P/C OI(近端) 4%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 58%）｜近端持仓极端 Call 重（P/C OI 分位 4%，历史极低区）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-12（1D）±0.6% ｜ 11-13（2D）±0.0% ｜ 11-16（5D）±1.1% ｜ 11-17（6D）±1.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 95,127,223 | GEX Change vs 上次快照 199,887,469 | Flip: Primary Flip: 759.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 3207 / LOW 370 / INVALID 1799
结构观察区: Primary Flip 759.06（全链重定价，覆盖 95%）
最近结构参考: Flip 759（现价高于该位 0.1%）
量化视角： 正 Gamma（9513万，历史分位 58%，中性区）｜由负转正（+2.00亿）｜现价位于 Flip 上方 0.10%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 749（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 759（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-12  C +23.3k / P +12.2k ｜ Activity HIGH ｜ 1D
11-13  C +48.2k / P +42.5k ｜ Activity HIGH ｜ 2D
11-16  C +17.3k / P +15.6k ｜ Activity HIGH ｜ 5D
11-17  C +7.7k / P +7.1k ｜ Activity HIGH ｜ 6D

📆 11-12 Forward Structure
存量OI: C 90.0k / P 108.4k，今日变化ΔOI: C +23.3k / P +12.2k，平值价格ATM: C $2.34 / P $2.03 ｜ ATM IV 13.7%，净 delta 敞口 1.3M shares
Top ΔOI: P 744 -6,176 ｜ P 748 +3,778 ｜ C 759 +2,953
仓位参考: Max Pain 748 ｜ Call Wall 775（+2.0%）（OI 6.8k） ｜ Put Wall 744（-2.1%，弱）（OI 13.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 13.7%｜历史 Rank 28%（近端代理）｜IV/RV 0.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,295,533 股

📆 11-13 Forward Structure
存量OI: C 364.9k / P 543.4k，今日变化ΔOI: C +48.2k / P +42.5k，平值价格ATM: C $0.26 / P $0.00 ｜ ATM IV 0.0%，净 delta 敞口 591k shares
Top ΔOI: P 760 +21,498 ｜ P 716 +4,479 ｜ C 779 +4,240
仓位参考: Max Pain 755 ｜ Call Wall 776（+2.1%，弱）（OI 24.3k） ｜ Put Wall 745（-1.9%，弱）（OI 29.5k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜净 delta 敞口 正 590,771 股

📆 11-16 Forward Structure
存量OI: C 81.9k / P 81.0k，今日变化ΔOI: C +17.3k / P +15.6k，平值价格ATM: C $4.40 / P $3.77 ｜ ATM IV 11.4%，净 delta 敞口 307k shares
Top ΔOI: P 715 +4,440 ｜ P 720 +3,946 ｜ C 788 +3,368
仓位参考: Max Pain 749 ｜ Call Wall 770（+1.3%，弱）（OI 6.5k） ｜ Put Wall 740（-2.6%，弱）（OI 3.8k）
量化解读： 存量两侧均衡｜ATM IV 11.4%｜历史 Rank 28%（近端代理）｜IV/RV 0.53×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 306,660 股

📆 11-17 Forward Structure
存量OI: C 35.5k / P 32.2k，今日变化ΔOI: C +7.7k / P +7.1k，平值价格ATM: C $5.22 / P $4.54 ｜ ATM IV 12.5%，净 delta 敞口 255k shares
Top ΔOI: C 782 +1,574 ｜ P 685 +1,061 ｜ P 715 +588
仓位参考: Max Pain 749 ｜ Call Wall 782（+2.9%）（OI 3.9k） ｜ Put Wall 750（-1.3%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜ATM IV 12.5%｜历史 Rank 28%（近端代理）｜IV/RV 0.58×（近似）｜净 delta 敞口 正 254,716 股

📅 事件差分（观察，非因果）: 11-12（1D）ATM IV 13.7% vs 11-13 0.0%（差 +13.7pp）——覆盖 成屋销售
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/SPY_evening.json