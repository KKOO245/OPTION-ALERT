# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $774.46 ｜ QQQ $754.65
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
🟡 **近现价集中开仓**: 10-09 135P ΔOI +492（距现价 -2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 137.97 → 今开 139.50（+1.1%） | 较昨收变动（含盘初走势） ｜ 今日高 140.80 ｜ 低 137.49

Options: P/C成交量 0.21 | OI比 0.77 | ATM IV 53.9% | Skew 0.4pp | Term 1.09 | ExpMove ±3.5%（近端） | Rank 32%
量化视角： IV 中性（Rank 32%）｜期限结构正常（Term 1.09）｜保护溢价薄（Skew 0.4pp）｜存量 Call 偏重（OI比 0.77）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.21×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（2D）±3.5% ｜ 10-16（9D）±6.4% ｜ 10-23（16D）±8.2% ｜ 10-30（23D）±13.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 14,614,162 | GEX Change vs 上次快照 1,232,340 | Flip: Primary Flip: 133.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 532 / LOW 37 / INVALID 129
结构观察区: Primary Flip 133.64（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 7.8%）
最近结构参考: Flip 134（现价高于该位 3.5%）
量化视角： 正 Gamma（1461万，无历史分位）｜正 Gamma 增强（+123万）｜现价位于 Flip 上方 3.47%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 134（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-23 160.0C — Vol 2,786 | 最新价 $0.71 | OI 729→2844 (ΔOI +2115张) | ΔOI/Volume 75.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2115张（+290.1% vs前日OI），连续性待观察（方向未知）
10-09 135.0P — Vol 1,345 | 最新价 $1.42 | OI 741→1233 (ΔOI +492张) | ΔOI/Volume 36.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增492张（+66.4% vs前日OI），连续性待观察（方向未知）
10-23 142.0C — Vol 549 | 最新价 $4.45 | OI 123→585 (ΔOI +462张) | ΔOI/Volume 84.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增462张（+375.6% vs前日OI），连续性待观察（方向未知）
10-09 148.0C — Vol 396 | 最新价 $0.31 | OI 489→758 (ΔOI +269张) | ΔOI/Volume 67.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增269张（+55.0% vs前日OI），连续性待观察（方向未知）
10-09 126.0P — Vol 382 | 最新价 $0.15 | OI 706→967 (ΔOI +261张) | ΔOI/Volume 68.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增261张（+37.0% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,599 张（Put 753 / Call 2,846），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +1.1k / P +1.3k ｜ Activity HIGH ｜ 2D
10-16  C +0.5k / P +76 ｜ Activity MEDIUM △ ｜ 9D
10-23  C +3.2k / P +0.9k ｜ Activity HIGH ｜ 16D
10-30  C +0.6k / P +0.3k ｜ Activity MEDIUM △ ｜ 23D

📆 10-09 Forward Structure
存量OI: C 24.7k / P 19.0k，今日变化ΔOI: C +1.1k / P +1.3k，平值价格ATM: C $2.52 / P $2.25 ｜ ATM IV 53.9%，净 delta 敞口 -20k shares
Top ΔOI: P 135 +492 ｜ C 148 +269 ｜ P 126 +261
仓位参考: Max Pain 135 ｜ Call Wall 150（+8.5%）（OI 5.3k） ｜ Put Wall 135（-2.4%，弱）（OI 1.2k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 53.9%｜历史 Rank 32%（近端代理）｜IV/RV 1.87×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 20,374 股

10-16（MEDIUM △）Top ΔOI: 125P -209 ｜ 145C +207
10-16（MEDIUM △）仓位参考: Max Pain 130 ｜ Call Wall 150（+8.5%）（OI 14.2k） ｜ Put Wall 125（-9.6%，弱）（OI 5.4k）

📆 10-23 Forward Structure
存量OI: C 13.3k / P 17.0k，今日变化ΔOI: C +3.2k / P +0.9k，平值价格ATM: C $5.70 / P $5.60 ｜ ATM IV 47.9%，净 delta 敞口 45k shares
Top ΔOI: C 160 +2,115 ｜ C 142 +462
仓位参考: Max Pain 134 ｜ Call Wall 140（+1.2%，弱）（OI 1.0k） ｜ Put Wall 125（-9.6%，弱）（OI 2.0k）
量化解读： 存量 Put 重｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 47.9%｜历史 Rank 32%（近端代理）｜IV/RV 1.66×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 44,901 股

10-30（MEDIUM △）Top ΔOI: 150C +117 ｜ 138P +94
10-30（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 150（+8.5%，弱）（OI 0.7k） ｜ Put Wall 130（-6.0%，弱）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 53.9% vs 10-16 48.6%（差 +5.4pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/NOW_morning.json