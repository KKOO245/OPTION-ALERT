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

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 51.4% vs 09-21 39.8%（差 +11.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 58.35 → 收盘 57.05（-2.2%） ｜ 今日高 58.63 ｜ 低 56.28 ｜ 昨收 57.53 → 收盘 57.05（-0.8%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-23，窗口结束前不做对错判定）

Options: P/C成交量 0.83 | OI比 0.48 | ATM IV 51.4% | Skew 2.9pp | Term 0.81 | ExpMove ±3.1%（近端） | Rank 84%
量化视角： IV 历史高位（Rank 84%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价中性（Skew 2.9pp）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±3.1% ｜ 09-21（5D）±3.7% ｜ 09-23（7D）±4.4% ｜ 09-25（9D）±5.4%
   ⇒ IV–VIX Spread: +33.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,493,298 | GEX Change vs 上次快照 -63,691,194 | Flip: Primary Flip: 56.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 864 / LOW 191 / INVALID 461
结构观察区: Primary Flip 56.69（全链重定价，覆盖 92%）
最近结构参考: Flip 57（现价高于该位 0.6%）
量化视角： 正 Gamma（1149万，无历史分位）｜正 Gamma 减弱（6369万）｜现价位于 Flip 上方 0.64%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 59（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-21  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-18 Forward Structure
存量OI: C 978.0k / P 467.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.91 / P $0.84 ｜ ATM IV 51.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 59 ｜ Call Wall 60（+5.2%，弱）（OI 43.5k） ｜ Put Wall 55（-3.6%，弱）（OI 24.2k）
量化解读： 存量 Call 重｜ATM IV 51.4%｜历史 Rank 84%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-21（Activity LOW）仓位参考: Max Pain 57 ｜ Call Wall 57（-0.1%）（OI 3.2k） ｜ Put Wall 54（-5.3%，弱）（OI 0.6k）

09-23（Activity LOW）仓位参考: Max Pain 59 ｜ Call Wall 61.5（+7.8%，弱）（OI 0.5k） ｜ Put Wall 55（-3.6%，弱）（OI 1.3k）

09-25（Activity LOW）仓位参考: Max Pain 60 ｜ Put Wall 55（-3.6%，弱）（OI 5.2k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 51.4% vs 09-21 39.8%（差 +11.6pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/SLV_evening.json