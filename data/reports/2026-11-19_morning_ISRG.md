# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $nan ｜ QQQ $nan
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 420.95 → 今开 420.95（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 425.08 ｜ 低 418.22

Options: P/C成交量 0.48 | OI比 0.98 | ATM IV 56.6% | Skew -4.8pp | Term 0.60 | ExpMove ±2.3%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜Put 保护异常便宜（Skew -4.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.98×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（1D）±2.3% ｜ 11-27（8D）±2.8% ｜ 12-04（15D）±7.9% ｜ 12-11（22D）±19.0%
   ⇒ IV–VIX Spread: +33.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 914,923 | GEX Change vs 上次快照 -244,891 | Flip: Primary Flip: 415.71（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 272 / LOW 200 / INVALID 510
结构观察区: Primary Flip 415.71（全链重定价，覆盖 88%）
最近结构参考: Flip 416（现价高于该位 1.0%）
量化视角： 正 Gamma（91万，无历史分位）｜正 Gamma 减弱（24万）｜现价位于 Flip 上方 1.04%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 405（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 416（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-18 435.0C — Vol 161 | 最新价 $12.79 | OI 41→199 (ΔOI +158张) | ΔOI/Volume 98.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增158张（+385.4% vs前日OI），连续性待观察（方向未知）
12-18 400.0P — Vol 96 | 最新价 $7.45 | OI 446→528 (ΔOI +82张) | ΔOI/Volume 85.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增82张（+18.4% vs前日OI），连续性待观察（方向未知）
11-27 432.5C — Vol 54 | 最新价 $8.40 | OI 11→57 (ΔOI +46张) | ΔOI/Volume 85.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增46张（+418.2% vs前日OI），连续性待观察（方向未知）
11-20 435.0C — Vol 176 | 最新价 $2.10 | OI 581→624 (ΔOI +43张) | ΔOI/Volume 24.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增43张（+7.4% vs前日OI），值得跟踪（方向未知）
12-18 425.0P — Vol 68 | 最新价 $16.40 | OI 73→111 (ΔOI +38张) | ΔOI/Volume 55.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增38张（+52.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 367 张（Put 120 / Call 247），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +67 / P -0.4k ｜ Activity MEDIUM △ ｜ 1D
11-27  C +70 / P +31 ｜ Activity MEDIUM △ ｜ 8D
12-04  C +24 / P +18 ｜ Activity LOW ｜ 15D
12-11  C -1 / P +2 ｜ Activity LOW ｜ 22D

📆 11-20 Forward Structure
存量OI: C 10.6k / P 10.4k，今日变化ΔOI: C +67 / P -0.4k，平值价格ATM: C $5.00 / P $4.50 ｜ ATM IV 56.6%，净 delta 敞口 36k shares
Top ΔOI: P 470 -105 ｜ P 460 -89 ｜ P 475 -71
仓位参考: Max Pain 405 ｜ Call Wall 420（-0.0%，弱）（OI 0.8k） ｜ Put Wall 380（-9.5%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 56.6%｜历史 Rank 89%（近端代理）｜IV/RV 1.31×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 35,654 股

11-27（MEDIUM △）Top ΔOI: 432C +46 ｜ 450C +17
11-27（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 450（+7.1%，弱）（OI 69） ｜ Put Wall 395（-6.0%，弱）（OI 0.2k）

12-04（Activity LOW）仓位参考: Max Pain 450 ｜ Call Wall 460（+9.5%，弱）（OI 37） ｜ Put Wall 405（-3.6%，弱）（OI 24）

12-11（Activity LOW）仓位参考: Max Pain 440 ｜ Call Wall 450（+7.1%）（OI 0.1k） ｜ Put Wall 435（+3.6%）（OI 36）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/ISRG_morning.json