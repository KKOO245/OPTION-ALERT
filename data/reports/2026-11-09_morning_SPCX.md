# 期权晨报 2026-11-09（快照 10:20 ET）

📊 市场环境

SPY $748.63 ｜ QQQ $674.68
VIX 21.34 ↓16.8%（5D +0.9%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 31.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-09

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 待公布 ｜ 前值 0.3
- 周二 11-10 08:30　【高】Core Inflation Rate YoY　预测 2.8 ｜ 实际 待公布 ｜ 前值 2.6
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.6
- 周二 11-10 08:30　【高】Inflation Rate YoY　预测 3.9 ｜ 实际 待公布 ｜ 前值 3.7
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-11 140C ΔOI +554（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SPCX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SPCX  昨收 134.27 → 今开 136.53（+1.7%） | 较昨收变动（含盘初走势） ｜ 今日高 143.20 ｜ 低 135.37

Options: P/C成交量 0.43 | OI比 1.23 | ATM IV 94.4% | Skew 5.0pp | Term 0.63 | ExpMove ±4.9%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.63，近月 IV 高于远月）｜保护溢价中性（Skew 5.0pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.43×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-11（2D）±4.9% ｜ 11-13（4D）±6.4% ｜ 11-16（7D）±7.3% ｜ 11-18（9D）±13.1%
   ⇒ IV–VIX Spread: +73.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 42,515,101 | GEX Change vs 上次快照 59,131,379 | Flip: Primary Flip: 136.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 875 / LOW 198 / INVALID 637
结构观察区: Primary Flip 136.53（全链重定价，覆盖 99%）
Put Wall 130（弱结构｜现价高于该位 9.0%）
最近结构参考: Flip 137（现价高于该位 3.8%）
量化视角： 正 Gamma（4252万，无历史分位）｜由负转正（+5913万）｜现价位于 Flip 上方 3.77%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 130（Put Wall，弱结构） / 131（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 137（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 160.0C — Vol 44,046 | 最新价 $0.70 | OI 40334→72305 (ΔOI +31971张) | ΔOI/Volume 72.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增31971张（+79.3% vs前日OI），连续性待观察（方向未知）
11-13 75.0P — Vol 9,489 | 最新价 $0.04 | OI 1268→8586 (ΔOI +7318张) | ΔOI/Volume 77.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7318张（+577.1% vs前日OI），连续性待观察（方向未知）
11-13 80.0P — Vol 5,825 | 最新价 $0.05 | OI 5050→10692 (ΔOI +5642张) | ΔOI/Volume 96.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5642张（+111.7% vs前日OI），连续性待观察（方向未知）
11-20 150.0C — Vol 15,868 | 最新价 $1.85 | OI 29250→34874 (ΔOI +5624张) | ΔOI/Volume 35.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5624张（+19.2% vs前日OI），连续性待观察（方向未知）
11-20 155.0C — Vol 7,013 | 最新价 $1.16 | OI 11273→15809 (ΔOI +4536张) | ΔOI/Volume 64.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4536张（+40.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 55,091 张（Put 12,960 / Call 42,131），跨 2 个期限｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 47.4k / P 58.6k，今日成交量: C 81.2k / P 34.7k，平值价格ATM: C $1.15 / P $1.79 ｜ ATM IV 94.4%，预期波动 ±2.1%，Max Pain 131
Top ΔOI: C 143 +3,470 ｜ C 140 +2,772 ｜ C 144 +2,117

📆 Forward Expiration Structure

11-11  C +3.8k / P +3.0k ｜ Activity HIGH ｜ 2D
11-13  C +23.0k / P +34.2k ｜ Activity HIGH ｜ 4D
11-16  C +1.9k / P +0.5k ｜ Activity HIGH ｜ 7D
11-18  C +0.9k / P +0.4k ｜ Activity HIGH ｜ 9D

📆 11-11 Forward Structure
存量OI: C 17.9k / P 13.9k，今日变化ΔOI: C +3.8k / P +3.0k，平值价格ATM: C $3.19 / P $3.74 ｜ ATM IV 77.8%，净 delta 敞口 199k shares
Top ΔOI: C 140 +554 ｜ P 130 +467 ｜ C 144 +451
仓位参考: Max Pain 130 ｜ Call Wall 140（-1.2%，弱）（OI 1.8k） ｜ Put Wall 130（-8.2%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜ATM IV 77.8%｜历史 Rank 93%（近端代理）｜IV/RV 1.07×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 199,235 股

📆 11-13 Forward Structure
存量OI: C 116.3k / P 112.1k，今日变化ΔOI: C +23.0k / P +34.2k，平值价格ATM: C $4.25 / P $4.80 ｜ ATM IV 74.3%，净 delta 敞口 915k shares
Top ΔOI: C 135 +3,678
仓位参考: Max Pain 140 ｜ Call Wall 150（+5.9%，弱）（OI 6.5k） ｜ Put Wall 135（-4.7%，弱）（OI 6.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 74.3%｜历史 Rank 93%（近端代理）｜IV/RV 1.02×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 915,347 股

📆 11-16 Forward Structure
存量OI: C 5.1k / P 2.0k，今日变化ΔOI: C +1.9k / P +0.5k，平值价格ATM: C $5.05 / P $5.30 ｜ ATM IV 64.4%，净 delta 敞口 53k shares
Top ΔOI: C 150 +148
仓位参考: Max Pain 132 ｜ Call Wall 150（+5.9%，弱）（OI 1.0k） ｜ Put Wall 130（-8.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 64.4%｜历史 Rank 93%（近端代理）｜IV/RV 0.89×（近似）｜净 delta 敞口 正 52,974 股

📆 11-18 Forward Structure
存量OI: C 2.7k / P 1.7k，今日变化ΔOI: C +0.9k / P +0.4k，平值价格ATM: C $5.80 / P $12.75 ｜ ATM IV 65.9%，净 delta 敞口 50k shares
Top ΔOI: C 130 +187 ｜ C 140 +131 ｜ C 145 +115
仓位参考: Max Pain 130 ｜ Call Wall 145（+2.3%，弱）（OI 0.4k） ｜ Put Wall 130（-8.2%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 65.9%｜历史 Rank 93%（近端代理）｜IV/RV 0.91×（近似）｜净 delta 敞口 正 49,761 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/SPCX_morning.json