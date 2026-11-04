# 期权晨报 2026-11-04（快照 10:20 ET）

📊 市场环境

SPY $767.96 ｜ QQQ $691.95
VIX 17.01 ↓18.3%（5D +0.6%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.3（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-11-04

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 11-04 10:00　【高】ISM 非制造业 PMI　预测 54.8 ｜ 实际 54.5 ｜ 前值 54.9　✅ 今日已公布
- 周五 11-06 08:30　【高】Non Farm Payrolls　预测 65 ｜ 实际 待公布 ｜ 前值 29
- 周五 11-06 08:30　【高】失业率　预测 4.2 ｜ 实际 待公布 ｜ 前值 4.2
- 周五 11-06 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 48 ｜ 实际 待公布 ｜ 前值 46.3

🔍 重点速览
🟡 **事件差分**: 11-06 ATM IV 94.8% vs 11-13 80.7%（差 +14.1pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 11-06 140C ΔOI +7,148（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 135.63 → 今开 136.47（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 146.04 ｜ 低 135.80

Options: P/C成交量 0.64 | OI比 0.62 | ATM IV 94.8% | Skew -0.8pp | Term 0.77 | ExpMove ±6.0%（近端） | Rank 74%
量化视角： IV 中性（Rank 74%）｜期限结构倒挂（Term 0.77，近月 IV 高于远月）｜Put 保护异常便宜（Skew -0.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.62）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.64×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.62×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 11-06（2D）±6.0% ｜ 11-13（9D）±10.1% ｜ 11-20（16D）±13.3% ｜ 11-27（23D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 87,431,521 | GEX Change vs 上次快照 11,107,839 | Flip: Primary Flip: 123.90（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 459 / LOW 119 / INVALID 262
结构观察区: Primary Flip 123.90（全链重定价，覆盖 100%）
Call Wall 135（现价高于该位 5.0%）
最近结构参考: Call Wall 135（现价高于该位 5.0%）
量化视角： 正 Gamma（8743万，无历史分位）｜正 Gamma 增强（+1111万）｜现价位于 Flip 上方 14.38%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 135（MaxPain，仅结算参考） / 135（Call Wall）。
• Gamma 区域：切换参考 124（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-06 140.0C — Vol 12,702 | 最新价 $3.05 | OI 3457→10605 (ΔOI +7148张) | ΔOI/Volume 56.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7148张（+206.8% vs前日OI），连续性待观察（方向未知）
11-20 110.0P — Vol 6,467 | 最新价 $1.60 | OI 4969→10753 (ΔOI +5784张) | ΔOI/Volume 89.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5784张（+116.4% vs前日OI），连续性待观察（方向未知）
11-06 85.0P — Vol 5,450 | 最新价 $0.02 | OI 1016→5685 (ΔOI +4669张) | ΔOI/Volume 85.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4669张（+459.6% vs前日OI），连续性待观察（方向未知）
11-06 136.0C — Vol 4,667 | 最新价 $4.69 | OI 24254→26527 (ΔOI +2273张) | ΔOI/Volume 48.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2273张（+9.4% vs前日OI），连续性待观察（方向未知）
11-06 160.0C — Vol 4,623 | 最新价 $0.21 | OI 4343→6490 (ΔOI +2147张) | ΔOI/Volume 46.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2147张（+49.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 22,021 张（Put 10,453 / Call 11,568），跨 2 个期限｜有实质成本保护 1 档（权利金 >$1，买/卖方向不可观测）｜远端彩票/名义（2 档，距现价 >10%，价 ≤$0.05）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

11-06  C +7.4k / P +5.5k ｜ Activity HIGH ｜ 2D
11-13  C +3.5k / P +3.6k ｜ Activity HIGH ｜ 9D
11-20  C +1.3k / P +9.3k ｜ Activity HIGH ｜ 16D
11-27  C +0.2k / P +3.1k ｜ Activity MEDIUM △ ｜ 23D

📆 11-06 Forward Structure
存量OI: C 236.2k / P 146.6k，今日变化ΔOI: C +7.4k / P +5.5k，平值价格ATM: C $4.25 / P $4.20 ｜ ATM IV 94.8%，净 delta 敞口 252k shares
Top ΔOI: C 140 +7,148 ｜ C 135 -2,748
仓位参考: Max Pain 135 ｜ Call Wall 136（-4.0%，弱）（OI 26.5k）
量化解读： 存量 Call 重｜ATM IV 94.8%｜历史 Rank 74%（近端代理）｜IV/RV 1.36×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 251,578 股

📆 11-13 Forward Structure
存量OI: C 27.4k / P 70.0k，今日变化ΔOI: C +3.5k / P +3.6k，平值价格ATM: C $6.50 / P $7.75 ｜ ATM IV 80.7%，净 delta 敞口 71k shares
Top ΔOI: C 165 +845
仓位参考: Max Pain 152 ｜ Call Wall 150（+5.8%，弱）（OI 1.2k） ｜ Put Wall 155（+9.4%，弱）（OI 3.0k）
量化解读： 存量 Put 重｜ATM IV 80.7%｜历史 Rank 74%（近端代理）｜IV/RV 1.15×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 70,525 股

📆 11-20 Forward Structure
存量OI: C 153.4k / P 132.9k，今日变化ΔOI: C +1.3k / P +9.3k，平值价格ATM: C $9.00 / P $9.80 ｜ ATM IV 77.5%，净 delta 敞口 -36k shares
Top ΔOI: P 110 +5,784 ｜ P 150 +1,049
仓位参考: Max Pain 135 ｜ Call Wall 135（-4.7%）（OI 42.9k） ｜ Put Wall 150（+5.8%，弱）（OI 5.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 77.5%｜历史 Rank 74%（近端代理）｜IV/RV 1.11×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 35,880 股

11-27（MEDIUM △）仓位参考: Max Pain 155 ｜ Call Wall 150（+5.8%，弱）（OI 1.0k） ｜ Put Wall 140（-1.2%，弱）（OI 2.5k）

📅 事件差分（观察，非因果）: 11-06（2D）ATM IV 94.8% vs 11-13 80.7%（差 +14.1pp）——覆盖 ISM 非制造业 PMI、Non Farm Payrolls、失业率、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-11-04/MSTR_morning.json