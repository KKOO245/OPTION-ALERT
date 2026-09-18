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


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 95.85 → 收盘 95.92（+0.1%） ｜ 今日高 96.68 ｜ 低 94.45 ｜ 昨收 92.80 → 收盘 95.92（+3.4%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.14 | OI比 1.25 | ATM IV 43.7% | Skew -3.9pp | Term 0.98 | ExpMove ±1.8%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构正常（Term 0.98）｜Put 保护异常便宜（Skew -3.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.14×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.25×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±1.8% ｜ 09-25（8D）±4.9% ｜ 10-02（15D）±6.8% ｜ 10-09（22D）±11.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 20,054,650 | GEX Change vs 上次快照 255,799 | Flip: Primary Flip: 95.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 489 / LOW 156 / INVALID 265
结构观察区: Primary Flip 95.37（全链重定价，覆盖 86%）
Call Wall 100（弱结构｜现价低于该位 4.1%）
最近结构参考: Flip 95（现价高于该位 0.6%）
量化视角： 正 Gamma（2005万，无历史分位）｜正 Gamma 增强（+26万）｜现价位于 Flip 上方 0.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 91（MaxPain，仅结算参考）；上方 100（Call Wall，弱结构）。
• Gamma 区域：切换参考 95（全链重定价，覆盖 86%）。
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
存量OI: C 341.1k / P 424.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.85 / P $0.86 ｜ ATM IV 43.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 91 ｜ Call Wall 100（+4.3%，弱）（OI 32.2k） ｜ Put Wall 90（-6.2%，弱）（OI 40.5k）
量化解读： 存量 Put 重｜ATM IV 43.7%｜历史 Rank 69%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 95 ｜ Call Wall 105（+9.5%，弱）（OI 8.1k） ｜ Put Wall 93（-3.0%，弱）（OI 3.9k）

10-02（Activity LOW）仓位参考: Max Pain 99 ｜ Call Wall 100（+4.3%，弱）（OI 3.1k） ｜ Put Wall 97（+1.1%）（OI 11.3k）

10-09（Activity LOW）仓位参考: Max Pain 94 ｜ Call Wall 94（-2.0%，弱）（OI 0.7k） ｜ Put Wall 90（-6.2%，弱）（OI 1.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/GDX_evening.json