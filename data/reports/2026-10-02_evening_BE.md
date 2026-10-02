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
🟡 **近现价集中开仓**: 10-09 300C ΔOI +543（距现价 +3.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 267.9）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 284.00 → 收盘 289.15（+1.8%） ｜ 今日高 297.59 ｜ 低 283.10 ｜ 昨收 277.58 → 收盘 289.15（+4.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.53 | OI比 1.16 | ATM IV 111.9% | Skew -8.3pp | Term 0.69 | ExpMove ±7.0%（近端） | Rank 71%
量化视角： IV 中性（Rank 71%）｜期限结构倒挂（Term 0.69，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.3pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.16×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（7D）±7.0% ｜ 10-16（14D）±10.1% ｜ 10-23（21D）±12.9% ｜ 10-30（28D）±17.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 9,510,827 | GEX Change vs 上次快照 -1,897,559 | Flip: Candidates 267.89 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 80%（带内） ｜ IV 有效性: VALID 496 / LOW 111 / INVALID 283
结构观察区: ≈268（全链重定价，覆盖 80%，CONDITIONAL）
Call Wall 300（弱结构｜现价低于该位 3.6%）
最近结构参考: Call Wall 300（现价低于该位 3.6%）
量化视角： 正 Gamma（951万，无历史分位）｜正 Gamma 减弱（190万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 278（MaxPain，仅结算参考）；上方 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 268（全链重定价，覆盖 80%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +2.5k / P +2.4k ｜ Activity HIGH ｜ 7D
10-16  C +4.1k / P +4.1k ｜ Activity HIGH ｜ 14D
10-23  C +0.9k / P +1.0k ｜ Activity HIGH ｜ 21D
10-30  C +0.2k / P +0.8k ｜ Activity HIGH ｜ 28D

📆 10-09 Forward Structure
存量OI: C 17.6k / P 21.5k，今日变化ΔOI: C +2.5k / P +2.4k，平值价格ATM: C $9.93 / P $10.45 ｜ ATM IV 63.4%，净 delta 敞口 97k shares
Top ΔOI: C 300 +543 ｜ C 280 +310
仓位参考: Max Pain 272 ｜ Call Wall 300（+3.8%，弱）（OI 1.6k） ｜ Put Wall 290（+0.3%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 63.4%｜历史 Rank 71%（近端代理）｜IV/RV 0.79×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 97,430 股

📆 10-16 Forward Structure
存量OI: C 77.3k / P 84.6k，今日变化ΔOI: C +4.1k / P +4.1k，平值价格ATM: C $14.63 / P $14.45 ｜ ATM IV 65.4%，净 delta 敞口 155k shares
Top ΔOI: P 275 +2,989 ｜ C 277 +1,920 ｜ C 275 +802
仓位参考: Max Pain 265 ｜ Call Wall 270（-6.6%，弱）（OI 8.3k） ｜ Put Wall 275（-4.9%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜ATM IV 65.4%｜历史 Rank 71%（近端代理）｜IV/RV 0.82×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 155,270 股

📆 10-23 Forward Structure
存量OI: C 12.2k / P 16.1k，今日变化ΔOI: C +0.9k / P +1.0k，平值价格ATM: C $19.50 / P $17.78 ｜ ATM IV 68.3%，净 delta 敞口 22k shares
Top ΔOI: C 300 +329
仓位参考: Max Pain 270 ｜ Call Wall 300（+3.8%，弱）（OI 1.4k） ｜ Put Wall 280（-3.2%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 68.3%｜历史 Rank 71%（近端代理）｜IV/RV 0.86×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 21,826 股

📆 10-30 Forward Structure
存量OI: C 8.6k / P 16.9k，今日变化ΔOI: C +0.2k / P +0.8k，平值价格ATM: C $25.40 / P $24.00 ｜ ATM IV 77.0%，净 delta 敞口 -4k shares
Top ΔOI: P 250 +116
仓位参考: Max Pain 285 ｜ Call Wall 300（+3.8%，弱）（OI 1.2k） ｜ Put Wall 285（-1.4%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 77.0%｜历史 Rank 71%（近端代理）｜IV/RV 0.97×（近似）｜净 delta 敞口 负 4,397 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-02/BE_evening.json