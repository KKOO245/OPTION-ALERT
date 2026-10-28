# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $770.35 ｜ QQQ $725.61
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 35.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 4 ｜ 前值 4　✅ 今日已公布
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　✅ 今日已公布
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 10-30 ATM IV 56.3% vs 11-06 45.2%（差 +11.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 10-30 500C ΔOI -1,893（距现价 -3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SOXX  昨收 511.06 → 今开 515.71（+0.9%） | 较昨收变动（含盘初走势） ｜ 今日高 517.87 ｜ 低 511.66

Options: P/C成交量 3.08 | OI比 6.20 | ATM IV 56.3% | Skew 12.3pp | Term 0.72 | ExpMove ±3.7%（近端） | Rank 91%
量化视角： IV 历史高位（Rank 91%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜保护溢价显著（Skew 12.3pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 3.08）——观察点，非方向信号
   ⇒ Put/Call Volume: 3.08×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 6.20×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±3.7% ｜ 11-06（9D）±5.5% ｜ 11-13（16D）±8.7% ｜ 11-20（23D）±8.7%
   ⇒ IV–VIX Spread: +38.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,520,488 | GEX Change vs 上次快照 7,774,408 | Flip: Primary Flip: 513.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 589 / LOW 261 / INVALID 742
结构观察区: Primary Flip 513.28（全链重定价，覆盖 98%）
最近结构参考: Flip 513（现价高于该位 0.4%）
量化视角： 正 Gamma（252万，无历史分位）｜由负转正（+777万）｜现价位于 Flip 上方 0.41%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 515（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 513（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 550.0C — Vol 8,603 | 最新价 $2.78 | OI 564→8970 (ΔOI +8406张) | ΔOI/Volume 97.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8406张（+1490.4% vs前日OI），连续性待观察（方向未知）
11-06 540.0C — Vol 6,604 | 最新价 $4.55 | OI 76→6619 (ΔOI +6543张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6543张（+8609.2% vs前日OI），连续性待观察（方向未知）
11-20 580.0C — Vol 2,538 | 最新价 $3.07 | OI 3057→5139 (ΔOI +2082张) | ΔOI/Volume 82.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2082张（+68.1% vs前日OI），连续性待观察（方向未知）
11-20 540.0C — Vol 2,085 | 最新价 $11.35 | OI 1070→3047 (ΔOI +1977张) | ΔOI/Volume 94.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1977张（+184.8% vs前日OI），连续性待观察（方向未知）
11-20 555.0C — Vol 1,311 | 最新价 $7.06 | OI 91→1368 (ΔOI +1277张) | ΔOI/Volume 97.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1277张（+1403.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 20,285 张（Put 0 / Call 20,285），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C -1.0k / P +0.5k ｜ Activity HIGH ｜ 2D
11-06  C +15.2k / P +0.9k ｜ Activity HIGH ｜ 9D
11-13  C +1.1k / P +0.6k ｜ Activity MEDIUM △ ｜ 16D
11-20  C +4.6k / P +0.1k ｜ Activity MEDIUM △ ｜ 23D

📆 10-30 Forward Structure
存量OI: C 28.2k / P 174.7k，今日变化ΔOI: C -1.0k / P +0.5k，平值价格ATM: C $10.00 / P $9.10 ｜ ATM IV 56.3%，净 delta 敞口 -106k shares
Top ΔOI: C 500 -1,893 ｜ P 470 +1,160 ｜ C 525 -721
仓位参考: Max Pain 515 ｜ Call Wall 500（-3.0%，弱）（OI 2.8k）
量化解读： 存量 Put 重｜ATM IV 56.3%｜历史 Rank 91%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 105,820 股

📆 11-06 Forward Structure
存量OI: C 22.9k / P 8.5k，今日变化ΔOI: C +15.2k / P +0.9k，平值价格ATM: C $14.80 / P $13.68 ｜ ATM IV 45.2%，净 delta 敞口 327k shares
Top ΔOI: C 550 +8,406 ｜ C 540 +6,543 ｜ P 500 +407
仓位参考: Max Pain 505 ｜ Call Wall 540（+4.8%，弱）（OI 6.6k） ｜ Put Wall 495（-4.0%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 45.2%｜历史 Rank 91%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 327,077 股

11-13（MEDIUM △）Top ΔOI: 530C +327 ｜ 500C +313
11-13（MEDIUM △）仓位参考: Max Pain 510 ｜ Call Wall 510（-1.0%，弱）（OI 9.6k）

11-20（MEDIUM △）Top ΔOI: 580C +2,082 ｜ 540C +1,977
11-20（MEDIUM △）仓位参考: Max Pain 535 ｜ Call Wall 540（+4.8%，弱）（OI 3.0k） ｜ Put Wall 490（-4.9%，弱）（OI 3.6k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 56.3% vs 11-06 45.2%（差 +11.0pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/SOXX_morning.json