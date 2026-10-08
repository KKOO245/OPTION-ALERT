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

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 13.23 → 今开 13.02（-1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 13.29 ｜ 低 12.97

Options: P/C成交量 1.01 | OI比 0.30 | ATM IV 72.4% | Skew -6.3pp | Term 0.96 | ExpMove ±3.6%（近端） | Rank 6%
量化视角： IV 历史低位（Rank 6%，期权偏便宜）｜期限结构正常（Term 0.96）｜Put 保护异常便宜（Skew -6.3pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.6% ｜ 10-16（8D）±7.5% ｜ 10-23（15D）±11.8% ｜ 10-30（22D）±15.2%
   ⇒ IV–VIX Spread: +56.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,368,490 | GEX Change vs 上次快照 1,036,206 | Flip: Primary Flip: 13.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 190 / LOW 82 / INVALID 124
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 13.46（全链重定价，覆盖 98%）
最近结构参考: Flip 13（现价低于该位 3.1%）
量化视角： 负 Gamma（237万，无历史分位）｜负 Gamma 缓解（+104万）｜现价位于 Flip 下方 3.14%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 14（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 13（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 13.0P — Vol 580 | 最新价 $0.40 | OI 1172→1619 (ΔOI +447张) | ΔOI/Volume 77.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增447张（+38.1% vs前日OI），连续性待观察（方向未知）
10-30 14.0C — Vol 381 | 最新价 $0.60 | OI 350→683 (ΔOI +333张) | ΔOI/Volume 87.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增333张（+95.1% vs前日OI），连续性待观察（方向未知）
11-06 16.5P — Vol 297 | 最新价 $3.45 | OI 87→384 (ΔOI +297张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增297张（+341.4% vs前日OI），连续性待观察（方向未知）
10-09 14.0C — Vol 1,116 | 最新价 $0.06 | OI 1902→2183 (ΔOI +281张) | ΔOI/Volume 25.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增281张（+14.8% vs前日OI），连续性待观察（方向未知）
10-16 14.0P — Vol 385 | 最新价 $1.00 | OI 1960→2211 (ΔOI +251张) | ΔOI/Volume 65.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增251张（+12.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,609 张（Put 995 / Call 614），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.3k / P -1.7k ｜ Activity HIGH ｜ 1D
10-16  C +0.5k / P +0.4k ｜ Activity LOW ｜ 8D
10-23  C +0.6k / P -0.4k ｜ Activity MEDIUM △ ｜ 15D
10-30  C +35 / P +0.4k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 19.2k / P 5.8k，今日变化ΔOI: C +0.3k / P -1.7k，平值价格ATM: C $0.34 / P $0.13 ｜ ATM IV 72.4%，净 delta 敞口 189k shares
Top ΔOI: P 16 -1,010 ｜ P 15 -294
仓位参考: Max Pain 14 ｜ Call Wall 14（+7.4%，弱）（OI 2.2k） ｜ Put Wall 13（-0.3%，弱）（OI 1.5k）
量化解读： 存量 Call 重｜ATM IV 72.4%｜历史 Rank 6%（近端代理）｜IV/RV 1.41×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 189,319 股

10-16（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 14（+7.4%，弱）（OI 2.2k）

10-23（MEDIUM △）Top ΔOI: 16P -255 ｜ 17P -153
10-23（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 14（+7.4%，弱）（OI 0.6k）

10-30（MEDIUM △）Top ΔOI: 14C +333 ｜ 12P +239
10-30（MEDIUM △）仓位参考: Max Pain 16 ｜ Call Wall 14（+7.4%，弱）（OI 0.7k） ｜ Put Wall 14（+7.4%）（OI 2.6k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 72.4% vs 10-16 63.8%（差 +8.6pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/USAR_morning.json