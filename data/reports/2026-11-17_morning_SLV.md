# 期权晨报 2026-11-17（快照 10:20 ET）

📊 市场环境

SPY $734.92 ｜ QQQ $656.95
VIX 22.73 ↓0.8%（5D +16.8%） ｜ Vol Regime: ELEVATED
CNN 恐惧贪婪 25.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-17

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-17 08:30　【高】零售销售 MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.8　✅ 今日已公布
- 周三 11-18 08:30　【高】新屋开工　预测 1.245 ｜ 实际 待公布 ｜ 前值 1.221
- 周三 11-18 08:30　【高】建筑许可 Prel　预测 1.377 ｜ 实际 待公布 ｜ 前值 1.4

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 11-18 43C ΔOI +2,585（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 11-23 45C ΔOI +3,917 占该期限总 OI 23.4%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## SLV

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SLV  昨收 42.39 → 今开 42.88（+1.2%） | 较昨收变动（含盘初走势） ｜ 今日高 43.25 ｜ 低 42.87

Options: P/C成交量 0.38 | OI比 0.46 | ATM IV 48.6% | Skew 3.6pp | Term 0.88 | ExpMove ±2.3%（近端） | Rank 80%
量化视角： IV 历史高位（Rank 80%，期权偏贵）｜期限结构倒挂（Term 0.88，近月 IV 高于远月）｜保护溢价中性（Skew 3.6pp）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.38×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-18（1D）±2.3% ｜ 11-20（3D）±3.7% ｜ 11-23（6D）±4.4% ｜ 11-25（8D）±5.3%
   ⇒ IV–VIX Spread: +25.9pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,833,844 | GEX Change vs 上次快照 50,037,547 | Flip: Primary Flip: 42.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 668 / LOW 148 / INVALID 386
结构观察区: Primary Flip 42.70（全链重定价，覆盖 97%）
Put Wall 40（弱结构｜现价高于该位 7.8%）
最近结构参考: Flip 43（现价高于该位 1.0%）
量化视角： 正 Gamma（1283万，无历史分位）｜由负转正（+5004万）｜现价位于 Flip 上方 0.96%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 40（Put Wall，弱结构）；上方 44（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 43（全链重定价，覆盖 97%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 44.5C — Vol 14,682 | 最新价 $0.25 | OI 489→13940 (ΔOI +13451张) | ΔOI/Volume 91.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增13451张（+2750.7% vs前日OI），连续性待观察（方向未知）
12-18 52.0C — Vol 12,857 | 最新价 $0.22 | OI 50266→62437 (ΔOI +12171张) | ΔOI/Volume 94.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12171张（+24.2% vs前日OI），连续性待观察（方向未知）
11-23 45.5C — Vol 4,516 | 最新价 $0.17 | OI 86→4003 (ΔOI +3917张) | ΔOI/Volume 86.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3917张（+4554.6% vs前日OI），连续性待观察（方向未知）
11-20 45.0C — Vol 6,210 | 最新价 $0.17 | OI 2715→6494 (ΔOI +3779张) | ΔOI/Volume 60.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3779张（+139.2% vs前日OI），连续性待观察（方向未知）
12-18 28.0P — Vol 3,555 | 最新价 $0.05 | OI 30135→33395 (ΔOI +3260张) | ΔOI/Volume 91.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3260张（+10.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,578 张（Put 3,260 / Call 33,318），跨 3 个期限｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-18  C +11.4k / P +3.4k ｜ Activity HIGH ｜ 1D
11-20  C +21.6k / P +0.7k ｜ Activity HIGH ｜ 3D
11-23  C +5.8k / P +2.3k ｜ Activity HIGH ｜ 6D
11-25  C +1.2k / P +0.4k ｜ Activity HIGH ｜ 8D

📆 11-18 Forward Structure
存量OI: C 33.5k / P 15.4k，今日变化ΔOI: C +11.4k / P +3.4k，平值价格ATM: C $0.55 / P $0.45 ｜ ATM IV 48.6%，净 delta 敞口 365k shares
Top ΔOI: C 43 +2,585 ｜ C 44 +2,134 ｜ C 43 +1,465
仓位参考: Max Pain 44 ｜ Call Wall 43（-0.3%，弱）（OI 2.6k） ｜ Put Wall 40（-7.2%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 48.6%｜历史 Rank 80%（近端代理）｜IV/RV 1.20×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 365,466 股

📆 11-20 Forward Structure
存量OI: C 592.7k / P 157.0k，今日变化ΔOI: C +21.6k / P +0.7k，平值价格ATM: C $0.88 / P $0.73 ｜ ATM IV 49.5%，净 delta 敞口 991k shares
Top ΔOI: C 44 +13,451 ｜ C 45 +3,779
仓位参考: Max Pain 48 ｜ Put Wall 45（+4.4%，弱）（OI 14.4k）
量化解读： 存量 Call 重｜ATM IV 49.5%｜历史 Rank 80%（近端代理）｜IV/RV 1.22×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 991,015 股

📆 11-23 Forward Structure
存量OI: C 13.1k / P 3.6k，今日变化ΔOI: C +5.8k / P +2.3k，平值价格ATM: C $0.99 / P $0.90 ｜ ATM IV 42.1%，净 delta 敞口 78k shares
Top ΔOI: C 45 +3,917 ｜ P 39 +656 ｜ C 46 +352
仓位参考: Max Pain 43 ｜ Call Wall 45.5（+5.5%，弱）（OI 4.0k） ｜ Put Wall 39（-9.5%，弱）（OI 0.8k）
量化解读： 存量 Call 重｜ATM IV 42.1%｜历史 Rank 80%（近端代理）｜IV/RV 1.04×（近似）｜净 delta 敞口 正 78,382 股

📆 11-25 Forward Structure
存量OI: C 2.5k / P 1.4k，今日变化ΔOI: C +1.2k / P +0.4k，平值价格ATM: C $1.23 / P $1.06 ｜ ATM IV 43.9%，净 delta 敞口 25k shares
Top ΔOI: C 46 +417 ｜ P 42 +204 ｜ C 43 +145
仓位参考: Max Pain 44 ｜ Call Wall 46（+6.7%）（OI 0.5k） ｜ Put Wall 42（-2.6%，弱）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 43.9%｜历史 Rank 80%（近端代理）｜IV/RV 1.08×（近似）｜净 delta 敞口 正 25,111 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol ELEVATED（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-17/SLV_morning.json