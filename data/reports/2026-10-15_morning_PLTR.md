# 期权晨报 2026-10-15（快照 10:20 ET）

📊 市场环境

SPY $771.47 ｜ QQQ $728.00
VIX 17.51 ↑3.8%（5D +13.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.5（fear）
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
🟡 **事件差分**: 10-16 ATM IV 62.1% vs 10-23 47.5%（差 +14.6pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-23 197P ΔOI +1,054（距现价 +1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 200.97 → 今开 196.58（-2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 198.98 ｜ 低 192.71

Options: P/C成交量 0.91 | OI比 1.15 | ATM IV 62.1% | Skew 4.2pp | Term 1.00 | ExpMove ±2.9%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构正常（Term 1.00）｜保护溢价中性（Skew 4.2pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.91×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（1D）±2.9% ｜ 10-23（8D）±5.8% ｜ 10-30（15D）±7.6% ｜ 11-06（22D）±13.1%
   ⇒ IV–VIX Spread: +44.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,665,573 | GEX Change vs 上次快照 -29,547,665 | Flip: Primary Flip: 193.26（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 648 / LOW 58 / INVALID 206
结构观察区: Primary Flip 193.26（全链重定价，覆盖 100%）
最近结构参考: Flip 193（现价高于该位 1.0%）
量化视角： 正 Gamma（867万，无历史分位）｜正 Gamma 减弱（2955万）｜现价位于 Flip 上方 0.96%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 193（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 215.0C — Vol 14,870 | 最新价 $0.17 | OI 13606→16427 (ΔOI +2821张) | ΔOI/Volume 19.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2821张（+20.7% vs前日OI），连续性待观察（方向未知）
10-23 205.0P — Vol 5,189 | 最新价 $8.06 | OI 1344→3442 (ΔOI +2098张) | ΔOI/Volume 40.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2098张（+156.1% vs前日OI），连续性待观察（方向未知）
11-13 155.0P — Vol 1,446 | 最新价 $1.53 | OI 149→1547 (ΔOI +1398张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1398张（+938.3% vs前日OI），连续性待观察（方向未知）
10-30 200.0P — Vol 4,675 | 最新价 $6.92 | OI 1401→2686 (ΔOI +1285张) | ΔOI/Volume 27.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1285张（+91.7% vs前日OI），连续性待观察（方向未知）
10-30 187.5P — Vol 1,372 | 最新价 $2.86 | OI 924→2037 (ΔOI +1113张) | ΔOI/Volume 81.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1113张（+120.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 8,715 张（Put 5,894 / Call 2,821），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C -1.7k / P -6.9k ｜ Activity MEDIUM △ ｜ 1D
10-23  C +4.2k / P +4.3k ｜ Activity HIGH ｜ 8D
10-30  C +1.7k / P +1.3k ｜ Activity HIGH ｜ 15D
11-06  C +1.0k / P +1.1k ｜ Activity HIGH ｜ 22D

📆 10-16 Forward Structure
存量OI: C 230.4k / P 263.8k，今日变化ΔOI: C -1.7k / P -6.9k，平值价格ATM: C $3.33 / P $2.41 ｜ ATM IV 62.1%，净 delta 敞口 236k shares
Top ΔOI: P 205 -2,793
仓位参考: Max Pain 185 ｜ Call Wall 207.5（+6.3%，弱）（OI 14.8k） ｜ Put Wall 190（-2.6%，弱）（OI 10.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 62.1%｜历史 Rank 96%（近端代理）｜IV/RV 2.12×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 235,515 股

📆 10-23 Forward Structure
存量OI: C 46.9k / P 62.2k，今日变化ΔOI: C +4.2k / P +4.3k，平值价格ATM: C $6.03 / P $5.20 ｜ ATM IV 47.5%，净 delta 敞口 -175k shares
Top ΔOI: P 205 +2,098 ｜ P 197 +1,054
仓位参考: Max Pain 195 ｜ Call Wall 180（-7.7%，弱）（OI 4.6k） ｜ Put Wall 205（+5.1%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 47.5%｜历史 Rank 96%（近端代理）｜IV/RV 1.62×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 174,870 股

📆 10-30 Forward Structure
存量OI: C 39.6k / P 37.7k，今日变化ΔOI: C +1.7k / P +1.3k，平值价格ATM: C $8.00 / P $6.90 ｜ ATM IV 46.7%，净 delta 敞口 53k shares
Top ΔOI: P 202 -1,930 ｜ P 200 +1,285 ｜ P 187 +1,113
仓位参考: Max Pain 192 ｜ Call Wall 205（+5.1%，弱）（OI 3.4k） ｜ Put Wall 190（-2.6%）（OI 4.4k）
量化解读： 存量两侧均衡｜ATM IV 46.7%｜历史 Rank 96%（近端代理）｜IV/RV 1.59×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 53,324 股

📆 11-06 Forward Structure
存量OI: C 18.0k / P 17.3k，今日变化ΔOI: C +1.0k / P +1.1k，平值价格ATM: C $13.25 / P $12.25 ｜ ATM IV 65.9%，净 delta 敞口 25k shares
Top ΔOI: C 205 +535 ｜ P 172 +310 ｜ P 185 +263
仓位参考: Max Pain 192 ｜ Call Wall 205（+5.1%，弱）（OI 1.3k） ｜ Put Wall 190（-2.6%）（OI 3.0k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 65.9%｜历史 Rank 96%（近端代理）｜IV/RV 2.24×（近似）｜净 delta 敞口 正 24,522 股

📅 事件差分（观察，非因果）: 10-16（1D）ATM IV 62.1% vs 10-23 47.5%（差 +14.6pp）——覆盖 PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-15/PLTR_morning.json