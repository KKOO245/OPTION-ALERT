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
🟡 **近现价集中开仓**: 10-23 220C ΔOI +5,307（距现价 -0.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NVDA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NVDA: 今开 220.96 → 收盘 221.97（+0.5%） ｜ 今日高 222.19 ｜ 低 217.66 ｜ 昨收 216.47 → 收盘 221.97（+2.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-28，窗口结束前不做对错判定）

Options: P/C成交量 0.61 | OI比 0.76 | ATM IV 82.8% | Skew 3.6pp | Term 0.47 | ExpMove ±2.2%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.47，近月 IV 高于远月）｜保护溢价中性（Skew 3.6pp）｜存量 Call 偏重（OI比 0.76）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-23（2D）±2.2% ｜ 10-26（5D）±2.8% ｜ 10-28（7D）±3.6% ｜ 10-30（9D）±4.2%
   ⇒ IV–VIX Spread: +66.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 380,748,165 | GEX Change vs 上次快照 23,701,971 | Flip: Primary Flip: 212.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 693 / LOW 226 / INVALID 643
结构观察区: Primary Flip 212.22（全链重定价，覆盖 96%）
Call Wall 230（弱结构｜现价低于该位 3.5%）
最近结构参考: Call Wall 230（现价低于该位 3.5%）
量化视角： 正 Gamma（3.81亿，无历史分位）｜正 Gamma 增强（+2370万）｜现价位于 Flip 上方 4.60%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 218（MaxPain，仅结算参考）；上方 230（Call Wall，弱结构）。
• Gamma 区域：切换参考 212（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +21.7k / P +11.0k ｜ Activity HIGH ｜ 2D
10-26  C +9.6k / P +11.4k ｜ Activity HIGH ｜ 5D
10-28  C +3.3k / P +3.3k ｜ Activity HIGH ｜ 7D
10-30  C +18.4k / P +12.8k ｜ Activity HIGH ｜ 9D

📆 10-23 Forward Structure
存量OI: C 441.7k / P 355.4k，今日变化ΔOI: C +21.7k / P +11.0k，平值价格ATM: C $2.22 / P $2.70 ｜ ATM IV 36.9%，净 delta 敞口 1.1M shares
Top ΔOI: C 220 +5,307 ｜ C 222 +3,409
仓位参考: Max Pain 220 ｜ Call Wall 240（+8.1%，弱）（OI 58.3k） ｜ Put Wall 210（-5.4%，弱）（OI 18.6k）
量化解读： 存量 Call 重｜ATM IV 36.9%｜历史 Rank 94%（近端代理）｜IV/RV 1.67×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,081,602 股

📆 10-26 Forward Structure
存量OI: C 39.7k / P 32.0k，今日变化ΔOI: C +9.6k / P +11.4k，平值价格ATM: C $2.86 / P $3.30 ｜ ATM IV 29.6%，净 delta 敞口 217k shares
Top ΔOI: P 200 +2,480 ｜ P 210 +1,738 ｜ P 220 +1,502
仓位参考: Max Pain 218 ｜ Call Wall 237.5（+7.0%）（OI 10.1k） ｜ Put Wall 200（-9.9%）（OI 7.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 29.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.34×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 216,823 股

📆 10-28 Forward Structure
存量OI: C 13.5k / P 12.4k，今日变化ΔOI: C +3.3k / P +3.3k，平值价格ATM: C $3.85 / P $4.15 ｜ ATM IV 32.6%，净 delta 敞口 103k shares
Top ΔOI: P 212 +1,227 ｜ C 222 +505 ｜ C 220 +503
仓位参考: Max Pain 218 ｜ Call Wall 230（+3.6%）（OI 4.8k） ｜ Put Wall 215（-3.1%，弱）（OI 1.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 32.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.48×（近似）｜净 delta 敞口 正 103,163 股

📆 10-30 Forward Structure
存量OI: C 194.8k / P 169.4k，今日变化ΔOI: C +18.4k / P +12.8k，平值价格ATM: C $4.59 / P $4.80 ｜ ATM IV 33.8%，净 delta 敞口 464k shares
Top ΔOI: C 220 +3,755 ｜ C 230 +3,568
仓位参考: Max Pain 220 ｜ Call Wall 240（+8.1%）（OI 27.7k） ｜ Put Wall 200（-9.9%，弱）（OI 12.4k）
量化解读： 存量两侧均衡｜ATM IV 33.8%｜历史 Rank 94%（近端代理）｜IV/RV 1.53×（近似）｜净 delta 敞口 正 464,052 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/NVDA_evening.json