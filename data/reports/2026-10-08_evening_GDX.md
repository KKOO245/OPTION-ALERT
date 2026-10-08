# 期权晚报 2026-10-08（快照 16:40 ET）

📊 市场环境

SPY $773.93 ｜ QQQ $747.58
VIX 15.41 ↑2.2%（5D -6.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 84P ΔOI -2,159（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-21 95C ΔOI +401 占该期限总 OI 58.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 85.41 → 收盘 86.72（+1.5%） ｜ 今日高 87.12 ｜ 低 85.03 ｜ 昨收 85.46 → 收盘 86.72（+1.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.23 | OI比 0.31 | ATM IV 43.7% | Skew -1.5pp | Term 0.93 | ExpMove ±1.8%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -1.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.23×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±1.8% ｜ 10-16（8D）±4.7% ｜ 10-19（11D）±4.7% ｜ 10-21（13D）±6.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 38,484,922 | GEX Change vs 上次快照 18,787,579 | Flip: Primary Flip: 85.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 446 / LOW 153 / INVALID 375
结构观察区: Primary Flip 85.65（全链重定价，覆盖 92%）
Put Wall 85（弱结构｜现价高于该位 2.0%） | Call Wall 90（弱结构｜现价低于该位 3.6%）
最近结构参考: Flip 86（现价高于该位 1.2%）
量化视角： 正 Gamma（3848万，无历史分位）｜正 Gamma 增强（+1879万）｜现价位于 Flip 上方 1.25%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（Put Wall，弱结构）；上方 87（MaxPain，仅结算参考） / 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 86（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +0.7k / P -1.3k ｜ Activity MEDIUM △ ｜ 1D
10-16  C +5.7k / P -6.3k ｜ Activity HIGH ｜ 8D
10-19  C +89 / P +18 ｜ Activity HIGH ｜ 11D
10-21  C +0.6k / P +93 ｜ Activity HIGH ｜ 13D

📆 10-09 Forward Structure
存量OI: C 97.4k / P 30.6k，今日变化ΔOI: C +0.7k / P -1.3k，平值价格ATM: C $0.63 / P $0.90 ｜ ATM IV 43.8%，净 delta 敞口 243k shares
Top ΔOI: P 94 -1,280 ｜ C 92 -613 ｜ C 88 +374
仓位参考: Max Pain 87 ｜ Call Wall 88（+1.5%，弱）（OI 16.7k） ｜ Put Wall 82（-5.4%，弱）（OI 6.8k）
量化解读： 存量 Call 重｜ATM IV 43.8%｜历史 Rank 69%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 243,301 股

📆 10-16 Forward Structure
存量OI: C 112.7k / P 109.2k，今日变化ΔOI: C +5.7k / P -6.3k，平值价格ATM: C $1.89 / P $2.19 ｜ ATM IV 41.0%，净 delta 敞口 599k shares
Top ΔOI: P 84 -2,159 ｜ C 89 +1,772 ｜ P 100 -1,043
仓位参考: Max Pain 90 ｜ Call Wall 90（+3.8%，弱）（OI 10.0k） ｜ Put Wall 90（+3.8%，弱）（OI 10.4k）
量化解读： 存量两侧均衡｜ATM IV 41.0%｜历史 Rank 69%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 598,831 股

📆 10-19 Forward Structure
存量OI: C 0.2k / P 0.1k，今日变化ΔOI: C +89 / P +18，平值价格ATM: C $1.85 / P $2.22 ｜ ATM IV 36.2%，净 delta 敞口 4k shares
Top ΔOI: C 91 +22 ｜ C 90 +12 ｜ C 84 +9
仓位参考: Max Pain 88 ｜ Call Wall 91（+4.9%，弱）（OI 26） ｜ Put Wall 90（+3.8%，弱）（OI 23）
量化解读： 存量 Call 重｜ATM IV 36.2%｜历史 Rank 69%（近端代理）｜IV/RV 1.03×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 4,358 股

📆 10-21 Forward Structure
存量OI: C 0.6k / P 0.1k，今日变化ΔOI: C +0.6k / P +93，平值价格ATM: C $2.23 / P $3.38 ｜ ATM IV 38.7%，净 delta 敞口 8k shares
Top ΔOI: C 95 +401
仓位参考: Max Pain 85 ｜ Put Wall 85（-2.0%，弱）（OI 14）
量化解读： 存量 Call 重｜ATM IV 38.7%｜历史 Rank 69%（近端代理）｜IV/RV 1.11×（近似）｜净 delta 敞口 正 7,730 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/GDX_evening.json