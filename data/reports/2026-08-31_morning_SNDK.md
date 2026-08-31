# 期权晨报 2026-08-31

📊 市场环境

SPY $765.79 ｜ QQQ $714.42
VIX 15.33 ↑6.2%（5D -3.3%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 50.4（neutral）
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
🟡 **单日价格波动**: +2.9%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,484.98 → 今晨 1,528.00（+2.9%） | 较昨收变动（含盘初走势） ｜ 今日高 1540.93 ｜ 低 1484.00

Options: P/C量 0.49 | OI比 1.17 | ATM IV 75.9% | Skew -2.7pp | Term 0.92 | ExpMove ±6.6%（近端） | Rank 28%
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 1.17×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（4D）±6.5% ｜ 09-11（11D）±9.4% ｜ 09-18（18D）±12.7% ｜ 09-25（25D）±14.6%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 1526.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 1829 / LOW 517 / INVALID 1164
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: Primary Flip 1526.30（全链重定价，覆盖 100%）
Call Wall 1,500（弱结构｜现价高于该位 1.9%）
最近结构参考: Flip 1526（现价高于该位 0.1%）
🧭 结构解读（全部依赖上方假设）
• Gamma 区域：切换参考 1526（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 800.0P — Vol 0 | 最新价 $0.03 | OI 267→3003 (ΔOI +2736张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2736张（+1024.7% vs前日OI），连续性待观察（方向未知）
09-18 900.0C — Vol 0 | 最新价 $600.90 | OI 260→2190 (ΔOI +1930张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1930张（+742.3% vs前日OI），连续性待观察（方向未知）
09-04 1450.0P — Vol 455 | 最新价 $20.40 | OI 416→1599 (ΔOI +1183张) | ΔOI/Volume 260.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1183张（+284.4% vs前日OI），连续性待观察（方向未知）
09-04 1270.0P — Vol 76 | 最新价 $1.05 | OI 122→1294 (ΔOI +1172张) | ΔOI/Volume 1542.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1172张（+960.7% vs前日OI），连续性待观察（方向未知）
09-04 1715.0C — Vol 19 | 最新价 $6.24 | OI 25→1169 (ΔOI +1144张) | ΔOI/Volume 6021.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1144张（+4576.0% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +6.8k / P +12.6k ｜ Activity HIGH ｜ 4D
09-11  C +0.6k / P +0.7k ｜ Activity HIGH ｜ 11D
09-18  C +3.2k / P +0.1k ｜ Activity HIGH ｜ 18D
09-25  C +0.4k / P +1.0k ｜ Activity HIGH ｜ 25D

📆 09-04 Forward Structure
OI:       C 31.3k / P 36.8k
ΔOI:      C +6.8k / P +12.6k
ATM:      C 46.00 / P 53.65
ATM IV:   75.9%
ΔOI Δ Exposure*: 15k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 800 ｜ +2,736 ｜ $0.03 ｜ 名义 $8.2k* ｜ -47.6%
P 1450 ｜ +1,183 ｜ $20.40 ｜ 名义 $2.41M* ｜ -5.1%
P 1270 ｜ +1,172 ｜ $1.05 ｜ 名义 $123.1k* ｜ -16.9%
结构参考：800（-47.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 6.3k / P 10.2k
ΔOI:      C +0.6k / P +0.7k
ATM:      C 71.20 / P 72.40
ATM IV:   67.9%
ΔOI Δ Exposure*: 10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1375 ｜ +105 ｜ $18.32 ｜ 名义 $192.4k* ｜ -10.0%
P 1507 ｜ +72 ｜ $82.00 ｜ 名义 $590.4k* ｜ -1.3%
P 1200 ｜ +66 ｜ $2.27 ｜ 名义 $15.0k* ｜ -21.5%
结构参考：1375（-10.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 56.5k / P 68.6k
ΔOI:      C +3.2k / P +0.1k
ATM:      C 100.40 / P 93.82
ATM IV:   67.6%
ΔOI Δ Exposure*: 212k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 900 ｜ +1,930 ｜ $600.90 ｜ 名义 $115.97M* ｜ -41.1%
P 800 ｜ -449 ｜ $0.20 ｜ 名义 $-9.0k* ｜ -47.6%
P 900 ｜ +299 ｜ $0.21 ｜ 名义 $6.3k* ｜ -41.1%
结构参考：900（-41.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 4.6k / P 10.2k
ΔOI:      C +0.4k / P +1.0k
ATM:      C 113.11 / P 109.90
ATM IV:   68.5%
ΔOI Δ Exposure*: -8k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1200 ｜ +289 ｜ $11.00 ｜ 名义 $317.9k* ｜ -21.5%
P 1250 ｜ +149 ｜ $17.20 ｜ 名义 $256.3k* ｜ -18.2%
P 1430 ｜ +102 ｜ $75.98 ｜ 名义 $775.0k* ｜ -6.4%
结构参考：1200（-21.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 09-04（4D）ATM IV 75.9% vs 09-11 67.9%（差 +8.0pp）——覆盖 职位空缺(JOLTS) Job Openings、ISM 制造业 PMI 等
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-31/SNDK_morning.json