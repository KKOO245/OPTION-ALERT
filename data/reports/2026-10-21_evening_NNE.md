# 期权晚报 2026-10-21（快照 16:40 ET）

📊 市场环境

SPY $773.09 ｜ QQQ $725.20
VIX 16.68 ↓3.6%（5D -1.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 14C ΔOI +99（距现价 +5.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 13.48 → 收盘 13.33（-1.1%） ｜ 今日高 13.66 ｜ 低 13.04 ｜ 昨收 12.96 → 收盘 13.33（+2.9%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.47 | OI比 0.23 | ATM IV 79.1% | Skew 7.5pp | Term 0.91 | ExpMove ±5.2%（近端） | Rank 10%
量化视角： IV 历史低位（Rank 10%，期权偏便宜）｜期限结构正常（Term 0.91）｜保护溢价显著（Skew 7.5pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.23）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.23×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±5.2% ｜ 10-30（9D）±10.1% ｜ 11-06（16D）±23.0% ｜ 11-13（23D）±16.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 999,392 | GEX Change vs 上次快照 69,877 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 178 / LOW 84 / INVALID 140
结构观察区: NO_CROSS
Put Wall 14（现价低于该位 4.8%）
最近结构参考: Put Wall 14（现价低于该位 4.8%）
量化视角： 正 Gamma（100万，无历史分位）｜正 Gamma 增强（+7万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（Put Wall） / 14（MaxPain，仅结算参考）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +0.3k / P -0.2k ｜ Activity MEDIUM △ ｜ 2D
10-30  C +77 / P +10 ｜ Activity MEDIUM △ ｜ 9D
11-06  C +12 / P -2 ｜ Activity MEDIUM △ ｜ 16D
11-13  C +50 / P -27 ｜ Activity HIGH ｜ 23D

📆 10-23 Forward Structure
存量OI: C 6.8k / P 1.6k，今日变化ΔOI: C +0.3k / P -0.2k，平值价格ATM: C $0.30 / P $0.40 ｜ ATM IV 79.1%，净 delta 敞口 30k shares
Top ΔOI: C 13 +139 ｜ C 14 +99
仓位参考: Max Pain 14 ｜ Put Wall 14（+5.0%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 79.1%｜历史 Rank 10%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 30,266 股

10-30（MEDIUM △）Top ΔOI: 14C +30 ｜ 14C +21
10-30（MEDIUM △）仓位参考: Max Pain 14 ｜ Put Wall 14（+5.0%）（OI 0.4k）

11-06（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 13（-2.5%，弱）（OI 77）

📆 11-13 Forward Structure
存量OI: C 0.7k / P 0.4k，今日变化ΔOI: C +50 / P -27，平值价格ATM: C $1.03 / P $1.12 ｜ ATM IV 73.9%，净 delta 敞口 2k shares
Top ΔOI: P 12 -41 ｜ P 12 +5
仓位参考: Max Pain 14 ｜ Call Wall 14.5（+8.8%，弱）（OI 0.1k） ｜ Put Wall 13（-2.5%，弱）（OI 71）
量化解读： 存量 Call 重｜ATM IV 73.9%｜历史 Rank 10%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 正 1,708 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/NNE_evening.json