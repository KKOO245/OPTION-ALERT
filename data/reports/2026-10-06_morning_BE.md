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

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 305P ΔOI +566（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 286.65 → 今开 295.25（+3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 297.85 ｜ 低 285.64

Options: P/C成交量 0.47 | OI比 1.17 | ATM IV 75.0% | Skew -0.8pp | Term 1.08 | ExpMove ±5.7%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 1.08）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（3D）±5.7% ｜ 10-16（10D）±9.0% ｜ 10-23（17D）±11.3% ｜ 10-30（24D）±16.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 11,237,058 | GEX Change vs 上次快照 2,915,066 | Flip: Primary Flip: 275.89（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 596 / LOW 84 / INVALID 152
结构观察区: Primary Flip 275.89（全链重定价，覆盖 100%）
Call Wall 300（弱结构｜现价低于该位 1.4%）
最近结构参考: Call Wall 300（现价低于该位 1.4%）
量化视角： 正 Gamma（1124万，无历史分位）｜正 Gamma 增强（+292万）｜现价位于 Flip 上方 7.18%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 280（MaxPain，仅结算参考）；上方 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 276（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 230.0P — Vol 2,723 | 最新价 $0.50 | OI 2439→4032 (ΔOI +1593张) | ΔOI/Volume 58.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1593张（+65.3% vs前日OI），连续性待观察（方向未知）
10-09 240.0P — Vol 1,564 | 最新价 $0.21 | OI 1452→2592 (ΔOI +1140张) | ΔOI/Volume 72.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1140张（+78.5% vs前日OI），连续性待观察（方向未知）
10-09 267.5C — Vol 1,163 | 最新价 $23.10 | OI 103→977 (ΔOI +874张) | ΔOI/Volume 75.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增874张（+848.5% vs前日OI），连续性待观察（方向未知）
10-09 245.0P — Vol 1,826 | 最新价 $0.27 | OI 1111→1927 (ΔOI +816张) | ΔOI/Volume 44.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增816张（+73.5% vs前日OI），连续性待观察（方向未知）
10-09 270.0P — Vol 1,470 | 最新价 $2.56 | OI 815→1554 (ΔOI +739张) | ΔOI/Volume 50.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增739张（+90.7% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 5,162 张（Put 4,288 / Call 874），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +7.6k / P +9.8k ｜ Activity HIGH ｜ 3D
10-16  C +1.0k / P +4.2k ｜ Activity HIGH ｜ 10D
10-23  C +0.3k / P -0.3k ｜ Activity MEDIUM △ ｜ 17D
10-30  C +0.2k / P +1.9k ｜ Activity MEDIUM △ ｜ 24D

📆 10-09 Forward Structure
存量OI: C 31.6k / P 36.9k，今日变化ΔOI: C +7.6k / P +9.8k，平值价格ATM: C $8.65 / P $8.15 ｜ ATM IV 75.0%，净 delta 敞口 185k shares
Top ΔOI: C 267 +874
仓位参考: Max Pain 280 ｜ Call Wall 300（+1.5%）（OI 2.8k） ｜ Put Wall 280（-5.3%，弱）（OI 1.9k）
量化解读： 存量两侧均衡｜ATM IV 75.0%｜历史 Rank 32%（近端代理）｜IV/RV 0.99×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 185,018 股

📆 10-16 Forward Structure
存量OI: C 77.8k / P 89.0k，今日变化ΔOI: C +1.0k / P +4.2k，平值价格ATM: C $13.80 / P $12.85 ｜ ATM IV 66.9%，净 delta 敞口 -26k shares
Top ΔOI: P 230 +1,593 ｜ P 305 +566
仓位参考: Max Pain 270 ｜ Call Wall 270（-8.7%，弱）（OI 7.6k） ｜ Put Wall 275（-7.0%，弱）（OI 3.3k）
量化解读： 存量两侧均衡｜ATM IV 66.9%｜历史 Rank 32%（近端代理）｜IV/RV 0.89×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 26,333 股

10-23（MEDIUM △）Top ΔOI: 230P -644
10-23（MEDIUM △）仓位参考: Max Pain 270 ｜ Call Wall 300（+1.5%，弱）（OI 1.1k） ｜ Put Wall 280（-5.3%，弱）（OI 0.7k）

10-30（MEDIUM △）仓位参考: Max Pain 285 ｜ Call Wall 300（+1.5%，弱）（OI 1.3k） ｜ Put Wall 285（-3.6%，弱）（OI 1.8k）

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 75.0% vs 10-16 66.9%（差 +8.1pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/BE_morning.json