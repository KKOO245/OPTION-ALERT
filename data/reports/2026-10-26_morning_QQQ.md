# 期权晨报 2026-10-26（快照 09:08 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 19.22 ↓1.2%（5D +4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-27 685P ΔOI +4,833（距现价 -3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## QQQ

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 704.40 → 今开 702.20（-0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 709.30 ｜ 低 701.16

Options: P/C成交量 1.06 | OI比 1.59 | ATM IV 44.2% | Skew 8.8pp | Term 0.55 | ExpMove ±1.9%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.55，近月 IV 高于远月）｜保护溢价显著（Skew 8.8pp，Put 明显贵于 Call）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 1.06×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.59×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ⇒ 历史分位（15年 lambdaclass 全链口径）: GEX 14% ｜ P/C OI(近端) 47%
量化视角的组合解读： Gamma 异常偏负（GEX 分位 14%）｜近端持仓结构中性（P/C OI 分位 47%）——观察点，非方向信号
   ExpMove 期限化（expmove_v1）: 10-27（1D）±1.9% ｜ 10-28（2D）±2.4% ｜ 10-29（3D）±2.7% ｜ 10-30（4D）±3.1%
   ⇒ IV–VIX Spread: +25.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -659,916,851 | GEX Change vs 上次快照 232,780,940 | Flip: Primary Flip: 726.34（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 3057 / LOW 406 / INVALID 1227
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 726.34（全链重定价，覆盖 99%）
Put Wall 690（弱结构｜现价高于该位 2.7%）
最近结构参考: Flip 726（现价低于该位 2.4%）
量化视角： 负 Gamma（6.60亿，历史分位偏负区，比 86% 的交易日更负）｜负 Gamma 缓解（+2.33亿）｜现价位于 Flip 下方 2.43%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 690（Put Wall，弱结构）；上方 712（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 726（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-02 740.0C — Vol 15,691 | 最新价 $0.97 | OI 736→15988 (ΔOI +15252张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15252张（+2072.3% vs前日OI），连续性待观察（方向未知）
11-20 680.0P — Vol 15,173 | 最新价 $10.60 | OI 65697→76958 (ΔOI +11261张) | ΔOI/Volume 74.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11261张（+17.1% vs前日OI），连续性待观察（方向未知）
10-26 720.0C — Vol 27,730 | 最新价 $0.35 | OI 2097→12659 (ΔOI +10562张) | ΔOI/Volume 38.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10562张（+503.7% vs前日OI），连续性待观察（方向未知）
11-06 713.0P — Vol 10,143 | 最新价 $18.32 | OI 39314→49355 (ΔOI +10041张) | ΔOI/Volume 99.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10041张（+25.5% vs前日OI），连续性待观察（方向未知）
11-02 720.0C — Vol 9,265 | 最新价 $5.09 | OI 871→9366 (ΔOI +8495张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8495张（+975.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 55,611 张（Put 21,302 / Call 34,309），跨 4 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $30M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 135.5k / P 215.6k，今日成交量: C 376.9k / P 398.6k，平值价格ATM: C $3.49 / P $3.91 ｜ ATM IV 44.2%，预期波动 ±1.0%，Max Pain 712
Top ΔOI: C 720 +10,562 ｜ P 680 +6,164 ｜ C 710 +6,152

📆 Forward Expiration Structure

10-27  C +19.5k / P +25.8k ｜ Activity HIGH ｜ 1D
10-28  C +12.6k / P +20.9k ｜ Activity HIGH ｜ 2D
10-29  C +16.4k / P +9.4k ｜ Activity HIGH ｜ 3D
10-30  C +8.8k / P +5.5k ｜ Activity MEDIUM △ ｜ 4D

📆 10-27 Forward Structure
存量OI: C 94.3k / P 114.4k，今日变化ΔOI: C +19.5k / P +25.8k，平值价格ATM: C $4.73 / P $8.57 ｜ ATM IV 32.3%，净 delta 敞口 262k shares
Top ΔOI: P 685 +4,833 ｜ C 719 +4,166 ｜ C 710 +3,259
仓位参考: Max Pain 715 ｜ Call Wall 710（+0.2%，弱）（OI 4.4k） ｜ Put Wall 690（-2.6%，弱）（OI 3.4k）
量化解读： 存量 Put 重｜ATM IV 32.3%｜历史 Rank 98%（近端代理）｜IV/RV 1.78×（近似）｜净 delta 敞口 正 262,387 股

📆 10-28 Forward Structure
存量OI: C 42.3k / P 53.9k，今日变化ΔOI: C +12.6k / P +20.9k，平值价格ATM: C $6.41 / P $10.57 ｜ ATM IV 33.0%，净 delta 敞口 156k shares
仓位参考: Max Pain 716 ｜ Call Wall 720（+1.6%，弱）（OI 1.8k） ｜ Put Wall 720（+1.6%，弱）（OI 2.6k）
量化解读： 存量 Put 重｜ATM IV 33.0%｜历史 Rank 98%（近端代理）｜IV/RV 1.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 156,100 股

📆 10-29 Forward Structure
存量OI: C 36.0k / P 54.5k，今日变化ΔOI: C +16.4k / P +9.4k，平值价格ATM: C $7.65 / P $11.17 ｜ ATM IV 33.4%，净 delta 敞口 126k shares
Top ΔOI: P 660 +3,829 ｜ C 725 +1,915 ｜ C 753 +1,778
仓位参考: Max Pain 718 ｜ Call Wall 725（+2.3%，弱）（OI 2.3k） ｜ Put Wall 705（-0.5%，弱）（OI 1.8k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 33.4%｜历史 Rank 98%（近端代理）｜IV/RV 1.84×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 126,014 股

10-30（MEDIUM △）Top ΔOI: 700P -16,350 ｜ 675P -12,136
10-30（MEDIUM △）仓位参考: Max Pain 725 ｜ Call Wall 729（+2.9%，弱）（OI 13.2k） ｜ Put Wall 690（-2.6%，弱）（OI 90.9k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/QQQ_morning.json