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
🔴 **事件差分**: 10-30（2D）ATM IV 52.3% vs 11-02 36.7%（差 +15.6pp），覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 11-02 76P ΔOI +375 占该期限总 OI 12.0%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 83.19 → 今开 82.78（-0.5%） | 较昨收变动（含盘初走势） ｜ 今日高 82.89 ｜ 低 82.09

Options: P/C成交量 0.07 | OI比 1.15 | ATM IV 82.7% | Skew -0.5pp | Term 0.49 | ExpMove ±3.2%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.49，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.07×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.15×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（2D）±3.2% ｜ 11-02（5D）±3.5% ｜ 11-04（7D）±2.5% ｜ 11-06（9D）±5.6%
   ⇒ IV–VIX Spread: +65.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 60,533,775 | GEX Change vs 上次快照 -1,606,754 | Flip: Primary Flip: 79.39（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 532 / LOW 149 / INVALID 507
结构观察区: Primary Flip 79.39（全链重定价，覆盖 94%）
Put Wall 80（弱结构｜现价高于该位 3.3%） | Call Wall 85（弱结构｜现价低于该位 2.8%）
最近结构参考: Call Wall 85（现价低于该位 2.8%）
量化视角： 正 Gamma（6053万，无历史分位）｜正 Gamma 减弱（161万）｜现价位于 Flip 上方 4.07%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall，弱结构）；上方 84（MaxPain，仅结算参考） / 85（Call Wall，弱结构）。
• Gamma 区域：切换参考 79（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 84.0C — Vol 2,690 | 最新价 $1.01 | OI 8554→10208 (ΔOI +1654张) | ΔOI/Volume 61.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1654张（+19.3% vs前日OI），连续性待观察（方向未知）
11-20 87.0C — Vol 1,238 | 最新价 $1.98 | OI 1242→2001 (ΔOI +759张) | ΔOI/Volume 61.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增759张（+61.1% vs前日OI），连续性待观察（方向未知）
11-20 83.0P — Vol 858 | 最新价 $3.40 | OI 1115→1830 (ΔOI +715张) | ΔOI/Volume 83.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增715张（+64.1% vs前日OI），连续性待观察（方向未知）
10-28 85.0C — Vol 1,053 | 最新价 $0.18 | OI 585→1180 (ΔOI +595张) | ΔOI/Volume 56.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增595张（+101.7% vs前日OI），连续性待观察（方向未知）
11-27 98.0C — Vol 550 | 最新价 $0.43 | OI 2313→2858 (ΔOI +545张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增545张（+23.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,268 张（Put 715 / Call 3,553），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 4.8k / P 5.6k，今日成交量: C 1.7k / P 0.1k，平值价格ATM: C $0.55 / P $0.95 ｜ ATM IV 82.7%，预期波动 ±1.8%，Max Pain 84
Top ΔOI: P 84 -994 ｜ C 85 +595 ｜ P 79 +317

📆 Forward Expiration Structure

10-30  C +1.7k / P +0.3k ｜ Activity MEDIUM △ ｜ 2D
11-02  C +0.5k / P +0.7k ｜ Activity HIGH ｜ 5D
11-04  C +96 / P +65 ｜ Activity MEDIUM △ ｜ 7D
11-06  C +0.2k / P +0.2k ｜ Activity LOW ｜ 9D

📆 10-30 Forward Structure
存量OI: C 135.2k / P 33.6k，今日变化ΔOI: C +1.7k / P +0.3k，平值价格ATM: C $1.50 / P $1.16 ｜ ATM IV 52.3%，净 delta 敞口 81k shares
Top ΔOI: C 84 +1,654 ｜ P 75 +385 ｜ P 86 -249
仓位参考: Max Pain 81 ｜ Call Wall 85（+2.9%，弱）（OI 28.1k） ｜ Put Wall 79（-4.4%，弱）（OI 3.7k）
量化解读： 存量 Call 重｜ATM IV 52.3%｜历史 Rank 100%（近端代理）｜IV/RV 1.35×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 81,067 股

📆 11-02 Forward Structure
存量OI: C 1.5k / P 1.6k，今日变化ΔOI: C +0.5k / P +0.7k，平值价格ATM: C $1.31 / P $1.58 ｜ ATM IV 36.7%，净 delta 敞口 -522 shares
Top ΔOI: P 76 +375 ｜ C 86 +272 ｜ P 82 +152
仓位参考: Max Pain 84 ｜ Call Wall 86（+4.1%）（OI 0.8k） ｜ Put Wall 81（-2.0%，弱）（OI 0.3k）
量化解读： 存量两侧均衡｜ATM IV 36.7%｜历史 Rank 100%（近端代理）｜IV/RV 0.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 522 股

11-04（MEDIUM △）Top ΔOI: 79P +53 ｜ 87C +47
11-04（MEDIUM △）仓位参考: Max Pain 82 ｜ Call Wall 83（+0.5%，弱）（OI 0.2k） ｜ Put Wall 79（-4.4%）（OI 57）

11-06（Activity LOW）仓位参考: Max Pain 85 ｜ Call Wall 85（+2.9%）（OI 3.2k） ｜ Put Wall 80（-3.2%，弱）（OI 2.3k）

📅 事件差分（观察，非因果）: 10-30（2D）ATM IV 52.3% vs 11-02 36.7%（差 +15.6pp）——覆盖 美联储议息会议 Statement、美联储利率决议 Decision、Fed Press Conference、PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Adv、Personal Income MoM、Personal Spending MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-28/GDX_morning.json