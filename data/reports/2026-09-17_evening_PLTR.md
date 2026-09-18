# 期权晚报 2026-09-17（快照 21:08 ET）

📊 市场环境

SPY $762.60 ｜ QQQ $nan
VIX 15.44 ↓12.8%（5D -13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 1.275 ｜ 前值 1.309　✅ 今日已公布
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 1.394 ｜ 前值 1.433　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 175.76 → 收盘 176.24（+0.3%） ｜ 今日高 177.88 ｜ 低 172.61 ｜ 昨收 174.34 → 收盘 176.24（+1.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.47 | OI比 0.84 | ATM IV 51.7% | Skew 0.4pp | Term 0.91 | ExpMove ±2.2%（近端） | Rank 28%
量化视角： IV 中性（Rank 28%）｜期限结构正常（Term 0.91）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-18（1D）±2.2% ｜ 09-25（8D）±5.5% ｜ 10-02（15D）±7.6% ｜ 10-09（22D）±9.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 111,390,913 | GEX Change vs 上次快照 5,694,833 | Flip: Primary Flip: 167.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 562 / LOW 109 / INVALID 149
结构观察区: Primary Flip 167.05（全链重定价，覆盖 98%）
Put Wall 170（弱结构｜现价高于该位 3.7%） | Call Wall 180（弱结构｜现价低于该位 2.1%）
最近结构参考: Call Wall 180（现价低于该位 2.1%）
量化视角： 正 Gamma（1.11亿，无历史分位）｜正 Gamma 增强（+569万）｜现价位于 Flip 上方 5.50%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 170（Put Wall，弱结构） / 160（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 167（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 1D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 8D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 15D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 22D

📆 09-18 Forward Structure
存量OI: C 350.5k / P 295.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.62 / P $1.34 ｜ ATM IV 51.7%，净 delta 敞口 0 shares
仓位参考: Max Pain 160 ｜ Call Wall 180（+2.1%）（OI 33.1k） ｜ Put Wall 160（-9.2%，弱）（OI 18.9k）
量化解读： 存量 Call 重｜ATM IV 51.7%｜历史 Rank 28%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 172 ｜ Call Wall 190（+7.8%，弱）（OI 4.8k） ｜ Put Wall 170（-3.5%，弱）（OI 4.6k）

10-02（Activity LOW）仓位参考: Max Pain 172 ｜ Call Wall 180（+2.1%，弱）（OI 2.9k） ｜ Put Wall 170（-3.5%）（OI 4.5k）

10-09（Activity LOW）仓位参考: Max Pain 170 ｜ Call Wall 190（+7.8%，弱）（OI 0.7k） ｜ Put Wall 170（-3.5%，弱）（OI 3.1k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 51.7% vs 09-25 46.5%（差 +5.2pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/PLTR_evening.json