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
🟡 **近现价集中开仓**: 09-04 18P ΔOI +1,640（距现价 +1.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## USAR

📋 Thesis Scorecard（今开/晨间条件 vs 收盘实况，只打事实勾）
USAR: 今开 17.83 → 收盘 17.82（-0.1%） ｜ 今日高 18.19 ｜ 低 17.59
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.44 | OI比 0.29 | ATM IV 86.4% | Skew -7.4pp | Term 0.92 | ExpMove ±7.1%（近端） | Rank 5%
   ⇒ Put/Call Volume: 0.44×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.29×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（4D）±7.1% ｜ 09-11（11D）±10.3% ｜ 09-18（18D）±13.8% ｜ 09-25（25D）±18.1%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) 5,017,926 | GEX Change vs 上次快照 -1,680,499 | Flip: Primary Flip: 16.82（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 252 / LOW 98 / INVALID 178
结构观察区: Primary Flip 16.82（全链重定价，覆盖 100%）
最近结构参考: Flip 17（现价高于该位 5.9%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 17（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 18.0P — Vol 330 | 最新价 $0.70 | OI 401→2041 (ΔOI +1640张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1640张（+409.0% vs前日OI），连续性待观察（方向未知）
09-18 25.0C — Vol 285 | 最新价 $0.08 | OI 7932→8830 (ΔOI +898张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增898张（+11.3% vs前日OI），值得跟踪（方向未知）
09-04 16.5P — Vol 680 | 最新价 $0.17 | OI 314→1069 (ΔOI +755张) | ΔOI/Volume N/A（量数据不完整） | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增755张（+240.4% vs前日OI），连续性待观察（方向未知）
09-04 18.0C — Vol 701 | 最新价 $0.56 | OI 310→898 (ΔOI +588张) | ΔOI/Volume 83.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增588张（+189.7% vs前日OI），连续性待观察（方向未知）
09-04 17.0P — Vol 647 | 最新价 $0.26 | OI 556→1038 (ΔOI +482张) | ΔOI/Volume 74.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增482张（+86.7% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +2.8k / P +3.7k ｜ Activity HIGH ｜ 4D
09-11  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 11D
09-18  C +0.8k / P +39 ｜ Activity MEDIUM △ ｜ 18D
09-25  C +0.1k / P +0.2k ｜ Activity HIGH ｜ 25D

📆 09-04 Forward Structure
OI:       C 28.5k / P 8.2k
ΔOI:      C +2.8k / P +3.7k
ATM:      C 0.56 / P 0.70
ATM IV:   86.4%
ΔOI Δ Exposure*: -90k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 18 ｜ +1,640 ｜ $0.70 ｜ 名义 $114.8k* ｜ +1.0%
P 16 ｜ +755 ｜ $0.17 ｜ 名义 $12.8k* ｜ -7.4%
C 18 ｜ +588 ｜ $0.56 ｜ 名义 $32.9k* ｜ +1.0%
结构参考：18（+1.0%）上方 / 16（-7.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 9.9k / P 2.2k
ΔOI:      C +0.6k / P +0.2k
ATM:      C 0.80 / P 1.04
ATM IV:   77.7%
ΔOI Δ Exposure*: -3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 25 ｜ +427 ｜ $0.03 ｜ 名义 $1.3k* ｜ +40.3%
C 18 ｜ +90 ｜ $0.80 ｜ 名义 $7.2k* ｜ +1.0%
P 18 ｜ +74 ｜ $1.19 ｜ 名义 $8.8k* ｜ +3.8%
结构参考：25（+40.3%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 25C +898 ｜ 19C +253

📆 09-25 Forward Structure
OI:       C 7.5k / P 2.7k
ΔOI:      C +0.1k / P +0.2k
ATM:      C 1.61 / P 1.61
ATM IV:   78.9%
ΔOI Δ Exposure*: -5k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 28 ｜ -74 ｜ $0.09 ｜ 名义 $-666* ｜ +57.1%
C 19 ｜ +59 ｜ $1.05 ｜ 名义 $6.2k* ｜ +6.6%
P 17 ｜ +54 ｜ $1.13 ｜ 名义 $6.1k* ｜ -4.6%
结构参考：19（+6.6%）上方 / 17（-4.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 86.4% vs 09-11 77.7%（差 +8.7pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/USAR_evening.json