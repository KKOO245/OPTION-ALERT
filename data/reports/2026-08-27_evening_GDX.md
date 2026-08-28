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
🔴 **事件差分**: 08-28（1D）ATM IV 61.6% vs 09-04 46.2%（差 +15.4pp），覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   ⇒ 覆盖【高】事件的期限隐含波动显著更高（美联储 IFDP 1376 实证；单日截面，需连续多日确认；观察，非预测）
🟡 **近现价集中开仓**: 08-28 108C ΔOI +5,287（距现价 +4.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## GDX

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
GDX: 今晨 103.42 → 收盘 103.69（+0.3%） ｜ 今日高 104.11 ｜ 低 101.69
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.73 | OI比 0.66 | ATM IV 61.6% | Skew -2.0pp | Term 0.74 | ExpMove ±2.6%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.73×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.66×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±2.4% ｜ 09-04（8D）±5.5% ｜ 09-11（15D）±7.3% ｜ 09-18（22D）±9.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 99.70（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 94%（带内） ｜ IV 有效性: VALID 568 / LOW 211 / INVALID 263
结构观察区: ≈100（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 80: +29.6% | 距 Call Wall 104: -0.3%
最近结构参考: Call Wall 104（距现价 -0.3%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 80（Put Wall）；上方 104（Call Wall）。
• Gamma 区域：切换参考 100（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 108.0C — Vol 14,955 | 最新价 $0.17 | OI 12904→18191 (ΔOI +5287张) | ΔOI/Volume 35.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增5287张（+41.0% vs前日OI），连续性待观察（方向未知）
09-18 99.0P — Vol 530 | 最新价 $2.41 | OI 1682→6051 (ΔOI +4369张) | ΔOI/Volume 824.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4369张（+259.8% vs前日OI），连续性待观察（方向未知）
09-04 100.0P — Vol 1,487 | 最新价 $1.25 | OI 2879→6745 (ΔOI +3866张) | ΔOI/Volume 260.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增3866张（+134.3% vs前日OI），连续性待观察（方向未知）
09-18 85.0P — Vol 2,604 | 最新价 $0.22 | OI 29096→31509 (ΔOI +2413张) | ΔOI/Volume 92.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2413张（+8.3% vs前日OI），连续性待观察（方向未知）
09-18 89.0P — Vol 2,020 | 最新价 $0.44 | OI 3304→5635 (ΔOI +2331张) | ΔOI/Volume 115.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2331张（+70.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +5.5k / P +3.1k ｜ Activity MEDIUM △ ｜ 1D
09-04  C +1.8k / P +6.5k ｜ Activity HIGH ｜ 8D
09-11  C +73 / P -9 ｜ Activity MEDIUM △ ｜ 15D
09-18  C -6.8k / P +5.4k ｜ Activity HIGH ｜ 22D

   Top ΔOI: 108C +5,287 ｜ 104C -3,393

📆 09-04 Forward Structure
OI:       C 14.6k / P 58.2k
ΔOI:      C +1.8k / P +6.5k
ATM:      C 2.76 / P 2.95
ATM IV:   46.2%
ΔOI Δ Exposure*: -163k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 100 ｜ +3,866 ｜ $1.25 ｜ 名义 $483.2k* ｜ -3.6%
P 95 ｜ +1,356 ｜ $0.33 ｜ 名义 $44.7k* ｜ -8.4%
C 116 ｜ +1,013 ｜ $0.31 ｜ 名义 $31.4k* ｜ +11.9%
结构参考：116（+11.9%）上方 / 100（-3.6%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 97P +162 ｜ 90P -145

📆 09-18 Forward Structure
OI:       C 248.0k / P 376.1k
ΔOI:      C -6.8k / P +5.4k
ATM:      C 4.67 / P 4.65
ATM IV:   45.4%
ΔOI Δ Exposure*: -709k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 95 ｜ -4,385 ｜ $10.10 ｜ 名义 $-4.43M* ｜ -8.4%
P 99 ｜ +4,369 ｜ $2.41 ｜ 名义 $1.05M* ｜ -4.5%
P 85 ｜ +2,413 ｜ $0.22 ｜ 名义 $53.1k* ｜ -18.0%
结构参考：99（-4.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 61.6% vs 09-04 46.2%（差 +15.4pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/GDX_evening.json