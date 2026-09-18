# 期权晚报 2026-09-18（快照 16:40 ET）

📊 市场环境

SPY $761.69 ｜ QQQ $721.45
VIX 14.81 ↓4.1%（5D -6.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 29.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-02 175C ΔOI +983（距现价 -1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 165.6）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📌 周末待办：
• 每周同步：cd D:\git\Option Alert-数据储存；git pull


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 177.04 → 收盘 177.64（+0.3%） ｜ 今日高 177.75 ｜ 低 172.00 ｜ 昨收 176.24 → 收盘 177.64（+0.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.52 | OI比 0.83 | ATM IV 43.9% | Skew -1.4pp | Term 1.05 | ExpMove ±4.9%（近端） | Rank 22%
量化视角： IV 历史低位（Rank 22%，期权偏便宜）｜期限结构正常（Term 1.05）｜Put 保护异常便宜（Skew -1.4pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.83）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.83×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-25（7D）±4.9% ｜ 10-02（14D）±7.0% ｜ 10-09（21D）±8.8% ｜ 10-16（28D）±10.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 72,172,919 | GEX Change vs 上次快照 -11,157,880 | Flip: Candidates 165.63 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 76%（带内） ｜ IV 有效性: VALID 505 / LOW 85 / INVALID 246
结构观察区: ≈166（全链重定价，覆盖 76%，CONDITIONAL）
Call Wall 180（弱结构｜现价低于该位 1.3%）
最近结构参考: Call Wall 180（现价低于该位 1.3%）
量化视角： 正 Gamma（7217万，无历史分位）｜正 Gamma 减弱（1116万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 160（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 166（全链重定价，覆盖 76%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +6.5k / P +12.6k ｜ Activity HIGH ｜ 7D
10-02  C +3.9k / P +1.0k ｜ Activity HIGH ｜ 14D
10-09  C +0.5k / P +4.1k ｜ Activity HIGH ｜ 21D
10-16  C +1.8k / P +8.5k ｜ Activity HIGH ｜ 28D

📆 09-25 Forward Structure
存量OI: C 47.9k / P 59.9k，今日变化ΔOI: C +6.5k / P +12.6k，平值价格ATM: C $4.43 / P $4.30 ｜ ATM IV 44.1%，净 delta 敞口 6k shares
Top ΔOI: P 165 +1,812 ｜ P 160 +1,507
仓位参考: Max Pain 172 ｜ Call Wall 190（+7.0%，弱）（OI 6.0k） ｜ Put Wall 170（-4.3%，弱）（OI 5.6k）
量化解读： 存量 Put 重｜ATM IV 44.1%｜历史 Rank 22%（近端代理）｜净 delta 敞口 正 5,616 股

📆 10-02 Forward Structure
存量OI: C 24.5k / P 26.1k，今日变化ΔOI: C +3.9k / P +1.0k，平值价格ATM: C $6.30 / P $6.20 ｜ ATM IV 45.4%，净 delta 敞口 129k shares
Top ΔOI: C 175 +983 ｜ C 187 +672
仓位参考: Max Pain 172 ｜ Call Wall 180（+1.3%，弱）（OI 3.1k） ｜ Put Wall 170（-4.3%）（OI 4.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 45.4%｜历史 Rank 22%（近端代理）｜净 delta 敞口 正 129,209 股

📆 10-09 Forward Structure
存量OI: C 11.2k / P 20.1k，今日变化ΔOI: C +0.5k / P +4.1k，平值价格ATM: C $8.02 / P $7.65 ｜ ATM IV 45.7%，净 delta 敞口 -22k shares
Top ΔOI: P 170 +329 ｜ P 172 +312
仓位参考: Max Pain 172 ｜ Call Wall 190（+7.0%，弱）（OI 0.8k） ｜ Put Wall 170（-4.3%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 45.7%｜历史 Rank 22%（近端代理）｜净 delta 敞口 负 21,613 股

📆 10-16 Forward Structure
存量OI: C 127.0k / P 151.6k，今日变化ΔOI: C +1.8k / P +8.5k，平值价格ATM: C $8.25 / P $10.10 ｜ ATM IV 46.0%，净 delta 敞口 -13k shares
Top ΔOI: P 100 +6,959 ｜ P 170 +994 ｜ C 200 +709
仓位参考: Max Pain 160 ｜ Call Wall 170（-4.3%）（OI 16.4k） ｜ Put Wall 170（-4.3%，弱）（OI 14.7k）
量化解读： 存量 Put 重｜ATM IV 46.0%｜历史 Rank 22%（近端代理）｜净 delta 敞口 负 13,315 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-18/PLTR_evening.json