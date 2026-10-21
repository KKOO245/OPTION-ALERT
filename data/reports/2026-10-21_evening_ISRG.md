# 期权晚报 2026-10-21（快照 16:40 ET）

📊 市场环境

SPY $773.09 ｜ QQQ $725.20
VIX 16.68 ↓3.6%（5D -1.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 402.49 → 收盘 428.12（+6.4%） ｜ 今日高 432.75 ｜ 低 398.99 ｜ 昨收 438.00 → 收盘 428.12（-2.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.11 | OI比 1.01 | ATM IV 42.6% | Skew -3.5pp | Term 0.78 | ExpMove ±3.0%（近端） | Rank 65%
量化视角： IV 中性（Rank 65%）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±3.0% ｜ 10-30（9D）±5.3% ｜ 11-06（16D）±5.4% ｜ 11-13（23D）±6.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,451,042 | GEX Change vs 上次快照 2,309,387 | Flip: Primary Flip: 422.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 320 / LOW 199 / INVALID 447
结构观察区: Primary Flip 422.42（全链重定价，覆盖 91%）
最近结构参考: Flip 422（现价高于该位 1.3%）
量化视角： 正 Gamma（145万，无历史分位）｜由负转正（+231万）｜现价位于 Flip 上方 1.35%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 425（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 422（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +3.2k / P +3.8k ｜ Activity HIGH ｜ 2D
10-30  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 9D
11-06  C +20 / P +85 ｜ Activity HIGH ｜ 16D
11-13  C +35 / P +47 ｜ Activity MEDIUM △ ｜ 23D

📆 10-23 Forward Structure
存量OI: C 8.6k / P 8.7k，今日变化ΔOI: C +3.2k / P +3.8k，平值价格ATM: C $7.80 / P $4.93 ｜ ATM IV 42.6%，净 delta 敞口 -46k shares
Top ΔOI: P 390 +526 ｜ P 400 +347
仓位参考: Max Pain 425 ｜ Call Wall 450（+5.1%，弱）（OI 0.7k） ｜ Put Wall 400（-6.6%，弱）（OI 0.8k）
量化解读： 存量两侧均衡｜ATM IV 42.6%｜历史 Rank 65%（近端代理）｜IV/RV 1.83×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 46,242 股

📆 10-30 Forward Structure
存量OI: C 1.8k / P 1.2k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $11.60 / P $11.06 ｜ ATM IV 30.3%，净 delta 敞口 -2k shares
Top ΔOI: P 397 +101
仓位参考: Max Pain 410 ｜ Call Wall 450（+5.1%，弱）（OI 0.1k） ｜ Put Wall 397.5（-7.2%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 30.3%｜历史 Rank 65%（近端代理）｜IV/RV 1.30×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 2,328 股

📆 11-06 Forward Structure
存量OI: C 0.4k / P 0.5k，今日变化ΔOI: C +20 / P +85，平值价格ATM: C $11.60 / P $11.60 ｜ ATM IV 34.2%，净 delta 敞口 -2k shares
Top ΔOI: P 400 +33 ｜ P 405 +31 ｜ P 437 +21
仓位参考: Max Pain 420 ｜ Call Wall 455（+6.3%，弱）（OI 54） ｜ Put Wall 400（-6.6%，弱）（OI 65）
量化解读： 存量两侧均衡｜ATM IV 34.2%｜历史 Rank 65%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,940 股

11-13（MEDIUM △）Top ΔOI: 400P +26 ｜ 395P +7
11-13（MEDIUM △）仓位参考: Max Pain 420 ｜ Call Wall 410（-4.2%，弱）（OI 26） ｜ Put Wall 420（-1.9%，弱）（OI 68）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/ISRG_evening.json