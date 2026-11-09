# 期权晚报 2026-11-09（快照 16:40 ET）

📊 市场环境

SPY $752.69 ｜ QQQ $679.35
VIX 19.92 ↓22.3%（5D -5.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.7（fear）
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
🟡 **近现价集中开仓**: 11-20 150P ΔOI -6,806（距现价 +2.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-13 101P ΔOI +120,790 占该期限总 OI 37.5%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SOXX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
SOXX: 今开 138.58 → 收盘 146.76（+5.9%） ｜ 今日高 148.01 ｜ 低 137.97 ｜ 昨收 136.53 → 收盘 146.76（+7.5%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-11-16，窗口结束前不做对错判定）

Options: P/C成交量 7.24 | OI比 2.02 | ATM IV 66.9% | Skew 9.1pp | Term 0.81 | ExpMove ±5.5%（近端） | Rank 95%
量化视角： IV 历史高位（Rank 95%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价显著（Skew 9.1pp，Put 明显贵于 Call）｜当日成交偏 Put（P/C量 7.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 7.24×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 2.02×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 11-13（4D）±5.5% ｜ 11-20（11D）±8.0% ｜ 11-27（18D）±7.4% ｜ 12-04（25D）±11.5%
   ⇒ IV–VIX Spread: +47.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -71,022,479 | GEX Change vs 上次快照 4,921,689 | Flip: Primary Flip: 158.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 518 / LOW 425 / INVALID 861
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 158.23（全链重定价，覆盖 99%）
最近结构参考: Flip 158（现价低于该位 7.2%）
量化视角： 负 Gamma（7102万，无历史分位）｜负 Gamma 缓解（+492万）｜现价位于 Flip 下方 7.25%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 153（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 158（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-13 101.67P — Vol 2,866 | 最新价 $0.09 | OI 434→121224 (ΔOI +120790张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增120790张（+27831.8% vs前日OI），连续性待观察（方向未知）
11-20 135.0P — Vol 423 | 最新价 $2.06 | OI 2818→7404 (ΔOI +4586张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4586张（+162.7% vs前日OI），连续性待观察（方向未知）
11-20 145.0C — Vol 518 | 最新价 $7.55 | OI 692→5153 (ΔOI +4461张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4461张（+644.6% vs前日OI），连续性待观察（方向未知）
11-20 150.0C — Vol 4,898 | 最新价 $4.50 | OI 637→4871 (ΔOI +4234张) | ΔOI/Volume 86.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4234张（+664.7% vs前日OI），连续性待观察（方向未知）
11-20 115.0P — Vol 50 | 最新价 $0.46 | OI 2696→6382 (ΔOI +3686张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3686张（+136.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 137,757 张（Put 129,062 / Call 8,695），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +3.6k / P +87.7k ｜ Activity HIGH ｜ 4D
11-20  C +11.8k / P -16.1k ｜ Activity HIGH ｜ 11D
11-27  C +0.5k / P +0.2k ｜ Activity HIGH ｜ 18D
12-04  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 25D

📆 11-13 Forward Structure
存量OI: C 106.6k / P 215.5k，今日变化ΔOI: C +3.6k / P +87.7k，平值价格ATM: C $4.07 / P $3.96 ｜ ATM IV 66.9%，净 delta 敞口 245k shares
Top ΔOI: P 101 +120,790 ｜ P 125 -21,742 ｜ P 110 -16,610
仓位参考: Max Pain 153
量化解读： 存量 Put 重｜ATM IV 66.9%｜历史 Rank 95%（近端代理）｜IV/RV 0.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 244,887 股

📆 11-20 Forward Structure
存量OI: C 189.1k / P 311.6k，今日变化ΔOI: C +11.8k / P -16.1k，平值价格ATM: C $6.10 / P $5.61 ｜ ATM IV 58.1%，净 delta 敞口 1.5M shares
Top ΔOI: P 133 -11,368 ｜ P 150 -6,806 ｜ P 135 +4,586
仓位参考: Max Pain 163 ｜ Put Wall 150（+2.2%，弱）（OI 21.2k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 58.1%｜历史 Rank 95%（近端代理）｜IV/RV 0.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,513,724 股

📆 11-27 Forward Structure
存量OI: C 26.4k / P 23.0k，今日变化ΔOI: C +0.5k / P +0.2k，平值价格ATM: C $3.29 / P $7.60 ｜ ATM IV 55.2%，净 delta 敞口 36k shares
Top ΔOI: C 150 +330 ｜ P 166 -118
仓位参考: Max Pain 162 ｜ Put Wall 146.67（-0.1%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜ATM IV 55.2%｜历史 Rank 95%（近端代理）｜IV/RV 0.13×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 36,378 股

📆 12-04 Forward Structure
存量OI: C 4.6k / P 7.9k，今日变化ΔOI: C +0.5k / P +0.4k，平值价格ATM: C $7.37 / P $9.57 ｜ ATM IV 52.5%，净 delta 敞口 11k shares
Top ΔOI: C 150 +242 ｜ C 155 +131 ｜ P 133 +130
仓位参考: Max Pain 162 ｜ Call Wall 153.33（+4.5%，弱）（OI 0.3k） ｜ Put Wall 148.33（+1.1%，弱）（OI 0.9k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 52.5%｜历史 Rank 95%（近端代理）｜IV/RV 0.12×（近似）｜净 delta 敞口 正 11,299 股

📅 事件差分（观察，非因果）: 11-13（4D）ATM IV 66.9% vs 11-20 58.1%（差 +8.8pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-09/SOXX_evening.json