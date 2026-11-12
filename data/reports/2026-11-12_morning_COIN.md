# 期权晨报 2026-11-12（快照 10:20 ET）

📊 市场环境

SPY $756.94 ｜ QQQ $685.55
VIX 18.45 ↑5.5%（5D -34.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-12

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 3.75 ｜ 前值 3.97　✅ 今日已公布
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 87.8% vs 11-20 72.9%（差 +14.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 136.27 → 今开 129.97（-4.6%） | 较昨收变动（含盘初走势） ｜ 今日高 132.05 ｜ 低 129.62

Options: P/C成交量 0.45 | OI比 0.48 | ATM IV 87.8% | Skew 0.8pp | Term 0.79 | ExpMove ±4.1%（近端） | Rank 77%
量化视角： IV 历史高位（Rank 77%，期权偏贵）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价薄（Skew 0.8pp）｜存量 Call 偏重（OI比 0.48）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.48×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（1D）±4.1% ｜ 11-20（8D）±8.8% ｜ 11-27（15D）±8.9% ｜ 12-04（22D）±13.1%
   ⇒ IV–VIX Spread: +69.3pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 185,575 | GEX Change vs 上次快照 -20,227,014 | Flip: Primary Flip: 130.88（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 463 / LOW 227 / INVALID 302
结构观察区: Primary Flip 130.88（全链重定价，覆盖 99%）
Call Wall 140（弱结构｜现价低于该位 6.5%）
最近结构参考: Flip 131（现价高于该位 0.0%）
量化视角： 正 Gamma（19万，无历史分位）｜正 Gamma 减弱（2023万）｜现价位于 Flip 上方 0.04%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 137（MaxPain，仅结算参考） / 140（Call Wall，弱结构）。
• Gamma 区域：切换参考 131（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 150.0C — Vol 5,843 | 最新价 $1.74 | OI 2560→5035 (ΔOI +2475张) | ΔOI/Volume 42.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2475张（+96.7% vs前日OI），连续性待观察（方向未知）
11-20 70.0P — Vol 1,310 | 最新价 $0.06 | OI 44→1276 (ΔOI +1232张) | ΔOI/Volume 94.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1232张（+2800.0% vs前日OI），连续性待观察（方向未知）
11-13 150.0C — Vol 2,751 | 最新价 $0.25 | OI 1938→2863 (ΔOI +925张) | ΔOI/Volume 33.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增925张（+47.7% vs前日OI），连续性待观察（方向未知）
11-13 140.0C — Vol 5,842 | 最新价 $1.75 | OI 3671→4544 (ΔOI +873张) | ΔOI/Volume 14.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增873张（+23.8% vs前日OI），连续性待观察（方向未知）
11-13 149.0C — Vol 746 | 最新价 $0.26 | OI 357→1003 (ΔOI +646张) | ΔOI/Volume 86.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增646张（+180.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 6,151 张（Put 1,232 / Call 4,919），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +4.1k / P -0.2k ｜ Activity MEDIUM △ ｜ 1D
11-20  C +4.0k / P +0.7k ｜ Activity HIGH ｜ 8D
11-27  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 15D
12-04  C +0.2k / P +0.4k ｜ Activity LOW ｜ 22D

📆 11-13 Forward Structure
存量OI: C 76.6k / P 37.2k，今日变化ΔOI: C +4.1k / P -0.2k，平值价格ATM: C $2.60 / P $2.71 ｜ ATM IV 87.8%，净 delta 敞口 63k shares
Top ΔOI: C 140 +873
仓位参考: Max Pain 137 ｜ Call Wall 141（+7.7%，弱）（OI 9.3k） ｜ Put Wall 130（-0.7%，弱）（OI 2.2k）
量化解读： 存量 Call 重｜ATM IV 87.8%｜历史 Rank 77%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 63,311 股

📆 11-20 Forward Structure
存量OI: C 85.4k / P 61.9k，今日变化ΔOI: C +4.0k / P +0.7k，平值价格ATM: C $5.85 / P $5.69 ｜ ATM IV 72.9%，净 delta 敞口 171k shares
Top ΔOI: C 150 +2,475
仓位参考: Max Pain 155 ｜ Call Wall 140（+6.9%，弱）（OI 2.4k） ｜ Put Wall 120（-8.3%）（OI 7.3k）
量化解读： 存量 Call 重｜ATM IV 72.9%｜历史 Rank 77%（近端代理）｜IV/RV 1.08×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 171,280 股

11-27（MEDIUM △）Top ΔOI: 140C +91
11-27（MEDIUM △）仓位参考: Max Pain 142 ｜ Call Wall 140（+6.9%，弱）（OI 0.4k） ｜ Put Wall 120（-8.3%，弱）（OI 0.6k）

12-04（Activity LOW）仓位参考: Max Pain 140 ｜ Call Wall 140（+6.9%）（OI 1.4k） ｜ Put Wall 135（+3.1%）（OI 2.2k）

📅 事件差分（观察，非因果）: 11-13（1D）ATM IV 87.8% vs 11-20 72.9%（差 +14.8pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup C v1 — Core Conditions
Price Regime DOWN | Location above_flip | Gamma Regime POSITIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 1 ｜ ? 1（? put_buy_confirmation）
验证状态: N=0 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_mdd >= 0.03 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=0）
环境: Vol NORMAL（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-12/COIN_morning.json