# 期权晚报 2026-09-29（快照 16:40 ET）

📊 市场环境

SPY $764.20 ｜ QQQ $737.93
VIX 16.04 ↓0.2%（5D +12.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-29 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.23 ｜ 实际 7.079 ｜ 前值 7.335　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 待公布 ｜ 前值 2.1
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🟡 **事件差分**: 10-02 ATM IV 81.8% vs 10-09 69.0%（差 +12.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 1800P ΔOI +709（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SNDK: 今开 1,744.41 → 收盘 1,729.76（-0.8%） ｜ 今日高 1749.78 ｜ 低 1693.00 ｜ 昨收 1,712.89 → 收盘 1,729.76（+1.0%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.44 | OI比 0.97 | ATM IV 81.8% | Skew -3.4pp | Term 0.86 | ExpMove ±6.1%（近端） | Rank 38%
量化视角： IV 中性（Rank 38%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜Put 保护异常便宜（Skew -3.4pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.97×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（3D）±6.1% ｜ 10-09（10D）±9.2% ｜ 10-16（17D）±12.0% ｜ 10-23（24D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,725,096 | GEX Change vs 上次快照 371,207 | Flip: Primary Flip: 1706.33（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1869 / LOW 374 / INVALID 1023
结构观察区: Primary Flip 1706.33（全链重定价，覆盖 100%）
Put Wall 1,600（弱结构｜现价高于该位 8.1%）
最近结构参考: Flip 1706（现价高于该位 1.4%）
量化视角： 正 Gamma（173万，无历史分位）｜正 Gamma 增强（+37万）｜现价位于 Flip 上方 1.37%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,600（Put Wall，弱结构） / 1,700（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1706（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +7.4k / P +6.8k ｜ Activity HIGH ｜ 3D
10-09  C +1.6k / P +2.3k ｜ Activity HIGH ｜ 10D
10-16  C +1.2k / P +1.6k ｜ Activity HIGH ｜ 17D
10-23  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 38.7k / P 37.5k，今日变化ΔOI: C +7.4k / P +6.8k，平值价格ATM: C $52.50 / P $53.40 ｜ ATM IV 81.8%，净 delta 敞口 133k shares
Top ΔOI: C 2000 +1,192 ｜ P 1600 +990 ｜ P 1620 +634
仓位参考: Max Pain 1,700 ｜ Call Wall 1900（+9.8%，弱）（OI 1.8k） ｜ Put Wall 1600（-7.5%，弱）（OI 2.0k）
量化解读： 存量两侧均衡｜ATM IV 81.8%｜历史 Rank 38%（近端代理）｜IV/RV 1.10×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 133,003 股

📆 10-09 Forward Structure
存量OI: C 11.5k / P 10.7k，今日变化ΔOI: C +1.6k / P +2.3k，平值价格ATM: C $81.00 / P $78.71 ｜ ATM IV 69.0%，净 delta 敞口 -27k shares
Top ΔOI: P 1800 +709 ｜ C 2000 +194 ｜ C 1875 +140
仓位参考: Max Pain 1,640 ｜ Call Wall 1900（+9.8%，弱）（OI 0.5k） ｜ Put Wall 1800（+4.1%）（OI 0.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 69.0%｜历史 Rank 38%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 26,621 股

📆 10-16 Forward Structure
存量OI: C 37.7k / P 48.1k，今日变化ΔOI: C +1.2k / P +1.6k，平值价格ATM: C $102.74 / P $104.09 ｜ ATM IV 68.3%，净 delta 敞口 10k shares
Top ΔOI: C 2100 -322 ｜ P 1380 +207 ｜ P 1400 +200
仓位参考: Max Pain 1,650 ｜ Call Wall 1800（+4.1%，弱）（OI 1.2k） ｜ Put Wall 1600（-7.5%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 68.3%｜历史 Rank 38%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 9,546 股

📆 10-23 Forward Structure
存量OI: C 4.5k / P 6.5k，今日变化ΔOI: C +0.4k / P +0.4k，平值价格ATM: C $121.20 / P $132.00 ｜ ATM IV 68.4%，净 delta 敞口 6k shares
Top ΔOI: P 1700 +77 ｜ C 1845 +41
仓位参考: Max Pain 1,745 ｜ Call Wall 1840（+6.4%，弱）（OI 0.2k） ｜ Put Wall 1650（-4.6%，弱）（OI 0.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 68.4%｜历史 Rank 38%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 6,139 股

📅 事件差分（观察，非因果）: 10-02（3D）ATM IV 81.8% vs 10-09 69.0%（差 +12.8pp）——覆盖 职位空缺(JOLTS) Job Openings、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/SNDK_evening.json