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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-04 47C ΔOI +2,566（距现价 +4.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SLV: 今开 45.08 → 收盘 44.84（-0.5%） ｜ 今日高 45.25 ｜ 低 44.58 ｜ 昨收 45.57 → 收盘 44.84（-1.6%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-11-06，窗口结束前不做对错判定）

Options: P/C成交量 0.50 | OI比 0.39 | ATM IV 56.5% | Skew 4.6pp | Term 0.74 | ExpMove ±2.4%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价中性（Skew 4.6pp）｜存量 Call 偏重（OI比 0.39）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.39×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-04（1D）±2.4% ｜ 11-06（3D）±4.0% ｜ 11-09（6D）±4.4% ｜ 11-11（8D）±5.7%
   ⇒ IV–VIX Spread: +35.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -5,576,640 | GEX Change vs 上次快照 -7,640,212 | Flip: Primary Flip: 45.11（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 678 / LOW 119 / INVALID 351
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 45.11（全链重定价，覆盖 99%）
Put Wall 45（弱结构｜现价低于该位 0.4%）
最近结构参考: Put Wall 45（现价低于该位 0.4%）
量化视角： 负 Gamma（558万，无历史分位）｜由正转负（764万）｜现价位于 Flip 下方 0.59%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 45（Put Wall，弱结构） / 45（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 45（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-04  C +8.5k / P +3.7k ｜ Activity HIGH ｜ 1D
11-06  C +4.6k / P +3.7k ｜ Activity HIGH ｜ 3D
11-09  C +1.8k / P +1.4k ｜ Activity HIGH ｜ 6D
11-11  C +1.0k / P +0.4k ｜ Activity HIGH ｜ 8D

📆 11-04 Forward Structure
存量OI: C 32.7k / P 12.9k，今日变化ΔOI: C +8.5k / P +3.7k，平值价格ATM: C $0.45 / P $0.62 ｜ ATM IV 56.5%，净 delta 敞口 -21k shares
Top ΔOI: C 47 +2,566 ｜ C 46 +1,156 ｜ C 49 +1,033
仓位参考: Max Pain 45 ｜ Call Wall 47（+4.8%，弱）（OI 3.2k） ｜ Put Wall 44（-1.9%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜ATM IV 56.5%｜历史 Rank 89%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 21,196 股

📆 11-06 Forward Structure
存量OI: C 142.1k / P 40.3k，今日变化ΔOI: C +4.6k / P +3.7k，平值价格ATM: C $0.81 / P $0.97 ｜ ATM IV 53.8%，净 delta 敞口 73k shares
Top ΔOI: C 49 +1,202 ｜ C 47 +1,132
仓位参考: Max Pain 48 ｜ Put Wall 45（+0.4%，弱）（OI 4.6k）
量化解读： 存量 Call 重｜ATM IV 53.8%｜历史 Rank 89%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 73,255 股

📆 11-09 Forward Structure
存量OI: C 4.6k / P 3.5k，今日变化ΔOI: C +1.8k / P +1.4k，平值价格ATM: C $0.91 / P $1.06 ｜ ATM IV 43.3%，净 delta 敞口 -8k shares
Top ΔOI: C 47 +564 ｜ P 45 +303
仓位参考: Max Pain 46 ｜ Call Wall 47（+4.8%，弱）（OI 1.0k） ｜ Put Wall 43（-4.1%）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 43.3%｜历史 Rank 89%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 负 7,650 股

📆 11-11 Forward Structure
存量OI: C 5.9k / P 1.9k，今日变化ΔOI: C +1.0k / P +0.4k，平值价格ATM: C $1.14 / P $1.41 ｜ ATM IV 45.3%，净 delta 敞口 1k shares
Top ΔOI: C 49 +182 ｜ P 44 +173
仓位参考: Max Pain 45 ｜ Call Wall 47（+4.8%，弱）（OI 0.6k） ｜ Put Wall 45（+0.4%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 45.3%｜历史 Rank 89%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 正 1,069 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=72 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=72）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/SLV_evening.json