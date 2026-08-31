# 期权晨报 2026-08-31

📊 市场环境

SPY $765.88 ｜ QQQ $713.51
VIX 15.33 ↑6.2%（5D -3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 50.1（neutral）
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
🟡 **事件差分**: 09-04 ATM IV 76.9% vs 09-11 66.4%（差 +10.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-11 133C ΔOI +3,533（距现价 +4.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MSTR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
MSTR  昨收 127.31 → 今晨 127.01（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 128.87 ｜ 低 125.74

Options: P/C量 0.77 | OI比 0.69 | ATM IV 76.9% | Skew -4.3pp | Term 0.90 | ExpMove ±6.6%（近端） | Rank 43%
   ⇒ Put/Call Volume: 0.77×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.69×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±6.6% ｜ 09-11（11D）±9.3% ｜ 09-18（18D）±12.1% ｜ 09-25（25D）±13.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 112.03（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 928 / LOW 87 / INVALID 315
结构观察区: Primary Flip 112.03（全链重定价，覆盖 100%）
最近结构参考: Flip 112（现价高于该位 13.4%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 112（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 137.0C — Vol 90 | 最新价 $1.29 | OI 673→19682 (ΔOI +19009张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增19009张（+2824.5% vs前日OI），连续性待观察（方向未知）
09-04 70.0P — Vol 6 | 最新价 $0.02 | OI 6445→21942 (ΔOI +15497张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15497张（+240.4% vs前日OI），连续性待观察（方向未知）
09-04 136.0C — Vol 387 | 最新价 $1.54 | OI 406→15135 (ΔOI +14729张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14729张（+3627.8% vs前日OI），连续性待观察（方向未知）
09-11 80.0P — Vol 21 | 最新价 $0.10 | OI 2323→16339 (ΔOI +14016张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增14016张（+603.4% vs前日OI），连续性待观察（方向未知）
09-04 130.0C — Vol 1,231 | 最新价 $2.92 | OI 2321→13573 (ΔOI +11252张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增11252张（+484.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +109.3k / P +39.3k ｜ Activity HIGH ｜ 4D
09-11  C +9.6k / P +18.5k ｜ Activity HIGH ｜ 11D
09-18  C +5.8k / P +4.1k ｜ Activity HIGH ｜ 18D
09-25  C +1.6k / P +1.6k ｜ Activity HIGH ｜ 25D

📆 09-04 Forward Structure
OI:       C 243.0k / P 167.4k
ΔOI:      C +109.3k / P +39.3k
ATM:      C 4.25 / P 4.12
ATM IV:   76.9%
ΔOI Δ Exposure*: 2.8M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 137 ｜ +19,009 ｜ $1.29 ｜ 名义 $2.45M* ｜ +7.9%
P 70 ｜ +15,497 ｜ $0.02 ｜ 名义 $31.0k* ｜ -44.9%
C 136 ｜ +14,729 ｜ $1.54 ｜ 名义 $2.27M* ｜ +7.1%
结构参考：137（+7.9%）上方 / 70（-44.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 33.0k / P 68.8k
ΔOI:      C +9.6k / P +18.5k
ATM:      C 6.00 / P 5.87
ATM IV:   66.4%
ΔOI Δ Exposure*: 189k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 80 ｜ +14,016 ｜ $0.10 ｜ 名义 $140.2k* ｜ -37.0%
C 133 ｜ +3,533 ｜ $3.60 ｜ 名义 $1.27M* ｜ +4.7%
C 138 ｜ +3,465 ｜ $2.47 ｜ 名义 $855.9k* ｜ +8.7%
结构参考：133（+4.7%）上方 / 80（-37.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 263.5k / P 180.1k
ΔOI:      C +5.8k / P +4.1k
ATM:      C 7.78 / P 7.64
ATM IV:   67.3%
ΔOI Δ Exposure*: 10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 160 ｜ +1,121 ｜ $1.17 ｜ 名义 $131.2k* ｜ +26.0%
C 150 ｜ +982 ｜ $1.93 ｜ 名义 $189.5k* ｜ +18.1%
P 120 ｜ +727 ｜ $4.35 ｜ 名义 $316.2k* ｜ -5.5%
结构参考：160（+26.0%）上方 / 120（-5.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 15.5k / P 18.9k
ΔOI:      C +1.6k / P +1.6k
ATM:      C 9.00 / P 8.68
ATM IV:   67.9%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 127 ｜ +522 ｜ $9.00 ｜ 名义 $469.8k* ｜ -0.0%
P 137 ｜ +373 ｜ $15.70 ｜ 名义 $585.6k* ｜ +7.9%
P 115 ｜ +324 ｜ $4.00 ｜ 名义 $129.6k* ｜ -9.5%
结构参考：137（+7.9%）上方 / 115（-9.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 76.9% vs 09-11 66.4%（差 +10.4pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/MSTR_morning.json