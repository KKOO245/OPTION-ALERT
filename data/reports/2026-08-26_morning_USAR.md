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


## USAR

🔍 重点速览
🟡 **单日价格波动**: +3.8%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 08-28 ATM IV 102.8% vs 09-04 90.5%（差 +12.3pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 08-28 19P ΔOI +352（距现价 +3.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 19.50 → 今晨 18.93（-2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 20.52 ｜ 低 18.73

Options: P/C量 0.31 | OI比 0.56 | ATM IV 102.8% | Skew -1.1pp | Term 0.88 | ExpMove ±6.4%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.56×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（2D）±6.4% ｜ 09-04（9D）±11.2% ｜ 09-11（16D）±13.9% ｜ 09-18（23D）±17.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Candidates 6.38 / 8.74 / 21.78 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 Top-3 近似 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: 待审计
结构观察区: 6–9（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 15: +26.2% | 距 Call Wall 20: -5.3%
最近结构参考: Call Wall 20（距现价 -5.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 20（Call Wall）。
• Gamma 区域：切换参考 6（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 25.0C — Vol N/A | OI 551→1660 (ΔOI +1109张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增1109张（+201.3% vs前日OI），连续性待观察（方向未知）
09-18 20.0C — Vol N/A | OI 12167→13115 (ΔOI +948张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增948张（+7.8% vs前日OI），值得跟踪（方向未知）
09-18 21.5C — Vol N/A | OI 9→768 (ΔOI +759张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增759张（+8433.3% vs前日OI），连续性待观察（方向未知）
09-04 19.5C — Vol N/A | OI 154→890 (ΔOI +736张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增736张（+477.9% vs前日OI），连续性待观察（方向未知）
09-04 22.0C — Vol N/A | OI 762→1370 (ΔOI +608张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增608张（+79.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +2.5k / P +0.5k ｜ Activity HIGH ｜ 2D
09-04  C +2.4k / P +0.4k ｜ Activity HIGH ｜ 9D
09-11  C +0.4k / P +67 ｜ Activity HIGH ｜ 16D
09-18  C +2.1k / P +0.4k ｜ Activity HIGH ｜ 23D

📆 08-28 Forward Structure
OI:       C 20.0k / P 11.2k
ΔOI:      C +2.5k / P +0.5k
ATM:      C 0.57 / P 0.65
ATM IV:   102.8%
ΔOI Δ Exposure*: 18k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 21 ｜ +449 ｜ $0.08 ｜ 名义 $3.6k* ｜ +10.9%
P 19 ｜ +352 ｜ $0.96 ｜ 名义 $33.8k* ｜ +3.0%
C 20 ｜ +306 ｜ $0.14 ｜ 名义 $4.3k* ｜ +8.3%
结构参考：21（+10.9%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 16.5k / P 2.6k
ΔOI:      C +2.4k / P +0.4k
ATM:      C 1.01 / P 1.12
ATM IV:   90.5%
ΔOI Δ Exposure*: 62k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +736 ｜ $0.83 ｜ 名义 $61.1k* ｜ +3.0%
C 22 ｜ +608 ｜ $0.27 ｜ 名义 $16.4k* ｜ +16.2%
C 23 ｜ +369 ｜ $0.29 ｜ 名义 $10.7k* ｜ +24.1%
结构参考：19（+3.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 8.2k / P 1.7k
ΔOI:      C +0.4k / P +67
ATM:      C 1.24 / P 1.40
ATM IV:   86.7%
ΔOI Δ Exposure*: 13k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 20 ｜ +226 ｜ $1.16 ｜ 名义 $26.2k* ｜ +8.3%
C 22 ｜ +71 ｜ $0.49 ｜ 名义 $3.5k* ｜ +16.2%
C 21 ｜ +60 ｜ $0.78 ｜ 名义 $4.7k* ｜ +13.5%
结构参考：20（+8.3%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 106.9k / P 64.3k
ΔOI:      C +2.1k / P +0.4k
ATM:      C 1.53 / P 1.73
ATM IV:   87.1%
ΔOI Δ Exposure*: 68k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 20 ｜ +948 ｜ $1.26 ｜ 名义 $119.4k* ｜ +5.6%
C 21 ｜ +759 ｜ $0.87 ｜ 名义 $66.0k* ｜ +13.5%
C 25 ｜ -349 ｜ $0.30 ｜ 名义 $-10.5k* ｜ +32.0%
结构参考：20（+5.6%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（2D）ATM IV 102.8% vs 09-04 90.5%（差 +12.3pp）——覆盖 Personal Spending MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM、PCE 物价 Price Index MoM、美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-26/USAR_morning.json