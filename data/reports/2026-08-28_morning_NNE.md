# 期权晨报 2026-08-28

📊 市场环境

SPY $769.34 ｜ QQQ $716.43
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: -4.1%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 19.40 → 今晨 18.44（-4.9%） | 较昨收变动（含盘初走势） ｜ 今日高 19.30 ｜ 低 18.14

Options: P/C量 0.81 | OI比 0.82 | ATM IV 142.8% | Skew 3.1pp | Term 0.55 | ExpMove ±3.0%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（7D）±10.1% ｜ 09-11（14D）±12.8% ｜ 09-18（21D）±16.0% ｜ 09-25（28D）±20.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 17.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 219 / LOW 79 / INVALID 194
结构观察区: Primary Flip 17.00（全链重定价，覆盖 84%）
Put Wall 16（现价高于该位 15.3%） | Call Wall 22（现价低于该位 18.0%）
最近结构参考: Flip 17（现价高于该位 8.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall）；上方 22（Call Wall）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 84%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-11 22.0C — Vol 0 | 最新价 $0.37 | OI 43→196 (ΔOI +153张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增153张（+355.8% vs前日OI），值得跟踪（方向未知）
09-04 19.5C — Vol 2 | 最新价 $0.73 | OI 47→198 (ΔOI +151张) | ΔOI/Volume 7550.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增151张（+321.3% vs前日OI），连续性待观察（方向未知）
09-04 21.0C — Vol 4 | 最新价 $0.32 | OI 349→486 (ΔOI +137张) | ΔOI/Volume 3425.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增137张（+39.3% vs前日OI），连续性待观察（方向未知）
09-18 23.0C — Vol 0 | 最新价 $0.45 | OI 197→322 (ΔOI +125张) | ΔOI/Volume N/A | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增125张（+63.5% vs前日OI），值得跟踪（方向未知）
08-28 19.0P — Vol 64 | 最新价 $0.85 | OI 171→239 (ΔOI +68张) | ΔOI/Volume 106.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增68张（+39.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +0.4k / P +73 ｜ Activity HIGH ｜ 7D
09-11  C +0.2k / P +24 ｜ Activity HIGH ｜ 14D
09-18  C +0.3k / P -35 ｜ Activity HIGH ｜ 21D
09-25  C +38 / P -3 ｜ Activity MEDIUM △ ｜ 28D

📆 09-04 Forward Structure
OI:       C 2.3k / P 1.2k
ΔOI:      C +0.4k / P +73
ATM:      C 0.87 / P 1.00
ATM IV:   85.3%
ΔOI Δ Exposure*: 8k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +151 ｜ $0.73 ｜ 名义 $11.0k* ｜ +5.7%
C 21 ｜ +137 ｜ $0.32 ｜ 名义 $4.4k* ｜ +13.9%
P 17 ｜ +53 ｜ $0.50 ｜ 名义 $2.6k* ｜ -5.1%
结构参考：19（+5.7%）上方 / 17（-5.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.2k / P 0.9k
ΔOI:      C +0.2k / P +24
ATM:      C 1.60 / P 0.76
ATM IV:   75.4%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 22 ｜ +153 ｜ $0.37 ｜ 名义 $5.7k* ｜ +19.3%
C 23 ｜ +19 ｜ $0.18 ｜ 名义 $342* ｜ +24.7%
P 15 ｜ +11 ｜ $0.10 ｜ 名义 $110* ｜ -18.7%
结构参考：22（+19.3%）上方 / 15（-18.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 4.7k / P 2.6k
ΔOI:      C +0.3k / P -35
ATM:      C 1.50 / P 1.45
ATM IV:   83.0%
ΔOI Δ Exposure*: 8k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 23 ｜ +125 ｜ $0.45 ｜ 名义 $5.6k* ｜ +24.7%
C 18 ｜ +47 ｜ $2.05 ｜ 名义 $9.6k* ｜ -2.4%
C 24 ｜ +38 ｜ $0.31 ｜ 名义 $1.2k* ｜ +30.2%
结构参考：23（+24.7%）上方 / 18（-2.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 22C +22 ｜ 24C +11

📅 事件差分（观察，非因果）: 09-04（7D）ATM IV 85.3% vs 09-11 75.4%（差 +9.9pp）——覆盖 Non Farm Payrolls Annual Revision Prel、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/NNE_morning.json