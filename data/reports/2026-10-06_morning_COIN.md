# 期权晨报 2026-10-06（快照 10:20 ET）

📊 市场环境

SPY $779.09 ｜ QQQ $759.66
VIX 15.48 ↓0.3%（5D -3.5%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 47.4（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-06

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 188.22 → 今开 188.26（+0.0%） | 较昨收变动（含盘初走势） ｜ 今日高 191.88 ｜ 低 187.65

Options: P/C成交量 0.34 | OI比 0.55 | ATM IV 63.2% | Skew -3.7pp | Term 1.05 | ExpMove ±4.8%（近端） | Rank 17%
量化视角： IV 历史低位（Rank 17%，期权偏便宜）｜期限结构正常（Term 1.05）｜Put 保护异常便宜（Skew -3.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.55）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.34×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.55×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±4.8% ｜ 10-16（10D）±7.6% ｜ 10-23（17D）±10.2% ｜ 10-30（24D）±13.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,075,914 | GEX Change vs 上次快照 4,131,419 | Flip: Primary Flip: 175.56（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 480 / LOW 119 / INVALID 239
结构观察区: Primary Flip 175.56（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 5.0%）
最近结构参考: Call Wall 200（现价低于该位 5.0%）
量化视角： 正 Gamma（3108万，无历史分位）｜正 Gamma 增强（+413万）｜现价位于 Flip 上方 8.22%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 188（MaxPain，仅结算参考）；上方 200（Call Wall，弱结构）。
• Gamma 区域：切换参考 176（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 105.0P — Vol 1,494 | 最新价 $0.05 | OI 4169→5519 (ΔOI +1350张) | ΔOI/Volume 90.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1350张（+32.4% vs前日OI），连续性待观察（方向未知）
10-09 205.0C — Vol 2,524 | 最新价 $0.81 | OI 1703→2532 (ΔOI +829张) | ΔOI/Volume 32.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增829张（+48.7% vs前日OI），连续性待观察（方向未知）
11-06 110.0P — Vol 853 | 最新价 $0.15 | OI 520→1239 (ΔOI +719张) | ΔOI/Volume 84.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增719张（+138.3% vs前日OI），连续性待观察（方向未知）
10-09 187.5C — Vol 2,827 | 最新价 $5.15 | OI 7833→8490 (ΔOI +657张) | ΔOI/Volume 23.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增657张（+8.4% vs前日OI），连续性待观察（方向未知）
11-06 105.0P — Vol 641 | 最新价 $0.19 | OI 4→643 (ΔOI +639张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增639张（+15975.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 4,194 张（Put 2,708 / Call 1,486），跨 3 个期限｜远端彩票/名义（3 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +4.7k / P +3.4k ｜ Activity HIGH ｜ 3D
10-16  C -5.9k / P +1.9k ｜ Activity HIGH ｜ 10D
10-23  C +0.6k / P +0.2k ｜ Activity MEDIUM △ ｜ 17D
10-30  C +0.5k / P +0.6k ｜ Activity MEDIUM △ ｜ 24D

📆 10-09 Forward Structure
存量OI: C 65.2k / P 36.2k，今日变化ΔOI: C +4.7k / P +3.4k，平值价格ATM: C $4.45 / P $4.70 ｜ ATM IV 63.2%，净 delta 敞口 50k shares
Top ΔOI: C 205 +829 ｜ C 187 +657 ｜ C 200 +615
仓位参考: Max Pain 188 ｜ Call Wall 195（+2.6%）（OI 12.8k） ｜ Put Wall 177.5（-6.6%，弱）（OI 1.9k）
量化解读： 存量 Call 重｜ATM IV 63.2%｜历史 Rank 17%（近端代理）｜IV/RV 0.86×（近似）｜净 delta 敞口 正 49,959 股

📆 10-16 Forward Structure
存量OI: C 85.5k / P 79.3k，今日变化ΔOI: C -5.9k / P +1.9k，平值价格ATM: C $7.45 / P $7.05 ｜ ATM IV 57.0%，净 delta 敞口 -474k shares
Top ΔOI: C 150 -4,694 ｜ C 220 -1,015
仓位参考: Max Pain 180 ｜ Call Wall 200（+5.3%，弱）（OI 7.0k） ｜ Put Wall 200（+5.3%，弱）（OI 3.9k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 57.0%｜历史 Rank 17%（近端代理）｜IV/RV 0.77×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 473,801 股

10-23（MEDIUM △）Top ΔOI: 190C +119 ｜ 200C +119
10-23（MEDIUM △）仓位参考: Max Pain 190 ｜ Call Wall 190（+0.0%，弱）（OI 0.8k） ｜ Put Wall 192.5（+1.3%，弱）（OI 0.4k）

10-30（MEDIUM △）Top ΔOI: 190C +117 ｜ 180P +108
10-30（MEDIUM △）仓位参考: Max Pain 185 ｜ Call Wall 185（-2.6%，弱）（OI 1.2k） ｜ Put Wall 185（-2.6%，弱）（OI 0.3k）

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 63.2% vs 10-16 57.0%（差 +6.2pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/COIN_morning.json