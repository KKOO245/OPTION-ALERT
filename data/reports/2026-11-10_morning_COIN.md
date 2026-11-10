# 期权晨报 2026-11-10（快照 10:20 ET）

📊 市场环境

SPY $750.86 ｜ QQQ $674.76
VIX 19.85 ↓0.3%（5D -4.7%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 33.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-10

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 11-10 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周二 11-10 08:30　【高】Inflation Rate MoM　预测 0.3 ｜ 实际 0.4 ｜ 前值 0.6　✅ 今日已公布
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 85.7% vs 11-20 75.0%（差 +10.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 136.10 → 今开 132.31（-2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 136.25 ｜ 低 130.25

Options: P/C成交量 0.62 | OI比 0.52 | ATM IV 85.7% | Skew 4.6pp | Term 0.83 | ExpMove ±6.5%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜保护溢价中性（Skew 4.6pp）｜存量 Call 偏重（OI比 0.52）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.62×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（3D）±6.5% ｜ 11-20（10D）±10.3% ｜ 11-27（17D）±12.3% ｜ 12-04（24D）±15.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 12,530,850 | GEX Change vs 上次快照 1,431,527 | Flip: Primary Flip: 128.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 445 / LOW 210 / INVALID 333
结构观察区: Primary Flip 128.79（全链重定价，覆盖 100%）
Call Wall 140（弱结构｜现价低于该位 3.8%）
最近结构参考: Call Wall 140（现价低于该位 3.8%）
量化视角： 正 Gamma（1253万，无历史分位）｜正 Gamma 增强（+143万）｜现价位于 Flip 上方 4.61%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 137（MaxPain，仅结算参考） / 140（Call Wall，弱结构）。
• Gamma 区域：切换参考 129（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 165.0C — Vol 5,477 | 最新价 $0.62 | OI 2777→6981 (ΔOI +4204张) | ΔOI/Volume 76.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4204张（+151.4% vs前日OI），连续性待观察（方向未知）
11-13 145.0C — Vol 2,088 | 最新价 $1.50 | OI 2574→3715 (ΔOI +1141张) | ΔOI/Volume 54.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1141张（+44.3% vs前日OI），连续性待观察（方向未知）
11-13 150.0C — Vol 1,918 | 最新价 $0.75 | OI 892→1800 (ΔOI +908张) | ΔOI/Volume 47.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增908张（+101.8% vs前日OI），连续性待观察（方向未知）
11-13 157.5C — Vol 602 | 最新价 $0.27 | OI 520→1001 (ΔOI +481张) | ΔOI/Volume 79.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增481张（+92.5% vs前日OI），连续性待观察（方向未知）
11-20 150.0C — Vol 893 | 最新价 $2.30 | OI 1860→2334 (ΔOI +474张) | ΔOI/Volume 53.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增474张（+25.5% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 7,208 张（Put 0 / Call 7,208），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +6.3k / P +1.3k ｜ Activity HIGH ｜ 3D
11-20  C +1.4k / P -1.2k ｜ Activity HIGH ｜ 10D
11-27  C +0.7k / P +0.6k ｜ Activity MEDIUM △ ｜ 17D
12-04  C +0.6k / P +0.8k ｜ Activity MEDIUM △ ｜ 24D

📆 11-13 Forward Structure
存量OI: C 69.8k / P 36.6k，今日变化ΔOI: C +6.3k / P +1.3k，平值价格ATM: C $4.10 / P $4.60 ｜ ATM IV 85.7%，净 delta 敞口 158k shares
Top ΔOI: C 145 +1,141 ｜ C 150 +908
仓位参考: Max Pain 137 ｜ Call Wall 147（+9.1%，弱）（OI 8.8k） ｜ Put Wall 135（+0.2%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 85.7%｜历史 Rank 73%（近端代理）｜IV/RV 1.30×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 157,502 股

📆 11-20 Forward Structure
存量OI: C 79.5k / P 61.2k，今日变化ΔOI: C +1.4k / P -1.2k，平值价格ATM: C $6.90 / P $7.00 ｜ ATM IV 75.0%，净 delta 敞口 199k shares
Top ΔOI: C 170 -5,074 ｜ C 165 +4,204 ｜ P 195 -774
仓位参考: Max Pain 162 ｜ Put Wall 140（+3.9%，弱）（OI 3.4k）
量化解读： 存量 Call 重｜ATM IV 75.0%｜历史 Rank 73%（近端代理）｜IV/RV 1.14×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 199,303 股

11-27（MEDIUM △）仓位参考: Max Pain 145 ｜ Call Wall 140（+3.9%，弱）（OI 0.2k） ｜ Put Wall 130（-3.5%，弱）（OI 0.4k）

12-04（MEDIUM △）Top ΔOI: 125P +460 ｜ 140C +99
12-04（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 140（+3.9%）（OI 1.4k） ｜ Put Wall 135（+0.2%）（OI 1.8k）

📅 事件差分（观察，非因果）: 11-13（3D）ATM IV 85.7% vs 11-20 75.0%（差 +10.7pp）——覆盖 Core Inflation Rate MoM、Inflation Rate MoM 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-10/COIN_morning.json