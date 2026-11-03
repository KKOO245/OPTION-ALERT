# 期权晨报 2026-11-03（快照 10:20 ET）

📊 市场环境

SPY $753.95 ｜ QQQ $685.65
VIX 21.03 ↓0.6%（5D +20.0%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-03

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.1 ｜ 实际 7.523 ｜ 前值 7.19　✅ 今日已公布
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（3D）ATM IV 101.7% vs 11-13 85.5%（差 +16.1pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 130.76 → 今开 131.18（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 135.40 ｜ 低 131.09

Options: P/C成交量 0.91 | OI比 0.62 | ATM IV 101.7% | Skew 3.8pp | Term 0.74 | ExpMove ±7.5%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.74，近月 IV 高于远月）｜保护溢价中性（Skew 3.8pp）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.91×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（3D）±7.5% ｜ 11-13（10D）±11.3% ｜ 11-20（17D）±14.2% ｜ 11-27（24D）±15.6%
   ⇒ IV–VIX Spread: +80.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 60,320,230 | GEX Change vs 上次快照 14,650,307 | Flip: Primary Flip: 120.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 519 / LOW 94 / INVALID 227
结构观察区: Primary Flip 120.42（全链重定价，覆盖 100%）
Call Wall 135（现价低于该位 0.1%）
最近结构参考: Call Wall 135（现价低于该位 0.1%）
量化视角： 正 Gamma（6032万，无历史分位）｜正 Gamma 增强（+1465万）｜现价位于 Flip 上方 11.95%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 135（MaxPain，仅结算参考） / 135（Call Wall）。
• Gamma 区域：切换参考 120（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
12-04 200.0C — Vol 5,123 | 最新价 $0.56 | OI 240→5252 (ΔOI +5012张) | ΔOI/Volume 97.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5012张（+2088.3% vs前日OI），连续性待观察（方向未知）
11-06 170.0C — Vol 1,845 | 最新价 $0.06 | OI 2859→4269 (ΔOI +1410张) | ΔOI/Volume 76.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1410张（+49.3% vs前日OI），连续性待观察（方向未知）
11-13 115.0P — Vol 1,657 | 最新价 $2.40 | OI 783→2135 (ΔOI +1352张) | ΔOI/Volume 81.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1352张（+172.7% vs前日OI），连续性待观察（方向未知）
11-13 125.0P — Vol 2,035 | 最新价 $5.38 | OI 941→2256 (ΔOI +1315张) | ΔOI/Volume 64.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1315张（+139.7% vs前日OI），连续性待观察（方向未知）
11-06 135.0C — Vol 5,641 | 最新价 $3.50 | OI 22086→23197 (ΔOI +1111张) | ΔOI/Volume 19.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1111张（+5.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,200 张（Put 2,667 / Call 7,533），跨 3 个期限｜有实质成本保护 2 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +9.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 3D
11-13  C +2.6k / P +6.9k ｜ Activity MEDIUM △ ｜ 10D
11-20  C +1.6k / P +3.1k ｜ Activity HIGH ｜ 17D
11-27  C +1.1k / P +3.0k ｜ Activity MEDIUM △ ｜ 24D

📆 11-06 Forward Structure
存量OI: C 228.8k / P 141.1k，今日变化ΔOI: C +9.2k / P +0.1k，平值价格ATM: C $4.91 / P $5.21 ｜ ATM IV 101.7%，净 delta 敞口 340k shares
Top ΔOI: P 115 -1,493
仓位参考: Max Pain 135 ｜ Call Wall 136（+0.9%，弱）（OI 24.3k） ｜ Put Wall 125（-7.3%，弱）（OI 6.5k）
量化解读： 存量 Call 重｜ATM IV 101.7%｜历史 Rank 82%（近端代理）｜IV/RV 1.50×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 339,804 股

11-13（MEDIUM △）Top ΔOI: 115P +1,352 ｜ 125P +1,315
11-13（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 144（+6.8%，弱）（OI 0.8k） ｜ Put Wall 125（-7.3%，弱）（OI 2.3k）

📆 11-20 Forward Structure
存量OI: C 152.1k / P 123.6k，今日变化ΔOI: C +1.6k / P +3.1k，平值价格ATM: C $9.60 / P $9.53 ｜ ATM IV 81.2%，净 delta 敞口 23k shares
仓位参考: Max Pain 135 ｜ Call Wall 135（+0.1%）（OI 42.8k） ｜ Put Wall 130（-3.6%，弱）（OI 5.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 81.2%｜历史 Rank 82%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 23,142 股

11-27（MEDIUM △）Top ΔOI: 125P +866 ｜ 105P +502
11-27（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 145（+7.6%，弱）（OI 0.9k） ｜ Put Wall 140（+3.8%，弱）（OI 2.4k）

📅 事件差分（观察，非因果）: 11-06（3D）ATM IV 101.7% vs 11-13 85.5%（差 +16.1pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 非制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-03/MSTR_morning.json