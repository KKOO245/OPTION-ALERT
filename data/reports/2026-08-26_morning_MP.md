# 期权晨报 2026-08-26

📊 市场环境

SPY $769.98 ｜ QQQ $711.37
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


## MP

🔍 重点速览
🟡 **单日价格波动**: +3.1%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 08-28 62C ΔOI +2,258（距现价 +4.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 57.0 / 59.5 / 59.7）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 60.34 → 今晨 59.26（-1.8%） | 较昨收变动（含盘初走势） ｜ 今日高 62.45 ｜ 低 58.56

Options: P/C量 0.32 | OI比 0.51 | ATM IV 81.2% | Skew -2.3pp | Term 0.82 | ExpMove ±5.1%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（2D）±5.0% ｜ 09-04（9D）±9.4% ｜ 09-11（16D）±12.0% ｜ 09-18（23D）±16.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Candidates 57.01 / 59.48 / 59.74 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 Top-3 近似 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: 待审计
结构观察区: 57–59（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 55: +7.7% | 距 Call Wall 70: -15.3%
最近结构参考: Flip 59（距现价 -0.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall）；上方 70（Call Wall）。
• Gamma 区域：切换参考 57（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 62.0C — Vol N/A | OI 413→2671 (ΔOI +2258张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增2258张（+546.7% vs前日OI），连续性待观察（方向未知）
08-28 70.0C — Vol N/A | OI 887→1586 (ΔOI +699张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增699张（+78.8% vs前日OI），连续性待观察（方向未知）
08-28 54.0P — Vol N/A | OI 372→755 (ΔOI +383张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增383张（+103.0% vs前日OI），值得跟踪（方向未知）
08-28 69.0C — Vol N/A | OI 81→307 (ΔOI +226张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增226张（+279.0% vs前日OI），值得跟踪（方向未知）
09-04 53.0P — Vol N/A | OI 134→359 (ΔOI +225张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: LOW
   ⇒ 净增225张（+167.9% vs前日OI），值得跟踪（方向未知）
📆 Forward Expiration Structure

08-28  C +3.9k / P +0.4k ｜ Activity HIGH ｜ 2D
09-04  C +0.9k / P +0.7k ｜ Activity HIGH ｜ 9D
09-11  C +0.1k / P +78 ｜ Activity HIGH ｜ 16D
09-18  C +0.6k / P +12 ｜ Activity HIGH ｜ 23D

📆 08-28 Forward Structure
OI:       C 16.9k / P 8.7k
ΔOI:      C +3.9k / P +0.4k
ATM:      C 1.75 / P 1.24
ATM IV:   81.2%
ΔOI Δ Exposure*: 75k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 62 ｜ +2,258 ｜ $0.65 ｜ 名义 $146.8k* ｜ +4.6%
C 70 ｜ +699 ｜ $0.05 ｜ 名义 $3.5k* ｜ +18.1%
P 54 ｜ +383 ｜ $0.17 ｜ 名义 $6.5k* ｜ -8.9%
结构参考：62（+4.6%）上方 / 54（-8.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 6.6k / P 5.1k
ΔOI:      C +0.9k / P +0.7k
ATM:      C 2.75 / P 2.83
ATM IV:   72.1%
ΔOI Δ Exposure*: 9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 53 ｜ +225 ｜ $0.53 ｜ 名义 $11.9k* ｜ -10.6%
P 60 ｜ +172 ｜ $2.10 ｜ 名义 $36.1k* ｜ +1.2%
C 60 ｜ +135 ｜ $2.53 ｜ 名义 $34.2k* ｜ +1.2%
结构参考：60（+1.2%）上方 / 53（-10.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.5k / P 3.0k
ΔOI:      C +0.1k / P +78
ATM:      C 4.00 / P 3.13
ATM IV:   68.3%
ΔOI Δ Exposure*: 863 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 53 ｜ +28 ｜ $0.98 ｜ 名义 $2.7k* ｜ -10.6%
C 58 ｜ +24 ｜ $3.96 ｜ 名义 $9.5k* ｜ -2.1%
C 65 ｜ +23 ｜ $1.52 ｜ 名义 $3.5k* ｜ +9.7%
结构参考：65（+9.7%）上方 / 53（-10.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 47.0k / P 44.3k
ΔOI:      C +0.6k / P +12
ATM:      C 5.63 / P 4.00
ATM IV:   68.1%
ΔOI Δ Exposure*: 4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 55 ｜ -324 ｜ $7.31 ｜ 名义 $-236.8k* ｜ -7.2%
C 60 ｜ +202 ｜ $3.95 ｜ 名义 $79.8k* ｜ +1.2%
C 75 ｜ +186 ｜ $0.55 ｜ 名义 $10.2k* ｜ +26.6%
结构参考：60（+1.2%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（2D）ATM IV 81.2% vs 09-04 72.1%（差 +9.1pp）——覆盖 Personal Spending MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM、PCE 物价 Price Index MoM、美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-26/MP_morning.json