# 期权晚报 2026-09-24（快照 16:40 ET）

📊 市场环境

SPY $767.18 ｜ QQQ $741.10
VIX 15.67 ↑3.2%（5D -11.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-24

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **事件差分**: 09-25（1D）ATM IV 96.0% vs 10-02 78.4%（差 +17.5pp），覆盖 耐用品订单 Orders MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 09-25 17P ΔOI +787（距现价 -0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 16.67 → 收盘 17.02（+2.1%） ｜ 今日高 17.11 ｜ 低 16.36 ｜ 昨收 17.01 → 收盘 17.02（+0.1%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.37 | OI比 0.52 | ATM IV 96.0% | Skew 9.2pp | Term 0.77 | ExpMove ±4.2%（近端） | Rank 30%
量化视角： IV 中性（Rank 30%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价显著（Skew 9.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.37×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±4.2% ｜ 10-02（8D）±8.2% ｜ 10-09（15D）±10.9% ｜ 10-16（22D）±15.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,036,785 | GEX Change vs 上次快照 -444,430 | Flip: Primary Flip: 15.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 214 / LOW 90 / INVALID 152
结构观察区: Primary Flip 15.75（全链重定价，覆盖 88%）
Put Wall 17（弱结构｜现价高于该位 0.1%）
最近结构参考: Put Wall 17（现价高于该位 0.1%）
量化视角： 正 Gamma（204万，无历史分位）｜正 Gamma 减弱（44万）｜现价位于 Flip 上方 8.06%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 17（Put Wall，弱结构） / 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0.5k / P +0.9k ｜ Activity HIGH ｜ 1D
10-02  C +0.3k / P +8 ｜ Activity MEDIUM △ ｜ 8D
10-09  C +14 / P +45 ｜ Activity MEDIUM △ ｜ 15D
10-16  C +3 / P +0.1k ｜ Activity LOW ｜ 22D

📆 09-25 Forward Structure
存量OI: C 8.0k / P 4.2k，今日变化ΔOI: C +0.5k / P +0.9k，平值价格ATM: C $0.23 / P $0.48 ｜ ATM IV 96.0%，净 delta 敞口 -38k shares
Top ΔOI: P 17 +787 ｜ C 18 +213 ｜ C 18 +79
仓位参考: Max Pain 17 ｜ Call Wall 18（+5.8%，弱）（OI 1.1k） ｜ Put Wall 17（-0.1%）（OI 1.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 96.0%｜历史 Rank 30%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 37,829 股

10-02（MEDIUM △）Top ΔOI: 18C +101 ｜ 26P -88
10-02（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（-6.0%，弱）（OI 0.2k）

10-09（MEDIUM △）Top ΔOI: 18C -178
10-09（MEDIUM △）仓位参考: Max Pain 18 ｜ Put Wall 16（-6.0%）（OI 0.1k）

10-16（Activity LOW）仓位参考: Max Pain 20 ｜ Put Wall 17（-0.1%，弱）（OI 0.7k）

📅 事件差分（观察，非因果）: 09-25（1D）ATM IV 96.0% vs 10-02 78.4%（差 +17.5pp）——覆盖 耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/NNE_evening.json