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
🟡 **近现价集中开仓**: 10-09 175C ΔOI +1,678（距现价 +4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 164.43 → 今开 165.82（+0.8%） | 较昨收变动（含盘初走势） ｜ 今日高 168.63 ｜ 低 164.54

Options: P/C成交量 0.47 | OI比 0.73 | ATM IV 67.8% | Skew -7.8pp | Term 0.95 | ExpMove ±5.1%（近端） | Rank 24%
量化视角： IV 历史低位（Rank 24%，期权偏便宜）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -7.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.73）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（3D）±5.1% ｜ 10-16（10D）±8.2% ｜ 10-23（17D）±10.4% ｜ 10-30（24D）±13.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 91,628,205 | GEX Change vs 上次快照 9,717,199 | Flip: Primary Flip: 148.48（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 682 / LOW 94 / INVALID 156
结构观察区: Primary Flip 148.48（全链重定价，覆盖 100%）
最近结构参考: Flip 148（现价高于该位 12.8%）
量化视角： 正 Gamma（9163万，无历史分位）｜正 Gamma 增强（+972万）｜现价位于 Flip 上方 12.85%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 155（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 148（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 125.0P — Vol 2,351 | 最新价 $0.70 | OI 498→2771 (ΔOI +2273张) | ΔOI/Volume 96.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2273张（+456.4% vs前日OI），连续性待观察（方向未知）
10-09 185.0C — Vol 4,959 | 最新价 $0.54 | OI 1583→3672 (ΔOI +2089张) | ΔOI/Volume 42.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2089张（+132.0% vs前日OI），连续性待观察（方向未知）
10-16 100.0P — Vol 2,223 | 最新价 $0.06 | OI 6897→8732 (ΔOI +1835张) | ΔOI/Volume 82.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1835张（+26.6% vs前日OI），连续性待观察（方向未知）
10-09 175.0C — Vol 6,905 | 最新价 $1.52 | OI 19361→21039 (ΔOI +1678张) | ΔOI/Volume 24.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1678张（+8.7% vs前日OI），连续性待观察（方向未知）
10-09 160.0P — Vol 7,132 | 最新价 $2.55 | OI 2591→3934 (ΔOI +1343张) | ΔOI/Volume 18.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1343张（+51.8% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 9,218 张（Put 5,451 / Call 3,767），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +8.4k / P +3.0k ｜ Activity HIGH ｜ 3D
10-16  C -0.5k / P +5.5k ｜ Activity HIGH ｜ 10D
10-23  C +0.9k / P +2.0k ｜ Activity HIGH ｜ 17D
10-30  C +0.4k / P +4.1k ｜ Activity MEDIUM △ ｜ 24D

📆 10-09 Forward Structure
存量OI: C 210.4k / P 153.6k，今日变化ΔOI: C +8.4k / P +3.0k，平值价格ATM: C $4.05 / P $4.45 ｜ ATM IV 67.8%，净 delta 敞口 5k shares
Top ΔOI: C 185 +2,089 ｜ C 175 +1,678 ｜ P 160 +1,343
仓位参考: Max Pain 155 ｜ Call Wall 165（-1.5%，弱）（OI 25.3k）
量化解读： 存量 Call 重｜ATM IV 67.8%｜历史 Rank 24%（近端代理）｜IV/RV 0.92×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 4,573 股

📆 10-16 Forward Structure
存量OI: C 176.3k / P 167.5k，今日变化ΔOI: C -0.5k / P +5.5k，平值价格ATM: C $6.85 / P $6.90 ｜ ATM IV 61.8%，净 delta 敞口 -58k shares
Top ΔOI: C 180 -1,467
仓位参考: Max Pain 130 ｜ Call Wall 155（-7.5%，弱）（OI 10.5k） ｜ Put Wall 160（-4.5%，弱）（OI 4.8k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 61.8%｜历史 Rank 24%（近端代理）｜IV/RV 0.83×（近似）｜净 delta 敞口 负 58,109 股

📆 10-23 Forward Structure
存量OI: C 25.5k / P 36.9k，今日变化ΔOI: C +0.9k / P +2.0k，平值价格ATM: C $8.96 / P $8.50 ｜ ATM IV 61.1%，净 delta 敞口 10k shares
仓位参考: Max Pain 160 ｜ Call Wall 172.5（+3.0%，弱）（OI 2.5k） ｜ Put Wall 155（-7.5%，弱）（OI 3.1k）
量化解读： 存量 Put 重｜ATM IV 61.1%｜历史 Rank 24%（近端代理）｜IV/RV 0.82×（近似）｜净 delta 敞口 正 9,578 股

10-30（MEDIUM △）Top ΔOI: 125P +2,273 ｜ 210C +525
10-30（MEDIUM △）仓位参考: Max Pain 160 ｜ Call Wall 162.5（-3.0%，弱）（OI 2.6k） ｜ Put Wall 160（-4.5%，弱）（OI 2.9k）

📅 事件差分（观察，非因果）: 10-09（3D）ATM IV 67.8% vs 10-16 61.8%（差 +6.0pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-06/MSTR_morning.json