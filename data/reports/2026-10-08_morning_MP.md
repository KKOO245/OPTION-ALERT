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


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 46.31 → 今开 45.37（-2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 46.75 ｜ 低 45.28

Options: P/C成交量 0.83 | OI比 0.79 | ATM IV 61.1% | Skew -1.6pp | Term 0.93 | ExpMove ±2.6%（近端） | Rank 39%
量化视角： IV 中性（Rank 39%）｜期限结构正常（Term 0.93）｜Put 保护异常便宜（Skew -1.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.79）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.79×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.6% ｜ 10-16（8D）±6.4% ｜ 10-23（15D）±9.2% ｜ 10-30（22D）±11.4%
   ⇒ IV–VIX Spread: +45.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -6,169,868 | GEX Change vs 上次快照 -276,640 | Flip: Primary Flip: 47.67（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 287 / LOW 65 / INVALID 100
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 47.67（全链重定价，覆盖 96%）
Put Wall 45（现价高于该位 2.3%） | Call Wall 50（弱结构｜现价低于该位 7.9%）
最近结构参考: Put Wall 45（现价高于该位 2.3%）
量化视角： 负 Gamma（617万，无历史分位）｜负 Gamma 加深（28万）｜现价位于 Flip 下方 3.41%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall）；上方 48（MaxPain，仅结算参考） / 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 48（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 48.0C — Vol 770 | 最新价 $0.24 | OI 430→885 (ΔOI +455张) | ΔOI/Volume 59.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增455张（+105.8% vs前日OI），连续性待观察（方向未知）
10-16 50.0C — Vol 784 | 最新价 $0.43 | OI 4157→4513 (ΔOI +356张) | ΔOI/Volume 45.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增356张（+8.6% vs前日OI），连续性待观察（方向未知）
10-30 55.0C — Vol 249 | 最新价 $0.42 | OI 474→671 (ΔOI +197张) | ΔOI/Volume 79.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增197张（+41.6% vs前日OI），连续性待观察（方向未知）
10-09 45.5P — Vol 251 | 最新价 $0.55 | OI 1197→1382 (ΔOI +185张) | ΔOI/Volume 73.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增185张（+15.5% vs前日OI），连续性待观察（方向未知）
10-09 47.0C — Vol 328 | 最新价 $0.52 | OI 226→411 (ΔOI +185张) | ΔOI/Volume 56.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增185张（+81.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,378 张（Put 185 / Call 1,193），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.3k / P +0.4k ｜ Activity MEDIUM △ ｜ 1D
10-16  C +0.6k / P +0.6k ｜ Activity MEDIUM △ ｜ 8D
10-23  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 15D
10-30  C +0.2k / P +0.3k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 12.0k / P 9.5k，今日变化ΔOI: C +0.3k / P +0.4k，平值价格ATM: C $0.69 / P $0.50 ｜ ATM IV 61.1%，净 delta 敞口 20k shares
Top ΔOI: C 48 +455 ｜ C 50 -256
仓位参考: Max Pain 48 ｜ Call Wall 50（+8.6%，弱）（OI 1.9k） ｜ Put Wall 47（+2.1%）（OI 2.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.1%｜历史 Rank 39%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 19,726 股

10-16（MEDIUM △）Top ΔOI: 50C +356
10-16（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+8.6%）（OI 4.5k） ｜ Put Wall 45（-2.3%，弱）（OI 4.4k）

10-23（MEDIUM △）Top ΔOI: 50C +58
10-23（MEDIUM △）仓位参考: Max Pain 50 ｜ Call Wall 50（+8.6%，弱）（OI 0.2k） ｜ Put Wall 45（-2.3%，弱）（OI 0.2k）

10-30（MEDIUM △）Top ΔOI: 48P +59
10-30（MEDIUM △）仓位参考: Max Pain 48 ｜ Call Wall 50（+8.6%，弱）（OI 0.3k） ｜ Put Wall 44（-4.4%）（OI 1.6k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 61.1% vs 10-16 52.7%（差 +8.4pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/MP_morning.json