# 期权晚报 2026-08-28

📊 市场环境

SPY $769.35 ｜ QQQ $716.43
VIX 14.43 ↓0.6%（5D -4.6%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: -2.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-04 ATM IV 83.9% vs 09-11 73.1%（差 +10.8pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 17P ΔOI +53（距现价 -2.6%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## NNE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NNE: 今开 19.08 → 收盘 17.97（-5.8%） ｜ 今日高 19.30 ｜ 低 17.81
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.81 | OI比 0.82 | ATM IV 168.7% | Skew 3.1pp | Term 0.47 | ExpMove ±4.3%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.81×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.82×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（7D）±12.9% ｜ 09-11（14D）±15.0% ｜ 09-18（21D）±18.4% ｜ 09-25（28D）±20.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 17.00（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 84%（带内） ｜ IV 有效性: VALID 219 / LOW 79 / INVALID 194
结构观察区: Primary Flip 17.00（全链重定价，覆盖 84%）
Put Wall 16（现价高于该位 12.3%） | Call Wall 22（现价低于该位 20.1%）
最近结构参考: Flip 17（现价高于该位 5.7%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 16（Put Wall）；上方 22（Call Wall）。
• Gamma 区域：切换参考 17（全链重定价，覆盖 84%）。
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

09-04  C +0.4k / P +73 ｜ Activity HIGH ｜ 7D
09-11  C +0.2k / P +24 ｜ Activity HIGH ｜ 14D
09-18  C +0.3k / P -35 ｜ Activity HIGH ｜ 21D
09-25  C +38 / P -3 ｜ Activity MEDIUM △ ｜ 28D

📆 09-04 Forward Structure
OI:       C 2.3k / P 1.2k
ΔOI:      C +0.4k / P +73
ATM:      C 1.72 / P 0.60
ATM IV:   83.9%
ΔOI Δ Exposure*: 8k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +151 ｜ $0.73 ｜ 名义 $11.0k* ｜ +8.5%
C 21 ｜ +137 ｜ $0.32 ｜ 名义 $4.4k* ｜ +16.9%
P 17 ｜ +53 ｜ $0.50 ｜ 名义 $2.6k* ｜ -2.6%
结构参考：19（+8.5%）上方 / 17（-2.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.2k / P 0.9k
ΔOI:      C +0.2k / P +24
ATM:      C 1.95 / P 0.75
ATM IV:   73.1%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 22 ｜ +153 ｜ $0.37 ｜ 名义 $5.7k* ｜ +22.4%
C 23 ｜ +19 ｜ $0.18 ｜ 名义 $342* ｜ +28.0%
P 15 ｜ +11 ｜ $0.10 ｜ 名义 $110* ｜ -16.5%
结构参考：22（+22.4%）上方 / 15（-16.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 4.7k / P 2.6k
ΔOI:      C +0.3k / P -35
ATM:      C 2.05 / P 1.26
ATM IV:   80.4%
ΔOI Δ Exposure*: 8k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 23 ｜ +125 ｜ $0.45 ｜ 名义 $5.6k* ｜ +28.0%
C 18 ｜ +47 ｜ $2.05 ｜ 名义 $9.6k* ｜ +0.2%
C 24 ｜ +38 ｜ $0.31 ｜ 名义 $1.2k* ｜ +33.6%
结构参考：23（+28.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 22C +22 ｜ 24C +11

📅 事件差分（观察，非因果）: 09-04（7D）ATM IV 83.9% vs 09-11 73.1%（差 +10.8pp）——覆盖 Non Farm Payrolls Annual Revision Prel、美联储主席讲话 Warsh Speech
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/NNE_evening.json