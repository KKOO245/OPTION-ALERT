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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-22 782C ΔOI +4,118（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 766P ΔOI +19,508 占该期限总 OI 11.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPY

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPY: 今开 771.17 → 收盘 773.09（+0.2%） ｜ 今日高 774.43 ｜ 低 768.40 ｜ 昨收 769.05 → 收盘 773.09（+0.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-28，窗口结束前不做对错判定）

Options: P/C成交量 0.94 | OI比 1.74 | ATM IV 24.9% | Skew 0.7pp | Term 0.54 | ExpMove ±0.5%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.54，近月 IV 高于远月）｜保护溢价薄（Skew 0.7pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.94×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.74×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 50% ｜ P/C OI(近端) 42%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 50%）｜近端持仓结构中性（P/C OI 分位 42%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-22（1D）±0.5% ｜ 10-23（2D）±0.8% ｜ 10-26（5D）±1.0% ｜ 10-27（6D）±1.2%
   ⇒ IV–VIX Spread: +8.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -281,488,965 | GEX Change vs 上次快照 375,117,453 | Flip: Primary Flip: 774.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 3283 / LOW 361 / INVALID 1658
结构观察区: Primary Flip 774.67（全链重定价，覆盖 96%）
最近结构参考: Flip 775（现价低于该位 0.2%）
量化视角： 负 Gamma（2.81亿，历史分位 50%，中性区）｜负 Gamma 缓解（+3.75亿）｜现价位于 Flip 下方 0.20%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 769（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 775（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-22  C +24.4k / P +19.4k ｜ Activity HIGH ｜ 1D
10-23  C +40.7k / P +1.6k ｜ Activity HIGH ｜ 2D
10-26  C +6.8k / P +38.8k ｜ Activity HIGH ｜ 5D
10-27  C +9.4k / P +8.8k ｜ Activity HIGH ｜ 6D

📆 10-22 Forward Structure
存量OI: C 101.8k / P 108.8k，今日变化ΔOI: C +24.4k / P +19.4k，平值价格ATM: C $2.23 / P $1.98 ｜ ATM IV 12.9%，净 delta 敞口 501k shares
Top ΔOI: C 782 +4,118 ｜ C 770 +2,227 ｜ C 783 +2,076
仓位参考: Max Pain 769 ｜ Call Wall 784（+1.4%，弱）（OI 7.8k） ｜ Put Wall 760（-1.7%，弱）（OI 2.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 12.9%｜历史 Rank 94%（近端代理）｜IV/RV 1.62×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 500,622 股

📆 10-23 Forward Structure
存量OI: C 327.8k / P 574.3k，今日变化ΔOI: C +40.7k / P +1.6k，平值价格ATM: C $3.27 / P $2.74 ｜ ATM IV 13.1%，净 delta 敞口 818k shares
Top ΔOI: C 788 +12,449 ｜ P 761 -5,992 ｜ P 740 -3,880
仓位参考: Max Pain 770 ｜ Call Wall 790（+2.2%）（OI 36.0k） ｜ Put Wall 769（-0.5%，弱）（OI 30.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 13.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.64×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 818,219 股

📆 10-26 Forward Structure
存量OI: C 69.6k / P 107.1k，今日变化ΔOI: C +6.8k / P +38.8k，平值价格ATM: C $4.26 / P $3.51 ｜ ATM IV 10.5%，净 delta 敞口 -446k shares
Top ΔOI: P 766 +19,508 ｜ P 762 +8,135 ｜ P 743 +1,314
仓位参考: Max Pain 769 ｜ Call Wall 780（+0.9%，弱）（OI 4.0k） ｜ Put Wall 766（-0.9%，弱）（OI 20.1k）
量化解读： 存量 Put 重｜ATM IV 10.5%｜历史 Rank 94%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 负 445,765 股

📆 10-27 Forward Structure
存量OI: C 41.5k / P 43.0k，今日变化ΔOI: C +9.4k / P +8.8k，平值价格ATM: C $4.97 / P $4.00 ｜ ATM IV 11.0%，净 delta 敞口 168k shares
Top ΔOI: C 801 +1,490 ｜ P 715 +1,164 ｜ C 796 +1,103
仓位参考: Max Pain 768 ｜ Call Wall 787（+1.8%，弱）（OI 2.3k） ｜ Put Wall 765（-1.0%，弱）（OI 1.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 11.0%｜历史 Rank 94%（近端代理）｜IV/RV 1.38×（近似）｜净 delta 敞口 正 167,980 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location below_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/SPY_evening.json