# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $767.19 ｜ QQQ $720.47
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 24.6（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-15

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 1.3 ｜ 前值 0.5　✅ 今日已公布
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 0.8 ｜ 前值 1.3　✅ 今日已公布
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布　⏰ 今日

🔍 重点速览
🔵 **Flip 状态**: CONDITIONAL（Candidates: 411.4）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 420.24 → 今开 425.84（+1.3%） | 较昨收变动（含盘初走势） ｜ 今日高 427.07 ｜ 低 419.54

Options: P/C成交量 1.31 | OI比 0.90 | ATM IV 46.4% | Skew -0.8pp | Term 0.97 | ExpMove ±2.4%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 1.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.31×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.4% ｜ 10-23（8D）±8.2% ｜ 10-30（15D）±4.5% ｜ 11-06（22D）±9.7%
   ⇒ IV–VIX Spread: +28.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,790,928 | GEX Change vs 上次快照 -285,252 | Flip: Candidates 411.38 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 79%（带内） ｜ IV 有效性: VALID 336 / LOW 157 / INVALID 475
结构观察区: ≈411（全链重定价，覆盖 79%，CONDITIONAL）
Call Wall 420（弱结构｜现价高于该位 0.6%）
最近结构参考: Call Wall 420（现价高于该位 0.6%）
量化视角： 正 Gamma（279万，无历史分位）｜正 Gamma 减弱（29万）｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 390（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 411（全链重定价，覆盖 79%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 190.0C — Vol 187 | 最新价 $226.98 | OI 29→84 (ΔOI +55张) | ΔOI/Volume 29.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增55张（+189.7% vs前日OI），连续性待观察（方向未知）
10-16 195.0C — Vol 213 | 最新价 $222.01 | OI 29→81 (ΔOI +52张) | ΔOI/Volume 24.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增52张（+179.3% vs前日OI），连续性待观察（方向未知）
10-16 425.0C — Vol 122 | 最新价 $2.17 | OI 312→354 (ΔOI +42张) | ΔOI/Volume 34.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增42张（+13.5% vs前日OI），值得跟踪（方向未知）
10-16 400.0P — Vol 69 | 最新价 $0.50 | OI 550→588 (ΔOI +38张) | ΔOI/Volume 55.1% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增38张（+6.9% vs前日OI），值得跟踪（方向未知）
10-23 315.0P — Vol 32 | 最新价 $0.23 | OI 20→51 (ΔOI +31张) | ΔOI/Volume 96.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31张（+155.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 218 张（Put 69 / Call 149），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +0.2k / P -4 ｜ Activity MEDIUM △ ｜ 1D
10-23  C +50 / P +98 ｜ Activity MEDIUM △ ｜ 8D
10-30  C +54 / P +20 ｜ Activity MEDIUM △ ｜ 15D
11-06  C +11 / P +3 ｜ Activity MEDIUM △ ｜ 22D

📆 10-16 Forward Structure
存量OI: C 12.0k / P 10.8k，今日变化ΔOI: C +0.2k / P -4，平值价格ATM: C $2.25 / P $7.70 ｜ ATM IV 46.4%，净 delta 敞口 22k shares
Top ΔOI: C 190 +55 ｜ C 195 +52 ｜ C 425 +42
仓位参考: Max Pain 390 ｜ Call Wall 400（-5.3%，弱）（OI 0.8k） ｜ Put Wall 400（-5.3%，弱）（OI 0.6k）
量化解读： 存量两侧均衡｜ATM IV 46.4%｜历史 Rank 82%（近端代理）｜IV/RV 1.94×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 21,712 股

10-23（MEDIUM △）Top ΔOI: 417P +30 ｜ 382P +21
10-23（MEDIUM △）仓位参考: Max Pain 415 ｜ Call Wall 425（+0.6%，弱）（OI 0.5k） ｜ Put Wall 415（-1.8%）（OI 0.5k）

10-30（MEDIUM △）仓位参考: Max Pain 395 ｜ Call Wall 460（+8.9%，弱）（OI 95） ｜ Put Wall 400（-5.3%，弱）（OI 43）

11-06（MEDIUM △）Top ΔOI: 430C -2
11-06（MEDIUM △）仓位参考: Max Pain 405 ｜ Call Wall 455（+7.7%，弱）（OI 51） ｜ Put Wall 390（-7.7%）（OI 52）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/ISRG_morning.json