# 期权晚报 2026-08-26

📊 市场环境

SPY $770.35 ｜ QQQ $711.37
VIX 15.21 ↓1.6%（5D +2.1%） ｜ Vol Regime: NORMAL
CNN 恐惧贪婪 55.2（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周三 08-26 08:30　【高】Personal Spending MoM　预测 0.1 ｜ 实际 0.2 ｜ 前值 0.3　✅ 今日已公布
- 周三 08-26 08:30　【高】Personal Income MoM　预测 0.2 ｜ 实际 0.4 ｜ 前值 0.2　✅ 今日已公布
- 周三 08-26 08:30　【高】GDP 增速 Rate QoQ 2nd Est　预测 1.5 ｜ 实际 1.5 ｜ 前值 2.1　✅ 今日已公布
- 周三 08-26 08:30　【高】耐用品订单 Orders MoM　预测 0.5 ｜ 实际 1.1 ｜ 前值 0.5　✅ 今日已公布
- 周三 08-26 08:30　【高】PCE 物价 Price Index MoM　预测 0.2 ｜ 实际 0.2 ｜ 前值 0.1　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911


## TSLA

🔍 重点速览
🔴 **Gamma Regime 切换**: NEGATIVE → POSITIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 08-28 352P ΔOI +2,019（距现价 +1.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 395.1 / 400.0 / 418.9）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
TSLA: 今晨 344.09 → 收盘 347.79（+1.1%） ｜ 今日高 351.93 ｜ 低 342.53
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.87 | OI比 0.58 | ATM IV 40.6% | Skew -1.1pp | Term 0.99 | ExpMove ±0.5%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.87×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（2D）±2.8% ｜ 08-31（5D）±3.4% ｜ 09-02（7D）±4.4% ｜ 09-04（9D）±5.2%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Candidates 395.10 / 399.96 / 418.93 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 Top-3 近似 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: 待审计
结构观察区: 395–400（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 300: +15.9% | 距 Call Wall 400: -13.1%
最近结构参考: Flip 395（距现价 -12.0%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 300（Put Wall）；上方 400（Call Wall）。
• Gamma 区域：切换参考 395（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-26 365.0C — Vol 8,266 | 最新价 $0.01 | OI 2766→8000 (ΔOI +5234张) | ΔOI/Volume 63.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5234张（+189.2% vs前日OI），连续性待观察（方向未知）
08-26 355.0C — Vol 66,213 | 最新价 $0.01 | OI 3152→8321 (ΔOI +5169张) | ΔOI/Volume 7.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5169张（+164.0% vs前日OI），连续性待观察（方向未知）
08-26 360.0C — Vol 38,998 | 最新价 $0.01 | OI 7326→11798 (ΔOI +4472张) | ΔOI/Volume 11.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4472张（+61.0% vs前日OI），连续性待观察（方向未知）
08-26 350.0P — Vol 26,666 | 最新价 $4.32 | OI 2712→7109 (ΔOI +4397张) | ΔOI/Volume 16.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4397张（+162.1% vs前日OI），连续性待观察（方向未知）
08-26 352.5C — Vol 95,938 | 最新价 $0.01 | OI 1821→5811 (ΔOI +3990张) | ΔOI/Volume 4.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3990张（+219.1% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +15.6k / P +12.0k ｜ Activity HIGH ｜ 2D
08-31  C +4.8k / P +2.3k ｜ Activity HIGH ｜ 5D
09-02  C +3.5k / P +2.3k ｜ Activity HIGH ｜ 7D
09-04  C +4.4k / P +4.5k ｜ Activity HIGH ｜ 9D

📆 08-28 Forward Structure
OI:       C 224.6k / P 187.6k
ΔOI:      C +15.6k / P +12.0k
ATM:      C 4.08 / P 5.64
ATM IV:   46.4%
ΔOI Δ Exposure*: -208k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 387 ｜ +2,678 ｜ $0.08 ｜ 名义 $21.4k* ｜ +11.4%
P 160 ｜ +2,111 ｜ $0.01 ｜ 名义 $2.1k* ｜ -54.0%
P 352 ｜ +2,019 ｜ $8.98 ｜ 名义 $1.81M* ｜ +1.4%
结构参考：387（+11.4%）上方 / 160（-54.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-31 Forward Structure
OI:       C 42.3k / P 14.0k
ΔOI:      C +4.8k / P +2.3k
ATM:      C 5.20 / P 6.66
ATM IV:   37.0%
ΔOI Δ Exposure*: -48k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 395 ｜ +704 ｜ $0.13 ｜ 名义 $9.2k* ｜ +13.6%
C 450 ｜ +609 ｜ $0.03 ｜ 名义 $1.8k* ｜ +29.4%
P 350 ｜ +443 ｜ $8.31 ｜ 名义 $368.1k* ｜ +0.6%
结构参考：395（+13.6%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 14.8k / P 8.4k
ΔOI:      C +3.5k / P +2.3k
ATM:      C 6.90 / P 8.40
ATM IV:   39.7%
ΔOI Δ Exposure*: 3k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 400 ｜ +949 ｜ $0.23 ｜ 名义 $21.8k* ｜ +15.0%
C 375 ｜ +419 ｜ $0.94 ｜ 名义 $39.4k* ｜ +7.8%
C 360 ｜ +385 ｜ $2.85 ｜ 名义 $109.7k* ｜ +3.5%
结构参考：400（+15.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 66.9k / P 56.0k
ΔOI:      C +4.4k / P +4.5k
ATM:      C 8.35 / P 9.79
ATM IV:   41.8%
ΔOI Δ Exposure*: -17k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 315 ｜ +875 ｜ $0.95 ｜ 名义 $83.1k* ｜ -9.4%
P 270 ｜ +800 ｜ $0.09 ｜ 名义 $7.2k* ｜ -22.4%
C 550 ｜ +674 ｜ $0.03 ｜ 名义 $2.0k* ｜ +58.1%
结构参考：550（+58.1%）上方 / 315（-9.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（2D）ATM IV 46.4% vs 08-31 37.0%（差 +9.4pp）——覆盖 Personal Spending MoM、Personal Income MoM、GDP 增速 Rate QoQ 2nd Est、耐用品订单 Orders MoM、PCE 物价 Price Index MoM、美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-26/TSLA_evening.json