# 期权晚报 2026-11-18（快照 16:40 ET）

📊 市场环境

SPY $730.20 ｜ QQQ $nan
VIX 24.56 ↓3.5%（5D +40.4%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 12-04 10P ΔOI +1（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 10.62 → 收盘 10.35（-2.5%） ｜ 今日高 11.25 ｜ 低 10.19 ｜ 昨收 10.49 → 收盘 10.35（-1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.03 | OI比 0.30 | ATM IV 95.2% | Skew 14.2pp | Term 1.01 | ExpMove ±8.2%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常（Term 1.01）｜保护溢价显著（Skew 14.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（2D）±8.2% ｜ 11-27（9D）±9.7% ｜ 12-04（16D）±21.1% ｜ 12-11（23D）±16.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 697,842 | GEX Change vs 上次快照 -812,894 | Flip: Primary Flip: 9.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 166 / LOW 71 / INVALID 129
结构观察区: Primary Flip 9.29（全链重定价，覆盖 91%）
Put Wall 11（弱结构｜现价低于该位 5.9%）
最近结构参考: Put Wall 11（现价低于该位 5.9%）
量化视角： 正 Gamma（70万，无历史分位）｜正 Gamma 减弱（81万）｜现价位于 Flip 上方 11.36%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 11（Put Wall，弱结构） / 12（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 9（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C +0.2k / P -13 ｜ Activity MEDIUM △ ｜ 2D
11-27  C +9 / P +1 ｜ Activity MEDIUM △ ｜ 9D
12-04  C +67 / P +3 ｜ Activity HIGH ｜ 16D
12-11  C +18 / P +1 ｜ Activity MEDIUM △ ｜ 23D

📆 11-20 Forward Structure
存量OI: C 7.0k / P 2.1k，今日变化ΔOI: C +0.2k / P -13，平值价格ATM: C $0.30 / P $0.55 ｜ ATM IV 95.2%，净 delta 敞口 7k shares
Top ΔOI: C 11 +127 ｜ P 11 -32
仓位参考: Max Pain 12 ｜ Call Wall 11（+6.3%，弱）（OI 0.3k） ｜ Put Wall 10（-3.4%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 95.2%｜历史 Rank 36%（近端代理）｜IV/RV 0.98×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 7,120 股

11-27（MEDIUM △）Top ΔOI: 10C +7 ｜ 11P +7
11-27（MEDIUM △）仓位参考: Max Pain 12 ｜ Put Wall 10（-3.4%，弱）（OI 0.1k）

📆 12-04 Forward Structure
存量OI: C 0.6k / P 0.4k，今日变化ΔOI: C +67 / P +3，平值价格ATM: C $1.25 / P $0.93 ｜ ATM IV 92.8%，净 delta 敞口 3k shares
Top ΔOI: C 11 +64 ｜ P 10 +1
仓位参考: Max Pain 12 ｜ Call Wall 11（+6.3%，弱）（OI 65） ｜ Put Wall 9.5（-8.2%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 92.8%｜历史 Rank 36%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 正 2,684 股

12-11（MEDIUM △）仓位参考: Max Pain 11 ｜ Call Wall 11（+6.3%，弱）（OI 41） ｜ Put Wall 11（+6.3%，弱）（OI 14）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/NNE_evening.json