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
🟡 **近现价集中开仓**: 10-26 155C ΔOI +1,312（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-28 144P ΔOI +2,981 占该期限总 OI 18.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SPCX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SPCX: 今开 160.56 → 收盘 159.31（-0.8%） ｜ 今日高 166.18 ｜ 低 156.93 ｜ 昨收 147.79 → 收盘 159.31（+7.8%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-28，窗口结束前不做对错判定）

Options: P/C成交量 0.66 | OI比 1.08 | ATM IV 80.8% | Skew 21.3pp | Term 0.64 | ExpMove ±4.2%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.64，近月 IV 高于远月）｜保护溢价显著（Skew 21.3pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.66×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.08×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±4.2% ｜ 10-26（5D）±5.0% ｜ 10-28（7D）±6.0% ｜ 10-30（9D）±7.0%
   ⇒ IV–VIX Spread: +64.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 105,088,353 | GEX Change vs 上次快照 -27,324,780 | Flip: Primary Flip: 148.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 844 / LOW 165 / INVALID 577
结构观察区: Primary Flip 148.90（全链重定价，覆盖 94%）
Call Wall 170（弱结构｜现价低于该位 6.3%）
最近结构参考: Call Wall 170（现价低于该位 6.3%）
量化视角： 正 Gamma（1.05亿，无历史分位）｜正 Gamma 减弱（2732万）｜现价位于 Flip 上方 6.99%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 147（MaxPain，仅结算参考）；上方 170（Call Wall，弱结构）。
• Gamma 区域：切换参考 149（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +35.2k / P +31.2k ｜ Activity HIGH ｜ 2D
10-26  C +6.8k / P +5.0k ｜ Activity HIGH ｜ 5D
10-28  C +1.7k / P +3.1k ｜ Activity HIGH ｜ 7D
10-30  C +10.2k / P +10.3k ｜ Activity HIGH ｜ 9D

📆 10-23 Forward Structure
存量OI: C 188.6k / P 183.7k，今日变化ΔOI: C +35.2k / P +31.2k，平值价格ATM: C $3.05 / P $3.70 ｜ ATM IV 70.7%，净 delta 敞口 1.2M shares
Top ΔOI: P 140 +5,966 ｜ C 170 +5,345
仓位参考: Max Pain 149 ｜ Call Wall 170（+6.7%）（OI 26.7k） ｜ Put Wall 145（-9.0%，弱）（OI 10.4k）
量化解读： 存量两侧均衡｜ATM IV 70.7%｜历史 Rank 95%（近端代理）｜IV/RV 1.45×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,247,420 股

📆 10-26 Forward Structure
存量OI: C 16.0k / P 10.6k，今日变化ΔOI: C +6.8k / P +5.0k，平值价格ATM: C $3.69 / P $4.26 ｜ ATM IV 52.8%，净 delta 敞口 321k shares
Top ΔOI: C 155 +1,312 ｜ C 170 +981 ｜ C 175 +714
仓位参考: Max Pain 147 ｜ Call Wall 155（-2.7%，弱）（OI 2.2k） ｜ Put Wall 144（-9.6%，弱）（OI 0.9k）
量化解读： 存量 Call 重｜ATM IV 52.8%｜历史 Rank 95%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 320,970 股

📆 10-28 Forward Structure
存量OI: C 4.4k / P 11.5k，今日变化ΔOI: C +1.7k / P +3.1k，平值价格ATM: C $4.52 / P $5.10 ｜ ATM IV 53.5%，净 delta 敞口 91k shares
Top ΔOI: P 144 +2,981 ｜ P 148 -510 ｜ C 148 +152
仓位参考: Max Pain 148 ｜ Call Wall 165（+3.6%，弱）（OI 0.5k） ｜ Put Wall 148（-7.1%，弱）（OI 3.6k）
量化解读： 存量 Put 重｜ATM IV 53.5%｜历史 Rank 95%（近端代理）｜IV/RV 1.10×（近似）｜净 delta 敞口 正 91,424 股

📆 10-30 Forward Structure
存量OI: C 141.8k / P 102.7k，今日变化ΔOI: C +10.2k / P +10.3k，平值价格ATM: C $5.25 / P $5.90 ｜ ATM IV 55.1%，净 delta 敞口 615k shares
Top ΔOI: C 190 -5,126 ｜ C 162 +3,956
仓位参考: Max Pain 155 ｜ Call Wall 172.5（+8.3%，弱）（OI 13.6k） ｜ Put Wall 150（-5.8%，弱）（OI 7.7k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 55.1%｜历史 Rank 95%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 正 615,135 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/SPCX_evening.json