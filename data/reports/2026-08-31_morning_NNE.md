# 期权晨报 2026-08-31

📊 市场环境

SPY $765.66 ｜ QQQ $715.06
VIX 15.22 ↑5.5%（5D -4.0%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 49.9（neutral）
全市场 P/C OI（OCC 结算 08-28，2023-06 以来）: Equity 0.75（分位 12%） ｜ Index 0.94（分位 11%）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周二 09-01 10:00　【高】职位空缺(JOLTS) Job Openings　预测 7.3 ｜ 实际 待公布 ｜ 前值 7.359
- 周二 09-01 10:00　【高】ISM 制造业 PMI　预测 55.2 ｜ 实际 待公布 ｜ 前值 55.6
- 周四 09-03 10:00　【高】ISM 非制造业 PMI　预测 54.3 ｜ 实际 待公布 ｜ 前值 54.1
- 周五 09-04 08:30　【高】Non Farm Payrolls　预测 58 ｜ 实际 待公布 ｜ 前值 -23
- 周五 09-04 08:30　【高】失业率　预测 4.1 ｜ 实际 待公布 ｜ 前值 4.1

🔍 重点速览
🔴 **事件差分**: 09-04（4D）ATM IV 90.6% vs 09-11 73.6%（差 +17.1pp），覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🔴 **Vol Regime 升档**: LOW → NORMAL（vol_regime_v1）
   ⇒ 波动环境升档仅作环境标签，不判方向、不参与 Gate
🟡 **近现价集中开仓**: 09-11 18P ΔOI +188（距现价 +1.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## NNE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NNE  昨收 17.97 → 今晨 18.23（+1.4%） | 较昨收变动（含盘初走势） ｜ 今日高 18.38 ｜ 低 17.80

Options: P/C量 0.29 | OI比 0.76 | ATM IV 90.6% | Skew 7.3pp | Term 0.94 | ExpMove ±8.0%（近端） | Rank 16%
   ⇒ Put/Call Volume: 0.29×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±8.0% ｜ 09-11（11D）±10.9% ｜ 09-18（18D）±14.0% ｜ 09-25（25D）±16.7%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 816,957 | GEX Change vs 上次快照 79,646 | Flip: Primary Flip: 17.07（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 214 / LOW 66 / INVALID 186
结构观察区: Primary Flip 17.07（全链重定价，覆盖 100%）
最近结构参考: Flip 17（现价高于该位 6.8%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 22.5C — Vol 2,303 | 最新价 $0.55 | OI 44→2023 (ΔOI +1979张) | ΔOI/Volume 85.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1979张（+4497.7% vs前日OI），连续性待观察（方向未知）
09-11 16.0P — Vol 189 | 最新价 $0.25 | OI 194→383 (ΔOI +189张) | ΔOI/Volume 100.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增189张（+97.4% vs前日OI），连续性待观察（方向未知）
09-11 18.5P — Vol 189 | 最新价 $1.18 | OI 56→244 (ΔOI +188张) | ΔOI/Volume 99.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增188张（+335.7% vs前日OI），连续性待观察（方向未知）
09-04 16.0P — Vol 131 | 最新价 $0.11 | OI 470→600 (ΔOI +130张) | ΔOI/Volume 99.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增130张（+27.7% vs前日OI），连续性待观察（方向未知）
09-18 18.0P — Vol 167 | 最新价 $1.40 | OI 573→695 (ΔOI +122张) | ΔOI/Volume 73.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增122张（+21.3% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +0.1k / P +0.6k ｜ Activity HIGH ｜ 4D
09-11  C +68 / P +0.6k ｜ Activity HIGH ｜ 11D
09-18  C -31 / P +0.4k ｜ Activity MEDIUM △ ｜ 18D
09-25  C -6 / P +38 ｜ Activity LOW ｜ 25D

📆 09-04 Forward Structure
OI:       C 2.4k / P 1.8k
ΔOI:      C +0.1k / P +0.6k
ATM:      C 0.85 / P 0.60
ATM IV:   90.6%
ΔOI Δ Exposure*: -14k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +130 ｜ $0.15 ｜ 名义 $1.9k* ｜ -12.2%
P 17 ｜ +121 ｜ $0.38 ｜ 名义 $4.6k* ｜ -4.0%
P 17 ｜ +69 ｜ $0.27 ｜ 名义 $1.9k* ｜ -6.7%
结构参考：16（-12.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.2k / P 1.5k
ΔOI:      C +68 / P +0.6k
ATM:      C 1.13 / P 0.85
ATM IV:   73.6%
ΔOI Δ Exposure*: -21k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 16 ｜ +189 ｜ $0.32 ｜ 名义 $6.0k* ｜ -12.2%
P 18 ｜ +188 ｜ $1.18 ｜ 名义 $22.2k* ｜ +1.5%
P 20 ｜ +84 ｜ $2.52 ｜ 名义 $21.2k* ｜ +12.5%
结构参考：18（+1.5%）上方 / 16（-12.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 18P +122 ｜ 26P +94

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 90.6% vs 09-11 73.6%（差 +17.1pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/NNE_morning.json