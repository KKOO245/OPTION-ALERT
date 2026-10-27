# 期权晨报 2026-10-26（快照 09:08 ET）

📊 市场环境

SPY $765.37 ｜ QQQ $712.20
VIX 19.22 ↓1.2%（5D +4.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 27.1（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-26

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 待公布 ｜ 前值 0
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 10-30 450P ΔOI +70（距现价 -0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
ISRG  昨收 452.29 → 今开 443.65（-1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 458.45 ｜ 低 442.56

Options: P/C成交量 0.50 | OI比 0.84 | ATM IV 37.8% | Skew -8.2pp | Term 0.83 | ExpMove ±3.6%（近端） | Rank 36%
量化视角： IV 中性（Rank 36%）｜期限结构倒挂（Term 0.83，近月 IV 高于远月）｜Put 保护异常便宜（Skew -8.2pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.84）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.50×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（4D）±3.6% ｜ 11-06（11D）±5.2% ｜ 11-13（18D）±10.1% ｜ 11-20（25D）±4.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,484,746 | GEX Change vs 上次快照 -20,101 | Flip: Primary Flip: 414.68（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 272 / LOW 170 / INVALID 486
结构观察区: Primary Flip 414.68（全链重定价，覆盖 93%）
Call Wall 420（弱结构｜现价高于该位 7.6%）
最近结构参考: Call Wall 420（现价高于该位 7.6%）
量化视角： 正 Gamma（248万，无历史分位）｜正 Gamma 减弱（2万）｜现价位于 Flip 上方 9.01%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 430（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 415（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 427.5P — Vol 339 | 最新价 $6.00 | OI 17→355 (ΔOI +338张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增338张（+1988.2% vs前日OI），连续性待观察（方向未知）
10-30 455.0P — Vol 202 | 最新价 $9.78 | OI 0→202 (ΔOI +202张) | ΔOI/Volume 100.0% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增202张（前日OI缺失），值得跟踪（方向未知）
11-06 530.0C — Vol 300 | 最新价 $0.28 | OI 1→118 (ΔOI +117张) | ΔOI/Volume 39.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增117张（+11700.0% vs前日OI），连续性待观察（方向未知）
10-30 502.5C — Vol 211 | 最新价 $0.39 | OI 0→100 (ΔOI +100张) | ΔOI/Volume 47.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增100张（前日OI缺失），值得跟踪（方向未知）
11-06 360.0P — Vol 305 | 最新价 $0.20 | OI 14→113 (ΔOI +99张) | ΔOI/Volume 32.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增99张（+707.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 856 张（Put 639 / Call 217），跨 3 个期限｜近端保护（1 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.4k / P +0.4k ｜ Activity HIGH ｜ 4D
11-06  C +0.3k / P +0.1k ｜ Activity HIGH ｜ 11D
11-13  C +44 / P +37 ｜ Activity MEDIUM △ ｜ 18D
11-20  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 10-30 Forward Structure
存量OI: C 2.3k / P 1.9k，今日变化ΔOI: C +0.4k / P +0.4k，平值价格ATM: C $8.40 / P $7.90 ｜ ATM IV 37.8%，净 delta 敞口 -10k shares
Top ΔOI: P 455 +202 ｜ P 450 +70
仓位参考: Max Pain 430 ｜ Call Wall 450（-0.5%，弱）（OI 0.2k） ｜ Put Wall 455（+0.7%）（OI 0.2k）
量化解读： 存量 Call 重｜ATM IV 37.8%｜历史 Rank 36%（近端代理）｜IV/RV 1.38×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 10,186 股

📆 11-06 Forward Structure
存量OI: C 1.1k / P 0.7k，今日变化ΔOI: C +0.3k / P +0.1k，平值价格ATM: C $13.02 / P $10.50 ｜ ATM IV 34.1%，净 delta 敞口 2k shares
仓位参考: Max Pain 425 ｜ Call Wall 430（-4.9%，弱）（OI 0.1k） ｜ Put Wall 450（-0.5%，弱）（OI 64）
量化解读： 存量 Call 重｜ATM IV 34.1%｜历史 Rank 36%（近端代理）｜IV/RV 1.25×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 正 1,583 股

11-13（MEDIUM △）Top ΔOI: 410C +14
11-13（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 435（-3.8%）（OI 0.1k） ｜ Put Wall 420（-7.1%，弱）（OI 80）

11-20（MEDIUM △）Top ΔOI: 427P +338 ｜ 480C +74
11-20（MEDIUM △）仓位参考: Max Pain 400 ｜ Call Wall 420（-7.1%，弱）（OI 0.8k） ｜ Put Wall 410（-9.3%，弱）（OI 0.4k）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-26/ISRG_morning.json