# 期权晨报 2026-10-01（快照 10:20 ET）

📊 市场环境

SPY $764.48 ｜ QQQ $742.03
VIX 17.57 ↑7.5%（5D +12.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 28.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-01

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 54.5 ｜ 前值 54.6　✅ 今日已公布
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 406.63 → 今开 409.05（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 410.52 ｜ 低 405.13

Options: P/C成交量 0.02 | OI比 1.60 | ATM IV 42.3% | Skew -0.6pp | Term 1.03 | ExpMove ±2.0%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构正常（Term 1.03）｜Put 保护异常便宜（Skew -0.6pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.02×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.60×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-02（1D）±2.0% ｜ 10-09（8D）±3.6% ｜ 10-16（15D）±5.5% ｜ 10-23（22D）±10.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,564,355 | GEX Change vs 上次快照 -213,962 | Flip: Primary Flip: 393.37（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 301 / LOW 165 / INVALID 396
结构观察区: Primary Flip 393.37（全链重定价，覆盖 96%）
Call Wall 420（弱结构｜现价低于该位 3.2%）
最近结构参考: Call Wall 420（现价低于该位 3.2%）
量化视角： 正 Gamma（256万，无历史分位）｜正 Gamma 减弱（21万）｜现价位于 Flip 上方 3.33%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 395（MaxPain，仅结算参考）；上方 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 393（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 360.0P — Vol 69 | 最新价 $0.45 | OI 1349→1402 (ΔOI +53张) | ΔOI/Volume 76.8% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增53张（+3.9% vs前日OI），值得跟踪（方向未知）
10-16 420.0C — Vol 44 | 最新价 $6.78 | OI 692→726 (ΔOI +34张) | ΔOI/Volume 77.3% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增34张（+4.9% vs前日OI），值得跟踪（方向未知）
10-02 425.0C — Vol 92 | 最新价 $0.30 | OI 178→200 (ΔOI +22张) | ΔOI/Volume 23.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增22张（+12.4% vs前日OI），值得跟踪（方向未知）
10-16 410.0P — Vol 21 | 最新价 $10.95 | OI 250→271 (ΔOI +21张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增21张（+8.4% vs前日OI），值得跟踪（方向未知）
10-09 417.5P — Vol 20 | 最新价 $13.40 | OI 1→21 (ΔOI +20张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增20张（+2000.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 150 张（Put 94 / Call 56），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +5 / P +70 ｜ Activity LOW ｜ 1D
10-09  C +31 / P +67 ｜ Activity MEDIUM △ ｜ 8D
10-16  C +20 / P +0.1k ｜ Activity MEDIUM △ ｜ 15D
10-23  C +18 / P +12 ｜ Activity LOW ｜ 22D

📆 10-02 Forward Structure
存量OI: C 2.2k / P 3.5k，今日变化ΔOI: C +5 / P +70，平值价格ATM: C $4.50 / P $3.74 ｜ ATM IV 42.3%，净 delta 敞口 -3k shares
Top ΔOI: C 425 +22 ｜ P 410 +13 ｜ P 397 +11
仓位参考: Max Pain 395 ｜ Call Wall 410（+0.9%，弱）（OI 0.3k）
量化解读： 存量 Put 重｜ATM IV 42.3%｜历史 Rank 63%（近端代理）｜IV/RV 1.56×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 3,231 股

10-09（MEDIUM △）Top ΔOI: 417P +20 ｜ 400P +11
10-09（MEDIUM △）仓位参考: Max Pain 380 ｜ Call Wall 420（+3.3%，弱）（OI 0.1k） ｜ Put Wall 417.5（+2.7%，弱）（OI 21）

10-16（MEDIUM △）Top ΔOI: 420C +34 ｜ 410P +21
10-16（MEDIUM △）仓位参考: Max Pain 390 ｜ Call Wall 400（-1.6%，弱）（OI 0.9k） ｜ Put Wall 380（-6.5%，弱）（OI 0.6k）

10-23（Activity LOW）仓位参考: Max Pain 415 ｜ Call Wall 425（+4.6%）（OI 0.5k） ｜ Put Wall 415（+2.1%）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-02（1D）ATM IV 42.3% vs 10-09 35.5%（差 +6.8pp）——覆盖 ISM 制造业 PMI、Non Farm Payrolls、失业率
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-01/ISRG_morning.json