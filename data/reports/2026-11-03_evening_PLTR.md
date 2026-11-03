# 期权晚报 2026-11-03（快照 16:41 ET）

📊 市场环境

SPY $754.35 ｜ QQQ $685.28
VIX 20.83 ↓1.5%（5D +18.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **事件差分**: 11-06 ATM IV 73.4% vs 11-13 59.3%（差 +14.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-13 170P ΔOI +552（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 167.90 → 收盘 175.40（+4.5%） ｜ 今日高 176.54 ｜ 低 165.25 ｜ 昨收 178.34 → 收盘 175.40（-1.6%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 0.70 | OI比 1.20 | ATM IV 73.4% | Skew 0.2pp | Term 0.70 | ExpMove ±5.3%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价薄（Skew 0.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.20×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±5.3% ｜ 11-13（10D）±7.8% ｜ 11-20（17D）±9.7% ｜ 11-27（24D）±10.9%
   ⇒ IV–VIX Spread: +52.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -10,716,276 | GEX Change vs 上次快照 8,683,247 | Flip: Primary Flip: 178.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 627 / LOW 74 / INVALID 205
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 178.97（全链重定价，覆盖 100%）
最近结构参考: Flip 179（现价低于该位 2.0%）
量化视角： 负 Gamma（1072万，无历史分位）｜负 Gamma 缓解（+868万）｜现价位于 Flip 下方 1.99%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 188（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 179（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +50.9k / P +102.8k ｜ Activity HIGH ｜ 3D
11-13  C +4.7k / P +3.9k ｜ Activity HIGH ｜ 10D
11-20  C +5.1k / P +6.2k ｜ Activity MEDIUM △ ｜ 17D
11-27  C +1.2k / P +2.4k ｜ Activity HIGH ｜ 24D

📆 11-06 Forward Structure
存量OI: C 172.5k / P 207.5k，今日变化ΔOI: C +50.9k / P +102.8k，平值价格ATM: C $4.90 / P $4.38 ｜ ATM IV 73.4%，净 delta 敞口 -486k shares
仓位参考: Max Pain 188 ｜ Call Wall 187.5（+6.9%，弱）（OI 12.0k） ｜ Put Wall 170（-3.1%，弱）（OI 7.7k）
量化解读： 存量 Put 重｜ATM IV 73.4%｜历史 Rank 94%（近端代理）｜IV/RV 1.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 486,029 股

📆 11-13 Forward Structure
存量OI: C 28.8k / P 27.4k，今日变化ΔOI: C +4.7k / P +3.9k，平值价格ATM: C $7.20 / P $6.47 ｜ ATM IV 59.3%，净 delta 敞口 41k shares
Top ΔOI: P 150 +789 ｜ C 185 +559 ｜ P 170 +552
仓位参考: Max Pain 188 ｜ Call Wall 190（+8.3%，弱）（OI 0.8k） ｜ Put Wall 180（+2.6%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜ATM IV 59.3%｜历史 Rank 94%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,410 股

11-20（MEDIUM △）Top ΔOI: 160P +1,364 ｜ 215C +1,269
11-20（MEDIUM △）仓位参考: Max Pain 178 ｜ Call Wall 165（-5.9%，弱）（OI 11.7k） ｜ Put Wall 180（+2.6%，弱）（OI 11.1k）

📆 11-27 Forward Structure
存量OI: C 11.6k / P 14.2k，今日变化ΔOI: C +1.2k / P +2.4k，平值价格ATM: C $10.10 / P $9.00 ｜ ATM IV 53.1%，净 delta 敞口 13k shares
Top ΔOI: C 205 +323
仓位参考: Max Pain 190 ｜ Call Wall 160（-8.8%，弱）（OI 0.5k） ｜ Put Wall 180（+2.6%，弱）（OI 1.4k）
量化解读： 存量 Put 重｜ATM IV 53.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.16×（近似）｜净 delta 敞口 正 13,332 股

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 73.4% vs 11-13 59.3%（差 +14.1pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/PLTR_evening.json