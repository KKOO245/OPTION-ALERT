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
🔴 **事件差分**: 11-06（1D）ATM IV 68.9% vs 11-09 42.8%（差 +26.1pp），覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: NORMAL → ELEVATED（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 11-06 86C ΔOI +1,388（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 84.59 → 今开 86.61（+2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 87.96 ｜ 低 83.63

Options: P/C成交量 2.25 | OI比 0.33 | ATM IV 68.9% | Skew -16.8pp | Term 0.62 | ExpMove ±3.5%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.62，近月 IV 高于远月）｜Put 保护异常便宜（Skew -16.8pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.33）+ 当日成交偏 Put（P/C量 2.25）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 2.25×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.33×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（1D）±3.5% ｜ 11-09（4D）±3.4% ｜ 11-11（6D）±4.9% ｜ 11-13（8D）±6.1%
   ⇒ IV–VIX Spread: +47.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,196,014 | GEX Change vs 上次快照 5,521,849 | Flip: Primary Flip: 79.17（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 538 / LOW 136 / INVALID 466
结构观察区: Primary Flip 79.17（全链重定价，覆盖 95%）
Call Wall 81（弱结构｜现价高于该位 4.2%）
最近结构参考: Call Wall 81（现价高于该位 4.2%）
量化视角： 正 Gamma（3120万，无历史分位）｜正 Gamma 增强（+552万）｜现价位于 Flip 上方 6.63%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 78（MaxPain，仅结算参考） / 81（Call Wall，弱结构）。
• Gamma 区域：切换参考 79（全链重定价，覆盖 95%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 79.0P — Vol 6,386 | 最新价 $0.49 | OI 295→6375 (ΔOI +6080张) | ΔOI/Volume 95.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6080张（+2061.0% vs前日OI），连续性待观察（方向未知）
11-13 82.0P — Vol 3,347 | 最新价 $1.15 | OI 270→3521 (ΔOI +3251张) | ΔOI/Volume 97.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3251张（+1204.1% vs前日OI），连续性待观察（方向未知）
11-13 88.5C — Vol 3,144 | 最新价 $0.82 | OI 142→3279 (ΔOI +3137张) | ΔOI/Volume 99.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3137张（+2209.2% vs前日OI），连续性待观察（方向未知）
11-13 70.0P — Vol 3,030 | 最新价 $0.07 | OI 1068→3784 (ΔOI +2716张) | ΔOI/Volume 89.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2716张（+254.3% vs前日OI），连续性待观察（方向未知）
11-06 89.0C — Vol 2,445 | 最新价 $0.16 | OI 164→2550 (ΔOI +2386张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2386张（+1454.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 17,570 张（Put 12,047 / Call 5,523），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +3.7k / P +2.0k ｜ Activity HIGH ｜ 1D
11-09  C +0.4k / P +0.8k ｜ Activity HIGH ｜ 4D
11-11  C +1.2k / P +62 ｜ Activity HIGH ｜ 6D
11-13  C +5.0k / P +13.9k ｜ Activity HIGH ｜ 8D

📆 11-06 Forward Structure
存量OI: C 98.6k / P 33.0k，今日变化ΔOI: C +3.7k / P +2.0k，平值价格ATM: C $2.10 / P $0.90 ｜ ATM IV 68.9%，净 delta 敞口 -183k shares
Top ΔOI: C 89 +2,386 ｜ C 86 +1,388 ｜ C 88 +866
仓位参考: Max Pain 78 ｜ Call Wall 81（-4.1%，弱）（OI 21.9k） ｜ Put Wall 80（-5.2%，弱）（OI 3.1k）
量化解读： 存量 Call 重｜ATM IV 68.9%｜历史 Rank 98%（近端代理）｜IV/RV 1.29×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 183,493 股

📆 11-09 Forward Structure
存量OI: C 1.7k / P 1.4k，今日变化ΔOI: C +0.4k / P +0.8k，平值价格ATM: C $1.93 / P $0.96 ｜ ATM IV 42.8%，净 delta 敞口 3k shares
Top ΔOI: P 77 +561 ｜ P 86 +131 ｜ C 85 +106
仓位参考: Max Pain 79 ｜ Call Wall 83（-1.7%）（OI 0.4k） ｜ Put Wall 86（+1.9%，弱）（OI 0.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 42.8%｜历史 Rank 98%（近端代理）｜IV/RV 0.80×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 2,578 股

📆 11-11 Forward Structure
存量OI: C 3.9k / P 1.4k，今日变化ΔOI: C +1.2k / P +62，平值价格ATM: C $2.67 / P $1.50 ｜ ATM IV 47.6%，净 delta 敞口 16k shares
Top ΔOI: C 85 +239 ｜ P 82 +36
仓位参考: Max Pain 78 ｜ Call Wall 85（+0.7%）（OI 2.1k）
量化解读： 存量 Call 重｜ATM IV 47.6%｜历史 Rank 98%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 16,192 股

📆 11-13 Forward Structure
存量OI: C 12.2k / P 23.1k，今日变化ΔOI: C +5.0k / P +13.9k，平值价格ATM: C $2.74 / P $2.44 ｜ ATM IV 50.0%，净 delta 敞口 -126k shares
Top ΔOI: P 79 +6,080 ｜ P 82 +3,251 ｜ C 88 +3,137
仓位参考: Max Pain 84 ｜ Call Wall 88.5（+4.8%）（OI 3.3k） ｜ Put Wall 79（-6.4%，弱）（OI 6.4k）
量化解读： 存量 Put 重｜ATM IV 50.0%｜历史 Rank 98%（近端代理）｜IV/RV 0.94×（近似）｜净 delta 敞口 负 125,964 股

📅 事件差分（观察，非因果）: 11-06（1D）ATM IV 68.9% vs 11-09 42.8%（差 +26.1pp）——覆盖 Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-05/GDX_morning.json