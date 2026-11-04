# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.96 ｜ QQQ $691.95
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 160C ΔOI +105（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 154.97 → 今开 158.35（+2.2%） | 较昨收变动（含盘初走势） ｜ 今日高 158.35 ｜ 低 154.06

Options: P/C成交量 2.65 | OI比 1.74 | ATM IV 49.0% | Skew -1.8pp | Term 0.78 | ExpMove ±3.1%（近端） | Rank 97%
量化视角： IV 历史高位（Rank 97%，期权偏贵）｜期限结构倒挂（Term 0.78，近月 IV 高于远月）｜Put 保护异常便宜（Skew -1.8pp，Put IV < Call IV）｜当日成交偏 Put（P/C量 2.65）——观察点，非方向信号
   ⇒ Put/Call Volume: 2.65×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 1.74×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±3.1% ｜ 11-13（9D）±5.3% ｜ 11-20（16D）±7.4% ｜ 11-27（23D）±8.0%
   ⇒ IV–VIX Spread: +32.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,843,112 | GEX Change vs 上次快照 -1,338,030 | Flip: Primary Flip: 159.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 376 / LOW 64 / INVALID 332
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 159.42（全链重定价，覆盖 98%）
Call Wall 165（现价低于该位 6.0%）
最近结构参考: Flip 159（现价低于该位 2.7%）
量化视角： 负 Gamma（884万，无历史分位）｜负 Gamma 加深（134万）｜现价位于 Flip 下方 2.68%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 153（MaxPain，仅结算参考）；上方 165（Call Wall）。
• Gamma 区域：切换参考 159（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 150.0P — Vol 730 | 最新价 $2.70 | OI 1297→1686 (ΔOI +389张) | ΔOI/Volume 53.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增389张（+30.0% vs前日OI），连续性待观察（方向未知）
11-20 141.0P — Vol 473 | 最新价 $1.06 | OI 490→864 (ΔOI +374张) | ΔOI/Volume 79.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增374张（+76.3% vs前日OI），连续性待观察（方向未知）
11-20 160.0C — Vol 756 | 最新价 $3.45 | OI 2111→2389 (ΔOI +278张) | ΔOI/Volume 36.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增278张（+13.2% vs前日OI），连续性待观察（方向未知）
11-13 165.0C — Vol 144 | 最新价 $0.94 | OI 88→204 (ΔOI +116张) | ΔOI/Volume 80.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增116张（+131.8% vs前日OI），连续性待观察（方向未知）
11-13 146.0P — Vol 116 | 最新价 $0.94 | OI 53→164 (ΔOI +111张) | ΔOI/Volume 95.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增111张（+209.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,268 张（Put 874 / Call 394），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 2D
11-13  C +0.4k / P +0.3k ｜ Activity MEDIUM △ ｜ 9D
11-20  C -0.1k / P +0.8k ｜ Activity HIGH ｜ 16D
11-27  C +8 / P +0.1k ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 5.7k / P 9.9k，今日变化ΔOI: C +0.1k / P +0.2k，平值价格ATM: C $3.60 / P $1.26 ｜ ATM IV 49.0%，净 delta 敞口 -4k shares
Top ΔOI: C 162 +55 ｜ P 154 +51 ｜ P 141 +50
仓位参考: Max Pain 153 ｜ Call Wall 159（+2.5%，弱）（OI 0.4k） ｜ Put Wall 153（-1.4%）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 49.0%｜历史 Rank 97%（近端代理）｜IV/RV 1.59×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 4,191 股

11-13（MEDIUM △）Top ΔOI: 165C +116 ｜ 146P +111
11-13（MEDIUM △）仓位参考: Max Pain 153 ｜ Call Wall 160（+3.1%，弱）（OI 0.6k） ｜ Put Wall 148（-4.6%，弱）（OI 0.3k）

📆 11-20 Forward Structure
存量OI: C 23.3k / P 46.7k，今日变化ΔOI: C -0.1k / P +0.8k，平值价格ATM: C $6.48 / P $5.00 ｜ ATM IV 38.4%，净 delta 敞口 -17k shares
Top ΔOI: P 150 +389 ｜ P 141 +374 ｜ C 160 +278
仓位参考: Max Pain 155 ｜ Call Wall 165（+6.3%）（OI 6.9k） ｜ Put Wall 147（-5.3%，弱）（OI 5.7k）
量化解读： 存量 Put 重｜ATM IV 38.4%｜历史 Rank 97%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 16,670 股

11-27（MEDIUM △）Top ΔOI: 155P +51 ｜ 165P +51
11-27（MEDIUM △）仓位参考: Max Pain 158 ｜ Call Wall 152.5（-1.7%，弱）（OI 0.1k） ｜ Put Wall 156（+0.5%）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 49.0% vs 11-13 41.2%（差 +7.7pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/XBI_morning.json