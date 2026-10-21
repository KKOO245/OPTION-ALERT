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
🟡 **近现价集中开仓**: 10-23 87C ΔOI +245（距现价 +0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 90C ΔOI +1,090 占该期限总 OI 18.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 86.97 → 收盘 86.72（-0.3%） ｜ 今日高 87.17 ｜ 低 85.29 ｜ 昨收 86.10 → 收盘 86.72（+0.7%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-28，窗口结束前不做对错判定）

Options: P/C成交量 0.39 | OI比 1.13 | ATM IV 100.3% | Skew 30.8pp | Term 0.40 | ExpMove ±2.6%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.40，近月 IV 高于远月）｜保护溢价显著（Skew 30.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.39×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.13×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±2.6% ｜ 10-26（5D）±3.3% ｜ 10-28（7D）±4.8% ｜ 10-30（9D）±5.6%
   ⇒ IV–VIX Spread: +83.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 36,699,643 | GEX Change vs 上次快照 8,084,620 | Flip: Primary Flip: 85.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 553 / LOW 150 / INVALID 513
结构观察区: Primary Flip 85.03（全链重定价，覆盖 96%）
Call Wall 90（弱结构｜现价低于该位 3.6%）
最近结构参考: Flip 85（现价高于该位 2.0%）
量化视角： 正 Gamma（3670万，无历史分位）｜正 Gamma 增强（+808万）｜现价位于 Flip 上方 1.99%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 86（MaxPain，仅结算参考）；上方 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +1.4k / P +0.4k ｜ Activity HIGH ｜ 2D
10-26  C +1.3k / P +0.5k ｜ Activity HIGH ｜ 5D
10-28  C +0.4k / P +1.2k ｜ Activity HIGH ｜ 7D
10-30  C +13.5k / P +3.6k ｜ Activity HIGH ｜ 9D

📆 10-23 Forward Structure
存量OI: C 97.6k / P 33.4k，今日变化ΔOI: C +1.4k / P +0.4k，平值价格ATM: C $0.65 / P $1.63 ｜ ATM IV 45.1%，净 delta 敞口 40k shares
Top ΔOI: C 90 +256 ｜ C 87 +245 ｜ C 89 +214
仓位参考: Max Pain 86 ｜ Call Wall 90（+3.8%，弱）（OI 12.1k） ｜ Put Wall 85（-2.0%，弱）（OI 5.4k）
量化解读： 存量 Call 重｜ATM IV 45.1%｜历史 Rank 100%（近端代理）｜IV/RV 1.46×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 39,564 股

📆 10-26 Forward Structure
存量OI: C 4.3k / P 1.6k，今日变化ΔOI: C +1.3k / P +0.5k，平值价格ATM: C $1.28 / P $1.57 ｜ ATM IV 35.0%，净 delta 敞口 11k shares
Top ΔOI: C 90 +1,090 ｜ P 85 +177 ｜ C 88 +159
仓位参考: Max Pain 87 ｜ Call Wall 91（+4.9%，弱）（OI 1.8k） ｜ Put Wall 85（-2.0%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 35.0%｜历史 Rank 100%（近端代理）｜IV/RV 1.13×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 10,787 股

📆 10-28 Forward Structure
存量OI: C 0.8k / P 3.1k，今日变化ΔOI: C +0.4k / P +1.2k，平值价格ATM: C $1.83 / P $2.37 ｜ ATM IV 39.7%，净 delta 敞口 -25k shares
Top ΔOI: P 84 +1,043 ｜ C 90 +173 ｜ C 87 +70
仓位参考: Max Pain 87 ｜ Call Wall 88（+1.5%，弱）（OI 0.2k） ｜ Put Wall 84（-3.1%）（OI 2.1k）
量化解读： 存量 Put 重｜ATM IV 39.7%｜历史 Rank 100%（近端代理）｜IV/RV 1.28×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 24,909 股

📆 10-30 Forward Structure
存量OI: C 40.0k / P 15.8k，今日变化ΔOI: C +13.5k / P +3.6k，平值价格ATM: C $2.48 / P $2.34 ｜ ATM IV 42.5%，净 delta 敞口 355k shares
Top ΔOI: C 91 +6,531 ｜ C 90 +6,424
仓位参考: Max Pain 87 ｜ Call Wall 91（+4.9%）（OI 11.7k） ｜ Put Wall 85（-2.0%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 42.5%｜历史 Rank 100%（近端代理）｜IV/RV 1.37×（近似）｜净 delta 敞口 正 354,958 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/GDX_evening.json