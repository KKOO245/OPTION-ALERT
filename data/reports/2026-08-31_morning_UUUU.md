# 期权晨报 2026-08-31

📊 市场环境

SPY $767.34 ｜ QQQ $716.76
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
🟡 **近现价集中开仓**: 09-04 15C ΔOI +369（距现价 +2.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## UUUU

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
UUUU  昨收 14.67 → 今晨 14.71（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 14.77 ｜ 低 14.35

Options: P/C量 0.18 | OI比 0.41 | ATM IV 74.6% | Skew -1.0pp | Term 0.96 | ExpMove ±6.7%（近端） | Rank 52%
   ⇒ Put/Call Volume: 0.18×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.41×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±6.7% ｜ 09-11（11D）±9.4% ｜ 09-18（18D）±12.8% ｜ 09-25（25D）±15.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 4,056,288 | GEX Change vs 上次快照 388,440 | Flip: Primary Flip: 12.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 188 / LOW 49 / INVALID 169
结构观察区: Primary Flip 12.58（全链重定价，覆盖 100%）
最近结构参考: Flip 13（现价高于该位 17.0%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 13（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-18 16.0C — Vol 40 | 最新价 $0.41 | OI 1126→2122 (ΔOI +996张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增996张（+88.5% vs前日OI），连续性待观察（方向未知）
09-04 15.0C — Vol 258 | 最新价 $0.36 | OI 922→1291 (ΔOI +369张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增369张（+40.0% vs前日OI），值得跟踪（方向未知）
09-04 15.0P — Vol 10 | 最新价 $0.72 | OI 329→495 (ΔOI +166张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增166张（+50.5% vs前日OI），值得跟踪（方向未知）
09-04 16.0C — Vol 13 | 最新价 $0.12 | OI 2410→2553 (ΔOI +143张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增143张（+5.9% vs前日OI），值得跟踪（方向未知）
09-04 14.5P — Vol 13 | 最新价 $0.40 | OI 517→659 (ΔOI +142张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增142张（+27.5% vs前日OI），值得跟踪（方向未知）
📆 Forward Expiration Structure

09-04  C +0.9k / P +0.5k ｜ Activity HIGH ｜ 4D
09-11  C +0.3k / P +0.2k ｜ Activity HIGH ｜ 11D
09-18  C +0.9k / P +0.2k ｜ Activity MEDIUM △ ｜ 18D
09-25  C +0.1k / P +0.1k ｜ Activity MEDIUM △ ｜ 25D

📆 09-04 Forward Structure
OI:       C 8.9k / P 3.7k
ΔOI:      C +0.9k / P +0.5k
ATM:      C 0.60 / P 0.39
ATM IV:   74.6%
ΔOI Δ Exposure*: 6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 15 ｜ +369 ｜ $0.30 ｜ 名义 $11.1k* ｜ +2.0%
P 15 ｜ +166 ｜ $0.65 ｜ 名义 $10.8k* ｜ +2.0%
C 16 ｜ +143 ｜ $0.10 ｜ 名义 $1.4k* ｜ +8.8%
结构参考：15（+2.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 3.2k / P 2.7k
ΔOI:      C +0.3k / P +0.2k
ATM:      C 0.79 / P 0.59
ATM IV:   66.0%
ΔOI Δ Exposure*: -4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 16 ｜ +109 ｜ $0.29 ｜ 名义 $3.2k* ｜ +8.8%
P 15 ｜ +76 ｜ $0.93 ｜ 名义 $7.1k* ｜ +2.0%
C 14 ｜ +53 ｜ $1.10 ｜ 名义 $5.8k* ｜ -4.8%
结构参考：16（+8.8%）上方 / 14（-4.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 16C +996 ｜ 18C -166

   Top ΔOI: 17C +111 ｜ 12P +45

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 74.6% vs 09-11 66.0%（差 +8.5pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/UUUU_morning.json