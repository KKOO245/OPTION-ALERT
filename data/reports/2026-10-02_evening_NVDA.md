# 期权晚报 2026-10-02（快照 16:40 ET）

📊 市场环境

SPY $769.64 ｜ QQQ $749.58
VIX 15.31 ↓6.6%（5D +3.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 29 ｜ 前值 133　✅ 今日已公布
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 4.2 ｜ 前值 4.1　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-05 245C ΔOI +5,566（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 236.05 → 收盘 233.95（-0.9%） ｜ 今日高 237.87 ｜ 低 233.60 ｜ 昨收 230.86 → 收盘 233.95（+1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.54 | OI比 0.79 | ATM IV 32.5% | Skew -5.2pp | Term 0.89 | ExpMove ±1.4%（近端） | Rank 12%
量化视角： IV 历史低位（Rank 12%，期权偏便宜）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-05（3D）±1.4% ｜ 10-07（5D）±2.3% ｜ 10-09（7D）±2.9% ｜ 10-12（10D）±3.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 629,544,422 | GEX Change vs 上次快照 -180,199,050 | Flip: Primary Flip: 216.15（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 626 / LOW 201 / INVALID 493
结构观察区: Primary Flip 216.15（全链重定价，覆盖 87%）
Call Wall 250（弱结构｜现价低于该位 6.4%）
最近结构参考: Call Wall 250（现价低于该位 6.4%）
量化视角： 正 Gamma（6.30亿，无历史分位）｜正 Gamma 减弱（1.80亿）｜现价位于 Flip 上方 8.24%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 228（MaxPain，仅结算参考）；上方 250（Call Wall，弱结构）。
• Gamma 区域：切换参考 216（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-05  C +24.0k / P +23.3k ｜ Activity HIGH ｜ 3D
10-07  C +15.8k / P +7.8k ｜ Activity HIGH ｜ 5D
10-09  C +57.2k / P +49.2k ｜ Activity HIGH ｜ 7D
10-12  C +3.0k / P +1.6k ｜ Activity HIGH ｜ 10D

📆 10-05 Forward Structure
存量OI: C 73.3k / P 62.3k，今日变化ΔOI: C +24.0k / P +23.3k，平值价格ATM: C $1.13 / P $2.20 ｜ ATM IV 18.6%，净 delta 敞口 434k shares
Top ΔOI: C 245 +5,566
仓位参考: Max Pain 228 ｜ Call Wall 235（+0.4%）（OI 13.9k） ｜ Put Wall 220（-6.0%，弱）（OI 5.7k）
量化解读： 存量 Call 重｜ATM IV 18.6%｜历史 Rank 12%（近端代理）｜IV/RV 0.81×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 434,481 股

📆 10-07 Forward Structure
存量OI: C 30.7k / P 23.7k，今日变化ΔOI: C +15.8k / P +7.8k，平值价格ATM: C $2.19 / P $3.25 ｜ ATM IV 24.3%，净 delta 敞口 286k shares
Top ΔOI: C 247 +3,632 ｜ P 230 +2,991 ｜ C 235 +1,611
仓位参考: Max Pain 230 ｜ Call Wall 247.5（+5.8%）（OI 7.4k） ｜ Put Wall 230（-1.7%）（OI 8.5k）
量化解读： 存量 Call 重｜ATM IV 24.3%｜历史 Rank 12%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 286,423 股

📆 10-09 Forward Structure
存量OI: C 189.8k / P 237.8k，今日变化ΔOI: C +57.2k / P +49.2k，平值价格ATM: C $3.00 / P $3.85 ｜ ATM IV 25.9%，净 delta 敞口 1.3M shares
Top ΔOI: C 235 +17,235 ｜ C 242 +15,234
仓位参考: Max Pain 228 ｜ Call Wall 235（+0.4%，弱）（OI 29.9k） ｜ Put Wall 220（-6.0%，弱）（OI 23.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 25.9%｜历史 Rank 12%（近端代理）｜IV/RV 1.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,309,235 股

📆 10-12 Forward Structure
存量OI: C 9.3k / P 4.0k，今日变化ΔOI: C +3.0k / P +1.6k，平值价格ATM: C $3.50 / P $4.19 ｜ ATM IV 24.4%，净 delta 敞口 100k shares
Top ΔOI: C 230 +708 ｜ C 247 +469 ｜ C 232 +393
仓位参考: Max Pain 230 ｜ Call Wall 240（+2.6%）（OI 2.9k） ｜ Put Wall 222.5（-4.9%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 24.4%｜历史 Rank 12%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 正 100,496 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/NVDA_evening.json