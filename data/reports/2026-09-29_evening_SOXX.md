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
🟡 **近现价集中开仓**: 10-09 580P ΔOI +100（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 569.87 → 收盘 567.44（-0.4%） ｜ 今日高 574.47 ｜ 低 565.30 ｜ 昨收 560.79 → 收盘 567.44（+1.2%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 1.55 | OI比 1.57 | ATM IV 37.6% | Skew 4.6pp | Term 1.03 | ExpMove ±2.7%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构正常（Term 1.03）｜保护溢价中性（Skew 4.6pp）｜当日成交偏 Put（P/C量 1.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.55×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.57×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（3D）±2.7% ｜ 10-09（10D）±4.4% ｜ 10-16（17D）±6.6% ｜ 10-23（24D）±3.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 7,178,049 | GEX Change vs 上次快照 1,030,718 | Flip: Primary Flip: 554.29（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 555 / LOW 248 / INVALID 749
结构观察区: Primary Flip 554.29（全链重定价，覆盖 99%）
Call Wall 600（现价低于该位 5.4%）
最近结构参考: Flip 554（现价高于该位 2.4%）
量化视角： 正 Gamma（718万，无历史分位）｜正 Gamma 增强（+103万）｜现价位于 Flip 上方 2.37%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 542（MaxPain，仅结算参考）；上方 600（Call Wall）。
• Gamma 区域：切换参考 554（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-02  C +0.9k / P +0.7k ｜ Activity HIGH ｜ 3D
10-09  C +0.3k / P +0.3k ｜ Activity HIGH ｜ 10D
10-16  C +1.0k / P +1.1k ｜ Activity HIGH ｜ 17D
10-23  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 24D

📆 10-02 Forward Structure
存量OI: C 16.3k / P 25.6k，今日变化ΔOI: C +0.9k / P +0.7k，平值价格ATM: C $7.40 / P $7.95 ｜ ATM IV 37.6%，净 delta 敞口 28k shares
Top ΔOI: C 575 +201
仓位参考: Max Pain 542 ｜ Call Wall 542.5（-4.4%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 37.6%｜历史 Rank 63%（近端代理）｜IV/RV 0.99×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 28,022 股

📆 10-09 Forward Structure
存量OI: C 4.4k / P 2.9k，今日变化ΔOI: C +0.3k / P +0.3k，平值价格ATM: C $12.80 / P $12.25 ｜ ATM IV 36.4%，净 delta 敞口 4k shares
Top ΔOI: P 580 +100 ｜ C 550 +68 ｜ C 600 +52
仓位参考: Max Pain 525 ｜ Call Wall 537.5（-5.3%，弱）（OI 0.4k） ｜ Put Wall 540（-4.8%，弱）（OI 0.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 36.4%｜历史 Rank 63%（近端代理）｜IV/RV 0.96×（近似）｜净 delta 敞口 正 3,920 股

📆 10-16 Forward Structure
存量OI: C 40.1k / P 85.8k，今日变化ΔOI: C +1.0k / P +1.1k，平值价格ATM: C $20.50 / P $17.10 ｜ ATM IV 35.2%，净 delta 敞口 31k shares
Top ΔOI: C 580 +501 ｜ P 535 +497 ｜ C 590 +273
仓位参考: Max Pain 530 ｜ Call Wall 600（+5.7%）（OI 9.4k）
量化解读： 存量 Put 重｜ATM IV 35.2%｜历史 Rank 63%（近端代理）｜IV/RV 0.93×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 30,901 股

📆 10-23 Forward Structure
存量OI: C 1.0k / P 5.1k，今日变化ΔOI: C +0.1k / P +0.2k，平值价格ATM: C $0.00 / P $21.00 ｜ ATM IV 37.1%，净 delta 敞口 3k shares
Top ΔOI: P 555 +54
仓位参考: Max Pain 525 ｜ Call Wall 570（+0.5%，弱）（OI 95）
量化解读： 存量 Put 重｜ATM IV 37.1%｜历史 Rank 63%（近端代理）｜IV/RV 0.98×（近似）｜净 delta 敞口 正 3,194 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-29/SOXX_evening.json