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
🟡 **单日价格波动**: +4.7%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 09-04 ATM IV 80.5% vs 09-11 68.9%（差 +11.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 137C ΔOI +19,009（距现价 +3.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
MSTR: 今开 128.57 → 收盘 132.94（+3.4%） ｜ 今日高 133.38 ｜ 低 125.74
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.45 | OI比 0.69 | ATM IV 80.5% | Skew -6.3pp | Term 0.86 | ExpMove ±6.7%（近端） | Rank 50%
   ⇒ Put/Call Volume: 0.45×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±6.7% ｜ 09-11（11D）±9.7% ｜ 09-18（18D）±12.7% ｜ 09-25（25D）±14.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 80,521,315 | GEX Change vs 上次快照 8,157,211 | Flip: NO_CROSS
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 913 / LOW 115 / INVALID 302
结构观察区: NO_CROSS
🧭 结构解读（全部依赖上方假设）
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 137.0C — Vol 1,492 | 最新价 $2.90 | OI 673→19682 (ΔOI +19009张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19009张（+2824.5% vs前日OI），连续性待观察（方向未知）
09-04 70.0P — Vol 150 | 最新价 $0.01 | OI 6445→21942 (ΔOI +15497张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15497张（+240.4% vs前日OI），连续性待观察（方向未知）
09-04 136.0C — Vol 2,659 | 最新价 $3.20 | OI 406→15135 (ΔOI +14729张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14729张（+3627.8% vs前日OI），连续性待观察（方向未知）
09-11 80.0P — Vol 92 | 最新价 $0.07 | OI 2323→16339 (ΔOI +14016张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14016张（+603.4% vs前日OI），连续性待观察（方向未知）
09-04 130.0C — Vol 13,683 | 最新价 $6.00 | OI 2321→13573 (ΔOI +11252张) | ΔOI/Volume 82.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11252张（+484.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +109.3k / P +39.3k ｜ Activity HIGH ｜ 4D
09-11  C +9.6k / P +18.5k ｜ Activity HIGH ｜ 11D
09-18  C +5.8k / P +4.1k ｜ Activity HIGH ｜ 18D
09-25  C +1.6k / P +1.6k ｜ Activity HIGH ｜ 25D

📆 09-04 Forward Structure
OI:       C 243.0k / P 167.4k
ΔOI:      C +109.3k / P +39.3k
ATM:      C 4.46 / P 4.40
ATM IV:   80.5%
ΔOI Δ Exposure*: 4.6M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 137 ｜ +19,009 ｜ $2.90 ｜ 名义 $5.51M* ｜ +3.1%
P 70 ｜ +15,497 ｜ $0.01 ｜ 名义 $15.5k* ｜ -47.3%
C 136 ｜ +14,729 ｜ $3.20 ｜ 名义 $4.71M* ｜ +2.3%
结构参考：137（+3.1%）上方 / 70（-47.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 33.0k / P 68.8k
ΔOI:      C +9.6k / P +18.5k
ATM:      C 6.60 / P 6.30
ATM IV:   68.9%
ΔOI Δ Exposure*: 355k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 80 ｜ +14,016 ｜ $0.07 ｜ 名义 $98.1k* ｜ -39.8%
C 133 ｜ +3,533 ｜ $6.60 ｜ 名义 $2.33M* ｜ +0.0%
C 138 ｜ +3,465 ｜ $4.35 ｜ 名义 $1.51M* ｜ +3.8%
结构参考：138（+3.8%）上方 / 80（-39.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 263.5k / P 180.1k
ΔOI:      C +5.8k / P +4.1k
ATM:      C 8.32 / P 8.62
ATM IV:   69.8%
ΔOI Δ Exposure*: 77k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 160 ｜ +1,121 ｜ $1.94 ｜ 名义 $217.5k* ｜ +20.4%
C 150 ｜ +982 ｜ $3.20 ｜ 名义 $314.2k* ｜ +12.8%
P 120 ｜ +727 ｜ $2.87 ｜ 名义 $208.6k* ｜ -9.7%
结构参考：160（+20.4%）上方 / 120（-9.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 15.5k / P 18.9k
ΔOI:      C +1.6k / P +1.6k
ATM:      C 9.54 / P 9.50
ATM IV:   69.4%
ΔOI Δ Exposure*: 32k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 127 ｜ +522 ｜ $12.60 ｜ 名义 $657.7k* ｜ -4.5%
P 137 ｜ +373 ｜ $15.70 ｜ 名义 $585.6k* ｜ +3.1%
P 115 ｜ +324 ｜ $2.56 ｜ 名义 $82.9k* ｜ -13.5%
结构参考：137（+3.1%）上方 / 127（-4.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 80.5% vs 09-11 68.9%（差 +11.7pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/MSTR_evening.json