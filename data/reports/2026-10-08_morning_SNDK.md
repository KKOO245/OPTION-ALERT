# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $775.90 ｜ QQQ $755.90
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-23 1600P ΔOI +112（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,692.42 → 今开 1,669.49（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 1675.00 ｜ 低 1633.00

Options: P/C成交量 0.67 | OI比 0.90 | ATM IV 63.5% | Skew -3.1pp | Term 1.01 | ExpMove ±3.0%（近端） | Rank 20%
量化视角： IV 历史低位（Rank 20%，期权偏便宜）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -3.1pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.90×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.0% ｜ 10-16（8D）±6.9% ｜ 10-23（15D）±9.4% ｜ 10-30（22D）±13.0%
   ⇒ IV–VIX Spread: +48.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -9,394,523 | GEX Change vs 上次快照 -9,899,571 | Flip: Primary Flip: 1679.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1605 / LOW 460 / INVALID 1105
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 1679.03（全链重定价，覆盖 99%）
最近结构参考: Flip 1679（现价低于该位 2.4%）
量化视角： 负 Gamma（939万，无历史分位）｜由正转负（990万）｜现价位于 Flip 下方 2.41%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 1,690（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1679（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 1895.0C — Vol 1,424 | 最新价 $1.23 | OI 849→2174 (ΔOI +1325张) | ΔOI/Volume 93.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1325张（+156.1% vs前日OI），连续性待观察（方向未知）
10-16 2000.0C — Vol 3,346 | 最新价 $4.77 | OI 2568→3644 (ΔOI +1076张) | ΔOI/Volume 32.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1076张（+41.9% vs前日OI），连续性待观察（方向未知）
10-09 1800.0C — Vol 9,650 | 最新价 $4.45 | OI 2451→3336 (ΔOI +885张) | ΔOI/Volume 9.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增885张（+36.1% vs前日OI），连续性待观察（方向未知）
10-16 2180.0C — Vol 632 | 最新价 $1.67 | OI 118→717 (ΔOI +599张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增599张（+507.6% vs前日OI），连续性待观察（方向未知）
10-09 1750.0C — Vol 6,656 | 最新价 $11.43 | OI 1164→1755 (ΔOI +591张) | ΔOI/Volume 8.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增591张（+50.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,476 张（Put 0 / Call 4,476），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +7.4k / P +1.5k ｜ Activity HIGH ｜ 1D
10-16  C +4.1k / P +1.3k ｜ Activity HIGH ｜ 8D
10-23  C +0.8k / P +0.7k ｜ Activity MEDIUM △ ｜ 15D
10-30  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 46.0k / P 41.5k，今日变化ΔOI: C +7.4k / P +1.5k，平值价格ATM: C $24.40 / P $24.60 ｜ ATM IV 63.5%，净 delta 敞口 -8k shares
Top ΔOI: C 1800 +885 ｜ C 1750 +591
仓位参考: Max Pain 1,690 ｜ Call Wall 1800（+9.9%，弱）（OI 3.3k） ｜ Put Wall 1600（-2.4%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜ATM IV 63.5%｜历史 Rank 20%（近端代理）｜IV/RV 1.07×（近似）｜净 delta 敞口 负 7,800 股

📆 10-16 Forward Structure
存量OI: C 49.8k / P 55.9k，今日变化ΔOI: C +4.1k / P +1.3k，平值价格ATM: C $56.20 / P $56.32 ｜ ATM IV 56.5%，净 delta 敞口 -9k shares
Top ΔOI: C 2000 +1,076 ｜ C 2180 +599
仓位参考: Max Pain 1,680 ｜ Call Wall 1800（+9.9%，弱）（OI 1.8k） ｜ Put Wall 1500（-8.5%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 56.5%｜历史 Rank 20%（近端代理）｜IV/RV 0.96×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 9,366 股

10-23（MEDIUM △）Top ΔOI: 1600P +112
10-23（MEDIUM △）仓位参考: Max Pain 1,700 ｜ Call Wall 1800（+9.9%，弱）（OI 0.5k） ｜ Put Wall 1500（-8.5%）（OI 0.7k）

10-30（MEDIUM △）Top ΔOI: 1715P +91 ｜ 1780C +71
10-30（MEDIUM △）仓位参考: Max Pain 1,700 ｜ Call Wall 1700（+3.8%，弱）（OI 0.4k） ｜ Put Wall 1500（-8.5%，弱）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 63.5% vs 10-16 56.5%（差 +7.0pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/SNDK_morning.json