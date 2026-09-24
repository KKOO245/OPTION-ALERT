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
🟡 **近现价集中开仓**: 09-25 59P ΔOI +2,281（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 57.29 → 收盘 57.62（+0.6%） ｜ 今日高 57.83 ｜ 低 56.95 ｜ 昨收 58.16 → 收盘 57.62（-0.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.39 | OI比 0.42 | ATM IV 35.2% | Skew -1.2pp | Term 0.96 | ExpMove ±1.5%（近端） | Rank 57%
量化视角： IV 中性（Rank 57%）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -1.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.42）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-25（1D）±1.5% ｜ 09-28（4D）±2.2% ｜ 09-30（6D）±3.2% ｜ 10-02（8D）±3.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 42,477,972 | GEX Change vs 上次快照 -63,887,892 | Flip: Primary Flip: 56.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 768 / LOW 200 / INVALID 274
结构观察区: Primary Flip 56.53（全链重定价，覆盖 95%）
Put Wall 60（弱结构｜现价低于该位 4.0%）
最近结构参考: Flip 57（现价高于该位 1.9%）
量化视角： 正 Gamma（4248万，无历史分位）｜正 Gamma 减弱（6389万）｜现价位于 Flip 上方 1.92%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 60（Put Wall，弱结构） / 60（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 57（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-25  C +11.5k / P +5.8k ｜ Activity HIGH ｜ 1D
09-28  C +5.9k / P +2.7k ｜ Activity HIGH ｜ 4D
09-30  C +7.1k / P -18.0k ｜ Activity HIGH ｜ 6D
10-02  C +16.2k / P +4.7k ｜ Activity HIGH ｜ 8D

📆 09-25 Forward Structure
存量OI: C 123.4k / P 51.7k，今日变化ΔOI: C +11.5k / P +5.8k，平值价格ATM: C $0.49 / P $0.37 ｜ ATM IV 35.2%，净 delta 敞口 -187k shares
Top ΔOI: P 59 +2,281 ｜ P 63 -1,288 ｜ C 58 +1,273
仓位参考: Max Pain 60 ｜ Put Wall 55（-4.5%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 35.2%｜历史 Rank 57%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 187,262 股

📆 09-28 Forward Structure
存量OI: C 12.1k / P 8.9k，今日变化ΔOI: C +5.9k / P +2.7k，平值价格ATM: C $0.68 / P $0.61 ｜ ATM IV 25.7%，净 delta 敞口 -132k shares
Top ΔOI: C 62 +1,177 ｜ P 60 +1,094 ｜ C 60 +844
仓位参考: Max Pain 60 ｜ Call Wall 62.5（+8.5%，弱）（OI 2.3k） ｜ Put Wall 60（+4.1%，弱）（OI 1.6k）
量化解读： 存量 Call 重｜ATM IV 25.7%｜历史 Rank 57%（近端代理）｜IV/RV 0.69×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 131,874 股

📆 09-30 Forward Structure
存量OI: C 278.6k / P 134.5k，今日变化ΔOI: C +7.1k / P -18.0k，平值价格ATM: C $0.95 / P $0.88 ｜ ATM IV 29.3%，净 delta 敞口 1.9M shares
Top ΔOI: P 75 -15,316
仓位参考: Max Pain 58 ｜ Call Wall 60（+4.1%，弱）（OI 5.9k） ｜ Put Wall 53（-8.0%）（OI 11.4k）
量化解读： 存量 Call 重｜ATM IV 29.3%｜历史 Rank 57%（近端代理）｜IV/RV 0.79×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 1,933,403 股

📆 10-02 Forward Structure
存量OI: C 67.7k / P 33.3k，今日变化ΔOI: C +16.2k / P +4.7k，平值价格ATM: C $1.19 / P $1.07 ｜ ATM IV 32.7%，净 delta 敞口 -48k shares
Top ΔOI: C 60 +4,703 ｜ C 62 +3,805
仓位参考: Max Pain 60 ｜ Call Wall 60（+4.1%，弱）（OI 12.3k） ｜ Put Wall 55（-4.5%，弱）（OI 4.0k）
量化解读： 存量 Call 重｜ATM IV 32.7%｜历史 Rank 57%（近端代理）｜IV/RV 0.88×（近似）｜净 delta 敞口 负 48,078 股

📅 事件差分（观察，非因果）: 09-25（1D）ATM IV 35.2% vs 09-28 25.7%（差 +9.5pp）——覆盖 耐用品订单 Orders MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-24/SLV_evening.json