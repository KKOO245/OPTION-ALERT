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
🟡 **近现价集中开仓**: 09-04 1465P ΔOI +865（距现价 +0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SNDK

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
SNDK: 今晨 1,471.95 → 收盘 1,464.42（-0.5%） ｜ 今日高 1557.89 ｜ 低 1456.00
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.52 | OI比 0.70 | ATM IV 80.3% | Skew -1.7pp | Term 0.89 | ExpMove ±3.6%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.52×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.70×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±3.6% ｜ 09-04（8D）±8.9% ｜ 09-11（15D）±11.4% ｜ 09-18（22D）±13.5%
   ⇒ IV–VIX Spread: +65.8pp*（*近月 ATM IV − VIX；期限未对齐，仅作相对波动率 Proxy，不直接代表期权定价贵/便宜）
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: NEGATIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 1483.47（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 2213 / LOW 643 / INVALID 894
   ⇒ Gamma Regime 判定为 NEGATIVE；GEX 数值不可用，不对 Gamma 强度做判断。
结构观察区: ≈1483（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 800: +83.1% | 距 Call Wall 1,700: -13.9%
最近结构参考: Flip 1483（距现价 -1.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 800（Put Wall）；上方 1,700（Call Wall）。
• Gamma 区域：切换参考 1483（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 1700.0C — Vol 8,847 | 最新价 $0.32 | OI 6535→8127 (ΔOI +1592张) | ΔOI/Volume 18.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1592张（+24.4% vs前日OI），连续性待观察（方向未知）
09-04 1280.0P — Vol 35 | 最新价 $7.35 | OI 75→944 (ΔOI +869张) | ΔOI/Volume 2482.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增869张（+1158.7% vs前日OI），连续性待观察（方向未知）
09-04 1465.0P — Vol 41 | 最新价 $57.40 | OI 27→892 (ΔOI +865张) | ΔOI/Volume 2109.8% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增865张（+3203.7% vs前日OI），连续性待观察（方向未知）
09-04 1720.0C — Vol 73 | 最新价 $8.32 | OI 80→926 (ΔOI +846张) | ΔOI/Volume 1158.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增846张（+1057.5% vs前日OI），连续性待观察（方向未知）
08-28 1650.0C — Vol 3,453 | 最新价 $0.60 | OI 1449→2042 (ΔOI +593张) | ΔOI/Volume 17.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增593张（+40.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +7.6k / P +1.4k ｜ Activity HIGH ｜ 1D
09-04  C +2.9k / P +2.3k ｜ Activity HIGH ｜ 8D
09-11  C +0.2k / P +0.1k ｜ Activity MEDIUM △ ｜ 15D
09-18  C +0.6k / P +0.1k ｜ Activity MEDIUM △ ｜ 22D

📆 08-28 Forward Structure
OI:       C 72.9k / P 51.3k
ΔOI:      C +7.6k / P +1.4k
ATM:      C 37.40 / P 16.00
ATM IV:   80.3%
ΔOI Δ Exposure*: 64k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 1700 ｜ +1,592 ｜ $0.32 ｜ 名义 $50.9k* ｜ +16.1%
C 1650 ｜ +593 ｜ $0.60 ｜ 名义 $35.6k* ｜ +12.7%
C 1600 ｜ +571 ｜ $1.65 ｜ 名义 $94.2k* ｜ +9.3%
结构参考：1700（+16.1%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 20.0k / P 19.0k
ΔOI:      C +2.9k / P +2.3k
ATM:      C 73.71 / P 57.40
ATM IV:   71.4%
ΔOI Δ Exposure*: 10k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 1280 ｜ +869 ｜ $7.35 ｜ 名义 $638.7k* ｜ -12.6%
P 1465 ｜ +865 ｜ $57.40 ｜ 名义 $4.97M* ｜ +0.0%
C 1720 ｜ +846 ｜ $8.32 ｜ 名义 $703.9k* ｜ +17.5%
结构参考：1720（+17.5%）上方 / 1280（-12.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 1440C +56 ｜ 1460C +45

   Top ΔOI: 2000C -288 ｜ 1600P -268

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 80.3% vs 09-04 71.4%（差 +8.9pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup A v1 — Core Conditions
Price Regime DOWN | Location below_flip | Gamma Regime NEGATIVE（模型层）
Confirmation: ✓ 0 ｜ ✗ 3 ｜ ? 1（? put_buy_confirmation）
验证状态: N=2 ｜ OOS Lift N/A ｜ CI 下界 N/A
Target: 3D_close_return <= -0.02 — PENDING（evaluation date 待窗口结束）
Status: 实验中，样本不足（N=2）
环境: Vol LOW（仅环境标签，不参与计票）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/SNDK_evening.json