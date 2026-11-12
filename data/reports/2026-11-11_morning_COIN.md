# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.81 ｜ QQQ $nan
VIX 18.31 ↓5.9%（5D +10.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 37.0（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-11

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周四 11-12 10:00　【高】成屋销售　预测 3.85 ｜ 实际 待公布 ｜ 前值 3.99
- 周五 11-13 08:30　【高】PPI 生产者物价 MoM　预测 0.4 ｜ 实际 待公布 ｜ 前值 1.3

🔍 重点速览
🟡 **事件差分**: 11-13 ATM IV 83.1% vs 11-20 72.4%（差 +10.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-20 140C ΔOI +942（距现价 +4.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 132.13 → 今开 133.00（+0.7%） | 较昨收变动（含盘初走势） ｜ 今日高 136.30 ｜ 低 132.87

Options: P/C成交量 0.59 | OI比 0.51 | ATM IV 83.1% | Skew 3.5pp | Term 0.86 | ExpMove ±5.3%（近端） | Rank 68%
量化视角： IV 中性（Rank 68%）｜期限结构倒挂（Term 0.86，近月 IV 高于远月）｜保护溢价中性（Skew 3.5pp）｜存量 Call 偏重（OI比 0.51）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.59×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±5.3% ｜ 11-20（9D）±9.1% ｜ 11-27（16D）±10.9% ｜ 12-04（23D）±13.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 10,411,375 | GEX Change vs 上次快照 5,706,031 | Flip: Primary Flip: 129.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 438 / LOW 216 / INVALID 334
结构观察区: Primary Flip 129.90（全链重定价，覆盖 100%）
Call Wall 140（弱结构｜现价低于该位 4.7%）
最近结构参考: Flip 130（现价高于该位 2.7%）
量化视角： 正 Gamma（1041万，无历史分位）｜正 Gamma 增强（+571万）｜现价位于 Flip 上方 2.75%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 137（MaxPain，仅结算参考） / 140（Call Wall，弱结构）。
• Gamma 区域：切换参考 130（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 140.0C — Vol 2,942 | 最新价 $3.60 | OI 1727→2669 (ΔOI +942张) | ΔOI/Volume 32.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增942张（+54.5% vs前日OI），连续性待观察（方向未知）
11-13 147.0C — Vol 1,061 | 最新价 $0.38 | OI 8789→9280 (ΔOI +491张) | ΔOI/Volume 46.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增491张（+5.6% vs前日OI），连续性待观察（方向未知）
12-04 135.0P — Vol 445 | 最新价 $11.37 | OI 1754→2164 (ΔOI +410张) | ΔOI/Volume 92.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增410张（+23.4% vs前日OI），连续性待观察（方向未知）
11-13 141.0C — Vol 939 | 最新价 $1.24 | OI 8630→9033 (ΔOI +403张) | ΔOI/Volume 42.9% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增403张（+4.7% vs前日OI），值得跟踪（方向未知）
11-20 122.0P — Vol 422 | 最新价 $2.62 | OI 14→410 (ΔOI +396张) | ΔOI/Volume 93.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增396张（+2828.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,642 张（Put 806 / Call 1,836），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +2.8k / P +0.8k ｜ Activity HIGH ｜ 2D
11-20  C +1.9k / P +16 ｜ Activity MEDIUM △ ｜ 9D
11-27  C +0.5k / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
12-04  C +0.2k / P +0.4k ｜ Activity MEDIUM △ ｜ 23D

📆 11-13 Forward Structure
存量OI: C 72.6k / P 37.3k，今日变化ΔOI: C +2.8k / P +0.8k，平值价格ATM: C $3.90 / P $3.21 ｜ ATM IV 83.1%，净 delta 敞口 126k shares
Top ΔOI: C 141 +403 ｜ C 143 +377
仓位参考: Max Pain 137 ｜ Call Wall 141（+5.6%，弱）（OI 9.0k） ｜ Put Wall 135（+1.1%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 83.1%｜历史 Rank 68%（近端代理）｜IV/RV 1.26×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 125,803 股

11-20（MEDIUM △）Top ΔOI: 140C +942 ｜ 122P +396
11-20（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 140（+4.9%，弱）（OI 2.7k） ｜ Put Wall 140（+4.9%，弱）（OI 3.4k）

11-27（MEDIUM △）Top ΔOI: 140C +62
11-27（MEDIUM △）仓位参考: Max Pain 145 ｜ Call Wall 140（+4.9%，弱）（OI 0.3k） ｜ Put Wall 130（-2.6%，弱）（OI 0.4k）

12-04（MEDIUM △）Top ΔOI: 135P +410
12-04（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 140（+4.9%）（OI 1.4k） ｜ Put Wall 135（+1.1%）（OI 2.2k）

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 83.1% vs 11-20 72.4%（差 +10.7pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/COIN_morning.json