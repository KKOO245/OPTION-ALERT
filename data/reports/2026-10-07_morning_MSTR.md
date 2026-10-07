# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $774.46 ｜ QQQ $754.67
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.5（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　⏰ 今日
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 162P ΔOI +5,334（距现价 +4.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 164.55 → 今开 157.82（-4.1%） | 较昨收变动（含盘初走势） ｜ 今日高 158.66 ｜ 低 154.82

Options: P/C成交量 0.67 | OI比 0.73 | ATM IV 67.8% | Skew -2.8pp | Term 0.92 | ExpMove ±4.4%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.67×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±4.4% ｜ 10-16（9D）±7.8% ｜ 10-23（16D）±10.2% ｜ 10-30（23D）±12.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 31,386,198 | GEX Change vs 上次快照 -57,993,352 | Flip: Primary Flip: 150.75（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 668 / LOW 95 / INVALID 179
结构观察区: Primary Flip 150.75（全链重定价，覆盖 100%）
最近结构参考: Flip 151（现价高于该位 3.6%）
量化视角： 正 Gamma（3139万，无历史分位）｜正 Gamma 减弱（5799万）｜现价位于 Flip 上方 3.56%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 151（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 185.0C — Vol 9,311 | 最新价 $1.58 | OI 2996→8724 (ΔOI +5728张) | ΔOI/Volume 61.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5728张（+191.2% vs前日OI），连续性待观察（方向未知）
10-16 162.5P — Vol 5,847 | 最新价 $5.45 | OI 1205→6539 (ΔOI +5334张) | ΔOI/Volume 91.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5334张（+442.7% vs前日OI），连续性待观察（方向未知）
10-16 150.0P — Vol 9,910 | 最新价 $1.43 | OI 4839→9759 (ΔOI +4920张) | ΔOI/Volume 49.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4920张（+101.7% vs前日OI），连续性待观察（方向未知）
10-16 85.0P — Vol 5,051 | 最新价 $0.04 | OI 6561→11244 (ΔOI +4683张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4683张（+71.4% vs前日OI），连续性待观察（方向未知）
10-09 172.5C — Vol 8,979 | 最新价 $1.49 | OI 21079→25065 (ΔOI +3986张) | ΔOI/Volume 44.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3986张（+18.9% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 24,651 张（Put 14,937 / Call 9,714），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $4M，买/卖方向不可观测）｜远端彩票/名义（1 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +4.4k / P +3.2k ｜ Activity MEDIUM △ ｜ 2D
10-16  C +7.6k / P +16.5k ｜ Activity HIGH ｜ 9D
10-23  C +1.0k / P +3.2k ｜ Activity MEDIUM △ ｜ 16D
10-30  C +2.1k / P +2.2k ｜ Activity HIGH ｜ 23D

📆 10-09 Forward Structure
存量OI: C 214.8k / P 156.8k，今日变化ΔOI: C +4.4k / P +3.2k，平值价格ATM: C $4.15 / P $2.75 ｜ ATM IV 67.8%，净 delta 敞口 -314k shares
Top ΔOI: C 172 +3,986 ｜ C 167 +1,440 ｜ P 165 +1,360
仓位参考: Max Pain 155 ｜ Call Wall 165（+5.7%，弱）（OI 24.7k）
量化解读： 存量 Call 重｜ATM IV 67.8%｜历史 Rank 24%（近端代理）｜IV/RV 0.93×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 313,761 股

📆 10-16 Forward Structure
存量OI: C 183.9k / P 184.0k，今日变化ΔOI: C +7.6k / P +16.5k，平值价格ATM: C $6.98 / P $5.15 ｜ ATM IV 60.5%，净 delta 敞口 -572k shares
Top ΔOI: C 185 +5,728 ｜ P 162 +5,334 ｜ P 150 +4,920
仓位参考: Max Pain 130 ｜ Call Wall 155（-0.7%，弱）（OI 10.5k） ｜ Put Wall 150（-3.9%，弱）（OI 9.8k）
量化解读： 存量两侧均衡｜ATM IV 60.5%｜历史 Rank 24%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 负 572,133 股

10-23（MEDIUM △）Top ΔOI: 160P +728 ｜ 170C +608
10-23（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 170（+8.9%，弱）（OI 2.2k） ｜ Put Wall 160（+2.5%，弱）（OI 3.8k）

📆 10-30 Forward Structure
存量OI: C 22.2k / P 31.7k，今日变化ΔOI: C +2.1k / P +2.2k，平值价格ATM: C $10.80 / P $8.77 ｜ ATM IV 61.2%，净 delta 敞口 -6k shares
Top ΔOI: C 165 +883
仓位参考: Max Pain 160 ｜ Call Wall 162.5（+4.1%，弱）（OI 2.6k） ｜ Put Wall 160（+2.5%，弱）（OI 3.2k）
量化解读： 存量 Put 重｜ATM IV 61.2%｜历史 Rank 24%（近端代理）｜IV/RV 0.84×（近似）｜净 delta 敞口 负 6,339 股

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 67.8% vs 10-16 60.5%（差 +7.3pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/MSTR_morning.json