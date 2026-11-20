# 期权晨报 2026-11-19（快照 10:20 ET）

📊 市场环境

SPY $nan ｜ QQQ $nan
VIX 22.66 ↓7.7%（5D +21.2%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 18.7（extreme fear）
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
🟡 **近现价集中开仓**: 11-27 167C ΔOI +5,108（距现价 +0.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 156.67 → 今开 160.94（+2.7%） | 较昨收变动（含盘初走势） ｜ 今日高 167.13 ｜ 低 160.50

Options: P/C成交量 0.42 | OI比 0.82 | ATM IV 76.0% | Skew 6.9pp | Term 0.70 | ExpMove ±3.6%（近端） | Rank 87%
量化视角： IV 历史高位（Rank 87%，期权偏贵）｜期限结构倒挂（Term 0.70，近月 IV 高于远月）｜保护溢价显著（Skew 6.9pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.42×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 11-20（1D）±3.6% ｜ 11-27（8D）±6.4% ｜ 12-04（15D）±8.9% ｜ 12-11（22D）±14.3%
   ⇒ IV–VIX Spread: +53.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 25,058,746 | GEX Change vs 上次快照 47,453,050 | Flip: Primary Flip: 161.41（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 332 / LOW 189 / INVALID 297
结构观察区: Primary Flip 161.41（全链重定价，覆盖 98%）
Call Wall 180（弱结构｜现价低于该位 7.6%）
最近结构参考: Flip 161（现价高于该位 3.1%）
量化视角： 正 Gamma（2506万，无历史分位）｜由负转正（+4745万）｜现价位于 Flip 上方 3.07%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 165（MaxPain，仅结算参考）；上方 180（Call Wall，弱结构）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-27 167.5C — Vol 7,251 | 最新价 $1.75 | OI 1716→6824 (ΔOI +5108张) | ΔOI/Volume 70.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5108张（+297.7% vs前日OI），连续性待观察（方向未知）
11-27 162.5C — Vol 4,489 | 最新价 $3.20 | OI 119→4401 (ΔOI +4282张) | ΔOI/Volume 95.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4282张（+3598.3% vs前日OI），连续性待观察（方向未知）
11-27 170.0C — Vol 4,762 | 最新价 $1.27 | OI 774→4221 (ΔOI +3447张) | ΔOI/Volume 72.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3447张（+445.4% vs前日OI），连续性待观察（方向未知）
11-27 140.0P — Vol 2,565 | 最新价 $1.05 | OI 1563→3525 (ΔOI +1962张) | ΔOI/Volume 76.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1962张（+125.5% vs前日OI），连续性待观察（方向未知）
11-27 165.0C — Vol 2,108 | 最新价 $2.41 | OI 803→1878 (ΔOI +1075张) | ΔOI/Volume 51.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1075张（+133.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 15,874 张（Put 1,962 / Call 13,912），跨 1 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-20  C -7.7k / P -12.9k ｜ Activity HIGH ｜ 1D
11-27  C +15.8k / P +1.3k ｜ Activity HIGH ｜ 8D
12-04  C +1.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 15D
12-11  C +0.2k / P +95 ｜ Activity MEDIUM △ ｜ 22D

📆 11-20 Forward Structure
存量OI: C 235.4k / P 192.0k，今日变化ΔOI: C -7.7k / P -12.9k，平值价格ATM: C $2.62 / P $3.42 ｜ ATM IV 76.0%，净 delta 敞口 1.6M shares
Top ΔOI: C 180 -7,486 ｜ P 185 -7,476 ｜ P 190 -3,803
仓位参考: Max Pain 165 ｜ Call Wall 180（+8.2%，弱）（OI 17.8k） ｜ Put Wall 180（+8.2%，弱）（OI 9.2k）
量化解读： 存量 Call 重｜ATM IV 76.0%｜历史 Rank 87%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,642,209 股

📆 11-27 Forward Structure
存量OI: C 43.8k / P 39.0k，今日变化ΔOI: C +15.8k / P +1.3k，平值价格ATM: C $5.00 / P $5.70 ｜ ATM IV 54.0%，净 delta 敞口 935k shares
Top ΔOI: C 167 +5,108 ｜ C 162 +4,282 ｜ C 170 +3,447
仓位参考: Max Pain 160 ｜ Call Wall 167.5（+0.7%）（OI 6.8k） ｜ Put Wall 150（-9.8%，弱）（OI 4.6k）
量化解读： 存量两侧均衡｜ATM IV 54.0%｜历史 Rank 87%（近端代理）｜IV/RV 1.01×（近似）｜净 delta 敞口 正 935,460 股

12-04（MEDIUM △）Top ΔOI: 160C +276 ｜ 170C +245
12-04（MEDIUM △）仓位参考: Max Pain 168 ｜ Call Wall 180（+8.2%，弱）（OI 1.0k） ｜ Put Wall 155（-6.8%）（OI 2.8k）

12-11（MEDIUM △）Top ΔOI: 175C +60
12-11（MEDIUM △）仓位参考: Max Pain 170 ｜ Call Wall 180（+8.2%，弱）（OI 0.9k） ｜ Put Wall 150（-9.8%，弱）（OI 1.2k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-19/PLTR_morning.json