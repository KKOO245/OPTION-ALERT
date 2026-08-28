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
🟡 **近现价集中开仓**: 09-04 15C ΔOI +427（距现价 -3.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## UUUU

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
UUUU  昨收 15.88 → 今晨 15.58（-1.9%） | 较昨收变动（含盘初走势） ｜ 今日高 15.92 ｜ 低 15.49

Options: P/C量 0.30 | OI比 0.42 | ATM IV 80.8% | Skew -3.0pp | Term 0.89 | ExpMove ±3.8%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.30×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.42×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±4.1% ｜ 09-04（8D）±8.7% ｜ 09-11（15D）±11.6% ｜ 09-18（22D）±14.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 227 / LOW 59 / INVALID 106
结构观察区: NO_CROSS
距 Put Wall 11: +41.6% | 距 Call Wall 18: -13.4%
最近结构参考: Call Wall 18（距现价 -13.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 11（Put Wall）；上方 18（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 15.0C — Vol 73 | 最新价 $1.02 | OI 332→759 (ΔOI +427张) | ΔOI/Volume 584.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增427张（+128.6% vs前日OI），连续性待观察（方向未知）
09-04 14.5P — Vol 21 | 最新价 $0.22 | OI 197→489 (ΔOI +292张) | ΔOI/Volume 1390.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增292张（+148.2% vs前日OI），连续性待观察（方向未知）
09-18 20.0C — Vol 35 | 最新价 $0.15 | OI 1839→2015 (ΔOI +176张) | ΔOI/Volume 502.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增176张（+9.6% vs前日OI），连续性待观察（方向未知）
09-18 21.0C — Vol 0 | 最新价 $0.13 | OI 191→339 (ΔOI +148张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增148张（+77.5% vs前日OI），值得跟踪（方向未知）
08-28 17.0C — Vol 8 | 最新价 $0.03 | OI 1582→1719 (ΔOI +137张) | ΔOI/Volume 1712.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增137张（+8.7% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +0.2k / P -10 ｜ Activity MEDIUM △ ｜ 1D
09-04  C +0.5k / P +0.4k ｜ Activity HIGH ｜ 8D
09-11  C +0.2k / P +35 ｜ Activity HIGH ｜ 15D
09-18  C +0.4k / P +0.1k ｜ Activity MEDIUM △ ｜ 22D

   Top ΔOI: 14P -158 ｜ 17C +137

📆 09-04 Forward Structure
OI:       C 7.4k / P 2.9k
ΔOI:      C +0.5k / P +0.4k
ATM:      C 0.75 / P 0.60
ATM IV:   73.2%
ΔOI Δ Exposure*: 23k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 15 ｜ +427 ｜ $1.02 ｜ 名义 $43.6k* ｜ -3.7%
P 14 ｜ +292 ｜ $0.22 ｜ 名义 $6.4k* ｜ -6.9%
P 11 ｜ +50 ｜ $0.01 ｜ 名义 $50* ｜ -29.4%
结构参考：15（-3.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.7k / P 2.5k
ΔOI:      C +0.2k / P +35
ATM:      C 1.00 / P 0.81
ATM IV:   69.9%
ΔOI Δ Exposure*: 961 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +101 ｜ $0.18 ｜ 名义 $1.8k* ｜ +22.0%
C 22 ｜ +51 ｜ $0.05 ｜ 名义 $255* ｜ +41.2%
P 14 ｜ +12 ｜ $0.38 ｜ 名义 $456* ｜ -6.9%
结构参考：19（+22.0%）上方 / 14（-6.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 20C +176 ｜ 21C +148

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 80.8% vs 09-04 73.2%（差 +7.6pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/UUUU_morning.json