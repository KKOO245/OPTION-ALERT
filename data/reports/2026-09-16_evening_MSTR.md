# 期权晚报 2026-09-16（快照 21:12 ET）

📊 市场环境

SPY $754.05 ｜ QQQ $704.72
VIX 17.71 ↑3.0%（5D +7.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 26.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-16

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-16 08:30　【高】零售销售 MoM　预测 0.8 ｜ 实际 1.2 ｜ 前值 -0.5　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 3.75　✅ 今日已公布
- 周三 09-16 14:00　【高】美联储议息会议 Economic Projections　实际 待公布　✅ 今日已公布
- 周三 09-16 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 09-17 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.239
- 周四 09-17 08:30　【高】建筑许可 Prel　预测 1.41 ｜ 实际 待公布 ｜ 前值 1.433

🔍 重点速览
🟡 **事件差分**: 09-18 ATM IV 79.5% vs 09-25 69.1%（差 +10.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 129.84 → 收盘 126.18（-2.8%） ｜ 今日高 130.42 ｜ 低 123.33 ｜ 昨收 129.60 → 收盘 126.18（-2.6%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.84 | OI比 0.63 | ATM IV 79.5% | Skew -2.3pp | Term 0.86 | ExpMove ±4.8%（近端） | Rank 48%
量化视角： IV 中性（Rank 48%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.84×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-18（2D）±4.8% ｜ 09-25（9D）±8.7% ｜ 10-02（16D）±11.0% ｜ 10-09（23D）±13.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,189,951 | GEX Change vs 上次快照 -26,119,735 | Flip: Primary Flip: 125.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 812 / LOW 135 / INVALID 251
结构观察区: Primary Flip 125.47（全链重定价，覆盖 99%）
最近结构参考: Flip 125（现价高于该位 0.6%）
量化视角： 正 Gamma（619万，无历史分位）｜正 Gamma 减弱（2612万）｜现价位于 Flip 上方 0.56%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 122（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 125（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

09-18  C +0 / P +0 ｜ Activity LOW ｜ 2D
09-25  C +0 / P +0 ｜ Activity LOW ｜ 9D
10-02  C +0 / P +0 ｜ Activity LOW ｜ 16D
10-09  C +0 / P +0 ｜ Activity LOW ｜ 23D

📆 09-18 Forward Structure
存量OI: C 475.7k / P 297.8k，今日变化ΔOI: C +0 / P +0，平值价格ATM: C $3.05 / P $2.96 ｜ ATM IV 79.5%，净 delta 敞口 0 shares
仓位参考: Max Pain 122 ｜ Call Wall 135（+7.0%，弱）（OI 24.0k） ｜ Put Wall 120（-4.9%，弱）（OI 14.1k）
量化解读： 存量 Call 重｜ATM IV 79.5%｜历史 Rank 48%（近端代理）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 0 股

09-25（Activity LOW）仓位参考: Max Pain 129 ｜ Call Wall 130（+3.0%，弱）（OI 1.4k） ｜ Put Wall 125（-0.9%，弱）（OI 2.7k）

10-02（Activity LOW）仓位参考: Max Pain 130 ｜ Put Wall 130（+3.0%，弱）（OI 2.6k）

10-09（Activity LOW）仓位参考: Max Pain 135 ｜ Call Wall 130（+3.0%，弱）（OI 0.4k） ｜ Put Wall 130（+3.0%，弱）（OI 2.4k）

📅 事件差分（观察，非因果）: 09-18（2D）ATM IV 79.5% vs 09-25 69.1%（差 +10.4pp）——覆盖 零售销售 MoM、美联储利率决议 Decision、美联储议息会议 Economic Projections、Fed Press Conference、新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-16/MSTR_evening.json