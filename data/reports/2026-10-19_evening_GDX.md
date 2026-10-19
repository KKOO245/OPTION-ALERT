# 期权晚报 2026-10-19（快照 16:40 ET）

📊 市场环境

SPY $766.48 ｜ QQQ $718.36
VIX 18.44 ↓7.8%（5D +21.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 23.1（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 83P ΔOI +581（距现价 -4.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-23 93C ΔOI +18,371 占该期限总 OI 14.8%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
GDX: 今开 87.14 → 收盘 86.47（-0.8%） ｜ 今日高 87.73 ｜ 低 86.43 ｜ 昨收 87.71 → 收盘 86.47（-1.4%）
Target 等待验证: 5D_rv_expansion >= 1.25（5D） — PENDING（评估日 ≈ 2026-10-26，窗口结束前不做对错判定）

Options: P/C成交量 1.01 | OI比 0.43 | ATM IV 69.9% | Skew 35.4pp | Term 0.58 | ExpMove ±2.3%（近端） | Rank 98%
量化视角： IV 历史高位（Rank 98%，期权偏贵）｜期限结构倒挂（Term 0.58，近月 IV 高于远月）｜保护溢价显著（Skew 35.4pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.43）——观察点，非方向信号
   ⇒ Put/Call Volume: 1.01×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.43×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-21（2D）±2.3% ｜ 10-23（4D）±3.6% ｜ 10-26（7D）±4.5% ｜ 10-28（9D）±5.3%
   ⇒ IV–VIX Spread: +51.4pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 23,215,803 | GEX Change vs 上次快照 -3,534,228 | Flip: Primary Flip: 84.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 571 / LOW 137 / INVALID 494
结构观察区: Primary Flip 84.87（全链重定价，覆盖 97%）
最近结构参考: Flip 85（现价高于该位 1.9%）
量化视角： 正 Gamma（2322万，无历史分位）｜正 Gamma 减弱（353万）｜现价位于 Flip 上方 1.88%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 87（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 93.0C — Vol 37 | 最新价 $0.14 | OI 259→18630 (ΔOI +18371张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增18371张（+7093.1% vs前日OI），连续性待观察（方向未知）
10-23 90.0C — Vol 582 | 最新价 $0.43 | OI 1249→11421 (ΔOI +10172张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10172张（+814.4% vs前日OI），连续性待观察（方向未知）
10-23 92.0C — Vol 97 | 最新价 $0.18 | OI 915→10979 (ΔOI +10064张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10064张（+1099.9% vs前日OI），连续性待观察（方向未知）
10-23 89.0C — Vol 115 | 最新价 $0.76 | OI 312→10198 (ΔOI +9886张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9886张（+3168.6% vs前日OI），连续性待观察（方向未知）
10-23 90.5C — Vol 20 | 最新价 $0.40 | OI 684→8285 (ΔOI +7601张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7601张（+1111.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 56,094 张（Put 0 / Call 56,094），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-21  C +0.3k / P +1.4k ｜ Activity HIGH ｜ 2D
10-23  C +58.4k / P +7.6k ｜ Activity HIGH ｜ 4D
10-26  C +76 / P +0.2k ｜ Activity MEDIUM △ ｜ 7D
10-28  C -11 / P +1.3k ｜ Activity HIGH ｜ 9D

📆 10-21 Forward Structure
存量OI: C 3.5k / P 5.4k，今日变化ΔOI: C +0.3k / P +1.4k，平值价格ATM: C $1.30 / P $0.70 ｜ ATM IV 38.3%，净 delta 敞口 -33k shares
Top ΔOI: P 83 +581 ｜ P 85 +298
仓位参考: Max Pain 87 ｜ Put Wall 83（-4.0%，弱）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 38.3%｜历史 Rank 98%（近端代理）｜IV/RV 1.05×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 33,045 股

📆 10-23 Forward Structure
存量OI: C 91.9k / P 32.0k，今日变化ΔOI: C +58.4k / P +7.6k，平值价格ATM: C $1.67 / P $1.44 ｜ ATM IV 42.5%，净 delta 敞口 721k shares
Top ΔOI: C 93 +18,371 ｜ C 90 +10,172 ｜ C 92 +10,064
仓位参考: Max Pain 86 ｜ Call Wall 90（+4.1%，弱）（OI 11.4k） ｜ Put Wall 85（-1.7%，弱）（OI 5.3k）
量化解读： 存量 Call 重｜ATM IV 42.5%｜历史 Rank 98%（近端代理）｜IV/RV 1.17×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 721,311 股

10-26（MEDIUM △）Top ΔOI: 84P +52 ｜ 87C +52
10-26（MEDIUM △）仓位参考: Max Pain 86 ｜ Call Wall 92（+6.4%，弱）（OI 0.4k）

📆 10-28 Forward Structure
存量OI: C 97 / P 1.8k，今日变化ΔOI: C -11 / P +1.3k，平值价格ATM: C $2.76 / P $1.86 ｜ ATM IV 40.9%，净 delta 敞口 -38k shares
Top ΔOI: P 84 +996 ｜ P 82 +225 ｜ P 81 +62
仓位参考: Max Pain 87 ｜ Call Wall 84（-2.9%）（OI 26） ｜ Put Wall 84（-2.9%）（OI 1.0k）
量化解读： 存量 Put 重｜ATM IV 40.9%｜历史 Rank 98%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 负 37,952 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/GDX_evening.json