# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $773.15 ｜ QQQ $736.29
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 10-16 52P ΔOI +574（距现价 +3.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-19 53C ΔOI +1,285 占该期限总 OI 13.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 53.49 → 今开 51.31（-4.1%） | 较昨收变动（含盘初走势） ｜ 今日高 51.67 ｜ 低 50.68

Options: P/C成交量 0.48 | OI比 0.35 | ATM IV 48.9% | Skew -8.1pp | Term 0.72 | ExpMove ±2.5%（近端） | Rank 82%
量化视角： IV 历史高位（Rank 82%，期权偏贵）｜期限结构倒挂（Term 0.72，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.1pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.35）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.48×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.35×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±2.5% ｜ 10-19（5D）±3.2% ｜ 10-21（7D）±3.8% ｜ 10-23（9D）±4.5%
   ⇒ IV–VIX Spread: +33.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -463,318 | GEX Change vs 上次快照 -31,398,869 | Flip: Primary Flip: 50.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 739 / LOW 170 / INVALID 429
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 50.88（全链重定价，覆盖 94%）
Put Wall 50（弱结构｜现价高于该位 1.7%）
最近结构参考: Flip 51（现价低于该位 0.1%）
量化视角： 负 Gamma（46万，无历史分位）｜由正转负（3140万）｜现价位于 Flip 下方 0.07%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall，弱结构）；上方 54（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 51（全链重定价，覆盖 94%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-14 56.0C — Vol 5,546 | 最新价 $0.04 | OI 3796→8911 (ΔOI +5115张) | ΔOI/Volume 92.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5115张（+134.8% vs前日OI），连续性待观察（方向未知）
11-13 59.0C — Vol 4,245 | 最新价 $0.63 | OI 238→4463 (ΔOI +4225张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4225张（+1775.2% vs前日OI），连续性待观察（方向未知）
11-13 61.0C — Vol 4,240 | 最新价 $0.40 | OI 123→4274 (ΔOI +4151张) | ΔOI/Volume 97.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4151张（+3374.8% vs前日OI），连续性待观察（方向未知）
10-14 55.5C — Vol 5,801 | 最新价 $0.06 | OI 1517→5396 (ΔOI +3879张) | ΔOI/Volume 66.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3879张（+255.7% vs前日OI），连续性待观察（方向未知）
10-23 57.0C — Vol 3,384 | 最新价 $0.24 | OI 3913→6759 (ΔOI +2846张) | ΔOI/Volume 84.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2846张（+72.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 20,216 张（Put 0 / Call 20,216），跨 3 个期限——方向未知，观察连续性，观察点，非方向信号
🎯 今日到期（0DTE）
存量OI: C 39.6k / P 13.7k，今日成交量: C 13.3k / P 6.4k，平值价格ATM: C $0.19 / P $0.37 ｜ ATM IV 48.9%，预期波动 ±1.1%，Max Pain 54
Top ΔOI: C 56 +5,115 ｜ C 55 +3,879 ｜ C 54 +1,996

📆 Forward Expiration Structure

10-16  C +3.6k / P +0.6k ｜ Activity HIGH ｜ 2D
10-19  C +2.3k / P +1.0k ｜ Activity HIGH ｜ 5D
10-21  C +2.0k / P +1.2k ｜ Activity HIGH ｜ 7D
10-23  C +7.0k / P +2.1k ｜ Activity HIGH ｜ 9D

📆 10-16 Forward Structure
存量OI: C 475.0k / P 196.5k，今日变化ΔOI: C +3.6k / P +0.6k，平值价格ATM: C $0.55 / P $0.70 ｜ ATM IV 40.8%，净 delta 敞口 174k shares
Top ΔOI: C 55 +1,038 ｜ C 54 +919 ｜ P 52 +574
仓位参考: Max Pain 56 ｜ Call Wall 50（-1.7%，弱）（OI 27.0k） ｜ Put Wall 50（-1.7%，弱）（OI 23.5k）
量化解读： 存量 Call 重｜ATM IV 40.8%｜历史 Rank 82%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 173,730 股

📆 10-19 Forward Structure
存量OI: C 5.9k / P 3.4k，今日变化ΔOI: C +2.3k / P +1.0k，平值价格ATM: C $0.73 / P $0.92 ｜ ATM IV 32.6%，净 delta 敞口 -53k shares
Top ΔOI: C 53 +1,285 ｜ C 54 +331 ｜ P 53 +325
仓位参考: Max Pain 53 ｜ Call Wall 53（+4.2%）（OI 1.4k） ｜ Put Wall 52.5（+3.3%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 32.6%｜历史 Rank 82%（近端代理）｜IV/RV 1.04×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 52,508 股

📆 10-21 Forward Structure
存量OI: C 5.7k / P 2.6k，今日变化ΔOI: C +2.0k / P +1.2k，平值价格ATM: C $0.94 / P $1.01 ｜ ATM IV 34.4%，净 delta 敞口 -53k shares
Top ΔOI: P 50 +277 ｜ C 53 +242
仓位参考: Max Pain 54 ｜ Call Wall 53.5（+5.2%，弱）（OI 0.7k） ｜ Put Wall 50.5（-0.7%，弱）（OI 0.3k）
量化解读： 存量 Call 重｜ATM IV 34.4%｜历史 Rank 82%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 负 52,745 股

📆 10-23 Forward Structure
存量OI: C 45.0k / P 35.1k，今日变化ΔOI: C +7.0k / P +2.1k，平值价格ATM: C $1.06 / P $1.20 ｜ ATM IV 35.2%，净 delta 敞口 52k shares
Top ΔOI: C 54 +800
仓位参考: Max Pain 57 ｜ Call Wall 55（+8.2%，弱）（OI 1.6k） ｜ Put Wall 55（+8.2%，弱）（OI 3.3k）
量化解读： 存量 Call 重｜ATM IV 35.2%｜历史 Rank 82%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 正 52,302 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 40.8% vs 10-19 32.6%（差 +8.2pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/SLV_morning.json