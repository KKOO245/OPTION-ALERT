# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $735.18 ｜ QQQ $663.48
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 28.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 本周剩余时间暂无【高】重要性美国数据公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-20 110C ΔOI +2,918（距现价 -1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NBIS  昨收 106.96 → 今开 111.73（+4.5%） | 较昨收变动（含盘初走势） ｜ 今日高 115.18 ｜ 低 106.13

Options: P/C成交量 0.29 | OI比 0.46 | ATM IV 148.7% | Skew 6.8pp | Term 0.70 | ExpMove ±6.9%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 6.8pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-20（1D）±6.9% ｜ 11-27（8D）±12.6% ｜ 12-04（15D）±17.6% ｜ 12-11（22D）±20.6%
   ⇒ IV–VIX Spread: +126.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,962,328 | GEX Change vs 上次快照 8,307,145 | Flip: Primary Flip: 107.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 583 / LOW 99 / INVALID 140
结构观察区: Primary Flip 107.80（全链重定价，覆盖 100%）
最近结构参考: Flip 108（现价高于该位 3.1%）
量化视角： 正 Gamma（496万，无历史分位）｜由负转正（+831万）｜现价位于 Flip 上方 3.10%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 120（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 108（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 130.0C — Vol 15,695 | 最新价 $0.25 | OI 5538→17223 (ΔOI +11685张) | ΔOI/Volume 74.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11685张（+211.0% vs前日OI），连续性待观察（方向未知）
11-20 110.0C — Vol 9,952 | 最新价 $3.54 | OI 4478→7396 (ΔOI +2918张) | ΔOI/Volume 29.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2918张（+65.2% vs前日OI），连续性待观察（方向未知）
11-20 105.0C — Vol 3,945 | 最新价 $6.00 | OI 653→2238 (ΔOI +1585张) | ΔOI/Volume 40.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1585张（+242.7% vs前日OI），连续性待观察（方向未知）
11-27 105.0C — Vol 1,810 | 最新价 $8.87 | OI 147→1682 (ΔOI +1535张) | ΔOI/Volume 84.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1535张（+1044.2% vs前日OI），连续性待观察（方向未知）
12-18 70.0P — Vol 2,337 | 最新价 $2.00 | OI 2539→3725 (ΔOI +1186张) | ΔOI/Volume 50.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1186张（+46.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 18,909 张（Put 1,186 / Call 17,723），跨 3 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C +17.4k / P -10.5k ｜ Activity HIGH ｜ 1D
11-27  C +7.0k / P -0.3k ｜ Activity MEDIUM △ ｜ 8D
12-04  C +1.4k / P +0.3k ｜ Activity HIGH ｜ 15D
12-11  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 22D

📆 11-20 Forward Structure
存量OI: C 217.8k / P 99.9k，今日变化ΔOI: C +17.4k / P -10.5k，平值价格ATM: C $4.00 / P $3.65 ｜ ATM IV 148.7%，净 delta 敞口 1.5M shares
Top ΔOI: C 130 +11,685 ｜ C 110 +2,918 ｜ P 150 -1,923
仓位参考: Max Pain 120 ｜ Call Wall 120（+8.0%，弱）（OI 8.7k） ｜ Put Wall 115（+3.5%，弱）（OI 9.4k）
量化解读： 存量 Call 重｜ATM IV 148.7%｜历史 Rank 90%（近端代理）｜IV/RV 1.03×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,493,259 股

11-27（MEDIUM △）Top ΔOI: 105C +1,535 ｜ 110C +974
11-27（MEDIUM △）仓位参考: Max Pain 115 ｜ Call Wall 110（-1.0%，弱）（OI 2.5k） ｜ Put Wall 110（-1.0%，弱）（OI 0.9k）

📆 12-04 Forward Structure
存量OI: C 16.0k / P 8.5k，今日变化ΔOI: C +1.4k / P +0.3k，平值价格ATM: C $9.60 / P $10.00 ｜ ATM IV 107.3%，净 delta 敞口 47k shares
Top ΔOI: C 130 +317
仓位参考: Max Pain 125 ｜ Call Wall 120（+8.0%，弱）（OI 0.8k） ｜ Put Wall 115（+3.5%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 107.3%｜历史 Rank 90%（近端代理）｜IV/RV 0.75×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 46,620 股

12-11（MEDIUM △）Top ΔOI: 85P +345 ｜ 135C +197
12-11（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 120（+8.0%，弱）（OI 0.5k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/NBIS_morning.json