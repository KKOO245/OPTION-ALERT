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
🟡 **近现价集中开仓**: 11-04 400P ΔOI +2,199（距现价 +0.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 406.31 → 收盘 398.50（-1.9%） ｜ 今日高 406.49 ｜ 低 396.54 ｜ 昨收 403.82 → 收盘 398.50（-1.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 0.98 | OI比 1.15 | ATM IV 66.7% | Skew 5.3pp | Term 0.66 | ExpMove ±2.8%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.66，近月 IV 高于远月）｜保护溢价中性（Skew 5.3pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.98×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-04（1D）±2.8% ｜ 11-06（3D）±4.4% ｜ 11-09（6D）±5.0% ｜ 11-11（8D）±5.8%
   ⇒ IV–VIX Spread: +45.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 53,227,473 | GEX Change vs 上次快照 -19,853,574 | Flip: Primary Flip: 386.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1382 / LOW 98 / INVALID 724
结构观察区: Primary Flip 386.48（全链重定价，覆盖 100%）
Call Wall 400（弱结构｜现价低于该位 0.4%）
最近结构参考: Call Wall 400（现价低于该位 0.4%）
量化视角： 正 Gamma（5323万，无历史分位）｜正 Gamma 减弱（1985万）｜现价位于 Flip 上方 3.11%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 400（MaxPain，仅结算参考） / 400（Call Wall，弱结构）。
• Gamma 区域：切换参考 386（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-04  C +24.1k / P +27.0k ｜ Activity HIGH ｜ 1D
11-06  C +35.9k / P +46.7k ｜ Activity HIGH ｜ 3D
11-09  C +8.1k / P +3.7k ｜ Activity HIGH ｜ 6D
11-11  C +2.7k / P +1.5k ｜ Activity HIGH ｜ 8D

📆 11-04 Forward Structure
存量OI: C 46.7k / P 53.6k，今日变化ΔOI: C +24.1k / P +27.0k，平值价格ATM: C $5.95 / P $5.25 ｜ ATM IV 66.7%，净 delta 敞口 -295k shares
Top ΔOI: C 420 +3,751 ｜ P 400 +2,199
仓位参考: Max Pain 400 ｜ Call Wall 420（+5.4%）（OI 5.6k） ｜ Put Wall 370（-7.2%，弱）（OI 4.4k）
量化解读： 存量两侧均衡｜ATM IV 66.7%｜历史 Rank 80%（近端代理）｜IV/RV 2.05×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 294,773 股

📆 11-06 Forward Structure
存量OI: C 158.3k / P 252.5k，今日变化ΔOI: C +35.9k / P +46.7k，平值价格ATM: C $9.43 / P $8.10 ｜ ATM IV 60.8%，净 delta 敞口 -509k shares
Top ΔOI: C 440 +7,639 ｜ C 435 +3,988
仓位参考: Max Pain 395 ｜ Call Wall 410（+2.9%，弱）（OI 10.2k） ｜ Put Wall 380（-4.6%，弱）（OI 10.4k）
量化解读： 存量 Put 重｜ATM IV 60.8%｜历史 Rank 80%（近端代理）｜IV/RV 1.87×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 509,162 股

📆 11-09 Forward Structure
存量OI: C 13.6k / P 9.6k，今日变化ΔOI: C +8.1k / P +3.7k，平值价格ATM: C $10.40 / P $9.32 ｜ ATM IV 49.3%，净 delta 敞口 -8k shares
Top ΔOI: C 420 +927
仓位参考: Max Pain 400 ｜ Call Wall 420（+5.4%）（OI 1.8k） ｜ Put Wall 380（-4.6%）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 49.3%｜历史 Rank 80%（近端代理）｜IV/RV 1.51×（近似）｜净 delta 敞口 负 7,615 股

📆 11-11 Forward Structure
存量OI: C 7.6k / P 4.3k，今日变化ΔOI: C +2.7k / P +1.5k，平值价格ATM: C $12.50 / P $10.80 ｜ ATM IV 49.5%，净 delta 敞口 -33k shares
Top ΔOI: P 405 +475 ｜ C 410 +425
仓位参考: Max Pain 400 ｜ Call Wall 405（+1.6%，弱）（OI 0.7k） ｜ Put Wall 405（+1.6%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 49.5%｜历史 Rank 80%（近端代理）｜IV/RV 1.52×（近似）｜净 delta 敞口 负 33,318 股

📅 事件差分（观察，非因果）: 11-04（1D）ATM IV 66.7% vs 11-06 60.8%（差 +5.9pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/TSLA_evening.json