# 期权晚报 2026-10-16（快照 21:00 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $nan
VIX 19.99 ↑21.4%（5D +34.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 17.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 86.61 → 收盘 87.71（+1.3%） ｜ 今日高 89.22 ｜ 低 86.36 ｜ 昨收 87.02 → 收盘 87.71（+0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.67 | OI比 0.34 | ATM IV 28.8% | Skew 2.4pp | Term 1.45 | ExpMove ±2.1%（近端） | Rank 8%
量化视角： IV 历史低位（Rank 8%，期权偏便宜）｜期限结构正常偏陡（Term 1.45）｜保护溢价中性（Skew 2.4pp）｜存量 Call 偏重（OI比 0.34）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.34×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-19（3D）±2.1% ｜ 10-21（5D）±4.0% ｜ 10-23（7D）±3.7% ｜ 10-26（10D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,001,757 | GEX Change vs 上次快照 -21,918,933 | Flip: Primary Flip: 86.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 499 / LOW 123 / INVALID 382
结构观察区: Primary Flip 86.53（全链重定价，覆盖 99%）
Call Wall 91（弱结构｜现价低于该位 3.6%）
最近结构参考: Flip 87（现价高于该位 1.4%）
量化视角： 正 Gamma（700万，无历史分位）｜正 Gamma 减弱（2192万）｜现价位于 Flip 上方 1.37%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 87（MaxPain，仅结算参考）；上方 91（Call Wall，弱结构）。
• Gamma 区域：切换参考 87（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +0 / P +0 ｜ Activity LOW ｜ 3D
10-21  C +0 / P +0 ｜ Activity LOW ｜ 5D
10-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-26  C +0 / P +0 ｜ Activity LOW ｜ 10D

📆 10-19 Forward Structure
存量OI: C 3.1k / P 1.0k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.74 / P $1.08 ｜ ATM IV 28.8%，净 delta 敞口 0 shares
仓位参考: Max Pain 87 ｜ Call Wall 87（-0.8%，弱）（OI 0.9k） ｜ Put Wall 89（+1.5%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 28.8%｜历史 Rank 8%（近端代理）｜IV/RV 0.74×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 0 股

10-21（Activity LOW）仓位参考: Max Pain 85

10-23（Activity LOW）仓位参考: Max Pain 86 ｜ Call Wall 91（+3.8%，弱）（OI 8.4k） ｜ Put Wall 85（-3.1%，弱）（OI 2.1k）

10-26（Activity LOW）仓位参考: Max Pain 83 ｜ Call Wall 92（+4.9%）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/GDX_evening.json