# 期权晨报 2026-10-05（快照 10:20 ET）

📊 市场环境

SPY $774.83 ｜ QQQ $nan
VIX 15.75 ↑2.9%（5D -2.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 43.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-05

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周一 10-05 10:00　【高】ISM 非制造业 PMI　预测 55 ｜ 实际 54.9 ｜ 前值 55.4　✅ 今日已公布
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 46.97 → 今开 47.27（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 47.80 ｜ 低 46.46

Options: P/C成交量 0.90 | OI比 0.82 | ATM IV 61.9% | Skew -3.8pp | Term 0.92 | ExpMove ±5.3%（近端） | Rank 40%
量化视角： IV 中性（Rank 40%）｜期限结构正常（Term 0.92）｜Put 保护异常便宜（Skew -3.8pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.82）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.90×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（4D）±5.3% ｜ 10-16（11D）±8.3% ｜ 10-23（18D）±11.0% ｜ 10-30（25D）±13.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -2,157,523 | GEX Change vs 上次快照 74,201 | Flip: Primary Flip: 48.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 252 / LOW 51 / INVALID 133
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 48.68（全链重定价，覆盖 98%）
Put Wall 45（弱结构｜现价高于该位 4.5%） | Call Wall 50（弱结构｜现价低于该位 6.0%）
最近结构参考: Flip 49（现价低于该位 3.4%）
量化视角： 负 Gamma（216万，无历史分位）｜负 Gamma 缓解（+7万）｜现价位于 Flip 下方 3.42%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 45（Put Wall，弱结构）；上方 48（MaxPain，仅结算参考） / 50（Call Wall，弱结构）。
• Gamma 区域：切换参考 49（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 50.0C — Vol 804 | 最新价 $0.39 | OI 539→1006 (ΔOI +467张) | ΔOI/Volume 58.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增467张（+86.6% vs前日OI），连续性待观察（方向未知）
10-30 43.0P — Vol 331 | 最新价 $1.05 | OI 68→380 (ΔOI +312张) | ΔOI/Volume 94.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增312张（+458.8% vs前日OI），连续性待观察（方向未知）
10-09 45.5P — Vol 331 | 最新价 $0.69 | OI 80→380 (ΔOI +300张) | ΔOI/Volume 90.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增300张（+375.0% vs前日OI），连续性待观察（方向未知）
10-09 49.0C — Vol 381 | 最新价 $0.60 | OI 176→472 (ΔOI +296张) | ΔOI/Volume 77.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增296张（+168.2% vs前日OI），连续性待观察（方向未知）
10-09 52.0C — Vol 791 | 最新价 $0.14 | OI 357→577 (ΔOI +220张) | ΔOI/Volume 27.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增220张（+61.6% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 1,595 张（Put 612 / Call 983），跨 2 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +1.7k / P +0.7k ｜ Activity HIGH ｜ 4D
10-16  C +0.3k / P -2 ｜ Activity LOW ｜ 11D
10-23  C +75 / P +35 ｜ Activity LOW ｜ 18D
10-30  C +0.3k / P +0.6k ｜ Activity HIGH ｜ 25D

📆 10-09 Forward Structure
存量OI: C 8.5k / P 7.0k，今日变化ΔOI: C +1.7k / P +0.7k，平值价格ATM: C $1.05 / P $1.44 ｜ ATM IV 61.9%，净 delta 敞口 9k shares
Top ΔOI: C 50 +467 ｜ P 45 +300 ｜ C 49 +296
仓位参考: Max Pain 48 ｜ Call Wall 50（+6.4%，弱）（OI 1.0k） ｜ Put Wall 47（-0.0%）（OI 2.3k）
量化解读： 存量 Call 重｜ATM IV 61.9%｜历史 Rank 40%（近端代理）｜IV/RV 1.44×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 8,989 股

10-16（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 50（+6.4%，弱）（OI 4.0k） ｜ Put Wall 45（-4.3%，弱）（OI 4.4k）

10-23（Activity LOW）仓位参考: Max Pain 50 ｜ Call Wall 50（+6.4%，弱）（OI 0.2k） ｜ Put Wall 45（-4.3%，弱）（OI 0.2k）

📆 10-30 Forward Structure
存量OI: C 3.1k / P 2.1k，今日变化ΔOI: C +0.3k / P +0.6k，平值价格ATM: C $3.40 / P $2.83 ｜ ATM IV 56.8%，净 delta 敞口 -6k shares
Top ΔOI: P 43 +312 ｜ C 47 +110
仓位参考: Max Pain 49 ｜ Call Wall 50（+6.4%，弱）（OI 0.3k） ｜ Put Wall 43（-8.5%，弱）（OI 0.4k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 56.8%｜历史 Rank 40%（近端代理）｜IV/RV 1.32×（近似）｜净 delta 敞口 负 6,279 股

📅 事件差分（观察，非因果）: 10-09（4D）ATM IV 61.9% vs 10-16 53.8%（差 +8.1pp）——覆盖 ISM 非制造业 PMI、美联储议息会议 Minutes 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-05/MP_morning.json