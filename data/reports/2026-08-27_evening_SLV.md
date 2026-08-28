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
🟡 **事件差分**: 08-28 ATM IV 49.6% vs 08-31 36.3%（差 +13.4pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 08-28 60P ΔOI +1,313（距现价 -4.4%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## SLV

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
SLV: 今晨 62.10 → 收盘 62.77（+1.1%） ｜ 今日高 62.97 ｜ 低 61.08
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.56 | OI比 0.58 | ATM IV 49.6% | Skew -5.0pp | Term 0.90 | ExpMove ±2.1%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.56×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.58×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±2.1% ｜ 08-31（4D）±3.0% ｜ 09-02（6D）±4.1% ｜ 09-04（8D）±5.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 54.97（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 1141 / LOW 275 / INVALID 464
结构观察区: ≈55（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 50: +25.5% | 距 Call Wall 70: -10.3%
最近结构参考: Call Wall 70（距现价 -10.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 50（Put Wall）；上方 70（Call Wall）。
• Gamma 区域：切换参考 55（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 62.0C — Vol 5,031 | 最新价 $1.99 | OI 2563→4701 (ΔOI +2138张) | ΔOI/Volume 42.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2138张（+83.4% vs前日OI），连续性待观察（方向未知）
09-18 63.0C — Vol 2,826 | 最新价 $2.65 | OI 64445→65758 (ΔOI +1313张) | ΔOI/Volume 46.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1313张（+2.0% vs前日OI），连续性待观察（方向未知）
08-28 60.0P — Vol 5,023 | 最新价 $0.04 | OI 3120→4433 (ΔOI +1313张) | ΔOI/Volume 26.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1313张（+42.1% vs前日OI），连续性待观察（方向未知）
08-28 58.0P — Vol 548 | 最新价 $0.01 | OI 1892→3071 (ΔOI +1179张) | ΔOI/Volume 215.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1179张（+62.3% vs前日OI），连续性待观察（方向未知）
08-28 62.5C — Vol 5,841 | 最新价 $0.80 | OI 777→1899 (ΔOI +1122张) | ΔOI/Volume 19.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1122张（+144.4% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +2.5k / P +5.1k ｜ Activity HIGH ｜ 1D
08-31  C +0.6k / P +0.9k ｜ Activity HIGH ｜ 4D
09-02  C +1.0k / P +1.1k ｜ Activity HIGH ｜ 6D
09-04  C +5.2k / P +2.5k ｜ Activity HIGH ｜ 8D

📆 08-28 Forward Structure
OI:       C 122.2k / P 70.5k
ΔOI:      C +2.5k / P +5.1k
ATM:      C 0.55 / P 0.78
ATM IV:   49.6%
ΔOI Δ Exposure*: 45k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 60 ｜ +1,313 ｜ $0.04 ｜ 名义 $5.3k* ｜ -4.4%
P 58 ｜ +1,179 ｜ $0.01 ｜ 名义 $1.2k* ｜ -7.6%
P 57 ｜ -1,137 ｜ $0.01 ｜ 名义 $-1.1k* ｜ -8.4%
结构参考：60（-4.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-31 Forward Structure
OI:       C 51.1k / P 8.6k
ΔOI:      C +0.6k / P +0.9k
ATM:      C 0.85 / P 1.02
ATM IV:   36.3%
ΔOI Δ Exposure*: 12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 61 ｜ +583 ｜ $0.45 ｜ 名义 $26.2k* ｜ -2.0%
C 62 ｜ +364 ｜ $1.39 ｜ 名义 $50.6k* ｜ -1.2%
C 65 ｜ -249 ｜ $0.31 ｜ 名义 $-7.7k* ｜ +3.6%
结构参考：61（-2.0%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 10.3k / P 4.1k
ΔOI:      C +1.0k / P +1.1k
ATM:      C 1.17 / P 1.43
ATM IV:   40.6%
ΔOI Δ Exposure*: 26k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 62 ｜ +343 ｜ $1.44 ｜ 名义 $49.4k* ｜ -0.4%
P 61 ｜ +275 ｜ $0.72 ｜ 名义 $19.8k* ｜ -2.0%
P 56 ｜ +215 ｜ $0.06 ｜ 名义 $1.3k* ｜ -10.8%
结构参考：62（-0.4%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 59.3k / P 30.3k
ΔOI:      C +5.2k / P +2.5k
ATM:      C 1.54 / P 1.78
ATM IV:   43.5%
ΔOI Δ Exposure*: 143k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 62 ｜ +2,138 ｜ $1.99 ｜ 名义 $425.5k* ｜ -1.2%
C 62 ｜ +1,093 ｜ $1.79 ｜ 名义 $195.6k* ｜ -0.4%
C 72 ｜ +1,090 ｜ $0.13 ｜ 名义 $14.2k* ｜ +14.7%
结构参考：72（+14.7%）上方 / 62（-1.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 49.6% vs 08-31 36.3%（差 +13.4pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/SLV_evening.json