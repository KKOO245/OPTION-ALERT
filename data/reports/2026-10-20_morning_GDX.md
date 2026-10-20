# 期权晨报 2026-10-20（快照 10:20 ET）

📊 市场环境

SPY $769.53 ｜ QQQ $717.63
VIX 18.12 ↓1.7%（5D +18.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-20

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.39 ｜ 实际 1.4 ｜ 前值 1.403　✅ 今日已公布
- 周二 10-20 08:30　【高】新屋开工　预测 1.3 ｜ 实际 1.221 ｜ 前值 1.288　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-21 84P ΔOI +605（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-26 91C ΔOI +1,804 占该期限总 OI 42.7%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 86.47 → 今开 85.62（-1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 87.13 ｜ 低 84.80

Options: P/C成交量 0.96 | OI比 1.50 | ATM IV 40.7% | Skew -0.2pp | Term 1.00 | ExpMove ±1.8%（近端） | Rank 59%
量化视角： IV 中性（Rank 59%）｜期限结构正常（Term 1.00）｜Put 保护异常便宜（Skew -0.2pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.96×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.50×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 10-21（1D）±1.8% ｜ 10-23（3D）±3.2% ｜ 10-26（6D）±3.6% ｜ 10-28（8D）±5.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 18,286,332 | GEX Change vs 上次快照 -3,877,643 | Flip: Primary Flip: 85.06（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 577 / LOW 134 / INVALID 499
结构观察区: Primary Flip 85.06（全链重定价，覆盖 98%）
最近结构参考: Flip 85（现价高于该位 1.2%）
量化视角： 正 Gamma（1829万，无历史分位）｜正 Gamma 减弱（388万）｜现价位于 Flip 上方 1.18%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 87（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 91.0C — Vol 2,595 | 最新价 $0.32 | OI 8451→10893 (ΔOI +2442张) | ΔOI/Volume 94.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2442张（+28.9% vs前日OI），连续性待观察（方向未知）
10-26 91.0C — Vol 1,840 | 最新价 $0.45 | OI 16→1820 (ΔOI +1804张) | ΔOI/Volume 98.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1804张（+11275.0% vs前日OI），连续性待观察（方向未知）
10-21 84.0P — Vol 615 | 最新价 $0.20 | OI 54→659 (ΔOI +605张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增605张（+1120.4% vs前日OI），连续性待观察（方向未知）
10-23 80.0P — Vol 588 | 最新价 $0.08 | OI 3099→3580 (ΔOI +481张) | ΔOI/Volume 81.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增481张（+15.5% vs前日OI），连续性待观察（方向未知）
10-23 150.0C — Vol 450 | 最新价 $0.05 | OI 14→464 (ΔOI +450张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增450张（+3214.3% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,782 张（Put 1,086 / Call 4,696），跨 3 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-21  C +0.8k / P +1.1k ｜ Activity HIGH ｜ 1D
10-23  C +4.2k / P +1.0k ｜ Activity MEDIUM △ ｜ 3D
10-26  C +1.9k / P +84 ｜ Activity HIGH ｜ 6D
10-28  C +0.2k / P +0.1k ｜ Activity HIGH ｜ 8D

📆 10-21 Forward Structure
存量OI: C 4.3k / P 6.5k，今日变化ΔOI: C +0.8k / P +1.1k，平值价格ATM: C $0.90 / P $0.68 ｜ ATM IV 40.7%，净 delta 敞口 -8k shares
Top ΔOI: P 84 +605 ｜ C 89 +242 ｜ P 81 +219
仓位参考: Max Pain 87 ｜ Call Wall 87（+1.1%，弱）（OI 0.4k） ｜ Put Wall 84（-2.4%，弱）（OI 0.7k）
量化解读： 存量 Put 重｜ATM IV 40.7%｜历史 Rank 59%（近端代理）｜IV/RV 1.12×（近似）｜净 delta 敞口 负 8,271 股

10-23（MEDIUM △）Top ΔOI: 91C +2,442 ｜ 80P +481
10-23（MEDIUM △）仓位参考: Max Pain 86 ｜ Call Wall 90（+4.6%，弱）（OI 11.8k） ｜ Put Wall 85（-1.2%，弱）（OI 5.3k）

📆 10-26 Forward Structure
存量OI: C 3.0k / P 1.2k，今日变化ΔOI: C +1.9k / P +84，平值价格ATM: C $1.65 / P $1.45 ｜ ATM IV 36.5%，净 delta 敞口 25k shares
Top ΔOI: C 91 +1,804 ｜ C 90 +44 ｜ P 90 +43
仓位参考: Max Pain 86 ｜ Call Wall 91（+5.7%）（OI 1.8k） ｜ Put Wall 90（+4.6%，弱）（OI 85）
量化解读： 存量 Call 重｜ATM IV 36.5%｜历史 Rank 59%（近端代理）｜IV/RV 1.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 25,042 股

📆 10-28 Forward Structure
存量OI: C 0.3k / P 1.9k，今日变化ΔOI: C +0.2k / P +0.1k，平值价格ATM: C $2.76 / P $1.94 ｜ ATM IV 41.1%，净 delta 敞口 7k shares
Top ΔOI: C 88 +222 ｜ P 79 +39 ｜ P 84 +25
仓位参考: Max Pain 87 ｜ Call Wall 88（+2.2%）（OI 0.2k） ｜ Put Wall 84（-2.4%）（OI 1.1k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 41.1%｜历史 Rank 59%（近端代理）｜IV/RV 1.13×（近似）｜净 delta 敞口 正 7,446 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-20/GDX_morning.json