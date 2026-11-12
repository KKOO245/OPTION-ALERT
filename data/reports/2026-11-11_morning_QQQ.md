# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-12 700C ΔOI +2,459（距现价 +2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 674.76 → 今开 687.28（+1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 689.02 ｜ 低 683.60

Options: P/C成交量 1.03 | OI比 1.37 | ATM IV 28.1% | Skew 4.1pp | Term 0.84 | ExpMove ±1.2%（近端） | Rank 86%
量化视角： IV 历史高位（Rank 86%，期权偏贵）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜保护溢价中性（Skew 4.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.03×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.37×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 49% ｜ P/C OI(近端) 26%
量化视角的组合解读： Gamma 处于历史中位（GEX 分位 49%）｜近端持仓结构中性（P/C OI 分位 26%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 11-12（1D）±1.2% ｜ 11-13（2D）±1.7% ｜ 11-16（5D）±2.1% ｜ 11-17（6D）±2.4%
   ⇒ IV–VIX Spread: +9.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) -35,790,967 | GEX Change vs 上次快照 418,513,111 | Flip: Primary Flip: 686.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3863 / LOW 330 / INVALID 1845
结构观察区: Primary Flip 686.93（全链重定价，覆盖 99%）
Call Wall 700（弱结构｜现价低于该位 2.0%）
最近结构参考: Flip 687（现价低于该位 0.1%）
量化视角： 负 Gamma（3579万，历史分位 49%，中性区）｜负 Gamma 缓解（+4.19亿）｜现价位于 Flip 下方 0.13%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 674（MaxPain，仅结算参考）；上方 700（Call Wall，弱结构）。
• Gamma 区域：切换参考 687（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-30 615.0P — Vol 25,605 | 最新价 $2.67 | OI 5303→28806 (ΔOI +23503张) | ΔOI/Volume 91.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增23503张（+443.2% vs前日OI），连续性待观察（方向未知）
11-24 600.0P — Vol 7,362 | 最新价 $1.29 | OI 0→6712 (ΔOI +6712张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6712张（前日OI缺失），连续性待观察（方向未知）
11-24 660.0P — Vol 6,748 | 最新价 $8.37 | OI 0→6587 (ΔOI +6587张) | ΔOI/Volume 97.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增6587张（前日OI缺失），连续性待观察（方向未知）
12-11 580.0P — Vol 7,099 | 最新价 $2.47 | OI 243→5462 (ΔOI +5219张) | ΔOI/Volume 73.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5219张（+2147.7% vs前日OI），连续性待观察（方向未知）
11-30 700.0C — Vol 5,930 | 最新价 $5.28 | OI 2879→7058 (ΔOI +4179张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4179张（+145.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 46,200 张（Put 42,021 / Call 4,179），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $14M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 118.2k / P 161.9k，今日成交量: C 440.2k / P 455.1k，平值价格ATM: C $2.23 / P $1.97 ｜ ATM IV 28.1%，预期波动 ±0.6%，Max Pain 674
Top ΔOI: C 682 +3,868 ｜ C 700 +3,628 ｜ C 680 +3,617

📆 Forward Expiration Structure

11-12  C +11.6k / P +18.1k ｜ Activity HIGH ｜ 1D
11-13  C +15.0k / P +26.4k ｜ Activity HIGH ｜ 2D
11-16  C +6.0k / P +3.4k ｜ Activity HIGH ｜ 5D
11-17  C +2.8k / P +8.7k ｜ Activity HIGH ｜ 6D

📆 11-12 Forward Structure
存量OI: C 64.3k / P 59.2k，今日变化ΔOI: C +11.6k / P +18.1k，平值价格ATM: C $4.36 / P $3.96 ｜ ATM IV 25.9%，净 delta 敞口 428k shares
Top ΔOI: C 700 +2,459 ｜ P 640 +1,981 ｜ P 670 +1,343
仓位参考: Max Pain 674 ｜ Call Wall 700（+2.0%，弱）（OI 4.2k） ｜ Put Wall 670（-2.3%，弱）（OI 2.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 25.9%｜历史 Rank 86%（近端代理）｜IV/RV 0.76×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 428,496 股

📆 11-13 Forward Structure
存量OI: C 302.2k / P 409.8k，今日变化ΔOI: C +15.0k / P +26.4k，平值价格ATM: C $6.16 / P $5.52 ｜ ATM IV 26.8%，净 delta 敞口 729k shares
Top ΔOI: C 680 +2,932
仓位参考: Max Pain 685 ｜ Call Wall 700（+2.0%，弱）（OI 15.3k） ｜ Put Wall 685（-0.1%，弱）（OI 23.9k）
量化解读： 存量 Put 重｜ATM IV 26.8%｜历史 Rank 86%（近端代理）｜IV/RV 0.79×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 729,201 股

📆 11-16 Forward Structure
存量OI: C 46.2k / P 41.5k，今日变化ΔOI: C +6.0k / P +3.4k，平值价格ATM: C $7.50 / P $6.75 ｜ ATM IV 21.8%，净 delta 敞口 136k shares
Top ΔOI: C 700 +456
仓位参考: Max Pain 675 ｜ Call Wall 704（+2.6%，弱）（OI 3.4k） ｜ Put Wall 670（-2.3%，弱）（OI 1.1k）
量化解读： 存量两侧均衡｜ATM IV 21.8%｜历史 Rank 86%（近端代理）｜IV/RV 0.64×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 136,180 股

📆 11-17 Forward Structure
存量OI: C 21.7k / P 22.6k，今日变化ΔOI: C +2.8k / P +8.7k，平值价格ATM: C $8.82 / P $7.92 ｜ ATM IV 23.3%，净 delta 敞口 67k shares
仓位参考: Max Pain 671 ｜ Call Wall 700（+2.0%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 23.3%｜历史 Rank 86%（近端代理）｜IV/RV 0.69×（近似）｜净 delta 敞口 正 66,742 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location near_call_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/QQQ_morning.json