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
🔴 **事件差分**: 09-25（3D）ATM IV 91.4% vs 10-02 74.1%（差 +17.3pp），覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 10-02 17C ΔOI +185（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-02 20C ΔOI +2,846 占该期限总 OI 12.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 16.90 → 收盘 16.99（+0.6%） ｜ 今日高 17.10 ｜ 低 16.24 ｜ 昨收 16.78 → 收盘 16.99（+1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.48 | OI比 0.51 | ATM IV 91.4% | Skew -8.1pp | Term 0.84 | ExpMove ±6.7%（近端） | Rank 15%
量化视角： IV 历史低位（Rank 15%，期权偏便宜）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（3D）±6.7% ｜ 10-02（10D）±10.3% ｜ 10-09（17D）±12.8% ｜ 10-16（24D）±15.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,455,545 | GEX Change vs 上次快照 2,962,300 | Flip: Primary Flip: 15.65（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 259 / LOW 58 / INVALID 125
结构观察区: Primary Flip 15.65（全链重定价，覆盖 99%）
最近结构参考: Flip 16（现价高于该位 8.6%）
量化视角： 正 Gamma（746万，无历史分位）｜正 Gamma 增强（+296万）｜现价位于 Flip 上方 8.57%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 17（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +6.8k / P +3.8k ｜ Activity HIGH ｜ 3D
10-02  C +4.1k / P +0.8k ｜ Activity HIGH ｜ 10D
10-09  C +0.5k / P +4 ｜ Activity HIGH ｜ 17D
10-16  C +6.4k / P +0.2k ｜ Activity HIGH ｜ 24D

📆 09-25 Forward Structure
存量OI: C 27.0k / P 13.6k，今日变化ΔOI: C +6.8k / P +3.8k，平值价格ATM: C $0.59 / P $0.54 ｜ ATM IV 91.4%，净 delta 敞口 56k shares
Top ΔOI: C 18 +2,549 ｜ P 15 +1,991
仓位参考: Max Pain 17 ｜ Call Wall 18（+5.9%，弱）（OI 4.9k） ｜ Put Wall 15.5（-8.8%，弱）（OI 2.8k）
量化解读： 存量 Call 重｜ATM IV 91.4%｜历史 Rank 15%（近端代理）｜IV/RV 1.69×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 56,121 股

📆 10-02 Forward Structure
存量OI: C 16.9k / P 6.0k，今日变化ΔOI: C +4.1k / P +0.8k，平值价格ATM: C $0.89 / P $0.86 ｜ ATM IV 74.1%，净 delta 敞口 55k shares
Top ΔOI: C 18 +389 ｜ C 17 +185
仓位参考: Max Pain 17 ｜ Call Wall 18.5（+8.9%，弱）（OI 2.1k） ｜ Put Wall 17（+0.1%）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 74.1%｜历史 Rank 15%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 55,020 股

📆 10-09 Forward Structure
存量OI: C 5.5k / P 3.0k，今日变化ΔOI: C +0.5k / P +4，平值价格ATM: C $1.12 / P $1.06 ｜ ATM IV 74.5%，净 delta 敞口 15k shares
Top ΔOI: C 18 +85
仓位参考: Max Pain 16 ｜ Put Wall 16（-5.8%）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 74.5%｜历史 Rank 15%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 14,835 股

📆 10-16 Forward Structure
存量OI: C 35.5k / P 12.9k，今日变化ΔOI: C +6.4k / P +0.2k，平值价格ATM: C $1.33 / P $1.32 ｜ ATM IV 72.7%，净 delta 敞口 136k shares
Top ΔOI: C 21 +4,602 ｜ C 16 +435
仓位参考: Max Pain 17 ｜ Call Wall 18（+5.9%，弱）（OI 4.4k） ｜ Put Wall 17（+0.1%，弱）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 72.7%｜历史 Rank 15%（近端代理）｜IV/RV 1.34×（近似）｜净 delta 敞口 正 136,326 股

📅 事件差分（观察，非因果）: 09-25（3D）ATM IV 91.4% vs 10-02 74.1%（差 +17.3pp）——覆盖 President Trump and President Xi Summit、耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-22/USAR_evening.json