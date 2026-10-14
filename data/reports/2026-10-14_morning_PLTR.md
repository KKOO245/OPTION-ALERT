# 期权晨报 2026-10-14（快照 10:20 ET）

📊 市场环境

SPY $773.15 ｜ QQQ $736.47
VIX 15.81 ↑3.5%（5D +4.8%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 38.8（fear）
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
🟡 **近现价集中开仓**: 10-16 207P ΔOI +3,306（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## PLTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
PLTR  昨收 208.67 → 今开 207.36（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 209.28 ｜ 低 204.41

Options: P/C成交量 0.95 | OI比 1.17 | ATM IV 49.7% | Skew 2.5pp | Term 1.16 | ExpMove ±3.1%（近端） | Rank 60%
量化视角： IV 中性（Rank 60%）｜期限结构正常偏陡（Term 1.16）｜保护溢价中性（Skew 2.5pp）｜当日成交与存量接近均衡——观察点，非方向信号
   ⇒ Put/Call Volume: 0.95×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 10-16（2D）±3.1% ｜ 10-23（9D）±5.5% ｜ 10-30（16D）±7.4% ｜ 11-06（23D）±12.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 82,278,656 | GEX Change vs 上次快照 -15,009,689 | Flip: Primary Flip: 192.23（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 663 / LOW 60 / INVALID 189
结构观察区: Primary Flip 192.23（全链重定价，覆盖 100%）
Call Wall 220（弱结构｜现价低于该位 5.5%）
最近结构参考: Call Wall 220（现价低于该位 5.5%）
量化视角： 正 Gamma（8228万，无历史分位）｜正 Gamma 减弱（1501万）｜现价位于 Flip 上方 8.11%｜⚠️ 重点观察：正 Gamma 由正转负（结构切换）——观察点，非方向信号
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 185（MaxPain，仅结算参考）；上方 220（Call Wall，弱结构）。
• Gamma 区域：切换参考 192（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-16 207.5P — Vol 17,181 | 最新价 $2.89 | OI 4175→7481 (ΔOI +3306张) | ΔOI/Volume 19.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3306张（+79.2% vs前日OI），连续性待观察（方向未知）
10-16 205.0P — Vol 17,132 | 最新价 $1.95 | OI 4519→6835 (ΔOI +2316张) | ΔOI/Volume 13.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2316张（+51.2% vs前日OI），连续性待观察（方向未知）
10-16 200.0P — Vol 13,972 | 最新价 $0.76 | OI 7415→9248 (ΔOI +1833张) | ΔOI/Volume 13.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1833张（+24.7% vs前日OI），连续性待观察（方向未知）
10-16 210.0P — Vol 10,191 | 最新价 $4.13 | OI 1838→3362 (ΔOI +1524张) | ΔOI/Volume 14.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1524张（+82.9% vs前日OI），连续性待观察（方向未知）
10-16 217.5C — Vol 6,769 | 最新价 $0.78 | OI 868→2292 (ΔOI +1424张) | ΔOI/Volume 21.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1424张（+164.1% vs前日OI），连续性待观察（方向未知）
量化视角： 5 个事件合计 ΔOI ≈ 10,403 张（Put 8,979 / Call 1,424），跨 1 个期限｜近端保护（4 档，距现价 ≤5%，权利金合计约 $2M，买/卖方向不可观测）｜Put 增仓为主（孤立/局部，暂不构成模式推断）——方向未知，观察连续性，观察点，非方向信号
📆 Forward Expiration Structure

10-16  C -5.8k / P +11.6k ｜ Activity HIGH ｜ 2D
10-23  C +3.4k / P +4.2k ｜ Activity HIGH ｜ 9D
10-30  C +1.7k / P +1.2k ｜ Activity HIGH ｜ 16D
11-06  C +1.1k / P +1.0k ｜ Activity MEDIUM △ ｜ 23D

📆 10-16 Forward Structure
存量OI: C 232.1k / P 270.7k，今日变化ΔOI: C -5.8k / P +11.6k，平值价格ATM: C $2.96 / P $3.50 ｜ ATM IV 49.7%，净 delta 敞口 -1.3M shares
Top ΔOI: C 185 -5,269 ｜ P 207 +3,306 ｜ P 205 +2,316
仓位参考: Max Pain 185 ｜ Call Wall 220（+5.9%，弱）（OI 17.7k） ｜ Put Wall 200（-3.8%，弱）（OI 9.2k）
量化解读： 存量两侧均衡｜ATM IV 49.7%｜历史 Rank 60%（近端代理）｜IV/RV 2.00×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 1,289,359 股

📆 10-23 Forward Structure
存量OI: C 42.7k / P 57.9k，今日变化ΔOI: C +3.4k / P +4.2k，平值价格ATM: C $6.10 / P $5.40 ｜ ATM IV 43.2%，净 delta 敞口 -30k shares
Top ΔOI: C 222 +628 ｜ C 210 +528 ｜ C 217 +510
仓位参考: Max Pain 192 ｜ Call Wall 220（+5.9%，弱）（OI 4.3k） ｜ Put Wall 200（-3.8%，弱）（OI 2.6k）
量化解读： 存量 Put 重｜ATM IV 43.2%｜历史 Rank 60%（近端代理）｜IV/RV 1.74×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 负 30,131 股

📆 10-30 Forward Structure
存量OI: C 37.9k / P 36.5k，今日变化ΔOI: C +1.7k / P +1.2k，平值价格ATM: C $7.90 / P $7.50 ｜ ATM IV 43.1%，净 delta 敞口 17k shares
Top ΔOI: C 220 +308 ｜ C 215 +291 ｜ P 190 +257
仓位参考: Max Pain 192 ｜ Call Wall 205（-1.4%，弱）（OI 3.1k） ｜ Put Wall 190（-8.6%，弱）（OI 3.5k）
量化解读： 存量两侧均衡｜ATM IV 43.1%｜历史 Rank 60%（近端代理）｜IV/RV 1.73×（近似）｜期限正常（远月高于近端）｜净 delta 敞口 正 16,866 股

11-06（MEDIUM △）Top ΔOI: 205P +161
11-06（MEDIUM △）仓位参考: Max Pain 192 ｜ Call Wall 220（+5.9%，弱）（OI 1.4k） ｜ Put Wall 190（-8.6%）（OI 2.9k）

📅 事件差分（观察，非因果）: 10-16（2D）ATM IV 49.7% vs 10-23 43.2%（差 +6.5pp）——覆盖 Core Inflation Rate MoM、Core Inflation Rate YoY、Inflation Rate YoY、Inflation Rate MoM、PPI 生产者物价 MoM、零售销售 MoM、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-10-14/PLTR_morning.json