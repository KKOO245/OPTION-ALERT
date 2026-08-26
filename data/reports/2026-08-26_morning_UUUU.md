# 期权晨报 2026-08-26

📊 市场环境

SPY $770.35 ｜ QQQ $711.37
VIX 15.62 ↑1.1%（5D +4.9%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 55.2（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 08-26 08:30　【高】Personal Spending MoM　预测 0.1 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周三 08-26 08:30　【高】Personal Income MoM　预测 0.2 ｜ 实际 0.4 ｜ 前值 0.2　✅ 今日已公布
- 周三 08-26 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 1.5 ｜ 实际 1.5 ｜ 前值 2.1　✅ 今日已公布
- 周三 08-26 08:30　【高】耐用品订单 Orders MoM　预测 0.5 ｜ 实际 1.1 ｜ 前值 0.5　✅ 今日已公布
- 周三 08-26 08:30　【高】PCE 物价 Price Index MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911


## UUUU

🔍 重点速览
🟡 **单日价格波动**: +4.8%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 08-28 ATM IV 86.5% vs 09-04 74.5%（差 +12.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 16C ΔOI +2,054（距现价 +2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
UUUU  昨收 16.08 → 今晨 15.59（-3.0%） | 较昨收变动（含盘初走势） ｜ 今日高 16.50 ｜ 低 15.47

Options: P/C量 0.24 | OI比 0.43 | ATM IV 86.5% | Skew -1.1pp | Term 0.86 | ExpMove ±5.3%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.24×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.43×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（2D）±5.0% ｜ 09-04（9D）±9.4% ｜ 09-11（16D）±12.7% ｜ 09-18（23D）±15.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Candidates 6.66 / 7.04 / 8.85 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 Top-3 近似 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: 待审计
结构观察区: 7–7（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 11: +41.7% | 距 Call Wall 18: -13.4%
最近结构参考: Call Wall 18（距现价 -13.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall）；上方 18（Call Wall）。
• Gamma 区域：切换参考 7（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 16.0C — Vol N/A | OI 284→2338 (ΔOI +2054张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增2054张（+723.2% vs前日OI），连续性待观察（方向未知）
08-28 18.0C — Vol N/A | OI 335→1424 (ΔOI +1089张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增1089张（+325.1% vs前日OI），连续性待观察（方向未知）
08-28 17.5C — Vol N/A | OI 679→1485 (ΔOI +806张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增806张（+118.7% vs前日OI），连续性待观察（方向未知）
08-28 16.5C — Vol N/A | OI 1254→1799 (ΔOI +545张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增545张（+43.5% vs前日OI），连续性待观察（方向未知）
09-18 16.5C — Vol N/A | OI 17→535 (ΔOI +518张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增518张（+3047.1% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +3.5k / P +0.2k ｜ Activity HIGH ｜ 2D
09-04  C +3.0k / P +0.4k ｜ Activity HIGH ｜ 9D
09-11  C +0.1k / P +0.5k ｜ Activity HIGH ｜ 16D
09-18  C +1.6k / P -12 ｜ Activity HIGH ｜ 23D

📆 08-28 Forward Structure
OI:       C 16.0k / P 6.9k
ΔOI:      C +3.5k / P +0.2k
ATM:      C 0.44 / P 0.34
ATM IV:   86.5%
ΔOI Δ Exposure*: 14k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 18 ｜ +1,089 ｜ $0.02 ｜ 名义 $2.2k* ｜ +15.5%
C 17 ｜ +806 ｜ $0.04 ｜ 名义 $3.2k* ｜ +12.3%
C 16 ｜ +545 ｜ $0.12 ｜ 名义 $6.5k* ｜ +5.8%
结构参考：18（+15.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 6.8k / P 2.5k
ΔOI:      C +3.0k / P +0.4k
ATM:      C 0.87 / P 0.60
ATM IV:   74.5%
ΔOI Δ Exposure*: 87k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 16 ｜ +2,054 ｜ $0.54 ｜ 名义 $110.9k* ｜ +2.6%
C 18 ｜ +293 ｜ $0.14 ｜ 名义 $4.1k* ｜ +15.5%
C 17 ｜ +239 ｜ $0.25 ｜ 名义 $6.0k* ｜ +12.3%
结构参考：16（+2.6%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.6k / P 2.5k
ΔOI:      C +0.1k / P +0.5k
ATM:      C 1.22 / P 0.76
ATM IV:   72.5%
ΔOI Δ Exposure*: -21k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +231 ｜ $1.00 ｜ 名义 $23.1k* ｜ +2.6%
P 15 ｜ +209 ｜ $0.54 ｜ 名义 $11.3k* ｜ -3.8%
C 15 ｜ -38 ｜ $1.71 ｜ 名义 $-6.5k* ｜ -3.8%
结构参考：16（+2.6%）上方 / 15（-3.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 18.6k / P 9.3k
ΔOI:      C +1.6k / P -12
ATM:      C 1.62 / P 0.82
ATM IV:   73.5%
ΔOI Δ Exposure*: 36k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 16 ｜ +518 ｜ $0.83 ｜ 名义 $43.0k* ｜ +5.8%
C 19 ｜ +155 ｜ $0.28 ｜ 名义 $4.3k* ｜ +21.9%
C 20 ｜ +148 ｜ $0.18 ｜ 名义 $2.7k* ｜ +28.3%
结构参考：16（+5.8%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（2D）ATM IV 86.5% vs 09-04 74.5%（差 +12.0pp）——覆盖 Personal Spending MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM、PCE 物价 Price Index MoM、美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-26/UUUU_morning.json