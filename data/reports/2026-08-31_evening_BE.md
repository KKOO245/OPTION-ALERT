# 期权晚报 2026-08-31

📊 市场环境

SPY $767.05 ｜ QQQ $716.76
VIX 14.92 ↑3.4%（5D -5.9%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 49.7（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 待公布 ｜ 前值 7.359
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 待公布 ｜ 前值 55.6
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（4D）ATM IV 95.4% vs 09-11 78.7%（差 +16.7pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 09-04 200P ΔOI +888（距现价 -3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
BE: 今开 208.88 → 收盘 206.30（-1.2%） ｜ 今日高 210.00 ｜ 低 202.88
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.76 | OI比 1.27 | ATM IV 95.4% | Skew -7.8pp | Term 0.81 | ExpMove ±8.1%（近端） | Rank 57%
   ⇒ Put/Call Volume: 0.76×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.27×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 两者结构不一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±8.1% ｜ 09-11（11D）±11.6% ｜ 09-18（18D）±14.2% ｜ 09-25（25D）±16.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 571,942 | GEX Change vs 上次快照 1,191,265 | Flip: Primary Flip: 205.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 556 / LOW 68 / INVALID 174
结构观察区: Primary Flip 205.42（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价高于该位 3.2%）
最近结构参考: Flip 205（现价高于该位 0.4%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 N/A。
• Gamma 区域：切换参考 205（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 180.0C — Vol 34 | 最新价 $26.35 | OI 84→1595 (ΔOI +1511张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1511张（+1798.8% vs前日OI），连续性待观察（方向未知）
09-04 190.0P — Vol 1,472 | 最新价 $2.05 | OI 1200→2206 (ΔOI +1006张) | ΔOI/Volume 68.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1006张（+83.8% vs前日OI），连续性待观察（方向未知）
09-04 200.0P — Vol 1,490 | 最新价 $5.12 | OI 1370→2258 (ΔOI +888张) | ΔOI/Volume 59.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增888张（+64.8% vs前日OI），连续性待观察（方向未知）
09-18 145.0P — Vol 20 | 最新价 $0.49 | OI 4172→5018 (ΔOI +846张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增846张（+20.3% vs前日OI），连续性待观察（方向未知）
09-04 250.0C — Vol 1,898 | 最新价 $0.44 | OI 2801→3440 (ΔOI +639张) | ΔOI/Volume 33.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增639张（+22.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +6.2k / P +8.5k ｜ Activity HIGH ｜ 4D
09-11  C +0.8k / P +1.6k ｜ Activity HIGH ｜ 11D
09-18  C -2.9k / P +1.0k ｜ Activity HIGH ｜ 18D
09-25  C +0.4k / P +0.6k ｜ Activity HIGH ｜ 25D

📆 09-04 Forward Structure
OI:       C 29.3k / P 37.3k
ΔOI:      C +6.2k / P +8.5k
ATM:      C 7.80 / P 8.90
ATM IV:   95.4%
ΔOI Δ Exposure*: -557 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 180 ｜ +1,511 ｜ $26.35 ｜ 名义 $3.98M* ｜ -12.7%
P 190 ｜ +1,006 ｜ $2.05 ｜ 名义 $206.2k* ｜ -7.9%
P 200 ｜ +888 ｜ $5.12 ｜ 名义 $454.7k* ｜ -3.1%
结构参考：180（-12.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 12.6k / P 11.3k
ΔOI:      C +0.8k / P +1.6k
ATM:      C 10.37 / P 13.50
ATM IV:   78.7%
ΔOI Δ Exposure*: -9k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 175 ｜ +309 ｜ $1.64 ｜ 名义 $50.7k* ｜ -15.2%
P 110 ｜ +247 ｜ $0.02 ｜ 名义 $494* ｜ -46.7%
P 100 ｜ +241 ｜ $0.02 ｜ 名义 $482* ｜ -51.5%
结构参考：175（-15.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 115.4k / P 94.1k
ΔOI:      C -2.9k / P +1.0k
ATM:      C 13.22 / P 16.10
ATM IV:   80.2%
ΔOI Δ Exposure*: -156k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 210 ｜ -2,801 ｜ $13.28 ｜ 名义 $-3.72M* ｜ +1.8%
C 260 ｜ -1,092 ｜ $2.54 ｜ 名义 $-277.4k* ｜ +26.0%
C 230 ｜ -882 ｜ $6.75 ｜ 名义 $-595.4k* ｜ +11.5%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 7.2k / P 6.5k
ΔOI:      C +0.4k / P +0.6k
ATM:      C 16.93 / P 16.10
ATM IV:   78.3%
ΔOI Δ Exposure*: -12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 225 ｜ +237 ｜ $9.75 ｜ 名义 $231.1k* ｜ +9.1%
P 225 ｜ +199 ｜ $26.29 ｜ 名义 $523.2k* ｜ +9.1%
P 180 ｜ +125 ｜ $5.85 ｜ 名义 $73.1k* ｜ -12.7%
结构参考：225（+9.1%）上方 / 180（-12.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 95.4% vs 09-11 78.7%（差 +16.7pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/BE_evening.json