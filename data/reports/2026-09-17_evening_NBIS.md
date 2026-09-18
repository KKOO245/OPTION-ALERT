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
🟡 **事件差分**: 09-18 ATM IV 88.6% vs 09-25 75.6%（差 +13.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 230.02 → 收盘 217.99（-5.2%） ｜ 今日高 232.81 ｜ 低 209.65 ｜ 昨收 209.37 → 收盘 217.99（+4.1%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-09-22，窗口结束前不做对错判定）

Options: P/C成交量 0.36 | OI比 1.27 | ATM IV 88.6% | Skew -1.2pp | Term 0.88 | ExpMove ±3.6%（近端） | Rank 21%
量化视角： IV 历史低位（Rank 21%，期权偏便宜）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.27×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±3.6% ｜ 09-25（8D）±9.1% ｜ 10-02（15D）±12.2% ｜ 10-09（22D）±15.0%
   ⇒ IV–VIX Spread: +73.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,486,151 | GEX Change vs 上次快照 -809,051 | Flip: Primary Flip: 225.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 512 / LOW 66 / INVALID 194
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 225.03（全链重定价，覆盖 94%）
Put Wall 210（弱结构｜现价高于该位 3.8%）
最近结构参考: Flip 225（现价低于该位 3.1%）
量化视角： 负 Gamma（1049万，无历史分位）｜负 Gamma 加深（81万）｜现价位于 Flip 下方 3.13%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 210（Put Wall，弱结构）；上方 220（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 225（全链重定价，覆盖 94%）。
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
存量OI: C 142.2k / P 181.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $4.23 / P $3.70 ｜ ATM IV 88.6%，净 delta 敞口 0 shares
仓位参考: Max Pain 220 ｜ Call Wall 200（-8.3%，弱）（OI 7.0k） ｜ Put Wall 210（-3.7%，弱）（OI 10.4k）
量化解读： 存量 Put 重｜ATM IV 88.6%｜历史 Rank 21%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 215 ｜ Call Wall 227.5（+4.4%）（OI 3.0k） ｜ Put Wall 200（-8.3%，弱）（OI 2.3k）

10-02（Activity LOW）仓位参考: Max Pain 218 ｜ Call Wall 215（-1.4%，弱）（OI 0.4k） ｜ Put Wall 200（-8.3%，弱）（OI 0.8k）

10-09（Activity LOW）仓位参考: Max Pain 220 ｜ Call Wall 215（-1.4%，弱）（OI 0.4k） ｜ Put Wall 200（-8.3%，弱）（OI 0.7k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 88.6% vs 09-25 75.6%（差 +13.0pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=24 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=24）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/NBIS_evening.json