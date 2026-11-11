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
🟡 **近现价集中开仓**: 11-12 700C ΔOI +2,459（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 687.28 → 收盘 690.38（+0.5%） ｜ 今日高 695.57 ｜ 低 683.60 ｜ 昨收 674.76 → 收盘 690.38（+2.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.93 | OI比 1.37 | ATM IV 17.3% | Skew -1.4pp | Term 1.35 | ExpMove ±1.1%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构正常偏陡（Term 1.35）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.93×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 59% ｜ P/C OI(近端) 26%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 59%）｜近端持仓结构中性（P/C OI 分位 26%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-12（1D）±1.1% ｜ 11-13（2D）±1.6% ｜ 11-16（5D）±1.9% ｜ 11-17（6D）±2.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 75,537,122 | GEX Change vs 上次快照 111,328,089 | Flip: Primary Flip: 688.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 3818 / LOW 437 / INVALID 1783
结构观察区: Primary Flip 688.28（全链重定价，覆盖 97%）
Call Wall 700（弱结构｜现价低于该位 1.4%）
最近结构参考: Flip 688（现价高于该位 0.3%）
量化视角： 正 Gamma（7554万，历史分位 59%，中性区）｜由负转正（+1.11亿）｜现价位于 Flip 上方 0.31%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 674（MaxPain，仅结算参考）；上方 700（Call Wall，弱结构）。
• Gamma 区域：切换参考 688（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-12  C +11.6k / P +18.1k ｜ Activity HIGH ｜ 1D
11-13  C +15.0k / P +26.4k ｜ Activity HIGH ｜ 2D
11-16  C +6.0k / P +3.4k ｜ Activity HIGH ｜ 5D
11-17  C +2.8k / P +8.7k ｜ Activity HIGH ｜ 6D

📆 11-12 Forward Structure
存量OI: C 64.3k / P 59.2k，今日变化ΔOI: C +11.6k / P +18.1k，平值价格ATM: C $3.63 / P $3.68 ｜ ATM IV 25.3%，净 delta 敞口 564k shares
Top ΔOI: C 700 +2,459 ｜ P 640 +1,981 ｜ P 670 +1,343
仓位参考: Max Pain 674 ｜ Call Wall 700（+1.4%，弱）（OI 4.2k） ｜ Put Wall 670（-3.0%，弱）（OI 2.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 25.3%｜历史 Rank 43%（近端代理）｜IV/RV 0.74×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 563,730 股

📆 11-13 Forward Structure
存量OI: C 302.2k / P 409.8k，今日变化ΔOI: C +15.0k / P +26.4k，平值价格ATM: C $5.45 / P $5.22 ｜ ATM IV 26.1%，净 delta 敞口 845k shares
Top ΔOI: C 680 +2,932
仓位参考: Max Pain 685 ｜ Call Wall 700（+1.4%，弱）（OI 15.3k） ｜ Put Wall 685（-0.8%，弱）（OI 23.9k）
量化解读： 存量 Put 重｜ATM IV 26.1%｜历史 Rank 43%（近端代理）｜IV/RV 0.77×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 845,218 股

📆 11-16 Forward Structure
存量OI: C 46.2k / P 41.5k，今日变化ΔOI: C +6.0k / P +3.4k，平值价格ATM: C $6.93 / P $6.54 ｜ ATM IV 21.1%，净 delta 敞口 160k shares
Top ΔOI: C 700 +456
仓位参考: Max Pain 675 ｜ Call Wall 704（+2.0%，弱）（OI 3.4k） ｜ Put Wall 670（-3.0%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 21.1%｜历史 Rank 43%（近端代理）｜IV/RV 0.62×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 159,699 股

📆 11-17 Forward Structure
存量OI: C 21.7k / P 22.6k，今日变化ΔOI: C +2.8k / P +8.7k，平值价格ATM: C $8.35 / P $7.83 ｜ ATM IV 22.9%，净 delta 敞口 87k shares
仓位参考: Max Pain 671 ｜ Call Wall 710（+2.8%）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 22.9%｜历史 Rank 43%（近端代理）｜IV/RV 0.67×（近似）｜净 delta 敞口 正 87,208 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/QQQ_evening.json