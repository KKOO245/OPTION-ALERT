# 期权晚报 2026-09-23（快照 21:00 ET）

📊 市场环境

SPY $767.81 ｜ QQQ $nan
VIX 15.18 ↑2.1%（5D -11.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-23

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布　✅ 今日已公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 59.00 → 收盘 58.16（-1.4%） ｜ 今日高 59.03 ｜ 低 58.02 ｜ 昨收 60.73 → 收盘 58.16（-4.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.28 | OI比 0.41 | ATM IV 40.1% | Skew -3.7pp | Term 0.91 | ExpMove ±5.3%（近端） | Rank 66%
量化视角： IV 中性（Rank 66%）｜期限结构正常（Term 0.91）｜Put 保护异常便宜（Skew -3.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.28×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.41×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（2D）±5.3% ｜ 09-28（5D）±5.6% ｜ 09-30（7D）±5.8% ｜ 10-02（9D）±6.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 35,431,411 | GEX Change vs 上次快照 -84,372,777 | Flip: Primary Flip: 56.81（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 757 / LOW 135 / INVALID 350
结构观察区: Primary Flip 56.81（全链重定价，覆盖 99%）
最近结构参考: Flip 57（现价高于该位 2.4%）
量化视角： 正 Gamma（3543万，无历史分位）｜正 Gamma 减弱（8437万）｜现价位于 Flip 上方 2.38%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 60（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-28  C +0 / P +0 ｜ Activity LOW ｜ 5D
09-30  C +0 / P +0 ｜ Activity LOW ｜ 7D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 9D

📆 09-25 Forward Structure
存量OI: C 111.9k / P 45.9k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $2.96 / P $0.10 ｜ ATM IV 40.1%，净 delta 敞口 0 shares
仓位参考: Max Pain 60 ｜ Put Wall 55（-5.4%，弱）（OI 4.7k）
量化解读： 存量 Call 重｜ATM IV 40.1%｜历史 Rank 66%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-28（Activity LOW）仓位参考: Max Pain 60 ｜ Call Wall 62.5（+7.5%）（OI 2.2k） ｜ Put Wall 52.5（-9.7%，弱）（OI 1.5k）

09-30（Activity LOW）仓位参考: Max Pain 62 ｜ Put Wall 53（-8.9%，弱）（OI 11.3k）

10-02（Activity LOW）仓位参考: Max Pain 59 ｜ Call Wall 60（+3.2%，弱）（OI 7.6k） ｜ Put Wall 56（-3.7%，弱）（OI 3.8k）

📅 事件差分（观察，非因果）: 09-25（2D）ATM IV 40.1% vs 09-28 33.7%（差 +6.3pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-23/SLV_evening.json