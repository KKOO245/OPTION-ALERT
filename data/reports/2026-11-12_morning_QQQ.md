# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $756.94 ｜ QQQ $685.45
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **近现价集中开仓**: 11-13 680P ΔOI +6,545（距现价 -0.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-17 707C ΔOI +9,526 占该期限总 OI 12.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 690.38 → 今开 680.21（-1.5%） | 较昨收变动（含盘初走势） ｜ 今日高 688.42 ｜ 低 679.84

Options: P/C成交量 0.83 | OI比 1.29 | ATM IV 40.6% | Skew 6.1pp | Term 0.60 | ExpMove ±1.5%（近端） | Rank 96%
量化视角： IV 历史高位（Rank 96%，期权偏贵）｜期限结构倒挂（Term 0.60，近月 IV 高于远月）｜保护溢价显著（Skew 6.1pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.83×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.29×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 33% ｜ P/C OI(近端) 20%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 33%）｜近端持仓结构中性（P/C OI 分位 20%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-13（1D）±1.5% ｜ 11-16（4D）±2.0% ｜ 11-17（5D）±2.4% ｜ 11-18（6D）±2.9%
   ⇒ IV–VIX Spread: +22.2pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -260,698,755 | GEX Change vs 上次快照 -277,118,484 | Flip: Primary Flip: 691.05（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 3833 / LOW 354 / INVALID 1731
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 691.05（全链重定价，覆盖 98%）
Put Wall 680（弱结构｜现价高于该位 0.8%） | Call Wall 700（弱结构｜现价低于该位 2.1%）
最近结构参考: Put Wall 680（现价高于该位 0.8%）
量化视角： 负 Gamma（2.61亿，历史分位 33%，中性区）｜由正转负（2.77亿）｜现价位于 Flip 下方 0.81%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 680（Put Wall，弱结构）；上方 688（MaxPain，仅结算参考） / 700（Call Wall，弱结构）。
• Gamma 区域：切换参考 691（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-18 620.0P — Vol 12,213 | 最新价 $0.32 | OI 402→11539 (ΔOI +11137张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11137张（+2770.4% vs前日OI），连续性待观察（方向未知）
11-20 680.0P — Vol 33,350 | 最新价 $7.17 | OI 76415→87076 (ΔOI +10661张) | ΔOI/Volume 32.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10661张（+13.9% vs前日OI），连续性待观察（方向未知）
11-20 700.0C — Vol 28,611 | 最新价 $6.67 | OI 24969→34890 (ΔOI +9921张) | ΔOI/Volume 34.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9921张（+39.7% vs前日OI），连续性待观察（方向未知）
11-17 707.0C — Vol 14,644 | 最新价 $1.86 | OI 768→10294 (ΔOI +9526张) | ΔOI/Volume 65.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9526张（+1240.4% vs前日OI），连续性待观察（方向未知）
11-12 685.0P — Vol 29,746 | 最新价 $1.98 | OI 462→8656 (ΔOI +8194张) | ΔOI/Volume 27.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8194张（+1773.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 49,439 张（Put 29,992 / Call 19,447），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $9M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 122.9k / P 158.4k，今日成交量: C 486.8k / P 404.0k，平值价格ATM: C $3.50 / P $2.53 ｜ ATM IV 40.6%，预期波动 ±0.9%，Max Pain 688
Top ΔOI: P 685 +8,194 ｜ P 690 +7,111 ｜ P 680 +5,816

📆 Forward Expiration Structure

11-13  C +24.7k / P +45.2k ｜ Activity HIGH ｜ 1D
11-16  C +10.8k / P +21.6k ｜ Activity HIGH ｜ 4D
11-17  C +16.4k / P +17.8k ｜ Activity HIGH ｜ 5D
11-18  C +6.2k / P +30.3k ｜ Activity HIGH ｜ 6D

📆 11-13 Forward Structure
存量OI: C 326.9k / P 455.0k，今日变化ΔOI: C +24.7k / P +45.2k，平值价格ATM: C $5.80 / P $4.64 ｜ ATM IV 32.4%，净 delta 敞口 -1.9M shares
Top ΔOI: P 680 +6,545 ｜ C 710 +5,411 ｜ P 678 +5,289
仓位参考: Max Pain 685 ｜ Call Wall 700（+2.1%，弱）（OI 14.4k） ｜ Put Wall 685（-0.1%，弱）（OI 26.5k）
量化解读： 存量 Put 重｜ATM IV 32.4%｜历史 Rank 96%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 1,922,605 股

📆 11-16 Forward Structure
存量OI: C 57.0k / P 63.0k，今日变化ΔOI: C +10.8k / P +21.6k，平值价格ATM: C $7.18 / P $6.48 ｜ ATM IV 23.5%，净 delta 敞口 -196k shares
Top ΔOI: C 700 +5,786 ｜ C 720 +2,495
仓位参考: Max Pain 685 ｜ Call Wall 700（+2.1%，弱）（OI 7.4k） ｜ Put Wall 690（+0.7%，弱）（OI 1.6k）
量化解读： 存量两侧均衡｜ATM IV 23.5%｜历史 Rank 96%（近端代理）｜IV/RV 0.67×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 196,254 股

📆 11-17 Forward Structure
存量OI: C 38.0k / P 40.4k，今日变化ΔOI: C +16.4k / P +17.8k，平值价格ATM: C $8.68 / P $8.02 ｜ ATM IV 25.4%，净 delta 敞口 50k shares
Top ΔOI: C 707 +9,526
仓位参考: Max Pain 676
量化解读： 存量两侧均衡｜ATM IV 25.4%｜历史 Rank 96%（近端代理）｜IV/RV 0.72×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 49,767 股

📆 11-18 Forward Structure
存量OI: C 20.9k / P 60.3k，今日变化ΔOI: C +6.2k / P +30.3k，平值价格ATM: C $10.49 / P $9.11 ｜ ATM IV 26.9%，净 delta 敞口 -194k shares
Top ΔOI: P 620 +11,137 ｜ P 600 +7,899 ｜ P 646 +2,315
仓位参考: Max Pain 678 ｜ Call Wall 700（+2.1%，弱）（OI 1.7k）
量化解读： 存量 Put 重｜ATM IV 26.9%｜历史 Rank 96%（近端代理）｜IV/RV 0.76×（近似）｜净 delta 敞口 负 193,629 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 32.4% vs 11-16 23.5%（差 +8.9pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/QQQ_morning.json