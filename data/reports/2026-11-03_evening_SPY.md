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
🟡 **近现价集中开仓**: 11-04 756P ΔOI +12,398（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 752.73 → 收盘 754.35（+0.2%） ｜ 今日高 757.07 ｜ 低 752.41 ｜ 昨收 752.10 → 收盘 754.35（+0.3%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-10，窗口结束前不做对错判定）

Options: P/C成交量 1.11 | OI比 1.37 | ATM IV 26.7% | Skew -1.9pp | Term 0.63 | ExpMove ±1.2%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.9pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.11×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 25% ｜ P/C OI(近端) 15%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 25%）｜近端持仓结构中性（P/C OI 分位 15%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-04（1D）±1.2% ｜ 11-05（2D）±1.4% ｜ 11-06（3D）±1.7% ｜ 11-09（6D）±1.9%
   ⇒ IV–VIX Spread: +5.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -1,425,548,873 | GEX Change vs 上次快照 65,370,423 | Flip: Primary Flip: 770.66（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 2331 / LOW 381 / INVALID 2392
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 770.66（全链重定价，覆盖 95%）
最近结构参考: Flip 771（现价低于该位 2.1%）
量化视角： 负 Gamma（14.26亿，历史分位 25%，中性区）｜负 Gamma 缓解（+6537万）｜现价位于 Flip 下方 2.12%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 756（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 771（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-04  C +29.3k / P +35.2k ｜ Activity HIGH ｜ 1D
11-05  C +17.6k / P +61.6k ｜ Activity HIGH ｜ 2D
11-06  C +27.6k / P +31.0k ｜ Activity HIGH ｜ 3D
11-09  C +7.0k / P +17.8k ｜ Activity HIGH ｜ 6D

📆 11-04 Forward Structure
存量OI: C 106.0k / P 266.3k，今日变化ΔOI: C +29.3k / P +35.2k，平值价格ATM: C $4.64 / P $4.09 ｜ ATM IV 27.5%，净 delta 敞口 -601k shares
Top ΔOI: P 756 +12,398 ｜ P 755 +5,401 ｜ P 767 -5,341
仓位参考: Max Pain 762 ｜ Call Wall 773（+2.5%，弱）（OI 6.9k） ｜ Put Wall 740（-1.9%，弱）（OI 58.6k）
量化解读： 存量 Put 重｜ATM IV 27.5%｜历史 Rank 95%（近端代理）｜IV/RV 2.60×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 601,399 股

📆 11-05 Forward Structure
存量OI: C 54.5k / P 91.0k，今日变化ΔOI: C +17.6k / P +61.6k，平值价格ATM: C $5.71 / P $5.09 ｜ ATM IV 24.2%，净 delta 敞口 111k shares
Top ΔOI: P 735 +12,076
仓位参考: Max Pain 755 ｜ Call Wall 765（+1.4%，弱）（OI 6.1k） ｜ Put Wall 735（-2.6%）（OI 15.2k）
量化解读： 存量 Put 重｜ATM IV 24.2%｜历史 Rank 95%（近端代理）｜IV/RV 2.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 110,545 股

📆 11-06 Forward Structure
存量OI: C 217.4k / P 419.0k，今日变化ΔOI: C +27.6k / P +31.0k，平值价格ATM: C $6.86 / P $5.97 ｜ ATM IV 23.3%，净 delta 敞口 -279k shares
Top ΔOI: P 750 +4,617 ｜ P 761 +4,230 ｜ P 754 +4,220
仓位参考: Max Pain 762 ｜ Call Wall 770（+2.1%，弱）（OI 15.2k） ｜ Put Wall 750（-0.6%）（OI 43.2k）
量化解读： 存量 Put 重｜ATM IV 23.3%｜历史 Rank 95%（近端代理）｜IV/RV 2.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 279,330 股

📆 11-09 Forward Structure
存量OI: C 25.0k / P 46.9k，今日变化ΔOI: C +7.0k / P +17.8k，平值价格ATM: C $7.74 / P $6.78 ｜ ATM IV 18.8%，净 delta 敞口 -270k shares
Top ΔOI: P 745 +4,700 ｜ C 790 +4,032 ｜ P 755 +3,202
仓位参考: Max Pain 765 ｜ Call Wall 775（+2.7%，弱）（OI 3.8k） ｜ Put Wall 745（-1.2%）（OI 6.7k）
量化解读： 存量 Put 重｜ATM IV 18.8%｜历史 Rank 95%（近端代理）｜IV/RV 1.78×（近似）｜净 delta 敞口 负 270,045 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/SPY_evening.json