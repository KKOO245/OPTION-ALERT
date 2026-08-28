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
🟡 **单日价格波动**: -2.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 58P ΔOI +132（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MP  昨收 58.60 → 今晨 56.96（-2.8%） | 较昨收变动（含盘初走势） ｜ 今日高 59.80 ｜ 低 56.15

Options: P/C量 0.47 | OI比 0.53 | ATM IV 84.1% | Skew -3.8pp | Term 0.81 | ExpMove ±2.0%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.47×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.53×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±7.7% ｜ 09-11（14D）±10.6% ｜ 09-18（21D）±11.8% ｜ 09-25（28D）±15.8%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 54.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 96%（带内） ｜ IV 有效性: VALID 280 / LOW 81 / INVALID 165
结构观察区: Primary Flip 54.82（全链重定价，覆盖 96%）
Put Wall 55（现价高于该位 3.6%） | Call Wall 60（现价低于该位 5.1%）
最近结构参考: Put Wall 55（现价高于该位 3.6%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall）；上方 60（Call Wall）。
• Gamma 区域：切换参考 55（全链重定价，覆盖 96%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 70.0C — Vol 32 | 最新价 $0.15 | OI 331→1265 (ΔOI +934张) | ΔOI/Volume 2918.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增934张（+282.2% vs前日OI），连续性待观察（方向未知）
09-04 47.0P — Vol 1 | 最新价 $0.10 | OI 183→350 (ΔOI +167张) | ΔOI/Volume 16700.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增167张（+91.3% vs前日OI），连续性待观察（方向未知）
08-28 75.0C — Vol 3 | 最新价 $0.05 | OI 485→651 (ΔOI +166张) | ΔOI/Volume 5533.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增166张（+34.2% vs前日OI），连续性待观察（方向未知）
09-18 63.0C — Vol 18 | 最新价 $1.96 | OI 50→193 (ΔOI +143张) | ΔOI/Volume 794.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增143张（+286.0% vs前日OI），连续性待观察（方向未知）
09-04 58.0P — Vol 21 | 最新价 $2.31 | OI 74→206 (ΔOI +132张) | ΔOI/Volume 628.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增132张（+178.4% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +1.6k / P +0.9k ｜ Activity HIGH ｜ 7D
09-11  C +94 / P +93 ｜ Activity MEDIUM △ ｜ 14D
09-18  C -0.4k / P +29 ｜ Activity MEDIUM △ ｜ 21D
09-25  C +60 / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 8.7k / P 6.2k
ΔOI:      C +1.6k / P +0.9k
ATM:      C 2.62 / P 1.76
ATM IV:   67.2%
ΔOI Δ Exposure*: 12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 70 ｜ +934 ｜ $0.15 ｜ 名义 $14.0k* ｜ +22.9%
P 47 ｜ +167 ｜ $0.10 ｜ 名义 $1.7k* ｜ -17.5%
P 58 ｜ +132 ｜ $2.31 ｜ 名义 $30.5k* ｜ +1.8%
结构参考：70（+22.9%）上方 / 47（-17.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 60C +56 ｜ 62C +24

   Top ΔOI: 70C -788 ｜ 63C +143

📆 09-25 Forward Structure
OI:       C 3.1k / P 3.3k
ΔOI:      C +60 / P +0.2k
ATM:      C 5.62 / P 3.41
ATM IV:   67.9%
ΔOI Δ Exposure*: -756 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 45 ｜ +100 ｜ $0.34 ｜ 名义 $3.4k* ｜ -21.0%
P 55 ｜ +48 ｜ $2.80 ｜ 名义 $13.4k* ｜ -3.4%
C 63 ｜ +17 ｜ $2.26 ｜ 名义 $3.8k* ｜ +10.6%
结构参考：63（+10.6%）上方 / 45（-21.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/MP_morning.json