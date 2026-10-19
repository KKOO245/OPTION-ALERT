# 期权晨报 2026-10-19（快照 10:20 ET）

📊 市场环境

SPY $766.65 ｜ QQQ $721.15
VIX 18.46 ↓7.7%（5D +21.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 22.8（extreme fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-19

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-20 08:30　【高】建筑许可 Prel　预测 1.4 ｜ 实际 待公布 ｜ 前值 1.403
- 周二 10-20 08:30　【高】新屋开工　预测 1.31 ｜ 实际 待公布 ｜ 前值 1.275

🔍 重点速览
🟡 **近现价集中开仓**: 10-23 146C ΔOI +3,006（距现价 +0.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 10-30 130P ΔOI +15,383 占该期限总 OI 29.9%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## XBI

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
XBI  昨收 144.32 → 今开 145.88（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 148.37 ｜ 低 145.30

Options: P/C成交量 0.36 | OI比 1.05 | ATM IV 42.5% | Skew 3.1pp | Term 0.81 | ExpMove ±2.6%（近端） | Rank 90%
量化视角： IV 历史高位（Rank 90%，期权偏贵）｜期限结构倒挂（Term 0.81，近月 IV 高于远月）｜保护溢价中性（Skew 3.1pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.36×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.05×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-23（4D）±2.6% ｜ 10-30（11D）±5.1% ｜ 11-06（18D）±9.6% ｜ 11-13（25D）±12.7%
   ⇒ IV–VIX Spread: +24.0pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -28,627,118 | GEX Change vs 上次快照 -5,123,875 | Flip: Primary Flip: 163.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 330 / LOW 88 / INVALID 348
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 163.53（全链重定价，覆盖 98%）
Put Wall 140（弱结构｜现价高于该位 4.1%） | Call Wall 155（弱结构｜现价低于该位 5.9%）
最近结构参考: Put Wall 140（现价高于该位 4.1%）
量化视角： 负 Gamma（2863万，无历史分位）｜负 Gamma 加深（512万）｜现价位于 Flip 下方 10.85%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 140（Put Wall，弱结构）；上方 146（MaxPain，仅结算参考） / 155（Call Wall，弱结构）。
• Gamma 区域：切换参考 164（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 130.0P — Vol 15,491 | 最新价 $0.38 | OI 55→15438 (ΔOI +15383张) | ΔOI/Volume 99.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15383张（+27969.1% vs前日OI），连续性待观察（方向未知）
10-30 140.0P — Vol 15,555 | 最新价 $2.10 | OI 6580→18780 (ΔOI +12200张) | ΔOI/Volume 78.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增12200张（+185.4% vs前日OI），连续性待观察（方向未知）
10-23 135.0P — Vol 3,074 | 最新价 $0.29 | OI 131→3157 (ΔOI +3026张) | ΔOI/Volume 98.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3026张（+2309.9% vs前日OI），连续性待观察（方向未知）
10-23 146.0C — Vol 3,009 | 最新价 $1.96 | OI 4→3010 (ΔOI +3006张) | ΔOI/Volume 99.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3006张（+75150.0% vs前日OI），连续性待观察（方向未知）
10-23 148.0C — Vol 3,109 | 最新价 $1.31 | OI 50→3046 (ΔOI +2996张) | ΔOI/Volume 96.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2996张（+5992.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 36,611 张（Put 30,609 / Call 6,002），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $3M，买/卖方向不可观测）｜多期限 Put 集中加仓呈尾部对冲特征（买/卖方向不可观测）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-23  C +13.0k / P +10.0k ｜ Activity HIGH ｜ 4D
10-30  C +0.9k / P +27.9k ｜ Activity HIGH ｜ 11D
11-06  C +0.3k / P -6 ｜ Activity MEDIUM △ ｜ 18D
11-13  C +4 / P +0.6k ｜ Activity HIGH ｜ 25D

📆 10-23 Forward Structure
存量OI: C 17.4k / P 18.3k，今日变化ΔOI: C +13.0k / P +10.0k，平值价格ATM: C $1.96 / P $1.78 ｜ ATM IV 42.5%，净 delta 敞口 349k shares
Top ΔOI: P 135 +3,026 ｜ C 146 +3,006 ｜ C 148 +2,996
仓位参考: Max Pain 146 ｜ Call Wall 150（+2.9%，弱）（OI 3.2k） ｜ Put Wall 144（-1.2%，弱）（OI 3.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 42.5%｜历史 Rank 90%（近端代理）｜IV/RV 1.54×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 349,152 股

📆 10-30 Forward Structure
存量OI: C 5.4k / P 46.1k，今日变化ΔOI: C +0.9k / P +27.9k，平值价格ATM: C $3.56 / P $3.87 ｜ ATM IV 37.9%，净 delta 敞口 -395k shares
Top ΔOI: P 130 +15,383 ｜ P 140 +12,200 ｜ C 155 +828
仓位参考: Max Pain 152 ｜ Call Wall 155（+6.3%）（OI 1.6k） ｜ Put Wall 140（-4.0%，弱）（OI 18.8k）
量化解读： 存量 Put 重｜ATM IV 37.9%｜历史 Rank 90%（近端代理）｜IV/RV 1.37×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 394,810 股

11-06（MEDIUM △）Top ΔOI: 154C +215 ｜ 150C +36
11-06（MEDIUM △）仓位参考: Max Pain 152 ｜ Call Wall 155（+6.3%，弱）（OI 0.3k） ｜ Put Wall 145（-0.5%，弱）（OI 0.4k）

📆 11-13 Forward Structure
存量OI: C 0.3k / P 1.7k，今日变化ΔOI: C +4 / P +0.6k，平值价格ATM: C $13.89 / P $4.57 ｜ ATM IV 35.5%，净 delta 敞口 -19k shares
Top ΔOI: P 140 +501 ｜ P 144 +33 ｜ P 151 +33
仓位参考: Max Pain 155 ｜ Call Wall 148（+1.5%，弱）（OI 15） ｜ Put Wall 140（-4.0%）（OI 0.6k）
量化解读： 存量 Put 重｜ATM IV 35.5%｜历史 Rank 90%（近端代理）｜IV/RV 1.29×（近似）｜净 delta 敞口 负 18,651 股

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup B1 v1 — Core Conditions
Price Regime UP | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 0
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 5D_rv_expansion >= 1.25 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-19/XBI_morning.json