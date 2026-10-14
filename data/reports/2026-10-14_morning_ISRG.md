# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $773.15 ｜ QQQ $736.43
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.8（fear）
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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 422.06 → 今开 424.81（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 425.39 ｜ 低 417.26

Options: P/C成交量 3.62 | OI比 0.92 | ATM IV 46.4% | Skew -10.7pp | Term 1.00 | ExpMove ±2.9%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -10.7pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 3.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.62×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.92×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±2.9% ｜ 10-23（9D）±8.2% ｜ 10-30（16D）±4.5% ｜ 11-06（23D）±9.7%
   ⇒ IV–VIX Spread: +30.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,667,317 | GEX Change vs 上次快照 -395,543 | Flip: Primary Flip: 402.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 381 / LOW 147 / INVALID 436
结构观察区: Primary Flip 402.93（全链重定价，覆盖 90%）
Call Wall 420（弱结构｜现价高于该位 0.3%）
最近结构参考: Call Wall 420（现价高于该位 0.3%）
量化视角： 正 Gamma（267万，无历史分位）｜正 Gamma 减弱（40万）｜现价位于 Flip 上方 4.58%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 403（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 485.0C — Vol 32 | 最新价 $4.00 | OI 7→38 (ΔOI +31张) | ΔOI/Volume 96.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31张（+442.9% vs前日OI），连续性待观察（方向未知）
10-30 470.0C — Vol 36 | 最新价 $5.05 | OI 14→45 (ΔOI +31张) | ΔOI/Volume 86.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31张（+221.4% vs前日OI），连续性待观察（方向未知）
10-16 405.0P — Vol 103 | 最新价 $1.05 | OI 180→205 (ΔOI +25张) | ΔOI/Volume 24.3% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增25张（+13.9% vs前日OI），值得跟踪（方向未知）
10-16 245.0C — Vol 39 | 最新价 $177.37 | OI 22→45 (ΔOI +23张) | ΔOI/Volume 59.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23张（+104.5% vs前日OI），连续性待观察（方向未知）
10-16 250.0C — Vol 108 | 最新价 $172.99 | OI 62→84 (ΔOI +22张) | ΔOI/Volume 20.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增22张（+35.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 132 张（Put 25 / Call 107），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +72 / P +87 ｜ Activity MEDIUM △ ｜ 2D
10-23  C +93 / P +0.1k ｜ Activity MEDIUM △ ｜ 9D
10-30  C +72 / P +24 ｜ Activity MEDIUM △ ｜ 16D
11-06  C +27 / P +22 ｜ Activity LOW ｜ 23D

📆 10-16 Forward Structure
存量OI: C 11.7k / P 10.8k，今日变化ΔOI: C +72 / P +87，平值价格ATM: C $6.60 / P $5.65 ｜ ATM IV 46.4%，净 delta 敞口 3k shares
Top ΔOI: C 400 -38 ｜ P 405 +25 ｜ C 245 +23
仓位参考: Max Pain 395 ｜ Call Wall 400（-5.1%，弱）（OI 0.8k） ｜ Put Wall 380（-9.8%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 46.4%｜历史 Rank 82%（近端代理）｜IV/RV 1.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 3,369 股

10-23（MEDIUM △）Top ΔOI: 460C +18 ｜ 380P +17
10-23（MEDIUM △）仓位参考: Max Pain 415 ｜ Call Wall 425（+0.9%，弱）（OI 0.5k） ｜ Put Wall 415（-1.5%）（OI 0.5k）

10-30（MEDIUM △）Top ΔOI: 390P +10
10-30（MEDIUM △）仓位参考: Max Pain 395 ｜ Call Wall 460（+9.2%，弱）（OI 95） ｜ Put Wall 380（-9.8%，弱）（OI 50）

11-06（Activity LOW）仓位参考: Max Pain 405 ｜ Call Wall 455（+8.0%，弱）（OI 50） ｜ Put Wall 390（-7.4%）（OI 52）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/ISRG_morning.json