# 期权晨报 2026-08-31

📊 市场环境

SPY $767.25 ｜ QQQ $716.76
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
🟡 **事件差分**: 09-04 ATM IV 90.0% vs 09-11 79.7%（差 +10.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 18P ΔOI +1,640（距现价 -0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 17.99 → 今晨 18.04（+0.3%） | 较昨收变动（含盘初走势） ｜ 今日高 18.19 ｜ 低 17.68

Options: P/C量 0.32 | OI比 0.29 | ATM IV 90.0% | Skew -4.1pp | Term 0.94 | ExpMove ±7.7%（近端） | Rank 6%
   ⇒ Put/Call Volume: 0.32×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.29×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±7.7% ｜ 09-11（11D）±11.1% ｜ 09-18（18D）±14.3% ｜ 09-25（25D）±17.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 6,698,425 | GEX Change vs 上次快照 123,514 | Flip: Primary Flip: 16.64（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 260 / LOW 87 / INVALID 181
结构观察区: Primary Flip 16.64（全链重定价，覆盖 100%）
最近结构参考: Flip 17（现价高于该位 8.4%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 18.0P — Vol 1,765 | 最新价 $0.78 | OI 401→2041 (ΔOI +1640张) | ΔOI/Volume 92.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1640张（+409.0% vs前日OI），连续性待观察（方向未知）
09-18 25.0C — Vol 1,429 | 最新价 $0.11 | OI 7932→8830 (ΔOI +898张) | ΔOI/Volume 62.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增898张（+11.3% vs前日OI），连续性待观察（方向未知）
09-04 16.5P — Vol 848 | 最新价 $0.20 | OI 314→1069 (ΔOI +755张) | ΔOI/Volume 89.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增755张（+240.4% vs前日OI），连续性待观察（方向未知）
09-04 18.0C — Vol 856 | 最新价 $0.89 | OI 310→898 (ΔOI +588张) | ΔOI/Volume 68.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增588张（+189.7% vs前日OI），连续性待观察（方向未知）
09-04 17.0P — Vol 648 | 最新价 $0.34 | OI 556→1038 (ΔOI +482张) | ΔOI/Volume 74.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增482张（+86.7% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +2.8k / P +3.7k ｜ Activity HIGH ｜ 4D
09-11  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 11D
09-18  C +0.8k / P +39 ｜ Activity HIGH ｜ 18D
09-25  C +0.1k / P +0.2k ｜ Activity MEDIUM △ ｜ 25D

📆 09-04 Forward Structure
OI:       C 28.5k / P 8.2k
ΔOI:      C +2.8k / P +3.7k
ATM:      C 0.69 / P 0.70
ATM IV:   90.0%
ΔOI Δ Exposure*: -74k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 18 ｜ +1,640 ｜ $0.70 ｜ 名义 $114.8k* ｜ -0.2%
P 16 ｜ +755 ｜ $0.16 ｜ 名义 $12.1k* ｜ -8.5%
C 18 ｜ +588 ｜ $0.69 ｜ 名义 $40.6k* ｜ -0.2%
结构参考：18（-0.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 9.9k / P 2.2k
ΔOI:      C +0.6k / P +0.2k
ATM:      C 1.00 / P 1.00
ATM IV:   79.7%
ΔOI Δ Exposure*: -2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 25 ｜ +427 ｜ $0.05 ｜ 名义 $2.1k* ｜ +38.6%
C 18 ｜ +90 ｜ $1.00 ｜ 名义 $9.0k* ｜ -0.2%
P 18 ｜ +74 ｜ $1.19 ｜ 名义 $8.8k* ｜ +2.5%
结构参考：25（+38.6%）上方 / 18（-0.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 109.0k / P 63.9k
ΔOI:      C +0.8k / P +39
ATM:      C 1.30 / P 1.28
ATM IV:   81.5%
ΔOI Δ Exposure*: 34k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 25 ｜ +898 ｜ $0.09 ｜ 名义 $8.1k* ｜ +38.6%
C 19 ｜ +253 ｜ $0.92 ｜ 名义 $23.3k* ｜ +5.3%
C 22 ｜ -216 ｜ $0.30 ｜ 名义 $-6.5k* ｜ +22.0%
结构参考：25（+38.6%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 28C -74 ｜ 19C +59

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 90.0% vs 09-11 79.7%（差 +10.4pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/USAR_morning.json