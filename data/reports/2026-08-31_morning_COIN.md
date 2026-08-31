# 期权晨报 2026-08-31

📊 市场环境

SPY $767.44 ｜ QQQ $716.76
VIX 15.16 ↑5.1%（5D -4.3%） ｜ Vol Regime: NORMAL
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
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **单日价格波动**: +3.4%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 190C ΔOI +3,604（距现价 +2.8%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 178.64 → 今晨 184.76（+3.4%） | 较昨收变动（含盘初走势） ｜ 今日高 185.88 ｜ 低 176.73

Options: P/C量 0.31 | OI比 0.44 | ATM IV 67.1% | Skew -5.7pp | Term 0.93 | ExpMove ±5.8%（近端） | Rank 25%
   ⇒ Put/Call Volume: 0.31×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.44×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±5.8% ｜ 09-11（11D）±8.6% ｜ 09-18（18D）±11.2% ｜ 09-25（25D）±13.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 25,981,935 | GEX Change vs 上次快照 11,002,740 | Flip: Primary Flip: 162.86（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 506 / LOW 160 / INVALID 378
结构观察区: Primary Flip 162.86（全链重定价，覆盖 99%）
Call Wall 200（弱结构｜现价低于该位 7.6%）
最近结构参考: Call Wall 200（现价低于该位 7.6%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 163（全链重定价，覆盖 99%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 200.0C — Vol 450 | 最新价 $0.59 | OI 2744→10657 (ΔOI +7913张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增7913张（+288.4% vs前日OI），连续性待观察（方向未知）
09-18 100.0P — Vol 1 | 最新价 $0.16 | OI 3354→7329 (ΔOI +3975张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3975张（+118.5% vs前日OI），连续性待观察（方向未知）
09-04 190.0C — Vol 270 | 最新价 $1.53 | OI 1977→5581 (ΔOI +3604张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3604张（+182.3% vs前日OI），连续性待观察（方向未知）
09-04 192.5C — Vol 33 | 最新价 $1.18 | OI 2181→4724 (ΔOI +2543张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2543张（+116.6% vs前日OI），连续性待观察（方向未知）
09-04 185.0C — Vol 327 | 最新价 $2.60 | OI 3506→5984 (ΔOI +2478张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2478张（+70.7% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +19.3k / P +6.2k ｜ Activity HIGH ｜ 4D
09-11  C +0.5k / P +2.2k ｜ Activity HIGH ｜ 11D
09-18  C +1.5k / P +5.2k ｜ Activity HIGH ｜ 18D
09-25  C +70 / P +0.3k ｜ Activity MEDIUM △ ｜ 25D

📆 09-04 Forward Structure
OI:       C 72.6k / P 32.0k
ΔOI:      C +19.3k / P +6.2k
ATM:      C 5.35 / P 5.29
ATM IV:   67.1%
ΔOI Δ Exposure*: 545k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 200 ｜ +7,913 ｜ $1.30 ｜ 名义 $1.03M* ｜ +8.2%
C 190 ｜ +3,604 ｜ $3.45 ｜ 名义 $1.24M* ｜ +2.8%
C 192 ｜ +2,543 ｜ $2.52 ｜ 名义 $640.8k* ｜ +4.2%
结构参考：200（+8.2%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 12.2k / P 9.9k
ΔOI:      C +0.5k / P +2.2k
ATM:      C 7.82 / P 8.00
ATM IV:   60.2%
ΔOI Δ Exposure*: 15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 115 ｜ +1,467 ｜ $0.04 ｜ 名义 $5.9k* ｜ -37.8%
C 205 ｜ -335 ｜ $2.17 ｜ 名义 $-72.7k* ｜ +11.0%
P 165 ｜ +196 ｜ $1.48 ｜ 名义 $29.0k* ｜ -10.7%
结构参考：115（-37.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 168.9k / P 80.0k
ΔOI:      C +1.5k / P +5.2k
ATM:      C 10.43 / P 10.36
ATM IV:   62.1%
ΔOI Δ Exposure*: 15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 100 ｜ +3,975 ｜ $0.07 ｜ 名义 $27.8k* ｜ -45.9%
P 120 ｜ +467 ｜ $0.12 ｜ 名义 $5.6k* ｜ -35.1%
C 205 ｜ +342 ｜ $4.05 ｜ 名义 $138.5k* ｜ +11.0%
结构参考：205（+11.0%）上方 / 100（-45.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 110P +102 ｜ 210C +68

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 67.1% vs 09-11 60.2%（差 +6.9pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/COIN_morning.json