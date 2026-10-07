# 期权晨报 2026-10-07（快照 10:20 ET）

📊 市场环境

SPY $777.04 ｜ QQQ $757.73
VIX 15.79 ↑5.2%（5D -3.4%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 44.6（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-07

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-07 14:00　【高】美联储议息会议 Minutes　实际 待公布　✅ 今日已公布
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 295P ΔOI +702（距现价 +1.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 295.78 → 今开 286.00（-3.3%） | 较昨收变动（含盘初走势） ｜ 今日高 296.83 ｜ 低 284.54

Options: P/C成交量 0.72 | OI比 1.13 | ATM IV 77.8% | Skew -2.8pp | Term 1.04 | ExpMove ±4.9%（近端） | Rank 35%
量化视角： IV 中性（Rank 35%）｜期限结构正常（Term 1.04）｜Put 保护异常便宜（Skew -2.8pp，Put IV < Call IV）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.72×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.13×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-09（2D）±4.9% ｜ 10-16（9D）±8.5% ｜ 10-23（16D）±11.2% ｜ 10-30（23D）±14.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 8,173,115 | GEX Change vs 上次快照 -4,388,502 | Flip: Primary Flip: 278.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 611 / LOW 89 / INVALID 162
结构观察区: Primary Flip 278.73（全链重定价，覆盖 100%）
Call Wall 300（弱结构｜现价低于该位 3.5%）
最近结构参考: Call Wall 300（现价低于该位 3.5%）
量化视角： 正 Gamma（817万，无历史分位）｜正 Gamma 减弱（439万）｜现价位于 Flip 上方 3.91%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 282（MaxPain，仅结算参考）；上方 300（Call Wall，弱结构）。
• Gamma 区域：切换参考 279（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 310.0C — Vol 5,138 | 最新价 $2.93 | OI 1531→2644 (ΔOI +1113张) | ΔOI/Volume 21.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1113张（+72.7% vs前日OI），连续性待观察（方向未知）
10-16 300.0P — Vol 1,071 | 最新价 $14.90 | OI 1074→1781 (ΔOI +707张) | ΔOI/Volume 66.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增707张（+65.8% vs前日OI），连续性待观察（方向未知）
10-09 295.0P — Vol 2,116 | 最新价 $7.29 | OI 397→1099 (ΔOI +702张) | ΔOI/Volume 33.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增702张（+176.8% vs前日OI），连续性待观察（方向未知）
10-16 312.5C — Vol 727 | 最新价 $8.48 | OI 25→563 (ΔOI +538张) | ΔOI/Volume 74.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增538张（+2152.0% vs前日OI），连续性待观察（方向未知）
10-09 305.0C — Vol 2,204 | 最新价 $4.35 | OI 956→1476 (ΔOI +520张) | ΔOI/Volume 23.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增520张（+54.4% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 3,580 张（Put 1,409 / Call 2,171），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C +3.9k / P +3.1k ｜ Activity HIGH ｜ 2D
10-16  C +2.5k / P +2.3k ｜ Activity HIGH ｜ 9D
10-23  C +0.8k / P +0.1k ｜ Activity MEDIUM △ ｜ 16D
10-30  C +0.6k / P +0.2k ｜ Activity MEDIUM △ ｜ 23D

📆 10-09 Forward Structure
存量OI: C 35.4k / P 40.0k，今日变化ΔOI: C +3.9k / P +3.1k，平值价格ATM: C $6.98 / P $7.15 ｜ ATM IV 77.8%，净 delta 敞口 -125k shares
Top ΔOI: C 310 +1,113 ｜ P 295 +702 ｜ C 305 +520
仓位参考: Max Pain 282 ｜ Call Wall 300（+3.6%，弱）（OI 2.9k） ｜ Put Wall 280（-3.3%，弱）（OI 2.1k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 77.8%｜历史 Rank 35%（近端代理）｜IV/RV 1.09×（近似）｜净 delta 敞口 负 125,484 股

📆 10-16 Forward Structure
存量OI: C 80.4k / P 91.3k，今日变化ΔOI: C +2.5k / P +2.3k，平值价格ATM: C $12.65 / P $11.93 ｜ ATM IV 68.2%，净 delta 敞口 -80k shares
Top ΔOI: P 300 +707 ｜ C 312 +538 ｜ P 282 +513
仓位参考: Max Pain 270 ｜ Call Wall 270（-6.8%，弱）（OI 7.5k） ｜ Put Wall 275（-5.1%，弱）（OI 3.4k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Put 重但当日 Call 增仓更多｜ATM IV 68.2%｜历史 Rank 35%（近端代理）｜IV/RV 0.96×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 79,789 股

10-23（MEDIUM △）Top ΔOI: 315C +200
10-23（MEDIUM △）仓位参考: Max Pain 270 ｜ Call Wall 300（+3.6%，弱）（OI 1.1k） ｜ Put Wall 280（-3.3%，弱）（OI 0.7k）

10-30（MEDIUM △）Top ΔOI: 320C +250 ｜ 350C +108
10-30（MEDIUM △）仓位参考: Max Pain 285 ｜ Call Wall 300（+3.6%，弱）（OI 1.3k） ｜ Put Wall 285（-1.6%，弱）（OI 1.8k）

📅 事件差分（观察，非因果）: 10-09（2D）ATM IV 77.8% vs 10-16 68.2%（差 +9.6pp）——覆盖 美联储议息会议 Minutes、密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-07/BE_morning.json