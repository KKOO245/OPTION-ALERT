# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $771.45 ｜ QQQ $732.49
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 36.2（fear）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）
⇒ 全市场个股期权存量 Put/Call = 0.75，Call 侧明显更重，815 个结算日中只高于 12% 的交易日，处于历史低位区间
⇒ 全市场指数期权存量 Put/Call = 0.94，接近均衡略偏 Call，815 个结算日中只高于 11% 的交易日，处于历史低位区间

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

📌 数据来源：全部更新自 2026-10-14

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 10-14 08:30　【高】Core Inflation Rate MoM　预测 0.2 ｜ 实际 0.3 ｜ 前值 0.3　✅ 今日已公布
- 周三 10-14 08:30　【高】Core Inflation Rate YoY　预测 2.5 ｜ 实际 2.6 ｜ 前值 2.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate YoY　预测 3.6 ｜ 实际 3.7 ｜ 前值 3.4　✅ 今日已公布
- 周三 10-14 08:30　【高】Inflation Rate MoM　预测 0.6 ｜ 实际 0.6 ｜ 前值 0.4　✅ 今日已公布
- 周四 10-15 08:30　【高】PPI 生产者物价 MoM　预测 0.5 ｜ 实际 待公布 ｜ 前值 0.4
- 周四 10-15 08:30　【高】零售销售 MoM　预测 0.3 ｜ 实际 待公布 ｜ 前值 1.2
- 周四 10-15 23:30　【高】美联储主席讲话 Warsh Speech　实际 待公布

🔍 重点速览
🟡 **近现价集中开仓**: 10-16 140C ΔOI -1,799（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NOW

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NOW  昨收 138.61 → 今开 139.49（+0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 142.80 ｜ 低 138.90

Options: P/C成交量 0.41 | OI比 0.81 | ATM IV 60.1% | Skew -1.7pp | Term 1.02 | ExpMove ±3.6%（近端） | Rank 69%
量化视角： IV 中性（Rank 69%）｜期限结构正常（Term 1.02）｜Put 保护异常便宜（Skew -1.7pp，Put IV < Call IV）｜存量 Call 偏重（OI比 0.81）——观察点，非方向信号
   ⇒ Put/Call Volume: 0.41×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.81×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±3.6% ｜ 10-23（9D）±6.5% ｜ 10-30（16D）±11.2% ｜ 11-06（23D）±14.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 18,771,931 | GEX Change vs 上次快照 3,609,277 | Flip: Primary Flip: 134.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 543 / LOW 28 / INVALID 67
结构观察区: Primary Flip 134.86（全链重定价，覆盖 100%）
Call Wall 150（现价低于该位 6.5%）
最近结构参考: Flip 135（现价高于该位 4.0%）
量化视角： 正 Gamma（1877万，无历史分位）｜正 Gamma 增强（+361万）｜现价位于 Flip 上方 4.03%——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 132（MaxPain，仅结算参考）；上方 150（Call Wall）。
• Gamma 区域：切换参考 135（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-30 130.0P — Vol 917 | 最新价 $4.50 | OI 679→1449 (ΔOI +770张) | ΔOI/Volume 84.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增770张（+113.4% vs前日OI），连续性待观察（方向未知）
10-16 142.0P — Vol 1,332 | 最新价 $5.25 | OI 203→857 (ΔOI +654张) | ΔOI/Volume 49.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增654张（+322.2% vs前日OI），连续性待观察（方向未知）
10-16 137.0P — Vol 898 | 最新价 $2.35 | OI 524→1139 (ΔOI +615张) | ΔOI/Volume 68.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增615张（+117.4% vs前日OI），连续性待观察（方向未知）
10-30 160.0C — Vol 1,093 | 最新价 $2.11 | OI 578→1034 (ΔOI +456张) | ΔOI/Volume 41.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增456张（+78.9% vs前日OI），连续性待观察（方向未知）
10-16 148.0C — Vol 945 | 最新价 $0.50 | OI 1030→1475 (ΔOI +445张) | ΔOI/Volume 47.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增445张（+43.2% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 2,940 张（Put 2,039 / Call 901），跨 2 个期限｜近端保护（2 档，距现价 ≤5%，权利金合计约 $1M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C -0.9k / P +2.4k ｜ Activity MEDIUM △ ｜ 2D
10-23  C +0.9k / P +1.2k ｜ Activity HIGH ｜ 9D
10-30  C +1.1k / P +1.1k ｜ Activity MEDIUM △ ｜ 16D
11-06  C +0.4k / P +0.4k ｜ Activity MEDIUM △ ｜ 23D

📆 10-16 Forward Structure
存量OI: C 87.4k / P 70.5k，今日变化ΔOI: C -0.9k / P +2.4k，平值价格ATM: C $2.38 / P $2.73 ｜ ATM IV 60.1%，净 delta 敞口 -208k shares
Top ΔOI: C 140 -1,799 ｜ P 142 +654 ｜ P 137 +615
仓位参考: Max Pain 132 ｜ Call Wall 150（+6.9%）（OI 15.3k） ｜ Put Wall 130（-7.3%，弱）（OI 5.0k）
量化解读： 存量 Call 重｜⚠️ 背离：存量 Call 重但当日 Put 增仓更多｜ATM IV 60.1%｜历史 Rank 69%（近端代理）｜IV/RV 2.19×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 208,070 股

📆 10-23 Forward Structure
存量OI: C 19.6k / P 20.4k，今日变化ΔOI: C +0.9k / P +1.2k，平值价格ATM: C $4.75 / P $4.37 ｜ ATM IV 51.5%，净 delta 敞口 -12k shares
Top ΔOI: C 140 +351 ｜ P 139 +241
仓位参考: Max Pain 136 ｜ Call Wall 145（+3.4%，弱）（OI 1.5k） ｜ Put Wall 130（-7.3%，弱）（OI 0.7k）
量化解读： 存量两侧均衡｜ATM IV 51.5%｜历史 Rank 69%（近端代理）｜IV/RV 1.88×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 12,320 股

10-30（MEDIUM △）Top ΔOI: 130P +770 ｜ 160C +456
10-30（MEDIUM △）仓位参考: Max Pain 135 ｜ Call Wall 150（+6.9%，弱）（OI 1.0k） ｜ Put Wall 130（-7.3%，弱）（OI 1.4k）

11-06（MEDIUM △）Top ΔOI: 131P +63
11-06（MEDIUM △）仓位参考: Max Pain 140 ｜ Call Wall 150（+6.9%，弱）（OI 0.3k） ｜ Put Wall 140（-0.2%）（OI 0.5k）

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 60.1% vs 10-23 51.5%（差 +8.6pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/NOW_morning.json