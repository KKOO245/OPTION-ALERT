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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 194.40 → 收盘 183.00（-5.9%） ｜ 今日高 200.35 ｜ 低 180.81 ｜ 昨收 189.29 → 收盘 183.00（-3.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.41 | OI比 0.77 | ATM IV 45.4% | Skew -8.7pp | Term 1.31 | ExpMove ±5.9%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构正常偏陡（Term 1.31）｜Put 保护异常便宜（Skew -8.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（7D）±5.9% ｜ 10-16（14D）±8.6% ｜ 10-23（21D）±10.8% ｜ 10-30（28D）±13.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 9,289,566 | GEX Change vs 上次快照 -18,591,519 | Flip: Primary Flip: 169.59（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 432 / LOW 116 / INVALID 344
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 169.59（全链重定价，覆盖 84%）
Call Wall 200（现价低于该位 8.5%）
最近结构参考: Flip 170（现价高于该位 7.9%）
量化视角： 正 Gamma（929万，无历史分位）｜正 Gamma 减弱（1859万）｜现价位于 Flip 上方 7.90%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 190（MaxPain，仅结算参考） / 200（Call Wall）。
• Gamma 区域：切换参考 170（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +21.6k / P +0.7k ｜ Activity HIGH ｜ 7D
10-16  C +0.6k / P -0.2k ｜ Activity MEDIUM △ ｜ 14D
10-23  C +0.2k / P +61 ｜ Activity MEDIUM △ ｜ 21D
10-30  C +0.4k / P +0.9k ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 34.3k / P 24.4k，今日变化ΔOI: C +21.6k / P +0.7k，平值价格ATM: C $5.67 / P $5.05 ｜ ATM IV 53.2%，净 delta 敞口 339k shares
Top ΔOI: C 195 +5,200 ｜ C 202 +5,040 ｜ C 192 +4,845
仓位参考: Max Pain 190 ｜ Call Wall 200（+9.3%，弱）（OI 7.7k）
量化解读： 存量 Call 重｜ATM IV 53.2%｜历史 Rank 90%（近端代理）｜IV/RV 0.73×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 338,929 股

10-16（MEDIUM △）仓位参考: Max Pain 175 ｜ Call Wall 200（+9.3%，弱）（OI 6.3k） ｜ Put Wall 200（+9.3%，弱）（OI 3.9k）

10-23（MEDIUM △）Top ΔOI: 200C +35
10-23（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 190（+3.8%，弱）（OI 0.5k） ｜ Put Wall 165（-9.8%，弱）（OI 0.4k）

📆 10-30 Forward Structure
存量OI: C 6.1k / P 6.1k，今日变化ΔOI: C +0.4k / P +0.9k，平值价格ATM: C $12.85 / P $12.00 ｜ ATM IV 59.4%，净 delta 敞口 -2k shares
Top ΔOI: C 200 +228 ｜ P 200 +178
仓位参考: Max Pain 192 ｜ Call Wall 200（+9.3%，弱）（OI 0.5k） ｜ Put Wall 170（-7.1%，弱）（OI 0.5k）
量化解读： 存量两侧均衡｜ATM IV 59.4%｜历史 Rank 90%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 负 2,187 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/COIN_evening.json