# 期权晨报 2026-08-28

📊 市场环境

SPY $769.24 ｜ QQQ $716.43
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: +2.3%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 1440P ΔOI +1,008（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,464.42 → 今晨 1,506.18（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 1517.75 ｜ 低 1435.61

Options: P/C量 0.49 | OI比 0.67 | ATM IV 85.4% | Skew -0.2pp | Term 0.79 | ExpMove ±1.7%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.67×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±7.6% ｜ 09-11（14D）±12.2% ｜ 09-18（21D）±12.9% ｜ 09-25（28D）±13.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 1467.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 1844 / LOW 688 / INVALID 1250
结构观察区: Primary Flip 1467.86（全链重定价，覆盖 92%）
Put Wall 1,200（现价高于该位 25.5%） | Call Wall 2,000（现价低于该位 24.7%）
最近结构参考: Flip 1468（现价高于该位 2.6%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 1,200（Put Wall）；上方 2,000（Call Wall）。
• Gamma 区域：切换参考 1468（全链重定价，覆盖 92%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 1530.0C — Vol 3,671 | 最新价 $4.90 | OI 247→1492 (ΔOI +1245张) | ΔOI/Volume 33.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1245张（+504.1% vs前日OI），连续性待观察（方向未知）
08-28 1600.0C — Vol 5,985 | 最新价 $0.15 | OI 2857→3995 (ΔOI +1138张) | ΔOI/Volume 19.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1138张（+39.8% vs前日OI），连续性待观察（方向未知）
09-04 1440.0P — Vol 72 | 最新价 $29.00 | OI 889→1897 (ΔOI +1008张) | ΔOI/Volume 1400.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1008张（+113.4% vs前日OI），连续性待观察（方向未知）
09-04 1265.0P — Vol 45 | 最新价 $2.75 | OI 894→1872 (ΔOI +978张) | ΔOI/Volume 2173.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增978张（+109.4% vs前日OI），连续性待观察（方向未知）
09-04 1710.0C — Vol 44 | 最新价 $7.20 | OI 895→1851 (ΔOI +956张) | ΔOI/Volume 2172.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增956张（+106.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +4.5k / P +5.2k ｜ Activity HIGH ｜ 7D
09-11  C +0.6k / P +0.5k ｜ Activity HIGH ｜ 14D
09-18  C +1.4k / P +0.2k ｜ Activity HIGH ｜ 21D
09-25  C +0.5k / P +0.5k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 24.5k / P 24.2k
ΔOI:      C +4.5k / P +5.2k
ATM:      C 57.85 / P 56.10
ATM IV:   67.4%
ΔOI Δ Exposure*: 12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1440 ｜ +1,008 ｜ $29.00 ｜ 名义 $2.92M* ｜ -4.4%
P 1265 ｜ +978 ｜ $2.75 ｜ 名义 $268.9k* ｜ -16.0%
C 1710 ｜ +956 ｜ $7.20 ｜ 名义 $688.3k* ｜ +13.5%
结构参考：1710（+13.5%）上方 / 1440（-4.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 5.6k / P 9.5k
ΔOI:      C +0.6k / P +0.5k
ATM:      C 80.52 / P 103.38
ATM IV:   65.7%
ΔOI Δ Exposure*: 15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1550 ｜ +106 ｜ $55.00 ｜ 名义 $583.0k* ｜ +2.9%
P 1100 ｜ +47 ｜ $1.43 ｜ 名义 $6.7k* ｜ -27.0%
P 1270 ｜ +38 ｜ $9.10 ｜ 名义 $34.6k* ｜ -15.7%
结构参考：1550（+2.9%）上方 / 1100（-27.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 53.4k / P 68.5k
ΔOI:      C +1.4k / P +0.2k
ATM:      C 97.09 / P 97.82
ATM IV:   66.5%
ΔOI Δ Exposure*: 83k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1700 ｜ +364 ｜ $35.80 ｜ 名义 $1.30M* ｜ +12.9%
C 1800 ｜ +270 ｜ $20.80 ｜ 名义 $561.6k* ｜ +19.5%
P 2300 ｜ -188 ｜ $800.88 ｜ 名义 $-15.06M* ｜ +52.7%
结构参考：1700（+12.9%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 4.2k / P 9.2k
ΔOI:      C +0.5k / P +0.5k
ATM:      C 89.00 / P 119.54
ATM IV:   67.8%
ΔOI Δ Exposure*: 6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1500 ｜ +97 ｜ $113.61 ｜ 名义 $1.10M* ｜ -0.4%
C 1550 ｜ +77 ｜ $95.00 ｜ 名义 $731.5k* ｜ +2.9%
C 1875 ｜ +69 ｜ $24.30 ｜ 名义 $167.7k* ｜ +24.5%
结构参考：1550（+2.9%）上方 / 1500（-0.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/SNDK_morning.json