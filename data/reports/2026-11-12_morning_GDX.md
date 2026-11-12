# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $757.88 ｜ QQQ $688.17
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 39.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 11-13 ATM IV 52.7% vs 11-16 42.0%（差 +10.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 83P ΔOI +1,953（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
GDX  昨收 85.21 → 今开 82.52（-3.2%） | 较昨收变动（含盘初走势） ｜ 今日高 83.51 ｜ 低 81.71

Options: P/C成交量 0.04 | OI比 0.46 | ATM IV 52.7% | Skew -0.7pp | Term 0.83 | ExpMove ±2.5%（近端） | Rank 85%
量化视角： IV 历史高位（Rank 85%，期权偏贵）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.46）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.04×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.46×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±2.5% ｜ 11-16（4D）±7.7% ｜ 11-18（6D）±12.0% ｜ 11-20（8D）±5.1%
   ⇒ IV–VIX Spread: +34.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -45,018,351 | GEX Change vs 上次快照 -50,461,730 | Flip: Primary Flip: 84.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 90%（带内） ｜ IV 有效性: VALID 614 / LOW 200 / INVALID 444
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 84.53（全链重定价，覆盖 90%）
最近结构参考: Flip 85（现价低于该位 2.6%）
量化视角： 负 Gamma（4502万，无历史分位）｜由正转负（5046万）｜现价位于 Flip 下方 2.60%｜⚠️ 重点观察：负 Gamma 且日内加深——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 85（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 85（全链重定价，覆盖 90%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 83.5P — Vol 2,010 | 最新价 $1.54 | OI 188→2141 (ΔOI +1953张) | ΔOI/Volume 97.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1953张（+1038.8% vs前日OI），连续性待观察（方向未知）
12-11 85.5P — Vol 1,112 | 最新价 $4.10 | OI 2→1078 (ΔOI +1076张) | ΔOI/Volume 96.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1076张（+53800.0% vs前日OI），连续性待观察（方向未知）
11-20 80.0P — Vol 1,500 | 最新价 $0.59 | OI 23850→24833 (ΔOI +983张) | ΔOI/Volume 65.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增983张（+4.1% vs前日OI），连续性待观察（方向未知）
11-13 83.5P — Vol 652 | 最新价 $0.54 | OI 136→577 (ΔOI +441张) | ΔOI/Volume 67.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增441张（+324.3% vs前日OI），连续性待观察（方向未知）
11-20 82.0P — Vol 1,688 | 最新价 $0.99 | OI 3506→3899 (ΔOI +393张) | ΔOI/Volume 23.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增393张（+11.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,846 张（Put 4,846 / Call 0），跨 3 个期限｜近端保护（5 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C -0.3k / P +0.8k ｜ Activity HIGH ｜ 1D
11-16  C +0.6k / P +0.6k ｜ Activity HIGH ｜ 4D
11-18  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 6D
11-20  C -1.1k / P +2.3k ｜ Activity HIGH ｜ 8D

📆 11-13 Forward Structure
存量OI: C 83.0k / P 37.9k，今日变化ΔOI: C -0.3k / P +0.8k，平值价格ATM: C $1.07 / P $1.01 ｜ ATM IV 52.7%，净 delta 敞口 -41k shares
Top ΔOI: P 83 +441 ｜ C 88 -163 ｜ P 79 +158
仓位参考: Max Pain 85 ｜ Put Wall 79（-4.1%，弱）（OI 6.8k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 52.7%｜历史 Rank 85%（近端代理）｜IV/RV 0.95×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 40,797 股

📆 11-16 Forward Structure
存量OI: C 2.5k / P 2.0k，今日变化ΔOI: C +0.6k / P +0.6k，平值价格ATM: C $5.15 / P $1.16 ｜ ATM IV 42.0%，净 delta 敞口 -17k shares
Top ΔOI: P 79 +305 ｜ C 87 +217 ｜ C 89 +215
仓位参考: Max Pain 86 ｜ Call Wall 87（+5.7%，弱）（OI 0.4k） ｜ Put Wall 84（+2.0%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜ATM IV 42.0%｜历史 Rank 85%（近端代理）｜IV/RV 0.76×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 16,686 股

11-18（MEDIUM △）Top ΔOI: 86C +106 ｜ 81P +43
11-18（MEDIUM △）仓位参考: Max Pain 85 ｜ Call Wall 86（+4.5%，弱）（OI 0.1k） ｜ Put Wall 84（+2.0%）（OI 0.2k）

📆 11-20 Forward Structure
存量OI: C 101.3k / P 170.8k，今日变化ΔOI: C -1.1k / P +2.3k，平值价格ATM: C $2.30 / P $1.87 ｜ ATM IV 45.0%，净 delta 敞口 -110k shares
Top ΔOI: P 83 +1,953 ｜ P 80 +983 ｜ P 87 -589
仓位参考: Max Pain 87 ｜ Call Wall 84（+2.0%，弱）（OI 8.5k） ｜ Put Wall 80（-2.8%，弱）（OI 24.8k）
量化解读： 存量 Put 重｜ATM IV 45.0%｜历史 Rank 85%（近端代理）｜IV/RV 0.81×（近似）｜净 delta 敞口 负 109,820 股

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 52.7% vs 11-16 42.0%（差 +10.7pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 2 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=94 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=94）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/GDX_morning.json