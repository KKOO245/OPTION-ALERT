# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.55 ｜ QQQ $759.66
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.3（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🔴 **事件差分**: 10-09（3D）ATM IV 89.8% vs 10-16 74.8%（差 +15.1pp），覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 15.51 → 今开 16.10（+3.8%） | 较昨收变动（含盘初走势） ｜ 今日高 16.80 ｜ 低 16.00

Options: P/C成交量 0.01 | OI比 0.38 | ATM IV 89.8% | Skew 23.0pp | Term 0.80 | ExpMove ±8.4%（近端） | Rank 21%
量化视角： IV 历史低位（Rank 21%，期权偏便宜）｜期限结构倒挂（Term 0.80，近月 IV 高于远月）｜保护溢价显著（Skew 23.0pp，Put 明显贵于 Call）｜存量 Call 偏重（OI比 0.38）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.01×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.38×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±8.4% ｜ 10-16（10D）±10.2% ｜ 10-23（17D）±12.9% ｜ 10-30（24D）±11.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,321,738 | GEX Change vs 上次快照 2,084,523 | Flip: Primary Flip: 14.93（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 88%（带内） ｜ IV 有效性: VALID 179 / LOW 92 / INVALID 157
结构观察区: Primary Flip 14.93（全链重定价，覆盖 88%）
Put Wall 15（弱结构｜现价高于该位 10.7%）
最近结构参考: Put Wall 15（现价高于该位 10.7%）
量化视角： 正 Gamma（232万，无历史分位）｜正 Gamma 增强（+208万）｜现价位于 Flip 上方 11.15%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构） / 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 88%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 15.5C — Vol 545 | 最新价 $0.47 | OI 20→286 (ΔOI +266张) | ΔOI/Volume 48.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增266张（+1330.0% vs前日OI），连续性待观察（方向未知）
10-09 16.0C — Vol 529 | 最新价 $0.29 | OI 116→360 (ΔOI +244张) | ΔOI/Volume 46.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增244张（+210.3% vs前日OI），连续性待观察（方向未知）
10-09 16.5C — Vol 227 | 最新价 $0.15 | OI 161→345 (ΔOI +184张) | ΔOI/Volume 81.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增184张（+114.3% vs前日OI），连续性待观察（方向未知）
10-09 15.0P — Vol 170 | 最新价 $0.26 | OI 280→415 (ΔOI +135张) | ΔOI/Volume 79.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增135张（+48.2% vs前日OI），连续性待观察（方向未知）
10-09 14.5P — Vol 109 | 最新价 $0.11 | OI 211→318 (ΔOI +107张) | ΔOI/Volume 98.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增107张（+50.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 936 张（Put 242 / Call 694），跨 1 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +0.9k / P +0.3k ｜ Activity MEDIUM △ ｜ 3D
10-16  C +0.3k / P -15 ｜ Activity MEDIUM △ ｜ 10D
10-23  C +36 / P +44 ｜ Activity LOW ｜ 17D
10-30  C +0.1k / P +10 ｜ Activity LOW ｜ 24D

📆 10-09 Forward Structure
存量OI: C 6.6k / P 2.5k，今日变化ΔOI: C +0.9k / P +0.3k，平值价格ATM: C $0.33 / P $1.07 ｜ ATM IV 89.8%，净 delta 敞口 49k shares
Top ΔOI: C 15 +266 ｜ C 16 +244 ｜ C 16 +184
仓位参考: Max Pain 16 ｜ Put Wall 15.5（-6.6%，弱）（OI 0.5k）
量化解读： 存量 Call 重｜ATM IV 89.8%｜历史 Rank 21%（近端代理）｜IV/RV 1.59×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 48,935 股

10-16（MEDIUM △）Top ΔOI: 15P +102 ｜ 17C +69
10-16（MEDIUM △）仓位参考: Max Pain 19 ｜ Put Wall 15（-9.6%，弱）（OI 1.0k）

10-23（Activity LOW）仓位参考: Max Pain 18 ｜ Put Wall 16（-3.6%，弱）（OI 0.2k）

10-30（Activity LOW）仓位参考: Max Pain 16 ｜ Put Wall 15（-9.6%，弱）（OI 89）

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 89.8% vs 10-16 74.8%（差 +15.1pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/NNE_morning.json