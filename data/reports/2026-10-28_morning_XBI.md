# 期权晨报 2026-10-28（快照 10:20 ET）

📊 市场环境

SPY $772.31 ｜ QQQ $725.61
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
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 152P ΔOI +3,473（距现价 -2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 154.84 → 今开 153.27（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 155.84 ｜ 低 152.83

Options: P/C成交量 2.86 | OI比 5.75 | ATM IV 42.4% | Skew 8.6pp | Term 0.78 | ExpMove ±2.5%（近端） | Rank 89%
量化视角： IV 历史高位（Rank 89%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜保护溢价显著（Skew 8.6pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 2.86）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.86×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 5.75×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-30（2D）±2.5% ｜ 11-06（9D）±4.3% ｜ 11-13（16D）±6.4% ｜ 11-20（23D）±7.2%
   ⇒ IV–VIX Spread: +25.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -14,176,301 | GEX Change vs 上次快照 -6,100,755 | Flip: Primary Flip: 158.85（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 331 / LOW 74 / INVALID 365
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 158.85（全链重定价，覆盖 96%）
Call Wall 165（现价低于该位 5.8%）
最近结构参考: Flip 159（现价低于该位 2.2%）
量化视角： 负 Gamma（1418万，无历史分位）｜负 Gamma 加深（610万）｜现价位于 Flip 下方 2.19%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 152（MaxPain，仅结算参考）；上方 165（Call Wall）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 152.0P — Vol 6,858 | 最新价 $1.12 | OI 1593→5066 (ΔOI +3473张) | ΔOI/Volume 50.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3473张（+218.0% vs前日OI），连续性待观察（方向未知）
10-30 152.5P — Vol 3,221 | 最新价 $1.35 | OI 128→3195 (ΔOI +3067张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3067张（+2396.1% vs前日OI），连续性待观察（方向未知）
11-20 147.0P — Vol 2,006 | 最新价 $2.28 | OI 3239→5238 (ΔOI +1999张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1999张（+61.7% vs前日OI），连续性待观察（方向未知）
10-30 145.0P — Vol 2,304 | 最新价 $0.10 | OI 1240→2953 (ΔOI +1713张) | ΔOI/Volume 74.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1713张（+138.2% vs前日OI），连续性待观察（方向未知）
10-30 148.0P — Vol 2,544 | 最新价 $0.31 | OI 2674→4037 (ΔOI +1363张) | ΔOI/Volume 53.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1363张（+51.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 11,615 张（Put 11,615 / Call 0），跨 2 个期限｜近端保护（3 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +1.2k / P +10.0k ｜ Activity MEDIUM △ ｜ 2D
11-06  C +0.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 9D
11-13  C +64 / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
11-20  C +0.2k / P +1.9k ｜ Activity HIGH ｜ 23D

📆 10-30 Forward Structure
存量OI: C 11.2k / P 64.4k，今日变化ΔOI: C +1.2k / P +10.0k，平值价格ATM: C $1.94 / P $1.87 ｜ ATM IV 42.4%，净 delta 敞口 -184k shares
Top ΔOI: P 152 +3,473 ｜ P 152 +3,067 ｜ P 145 +1,713
仓位参考: Max Pain 152 ｜ Call Wall 155（-0.2%，弱）（OI 2.2k） ｜ Put Wall 150（-3.5%，弱）（OI 9.1k）
量化解读： 存量 Put 重｜ATM IV 42.4%｜历史 Rank 89%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 183,837 股

11-06（MEDIUM △）Top ΔOI: 156C +210 ｜ 148P +61
11-06（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 156（+0.4%，弱）（OI 0.3k） ｜ Put Wall 151（-2.8%，弱）（OI 0.5k）

11-13（MEDIUM △）Top ΔOI: 140P +86 ｜ 145P +70
11-13（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 160（+3.0%）（OI 0.4k） ｜ Put Wall 153（-1.5%，弱）（OI 0.4k）

📆 11-20 Forward Structure
存量OI: C 20.0k / P 39.5k，今日变化ΔOI: C +0.2k / P +1.9k，平值价格ATM: C $5.40 / P $5.86 ｜ ATM IV 35.4%，净 delta 敞口 -49k shares
Top ΔOI: P 147 +1,999 ｜ P 140 -305 ｜ P 149 +118
仓位参考: Max Pain 155 ｜ Call Wall 165（+6.2%）（OI 7.3k） ｜ Put Wall 147（-5.4%，弱）（OI 5.2k）
量化解读： 存量 Put 重｜ATM IV 35.4%｜历史 Rank 89%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 负 48,950 股

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 42.4% vs 11-06 35.6%（差 +6.8pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/XBI_morning.json