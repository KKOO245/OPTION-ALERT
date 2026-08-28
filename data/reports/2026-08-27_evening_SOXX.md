# 期权晚报 2026-08-27

📊 市场环境

SPY $771.10 ｜ QQQ $721.11
VIX 14.51 ↓4.6%（5D -9.4%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.2（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911

🔍 重点速览
🟡 **近现价集中开仓**: 08-28 515P ΔOI +968（距现价 -1.1%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SOXX

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
SOXX: 今晨 523.14 → 收盘 520.65（-0.5%） ｜ 今日高 527.78 ｜ 低 517.00
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.49 | OI比 0.85 | ATM IV 44.3% | Skew 2.8pp | Term 0.87 | ExpMove ±1.9%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.85×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量接近均衡
   ExpMove 期限化（expmove_v1）: 08-28（1D）±2.0% ｜ 09-04（8D）±4.4% ｜ 09-11（15D）±5.9% ｜ 09-18（22D）±7.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 523.46（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 92%（带内） ｜ IV 有效性: VALID 607 / LOW 309 / INVALID 684
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: ≈523（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 500: +4.1% | 距 Call Wall 575: -9.5%
最近结构参考: Flip 523（距现价 -0.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 500（Put Wall）；上方 575（Call Wall）。
• Gamma 区域：切换参考 523（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-25 580.0C — Vol 5 | 最新价 $5.31 | OI 41→1878 (ΔOI +1837张) | ΔOI/Volume 36740.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1837张（+4480.5% vs前日OI），连续性待观察（方向未知）
08-28 475.0P — Vol 5 | 最新价 $0.07 | OI 782→1786 (ΔOI +1004张) | ΔOI/Volume 20080.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1004张（+128.4% vs前日OI），连续性待观察（方向未知）
08-28 515.0P — Vol 142 | 最新价 $2.50 | OI 565→1533 (ΔOI +968张) | ΔOI/Volume 681.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增968张（+171.3% vs前日OI），连续性待观察（方向未知）
08-28 527.5C — Vol 750 | 最新价 $2.33 | OI 14→768 (ΔOI +754张) | ΔOI/Volume 100.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增754张（+5385.7% vs前日OI），连续性待观察（方向未知）
09-04 510.0P — Vol 362 | 最新价 $6.41 | OI 322→647 (ΔOI +325张) | ΔOI/Volume 89.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增325张（+100.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +1.0k / P +1.9k ｜ Activity HIGH ｜ 1D
09-04  C -28 / P +0.8k ｜ Activity HIGH ｜ 8D
09-11  C -53 / P -19 ｜ Activity MEDIUM △ ｜ 15D
09-18  C -1.4k / P -1.0k ｜ Activity HIGH ｜ 22D

📆 08-28 Forward Structure
OI:       C 36.6k / P 31.2k
ΔOI:      C +1.0k / P +1.9k
ATM:      C 5.70 / P 4.89
ATM IV:   44.3%
ΔOI Δ Exposure*: 1k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 475 ｜ +1,004 ｜ $0.07 ｜ 名义 $7.0k* ｜ -8.8%
P 515 ｜ +968 ｜ $2.50 ｜ 名义 $242.0k* ｜ -1.1%
C 527 ｜ +754 ｜ $2.33 ｜ 名义 $175.7k* ｜ +1.3%
结构参考：527（+1.3%）上方 / 475（-8.8%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 24.7k / P 17.6k
ΔOI:      C -28 / P +0.8k
ATM:      C 12.50 / P 10.64
ATM IV:   37.6%
ΔOI Δ Exposure*: -16k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 510 ｜ +325 ｜ $6.41 ｜ 名义 $208.3k* ｜ -2.0%
P 500 ｜ +100 ｜ $4.21 ｜ 名义 $42.1k* ｜ -4.0%
P 465 ｜ +99 ｜ $0.60 ｜ 名义 $5.9k* ｜ -10.7%
结构参考：510（-2.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 537C -14 ｜ 542C -14

📆 09-18 Forward Structure
OI:       C 77.6k / P 75.9k
ΔOI:      C -1.4k / P -1.0k
ATM:      C 19.90 / P 18.26
ATM IV:   38.2%
ΔOI Δ Exposure*: -10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 590 ｜ -1,218 ｜ $2.07 ｜ 名义 $-252.1k* ｜ +13.3%
P 480 ｜ -781 ｜ $5.65 ｜ 名义 $-441.3k* ｜ -7.8%
C 510 ｜ -302 ｜ $27.80 ｜ 名义 $-839.6k* ｜ -2.0%
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 44.3% vs 09-04 37.6%（差 +6.6pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/SOXX_evening.json