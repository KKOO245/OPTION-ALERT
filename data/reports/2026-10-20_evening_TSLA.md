# 期权晚报 2026-10-20（快照 16:40 ET）

📊 市场环境

SPY $769.05 ｜ QQQ $717.63
VIX 17.31 ↓6.1%（5D +13.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 10-23（3D）ATM IV 89.2% vs 10-26 66.9%（差 +22.3pp），覆盖 建筑许可 Prel、新屋开工
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 10-26 455C ΔOI +6,026 占该期限总 OI 17.6%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## TSLA

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
TSLA: 今开 370.35 → 收盘 373.71（+0.9%） ｜ 今日高 377.59 ｜ 低 363.64 ｜ 昨收 368.06 → 收盘 373.71（+1.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-27，窗口结束前不做对错判定）

Options: P/C成交量 0.62 | OI比 0.90 | ATM IV 89.2% | Skew 0.4pp | Term 0.51 | ExpMove ±6.5%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.51，近月 IV 高于远月）｜保护溢价薄（Skew 0.4pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（3D）±6.5% ｜ 10-26（6D）±6.9% ｜ 10-28（8D）±7.4% ｜ 10-30（10D）±7.8%
   ⇒ IV–VIX Spread: +71.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 59,199,331 | GEX Change vs 上次快照 7,772,447 | Flip: Primary Flip: 348.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1306 / LOW 70 / INVALID 656
结构观察区: Primary Flip 348.90（全链重定价，覆盖 100%）
Call Wall 400（现价低于该位 6.6%）
最近结构参考: Call Wall 400（现价低于该位 6.6%）
量化视角： 正 Gamma（5920万，无历史分位）｜正 Gamma 增强（+777万）｜现价位于 Flip 上方 7.11%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 365（MaxPain，仅结算参考）；上方 400（Call Wall）。
• Gamma 区域：切换参考 349（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

10-23  C +46.4k / P +41.5k ｜ Activity HIGH ｜ 3D
10-26  C +11.5k / P +2.3k ｜ Activity HIGH ｜ 6D
10-28  C +1.3k / P +1.5k ｜ Activity HIGH ｜ 8D
10-30  C +5.0k / P +8.3k ｜ Activity HIGH ｜ 10D

📆 10-23 Forward Structure
存量OI: C 210.1k / P 189.5k，今日变化ΔOI: C +46.4k / P +41.5k，平值价格ATM: C $12.78 / P $11.45 ｜ ATM IV 89.2%，净 delta 敞口 612k shares
Top ΔOI: C 405 +4,941
仓位参考: Max Pain 365 ｜ Call Wall 400（+7.0%，弱）（OI 14.0k）
量化解读： 存量两侧均衡｜ATM IV 89.2%｜历史 Rank 94%（近端代理）｜IV/RV 2.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 611,677 股

📆 10-26 Forward Structure
存量OI: C 21.8k / P 12.5k，今日变化ΔOI: C +11.5k / P +2.3k，平值价格ATM: C $13.53 / P $12.20 ｜ ATM IV 66.9%，净 delta 敞口 133k shares
Top ΔOI: C 455 +6,026 ｜ C 400 +565
仓位参考: Max Pain 365 ｜ Call Wall 400（+7.0%，弱）（OI 1.6k） ｜ Put Wall 360（-3.7%，弱）（OI 1.0k）
量化解读： 存量 Call 重｜ATM IV 66.9%｜历史 Rank 94%（近端代理）｜IV/RV 2.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 133,122 股

📆 10-28 Forward Structure
存量OI: C 6.2k / P 6.3k，今日变化ΔOI: C +1.3k / P +1.5k，平值价格ATM: C $14.55 / P $13.05 ｜ ATM IV 62.6%，净 delta 敞口 2k shares
Top ΔOI: C 400 +252 ｜ P 367 +194
仓位参考: Max Pain 365 ｜ Call Wall 400（+7.0%，弱）（OI 0.8k） ｜ Put Wall 350（-6.3%）（OI 1.4k）
量化解读： 存量两侧均衡｜ATM IV 62.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.97×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 2,183 股

📆 10-30 Forward Structure
存量OI: C 73.8k / P 64.9k，今日变化ΔOI: C +5.0k / P +8.3k，平值价格ATM: C $15.45 / P $13.80 ｜ ATM IV 59.2%，净 delta 敞口 36k shares
仓位参考: Max Pain 370 ｜ Call Wall 400（+7.0%）（OI 9.5k） ｜ Put Wall 380（+1.7%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 59.2%｜历史 Rank 94%（近端代理）｜IV/RV 1.87×（近似）｜净 delta 敞口 正 36,207 股

📅 事件差分（观察，非因果）: 10-23（3D）ATM IV 89.2% vs 10-26 66.9%（差 +22.3pp）——覆盖 建筑许可 Prel、新屋开工
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/TSLA_evening.json