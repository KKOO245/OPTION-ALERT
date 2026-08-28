# 期权晨报 2026-08-28

📊 市场环境

SPY $769.10 ｜ QQQ $716.43
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览: 今日无重点项（机械检查 highlight_v1）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 19.18 → 今晨 18.48（-3.6%） | 较昨收变动（含盘初走势） ｜ 今日高 19.74 ｜ 低 18.37

Options: P/C量 0.30 | OI比 0.51 | ATM IV 112.5% | Skew -5.8pp | Term 0.78 | ExpMove ±2.2%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.30×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±9.0% ｜ 09-11（14D）±12.8% ｜ 09-18（21D）±16.2% ｜ 09-25（28D）±18.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 16.28（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 285 / LOW 90 / INVALID 159
结构观察区: Primary Flip 16.28（全链重定价，覆盖 93%）
Put Wall 15（现价高于该位 23.2%） | Call Wall 20（现价低于该位 7.6%）
最近结构参考: Call Wall 20（现价低于该位 7.6%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 20（Call Wall）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 93%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 23.0C — Vol 64 | 最新价 $0.08 | OI 652→1450 (ΔOI +798张) | ΔOI/Volume 1246.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增798张（+122.4% vs前日OI），连续性待观察（方向未知）
09-18 20.0C — Vol 1,728 | 最新价 $0.92 | OI 13275→13763 (ΔOI +488张) | ΔOI/Volume 28.2% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增488张（+3.7% vs前日OI），值得跟踪（方向未知）
09-25 25.0C — Vol 2 | 最新价 $0.35 | OI 1677→2143 (ΔOI +466张) | ΔOI/Volume 23300.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增466张（+27.8% vs前日OI），连续性待观察（方向未知）
09-04 22.5C — Vol 21 | 最新价 $0.08 | OI 482→670 (ΔOI +188张) | ΔOI/Volume 895.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增188张（+39.0% vs前日OI），连续性待观察（方向未知）
09-04 21.5C — Vol 15 | 最新价 $0.17 | OI 857→1044 (ΔOI +187张) | ΔOI/Volume 1246.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增187张（+21.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +1.9k / P +0.6k ｜ Activity HIGH ｜ 7D
09-11  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 14D
09-18  C +1.0k / P -0.5k ｜ Activity HIGH ｜ 21D
09-25  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 25.7k / P 4.5k
ΔOI:      C +1.9k / P +0.6k
ATM:      C 0.86 / P 0.81
ATM IV:   84.1%
ΔOI Δ Exposure*: 15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 23 ｜ +798 ｜ $0.08 ｜ 名义 $6.4k* ｜ +24.5%
C 22 ｜ +188 ｜ $0.08 ｜ 名义 $1.5k* ｜ +21.8%
C 21 ｜ +187 ｜ $0.17 ｜ 名义 $3.2k* ｜ +16.3%
结构参考：23（+24.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 9.4k / P 1.9k
ΔOI:      C +0.1k / P +0.2k
ATM:      C 1.20 / P 1.17
ATM IV:   81.5%
ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 22 ｜ +82 ｜ $0.29 ｜ 名义 $2.4k* ｜ +19.0%
P 16 ｜ +75 ｜ $0.33 ｜ 名义 $2.5k* ｜ -10.7%
P 17 ｜ +54 ｜ $0.46 ｜ 名义 $2.5k* ｜ -8.0%
结构参考：22（+19.0%）上方 / 16（-10.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 108.2k / P 63.9k
ΔOI:      C +1.0k / P -0.5k
ATM:      C 1.50 / P 1.50
ATM IV:   83.7%
ΔOI Δ Exposure*: 47k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 20 ｜ +488 ｜ $0.92 ｜ 名义 $44.9k* ｜ +8.2%
P 16 ｜ -215 ｜ $0.44 ｜ 名义 $-9.5k* ｜ -13.4%
C 22 ｜ +173 ｜ $0.48 ｜ 名义 $8.3k* ｜ +19.0%
结构参考：20（+8.2%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 7.4k / P 2.5k
ΔOI:      C +0.7k / P +0.2k
ATM:      C 1.93 / P 1.41
ATM IV:   88.1%
ΔOI Δ Exposure*: 9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 25 ｜ +466 ｜ $0.35 ｜ 名义 $16.3k* ｜ +35.3%
P 14 ｜ +105 ｜ $0.26 ｜ 名义 $2.7k* ｜ -24.2%
C 24 ｜ +74 ｜ $0.45 ｜ 名义 $3.3k* ｜ +29.9%
结构参考：25（+35.3%）上方 / 14（-24.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/USAR_morning.json