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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 09-18 ATM IV 69.9% vs 09-25 59.9%（差 +10.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 169.87 → 收盘 173.97（+2.4%） ｜ 今日高 174.15 ｜ 低 165.73 ｜ 昨收 164.51 → 收盘 173.97（+5.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.89 | OI比 0.53 | ATM IV 69.9% | Skew -4.3pp | Term 0.88 | ExpMove ±3.0%（近端） | Rank 31%
量化视角： IV 中性（Rank 31%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.53）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.89×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±3.0% ｜ 09-25（8D）±7.0% ｜ 10-02（15D）±10.3% ｜ 10-09（22D）±11.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 15,782,338 | GEX Change vs 上次快照 12,926,960 | Flip: Primary Flip: 169.32（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 460 / LOW 198 / INVALID 316
结构观察区: Primary Flip 169.32（全链重定价，覆盖 100%）
Put Wall 160（弱结构｜现价高于该位 8.7%）
最近结构参考: Flip 169（现价高于该位 2.7%）
量化视角： 正 Gamma（1578万，无历史分位）｜正 Gamma 增强（+1293万）｜现价位于 Flip 上方 2.74%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（Put Wall，弱结构）；上方 175（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 169（全链重定价，覆盖 100%）。
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
存量OI: C 227.6k / P 120.4k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.15 / P $3.10 ｜ ATM IV 69.9%，净 delta 敞口 0 shares
仓位参考: Max Pain 175 ｜ Call Wall 182.5（+4.9%，弱）（OI 10.4k） ｜ Put Wall 160（-8.0%，弱）（OI 13.7k）
量化解读： 存量 Call 重｜ATM IV 69.9%｜历史 Rank 31%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 185（+6.3%，弱）（OI 2.4k） ｜ Put Wall 165（-5.2%，弱）（OI 0.8k）

10-02（Activity LOW）仓位参考: Max Pain 185 ｜ Call Wall 187.5（+7.8%，弱）（OI 1.3k） ｜ Put Wall 172.5（-0.8%，弱）（OI 1.1k）

10-09（Activity LOW）仓位参考: Max Pain 188 ｜ Call Wall 185（+6.3%，弱）（OI 0.2k） ｜ Put Wall 160（-8.0%，弱）（OI 0.5k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 69.9% vs 09-25 59.9%（差 +10.0pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/COIN_evening.json