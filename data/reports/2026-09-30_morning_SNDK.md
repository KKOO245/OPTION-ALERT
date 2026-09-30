# 期权晨报 2026-09-30（快照 10:20 ET）

📊 市场环境

SPY $763.55 ｜ QQQ $739.77
VIX 15.68 ↓2.2%（5D +3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 30.8（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-09-30

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 09-30 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】GDP 增速 Rate QoQ Final　预测 1.5 ｜ 实际 2.2 ｜ 前值 2.5　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Spending MoM　预测 0.8 ｜ 实际 0.9 ｜ 前值 0.1　✅ 今日已公布
- 周三 09-30 08:30　【高】Personal Income MoM　预测 0.4 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周四 10-01 10:00　【高】ISM 制造业 PMI　预测 55 ｜ 实际 待公布 ｜ 前值 54.6
- 周五 10-02 08:30　【高】Non Farm Payrolls　预测 90 ｜ 实际 待公布 ｜ 前值 162
- 周五 10-02 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 10-02（2D）ATM IV 89.6% vs 10-09 70.1%（差 +19.5pp），覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,729.76 → 今开 1,729.23（-0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 1755.97 ｜ 低 1720.71

Options: P/C成交量 0.45 | OI比 0.89 | ATM IV 89.6% | Skew -5.5pp | Term 0.84 | ExpMove ±5.6%（近端） | Rank 43%
量化视角： IV 中性（Rank 43%）｜期限结构倒挂（Term 0.84，近月 IV 高于远月）｜Put 保护异常便宜（Skew -5.5pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.89×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-02（2D）±5.6% ｜ 10-09（9D）±9.0% ｜ 10-16（16D）±12.5% ｜ 10-23（23D）±15.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,650,623 | GEX Change vs 上次快照 943,154 | Flip: Primary Flip: 1705.79（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1742 / LOW 420 / INVALID 1104
结构观察区: Primary Flip 1705.79（全链重定价，覆盖 99%）
最近结构参考: Flip 1706（现价高于该位 1.6%）
量化视角： 正 Gamma（265万，无历史分位）｜正 Gamma 增强（+94万）｜现价位于 Flip 上方 1.65%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,700（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 1706（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 2000.0C — Vol 4,519 | 最新价 $3.30 | OI 5260→7002 (ΔOI +1742张) | ΔOI/Volume 38.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1742张（+33.1% vs前日OI），连续性待观察（方向未知）
10-02 1900.0C — Vol 3,673 | 最新价 $9.10 | OI 1840→2566 (ΔOI +726张) | ΔOI/Volume 19.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增726张（+39.5% vs前日OI），连续性待观察（方向未知）
10-02 1950.0C — Vol 1,582 | 最新价 $5.40 | OI 762→1344 (ΔOI +582张) | ΔOI/Volume 36.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增582张（+76.4% vs前日OI），连续性待观察（方向未知）
10-02 2170.0C — Vol 310 | 最新价 $0.65 | OI 45→320 (ΔOI +275张) | ΔOI/Volume 88.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增275张（+611.1% vs前日OI），连续性待观察（方向未知）
10-02 1750.0C — Vol 2,947 | 最新价 $42.96 | OI 684→957 (ΔOI +273张) | ΔOI/Volume 9.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增273张（+39.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,598 张（Put 0 / Call 3,598），跨 1 个期限——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-02  C +6.2k / P +2.6k ｜ Activity HIGH ｜ 2D
10-09  C +1.1k / P +1.0k ｜ Activity MEDIUM △ ｜ 9D
10-16  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 16D
10-23  C +0.3k / P +0.5k ｜ Activity MEDIUM △ ｜ 23D

📆 10-02 Forward Structure
存量OI: C 44.9k / P 40.1k，今日变化ΔOI: C +6.2k / P +2.6k，平值价格ATM: C $49.20 / P $48.66 ｜ ATM IV 89.6%，净 delta 敞口 56k shares
Top ΔOI: C 2000 +1,742 ｜ C 1900 +726 ｜ C 1950 +582
仓位参考: Max Pain 1,700 ｜ Call Wall 1900（+9.6%，弱）（OI 2.6k） ｜ Put Wall 1600（-7.7%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜ATM IV 89.6%｜历史 Rank 43%（近端代理）｜IV/RV 1.43×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 55,736 股

10-09（MEDIUM △）Top ΔOI: 2200C +161 ｜ 2000C +138
10-09（MEDIUM △）仓位参考: Max Pain 1,650 ｜ Call Wall 1900（+9.6%，弱）（OI 0.5k） ｜ Put Wall 1800（+3.8%）（OI 0.8k）

10-16（MEDIUM △）Top ΔOI: 1900C +187 ｜ 1840C +104
10-16（MEDIUM △）仓位参考: Max Pain 1,650 ｜ Call Wall 1900（+9.6%，弱）（OI 1.3k） ｜ Put Wall 1600（-7.7%，弱）（OI 1.6k）

10-23（MEDIUM △）Top ΔOI: 1315P +218 ｜ 2020C +47
10-23（MEDIUM △）仓位参考: Max Pain 1,750 ｜ Call Wall 1840（+6.1%，弱）（OI 0.2k） ｜ Put Wall 1650（-4.8%，弱）（OI 0.2k）

📅 事件差分（观察，非因果）: 10-02（2D）ATM IV 89.6% vs 10-09 70.1%（差 +19.5pp）——覆盖 PCE 物价 Price Index MoM、GDP 增速 Rate QoQ Final 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-09-30/SNDK_morning.json