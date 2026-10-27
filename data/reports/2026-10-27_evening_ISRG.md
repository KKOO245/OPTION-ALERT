# 期权晚报 2026-10-27（快照 16:40 ET）

📊 市场环境

SPY $769.66 ｜ QQQ $721.25
VIX 17.52 ↓4.7%（5D +1.2%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 32.7（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-27

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 10-27 08:30　【高】耐用品订单 Orders MoM　预测 1.5 ｜ 实际 1.8 ｜ 前值 0.1　✅ 今日已公布
- 周三 10-28 14:00　【高】美联储议息会议 Statement　实际 待公布
- 周三 10-28 14:00　【高】美联储利率决议 Decision　预测 4 ｜ 实际 待公布 ｜ 前值 4
- 周三 10-28 14:30　【高】Fed Press Conference　实际 待公布
- 周四 10-29 08:30　【高】PCE 物价 Price Index MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2
- 周四 10-29 08:30　【高】Personal Spending MoM　预测 0.6 ｜ 实际 待公布 ｜ 前值 0.9
- 周四 10-29 08:30　【高】GDP 增速 Rate QoQ Adv　预测 3.2 ｜ 实际 待公布 ｜ 前值 2.2
- 周四 10-29 08:30　【高】Personal Income MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 0.2

🔍 重点速览
🟡 **近现价集中开仓**: 11-20 452P ΔOI +123（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## ISRG

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
ISRG: 今开 451.63 → 收盘 445.88（-1.3%） ｜ 今日高 451.63 ｜ 低 443.85 ｜ 昨收 451.63 → 收盘 445.88（-1.3%）
Target 状态: 无待验证 Target（今日无 Setup 触发）

Options: P/C成交量 0.73 | OI比 0.88 | ATM IV 44.3% | Skew 4.8pp | Term 0.73 | ExpMove ±2.9%（近端） | Rank 73%
量化视角： IV 中性（Rank 73%）｜期限结构倒挂（Term 0.73，近月 IV 高于远月）｜保护溢价中性（Skew 4.8pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.88×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-30（3D）±2.9% ｜ 11-06（10D）±3.4% ｜ 11-13（17D）±6.7% ｜ 11-20（24D）±6.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 2,122,234 | GEX Change vs 上次快照 -11,180 | Flip: Primary Flip: 417.73（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 283 / LOW 177 / INVALID 524
结构观察区: Primary Flip 417.73（全链重定价，覆盖 93%）
Call Wall 420（弱结构｜现价高于该位 6.2%）
最近结构参考: Call Wall 420（现价高于该位 6.2%）
量化视角： 正 Gamma（212万，无历史分位）｜正 Gamma 减弱（1万）｜现价位于 Flip 上方 6.74%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 435（MaxPain，仅结算参考） / 420（Call Wall，弱结构）。
• Gamma 区域：切换参考 418（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
11-20 427.5P — Vol 339（Yahoo补） | 最新价 $6.00 | OI 17→355 (ΔOI +338张) | ΔOI/Volume 99.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增338张（+1988.2% vs前日OI），连续性待观察（方向未知）
10-30 455.0P — Vol 12 | 最新价 $10.05 | OI 0→202 (ΔOI +202张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增202张（量数据缺失），以日内换手为主
11-06 530.0C — Vol 300（Yahoo补） | 最新价 $0.28 | OI 1→118 (ΔOI +117张) | ΔOI/Volume 39.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增117张（+11700.0% vs前日OI），连续性待观察（方向未知）
10-30 502.5C — Vol 211（Yahoo补） | 最新价 $0.39 | OI 0→100 (ΔOI +100张) | ΔOI/Volume 47.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增100张（前日OI缺失），值得跟踪（方向未知）
11-06 360.0P — Vol 305（Yahoo补） | 最新价 $0.20 | OI 14→113 (ΔOI +99张) | ΔOI/Volume 32.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增99张（+707.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 856 张（Put 639 / Call 217），跨 3 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $0M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-30  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 3D
11-06  C +43 / P +64 ｜ Activity HIGH ｜ 10D
11-13  C +82 / P +11 ｜ Activity MEDIUM △ ｜ 17D
11-20  C +60 / P +0.1k ｜ Activity MEDIUM △ ｜ 24D

📆 10-30 Forward Structure
存量OI: C 2.4k / P 2.1k，今日变化ΔOI: C +0.1k / P +0.2k，平值价格ATM: C $6.73 / P $6.10 ｜ ATM IV 44.3%，净 delta 敞口 -5k shares
Top ΔOI: P 435 +63 ｜ C 472 +60 ｜ P 425 +44
仓位参考: Max Pain 435 ｜ Call Wall 450（+0.9%，弱）（OI 0.2k） ｜ Put Wall 455（+2.0%）（OI 0.2k）
量化解读： 存量两侧均衡｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 44.3%｜历史 Rank 73%（近端代理）｜IV/RV 1.82×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 5,341 股

📆 11-06 Forward Structure
存量OI: C 1.2k / P 0.7k，今日变化ΔOI: C +43 / P +64，平值价格ATM: C $15.04 / P $0.00 ｜ ATM IV 35.8%，净 delta 敞口 -638 shares
Top ΔOI: P 412 +40 ｜ P 420 +11
仓位参考: Max Pain 428 ｜ Call Wall 430（-3.6%，弱）（OI 0.1k） ｜ Put Wall 450（+0.9%，弱）（OI 64）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 35.8%｜历史 Rank 73%（近端代理）｜IV/RV 1.47×（近似）｜期限倒挂（近端 IV > 远月）｜净 delta 敞口 负 638 股

11-13（MEDIUM △）Top ΔOI: 440C +75
11-13（MEDIUM △）仓位参考: Max Pain 430 ｜ Call Wall 440（-1.3%，弱）（OI 0.1k） ｜ Put Wall 420（-5.8%，弱）（OI 80）

11-20（MEDIUM △）Top ΔOI: 452P +123
11-20（MEDIUM △）仓位参考: Max Pain 400 ｜ Call Wall 420（-5.8%，弱）（OI 0.8k） ｜ Put Wall 410（-8.0%，弱）（OI 0.4k）

📅 事件差分（观察，非因果）: 10-30（3D）ATM IV 44.3% vs 11-06 35.8%（差 +8.5pp）——覆盖 耐用品订单 Orders MoM、美联储议息会议 Statement 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-27/ISRG_evening.json