# 期权晚报 2026-10-16（快照 16:40 ET）

📊 市场环境

SPY $763.25 ｜ QQQ $709.80
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
🟡 **近现价集中开仓**: 10-23 13C ΔOI +95（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 15C ΔOI +196 占该期限总 OI 24.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 13.43 → 收盘 12.88（-4.1%） ｜ 今日高 13.83 ｜ 低 12.67 ｜ 昨收 13.59 → 收盘 12.88（-5.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.04 | OI比 0.16 | ATM IV 89.2% | Skew 14.3pp | Term 0.85 | ExpMove ±10.6%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价显著（Skew 14.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.16）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.04×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.16×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（7D）±10.6% ｜ 10-30（14D）±11.4% ｜ 11-06（21D）±26.4% ｜ 11-13（28D）±18.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 76,848 | GEX Change vs 上次快照 -644,129 | Flip: Primary Flip: 12.49（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 89%（带内） ｜ IV 有效性: VALID 165 / LOW 104 / INVALID 147
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 12.49（全链重定价，覆盖 89%）
Put Wall 14（弱结构｜现价低于该位 8.0%）
最近结构参考: Flip 12（现价高于该位 3.2%）
量化视角： 正 Gamma（8万，无历史分位）｜正 Gamma 减弱（64万）｜现价位于 Flip 上方 3.16%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall，弱结构） / 15（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 12（全链重定价，覆盖 89%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0.3k / P +20 ｜ Activity HIGH ｜ 7D
10-30  C +74 / P +86 ｜ Activity HIGH ｜ 14D
11-06  C +46 / P +16 ｜ Activity MEDIUM △ ｜ 21D
11-13  C +0.3k / P +69 ｜ Activity HIGH ｜ 28D

📆 10-23 Forward Structure
存量OI: C 5.7k / P 1.8k，今日变化ΔOI: C +0.3k / P +20，平值价格ATM: C $0.90 / P $0.47 ｜ ATM IV 73.3%，净 delta 敞口 10k shares
Top ΔOI: C 13 +95 ｜ C 14 +64
仓位参考: Max Pain 16 ｜ Put Wall 14（+8.7%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 73.3%｜历史 Rank 22%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 正 9,575 股

📆 10-30 Forward Structure
存量OI: C 6.4k / P 1.0k，今日变化ΔOI: C +74 / P +86，平值价格ATM: C $0.75 / P $0.72 ｜ ATM IV 73.6%，净 delta 敞口 3k shares
Top ΔOI: P 12 +58 ｜ C 13 +41 ｜ C 14 +33
仓位参考: Max Pain 15 ｜ Put Wall 14（+8.7%）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.6%｜历史 Rank 22%（近端代理）｜IV/RV 1.30×（近似）｜净 delta 敞口 正 2,776 股

11-06（MEDIUM △）Top ΔOI: 12C +8
11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（+0.9%，弱）（OI 76）

📆 11-13 Forward Structure
存量OI: C 0.6k / P 0.2k，今日变化ΔOI: C +0.3k / P +69，平值价格ATM: C $1.28 / P $1.05 ｜ ATM IV 75.6%，净 delta 敞口 9k shares
Top ΔOI: C 13 +47
仓位参考: Max Pain 14 ｜ Call Wall 13.5（+4.8%，弱）（OI 50） ｜ Put Wall 13（+0.9%，弱）（OI 21）
量化解读： 存量 Call 重｜ATM IV 75.6%｜历史 Rank 22%（近端代理）｜IV/RV 1.34×（近似）｜净 delta 敞口 正 9,087 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/NNE_evening.json