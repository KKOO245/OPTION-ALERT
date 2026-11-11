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
🔴 **事件差分**: 11-13（2D）ATM IV 124.6% vs 11-20 106.3%（差 +18.2pp），覆盖 成屋销售、PPI 生产者物价 MoM
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 7.92 → 今开 8.28（+4.5%） | 较昨收变动（含盘初走势） ｜ 今日高 8.55 ｜ 低 8.18

Options: P/C成交量 0.82 | OI比 0.24 | ATM IV 124.6% | Skew 4.7pp | Term 0.79 | ExpMove ±8.0%（近端） | Rank 63%
量化视角： IV 中性（Rank 63%）｜期限结构倒挂（Term 0.79，近月 IV 高于远月）｜保护溢价中性（Skew 4.7pp）｜存量 Call 偏重（OI比 0.24）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.82×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.24×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-13（2D）±8.0% ｜ 11-20（9D）±19.1% ｜ 11-27（16D）±17.8% ｜ 12-04（23D）±16.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,276,205 | GEX Change vs 上次快照 2,251,667 | Flip: Primary Flip: 7.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 243 / LOW 94 / INVALID 87
结构观察区: Primary Flip 7.97（全链重定价，覆盖 100%）
Put Wall 9（弱结构｜现价低于该位 6.8%） | Call Wall 9（现价低于该位 6.8%）
最近结构参考: Flip 8（现价高于该位 5.3%）
量化视角： 正 Gamma（228万，无历史分位）｜正 Gamma 增强（+225万）｜现价位于 Flip 上方 5.27%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：上方 9（Put Wall，弱结构） / 8（MaxPain，仅结算参考） / 9（Call Wall）。
• Gamma 区域：切换参考 8（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 7.0P — Vol 1,181 | 最新价 $0.20 | OI 2077→2896 (ΔOI +819张) | ΔOI/Volume 69.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增819张（+39.4% vs前日OI），连续性待观察（方向未知）
11-13 9.0P — Vol 2,310 | 最新价 $1.16 | OI 714→1501 (ΔOI +787张) | ΔOI/Volume 34.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增787张（+110.2% vs前日OI），连续性待观察（方向未知）
11-13 8.5C — Vol 1,244 | 最新价 $0.12 | OI 812→1297 (ΔOI +485张) | ΔOI/Volume 39.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增485张（+59.7% vs前日OI），连续性待观察（方向未知）
11-13 8.5P — Vol 475 | 最新价 $0.70 | OI 410→635 (ΔOI +225张) | ΔOI/Volume 47.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增225张（+54.9% vs前日OI），连续性待观察（方向未知）
11-13 7.5P — Vol 540 | 最新价 $0.16 | OI 541→734 (ΔOI +193张) | ΔOI/Volume 35.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增193张（+35.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,509 张（Put 2,024 / Call 485），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-13  C +0.2k / P +1.1k ｜ Activity MEDIUM △ ｜ 2D
11-20  C -0.1k / P +0.3k ｜ Activity MEDIUM △ ｜ 9D
11-27  C +0.1k / P -8 ｜ Activity MEDIUM △ ｜ 16D
12-04  C +0.1k / P +33 ｜ Activity MEDIUM △ ｜ 23D

📆 11-13 Forward Structure
存量OI: C 27.8k / P 6.7k，今日变化ΔOI: C +0.2k / P +1.1k，平值价格ATM: C $0.29 / P $0.38 ｜ ATM IV 124.6%，净 delta 敞口 -56k shares
Top ΔOI: P 9 +787 ｜ C 8 +485 ｜ C 9 -302
仓位参考: Max Pain 8 ｜ Call Wall 9（+7.3%，弱）（OI 3.3k） ｜ Put Wall 9（+7.3%）（OI 1.5k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 124.6%｜历史 Rank 63%（近端代理）｜IV/RV 1.19×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 55,640 股

11-20（MEDIUM △）Top ΔOI: 9P -786
11-20（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 9（+7.3%，弱）（OI 4.3k） ｜ Put Wall 8（-4.6%，弱）（OI 7.2k）

11-27（MEDIUM △）Top ΔOI: 9C +78
11-27（MEDIUM △）仓位参考: Max Pain 9 ｜ Call Wall 8.5（+1.3%，弱）（OI 1.1k） ｜ Put Wall 8（-4.6%，弱）（OI 0.5k）

12-04（MEDIUM △）Top ΔOI: 8C +83
12-04（MEDIUM △）仓位参考: Max Pain 10 ｜ Call Wall 9（+7.3%，弱）（OI 0.2k） ｜ Put Wall 8.5（+1.3%）（OI 0.2k）

📅 事件差分（观察，非因果）: 11-13（2D）ATM IV 124.6% vs 11-20 106.3%（差 +18.2pp）——覆盖 成屋销售、PPI 生产者物价 MoM
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-11/USAR_morning.json