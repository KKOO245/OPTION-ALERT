# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $775.90 ｜ QQQ $755.92
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 84P ΔOI -2,159（距现价 -2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-21 95C ΔOI +401 占该期限总 OI 58.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 85.46 → 今开 85.41（-0.1%） | 较昨收变动（含盘初走势） ｜ 今日高 86.66 ｜ 低 85.03

Options: P/C成交量 0.22 | OI比 0.31 | ATM IV 47.9% | Skew -2.6pp | Term 0.85 | ExpMove ±2.2%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.85，近月 IV 高于远月）｜Put 保护异常便宜（Skew -2.6pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.31）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.22×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.31×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±2.2% ｜ 10-16（8D）±5.0% ｜ 10-19（11D）±0.0% ｜ 10-21（13D）±5.9%
   ⇒ IV–VIX Spread: +32.5pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 19,697,343 | GEX Change vs 上次快照 31,163,191 | Flip: Primary Flip: 85.57（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 441 / LOW 152 / INVALID 381
结构观察区: Primary Flip 85.57（全链重定价，覆盖 90%）
Put Wall 85（弱结构｜现价高于该位 1.4%） | Call Wall 90（弱结构｜现价低于该位 4.2%）
最近结构参考: Flip 86（现价高于该位 0.8%）
量化视角： 正 Gamma（1970万，无历史分位）｜由负转正（+3116万）｜现价位于 Flip 上方 0.77%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 85（Put Wall，弱结构）；上方 87（MaxPain，仅结算参考） / 90（Call Wall，弱结构）。
• Gamma 区域：切换参考 86（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 89.0C — Vol 2,462 | 最新价 $0.90 | OI 1772→3544 (ΔOI +1772张) | ΔOI/Volume 72.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1772张（+100.0% vs前日OI），连续性待观察（方向未知）
10-16 90.0C — Vol 3,975 | 最新价 $0.68 | OI 9009→9951 (ΔOI +942张) | ΔOI/Volume 23.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增942张（+10.5% vs前日OI），连续性待观察（方向未知）
10-16 94.0C — Vol 2,934 | 最新价 $0.18 | OI 1888→2792 (ΔOI +904张) | ΔOI/Volume 30.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增904张（+47.9% vs前日OI），连续性待观察（方向未知）
10-16 86.0C — Vol 975 | 最新价 $1.90 | OI 395→1200 (ΔOI +805张) | ΔOI/Volume 82.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增805张（+203.8% vs前日OI），连续性待观察（方向未知）
10-16 88.0C — Vol 1,286 | 最新价 $1.18 | OI 1853→2606 (ΔOI +753张) | ΔOI/Volume 58.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增753张（+40.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,176 张（Put 0 / Call 5,176），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.7k / P -1.3k ｜ Activity MEDIUM △ ｜ 1D
10-16  C +5.7k / P -6.3k ｜ Activity MEDIUM △ ｜ 8D
10-19  C +89 / P +18 ｜ Activity MEDIUM △ ｜ 11D
10-21  C +0.6k / P +93 ｜ Activity HIGH ｜ 13D

📆 10-09 Forward Structure
存量OI: C 97.4k / P 30.6k，今日变化ΔOI: C +0.7k / P -1.3k，平值价格ATM: C $1.14 / P $0.77 ｜ ATM IV 47.9%，净 delta 敞口 232k shares
Top ΔOI: P 94 -1,280 ｜ C 92 -613 ｜ C 88 +374
仓位参考: Max Pain 87 ｜ Call Wall 88（+2.1%，弱）（OI 16.7k） ｜ Put Wall 82（-4.9%，弱）（OI 6.8k）
量化解读： 存量 Call 重｜ATM IV 47.9%｜历史 Rank 77%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 231,864 股

10-16（MEDIUM △）Top ΔOI: 84P -2,159 ｜ 89C +1,772
10-16（MEDIUM △）仓位参考: Max Pain 90 ｜ Call Wall 90（+4.4%，弱）（OI 10.0k） ｜ Put Wall 90（+4.4%，弱）（OI 10.4k）

10-19（MEDIUM △）Top ΔOI: 91C +22 ｜ 90C +12
10-19（MEDIUM △）仓位参考: Max Pain 88 ｜ Call Wall 91（+5.5%，弱）（OI 26） ｜ Put Wall 90（+4.4%，弱）（OI 23）

📆 10-21 Forward Structure
存量OI: C 0.6k / P 0.1k，今日变化ΔOI: C +0.6k / P +93，平值价格ATM: C $2.58 / P $2.50 ｜ ATM IV 38.3%，净 delta 敞口 7k shares
仓位参考: Max Pain 85 ｜ Put Wall 85（-1.4%，弱）（OI 14）
量化解读： 存量 Call 重｜ATM IV 38.3%｜历史 Rank 77%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 正 6,949 股

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 47.9% vs 10-16 39.7%（差 +8.2pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime DOWN | Location near_put_concentration | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 1 ｜ ✗ 2 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/GDX_morning.json