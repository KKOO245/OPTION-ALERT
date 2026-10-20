# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 766P ΔOI +2,556（距现价 -0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 765.86 → 收盘 769.05（+0.4%） ｜ 今日高 772.28 ｜ 低 764.26 ｜ 昨收 766.48 → 收盘 769.05（+0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.01 | OI比 1.77 | ATM IV 14.4% | Skew 1.0pp | Term 0.94 | ExpMove ±0.6%（近端） | Rank 62%
量化视角： IV 中性（Rank 62%）｜期限结构正常（Term 0.94）｜保护溢价薄（Skew 1.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.77×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 36% ｜ P/C OI(近端) 44%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 36%）｜近端持仓结构中性（P/C OI 分位 44%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-21（1D）±0.6% ｜ 10-22（2D）±0.8% ｜ 10-23（3D）±1.0% ｜ 10-26（6D）±1.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -876,791,197 | GEX Change vs 上次快照 184,902,823 | Flip: Primary Flip: 774.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 2554 / LOW 379 / INVALID 1799
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 774.65（全链重定价，覆盖 94%）
最近结构参考: Flip 775（现价低于该位 0.7%）
量化视角： 负 Gamma（8.77亿，历史分位 36%，中性区）｜负 Gamma 缓解（+1.85亿）｜现价位于 Flip 下方 0.72%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 768（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 775（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-21  C +12.7k / P +22.3k ｜ Activity MEDIUM △ ｜ 1D
10-22  C +6.5k / P +14.3k ｜ Activity HIGH ｜ 2D
10-23  C +9.5k / P +71.9k ｜ Activity HIGH ｜ 3D
10-26  C +21.6k / P +24.5k ｜ Activity HIGH ｜ 6D

📆 10-21 Forward Structure
存量OI: C 94.1k / P 213.4k，今日变化ΔOI: C +12.7k / P +22.3k，平值价格ATM: C $2.58 / P $1.80 ｜ ATM IV 13.4%，净 delta 敞口 176k shares
Top ΔOI: P 766 +2,556 ｜ C 769 +1,667 ｜ P 754 +1,557
仓位参考: Max Pain 769 ｜ Call Wall 778（+1.2%，弱）（OI 4.1k） ｜ Put Wall 746（-3.0%，弱）（OI 11.1k）
量化解读： 存量 Put 重｜ATM IV 13.4%｜历史 Rank 62%（近端代理）｜IV/RV 1.61×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 176,495 股

📆 10-22 Forward Structure
存量OI: C 77.4k / P 89.4k，今日变化ΔOI: C +6.5k / P +14.3k，平值价格ATM: C $3.55 / P $2.63 ｜ ATM IV 13.4%，净 delta 敞口 120k shares
Top ΔOI: P 735 +2,016 ｜ P 737 +1,594 ｜ C 801 +1,423
仓位参考: Max Pain 770 ｜ Call Wall 780（+1.4%，弱）（OI 6.2k） ｜ Put Wall 749（-2.6%，弱）（OI 3.6k）
量化解读： 存量两侧均衡｜ATM IV 13.4%｜历史 Rank 62%（近端代理）｜IV/RV 1.61×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 120,242 股

📆 10-23 Forward Structure
存量OI: C 287.1k / P 572.7k，今日变化ΔOI: C +9.5k / P +71.9k，平值价格ATM: C $4.38 / P $3.26 ｜ ATM IV 13.5%，净 delta 敞口 -463k shares
Top ΔOI: P 762 +13,435 ｜ P 740 +10,158
仓位参考: Max Pain 770 ｜ Call Wall 790（+2.7%）（OI 36.7k） ｜ Put Wall 769（-0.0%，弱）（OI 32.4k）
量化解读： 存量 Put 重｜ATM IV 13.5%｜历史 Rank 62%（近端代理）｜IV/RV 1.62×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 463,358 股

📆 10-26 Forward Structure
存量OI: C 62.8k / P 68.3k，今日变化ΔOI: C +21.6k / P +24.5k，平值价格ATM: C $5.15 / P $3.87 ｜ ATM IV 11.4%，净 delta 敞口 -171k shares
Top ΔOI: P 762 +9,709 ｜ C 805 +6,105 ｜ C 807 +6,058
仓位参考: Max Pain 769 ｜ Call Wall 780（+1.4%，弱）（OI 4.8k） ｜ Put Wall 762（-0.9%）（OI 10.3k）
量化解读： 存量两侧均衡｜ATM IV 11.4%｜历史 Rank 62%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 负 171,330 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/SPY_evening.json