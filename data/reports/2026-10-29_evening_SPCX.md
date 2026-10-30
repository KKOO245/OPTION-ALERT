# 期权晚报 2026-10-29（快照 21:00 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 17.20 ↑1.7%（5D -9.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **事件差分**: 10-30 ATM IV 55.4% vs 11-02 40.8%（差 +14.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 142.30 → 收盘 143.89（+1.1%） ｜ 今日高 144.95 ｜ 低 141.03 ｜ 昨收 145.23 → 收盘 143.89（-0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.70 | OI比 0.72 | ATM IV 55.4% | Skew -0.8pp | Term 0.88 | ExpMove ±2.3%（近端） | Rank 52%
量化视角： IV 中性（Rank 52%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.72）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.72×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（1D）±2.3% ｜ 11-02（4D）±3.5% ｜ 11-04（6D）±5.2% ｜ 11-06（8D）±6.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -56,023,981 | GEX Change vs 上次快照 -2,689,059 | Flip: Primary Flip: 146.91（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 738 / LOW 162 / INVALID 530
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 146.91（全链重定价，覆盖 99%）
Put Wall 140（弱结构｜现价高于该位 2.8%）
最近结构参考: Flip 147（现价低于该位 2.1%）
量化视角： 负 Gamma（5602万，无历史分位）｜负 Gamma 加深（269万）｜现价位于 Flip 下方 2.06%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 150（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 147（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-30  C +0 / P +0 ｜ Activity LOW ｜ 1D
11-02  C +0 / P +0 ｜ Activity LOW ｜ 4D
11-04  C +0 / P +0 ｜ Activity LOW ｜ 6D
11-06  C +0 / P +0 ｜ Activity LOW ｜ 8D

📆 10-30 Forward Structure
存量OI: C 287.1k / P 205.7k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.62 / P $1.71 ｜ ATM IV 55.4%，净 delta 敞口 0 shares
仓位参考: Max Pain 150 ｜ Call Wall 155（+7.7%，弱）（OI 19.7k） ｜ Put Wall 150（+4.2%，弱）（OI 20.1k）
量化解读： 存量 Call 重｜ATM IV 55.4%｜历史 Rank 52%（近端代理）｜IV/RV 1.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

11-02（Activity LOW）仓位参考: Max Pain 147 ｜ Call Wall 157.5（+9.5%，弱）（OI 3.4k） ｜ Put Wall 145（+0.8%，弱）（OI 2.2k）

11-04（Activity LOW）仓位参考: Max Pain 148 ｜ Call Wall 155（+7.7%，弱）（OI 1.1k） ｜ Put Wall 135（-6.2%，弱）（OI 0.8k）

11-06（Activity LOW）仓位参考: Max Pain 150 ｜ Put Wall 140（-2.7%）（OI 11.8k）

📅 事件差分（观察，非因果）: 10-30（1D）ATM IV 55.4% vs 11-02 40.8%（差 +14.6pp）——覆盖 GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM、PCE 物价 Price Index MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/SPCX_evening.json