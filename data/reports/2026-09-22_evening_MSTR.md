# 期权晚报 2026-09-22（快照 16:40 ET）

📊 市场环境

SPY $773.38 ｜ QQQ $747.46
VIX 14.21 ↓4.4%（5D -17.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 35.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-22

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-23 20:00　【高】President Trump and President Xi Summit　实际 待公布
- 周五 09-25 08:30　【高】耐用品订单 Orders MoM　预测 -0.4 ｜ 实际 待公布 ｜ 前值 1.1

🔍 重点速览
🟡 **近现价集中开仓**: 09-25 172C ΔOI +6,314（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 167.49 → 收盘 167.33（-0.1%） ｜ 今日高 171.17 ｜ 低 167.25 ｜ 昨收 168.50 → 收盘 167.33（-0.7%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.55 | OI比 0.80 | ATM IV 78.7% | Skew -10.5pp | Term 0.89 | ExpMove ±5.8%（近端） | Rank 46%
量化视角： IV 中性（Rank 46%）｜期限结构倒挂（Term 0.89，近月 IV 高于远月）｜Put 保护异常便宜（Skew -10.5pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.80）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.80×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±5.8% ｜ 10-02（10D）±9.5% ｜ 10-09（17D）±12.0% ｜ 10-16（24D）±14.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 65,259,403 | GEX Change vs 上次快照 4,947,244 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 901 / LOW 59 / INVALID 112
结构观察区: NO_CROSS
量化视角： 正 Gamma（6526万，无历史分位）｜正 Gamma 增强（+495万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 141（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +38.9k / P +44.4k ｜ Activity HIGH ｜ 3D
10-02  C +15.5k / P +11.2k ｜ Activity HIGH ｜ 10D
10-09  C +8.9k / P +4.3k ｜ Activity HIGH ｜ 17D
10-16  C +4.3k / P +5.8k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 264.5k / P 210.7k，今日变化ΔOI: C +38.9k / P +44.4k，平值价格ATM: C $4.80 / P $4.83 ｜ ATM IV 78.7%，净 delta 敞口 -775k shares
Top ΔOI: C 177 +6,318 ｜ C 172 +6,314
仓位参考: Max Pain 141 ｜ Call Wall 155（-7.4%，弱）（OI 20.0k） ｜ Put Wall 155（-7.4%，弱）（OI 5.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 78.7%｜历史 Rank 46%（近端代理）｜IV/RV 0.76×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 774,634 股

📆 10-02 Forward Structure
存量OI: C 51.9k / P 71.8k，今日变化ΔOI: C +15.5k / P +11.2k，平值价格ATM: C $7.99 / P $7.85 ｜ ATM IV 71.9%，净 delta 敞口 42k shares
Top ΔOI: C 200 +6,238 ｜ C 215 +2,344 ｜ C 180 +1,940
仓位参考: Max Pain 140 ｜ Call Wall 180（+7.6%，弱）（OI 5.3k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 71.9%｜历史 Rank 46%（近端代理）｜IV/RV 0.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,816 股

📆 10-09 Forward Structure
存量OI: C 25.9k / P 39.0k，今日变化ΔOI: C +8.9k / P +4.3k，平值价格ATM: C $10.30 / P $9.85 ｜ ATM IV 70.5%，净 delta 敞口 240k shares
Top ΔOI: C 200 +3,143 ｜ C 160 +2,319 ｜ P 120 +1,672
仓位参考: Max Pain 140 ｜ Call Wall 160（-4.4%，弱）（OI 4.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 70.5%｜历史 Rank 46%（近端代理）｜IV/RV 0.68×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 240,457 股

📆 10-16 Forward Structure
存量OI: C 161.4k / P 133.3k，今日变化ΔOI: C +4.3k / P +5.8k，平值价格ATM: C $12.45 / P $11.80 ｜ ATM IV 70.5%，净 delta 敞口 -243k shares
Top ΔOI: C 200 +3,687 ｜ C 150 -3,462 ｜ P 115 +2,408
仓位参考: Max Pain 115 ｜ Call Wall 180（+7.6%，弱）（OI 10.5k） ｜ Put Wall 160（-4.4%，弱）（OI 2.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 70.5%｜历史 Rank 46%（近端代理）｜IV/RV 0.68×（近似）｜净 delta 敞口 负 243,493 股

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 78.7% vs 10-02 71.9%（差 +6.8pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/MSTR_evening.json