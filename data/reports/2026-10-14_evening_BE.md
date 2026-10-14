# 期权晚报 2026-10-14（快照 16:42 ET）

📊 市场环境

SPY $769.60 ｜ QQQ $728.95
VIX 16.87 ↑10.5%（5D +11.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 237P ΔOI +339（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 257.50 → 收盘 239.34（-7.1%） ｜ 今日高 258.52 ｜ 低 235.70 ｜ 昨收 263.45 → 收盘 239.34（-9.2%）
Target 等待验证: 3D 收盘涨跌 <= -0.02（3D） — PENDING（评估日 ≈ 2026-10-19，窗口结束前不做对错判定）

Options: P/C成交量 0.82 | OI比 1.06 | ATM IV 100.6% | Skew 2.0pp | Term 0.85 | ExpMove ±6.0%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜保护溢价中性（Skew 2.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.06×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±6.0% ｜ 10-23（9D）±12.9% ｜ 10-30（16D）±15.5% ｜ 11-06（23D）±17.8%
   ⇒ IV–VIX Spread: +83.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -13,328,644 | GEX Change vs 上次快照 -3,421,726 | Flip: Primary Flip: 258.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 621 / LOW 79 / INVALID 180
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 258.03（全链重定价，覆盖 97%）
Put Wall 240（弱结构｜现价低于该位 0.3%）
最近结构参考: Put Wall 240（现价低于该位 0.3%）
量化视角： 负 Gamma（1333万，无历史分位）｜负 Gamma 加深（342万）｜现价位于 Flip 下方 7.24%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 240（Put Wall，弱结构） / 265（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 258（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-16  C +1.9k / P +0.7k ｜ Activity MEDIUM △ ｜ 2D
10-23  C +5.6k / P +3.8k ｜ Activity HIGH ｜ 9D
10-30  C +0.3k / P +0.9k ｜ Activity MEDIUM △ ｜ 16D
11-06  C +0.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 23D

📆 10-16 Forward Structure
存量OI: C 98.8k / P 104.3k，今日变化ΔOI: C +1.9k / P +0.7k，平值价格ATM: C $6.85 / P $7.60 ｜ ATM IV 100.6%，净 delta 敞口 56k shares
Top ΔOI: C 255 +657 ｜ P 237 +339
仓位参考: Max Pain 265 ｜ Call Wall 260（+8.6%，弱）（OI 2.9k） ｜ Put Wall 260（+8.6%，弱）（OI 4.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 100.6%｜历史 Rank 63%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 56,039 股

📆 10-23 Forward Structure
存量OI: C 25.4k / P 26.1k，今日变化ΔOI: C +5.6k / P +3.8k，平值价格ATM: C $15.15 / P $15.73 ｜ ATM IV 102.8%，净 delta 敞口 -53k shares
Top ΔOI: C 260 +1,913 ｜ P 255 +1,013 ｜ P 240 +805
仓位参考: Max Pain 260 ｜ Call Wall 260（+8.6%，弱）（OI 2.3k） ｜ Put Wall 240（+0.3%，弱）（OI 2.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 102.8%｜历史 Rank 63%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 52,975 股

10-30（MEDIUM △）Top ΔOI: 240P +372
10-30（MEDIUM △）仓位参考: Max Pain 280 ｜ Call Wall 250（+4.5%，弱）（OI 0.4k） ｜ Put Wall 230（-3.9%，弱）（OI 3.0k）

11-06（MEDIUM △）Top ΔOI: 270P +88 ｜ 275P +62
11-06（MEDIUM △）仓位参考: Max Pain 270 ｜ Call Wall 260（+8.6%，弱）（OI 0.4k） ｜ Put Wall 235（-1.8%，弱）（OI 2.3k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/BE_evening.json