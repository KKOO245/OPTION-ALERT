# 期权晨报 2026-11-11（快照 10:20 ET）

📊 市场环境

SPY $759.90 ｜ QQQ $690.38
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
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **事件差分**: 11-13 ATM IV 112.3% vs 11-20 98.4%（差 +13.9pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 859.99 → 今开 928.24（+7.9%） | 较昨收变动（含盘初走势） ｜ 今日高 978.36 ｜ 低 920.18

Options: P/C成交量 0.50 | OI比 0.63 | ATM IV 112.3% | Skew 0.8pp | Term 0.77 | ExpMove ±7.1%（近端） | Rank 70%
量化视角： IV 中性（Rank 70%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜保护溢价薄（Skew 0.8pp）｜存量 Call 偏重（OI比 0.63）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.63×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±7.1% ｜ 11-20（9D）±12.5% ｜ 11-27（16D）±15.4% ｜ 12-04（23D）±23.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,596,422 | GEX Change vs 上次快照 7,104,189 | Flip: Primary Flip: 899.13（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 2135 / LOW 743 / INVALID 1132
结构观察区: Primary Flip 899.13（全链重定价，覆盖 100%）
最近结构参考: Flip 899（现价高于该位 7.3%）
量化视角： 正 Gamma（460万，无历史分位）｜由负转正（+710万）｜现价位于 Flip 上方 7.32%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 900（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 899（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 1250.0C — Vol 419 | 最新价 $2.20 | OI 902→1300 (ΔOI +398张) | ΔOI/Volume 95.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增398张（+44.1% vs前日OI），连续性待观察（方向未知）
11-13 1100.0C — Vol 3,258 | 最新价 $0.83 | OI 2184→2528 (ΔOI +344张) | ΔOI/Volume 10.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增344张（+15.8% vs前日OI），值得跟踪（方向未知）
11-13 880.0C — Vol 3,736 | 最新价 $26.13 | OI 669→1000 (ΔOI +331张) | ΔOI/Volume 8.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增331张（+49.5% vs前日OI），连续性待观察（方向未知）
11-20 1080.0C — Vol 407 | 最新价 $6.90 | OI 759→1055 (ΔOI +296张) | ΔOI/Volume 72.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增296张（+39.0% vs前日OI），连续性待观察（方向未知）
11-13 900.0C — Vol 6,142 | 最新价 $19.10 | OI 1663→1947 (ΔOI +284张) | ΔOI/Volume 4.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增284张（+17.1% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,653 张（Put 0 / Call 1,653），跨 2 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +3.3k / P +2.6k ｜ Activity HIGH ｜ 2D
11-20  C +3.2k / P +0.4k ｜ Activity HIGH ｜ 9D
11-27  C +0.6k / P +0.2k ｜ Activity MEDIUM △ ｜ 16D
12-04  C +0.8k / P +0.3k ｜ Activity MEDIUM △ ｜ 23D

📆 11-13 Forward Structure
存量OI: C 48.3k / P 30.6k，今日变化ΔOI: C +3.3k / P +2.6k，平值价格ATM: C $37.11 / P $31.50 ｜ ATM IV 112.3%，净 delta 敞口 204k shares
Top ΔOI: C 1100 +344 ｜ C 880 +331 ｜ C 900 +284
仓位参考: Max Pain 900 ｜ Call Wall 1000（+3.6%，弱）（OI 2.6k） ｜ Put Wall 870（-9.8%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜ATM IV 112.3%｜历史 Rank 70%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 204,107 股

📆 11-20 Forward Structure
存量OI: C 75.2k / P 53.0k，今日变化ΔOI: C +3.2k / P +0.4k，平值价格ATM: C $63.00 / P $57.26 ｜ ATM IV 98.4%，净 delta 敞口 107k shares
Top ΔOI: C 1250 +398 ｜ C 1080 +296
仓位参考: Max Pain 1,100 ｜ Call Wall 1000（+3.6%，弱）（OI 2.1k） ｜ Put Wall 870（-9.8%，弱）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 98.4%｜历史 Rank 70%（近端代理）｜IV/RV 0.81×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 107,264 股

11-27（MEDIUM △）Top ΔOI: 740C +109 ｜ 770C +100
11-27（MEDIUM △）仓位参考: Max Pain 1,150 ｜ Put Wall 930（-3.6%，弱）（OI 0.2k）

12-04（MEDIUM △）Top ΔOI: 700P +74
12-04（MEDIUM △）仓位参考: Max Pain 1,000 ｜ Call Wall 950（-1.6%，弱）（OI 0.2k） ｜ Put Wall 970（+0.5%，弱）（OI 95）

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 112.3% vs 11-20 98.4%（差 +13.9pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/SNDK_morning.json