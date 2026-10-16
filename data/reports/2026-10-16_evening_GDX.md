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
🟡 **近现价集中开仓**: 10-19 89C ΔOI +97（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 91C ΔOI +8,029 占该期限总 OI 13.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 85.5）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 86.61 → 收盘 87.71（+1.3%） ｜ 今日高 89.22 ｜ 低 86.36 ｜ 昨收 87.02 → 收盘 87.71（+0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.06 | OI比 0.67 | ATM IV 44.5% | Skew 8.3pp | Term 0.94 | ExpMove ±2.1%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构正常（Term 0.94）｜保护溢价显著（Skew 8.3pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.67）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.06×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-19（3D）±2.1% ｜ 10-21（5D）±4.0% ｜ 10-23（7D）±3.7% ｜ 10-26（10D）±3.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,563,238 | GEX Change vs 上次快照 -5,357,453 | Flip: Candidates 85.50 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 77%（带内） ｜ IV 有效性: VALID 517 / LOW 162 / INVALID 497
结构观察区: ≈86（全链重定价，覆盖 77%，CONDITIONAL）
最近结构参考: Flip 86（现价高于该位 2.6%）
量化视角： 正 Gamma（2356万，无历史分位）｜正 Gamma 减弱（536万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 88（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 86（全链重定价，覆盖 77%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-19  C +0.4k / P +0.3k ｜ Activity HIGH ｜ 3D
10-21  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 5D
10-23  C +18.2k / P +6.4k ｜ Activity HIGH ｜ 7D
10-26  C +0.7k / P +4 ｜ Activity HIGH ｜ 10D

📆 10-19 Forward Structure
存量OI: C 3.1k / P 1.0k，今日变化ΔOI: C +0.4k / P +0.3k，平值价格ATM: C $0.74 / P $1.08 ｜ ATM IV 28.8%，净 delta 敞口 22k shares
Top ΔOI: C 87 +323 ｜ C 86 +101 ｜ C 89 +97
仓位参考: Max Pain 87 ｜ Call Wall 87（-0.8%，弱）（OI 0.9k） ｜ Put Wall 89（+1.5%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 28.8%｜历史 Rank 70%（近端代理）｜IV/RV 0.74×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 21,863 股

📆 10-21 Forward Structure
存量OI: C 3.2k / P 4.0k，今日变化ΔOI: C +0.3k / P +0.2k，平值价格ATM: C $1.34 / P $2.15 ｜ ATM IV 36.7%，净 delta 敞口 8k shares
Top ΔOI: C 91 +130 ｜ C 88 +67 ｜ C 86 +61
仓位参考: Max Pain 85
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 36.7%｜历史 Rank 70%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 正 7,982 股

📆 10-23 Forward Structure
存量OI: C 33.6k / P 24.4k，今日变化ΔOI: C +18.2k / P +6.4k，平值价格ATM: C $1.89 / P $1.39 ｜ ATM IV 41.2%，净 delta 敞口 636k shares
Top ΔOI: C 91 +8,029 ｜ C 88 +7,922 ｜ P 80 +2,023
仓位参考: Max Pain 86 ｜ Call Wall 91（+3.8%，弱）（OI 8.4k） ｜ Put Wall 85（-3.1%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 41.2%｜历史 Rank 70%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 636,134 股

📆 10-26 Forward Structure
存量OI: C 1.1k / P 0.9k，今日变化ΔOI: C +0.7k / P +4，平值价格ATM: C $1.69 / P $1.50 ｜ ATM IV 36.9%，净 delta 敞口 24k shares
Top ΔOI: C 92 +410 ｜ C 90 +121 ｜ C 86 +81
仓位参考: Max Pain 83 ｜ Call Wall 92（+4.9%）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 36.9%｜历史 Rank 70%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 正 23,536 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-16/GDX_evening.json