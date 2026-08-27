# 期权晨报 2026-08-27

📊 市场环境

SPY $770.63 ｜ QQQ $719.25
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.3（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911


## MP

🔍 重点速览
🟡 **单日价格波动**: -2.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-11 60C ΔOI +131（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 59.55 → 今晨 58.36（-2.0%） | 较昨收变动（含盘初走势） ｜ 今日高 59.47 ｜ 低 57.27

Options: P/C量 0.29 | OI比 0.52 | ATM IV 77.7% | Skew -3.0pp | Term 0.84 | ExpMove ±3.7%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±3.7% ｜ 09-04（8D）±8.3% ｜ 09-11（15D）±10.6% ｜ 09-18（22D）±12.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 55.45（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 287 / LOW 71 / INVALID 148
结构观察区: ≈55（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 55: +6.1% | 距 Call Wall 60: -2.7%
最近结构参考: Call Wall 60（距现价 -2.7%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall）；上方 60（Call Wall）。
• Gamma 区域：切换参考 55（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 65.0C — Vol 147 | 最新价 $0.04 | OI 1653→1971 (ΔOI +318张) | ΔOI/Volume 216.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增318张（+19.2% vs前日OI），连续性待观察（方向未知）
09-18 65.0C — Vol 81 | 最新价 $1.82 | OI 5230→5433 (ΔOI +203张) | ΔOI/Volume 250.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增203张（+3.9% vs前日OI），值得跟踪（方向未知）
09-18 64.0P — Vol 0 | 最新价 $7.15 | OI 0→144 (ΔOI +144张) | ΔOI/Volume N/A | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增144张（量数据缺失），以日内换手为主
08-28 63.0C — Vol 137 | 最新价 $0.09 | OI 1034→1174 (ΔOI +140张) | ΔOI/Volume 102.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增140张（+13.5% vs前日OI），连续性待观察（方向未知）
09-11 60.0C — Vol 86 | 最新价 $2.60 | OI 266→397 (ΔOI +131张) | ΔOI/Volume 152.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增131张（+49.2% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 1D
09-04  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 8D
09-11  C +0.2k / P +69 ｜ Activity HIGH ｜ 15D
09-18  C -72 / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

   Top ΔOI: 65C +318 ｜ 63C +140

📆 09-04 Forward Structure
OI:       C 7.1k / P 5.3k
ΔOI:      C +0.6k / P +0.2k
ATM:      C 2.60 / P 2.22
ATM IV:   69.7%
ΔOI Δ Exposure*: -258 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 68 ｜ +120 ｜ $0.47 ｜ 名义 $5.6k* ｜ +16.5%
C 76 ｜ +111 ｜ $0.15 ｜ 名义 $1.7k* ｜ +30.2%
C 70 ｜ +72 ｜ $0.23 ｜ 名义 $1.7k* ｜ +19.9%
结构参考：68（+16.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.7k / P 3.0k
ΔOI:      C +0.2k / P +69
ATM:      C 3.55 / P 2.65
ATM IV:   67.8%
ΔOI Δ Exposure*: 5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 60 ｜ +131 ｜ $2.60 ｜ 名义 $34.1k* ｜ +2.8%
P 60 ｜ +25 ｜ $3.75 ｜ 名义 $9.4k* ｜ +2.8%
C 64 ｜ +25 ｜ $1.53 ｜ 名义 $3.8k* ｜ +9.7%
结构参考：60（+2.8%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 70C -399 ｜ 65C +203

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 77.7% vs 09-04 69.7%（差 +8.0pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/MP_morning.json