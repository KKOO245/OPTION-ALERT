# 期权晚报 2026-10-21（快照 16:40 ET）

📊 市场环境

SPY $773.09 ｜ QQQ $725.20
VIX 16.68 ↓3.6%（5D -1.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 227C ΔOI +619（距现价 -4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 235.36 → 收盘 238.53（+1.3%） ｜ 今日高 241.37 ｜ 低 229.30 ｜ 昨收 222.65 → 收盘 238.53（+7.1%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-28，窗口结束前不做对错判定）

Options: P/C成交量 0.80 | OI比 0.85 | ATM IV 166.1% | Skew 2.7pp | Term 0.51 | ExpMove ±9.8%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.51，近月 IV 高于远月）｜保护溢价中性（Skew 2.7pp）｜存量 Call 偏重（OI比 0.85）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.80×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±9.8% ｜ 10-30（9D）±13.2% ｜ 11-06（16D）±15.6% ｜ 11-13（23D）±17.8%
   ⇒ IV–VIX Spread: +149.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,170,437 | GEX Change vs 上次快照 1,039,919 | Flip: Primary Flip: 244.94（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 696 / LOW 49 / INVALID 111
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 244.94（全链重定价，覆盖 100%）
最近结构参考: Flip 245（现价低于该位 2.6%）
量化视角： 负 Gamma（217万，无历史分位）｜负 Gamma 缓解（+104万）｜现价位于 Flip 下方 2.62%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 240（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 245（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +5.0k / P +3.7k ｜ Activity HIGH ｜ 2D
10-30  C +1.3k / P +1.3k ｜ Activity HIGH ｜ 9D
11-06  C +1.1k / P -0.3k ｜ Activity HIGH ｜ 16D
11-13  C +0.4k / P +0.8k ｜ Activity HIGH ｜ 23D

📆 10-23 Forward Structure
存量OI: C 52.6k / P 44.5k，今日变化ΔOI: C +5.0k / P +3.7k，平值价格ATM: C $12.55 / P $10.95 ｜ ATM IV 166.1%，净 delta 敞口 213k shares
Top ΔOI: C 227 +619 ｜ P 200 +585 ｜ P 222 +424
仓位参考: Max Pain 240 ｜ Call Wall 260（+9.0%，弱）（OI 3.7k） ｜ Put Wall 230（-3.6%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 166.1%｜历史 Rank 94%（近端代理）｜IV/RV 2.32×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 213,217 股

📆 10-30 Forward Structure
存量OI: C 20.3k / P 26.1k，今日变化ΔOI: C +1.3k / P +1.3k，平值价格ATM: C $16.58 / P $14.80 ｜ ATM IV 104.1%，净 delta 敞口 9k shares
仓位参考: Max Pain 250 ｜ Call Wall 240（+0.6%，弱）（OI 1.4k） ｜ Put Wall 240（+0.6%，弱）（OI 1.6k）
量化解读： 存量 Put 重｜ATM IV 104.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 9,497 股

📆 11-06 Forward Structure
存量OI: C 8.0k / P 11.6k，今日变化ΔOI: C +1.1k / P -0.3k，平值价格ATM: C $19.70 / P $17.49 ｜ ATM IV 93.8%，净 delta 敞口 97k shares
Top ΔOI: P 235 -932 ｜ C 225 +931
仓位参考: Max Pain 250 ｜ Call Wall 225（-5.7%）（OI 1.0k） ｜ Put Wall 235（-1.5%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 93.8%｜历史 Rank 94%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 97,287 股

📆 11-13 Forward Structure
存量OI: C 4.9k / P 8.8k，今日变化ΔOI: C +0.4k / P +0.8k，平值价格ATM: C $21.13 / P $21.41 ｜ ATM IV 87.2%，净 delta 敞口 -1k shares
Top ΔOI: P 230 +458 ｜ P 200 +270 ｜ C 220 +190
仓位参考: Max Pain 250 ｜ Call Wall 240（+0.6%，弱）（OI 0.6k） ｜ Put Wall 230（-3.6%）（OI 2.7k）
量化解读： 存量 Put 重｜ATM IV 87.2%｜历史 Rank 94%（近端代理）｜IV/RV 1.22×（近似）｜净 delta 敞口 负 1,482 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/BE_evening.json