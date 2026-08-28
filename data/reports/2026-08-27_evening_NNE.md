# 期权晚报 2026-08-27

📊 市场环境

SPY $771.10 ｜ QQQ $721.11
VIX 14.51 ↓4.6%（5D -9.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.2（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911

🔍 重点速览
🔴 **事件差分**: 08-28（1D）ATM IV 122.7% vs 09-04 83.6%（差 +39.1pp），覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 08-28 19C ΔOI +105（距现价 -2.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
NNE: 今晨 19.23 → 收盘 19.40（+0.9%） ｜ 今日高 19.55 ｜ 低 18.40
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.31 | OI比 0.78 | ATM IV 122.7% | Skew -4.0pp | Term 0.69 | ExpMove ±5.3%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±3.8% ｜ 09-04（8D）±9.8% ｜ 09-11（15D）±14.4% ｜ 09-18（22D）±19.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 17.87（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 91%（带内） ｜ IV 有效性: VALID 225 / LOW 87 / INVALID 174
结构观察区: ≈18（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 16: +21.2% | 距 Call Wall 22: -13.8%
最近结构参考: Flip 18（距现价 +8.6%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall）；上方 22（Call Wall）。
• Gamma 区域：切换参考 18（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 16.0P — Vol 2 | 最新价 $0.15 | OI 316→471 (ΔOI +155张) | ΔOI/Volume 7750.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增155张（+49.0% vs前日OI），连续性待观察（方向未知）
08-28 19.0C — Vol 143 | 最新价 $0.58 | OI 394→499 (ΔOI +105张) | ΔOI/Volume 73.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增105张（+26.6% vs前日OI），连续性待观察（方向未知）
09-04 24.0C — Vol 0 | 最新价 $0.05 | OI 37→137 (ΔOI +100张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增100张（+270.3% vs前日OI），值得跟踪（方向未知）
09-04 17.0P — Vol 34 | 最新价 $0.15 | OI 49→118 (ΔOI +69张) | ΔOI/Volume 202.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增69张（+140.8% vs前日OI），连续性待观察（方向未知）
08-28 18.0P — Vol 39 | 最新价 $0.05 | OI 247→310 (ΔOI +63张) | ΔOI/Volume 161.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增63张（+25.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +0.2k / P +93 ｜ Activity HIGH ｜ 1D
09-04  C +0.2k / P +0.3k ｜ Activity HIGH ｜ 8D
09-11  C +31 / P +34 ｜ Activity MEDIUM △ ｜ 15D
09-18  C +60 / P +17 ｜ Activity MEDIUM △ ｜ 22D

📆 08-28 Forward Structure
OI:       C 4.9k / P 3.8k
ΔOI:      C +0.2k / P +93
ATM:      C 0.32 / P 0.42
ATM IV:   122.7%
ΔOI Δ Exposure*: 6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +105 ｜ $0.58 ｜ 名义 $6.1k* ｜ -2.1%
P 18 ｜ +63 ｜ $0.05 ｜ 名义 $315* ｜ -7.2%
P 22 ｜ +62 ｜ $3.47 ｜ 名义 $21.5k* ｜ +13.4%
结构参考：22（+13.4%）上方 / 19（-2.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 1.9k / P 1.2k
ΔOI:      C +0.2k / P +0.3k
ATM:      C 0.88 / P 1.02
ATM IV:   83.6%
ΔOI Δ Exposure*: 89 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +155 ｜ $0.15 ｜ 名义 $2.3k* ｜ -17.5%
C 24 ｜ +100 ｜ $0.05 ｜ 名义 $500* ｜ +23.7%
P 17 ｜ +69 ｜ $0.15 ｜ 名义 $1.0k* ｜ -12.4%
结构参考：24（+23.7%）上方 / 16（-17.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 22C +26 ｜ 16P +17

   Top ΔOI: 25C +38 ｜ 17P +30

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 122.7% vs 09-04 83.6%（差 +39.1pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/NNE_evening.json