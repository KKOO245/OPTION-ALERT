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
🟡 **事件差分**: 11-06 ATM IV 70.3% vs 11-13 59.1%（差 +11.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 455P ΔOI +494（距现价 -2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 490C ΔOI +9,598 占该期限总 OI 18.2%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 466.01 → 收盘 465.00（-0.2%） ｜ 今日高 472.63 ｜ 低 461.83 ｜ 昨收 453.65 → 收盘 465.00（+2.5%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-06，窗口结束前不做对错判定）

Options: P/C成交量 1.84 | OI比 1.37 | ATM IV 70.3% | Skew -0.6pp | Term 0.70 | ExpMove ±5.2%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.84×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±5.2% ｜ 11-13（10D）±7.8% ｜ 11-20（17D）±9.6% ｜ 11-27（24D）±10.5%
   ⇒ IV–VIX Spread: +49.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,236,251 | GEX Change vs 上次快照 255,234 | Flip: Primary Flip: 484.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 567 / LOW 217 / INVALID 768
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 484.85（全链重定价，覆盖 96%）
最近结构参考: Flip 485（现价低于该位 4.1%）
量化视角： 负 Gamma（1424万，无历史分位）｜负 Gamma 缓解（+26万）｜现价位于 Flip 下方 4.09%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 495（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 485（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-06  C +0.8k / P +1.7k ｜ Activity MEDIUM △ ｜ 3D
11-13  C +4.5k / P +13.7k ｜ Activity HIGH ｜ 10D
11-20  C +6.0k / P +1.8k ｜ Activity HIGH ｜ 17D
11-27  C +0.2k / P +91 ｜ Activity MEDIUM △ ｜ 24D

📆 11-06 Forward Structure
存量OI: C 43.4k / P 59.7k，今日变化ΔOI: C +0.8k / P +1.7k，平值价格ATM: C $12.09 / P $12.06 ｜ ATM IV 70.3%，净 delta 敞口 -570 shares
Top ΔOI: P 430 +790 ｜ P 455 +494 ｜ P 450 -315
仓位参考: Max Pain 495
量化解读： 存量 Put 重｜ATM IV 70.3%｜历史 Rank 97%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 570 股

📆 11-13 Forward Structure
存量OI: C 30.2k / P 22.6k，今日变化ΔOI: C +4.5k / P +13.7k，平值价格ATM: C $18.50 / P $17.76 ｜ ATM IV 59.1%，净 delta 敞口 -4k shares
Top ΔOI: C 490 +9,598 ｜ C 510 -5,379 ｜ P 415 +4,470
仓位参考: Max Pain 490 ｜ Call Wall 490（+5.4%，弱）（OI 9.6k） ｜ Put Wall 460（-1.1%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 59.1%｜历史 Rank 97%（近端代理）｜IV/RV 1.16×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,275 股

📆 11-20 Forward Structure
存量OI: C 56.8k / P 77.7k，今日变化ΔOI: C +6.0k / P +1.8k，平值价格ATM: C $21.85 / P $22.60 ｜ ATM IV 55.8%，净 delta 敞口 282k shares
Top ΔOI: P 400 +2,135 ｜ C 495 +2,054 ｜ C 490 +1,072
仓位参考: Max Pain 500 ｜ Call Wall 495（+6.5%，弱）（OI 2.1k） ｜ Put Wall 460（-1.1%，弱）（OI 7.7k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 55.8%｜历史 Rank 97%（近端代理）｜IV/RV 1.09×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 282,203 股

11-27（MEDIUM △）Top ΔOI: 500C +166
11-27（MEDIUM △）仓位参考: Max Pain 500 ｜ Put Wall 490（+5.4%，弱）（OI 1.1k）

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 70.3% vs 11-13 59.1%（差 +11.2pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=72 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=72）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/SOXX_evening.json