# 期权晨报 2026-08-26

📊 市场环境

SPY $769.98 ｜ QQQ $711.37
VIX 15.62 ↑1.1%（5D +4.9%） ｜ Vol Regime: NORMAL
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


## QQQ

🔍 重点速览
🔴 **Gamma Regime 切换**: POSITIVE → NEGATIVE（模型分类）
   ⇒ Gamma 状态翻转是波动环境变化信号；仍为模型层，方向不可观测（Scenario A/B）
🟡 **近现价集中开仓**: 08-27 711C ΔOI +2,605（距现价 +0.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **Flip 状态**: CONDITIONAL（Candidates: 723.9）｜ Primary: N/A
   ⇒ Top-3 近似 + 有效覆盖待盘点，Gamma 层不作方向/强度解读

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
QQQ  昨收 711.00 → 今晨 709.28（-0.2%） | 较昨收变动（含盘初走势） ｜ 今日高 712.20 ｜ 低 707.97

Options: P/C量 1.06 | OI比 1.23 | ATM IV 28.6% | Skew 3.4pp | Term 0.67 | ExpMove ±0.5%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.06×（Put 与 Call 成交量接近）→ 方向 Unknown
   ⇒ Put/Call OI: 1.23×（存量 Put 仓位高于 Call）→ 存量 Put-dominant
   ⇒ 当日成交 vs 存量仓位：当日成交接近均衡，存量Put-dominant
   ExpMove 期限化（expmove_v1）: 08-27（1D）±1.1% ｜ 08-28（2D）±1.4% ｜ 08-31（5D）±1.7% ｜ 09-01（6D）±1.9%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Candidates 723.91 ｜ Primary: N/A（CONDITIONAL）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 Top-3 近似 ｜ Effective GEX 覆盖: 待盘点 ｜ IV 有效性: 待审计
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: ≈724（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 700: +1.3% | 距 Call Wall 750: -5.4%
最近结构参考: Put Wall 700（距现价 +1.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 700（Put Wall）；上方 750（Call Wall）。
• Gamma 区域：切换参考 724（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 505.0P — Vol N/A | OI 162→18399 (ΔOI +18237张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增18237张（+11257.4% vs前日OI），连续性待观察（方向未知）
08-28 510.0P — Vol N/A | OI 547→11945 (ΔOI +11398张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增11398张（+2083.7% vs前日OI），连续性待观察（方向未知）
08-26 713.0C — Vol N/A | OI 1393→8579 (ΔOI +7186张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增7186张（+515.9% vs前日OI），连续性待观察（方向未知）
08-26 716.0C — Vol N/A | OI 3142→10021 (ΔOI +6879张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增6879张（+218.9% vs前日OI），连续性待观察（方向未知）
08-28 470.0P — Vol N/A | OI 11237→17597 (ΔOI +6360张) | ΔOI/Volume N/A | Magnitude: HIGH | 完整度: LOW
   ⇒ 大额净增6360张（+56.6% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-27  C +15.7k / P +18.3k ｜ Activity HIGH ｜ 1D
08-28  C +14.7k / P +47.3k ｜ Activity HIGH ｜ 2D
08-31  C +7.1k / P +7.2k ｜ Activity HIGH ｜ 5D
09-01  C +3.7k / P +15.8k ｜ Activity HIGH ｜ 6D

📆 08-27 Forward Structure
OI:       C 53.6k / P 81.7k
ΔOI:      C +15.7k / P +18.3k
ATM:      C 3.95 / P 3.59
ATM IV:   23.5%
ΔOI Δ Exposure*: -17k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 711 ｜ +2,605 ｜ $2.92 ｜ 名义 $760.7k* ｜ +0.2%
C 712 ｜ +2,115 ｜ $2.53 ｜ 名义 $535.1k* ｜ +0.4%
P 714 ｜ +1,875 ｜ $6.45 ｜ 名义 $1.21M* ｜ +0.7%
结构参考：711（+0.2%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-28 Forward Structure
OI:       C 321.7k / P 292.4k
ΔOI:      C +14.7k / P +47.3k
ATM:      C 5.14 / P 4.58
ATM IV:   22.2%
ΔOI Δ Exposure*: 486k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 505 ｜ +18,237 ｜ $0.01 ｜ 名义 $18.2k* ｜ -28.8%
P 510 ｜ +11,398 ｜ $0.01 ｜ 名义 $11.4k* ｜ -28.1%
P 470 ｜ +6,360 ｜ $0.01 ｜ 名义 $6.4k* ｜ -33.7%
结构参考：505（-28.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-31 Forward Structure
OI:       C 365.3k / P 243.7k
ΔOI:      C +7.1k / P +7.2k
ATM:      C 6.21 / P 5.74
ATM IV:   17.8%
ΔOI Δ Exposure*: 144k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 650 ｜ +4,511 ｜ $0.06 ｜ 名义 $27.1k* ｜ -8.4%
C 720 ｜ +4,027 ｜ $1.90 ｜ 名义 $765.1k* ｜ +1.5%
P 652 ｜ +1,715 ｜ $0.07 ｜ 名义 $12.0k* ｜ -8.1%
结构参考：720（+1.5%）上方 / 650（-8.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-01 Forward Structure
OI:       C 25.0k / P 36.1k
ΔOI:      C +3.7k / P +15.8k
ATM:      C 7.06 / P 6.34
ATM IV:   18.2%
ΔOI Δ Exposure*: -92k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 650 ｜ +5,993 ｜ $0.13 ｜ 名义 $77.9k* ｜ -8.4%
P 645 ｜ +1,131 ｜ $0.11 ｜ 名义 $12.4k* ｜ -9.1%
P 655 ｜ +1,041 ｜ $0.15 ｜ 名义 $15.6k* ｜ -7.7%
结构参考：650（-8.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-26/QQQ_morning.json