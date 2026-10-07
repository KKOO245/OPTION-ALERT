# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $777.04 ｜ QQQ $757.73
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 55P ΔOI +1,025（距现价 +2.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 55.45 → 今开 53.90（-2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 53.95 ｜ 低 53.60

Options: P/C成交量 0.70 | OI比 0.41 | ATM IV 49.4% | Skew -5.9pp | Term 0.71 | ExpMove ±2.3%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.71，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.9pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.41）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.70×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.41×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±2.3% ｜ 10-12（5D）±3.0% ｜ 10-14（7D）±3.9% ｜ 10-16（9D）±4.2%
   ⇒ IV–VIX Spread: +33.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) 2,770,157 | GEX Change vs 上次快照 -37,792,639 | Flip: Primary Flip: 53.69（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 714 / LOW 162 / INVALID 402
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 53.69（全链重定价，覆盖 96%）
最近结构参考: Flip 54（现价高于该位 0.2%）
量化视角： 正 Gamma（277万，无历史分位）｜正 Gamma 减弱（3779万）｜现价位于 Flip 上方 0.17%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 54（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 54（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 61.0C — Vol 4,332 | 最新价 $0.68 | OI 663→4805 (ΔOI +4142张) | ΔOI/Volume 95.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4142张（+624.7% vs前日OI），连续性待观察（方向未知）
11-06 55.0C — Vol 4,361 | 最新价 $2.50 | OI 354→4188 (ΔOI +3834张) | ΔOI/Volume 87.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3834张（+1083.0% vs前日OI），连续性待观察（方向未知）
11-06 63.0C — Vol 4,223 | 最新价 $0.45 | OI 1678→5146 (ΔOI +3468张) | ΔOI/Volume 82.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3468张（+206.7% vs前日OI），连续性待观察（方向未知）
11-06 60.0C — Vol 4,669 | 最新价 $0.82 | OI 6168→9576 (ΔOI +3408张) | ΔOI/Volume 73.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3408张（+55.2% vs前日OI），连续性待观察（方向未知）
10-23 57.0C — Vol 3,363 | 最新价 $0.99 | OI 676→3381 (ΔOI +2705张) | ΔOI/Volume 80.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2705张（+400.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 17,557 张（Put 0 / Call 17,557），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 39.1k / P 16.1k，今日成交量: C 16.4k / P 11.5k，平值价格ATM: C $0.18 / P $0.42 ｜ ATM IV 49.4%，预期波动 ±1.1%，Max Pain 54
Top ΔOI: C 56 +1,719 ｜ C 57 +1,396 ｜ C 55 +1,039

📆 Forward Expiration Structure

10-09  C +5.4k / P +2.3k ｜ Activity HIGH ｜ 2D
10-12  C +1.2k / P +0.3k ｜ Activity HIGH ｜ 5D
10-14  C +3.4k / P +0.5k ｜ Activity HIGH ｜ 7D
10-16  C -8.0k / P +1.2k ｜ Activity MEDIUM △ ｜ 9D

📆 10-09 Forward Structure
存量OI: C 92.8k / P 27.3k，今日变化ΔOI: C +5.4k / P +2.3k，平值价格ATM: C $0.55 / P $0.70 ｜ ATM IV 38.7%，净 delta 敞口 54k shares
Top ΔOI: C 57 +1,648 ｜ P 50 +725 ｜ C 57 +526
仓位参考: Max Pain 55 ｜ Call Wall 58（+7.8%，弱）（OI 4.7k） ｜ Put Wall 55（+2.3%，弱）（OI 3.6k）
量化解读： 存量 Call 重｜ATM IV 38.7%｜历史 Rank 82%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 53,744 股

📆 10-12 Forward Structure
存量OI: C 4.9k / P 7.6k，今日变化ΔOI: C +1.2k / P +0.3k，平值价格ATM: C $0.70 / P $0.91 ｜ ATM IV 30.4%，净 delta 敞口 5k shares
Top ΔOI: C 55 +227 ｜ C 59 +191 ｜ C 58 +125
仓位参考: Max Pain 56 ｜ Call Wall 58（+7.8%，弱）（OI 0.6k） ｜ Put Wall 54（+0.4%）（OI 2.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 30.4%｜历史 Rank 82%（近端代理）｜IV/RV 0.95×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 4,920 股

📆 10-14 Forward Structure
存量OI: C 6.2k / P 3.9k，今日变化ΔOI: C +3.4k / P +0.5k，平值价格ATM: C $0.98 / P $1.12 ｜ ATM IV 33.4%，净 delta 敞口 -362 shares
Top ΔOI: C 58 +452
仓位参考: Max Pain 56 ｜ Call Wall 58.5（+8.8%，弱）（OI 0.5k） ｜ Put Wall 54（+0.4%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 33.4%｜历史 Rank 82%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 负 362 股

10-16（MEDIUM △）Top ΔOI: 55P +1,025 ｜ 56C +640
10-16（MEDIUM △）仓位参考: Max Pain 56 ｜ Call Wall 50（-7.0%，弱）（OI 26.9k） ｜ Put Wall 50（-7.0%，弱）（OI 23.2k）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 38.7% vs 10-12 30.4%（差 +8.3pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/SLV_morning.json