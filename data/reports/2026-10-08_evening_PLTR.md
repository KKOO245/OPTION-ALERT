# 期权晚报 2026-10-08（快照 16:40 ET）

📊 市场环境

SPY $773.93 ｜ QQQ $747.58
VIX 15.41 ↑2.2%（5D -6.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 195C ΔOI -1,248（距现价 -1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
PLTR: 今开 199.00 → 收盘 198.78（-0.1%） ｜ 今日高 204.44 ｜ 低 195.65 ｜ 昨收 194.12 → 收盘 198.78（+2.4%）
Target 等待验证: 3D_mdd >= 0.03（3D） — PENDING（评估日 ≈ 2026-10-13，窗口结束前不做对错判定）

Options: P/C成交量 0.39 | OI比 0.64 | ATM IV 47.5% | Skew 0.1pp | Term 1.20 | ExpMove ±2.0%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构正常偏陡（Term 1.20）｜保护溢价薄（Skew 0.1pp）｜存量 Call 偏重（OI比 0.64）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.64×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.0% ｜ 10-16（8D）±5.1% ｜ 10-23（15D）±6.8% ｜ 10-30（22D）±8.4%
   ⇒ IV–VIX Spread: +32.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 137,384,970 | GEX Change vs 上次快照 5,057,411 | Flip: Primary Flip: 185.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 554 / LOW 105 / INVALID 159
结构观察区: Primary Flip 185.56（全链重定价，覆盖 99%）
Call Wall 200（弱结构｜现价低于该位 0.6%）
最近结构参考: Call Wall 200（现价低于该位 0.6%）
量化视角： 正 Gamma（1.37亿，无历史分位）｜正 Gamma 增强（+506万）｜现价位于 Flip 上方 7.13%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 188（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 186（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-09  C +2.7k / P +0.5k ｜ Activity MEDIUM △ ｜ 1D
10-16  C +3.4k / P +5.2k ｜ Activity MEDIUM △ ｜ 8D
10-23  C +1.1k / P +1.0k ｜ Activity HIGH ｜ 15D
10-30  C +0.5k / P +1.6k ｜ Activity HIGH ｜ 22D

📆 10-09 Forward Structure
存量OI: C 125.1k / P 79.6k，今日变化ΔOI: C +2.7k / P +0.5k，平值价格ATM: C $1.44 / P $2.64 ｜ ATM IV 47.5%，净 delta 敞口 -20k shares
Top ΔOI: C 205 +1,866 ｜ C 195 -1,248 ｜ P 190 -1,245
仓位参考: Max Pain 188 ｜ Call Wall 205（+3.1%，弱）（OI 22.4k） ｜ Put Wall 185（-6.9%，弱）（OI 8.9k）
量化解读： 存量 Call 重｜ATM IV 47.5%｜历史 Rank 36%（近端代理）｜IV/RV 2.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 20,353 股

10-16（MEDIUM △）Top ΔOI: 192P +1,710 ｜ 205C +1,273
10-16（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 200（+0.6%）（OI 17.6k） ｜ Put Wall 180（-9.4%，弱）（OI 5.4k）

📆 10-23 Forward Structure
存量OI: C 26.2k / P 20.3k，今日变化ΔOI: C +1.1k / P +1.0k，平值价格ATM: C $6.25 / P $7.25 ｜ ATM IV 42.0%，净 delta 敞口 33k shares
Top ΔOI: C 200 +569 ｜ C 205 +255
仓位参考: Max Pain 180 ｜ Call Wall 180（-9.4%）（OI 4.7k） ｜ Put Wall 180（-9.4%，弱）（OI 0.7k）
量化解读： 存量 Call 重｜ATM IV 42.0%｜历史 Rank 36%（近端代理）｜IV/RV 2.13×（近似）｜净 delta 敞口 正 32,915 股

📆 10-30 Forward Structure
存量OI: C 28.2k / P 20.1k，今日变化ΔOI: C +0.5k / P +1.6k，平值价格ATM: C $7.94 / P $8.70 ｜ ATM IV 42.5%，净 delta 敞口 -25k shares
Top ΔOI: P 190 +1,007 ｜ P 180 +301 ｜ C 200 -242
仓位参考: Max Pain 185 ｜ Call Wall 200（+0.6%，弱）（OI 3.1k） ｜ Put Wall 180（-9.4%，弱）（OI 2.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.5%｜历史 Rank 36%（近端代理）｜IV/RV 2.16×（近似）｜净 delta 敞口 负 24,708 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/PLTR_evening.json