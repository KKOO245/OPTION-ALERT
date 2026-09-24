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
🟡 **近现价集中开仓**: 10-02 190P ΔOI +501（距现价 -4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 196.74 → 收盘 199.21（+1.3%） ｜ 今日高 202.78 ｜ 低 193.69 ｜ 昨收 198.13 → 收盘 199.21（+0.5%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.42 | OI比 0.54 | ATM IV 73.3% | Skew -7.2pp | Term 0.88 | ExpMove ±3.1%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜Put 保护异常便宜（Skew -7.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.54）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.54×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±3.1% ｜ 10-02（8D）±7.6% ｜ 10-09（15D）±10.3% ｜ 10-16（22D）±12.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 35,790,792 | GEX Change vs 上次快照 -872,796 | Flip: Primary Flip: 182.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 512 / LOW 161 / INVALID 239
结构观察区: Primary Flip 182.56（全链重定价，覆盖 100%）
最近结构参考: Flip 183（现价高于该位 9.1%）
量化视角： 正 Gamma（3579万，无历史分位）｜正 Gamma 减弱（87万）｜现价位于 Flip 上方 9.12%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 183（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +7.2k / P +1.7k ｜ Activity HIGH ｜ 1D
10-02  C +2.6k / P +2.3k ｜ Activity HIGH ｜ 8D（新行权价 C 21）
10-09  C +0.6k / P +0.8k ｜ Activity HIGH ｜ 15D
10-16  C +0.9k / P +1.4k ｜ Activity HIGH ｜ 22D

📆 09-25 Forward Structure
存量OI: C 94.2k / P 50.9k，今日变化ΔOI: C +7.2k / P +1.7k，平值价格ATM: C $2.72 / P $3.45 ｜ ATM IV 73.3%，净 delta 敞口 -6k shares
Top ΔOI: C 210 +2,858
仓位参考: Max Pain 185 ｜ Call Wall 210（+5.4%，弱）（OI 10.1k） ｜ Put Wall 180（-9.6%，弱）（OI 4.7k）
量化解读： 存量 Call 重｜ATM IV 73.3%｜历史 Rank 40%（近端代理）｜IV/RV 0.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 6,171 股

📆 10-02 Forward Structure
存量OI: C 22.1k / P 33.2k，今日变化ΔOI: C +2.6k / P +2.3k（新行权价 C 21），平值价格ATM: C $7.28 / P $7.87 ｜ ATM IV 64.3%，净 delta 敞口 -8k shares
Top ΔOI: P 190 +501 ｜ C 220 +306
仓位参考: Max Pain 188 ｜ Call Wall 187.5（-5.9%，弱）（OI 1.3k） ｜ Put Wall 187.5（-5.9%，弱）（OI 1.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 64.3%｜历史 Rank 40%（近端代理）｜IV/RV 0.74×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 8,028 股

📆 10-09 Forward Structure
存量OI: C 5.3k / P 12.1k，今日变化ΔOI: C +0.6k / P +0.8k，平值价格ATM: C $10.53 / P $10.05 ｜ ATM IV 62.6%，净 delta 敞口 5k shares
仓位参考: Max Pain 188 ｜ Call Wall 200（+0.4%，弱）（OI 0.4k）
量化解读： 存量 Put 重｜ATM IV 62.6%｜历史 Rank 40%（近端代理）｜IV/RV 0.72×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 5,421 股

📆 10-16 Forward Structure
存量OI: C 79.1k / P 72.9k，今日变化ΔOI: C +0.9k / P +1.4k，平值价格ATM: C $12.00 / P $12.24 ｜ ATM IV 61.3%，净 delta 敞口 -42k shares
Top ΔOI: P 200 +975 ｜ P 180 +354
仓位参考: Max Pain 175 ｜ Call Wall 200（+0.4%，弱）（OI 6.1k） ｜ Put Wall 200（+0.4%，弱）（OI 3.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.3%｜历史 Rank 40%（近端代理）｜IV/RV 0.70×（近似）｜净 delta 敞口 负 41,697 股

📅 事件差分（观察，非因果）: 09-25（1D）ATM IV 73.3% vs 10-02 64.3%（差 +9.0pp）——覆盖 耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/COIN_evening.json