# 期权晨报 2026-08-27

📊 市场环境

SPY $770.63 ｜ QQQ $719.20
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.3（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911


## MSTR

🔍 重点速览
🔴 **事件差分**: 08-28（1D）ATM IV 105.4% vs 09-04 80.2%（差 +25.2pp），覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +9.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 08-28 130C ΔOI +10,571（距现价 -4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 124.33 → 今晨 135.79（+9.2%） | 较昨收变动（含盘初走势） ｜ 今日高 137.75 ｜ 低 124.46

Options: P/C量 0.32 | OI比 0.77 | ATM IV 105.4% | Skew -12.8pp | Term 0.72 | ExpMove ±4.9%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.77×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±4.9% ｜ 09-04（8D）±9.5% ｜ 09-11（15D）±12.2% ｜ 09-18（22D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 95%（带内） ｜ IV 有效性: VALID 846 / LOW 88 / INVALID 242
结构观察区: NO_CROSS
距 Put Wall 60: +126.3% | 距 Call Wall 130: +4.5%
最近结构参考: Call Wall 130（距现价 +4.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 60（Put Wall）；上方 130（Call Wall）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 130.0C — Vol 22,508 | 最新价 $6.79 | OI 22587→33158 (ΔOI +10571张) | ΔOI/Volume 47.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增10571张（+46.8% vs前日OI），连续性待观察（方向未知）
08-28 128.0C — Vol 10,591 | 最新价 $8.55 | OI 9948→18083 (ΔOI +8135张) | ΔOI/Volume 76.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增8135张（+81.8% vs前日OI），连续性待观察（方向未知）
08-28 150.0C — Vol 7,016 | 最新价 $0.43 | OI 6821→12646 (ΔOI +5825张) | ΔOI/Volume 83.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5825张（+85.4% vs前日OI），连续性待观察（方向未知）
08-28 126.0C — Vol 5,343 | 最新价 $10.20 | OI 1835→7335 (ΔOI +5500张) | ΔOI/Volume 102.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5500张（+299.7% vs前日OI），连续性待观察（方向未知）
08-28 125.0C — Vol 5,993 | 最新价 $11.10 | OI 3280→7770 (ΔOI +4490张) | ΔOI/Volume 74.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4490张（+136.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +26.9k / P -1.2k ｜ Activity HIGH ｜ 1D
09-04  C +5.1k / P +9.9k ｜ Activity HIGH ｜ 8D
09-11  C +4.0k / P +2.3k ｜ Activity HIGH ｜ 15D
09-18  C +3.0k / P +0.5k ｜ Activity MEDIUM △ ｜ 22D

📆 08-28 Forward Structure
OI:       C 285.6k / P 221.1k
ΔOI:      C +26.9k / P -1.2k
ATM:      C 3.26 / P 3.40
ATM IV:   105.4%
ΔOI Δ Exposure*: 1.8M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 130 ｜ +10,571 ｜ $6.79 ｜ 名义 $7.18M* ｜ -4.3%
C 128 ｜ +8,135 ｜ $8.55 ｜ 名义 $6.96M* ｜ -5.7%
C 150 ｜ +5,825 ｜ $0.43 ｜ 名义 $250.5k* ｜ +10.5%
结构参考：150（+10.5%）上方 / 130（-4.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 52.2k / P 106.7k
ΔOI:      C +5.1k / P +9.9k
ATM:      C 6.44 / P 6.52
ATM IV:   80.2%
ΔOI Δ Exposure*: 264k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 130 ｜ +2,131 ｜ $9.59 ｜ 名义 $2.04M* ｜ -4.3%
P 113 ｜ +2,101 ｜ $0.52 ｜ 名义 $109.3k* ｜ -16.8%
P 119 ｜ +1,987 ｜ $0.92 ｜ 名义 $182.8k* ｜ -12.4%
结构参考：130（-4.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 20.6k / P 47.0k
ΔOI:      C +4.0k / P +2.3k
ATM:      C 8.40 / P 8.24
ATM IV:   75.3%
ΔOI Δ Exposure*: 173k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 150 ｜ +1,327 ｜ $3.93 ｜ 名义 $521.5k* ｜ +10.5%
P 110 ｜ +858 ｜ $0.75 ｜ 名义 $64.3k* ｜ -19.0%
C 128 ｜ +686 ｜ $12.42 ｜ 名义 $852.0k* ｜ -5.7%
结构参考：150（+10.5%）上方 / 110（-19.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 200C +1,659 ｜ 50P -649

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 105.4% vs 09-04 80.2%（差 +25.2pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/MSTR_morning.json