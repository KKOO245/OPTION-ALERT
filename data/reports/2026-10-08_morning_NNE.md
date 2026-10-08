# 期权晨报 2026-10-08（快照 10:20 ET）

📊 市场环境

SPY $775.90 ｜ QQQ $755.92
VIX 15.43 ↑2.3%（5D -5.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 41.9（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-08

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 10-09 10:00　【高】密歇根消费者信心 Consumer Sentiment Prel　预测 47.6 ｜ 实际 待公布 ｜ 前值 48.1

🔍 重点速览
🟡 **近现价集中开仓**: 10-09 15P ΔOI +197（距现价 -2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 16.01 → 今开 15.78（-1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 15.93 ｜ 低 15.66

Options: P/C成交量 1.33 | OI比 0.36 | ATM IV 73.7% | Skew -14.2pp | Term 0.95 | ExpMove ±4.4%（近端） | Rank 5%
量化视角： IV 历史低位（Rank 5%，期权偏便宜）｜期限结构正常（Term 0.95）｜Put 保护异常便宜（Skew -14.2pp，Put IV < Call IV）｜⚠️ 重点观察：存量 Call 重（OI比 0.36）+ 当日成交偏 Put（P/C量 1.33）——结构背离，买/卖方向不可观测——观察点，非方向信号
   ⇒ Put/Call Volume: 1.33×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.36×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 10-09（1D）±4.4% ｜ 10-16（8D）±9.4% ｜ 10-23（15D）±11.4% ｜ 10-30（22D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 1,322,004 | GEX Change vs 上次快照 -487,707 | Flip: Primary Flip: 15.21（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 196 / LOW 97 / INVALID 135
结构观察区: Primary Flip 15.21（全链重定价，覆盖 91%）
Put Wall 15（弱结构｜现价高于该位 5.4%）
最近结构参考: Flip 15（现价高于该位 4.0%）
量化视角： 正 Gamma（132万，无历史分位）｜正 Gamma 减弱（49万）｜现价位于 Flip 上方 3.97%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall，弱结构）；上方 16（MaxPain，仅结算参考）。
• Gamma 区域：切换参考 15（全链重定价，覆盖 91%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-09 15.5P — Vol 203 | 最新价 $0.25 | OI 441→638 (ΔOI +197张) | ΔOI/Volume 97.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增197张（+44.7% vs前日OI），连续性待观察（方向未知）
10-16 19.0C — Vol 118 | 最新价 $0.10 | OI 1125→1214 (ΔOI +89张) | ΔOI/Volume 75.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增89张（+7.9% vs前日OI），连续性待观察（方向未知）
10-16 17.0C — Vol 90 | 最新价 $0.33 | OI 1111→1175 (ΔOI +64张) | ΔOI/Volume 71.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增64张（+5.8% vs前日OI），连续性待观察（方向未知）
10-09 16.5C — Vol 113 | 最新价 $0.20 | OI 408→456 (ΔOI +48张) | ΔOI/Volume 42.5% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增48张（+11.8% vs前日OI），值得跟踪（方向未知）
10-09 15.0P — Vol 49 | 最新价 $0.09 | OI 413→456 (ΔOI +43张) | ΔOI/Volume 87.8% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增43张（+10.4% vs前日OI），值得跟踪（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 441 张（Put 240 / Call 201），跨 2 个期限｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-09  C -4 / P +0.2k ｜ Activity HIGH ｜ 1D
10-16  C +0.1k / P +17 ｜ Activity MEDIUM △ ｜ 8D
10-23  C +37 / P +40 ｜ Activity MEDIUM △ ｜ 15D
10-30  C +19 / P +29 ｜ Activity MEDIUM △ ｜ 22D

📆 10-09 Forward Structure
存量OI: C 7.8k / P 2.8k，今日变化ΔOI: C -4 / P +0.2k，平值价格ATM: C $0.29 / P $0.40 ｜ ATM IV 73.7%，净 delta 敞口 2k shares
Top ΔOI: P 15 +197 ｜ C 16 +48
仓位参考: Max Pain 16 ｜ Put Wall 15.5（-2.0%，弱）（OI 0.6k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 73.7%｜历史 Rank 5%（近端代理）｜IV/RV 1.21×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,750 股

10-16（MEDIUM △）Top ΔOI: 17C +64
10-16（MEDIUM △）仓位参考: Max Pain 18 ｜ Call Wall 17（+7.5%，弱）（OI 1.2k） ｜ Put Wall 15（-5.1%，弱）（OI 0.9k）

10-23（MEDIUM △）Top ΔOI: 17C +12
10-23（MEDIUM △）仓位参考: Max Pain 17 ｜ Put Wall 16（+1.2%，弱）（OI 0.2k）

10-30（MEDIUM △）Top ΔOI: 17C +11 ｜ 15C +9
10-30（MEDIUM △）仓位参考: Max Pain 16 ｜ Put Wall 15（-5.1%，弱）（OI 89）

📅 事件差分（观察，非因果）: 10-09（1D）ATM IV 73.7% vs 10-16 64.8%（差 +8.9pp）——覆盖 密歇根消费者信心 Consumer Sentiment Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-08/NNE_morning.json