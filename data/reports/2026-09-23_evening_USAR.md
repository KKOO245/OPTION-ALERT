# 期权晚报 2026-09-23（快照 16:40 ET）

📊 市场环境

SPY $767.81 ｜ QQQ $741.21
VIX 15.18 ↑2.1%（5D -11.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布　⏰ 今日
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 16.73 → 收盘 15.83（-5.4%） ｜ 今日高 16.76 ｜ 低 15.80 ｜ 昨收 16.99 → 收盘 15.83（-6.8%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.47 | OI比 0.51 | ATM IV 87.5% | Skew -7.9pp | Term 0.86 | ExpMove ±8.2%（近端） | Rank 11%
量化视角： IV 历史低位（Rank 11%，期权偏便宜）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（2D）±8.2% ｜ 10-02（9D）±10.9% ｜ 10-09（16D）±14.4% ｜ 10-16（23D）±15.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -129,824 | GEX Change vs 上次快照 -7,915,782 | Flip: Primary Flip: 15.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 260 / LOW 59 / INVALID 123
结构观察区: Primary Flip 15.85（全链重定价，覆盖 99%）
Put Wall 15（现价高于该位 5.5%）
最近结构参考: Flip 16（现价低于该位 0.1%）
量化视角： 负 Gamma（13万，无历史分位）｜由正转负（792万）｜现价位于 Flip 下方 0.14%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-16  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-25 Forward Structure
存量OI: C 27.0k / P 13.6k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $1.14 / P $0.16 ｜ ATM IV 87.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 17 ｜ Call Wall 17（+7.4%，弱）（OI 3.5k） ｜ Put Wall 15.5（-2.1%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 87.5%｜历史 Rank 11%（近端代理）｜IV/RV 1.63×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

10-02（Activity LOW）仓位参考: Max Pain 17 ｜ Put Wall 17（+7.4%）（OI 1.4k）

10-09（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 16（+1.1%）（OI 1.2k）

10-16（Activity LOW）仓位参考: Max Pain 17 ｜ Put Wall 15（-5.2%）（OI 5.3k）

📅 事件差分（观察，非因果）: 09-25（2D）ATM IV 87.5% vs 10-02 78.6%（差 +8.9pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/USAR_evening.json