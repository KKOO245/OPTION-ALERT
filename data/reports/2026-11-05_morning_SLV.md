# 期权晨报 2026-11-05（快照 10:20 ET）

📊 市场环境

SPY $732.06 ｜ QQQ $647.05
VIX 21.04 ↑26.7%（5D +22.3%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 19.9（extreme fear）
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
🔴 **事件差分**: 11-06（1D）ATM IV 52.8% vs 11-09 37.2%（差 +15.6pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 49C ΔOI +5,544（距现价 +3.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 47.16 → 今开 47.74（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 47.96 ｜ 低 46.86

Options: P/C成交量 0.42 | OI比 0.30 | ATM IV 52.8% | Skew 3.1pp | Term 0.76 | ExpMove ±2.5%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.76，近月 IV 高于远月）｜保护溢价中性（Skew 3.1pp）｜存量 Call 偏重（OI比 0.30）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.30×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±2.5% ｜ 11-09（4D）±3.1% ｜ 11-11（6D）±4.6% ｜ 11-13（8D）±5.2%
   ⇒ IV–VIX Spread: +31.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 46,636,822 | GEX Change vs 上次快照 12,628,152 | Flip: Primary Flip: 45.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 680 / LOW 113 / INVALID 371
结构观察区: Primary Flip 45.56（全链重定价，覆盖 98%）
最近结构参考: Flip 46（现价高于该位 3.5%）
量化视角： 正 Gamma（4664万，无历史分位）｜正 Gamma 增强（+1263万）｜现价位于 Flip 上方 3.49%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 47（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 46（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 49.0C — Vol 9,480 | 最新价 $0.18 | OI 3933→9477 (ΔOI +5544张) | ΔOI/Volume 58.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5544张（+141.0% vs前日OI），连续性待观察（方向未知）
11-13 40.0P — Vol 3,206 | 最新价 $0.06 | OI 1991→4582 (ΔOI +2591张) | ΔOI/Volume 80.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2591张（+130.1% vs前日OI），连续性待观察（方向未知）
12-04 40.0P — Vol 2,406 | 最新价 $0.31 | OI 861→3047 (ΔOI +2186张) | ΔOI/Volume 90.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2186张（+253.9% vs前日OI），连续性待观察（方向未知）
11-27 40.0P — Vol 3,031 | 最新价 $0.22 | OI 3110→4918 (ΔOI +1808张) | ΔOI/Volume 59.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1808张（+58.1% vs前日OI），连续性待观察（方向未知）
11-06 48.0C — Vol 5,972 | 最新价 $0.35 | OI 2810→4342 (ΔOI +1532张) | ΔOI/Volume 25.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1532张（+54.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 13,661 张（Put 6,585 / Call 7,076），跨 4 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +5.7k / P +5.0k ｜ Activity HIGH ｜ 1D
11-09  C +1.7k / P +5.1k ｜ Activity HIGH ｜ 4D
11-11  C +3.0k / P +3.1k ｜ Activity HIGH ｜ 6D
11-13  C +5.1k / P +6.4k ｜ Activity HIGH ｜ 8D

📆 11-06 Forward Structure
存量OI: C 153.2k / P 45.7k，今日变化ΔOI: C +5.7k / P +5.0k，平值价格ATM: C $0.67 / P $0.50 ｜ ATM IV 52.8%，净 delta 敞口 30k shares
Top ΔOI: C 49 +5,544 ｜ C 50 -2,693 ｜ C 48 +1,532
仓位参考: Max Pain 47 ｜ Call Wall 50（+6.0%，弱）（OI 10.2k） ｜ Put Wall 45（-4.6%，弱）（OI 4.8k）
量化解读： 存量 Call 重｜ATM IV 52.8%｜历史 Rank 86%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 29,669 股

📆 11-09 Forward Structure
存量OI: C 9.6k / P 10.6k，今日变化ΔOI: C +1.7k / P +5.1k，平值价格ATM: C $0.80 / P $0.67 ｜ ATM IV 37.2%，净 delta 敞口 -35k shares
Top ΔOI: P 45 +1,507 ｜ P 44 +805
仓位参考: Max Pain 46 ｜ Call Wall 50（+6.0%，弱）（OI 1.7k） ｜ Put Wall 45（-4.6%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜ATM IV 37.2%｜历史 Rank 86%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 35,429 股

📆 11-11 Forward Structure
存量OI: C 12.8k / P 6.3k，今日变化ΔOI: C +3.0k / P +3.1k，平值价格ATM: C $1.10 / P $1.09 ｜ ATM IV 41.8%，净 delta 敞口 12k shares
Top ΔOI: C 50 +880 ｜ P 43 +613
仓位参考: Max Pain 46 ｜ Call Wall 51（+8.2%）（OI 2.6k） ｜ Put Wall 44（-6.7%，弱）（OI 1.1k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 41.8%｜历史 Rank 86%（近端代理）｜IV/RV 0.90×（近似）｜净 delta 敞口 正 12,296 股

📆 11-13 Forward Structure
存量OI: C 54.8k / P 28.9k，今日变化ΔOI: C +5.1k / P +6.4k，平值价格ATM: C $1.34 / P $1.13 ｜ ATM IV 42.8%，净 delta 敞口 14k shares
仓位参考: Max Pain 49 ｜ Call Wall 50（+6.0%，弱）（OI 6.4k） ｜ Put Wall 45（-4.6%，弱）（OI 2.9k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.8%｜历史 Rank 86%（近端代理）｜IV/RV 0.92×（近似）｜净 delta 敞口 正 14,456 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 52.8% vs 11-09 37.2%（差 +15.6pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/SLV_morning.json