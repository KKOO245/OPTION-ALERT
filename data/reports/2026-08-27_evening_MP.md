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
🟡 **事件差分**: 08-28 ATM IV 79.1% vs 09-04 67.4%（差 +11.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-11 60C ΔOI +131（距现价 +2.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## MP

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
MP: 今晨 58.36 → 收盘 58.60（+0.4%） ｜ 今日高 59.49 ｜ 低 57.27
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.35 | OI比 0.52 | ATM IV 79.1% | Skew -4.8pp | Term 0.83 | ExpMove ±3.4%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.52×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±3.1% ｜ 09-04（8D）±8.2% ｜ 09-11（15D）±11.6% ｜ 09-18（22D）±13.5%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 55.63（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 331 / LOW 67 / INVALID 108
结构观察区: ≈56（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 55: +6.5% | 距 Call Wall 60: -2.3%
最近结构参考: Call Wall 60（距现价 -2.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 55（Put Wall）；上方 60（Call Wall）。
• Gamma 区域：切换参考 56（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
10-02 50.0P — Vol 21 | 最新价 $1.33 | OI 72→1079 (ΔOI +1007张) | ΔOI/Volume 4795.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1007张（+1398.6% vs前日OI），连续性待观察（方向未知）
08-28 65.0C — Vol 348 | 最新价 $0.03 | OI 1653→1971 (ΔOI +318张) | ΔOI/Volume 91.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增318张（+19.2% vs前日OI），连续性待观察（方向未知）
09-18 65.0C — Vol 187 | 最新价 $1.93 | OI 5230→5433 (ΔOI +203张) | ΔOI/Volume 108.6% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增203张（+3.9% vs前日OI），值得跟踪（方向未知）
09-18 64.0P — Vol 0 | 最新价 $7.15 | OI 0→144 (ΔOI +144张) | ΔOI/Volume N/A | Magnitude: LOW | 完整度: HIGH
   ⇒ 净增144张（量数据缺失），以日内换手为主
08-28 63.0C — Vol 264 | 最新价 $0.09 | OI 1034→1174 (ΔOI +140张) | ΔOI/Volume 53.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增140张（+13.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +0.3k / P +0.3k ｜ Activity MEDIUM △ ｜ 1D
09-04  C +0.6k / P +0.2k ｜ Activity HIGH ｜ 8D
09-11  C +0.2k / P +69 ｜ Activity HIGH ｜ 15D
09-18  C -72 / P +0.2k ｜ Activity MEDIUM △ ｜ 22D

   Top ΔOI: 65C +318 ｜ 63C +140

📆 09-04 Forward Structure
OI:       C 7.1k / P 5.3k
ΔOI:      C +0.6k / P +0.2k
ATM:      C 2.50 / P 2.28
ATM IV:   67.4%
ΔOI Δ Exposure*: 693 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 68 ｜ +120 ｜ $0.35 ｜ 名义 $4.2k* ｜ +16.0%
C 76 ｜ +111 ｜ $0.15 ｜ 名义 $1.7k* ｜ +29.7%
C 70 ｜ +72 ｜ $0.21 ｜ 名义 $1.5k* ｜ +19.5%
结构参考：68（+16.0%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 2.7k / P 3.0k
ΔOI:      C +0.2k / P +69
ATM:      C 3.35 / P 3.47
ATM IV:   68.5%
ΔOI Δ Exposure*: 6k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 60 ｜ +131 ｜ $2.82 ｜ 名义 $36.9k* ｜ +2.4%
P 60 ｜ +25 ｜ $3.75 ｜ 名义 $9.4k* ｜ +2.4%
C 64 ｜ +25 ｜ $1.54 ｜ 名义 $3.9k* ｜ +9.2%
结构参考：60（+2.4%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 70C -399 ｜ 65C +203

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 79.1% vs 09-04 67.4%（差 +11.7pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/MP_evening.json