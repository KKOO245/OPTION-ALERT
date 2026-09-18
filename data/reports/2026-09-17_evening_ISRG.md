# 期权晚报 2026-09-17（快照 21:08 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.44 ↓12.8%（5D -13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 09-18（1D）ATM IV 54.5% vs 09-25 35.8%（差 +18.7pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 385.01 → 收盘 383.54（-0.4%） ｜ 今日高 388.20 ｜ 低 378.28 ｜ 昨收 382.29 → 收盘 383.54（+0.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-24，窗口结束前不做对错判定）

Options: P/C成交量 4.74 | OI比 0.92 | ATM IV 54.5% | Skew 1.5pp | Term 0.70 | ExpMove ±2.0%（近端） | Rank 88%
量化视角： IV 历史高位（Rank 88%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价薄（Skew 1.5pp）｜当日成交偏 Put（P/C量 4.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 4.74×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（1D）±2.0% ｜ 09-25（8D）±4.9% ｜ 10-02（15D）±5.4% ｜ 10-09（22D）±6.7%
   ⇒ IV–VIX Spread: +39.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,228,578 | GEX Change vs 上次快照 1,528,268 | Flip: Primary Flip: 380.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 82%（带内） ｜ IV 有效性: VALID 244 / LOW 231 / INVALID 465
结构观察区: Primary Flip 380.30（全链重定价，覆盖 82%）
Put Wall 350（弱结构｜现价高于该位 9.6%） | Call Wall 400（弱结构｜现价低于该位 4.1%）
最近结构参考: Flip 380（现价高于该位 0.9%）
量化视角： 正 Gamma（123万，无历史分位）｜由负转正（+153万）｜现价位于 Flip 上方 0.85%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 350（Put Wall，弱结构） / 372（MaxPain，仅结算参考）；上方 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 380（全链重定价，覆盖 82%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 8D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 15D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 09-18 Forward Structure
存量OI: C 16.5k / P 15.1k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $5.33 / P $2.42 ｜ ATM IV 54.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 372 ｜ Call Wall 400（+4.3%，弱）（OI 1.1k） ｜ Put Wall 350（-8.7%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 54.5%｜历史 Rank 88%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 370 ｜ Call Wall 405（+5.6%，弱）（OI 0.2k） ｜ Put Wall 360（-6.1%，弱）（OI 0.2k）

10-02（Activity LOW）仓位参考: Max Pain 365 ｜ Call Wall 405（+5.6%）（OI 79）

10-09（Activity LOW）仓位参考: Max Pain 380 ｜ Call Wall 380（-0.9%）（OI 0.1k） ｜ Put Wall 385（+0.4%）（OI 0.2k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 54.5% vs 09-25 35.8%（差 +18.7pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/ISRG_evening.json