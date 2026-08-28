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
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **单日价格波动**: -5.2%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 1465P ΔOI +865（距现价 -0.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
SNDK  昨收 1,553.01 → 今晨 1,471.95（-5.2%） | 较昨收变动（含盘初走势） ｜ 今日高 1557.89 ｜ 低 1456.00

Options: P/C量 0.53 | OI比 0.70 | ATM IV 82.6% | Skew -2.3pp | Term 0.88 | ExpMove ±3.8%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±3.8% ｜ 09-04（8D）±8.9% ｜ 09-11（15D）±12.2% ｜ 09-18（22D）±13.8%
   ⇒ IV–VIX Spread: +68.1pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 1481.58（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2225 / LOW 573 / INVALID 952
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: ≈1482（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 800: +84.0% | 距 Call Wall 1,700: -13.4%
最近结构参考: Flip 1482（距现价 -0.6%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 800（Put Wall）；上方 1,700（Call Wall）。
• Gamma 区域：切换参考 1482（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 1700.0C — Vol 7,111 | 最新价 $0.39 | OI 6535→8127 (ΔOI +1592张) | ΔOI/Volume 22.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1592张（+24.4% vs前日OI），连续性待观察（方向未知）
09-04 1280.0P — Vol 25 | 最新价 $7.70 | OI 75→944 (ΔOI +869张) | ΔOI/Volume 3476.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增869张（+1158.7% vs前日OI），连续性待观察（方向未知）
09-04 1465.0P — Vol 16 | 最新价 $58.78 | OI 27→892 (ΔOI +865张) | ΔOI/Volume 5406.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增865张（+3203.7% vs前日OI），连续性待观察（方向未知）
09-04 1720.0C — Vol 57 | 最新价 $9.80 | OI 80→926 (ΔOI +846张) | ΔOI/Volume 1484.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增846张（+1057.5% vs前日OI），连续性待观察（方向未知）
08-28 1650.0C — Vol 1,834 | 最新价 $0.90 | OI 1449→2042 (ΔOI +593张) | ΔOI/Volume 32.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增593张（+40.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +7.6k / P +1.4k ｜ Activity HIGH ｜ 1D
09-04  C +2.9k / P +2.3k ｜ Activity HIGH ｜ 8D
09-11  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 15D
09-18  C +0.6k / P +0.1k ｜ Activity HIGH ｜ 22D

📆 08-28 Forward Structure
OI:       C 72.9k / P 51.3k
ΔOI:      C +7.6k / P +1.4k
ATM:      C 29.32 / P 26.69
ATM IV:   82.6%
ΔOI Δ Exposure*: 62k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1700 ｜ +1,592 ｜ $0.39 ｜ 名义 $62.1k* ｜ +15.5%
C 1650 ｜ +593 ｜ $0.90 ｜ 名义 $53.4k* ｜ +12.1%
C 1600 ｜ +571 ｜ $2.39 ｜ 名义 $136.5k* ｜ +8.7%
结构参考：1700（+15.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 20.0k / P 19.0k
ΔOI:      C +2.9k / P +2.3k
ATM:      C 67.00 / P 63.67
ATM IV:   75.1%
ΔOI Δ Exposure*: 2k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1280 ｜ +869 ｜ $7.70 ｜ 名义 $669.1k* ｜ -13.0%
P 1465 ｜ +865 ｜ $58.78 ｜ 名义 $5.08M* ｜ -0.5%
C 1720 ｜ +846 ｜ $9.80 ｜ 名义 $829.1k* ｜ +16.9%
结构参考：1720（+16.9%）上方 / 1280（-13.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 1440C +56 ｜ 1460C +45

📆 09-18 Forward Structure
OI:       C 52.0k / P 68.3k
ΔOI:      C +0.6k / P +0.1k
ATM:      C 108.81 / P 95.00
ATM IV:   71.8%
ΔOI Δ Exposure*: 8k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 2000 ｜ -288 ｜ $7.95 ｜ 名义 $-229.0k* ｜ +35.9%
P 1600 ｜ -268 ｜ $175.88 ｜ 名义 $-4.71M* ｜ +8.7%
C 3500 ｜ +224 ｜ $0.10 ｜ 名义 $2.2k* ｜ +137.8%
结构参考：3500（+137.8%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 82.6% vs 09-04 75.1%（差 +7.5pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=2 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=2）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/SNDK_morning.json