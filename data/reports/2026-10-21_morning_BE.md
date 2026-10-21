# 期权晨报 2026-10-21（快照 10:20 ET）

📊 市场环境

SPY $773.28 ｜ QQQ $725.20
VIX 17.20 ↓0.6%（5D +2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 31.4（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-21

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 227C ΔOI +619（距现价 -3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 222.65 → 今开 235.36（+5.7%） | 较昨收变动（含盘初走势） ｜ 今日高 239.00 ｜ 低 229.30

Options: P/C成交量 0.82 | OI比 0.85 | ATM IV 157.5% | Skew 5.8pp | Term 0.54 | ExpMove ±10.3%（近端） | Rank 93%
量化视角： IV 历史高位（Rank 93%，期权偏贵）｜期限结构倒挂（Term 0.54，近月 IV 高于远月）｜保护溢价中性（Skew 5.8pp）｜存量 Call 偏重（OI比 0.85）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（2D）±10.3% ｜ 10-30（9D）±13.7% ｜ 11-06（16D）±15.9% ｜ 11-13（23D）±17.8%
   ⇒ IV–VIX Spread: +140.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -3,210,355 | GEX Change vs 上次快照 4,511,381 | Flip: Primary Flip: 244.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 659 / LOW 61 / INVALID 136
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 244.64（全链重定价，覆盖 100%）
最近结构参考: Flip 245（现价低于该位 3.6%）
量化视角： 负 Gamma（321万，无历史分位）｜负 Gamma 缓解（+451万）｜现价位于 Flip 下方 3.65%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 240（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 245（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 225.0C — Vol 1,095 | 最新价 $18.40 | OI 89→1020 (ΔOI +931张) | ΔOI/Volume 85.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增931张（+1046.1% vs前日OI），连续性待观察（方向未知）
11-20 195.0P — Vol 885 | 最新价 $9.85 | OI 2729→3494 (ΔOI +765张) | ΔOI/Volume 86.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增765张（+28.0% vs前日OI），连续性待观察（方向未知）
10-23 227.5C — Vol 1,080 | 最新价 $9.70 | OI 329→948 (ΔOI +619张) | ΔOI/Volume 57.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增619张（+188.2% vs前日OI），连续性待观察（方向未知）
10-23 200.0P — Vol 1,803 | 最新价 $3.50 | OI 2557→3142 (ΔOI +585张) | ΔOI/Volume 32.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增585张（+22.9% vs前日OI），连续性待观察（方向未知）
11-13 230.0P — Vol 516 | 最新价 $24.75 | OI 2213→2671 (ΔOI +458张) | ΔOI/Volume 88.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增458张（+20.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,358 张（Put 1,808 / Call 1,550），跨 4 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +5.0k / P +3.7k ｜ Activity HIGH ｜ 2D
10-30  C +1.3k / P +1.3k ｜ Activity MEDIUM △ ｜ 9D
11-06  C +1.1k / P -0.3k ｜ Activity MEDIUM △ ｜ 16D
11-13  C +0.4k / P +0.8k ｜ Activity MEDIUM △ ｜ 23D

📆 10-23 Forward Structure
存量OI: C 52.6k / P 44.5k，今日变化ΔOI: C +5.0k / P +3.7k，平值价格ATM: C $12.02 / P $12.16 ｜ ATM IV 157.5%，净 delta 敞口 190k shares
Top ΔOI: C 227 +619 ｜ P 200 +585 ｜ P 222 +424
仓位参考: Max Pain 240 ｜ Call Wall 250（+6.1%，弱）（OI 1.9k） ｜ Put Wall 230（-2.4%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 157.5%｜历史 Rank 93%（近端代理）｜IV/RV 2.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 190,498 股

10-30（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 240（+1.8%，弱）（OI 1.4k） ｜ Put Wall 240（+1.8%，弱）（OI 1.6k）

11-06（MEDIUM △）Top ΔOI: 235P -932 ｜ 225C +931
11-06（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 225（-4.5%）（OI 1.0k） ｜ Put Wall 235（-0.3%，弱）（OI 1.8k）

11-13（MEDIUM △）Top ΔOI: 230P +458 ｜ 200P +270
11-13（MEDIUM △）仓位参考: Max Pain 250 ｜ Call Wall 240（+1.8%，弱）（OI 0.6k） ｜ Put Wall 230（-2.4%）（OI 2.7k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-21/BE_morning.json