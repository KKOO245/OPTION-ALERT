# 期权晚报 2026-11-18（快照 16:40 ET）

📊 市场环境

SPY $730.20 ｜ QQQ $659.51
VIX 24.56 ↓3.5%（5D +40.4%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-18

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 1.309 ｜ 前值 1.191　✅ 今日已公布
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 1.295 ｜ 前值 1.4　✅ 今日已公布

🔍 重点速览
🔴 **事件差分**: 11-20（2D）ATM IV 51.9% vs 11-27 32.9%（差 +19.0pp），覆盖 新屋开工、建筑许可 Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 12-11 485C ΔOI +71 占该期限总 OI 12.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 430.20 → 收盘 420.95（-2.2%） ｜ 今日高 437.33 ｜ 低 420.84 ｜ 昨收 430.53 → 收盘 420.95（-2.2%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-25，窗口结束前不做对错判定）

Options: P/C成交量 0.55 | OI比 1.02 | ATM IV 51.9% | Skew 2.1pp | Term 0.63 | ExpMove ±2.8%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价中性（Skew 2.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.55×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.02×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（2D）±2.8% ｜ 11-27（9D）±7.3% ｜ 12-04（16D）±7.9% ｜ 12-11（23D）±18.9%
   ⇒ IV–VIX Spread: +27.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 948,914 | GEX Change vs 上次快照 -1,057,302 | Flip: Primary Flip: 415.16（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 87%（带内） ｜ IV 有效性: VALID 277 / LOW 214 / INVALID 475
结构观察区: Primary Flip 415.16（全链重定价，覆盖 87%）
最近结构参考: Flip 415（现价高于该位 1.4%）
量化视角： 正 Gamma（95万，无历史分位）｜正 Gamma 减弱（106万）｜现价位于 Flip 上方 1.39%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 410（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 415（全链重定价，覆盖 87%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
- 无中高变动事件（全部低等级）
📆 Forward Expiration Structure

11-20  C -0.2k / P +66 ｜ Activity MEDIUM △ ｜ 2D
11-27  C +25 / P +14 ｜ Activity MEDIUM △ ｜ 9D
12-04  C +19 / P -15 ｜ Activity MEDIUM △ ｜ 16D
12-11  C +67 / P +22 ｜ Activity HIGH ｜ 23D

📆 11-20 Forward Structure
存量OI: C 10.5k / P 10.7k，今日变化ΔOI: C -0.2k / P +66，平值价格ATM: C $7.00 / P $4.70 ｜ ATM IV 51.9%，净 delta 敞口 -3k shares
Top ΔOI: C 440 -79 ｜ P 395 +29
仓位参考: Max Pain 410 ｜ Call Wall 420（-0.2%，弱）（OI 0.8k） ｜ Put Wall 380（-9.7%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 51.9%｜历史 Rank 85%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 2,600 股

11-27（MEDIUM △）Top ΔOI: 450C +10 ｜ 450P -8
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 430（+2.1%，弱）（OI 64） ｜ Put Wall 395（-6.2%，弱）（OI 0.2k）

12-04（MEDIUM △）Top ΔOI: 445P -11
12-04（MEDIUM △）仓位参考: Max Pain 450 ｜ Call Wall 460（+9.3%，弱）（OI 34） ｜ Put Wall 405（-3.8%，弱）（OI 24）

📆 12-11 Forward Structure
存量OI: C 0.4k / P 0.1k，今日变化ΔOI: C +67 / P +22，平值价格ATM: C $68.23 / P $11.52 ｜ ATM IV 33.7%，净 delta 敞口 -750 shares
Top ΔOI: P 435 +12 ｜ P 415 +4
仓位参考: Max Pain 440 ｜ Call Wall 450（+6.9%）（OI 0.1k） ｜ Put Wall 435（+3.3%）（OI 35）
量化解读： 存量 Call 重｜ATM IV 33.7%｜历史 Rank 85%（近端代理）｜IV/RV 0.79×（近似）｜净 delta 敞口 负 750 股

📅 事件差分（观察，非因果）: 11-20（2D）ATM IV 51.9% vs 11-27 32.9%（差 +19.0pp）——覆盖 新屋开工、建筑许可 Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-18/ISRG_evening.json