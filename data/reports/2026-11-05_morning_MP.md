# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $752.25 ｜ QQQ $657.13
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🔴 **事件差分**: 11-06（1D）ATM IV 163.7% vs 11-13 90.4%（差 +73.3pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 35P ΔOI +994（距现价 +2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 35.91 → 今开 36.15（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 36.54 ｜ 低 33.15

Options: P/C成交量 1.32 | OI比 0.47 | ATM IV 163.7% | Skew -8.8pp | Term 0.45 | ExpMove ±7.8%（近端） | Rank 100%
量化视角： IV 历史高位（Rank 100%，期权偏贵）｜期限结构倒挂（Term 0.45，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.8pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.47）+ 当日成交偏 Put（P/C量 1.32）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.32×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.47×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±7.8% ｜ 11-13（8D）±10.6% ｜ 11-20（15D）±12.5% ｜ 11-27（22D）±6.8%
   ⇒ IV–VIX Spread: +142.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -429,529 | GEX Change vs 上次快照 792,630 | Flip: Primary Flip: 34.76（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 238 / LOW 53 / INVALID 217
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 34.76（全链重定价，覆盖 99%）
Put Wall 35（现价低于该位 2.9%）
最近结构参考: Flip 35（现价低于该位 2.2%）
量化视角： 负 Gamma（43万，无历史分位）｜负 Gamma 缓解（+79万）｜现价位于 Flip 下方 2.18%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 35（Put Wall） / 38（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 35（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 65.0C — Vol 2,023 | 最新价 $0.05 | OI 1023→3006 (ΔOI +1983张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1983张（+193.8% vs前日OI），连续性待观察（方向未知）
11-06 36.0C — Vol 1,472 | 最新价 $1.25 | OI 7→1473 (ΔOI +1466张) | ΔOI/Volume 99.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1466张（+20942.9% vs前日OI），连续性待观察（方向未知）
11-06 35.0P — Vol 2,306 | 最新价 $1.20 | OI 1533→2527 (ΔOI +994张) | ΔOI/Volume 43.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增994张（+64.8% vs前日OI），连续性待观察（方向未知）
11-06 37.0C — Vol 876 | 最新价 $1.00 | OI 40→880 (ΔOI +840张) | ΔOI/Volume 95.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增840张（+2100.0% vs前日OI），连续性待观察（方向未知）
11-06 39.0C — Vol 712 | 最新价 $0.44 | OI 192→739 (ΔOI +547张) | ΔOI/Volume 76.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增547张（+284.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,830 张（Put 994 / Call 4,836），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +2.8k / P +1.7k ｜ Activity HIGH ｜ 1D
11-13  C +0.8k / P +72 ｜ Activity MEDIUM △ ｜ 8D
11-20  C +2.2k / P +0.7k ｜ Activity MEDIUM △ ｜ 15D
11-27  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

📆 11-06 Forward Structure
存量OI: C 17.2k / P 8.1k，今日变化ΔOI: C +2.8k / P +1.7k，平值价格ATM: C $1.37 / P $1.30 ｜ ATM IV 163.7%，净 delta 敞口 -20k shares
Top ΔOI: C 36 +1,466 ｜ P 35 +994 ｜ C 37 +840
仓位参考: Max Pain 38 ｜ Call Wall 36（+5.9%，弱）（OI 1.5k） ｜ Put Wall 35（+2.9%）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 163.7%｜历史 Rank 100%（近端代理）｜IV/RV 3.06×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 19,743 股

11-13（MEDIUM △）仓位参考: Max Pain 40 ｜ Call Wall 35（+2.9%，弱）（OI 0.5k） ｜ Put Wall 35（+2.9%，弱）（OI 0.3k）

11-20（MEDIUM △）Top ΔOI: 42P +248 ｜ 32P +131
11-20（MEDIUM △）仓位参考: Max Pain 44 ｜ Put Wall 35（+2.9%）（OI 3.7k）

11-27（MEDIUM △）Top ΔOI: 31P +70 ｜ 36C +44
11-27（MEDIUM △）仓位参考: Max Pain 44 ｜ Put Wall 31（-8.8%，弱）（OI 71）

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 163.7% vs 11-13 90.4%（差 +73.3pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=85 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=85）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/MP_morning.json