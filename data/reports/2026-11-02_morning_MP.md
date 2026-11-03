# 期权晨报 2026-11-02（快照 10:20 ET）

📊 市场环境

SPY $752.10 ｜ QQQ $681.09
VIX 18.83 ↓3.0%（5D +2.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.7（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-02

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 11-02 10:00　【高】ISM 制造业 PMI　预测 54.6 ｜ 实际 55.5 ｜ 前值 54.5　✅ 今日已公布
- 周一 11-02 19:00　【高】Midterm Elections　实际 待公布　✅ 今日已公布
- 周二 11-03 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.13 ｜ 实际 待公布 ｜ 前值 7.079
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 待公布 ｜ 前值 54.9
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48.2 ｜ 实际 待公布 ｜ 前值 48

🔍 重点速览
🔴 **事件差分**: 11-06（4D）ATM IV 102.2% vs 11-13 81.1%（差 +21.0pp），覆盖 ISM 制造业 PMI、Midterm Elections 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔵 **期限 OI 集中**: 11-13 48C ΔOI +749 占该期限总 OI 10.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 39.57 → 今开 40.19（+1.6%） | 较昨收变动（含盘初走势） ｜ 今日高 40.76 ｜ 低 39.48

Options: P/C成交量 0.07 | OI比 0.50 | ATM IV 102.2% | Skew 6.2pp | Term 0.65 | ExpMove ±10.6%（近端） | Rank 94%
量化视角： IV 历史高位（Rank 94%，期权偏贵）｜期限结构倒挂（Term 0.65，近月 IV 高于远月）｜保护溢价显著（Skew 6.2pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.50）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.07×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（4D）±10.6% ｜ 11-13（11D）±4.7% ｜ 11-20（18D）±13.9% ｜ 11-27（25D）±12.9%
   ⇒ IV–VIX Spread: +83.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,396,037 | GEX Change vs 上次快照 481,448 | Flip: Primary Flip: 36.96（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 308 / LOW 36 / INVALID 124
结构观察区: Primary Flip 36.96（全链重定价，覆盖 100%）
最近结构参考: Flip 37（现价高于该位 9.2%）
量化视角： 正 Gamma（240万，无历史分位）｜正 Gamma 增强（+48万）｜现价位于 Flip 上方 9.17%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 42（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 37（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 48.0C — Vol 756 | 最新价 $0.30 | OI 108→857 (ΔOI +749张) | ΔOI/Volume 99.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增749张（+693.5% vs前日OI），连续性待观察（方向未知）
11-06 38.0P — Vol 1,021 | 最新价 $1.08 | OI 862→1421 (ΔOI +559张) | ΔOI/Volume 54.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增559张（+64.8% vs前日OI），连续性待观察（方向未知）
11-06 45.0C — Vol 277 | 最新价 $0.32 | OI 1765→1971 (ΔOI +206张) | ΔOI/Volume 74.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增206张（+11.7% vs前日OI），连续性待观察（方向未知）
11-06 42.0C — Vol 260 | 最新价 $0.85 | OI 464→663 (ΔOI +199张) | ΔOI/Volume 76.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增199张（+42.9% vs前日OI），连续性待观察（方向未知）
11-13 39.0P — Vol 187 | 最新价 $2.03 | OI 497→625 (ΔOI +128张) | ΔOI/Volume 68.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增128张（+25.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,841 张（Put 687 / Call 1,154），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +1.0k / P +0.8k ｜ Activity HIGH ｜ 4D
11-13  C +0.8k / P +0.4k ｜ Activity HIGH ｜ 11D
11-20  C +29 / P +0.1k ｜ Activity LOW ｜ 18D
11-27  C +71 / P +24 ｜ Activity MEDIUM △ ｜ 25D

📆 11-06 Forward Structure
存量OI: C 11.0k / P 5.5k，今日变化ΔOI: C +1.0k / P +0.8k，平值价格ATM: C $1.60 / P $2.68 ｜ ATM IV 102.2%，净 delta 敞口 16k shares
Top ΔOI: P 38 +559 ｜ C 42 +199
仓位参考: Max Pain 42 ｜ Call Wall 43（+6.6%，弱）（OI 1.0k） ｜ Put Wall 38（-5.8%）（OI 1.4k）
量化解读： 存量 Call 重｜ATM IV 102.2%｜历史 Rank 94%（近端代理）｜IV/RV 1.86×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 16,219 股

📆 11-13 Forward Structure
存量OI: C 4.8k / P 2.3k，今日变化ΔOI: C +0.8k / P +0.4k，平值价格ATM: C $1.91 / P $0.00 ｜ ATM IV 81.1%，净 delta 敞口 150 shares
Top ΔOI: P 39 +128
仓位参考: Max Pain 40 ｜ Call Wall 40（-0.9%，弱）（OI 0.8k） ｜ Put Wall 39（-3.3%）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 81.1%｜历史 Rank 94%（近端代理）｜IV/RV 1.48×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 150 股

11-20（Activity LOW）仓位参考: Max Pain 45 ｜ Call Wall 40（-0.9%，弱）（OI 0.9k） ｜ Put Wall 40（-0.9%，弱）（OI 1.5k）

11-27（MEDIUM △）Top ΔOI: 44C +10
11-27（MEDIUM △）仓位参考: Max Pain 44 ｜ Call Wall 44（+9.0%，弱）（OI 1.0k） ｜ Put Wall 38（-5.8%，弱）（OI 68）

📅 事件差分（观察，非因果）: 11-06（4D）ATM IV 102.2% vs 11-13 81.1%（差 +21.0pp）——覆盖 ISM 制造业 PMI、Midterm Elections 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-02/MP_morning.json