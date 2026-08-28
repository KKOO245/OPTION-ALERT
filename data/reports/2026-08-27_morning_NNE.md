# 期权晨报 2026-08-27

📊 市场环境

SPY $771.10 ｜ QQQ $721.11
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.2（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911

🔍 重点速览
🟡 **单日价格波动**: +2.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 08-28 ATM IV 97.9% vs 09-04 84.5%（差 +13.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 08-28 19C ΔOI +105（距现价 -1.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 18.80 → 今晨 19.23（+2.3%） | 较昨收变动（含盘初走势） ｜ 今日高 19.40 ｜ 低 18.40

Options: P/C量 0.31 | OI比 0.78 | ATM IV 97.9% | Skew -0.8pp | Term 0.86 | ExpMove ±4.7%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.78×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±4.7% ｜ 09-04（8D）±10.6% ｜ 09-11（15D）±11.4% ｜ 09-18（22D）±16.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 17.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 233 / LOW 85 / INVALID 168
结构观察区: ≈18（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 16: +20.2% | 距 Call Wall 22: -14.5%
最近结构参考: Flip 18（距现价 +7.9%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall）；上方 22（Call Wall）。
• Gamma 区域：切换参考 18（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 16.0P — Vol 0 | 最新价 $0.20 | OI 316→471 (ΔOI +155张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增155张（+49.0% vs前日OI），值得跟踪（方向未知）
08-28 19.0C — Vol 47 | 最新价 $0.55 | OI 394→499 (ΔOI +105张) | ΔOI/Volume 223.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增105张（+26.6% vs前日OI），连续性待观察（方向未知）
09-04 24.0C — Vol 0 | 最新价 $0.05 | OI 37→137 (ΔOI +100张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增100张（+270.3% vs前日OI），值得跟踪（方向未知）
09-04 17.0P — Vol 11 | 最新价 $0.30 | OI 49→118 (ΔOI +69张) | ΔOI/Volume 627.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增69张（+140.8% vs前日OI），连续性待观察（方向未知）
08-28 18.0P — Vol 31 | 最新价 $0.10 | OI 247→310 (ΔOI +63张) | ΔOI/Volume 203.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增63张（+25.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +0.2k / P +93 ｜ Activity HIGH ｜ 1D
09-04  C +0.2k / P +0.3k ｜ Activity HIGH ｜ 8D
09-11  C +31 / P +34 ｜ Activity MEDIUM △ ｜ 15D
09-18  C +60 / P +17 ｜ Activity MEDIUM △ ｜ 22D

📆 08-28 Forward Structure
OI:       C 4.9k / P 3.8k
ΔOI:      C +0.2k / P +93
ATM:      C 0.55 / P 0.35
ATM IV:   97.9%
ΔOI Δ Exposure*: 6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +105 ｜ $0.55 ｜ 名义 $5.8k* ｜ -1.2%
P 18 ｜ +63 ｜ $0.10 ｜ 名义 $630* ｜ -6.4%
P 22 ｜ +62 ｜ $3.47 ｜ 名义 $21.5k* ｜ +14.4%
结构参考：22（+14.4%）上方 / 19（-1.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 1.9k / P 1.2k
ΔOI:      C +0.2k / P +0.3k
ATM:      C 0.90 / P 1.13
ATM IV:   84.5%
ΔOI Δ Exposure*: 32 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +155 ｜ $0.20 ｜ 名义 $3.1k* ｜ -16.8%
C 24 ｜ +100 ｜ $0.05 ｜ 名义 $500* ｜ +24.8%
P 17 ｜ +69 ｜ $0.30 ｜ 名义 $2.1k* ｜ -11.6%
结构参考：24（+24.8%）上方 / 16（-16.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 22C +26 ｜ 16P +17

   Top ΔOI: 25C +38 ｜ 17P +30

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 97.9% vs 09-04 84.5%（差 +13.4pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/NNE_morning.json