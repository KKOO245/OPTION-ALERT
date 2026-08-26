# 期权晨报 2026-08-26

📊 市场环境

SPY $769.88 ｜ QQQ $711.37
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


## SNDK

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: +2.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 08-28 1500P ΔOI +900（距现价 -0.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,482.76 → 今晨 1,504.02（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 1510.84 ｜ 低 1450.05

Options: P/C量 0.54 | OI比 0.76 | ATM IV 89.7% | Skew -1.2pp | Term 0.85 | ExpMove ±5.5%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.54×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（2D）±5.5% ｜ 09-04（9D）±10.3% ｜ 09-11（16D）±12.7% ｜ 09-18（23D）±15.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Candidates 1661.30 / 1799.35 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 Top-3 近似 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: 待审计
结构观察区: 1661–1799（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 800: +88.0% | 距 Call Wall 1,700: -11.5%
最近结构参考: Flip 1661（距现价 -9.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 800（Put Wall）；上方 1,700（Call Wall）。
• Gamma 区域：切换参考 1661（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 1700.0C — Vol N/A | OI 5187→6535 (ΔOI +1348张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增1348张（+26.0% vs前日OI），连续性待观察（方向未知）
08-28 1500.0P — Vol N/A | OI 1419→2319 (ΔOI +900张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增900张（+63.4% vs前日OI），连续性待观察（方向未知）
09-04 1265.0P — Vol N/A | OI 5→879 (ΔOI +874张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增874张（+17480.0% vs前日OI），连续性待观察（方向未知）
09-04 1710.0C — Vol N/A | OI 17→889 (ΔOI +872张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增872张（+5129.4% vs前日OI），连续性待观察（方向未知）
09-04 1440.0P — Vol N/A | OI 21→886 (ΔOI +865张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增865张（+4119.1% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +8.4k / P +5.1k ｜ Activity HIGH ｜ 2D
09-04  C +2.9k / P +2.9k ｜ Activity HIGH ｜ 9D
09-11  C +0.4k / P +0.3k ｜ Activity HIGH ｜ 16D
09-18  C +1.6k / P +0.5k ｜ Activity HIGH ｜ 23D

📆 08-28 Forward Structure
OI:       C 65.3k / P 49.9k
ΔOI:      C +8.4k / P +5.1k
ATM:      C 41.00 / P 42.00
ATM IV:   89.7%
ΔOI Δ Exposure*: 43k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1700 ｜ +1,348 ｜ $2.80 ｜ 名义 $377.4k* ｜ +13.0%
P 1500 ｜ +900 ｜ $39.40 ｜ 名义 $3.55M* ｜ -0.3%
C 1800 ｜ +566 ｜ $0.81 ｜ 名义 $45.8k* ｜ +19.7%
结构参考：1700（+13.0%）上方 / 1500（-0.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 17.1k / P 16.7k
ΔOI:      C +2.9k / P +2.9k
ATM:      C 73.63 / P 81.25
ATM IV:   80.1%
ΔOI Δ Exposure*: -339 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1265 ｜ +874 ｜ $7.56 ｜ 名义 $660.7k* ｜ -15.9%
C 1710 ｜ +872 ｜ $16.90 ｜ 名义 $1.47M* ｜ +13.7%
P 1440 ｜ +865 ｜ $47.60 ｜ 名义 $4.12M* ｜ -4.3%
结构参考：1710（+13.7%）上方 / 1265（-15.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 4.8k / P 8.8k
ΔOI:      C +0.4k / P +0.3k
ATM:      C 92.41 / P 98.72
ATM IV:   74.9%
ΔOI Δ Exposure*: 5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1110 ｜ +60 ｜ $4.11 ｜ 名义 $24.7k* ｜ -26.2%
C 1480 ｜ +35 ｜ $107.00 ｜ 名义 $374.5k* ｜ -1.6%
C 1500 ｜ +35 ｜ $96.50 ｜ 名义 $337.8k* ｜ -0.3%
结构参考：1110（-26.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 51.4k / P 68.2k
ΔOI:      C +1.6k / P +0.5k
ATM:      C 115.95 / P 111.12
ATM IV:   75.3%
ΔOI Δ Exposure*: 35k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1220 ｜ +320 ｜ $23.10 ｜ 名义 $739.2k* ｜ -18.9%
C 2300 ｜ +307 ｜ $2.74 ｜ 名义 $84.1k* ｜ +52.9%
C 2000 ｜ +273 ｜ $11.62 ｜ 名义 $317.2k* ｜ +33.0%
结构参考：2300（+52.9%）上方 / 1220（-18.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（2D）ATM IV 89.7% vs 09-04 80.1%（差 +9.6pp）——覆盖 Personal Spending MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM、PCE 物价 Price Index MoM、美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-26/SNDK_morning.json