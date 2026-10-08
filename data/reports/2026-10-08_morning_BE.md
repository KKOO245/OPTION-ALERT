# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $774.21 ｜ QQQ $747.58
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.1（fear）
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
🟡 **事件差分**: 10-09 ATM IV 76.1% vs 10-16 66.0%（差 +10.2pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-09 275P ΔOI +689（距现价 -1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 291.29 → 今开 283.83（-2.6%） | 较昨收变动（含盘初走势） ｜ 今日高 286.95 ｜ 低 275.83

Options: P/C成交量 0.85 | OI比 1.17 | ATM IV 76.1% | Skew -1.8pp | Term 1.06 | ExpMove ±3.6%（近端） | Rank 33%
量化视角： IV 中性（Rank 33%）｜期限结构正常（Term 1.06）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.85×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.6% ｜ 10-16（8D）±7.7% ｜ 10-23（15D）±11.0% ｜ 10-30（22D）±15.4%
   ⇒ IV–VIX Spread: +60.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -4,126,609 | GEX Change vs 上次快照 -13,802,515 | Flip: Primary Flip: 282.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 551 / LOW 102 / INVALID 217
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 282.00（全链重定价，覆盖 99%）
Call Wall 300（弱结构｜现价低于该位 7.4%）
最近结构参考: Flip 282（现价低于该位 1.5%）
量化视角： 负 Gamma（413万，无历史分位）｜由正转负（1380万）｜现价位于 Flip 下方 1.47%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 282（MaxPain，仅结算参考） / 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 282（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 275.0P — Vol 1,525 | 最新价 $1.15 | OI 1429→2118 (ΔOI +689张) | ΔOI/Volume 45.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增689张（+48.2% vs前日OI），连续性待观察（方向未知）
10-16 270.0P — Vol 1,075 | 最新价 $3.78 | OI 2074→2640 (ΔOI +566张) | ΔOI/Volume 52.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增566张（+27.3% vs前日OI），连续性待观察（方向未知）
10-09 270.0P — Vol 1,610 | 最新价 $0.64 | OI 1812→2198 (ΔOI +386张) | ΔOI/Volume 24.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增386张（+21.3% vs前日OI），连续性待观察（方向未知）
10-09 290.0C — Vol 2,028 | 最新价 $7.10 | OI 1630→1994 (ΔOI +364张) | ΔOI/Volume 17.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增364张（+22.3% vs前日OI），连续性待观察（方向未知）
10-16 265.0P — Vol 690 | 最新价 $2.75 | OI 721→1080 (ΔOI +359张) | ΔOI/Volume 52.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增359张（+49.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,364 张（Put 2,000 / Call 364），跨 2 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.8k / P +2.4k ｜ Activity HIGH ｜ 1D
10-16  C +0.9k / P +2.0k ｜ Activity HIGH ｜ 8D
10-23  C +0.6k / P +1.1k ｜ Activity HIGH ｜ 15D
10-30  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 36.3k / P 42.4k，今日变化ΔOI: C +0.8k / P +2.4k，平值价格ATM: C $5.15 / P $4.75 ｜ ATM IV 76.1%，净 delta 敞口 -62k shares
Top ΔOI: P 275 +689 ｜ P 270 +386 ｜ C 290 +364
仓位参考: Max Pain 282 ｜ Call Wall 300（+8.0%，弱）（OI 3.1k） ｜ Put Wall 280（+0.8%，弱）（OI 2.4k）
量化解读： 存量两侧均衡｜ATM IV 76.1%｜历史 Rank 33%（近端代理）｜IV/RV 1.06×（近似）｜净 delta 敞口 负 62,062 股

📆 10-16 Forward Structure
存量OI: C 81.3k / P 93.2k，今日变化ΔOI: C +0.9k / P +2.0k，平值价格ATM: C $10.75 / P $10.76 ｜ ATM IV 66.0%，净 delta 敞口 -85k shares
Top ΔOI: C 270 -579 ｜ P 270 +566 ｜ C 280 -498
仓位参考: Max Pain 270 ｜ Call Wall 270（-2.8%，弱）（OI 7.0k） ｜ Put Wall 260（-6.4%，弱）（OI 4.3k）
量化解读： 存量两侧均衡｜ATM IV 66.0%｜历史 Rank 33%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 84,849 股

📆 10-23 Forward Structure
存量OI: C 14.5k / P 16.7k，今日变化ΔOI: C +0.6k / P +1.1k，平值价格ATM: C $16.00 / P $14.53 ｜ ATM IV 65.9%，净 delta 敞口 -18k shares
Top ΔOI: C 315 +167
仓位参考: Max Pain 270 ｜ Call Wall 300（+8.0%，弱）（OI 1.1k） ｜ Put Wall 280（+0.8%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 65.9%｜历史 Rank 33%（近端代理）｜IV/RV 0.92×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 18,067 股

10-30（MEDIUM △）Top ΔOI: 250P +100 ｜ 260P +65
10-30（MEDIUM △）仓位参考: Max Pain 285 ｜ Call Wall 300（+8.0%，弱）（OI 1.4k） ｜ Put Wall 285（+2.6%，弱）（OI 1.8k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 76.1% vs 10-16 66.0%（差 +10.2pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/BE_morning.json