# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $770.58 ｜ QQQ $721.80
VIX 17.36 ↓0.9%（5D +4.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 34.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-28

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布　⏰ 今日
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4　⏰ 今日
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布　⏰ 今日
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-30 47P ΔOI +1,536（距现价 -3.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 49.16 → 今开 48.83（-0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 48.86 ｜ 低 48.51

Options: P/C成交量 0.53 | OI比 0.74 | ATM IV 71.6% | Skew 0.7pp | Term 0.52 | ExpMove ±2.9%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.52，近月 IV 高于远月）｜保护溢价薄（Skew 0.7pp）｜存量 Call 偏重（OI比 0.74）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.74×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±2.9% ｜ 11-02（5D）±3.4% ｜ 11-04（7D）±4.3% ｜ 11-06（9D）±5.0%
   ⇒ IV–VIX Spread: +54.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 1,726,233 | GEX Change vs 上次快照 -6,697,118 | Flip: Primary Flip: 48.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 722 / LOW 117 / INVALID 353
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 48.57（全链重定价，覆盖 97%）
Put Wall 50（弱结构｜现价低于该位 2.7%）
最近结构参考: Flip 49（现价高于该位 0.1%）
量化视角： 正 Gamma（173万，无历史分位）｜正 Gamma 减弱（670万）｜现价位于 Flip 上方 0.13%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 50（Put Wall，弱结构） / 49（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 56.5C — Vol 5,804 | 最新价 $0.34 | OI 294→5587 (ΔOI +5293张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5293张（+1800.3% vs前日OI），连续性待观察（方向未知）
11-27 54.5C — Vol 6,097 | 最新价 $0.57 | OI 350→5628 (ΔOI +5278张) | ΔOI/Volume 86.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5278张（+1508.0% vs前日OI），连续性待观察（方向未知）
10-30 40.0P — Vol 3,361 | 最新价 $0.01 | OI 3380→5302 (ΔOI +1922张) | ΔOI/Volume 57.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1922张（+56.9% vs前日OI），连续性待观察（方向未知）
10-30 47.0P — Vol 1,691 | 最新价 $0.17 | OI 719→2255 (ΔOI +1536张) | ΔOI/Volume 90.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1536张（+213.6% vs前日OI），连续性待观察（方向未知）
10-28 49.5C — Vol 3,961 | 最新价 $0.34 | OI 1923→3454 (ΔOI +1531张) | ΔOI/Volume 38.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1531张（+79.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,560 张（Put 3,458 / Call 12,102），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 29.3k / P 21.8k，今日成交量: C 10.5k / P 5.6k，平值价格ATM: C $0.42 / P $0.33 ｜ ATM IV 71.6%，预期波动 ±1.5%，Max Pain 49
Top ΔOI: C 49 +1,531 ｜ P 48 +1,223 ｜ P 48 +803

📆 Forward Expiration Structure

10-30  C +3.5k / P +4.1k ｜ Activity HIGH ｜ 2D
11-02  C +1.3k / P +3.1k ｜ Activity HIGH ｜ 5D
11-04  C +2.1k / P +1.4k ｜ Activity HIGH ｜ 7D
11-06  C -58 / P +0.7k ｜ Activity MEDIUM △ ｜ 9D

📆 10-30 Forward Structure
存量OI: C 91.4k / P 38.1k，今日变化ΔOI: C +3.5k / P +4.1k，平值价格ATM: C $0.75 / P $0.64 ｜ ATM IV 45.0%，净 delta 敞口 41k shares
Top ΔOI: P 47 +1,536 ｜ C 50 +956
仓位参考: Max Pain 50 ｜ Call Wall 50（+2.8%，弱）（OI 4.3k） ｜ Put Wall 45（-7.5%，弱）（OI 4.3k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 45.0%｜历史 Rank 94%（近端代理）｜IV/RV 1.23×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 41,196 股

📆 11-02 Forward Structure
存量OI: C 4.1k / P 5.7k，今日变化ΔOI: C +1.3k / P +3.1k，平值价格ATM: C $0.92 / P $0.75 ｜ ATM IV 35.1%，净 delta 敞口 -18k shares
Top ΔOI: P 45 +720 ｜ P 46 +475
仓位参考: Max Pain 50 ｜ Call Wall 50（+2.8%，弱）（OI 0.6k） ｜ Put Wall 45（-7.5%，弱）（OI 0.8k）
量化解读： 存量 Put 重｜ATM IV 35.1%｜历史 Rank 94%（近端代理）｜IV/RV 0.96×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 17,977 股

📆 11-04 Forward Structure
存量OI: C 10.4k / P 4.2k，今日变化ΔOI: C +2.1k / P +1.4k，平值价格ATM: C $1.18 / P $0.93 ｜ ATM IV 38.6%，净 delta 敞口 18k shares
Top ΔOI: C 50 +467
仓位参考: Max Pain 48 ｜ Call Wall 51.5（+5.9%，弱）（OI 3.1k） ｜ Put Wall 44（-9.5%）（OI 1.7k）
量化解读： 存量 Call 重｜ATM IV 38.6%｜历史 Rank 94%（近端代理）｜IV/RV 1.05×（近似）｜净 delta 敞口 正 18,299 股

11-06（MEDIUM △）Top ΔOI: 49C -2,323 ｜ 44P +502
11-06（MEDIUM △）仓位参考: Max Pain 52 ｜ Put Wall 50（+2.8%，弱）（OI 2.2k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 45.0% vs 11-02 35.1%（差 +9.9pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、GDP 增速 Rate QoQ Adv、PCE 物价 Price Index MoM、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime RANGE | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/SLV_morning.json