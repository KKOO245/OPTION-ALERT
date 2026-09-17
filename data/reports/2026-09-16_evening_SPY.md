# 期权晚报 2026-09-16（快照 21:12 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 17.71 ↑3.0%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 759.50 → 收盘 754.05（-0.7%） ｜ 今日高 761.67 ｜ 低 749.60 ｜ 昨收 757.39 → 收盘 754.05（-0.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-23，窗口结束前不做对错判定）

Options: P/C成交量 1.23 | OI比 1.73 | ATM IV 18.4% | Skew 3.7pp | Term 0.77 | ExpMove ±0.8%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价中性（Skew 3.7pp）｜当日成交偏 Put（P/C量 1.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.23×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.73×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 13% ｜ P/C OI(近端) 41%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 13%）｜近端持仓结构中性（P/C OI 分位 41%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 09-17（1D）±0.8% ｜ 09-18（2D）±1.1% ｜ 09-21（5D）±1.3% ｜ 09-22（6D）±1.4%
   ⇒ IV–VIX Spread: +0.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,254,045,805 | GEX Change vs 上次快照 -894,779,141 | Flip: Primary Flip: 767.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 2944 / LOW 279 / INVALID 2037
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 767.21（全链重定价，覆盖 96%）
Call Wall 800（弱结构｜现价低于该位 5.7%）
最近结构参考: Flip 767（现价低于该位 1.7%）
量化视角： 负 Gamma（22.54亿，历史分位偏负区，比 87% 的交易日更负）｜负 Gamma 加深（8.95亿）｜现价位于 Flip 下方 1.72%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 759（MaxPain，仅结算参考） / 800（Call Wall，弱结构）。
• Gamma 区域：切换参考 767（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-17  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-22  C +0 / P +0 ｜ Activity LOW ｜ 6D

📆 09-17 Forward Structure
存量OI: C 67.1k / P 116.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.99 / P $2.87 ｜ ATM IV 18.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 759 ｜ Call Wall 760（+0.8%，弱）（OI 4.8k） ｜ Put Wall 737（-2.3%，弱）（OI 6.7k）
量化解读： 存量 Put 重｜ATM IV 18.4%｜历史 Rank 80%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-18（Activity LOW）仓位参考: Max Pain 757 ｜ Call Wall 790（+4.8%，弱）（OI 57.4k） ｜ Put Wall 760（+0.8%，弱）（OI 127.0k）

09-21（Activity LOW）仓位参考: Max Pain 758 ｜ Call Wall 789（+4.6%，弱）（OI 7.0k） ｜ Put Wall 755（+0.1%）（OI 11.5k）

09-22（Activity LOW）仓位参考: Max Pain 760 ｜ Call Wall 785（+4.1%，弱）（OI 1.3k） ｜ Put Wall 760（+0.8%，弱）（OI 1.8k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/SPY_evening.json