# 期权晨报 2026-10-29（快照 10:20 ET）

📊 市场环境

SPY $769.36 ｜ QQQ $715.34
VIX 16.74 ↓1.0%（5D -12.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-29

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 3.4 ｜ 前值 2.2　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 0.5 ｜ 前值 0.9　✅ 今日已公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 195C ΔOI +892（距现价 -0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 196.81 → 今开 198.37（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 198.51 ｜ 低 190.36

Options: P/C成交量 0.58 | OI比 1.01 | ATM IV 62.4% | Skew 3.9pp | Term 1.04 | ExpMove ±3.0%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构正常（Term 1.04）｜保护溢价中性（Skew 3.9pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.58×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.01×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（1D）±3.0% ｜ 11-06（8D）±11.9% ｜ 11-13（15D）±13.2% ｜ 11-20（22D）±14.1%
   ⇒ IV–VIX Spread: +45.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 30,912,547 | GEX Change vs 上次快照 -4,317,451 | Flip: Primary Flip: 191.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 685 / LOW 65 / INVALID 188
结构观察区: Primary Flip 191.69（全链重定价，覆盖 100%）
Put Wall 180（弱结构｜现价高于该位 8.9%） | Call Wall 210（弱结构｜现价低于该位 6.7%）
最近结构参考: Flip 192（现价高于该位 2.2%）
量化视角： 正 Gamma（3091万，无历史分位）｜正 Gamma 减弱（432万）｜现价位于 Flip 上方 2.25%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall，弱结构） / 195（MaxPain，仅结算参考）；上方 210（Call Wall，弱结构）。
• Gamma 区域：切换参考 192（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 420.0C — Vol 4,552 | 最新价 $0.01 | OI 1982→6534 (ΔOI +4552张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4552张（+229.7% vs前日OI），连续性待观察（方向未知）
10-30 195.0C — Vol 10,224 | 最新价 $4.19 | OI 2908→3800 (ΔOI +892张) | ΔOI/Volume 8.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增892张（+30.7% vs前日OI），连续性待观察（方向未知）
10-30 197.5C — Vol 16,028 | 最新价 $2.77 | OI 2136→3023 (ΔOI +887张) | ΔOI/Volume 5.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增887张（+41.5% vs前日OI），连续性待观察（方向未知）
11-20 180.0P — Vol 611 | 最新价 $6.26 | OI 9278→10110 (ΔOI +832张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增832张（+9.0% vs前日OI），值得跟踪（方向未知）
10-30 187.5P — Vol 2,646 | 最新价 $0.56 | OI 3577→4298 (ΔOI +721张) | ΔOI/Volume 27.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增721张（+20.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,884 张（Put 1,553 / Call 6,331），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C -1.6k / P +0.9k ｜ Activity MEDIUM △ ｜ 1D
11-06  C +8.2k / P +3.9k ｜ Activity HIGH ｜ 8D
11-13  C +1.0k / P +0.8k ｜ Activity MEDIUM △ ｜ 15D
11-20  C -83 / P +0.2k ｜ Activity LOW ｜ 22D

📆 10-30 Forward Structure
存量OI: C 128.3k / P 130.1k，今日变化ΔOI: C -1.6k / P +0.9k，平值价格ATM: C $3.74 / P $2.19 ｜ ATM IV 62.4%，净 delta 敞口 47k shares
Top ΔOI: C 195 +892 ｜ C 197 +887 ｜ C 212 -854
仓位参考: Max Pain 195 ｜ Call Wall 210（+7.1%，弱）（OI 16.8k） ｜ Put Wall 180（-8.2%，弱）（OI 9.6k）
量化解读： 存量两侧均衡｜ATM IV 62.4%｜历史 Rank 93%（近端代理）｜IV/RV 1.38×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 47,372 股

📆 11-06 Forward Structure
存量OI: C 56.9k / P 56.8k，今日变化ΔOI: C +8.2k / P +3.9k，平值价格ATM: C $12.50 / P $10.82 ｜ ATM IV 98.8%，净 delta 敞口 24k shares
Top ΔOI: C 215 +539 ｜ P 195 +524
仓位参考: Max Pain 195 ｜ Call Wall 215（+9.7%，弱）（OI 3.8k） ｜ Put Wall 190（-3.1%，弱）（OI 3.7k）
量化解读： 存量两侧均衡｜ATM IV 98.8%｜历史 Rank 93%（近端代理）｜IV/RV 2.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 24,412 股

11-13（MEDIUM △）Top ΔOI: 205C +327 ｜ 197C +174
11-13（MEDIUM △）仓位参考: Max Pain 195 ｜ Call Wall 210（+7.1%，弱）（OI 1.4k） ｜ Put Wall 180（-8.2%，弱）（OI 1.6k）

11-20（Activity LOW）仓位参考: Max Pain 175 ｜ Call Wall 200（+2.0%，弱）（OI 13.0k） ｜ Put Wall 180（-8.2%，弱）（OI 10.1k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-29/PLTR_morning.json