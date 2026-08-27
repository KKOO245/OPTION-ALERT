# 期权晨报 2026-08-27

📊 市场环境

SPY $770.63 ｜ QQQ $719.25
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.3（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911


## USAR

🔍 重点速览
🟡 **事件差分**: 08-28 ATM IV 105.3% vs 09-04 90.6%（差 +14.7pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 09-04 19C ΔOI +4,767（距现价 +3.5%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-04 19C ΔOI +4,767 占该期限总 OI 17.3%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
USAR  昨收 18.95 → 今晨 18.84（-0.6%） | 较昨收变动（含盘初走势） ｜ 今日高 19.24 ｜ 低 18.46

Options: P/C量 0.26 | OI比 0.50 | ATM IV 105.3% | Skew -4.1pp | Term 0.84 | ExpMove ±4.9%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.26×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±4.9% ｜ 09-04（8D）±10.7% ｜ 09-11（15D）±14.6% ｜ 09-18（22D）±18.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 16.80（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 312 / LOW 88 / INVALID 128
结构观察区: ≈17（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 15: +25.6% | 距 Call Wall 20: -5.8%
最近结构参考: Call Wall 20（距现价 -5.8%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 15（Put Wall）；上方 20（Call Wall）。
• Gamma 区域：切换参考 17（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 19.5C — Vol 70 | 最新价 $0.86 | OI 890→5657 (ΔOI +4767张) | ΔOI/Volume 6810.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增4767张（+535.6% vs前日OI），连续性待观察（方向未知）
08-28 20.0C — Vol 338 | 最新价 $0.17 | OI 3706→4346 (ΔOI +640张) | ΔOI/Volume 189.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增640张（+17.3% vs前日OI），连续性待观察（方向未知）
08-28 21.0C — Vol 169 | 最新价 $0.04 | OI 1715→2338 (ΔOI +623张) | ΔOI/Volume 368.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增623张（+36.3% vs前日OI），连续性待观察（方向未知）
09-04 21.5C — Vol 8 | 最新价 $0.31 | OI 272→857 (ΔOI +585张) | ΔOI/Volume 7312.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增585张（+215.1% vs前日OI），连续性待观察（方向未知）
08-28 20.5C — Vol 135 | 最新价 $0.09 | OI 1552→2132 (ΔOI +580张) | ΔOI/Volume 429.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增580张（+37.4% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +2.6k / P +0.2k ｜ Activity HIGH ｜ 1D
09-04  C +7.3k / P +1.2k ｜ Activity HIGH ｜ 8D
09-11  C +1.0k / P +72 ｜ Activity HIGH ｜ 15D
09-18  C +0.3k / P +0.1k ｜ Activity MEDIUM △ ｜ 22D

📆 08-28 Forward Structure
OI:       C 22.6k / P 11.4k
ΔOI:      C +2.6k / P +0.2k
ATM:      C 0.53 / P 0.39
ATM IV:   105.3%
ΔOI Δ Exposure*: -50 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 20 ｜ +640 ｜ $0.17 ｜ 名义 $10.9k* ｜ +6.2%
C 21 ｜ +623 ｜ $0.04 ｜ 名义 $2.5k* ｜ +11.5%
C 20 ｜ +580 ｜ $0.09 ｜ 名义 $5.2k* ｜ +8.8%
结构参考：20（+6.2%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 23.8k / P 3.8k
ΔOI:      C +7.3k / P +1.2k
ATM:      C 1.03 / P 0.98
ATM IV:   90.6%
ΔOI Δ Exposure*: 242k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 19 ｜ +4,767 ｜ $0.86 ｜ 名义 $410.0k* ｜ +3.5%
C 21 ｜ +585 ｜ $0.31 ｜ 名义 $18.1k* ｜ +14.1%
C 20 ｜ +442 ｜ $0.53 ｜ 名义 $23.4k* ｜ +8.8%
结构参考：19（+3.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 9.3k / P 1.8k
ΔOI:      C +1.0k / P +72
ATM:      C 1.33 / P 1.42
ATM IV:   85.2%
ΔOI Δ Exposure*: 23k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 22 ｜ +416 ｜ $0.46 ｜ 名义 $19.1k* ｜ +16.8%
C 23 ｜ +358 ｜ $0.29 ｜ 名义 $10.4k* ｜ +22.1%
C 19 ｜ +186 ｜ $1.15 ｜ 名义 $21.4k* ｜ +3.5%
结构参考：22（+16.8%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

   Top ΔOI: 20C +160 ｜ 23C +138

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 105.3% vs 09-04 90.6%（差 +14.7pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/USAR_morning.json