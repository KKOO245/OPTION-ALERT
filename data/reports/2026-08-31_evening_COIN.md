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
🟡 **单日价格波动**: +5.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 190C ΔOI +3,604（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
COIN: 今开 178.56 → 收盘 188.12（+5.4%） ｜ 今日高 189.95 ｜ 低 176.73
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.33 | OI比 0.44 | ATM IV 71.9% | Skew -5.6pp | Term 0.90 | ExpMove ±6.1%（近端） | Rank 36%
   ⇒ Put/Call Volume: 0.33×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±6.1% ｜ 09-11（11D）±8.7% ｜ 09-18（18D）±10.6% ｜ 09-25（25D）±13.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 29,378,728 | GEX Change vs 上次快照 3,396,793 | Flip: Primary Flip: 160.08（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 565 / LOW 170 / INVALID 309
结构观察区: Primary Flip 160.08（全链重定价，覆盖 100%）
Call Wall 200（弱结构｜现价低于该位 5.9%）
最近结构参考: Call Wall 200（现价低于该位 5.9%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 160（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 200.0C — Vol 10,140 | 最新价 $2.03 | OI 2744→10657 (ΔOI +7913张) | ΔOI/Volume 78.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7913张（+288.4% vs前日OI），连续性待观察（方向未知）
09-18 100.0P — Vol 1,792 | 最新价 $0.07 | OI 3354→7329 (ΔOI +3975张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3975张（+118.5% vs前日OI），连续性待观察（方向未知）
09-04 190.0C — Vol 7,103 | 最新价 $5.00 | OI 1977→5581 (ΔOI +3604张) | ΔOI/Volume 50.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3604张（+182.3% vs前日OI），连续性待观察（方向未知）
09-04 192.5C — Vol 1,681 | 最新价 $4.00 | OI 2181→4724 (ΔOI +2543张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2543张（+116.6% vs前日OI），连续性待观察（方向未知）
09-04 185.0C — Vol 6,314 | 最新价 $7.45 | OI 3506→5984 (ΔOI +2478张) | ΔOI/Volume 39.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2478张（+70.7% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +19.3k / P +6.2k ｜ Activity HIGH ｜ 4D
09-11  C +0.5k / P +2.2k ｜ Activity HIGH ｜ 11D
09-18  C +1.5k / P +5.2k ｜ Activity HIGH ｜ 18D
09-25  C +70 / P +0.3k ｜ Activity MEDIUM △ ｜ 25D

📆 09-04 Forward Structure
OI:       C 72.6k / P 32.0k
ΔOI:      C +19.3k / P +6.2k
ATM:      C 6.20 / P 5.27
ATM IV:   71.9%
ΔOI Δ Exposure*: 710k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 200 ｜ +7,913 ｜ $2.03 ｜ 名义 $1.61M* ｜ +6.3%
C 190 ｜ +3,604 ｜ $5.00 ｜ 名义 $1.80M* ｜ +1.0%
C 192 ｜ +2,543 ｜ $4.00 ｜ 名义 $1.02M* ｜ +2.3%
结构参考：200（+6.3%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 12.2k / P 9.9k
ΔOI:      C +0.5k / P +2.2k
ATM:      C 8.79 / P 7.60
ATM IV:   63.0%
ΔOI Δ Exposure*: 18k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 115 ｜ +1,467 ｜ $0.08 ｜ 名义 $11.7k* ｜ -38.9%
C 205 ｜ -335 ｜ $3.15 ｜ 名义 $-105.5k* ｜ +9.0%
P 165 ｜ +196 ｜ $1.10 ｜ 名义 $21.6k* ｜ -12.3%
结构参考：115（-38.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 168.9k / P 80.0k
ΔOI:      C +1.5k / P +5.2k
ATM:      C 11.20 / P 8.75
ATM IV:   64.3%
ΔOI Δ Exposure*: 21k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 100 ｜ +3,975 ｜ $0.07 ｜ 名义 $27.8k* ｜ -46.8%
P 120 ｜ +467 ｜ $0.11 ｜ 名义 $5.1k* ｜ -36.2%
C 205 ｜ +342 ｜ $5.49 ｜ 名义 $187.8k* ｜ +9.0%
结构参考：205（+9.0%）上方 / 100（-46.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 110P +102 ｜ 210C +68

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 71.9% vs 09-11 63.0%（差 +9.0pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/COIN_evening.json