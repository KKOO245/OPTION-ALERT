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

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-09 180C ΔOI +1,210（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 178.45 → 今开 174.80（-2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 177.18 ｜ 低 172.77

Options: P/C成交量 0.21 | OI比 0.55 | ATM IV 64.2% | Skew -4.7pp | Term 0.97 | ExpMove ±3.1%（近端） | Rank 18%
量化视角： IV 历史低位（Rank 18%，期权偏便宜）｜期限结构正常（Term 0.97）｜Put 保护异常便宜（Skew -4.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.21×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±3.1% ｜ 10-16（8D）±6.7% ｜ 10-23（15D）±9.5% ｜ 10-30（22D）±12.3%
   ⇒ IV–VIX Spread: +48.7pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,890,227 | GEX Change vs 上次快照 -1,473,162 | Flip: Primary Flip: 177.40（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 410 / LOW 145 / INVALID 289
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 177.40（全链重定价，覆盖 96%）
最近结构参考: Flip 177（现价低于该位 0.8%）
量化视角： 负 Gamma（389万，无历史分位）｜负 Gamma 加深（147万）｜现价位于 Flip 下方 0.81%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 185（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 177（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 185.0C — Vol 3,368 | 最新价 $1.23 | OI 1175→2497 (ΔOI +1322张) | ΔOI/Volume 39.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1322张（+112.5% vs前日OI），连续性待观察（方向未知）
10-09 180.0C — Vol 2,844 | 最新价 $2.62 | OI 295→1505 (ΔOI +1210张) | ΔOI/Volume 42.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1210张（+410.2% vs前日OI），连续性待观察（方向未知）
10-16 205.0C — Vol 1,408 | 最新价 $0.75 | OI 1694→2857 (ΔOI +1163张) | ΔOI/Volume 82.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1163张（+68.7% vs前日OI），连续性待观察（方向未知）
10-16 225.0C — Vol 723 | 最新价 $0.17 | OI 358→1036 (ΔOI +678张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增678张（+189.4% vs前日OI），连续性待观察（方向未知）
10-09 182.5C — Vol 2,101 | 最新价 $1.80 | OI 290→937 (ΔOI +647张) | ΔOI/Volume 30.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增647张（+223.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,020 张（Put 0 / Call 5,020），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +2.8k / P +2.3k ｜ Activity HIGH ｜ 1D
10-16  C +5.3k / P +1.0k ｜ Activity HIGH ｜ 8D
10-23  C +1.0k / P +1.0k ｜ Activity MEDIUM △ ｜ 15D
10-30  C +0.7k / P +0.4k ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 71.4k / P 39.5k，今日变化ΔOI: C +2.8k / P +2.3k，平值价格ATM: C $3.40 / P $2.01 ｜ ATM IV 64.2%，净 delta 敞口 74k shares
Top ΔOI: C 185 +1,322 ｜ C 180 +1,210
仓位参考: Max Pain 185 ｜ Call Wall 187.5（+6.6%，弱）（OI 8.7k） ｜ Put Wall 177.5（+0.9%，弱）（OI 2.5k）
量化解读： 存量 Call 重｜ATM IV 64.2%｜历史 Rank 18%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 73,554 股

📆 10-16 Forward Structure
存量OI: C 91.3k / P 81.1k，今日变化ΔOI: C +5.3k / P +1.0k，平值价格ATM: C $6.55 / P $5.21 ｜ ATM IV 55.1%，净 delta 敞口 70k shares
Top ΔOI: C 185 +427
仓位参考: Max Pain 180 ｜ Call Wall 190（+8.0%，弱）（OI 2.9k） ｜ Put Wall 165（-6.2%，弱）（OI 3.4k）
量化解读： 存量两侧均衡｜ATM IV 55.1%｜历史 Rank 18%（近端代理）｜IV/RV 0.98×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 69,509 股

10-23（MEDIUM △）Top ΔOI: 170P +187 ｜ 190C +186
10-23（MEDIUM △）仓位参考: Max Pain 188 ｜ Call Wall 190（+8.0%，弱）（OI 1.1k） ｜ Put Wall 170（-3.4%，弱）（OI 0.7k）

10-30（MEDIUM △）Top ΔOI: 200C +314 ｜ 180C +146
10-30（MEDIUM △）仓位参考: Max Pain 185 ｜ Call Wall 185（+5.1%，弱）（OI 1.2k） ｜ Put Wall 170（-3.4%，弱）（OI 0.7k）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 64.2% vs 10-16 55.1%（差 +9.1pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=43 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=43）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/COIN_morning.json