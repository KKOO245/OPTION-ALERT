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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## XBI

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
XBI: 今开 157.31 → 收盘 158.25（+0.6%） ｜ 今日高 160.33 ｜ 低 156.94 ｜ 昨收 154.18 → 收盘 158.25（+2.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-09-24，窗口结束前不做对错判定）

Options: P/C成交量 4.79 | OI比 1.31 | ATM IV 40.4% | Skew -2.7pp | Term 0.75 | ExpMove ±1.7%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.75，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.7pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 4.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 4.79×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.31×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±1.7% ｜ 09-25（8D）±3.7% ｜ 10-02（15D）±3.8% ｜ 10-09（22D）±3.4%
   ⇒ IV–VIX Spread: +24.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -48,417,131 | GEX Change vs 上次快照 -20,744,978 | Flip: Primary Flip: 162.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 389 / LOW 131 / INVALID 324
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 162.42（全链重定价，覆盖 87%）
Put Wall 150（现价高于该位 5.5%） | Call Wall 170（弱结构｜现价低于该位 6.9%）
最近结构参考: Flip 162（现价低于该位 2.6%）
量化视角： 负 Gamma（4842万，无历史分位）｜负 Gamma 加深（2074万）｜现价位于 Flip 下方 2.56%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 150（Put Wall） / 156（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 162（全链重定价，覆盖 87%）。
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
存量OI: C 79.5k / P 104.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.43 / P $1.28 ｜ ATM IV 40.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 156 ｜ Call Wall 170（+7.4%，弱）（OI 10.1k） ｜ Put Wall 150（-5.2%，弱）（OI 11.8k）
量化解读： 存量 Put 重｜ATM IV 40.4%｜历史 Rank 85%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 157 ｜ Call Wall 160（+1.1%，弱）（OI 2.3k） ｜ Put Wall 145（-8.4%，弱）（OI 15.2k）

10-02（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 165（+4.3%）（OI 0.7k） ｜ Put Wall 157（-0.8%，弱）（OI 0.2k）

10-09（Activity LOW）仓位参考: Max Pain 160 ｜ Call Wall 172（+8.7%，弱）（OI 38） ｜ Put Wall 150（-5.2%，弱）（OI 0.1k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 40.4% vs 09-25 30.9%（差 +9.5pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/XBI_evening.json