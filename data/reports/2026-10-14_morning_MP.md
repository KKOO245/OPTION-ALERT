# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $773.15 ｜ QQQ $736.37
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
🔵 **期限 OI 集中**: 11-06 38P ΔOI +653 占该期限总 OI 12.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 42.7）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 42.43 → 今开 41.40（-2.4%） | 较昨收变动（含盘初走势） ｜ 今日高 41.88 ｜ 低 40.34

Options: P/C成交量 0.71 | OI比 0.71 | ATM IV 61.4% | Skew -5.0pp | Term 1.01 | ExpMove ±3.9%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 1.01）｜Put 保护异常便宜（Skew -5.0pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.71）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.71×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.71×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-16（2D）±3.9% ｜ 10-23（9D）±0.0% ｜ 10-30（16D）±10.4% ｜ 11-06（23D）±4.8%
   ⇒ IV–VIX Spread: +45.6pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,766,928 | GEX Change vs 上次快照 2,781,097 | Flip: Candidates 42.74 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 73%（带内） ｜ IV 有效性: VALID 201 / LOW 63 / INVALID 150
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: ≈43（全链重定价，覆盖 73%，CONDITIONAL）
最近结构参考: Flip 43（现价低于该位 5.1%）
量化视角： 负 Gamma（277万，无历史分位）｜负 Gamma 缓解（+278万）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 47（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 43（全链重定价，覆盖 73%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 38.0P — Vol 709 | 最新价 $0.76 | OI 63→716 (ΔOI +653张) | ΔOI/Volume 92.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增653张（+1036.5% vs前日OI），连续性待观察（方向未知）
11-13 39.0P — Vol 435 | 最新价 $1.39 | OI 124→546 (ΔOI +422张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增422张（+340.3% vs前日OI），连续性待观察（方向未知）
10-16 45.0C — Vol 784 | 最新价 $0.21 | OI 844→1259 (ΔOI +415张) | ΔOI/Volume 52.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增415张（+49.2% vs前日OI），连续性待观察（方向未知）
11-06 39.0P — Vol 327 | 最新价 $1.17 | OI 81→354 (ΔOI +273张) | ΔOI/Volume 83.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增273张（+337.0% vs前日OI），连续性待观察（方向未知）
10-16 42.0C — Vol 346 | 最新价 $1.25 | OI 55→247 (ΔOI +192张) | ΔOI/Volume 55.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增192张（+349.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,955 张（Put 1,348 / Call 607），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C +1.2k / P -3.5k ｜ Activity MEDIUM △ ｜ 2D
10-23  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 9D
10-30  C +0.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 16D
11-06  C +0.2k / P +1.1k ｜ Activity HIGH ｜ 23D

📆 10-16 Forward Structure
存量OI: C 23.9k / P 16.9k，今日变化ΔOI: C +1.2k / P -3.5k，平值价格ATM: C $0.80 / P $0.78 ｜ ATM IV 61.4%，净 delta 敞口 378k shares
Top ΔOI: P 55 -1,635 ｜ P 50 -1,509
仓位参考: Max Pain 47 ｜ Put Wall 40（-1.3%，弱）（OI 1.3k）
量化解读： 存量 Call 重｜ATM IV 61.4%｜历史 Rank 40%（近端代理）｜IV/RV 1.40×（近似）｜净 delta 敞口 正 378,133 股

10-23（MEDIUM △）Top ΔOI: 43C +90 ｜ 54P -76
10-23（MEDIUM △）仓位参考: Max Pain 47 ｜ Call Wall 43（+6.1%，弱）（OI 99） ｜ Put Wall 40（-1.3%，弱）（OI 0.3k）

10-30（MEDIUM △）Top ΔOI: 37P +86
10-30（MEDIUM △）仓位参考: Max Pain 47 ｜ Put Wall 44（+8.5%）（OI 1.6k）

📆 11-06 Forward Structure
存量OI: C 2.8k / P 2.5k，今日变化ΔOI: C +0.2k / P +1.1k，平值价格ATM: C $0.00 / P $1.94 ｜ ATM IV 62.3%，净 delta 敞口 -29k shares
Top ΔOI: P 38 +653 ｜ P 39 +273 ｜ P 37 +112
仓位参考: Max Pain 47 ｜ Put Wall 38（-6.3%）（OI 0.7k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 62.3%｜历史 Rank 40%（近端代理）｜IV/RV 1.42×（近似）｜净 delta 敞口 负 29,282 股

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 61.4% vs 10-23 52.6%（差 +8.7pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=51 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=51）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/MP_morning.json