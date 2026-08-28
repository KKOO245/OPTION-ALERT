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
🟡 **单日价格波动**: -2.6%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向

💾 每周本地备份提醒：请在 `D:\git\Option Alert-数据储存` 运行 `git pull`，把本周数据拉到本地。报告由 GitHub 自动发送，本地只做数据镜像。


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 19.47 → 收盘 17.99（-7.6%） ｜ 今日高 19.74 ｜ 低 17.81
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.56 | OI比 0.51 | ATM IV 105.9% | Skew -3.1pp | Term 0.80 | ExpMove ±0.6%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.51×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±9.3% ｜ 09-11（14D）±12.3% ｜ 09-18（21D）±14.8% ｜ 09-25（28D）±18.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 15.92（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 86%（带内） ｜ IV 有效性: VALID 259 / LOW 90 / INVALID 185
结构观察区: Primary Flip 15.92（全链重定价，覆盖 86%）
Put Wall 15（现价高于该位 19.9%） | Call Wall 20（现价低于该位 10.1%）
最近结构参考: Call Wall 20（现价低于该位 10.1%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 20（Call Wall）。
• Gamma 区域：切换参考 16（全链重定价，覆盖 86%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 19.5C — Vol 229 | 最新价 $0.89 | OI 890→5657 (ΔOI +4767张) | ΔOI/Volume 2081.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4767张（+535.6% vs前日OI），连续性待观察（方向未知）
08-28 20.0C — Vol 907 | 最新价 $0.16 | OI 3706→4346 (ΔOI +640张) | ΔOI/Volume 70.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增640张（+17.3% vs前日OI），连续性待观察（方向未知）
08-28 21.0C — Vol 198 | 最新价 $0.05 | OI 1715→2338 (ΔOI +623张) | ΔOI/Volume 314.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增623张（+36.3% vs前日OI），连续性待观察（方向未知）
09-04 21.5C — Vol 208 | 最新价 $0.35 | OI 272→857 (ΔOI +585张) | ΔOI/Volume 281.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增585张（+215.1% vs前日OI），连续性待观察（方向未知）
08-28 20.5C — Vol 516 | 最新价 $0.08 | OI 1552→2132 (ΔOI +580张) | ΔOI/Volume 112.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增580张（+37.4% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +1.9k / P +0.6k ｜ Activity HIGH ｜ 7D
09-11  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 14D
09-18  C +1.0k / P -0.5k ｜ Activity HIGH ｜ 21D
09-25  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 25.7k / P 4.5k
ΔOI:      C +1.9k / P +0.6k
ATM:      C 0.89 / P 0.78
ATM IV:   76.3%
ΔOI Δ Exposure*: 2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 23 ｜ +798 ｜ $0.03 ｜ 名义 $2.4k* ｜ +27.8%
C 22 ｜ +188 ｜ $0.04 ｜ 名义 $752* ｜ +25.1%
C 21 ｜ +187 ｜ $0.08 ｜ 名义 $1.5k* ｜ +19.5%
结构参考：23（+27.8%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 9.4k / P 1.9k
ΔOI:      C +0.1k / P +0.2k
ATM:      C 1.10 / P 1.11
ATM IV:   78.2%
ΔOI Δ Exposure*: -3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 22 ｜ +82 ｜ $0.17 ｜ 名义 $1.4k* ｜ +22.3%
P 16 ｜ +75 ｜ $0.47 ｜ 名义 $3.5k* ｜ -8.3%
P 17 ｜ +54 ｜ $0.57 ｜ 名义 $3.1k* ｜ -5.5%
结构参考：22（+22.3%）上方 / 16（-8.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 108.2k / P 63.9k
ΔOI:      C +1.0k / P -0.5k
ATM:      C 1.32 / P 1.35
ATM IV:   79.6%
ΔOI Δ Exposure*: 44k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 20 ｜ +488 ｜ $0.70 ｜ 名义 $34.2k* ｜ +11.2%
P 16 ｜ -215 ｜ $0.50 ｜ 名义 $-10.8k* ｜ -11.1%
C 22 ｜ +173 ｜ $0.34 ｜ 名义 $5.9k* ｜ +22.3%
结构参考：20（+11.2%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 7.4k / P 2.5k
ΔOI:      C +0.7k / P +0.2k
ATM:      C 1.67 / P 1.61
ATM IV:   84.6%
ΔOI Δ Exposure*: 6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 25 ｜ +466 ｜ $0.25 ｜ 名义 $11.7k* ｜ +39.0%
P 14 ｜ +105 ｜ $0.23 ｜ 名义 $2.4k* ｜ -22.2%
C 24 ｜ +74 ｜ $0.45 ｜ 名义 $3.3k* ｜ +33.4%
结构参考：25（+39.0%）上方 / 14（-22.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/USAR_evening.json