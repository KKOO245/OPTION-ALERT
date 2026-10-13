# 期权晚报 2026-10-13（快照 16:40 ET）

📊 市场环境

SPY $778.01 ｜ QQQ $743.57
VIX 15.27 ↑0.4%（5D +1.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-13

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-13 10:00　【高】成屋销售　预测 3.95 ｜ 实际 3.99 ｜ 前值 3.93　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 待公布 ｜ 前值 3.4
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 待公布 ｜ 前值 2.4
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-14 750C ΔOI +2,841（距现价 +0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
QQQ: 今开 739.53 → 收盘 743.57（+0.5%） ｜ 今日高 744.20 ｜ 低 738.84 ｜ 昨收 746.04 → 收盘 743.57（-0.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.98 | OI比 2.15 | ATM IV 16.3% | Skew 2.8pp | Term 1.14 | ExpMove ±0.9%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构正常（Term 1.14）｜保护溢价中性（Skew 2.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 2.15×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 26% ｜ P/C OI(近端) 83%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 26%）｜近端持仓结构中性（P/C OI 分位 83%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-14（1D）±0.9% ｜ 10-15（2D）±1.1% ｜ 10-16（3D）±1.4% ｜ 10-19（6D）±1.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -365,438,062 | GEX Change vs 上次快照 9,668,275 | Flip: Primary Flip: 748.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3060 / LOW 398 / INVALID 1550
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 748.34（全链重定价，覆盖 96%）
Call Wall 760（弱结构｜现价低于该位 2.2%）
最近结构参考: Flip 748（现价低于该位 0.6%）
量化视角： 负 Gamma（3.65亿，历史分位 26%，中性区）｜负 Gamma 缓解（+967万）｜现价位于 Flip 下方 0.64%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 748（MaxPain，仅结算参考） / 760（Call Wall，弱结构）。
• Gamma 区域：切换参考 748（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-14  C +21.7k / P +38.7k ｜ Activity HIGH ｜ 1D
10-15  C +7.6k / P +26.1k ｜ Activity HIGH ｜ 2D
10-16  C +2.4k / P +54.0k ｜ Activity MEDIUM △ ｜ 3D
10-19  C +8.8k / P +22.2k ｜ Activity HIGH ｜ 6D

📆 10-14 Forward Structure
存量OI: C 47.7k / P 104.1k，今日变化ΔOI: C +21.7k / P +38.7k，平值价格ATM: C $3.12 / P $3.24 ｜ ATM IV 20.5%，净 delta 敞口 26k shares
Top ΔOI: C 750 +2,841 ｜ C 760 +2,583
仓位参考: Max Pain 748 ｜ Call Wall 750（+0.9%，弱）（OI 3.7k） ｜ Put Wall 730（-1.8%，弱）（OI 5.2k）
量化解读： 存量 Put 重｜ATM IV 20.5%｜历史 Rank 38%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 26,236 股

📆 10-15 Forward Structure
存量OI: C 37.6k / P 75.8k，今日变化ΔOI: C +7.6k / P +26.1k，平值价格ATM: C $4.18 / P $4.27 ｜ ATM IV 19.2%，净 delta 敞口 -88k shares
Top ΔOI: C 770 +2,492 ｜ P 694 +1,613 ｜ C 762 +1,060
仓位参考: Max Pain 749 ｜ Call Wall 765（+2.9%，弱）（OI 2.4k） ｜ Put Wall 725（-2.5%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 19.2%｜历史 Rank 38%（近端代理）｜IV/RV 1.39×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 88,407 股

10-16（MEDIUM △）Top ΔOI: 655P +18,219 ｜ 770C -5,909
10-16（MEDIUM △）仓位参考: Max Pain 735 ｜ Call Wall 760（+2.2%）（OI 67.9k） ｜ Put Wall 740（-0.5%，弱）（OI 34.2k）

📆 10-19 Forward Structure
存量OI: C 26.7k / P 49.1k，今日变化ΔOI: C +8.8k / P +22.2k，平值价格ATM: C $5.97 / P $5.73 ｜ ATM IV 15.3%，净 delta 敞口 12k shares
Top ΔOI: C 766 +1,980
仓位参考: Max Pain 750 ｜ Call Wall 750（+0.9%，弱）（OI 1.7k） ｜ Put Wall 745（+0.2%，弱）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 15.3%｜历史 Rank 38%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 12,139 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-13/QQQ_evening.json