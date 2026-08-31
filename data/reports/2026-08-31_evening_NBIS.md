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
🟡 **近现价集中开仓**: 09-11 210P ΔOI +504（距现价 +1.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NBIS

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
NBIS: 今开 205.74 → 收盘 206.32（+0.3%） ｜ 今日高 208.88 ｜ 低 201.53
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.61 | OI比 0.96 | ATM IV 83.2% | Skew -0.8pp | Term 0.92 | ExpMove ±7.0%（近端） | Rank 11%
   ⇒ Put/Call Volume: 0.61×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.96×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（4D）±7.0% ｜ 09-11（11D）±10.4% ｜ 09-18（18D）±13.8% ｜ 09-25（25D）±16.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) -8,456,081 | GEX Change vs 上次快照 321,721 | Flip: Primary Flip: 222.99（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 588 / LOW 65 / INVALID 151
   ⇒ 全链负Gamma，波动易被放大（模型层）
结构观察区: Primary Flip 222.99（全链重定价，覆盖 100%）
Put Wall 200（弱结构｜现价高于该位 3.2%）
最近结构参考: Put Wall 200（现价高于该位 3.2%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 200（Put Wall，弱结构）；上方 N/A。
• Gamma 区域：切换参考 223（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 220.0P — Vol 293 | 最新价 $17.55 | OI 966→4394 (ΔOI +3428张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3428张（+354.9% vs前日OI），连续性待观察（方向未知）
09-04 240.0C — Vol 5,054 | 最新价 $0.59 | OI 2534→4322 (ΔOI +1788张) | ΔOI/Volume 35.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1788张（+70.6% vs前日OI），连续性待观察（方向未知）
09-04 220.0C — Vol 1,741 | 最新价 $2.75 | OI 1471→3141 (ΔOI +1670张) | ΔOI/Volume 95.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1670张（+113.5% vs前日OI），连续性待观察（方向未知）
09-04 200.0P — Vol 2,332 | 最新价 $4.45 | OI 4011→5436 (ΔOI +1425张) | ΔOI/Volume 61.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1425张（+35.5% vs前日OI），连续性待观察（方向未知）
09-04 190.0P — Vol 1,265 | 最新价 $1.74 | OI 1567→2694 (ΔOI +1127张) | ΔOI/Volume 89.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1127张（+71.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +7.5k / P +14.7k ｜ Activity HIGH ｜ 4D
09-11  C +3.3k / P +1.6k ｜ Activity HIGH ｜ 11D
09-18  C +0.3k / P +2.4k ｜ Activity HIGH ｜ 18D
09-25  C -41 / P +1.1k ｜ Activity HIGH ｜ 25D

📆 09-04 Forward Structure
OI:       C 46.6k / P 44.6k
ΔOI:      C +7.5k / P +14.7k
ATM:      C 6.79 / P 7.70
ATM IV:   83.2%
ΔOI Δ Exposure*: -400k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 220 ｜ +3,428 ｜ $17.55 ｜ 名义 $6.02M* ｜ +6.6%
C 240 ｜ +1,788 ｜ $0.59 ｜ 名义 $105.5k* ｜ +16.3%
C 220 ｜ +1,670 ｜ $2.75 ｜ 名义 $459.2k* ｜ +6.6%
结构参考：220（+6.6%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 13.8k / P 13.8k
ΔOI:      C +3.3k / P +1.6k
ATM:      C 10.03 / P 11.35
ATM IV:   75.7%
ΔOI Δ Exposure*: 10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 300 ｜ +667 ｜ $0.24 ｜ 名义 $16.0k* ｜ +45.4%
C 270 ｜ +507 ｜ $0.52 ｜ 名义 $26.4k* ｜ +30.9%
P 210 ｜ +504 ｜ $12.60 ｜ 名义 $635.0k* ｜ +1.8%
结构参考：300（+45.4%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 95.9k / P 150.5k
ΔOI:      C +0.3k / P +2.4k
ATM:      C 13.44 / P 15.00
ATM IV:   79.7%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 100 ｜ +901 ｜ $0.10 ｜ 名义 $9.0k* ｜ -51.5%
C 210 ｜ +671 ｜ $12.75 ｜ 名义 $855.5k* ｜ +1.8%
P 190 ｜ +372 ｜ $6.82 ｜ 名义 $253.7k* ｜ -7.9%
结构参考：210（+1.8%）上方 / 100（-51.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 6.8k / P 10.7k
ΔOI:      C -41 / P +1.1k
ATM:      C 17.50 / P 16.90
ATM IV:   78.0%
ΔOI Δ Exposure*: -22k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 280 ｜ +586 ｜ $2.06 ｜ 名义 $120.7k* ｜ +35.7%
C 300 ｜ -482 ｜ $1.31 ｜ 名义 $-63.1k* ｜ +45.4%
P 200 ｜ +288 ｜ $14.28 ｜ 名义 $411.3k* ｜ -3.1%
结构参考：280（+35.7%）上方 / 200（-3.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 83.2% vs 09-11 75.7%（差 +7.5pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/NBIS_evening.json