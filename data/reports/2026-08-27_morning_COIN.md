# 期权晨报 2026-08-27

📊 市场环境

SPY $771.10 ｜ QQQ $721.11
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.2（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911

🔍 重点速览
🔴 **事件差分**: 08-28（1D）ATM IV 88.1% vs 09-04 69.6%（差 +18.6pp），覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **单日价格波动**: +4.7%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 08-28 200C ΔOI -1,679（距现价 +4.3%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 183.10 → 今晨 191.70（+4.7%） | 较昨收变动（含盘初走势） ｜ 今日高 193.60 ｜ 低 180.11

Options: P/C量 0.46 | OI比 0.76 | ATM IV 88.1% | Skew -5.9pp | Term 0.76 | ExpMove ±4.1%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.46×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.76×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±4.1% ｜ 09-04（8D）±8.5% ｜ 09-11（15D）±12.2% ｜ 09-18（22D）±13.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 171.22（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 93%（带内） ｜ IV 有效性: VALID 533 / LOW 178 / INVALID 371
结构观察区: ≈171（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 100: +91.7% | 距 Call Wall 200: -4.2%
最近结构参考: Call Wall 200（距现价 -4.2%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall）；上方 200（Call Wall）。
• Gamma 区域：切换参考 171（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 185.0C — Vol 172 | 最新价 $11.64 | OI 522→3552 (ΔOI +3030张) | ΔOI/Volume 1761.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3030张（+580.5% vs前日OI），连续性待观察（方向未知）
09-04 192.5C — Vol 150 | 最新价 $8.01 | OI 269→2164 (ΔOI +1895张) | ΔOI/Volume 1263.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1895张（+704.5% vs前日OI），连续性待观察（方向未知）
09-18 75.0P — Vol 0 | 最新价 $0.05 | OI 664→2323 (ΔOI +1659张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1659张（+249.8% vs前日OI），连续性待观察（方向未知）
08-28 210.0C — Vol 978 | 最新价 $0.40 | OI 2534→3713 (ΔOI +1179张) | ΔOI/Volume 120.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1179张（+46.5% vs前日OI），连续性待观察（方向未知）
09-04 190.0C — Vol 588 | 最新价 $8.70 | OI 1218→1871 (ΔOI +653张) | ΔOI/Volume 111.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增653张（+53.6% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C -2.4k / P -2.2k ｜ Activity MEDIUM △ ｜ 1D
09-04  C +6.3k / P +1.0k ｜ Activity HIGH ｜ 8D
09-11  C +0.7k / P +0.2k ｜ Activity HIGH ｜ 15D
09-18  C +0.4k / P +2.6k ｜ Activity HIGH ｜ 22D

   Top ΔOI: 200C -1,679 ｜ 170P -1,241

📆 09-04 Forward Structure
OI:       C 29.8k / P 19.9k
ΔOI:      C +6.3k / P +1.0k
ATM:      C 8.01 / P 8.20
ATM IV:   69.6%
ΔOI Δ Exposure*: 339k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 185 ｜ +3,030 ｜ $11.64 ｜ 名义 $3.53M* ｜ -3.5%
C 192 ｜ +1,895 ｜ $8.01 ｜ 名义 $1.52M* ｜ +0.4%
C 190 ｜ +653 ｜ $8.70 ｜ 名义 $568.1k* ｜ -0.9%
结构参考：192（+0.4%）上方 / 185（-3.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 9.4k / P 7.4k
ΔOI:      C +0.7k / P +0.2k
ATM:      C 10.30 / P 13.08
ATM IV:   65.9%
ΔOI Δ Exposure*: 30k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 185 ｜ +363 ｜ $13.65 ｜ 名义 $495.5k* ｜ -3.5%
C 205 ｜ +184 ｜ $5.55 ｜ 名义 $102.1k* ｜ +6.9%
C 190 ｜ -107 ｜ $10.82 ｜ 名义 $-115.8k* ｜ -0.9%
结构参考：205（+6.9%）上方 / 185（-3.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 166.7k / P 75.4k
ΔOI:      C +0.4k / P +2.6k
ATM:      C 12.45 / P 13.00
ATM IV:   67.0%
ΔOI Δ Exposure*: -10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 75 ｜ +1,659 ｜ $0.05 ｜ 名义 $8.3k* ｜ -60.9%
P 105 ｜ +400 ｜ $0.10 ｜ 名义 $4.0k* ｜ -45.2%
C 260 ｜ +256 ｜ $1.14 ｜ 名义 $29.2k* ｜ +35.6%
结构参考：260（+35.6%）上方 / 75（-60.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 88.1% vs 09-04 69.6%（差 +18.6pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/COIN_morning.json