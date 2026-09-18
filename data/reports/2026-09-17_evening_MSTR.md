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

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 75.2% vs 09-25 64.7%（差 +10.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 129.88 → 收盘 132.25（+1.8%） ｜ 今日高 133.42 ｜ 低 127.82 ｜ 昨收 126.18 → 收盘 132.25（+4.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.61 | OI比 0.59 | ATM IV 75.2% | Skew -8.2pp | Term 0.86 | ExpMove ±3.2%（近端） | Rank 39%
量化视角： IV 中性（Rank 39%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.59）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.59×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（1D）±3.2% ｜ 09-25（8D）±7.7% ｜ 10-02（15D）±10.5% ｜ 10-09（22D）±12.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 84,533,971 | GEX Change vs 上次快照 34,469,714 | Flip: Primary Flip: 124.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 784 / LOW 115 / INVALID 299
结构观察区: Primary Flip 124.91（全链重定价，覆盖 100%）
最近结构参考: Flip 125（现价高于该位 5.9%）
量化视角： 正 Gamma（8453万，无历史分位）｜正 Gamma 增强（+3447万）｜现价位于 Flip 上方 5.87%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 120（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 125（全链重定价，覆盖 100%）。
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
存量OI: C 484.0k / P 283.2k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.28 / P $1.93 ｜ ATM IV 75.2%，净 delta 敞口 0 shares
仓位参考: Max Pain 120 ｜ Call Wall 145（+9.6%，弱）（OI 29.0k） ｜ Put Wall 125（-5.5%，弱）（OI 9.7k）
量化解读： 存量 Call 重｜ATM IV 75.2%｜历史 Rank 39%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 127 ｜ Call Wall 132（-0.2%，弱）（OI 2.5k） ｜ Put Wall 120（-9.3%，弱）（OI 3.1k）

10-02（Activity LOW）仓位参考: Max Pain 130 ｜ Call Wall 145（+9.6%，弱）（OI 2.8k） ｜ Put Wall 130（-1.7%，弱）（OI 2.7k）

10-09（Activity LOW）仓位参考: Max Pain 135 ｜ Call Wall 140（+5.9%，弱）（OI 1.2k） ｜ Put Wall 130（-1.7%，弱）（OI 2.5k）

📅 事件差分（观察，非因果）: 09-18（1D）ATM IV 75.2% vs 09-25 64.7%（差 +10.5pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-17/MSTR_evening.json