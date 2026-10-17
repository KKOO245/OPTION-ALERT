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

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 13.43 → 收盘 12.88（-4.1%） ｜ 今日高 13.83 ｜ 低 12.67 ｜ 昨收 13.59 → 收盘 12.88（-5.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.36 | OI比 0.31 | ATM IV 73.3% | Skew 2.3pp | Term 1.03 | ExpMove ±10.6%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常（Term 1.03）｜保护溢价中性（Skew 2.3pp）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±10.6% ｜ 10-30（14D）±11.4% ｜ 11-06（21D）±26.4% ｜ 11-13（28D）±18.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 302,777 | GEX Change vs 上次快照 -418,199 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 144 / LOW 69 / INVALID 99
结构观察区: NO_CROSS
Put Wall 14（现价低于该位 8.0%）
最近结构参考: Put Wall 14（现价低于该位 8.0%）
量化视角： 正 Gamma（30万，无历史分位）｜正 Gamma 减弱（42万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall） / 16（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-30  C +0 / P +0 ｜ Activity LOW ｜ 14D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 21D
11-13  C +0 / P +0 ｜ Activity LOW ｜ 28D

📆 10-23 Forward Structure
存量OI: C 5.7k / P 1.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $0.90 / P $0.47 ｜ ATM IV 73.3%，净 delta 敞口 0 shares
仓位参考: Max Pain 16 ｜ Put Wall 14（+8.7%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 73.3%｜历史 Rank 5%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 正 0 股

10-30（Activity LOW）仓位参考: Max Pain 15 ｜ Put Wall 14（+8.7%）（OI 0.4k）

11-06（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 13（+0.9%，弱）（OI 76）

11-13（Activity LOW）仓位参考: Max Pain 14 ｜ Call Wall 13.5（+4.8%，弱）（OI 50） ｜ Put Wall 13（+0.9%，弱）（OI 21）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/NNE_evening.json