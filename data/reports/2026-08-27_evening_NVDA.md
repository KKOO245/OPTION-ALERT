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
🟡 **事件差分**: 08-28 ATM IV 43.6% vs 08-31 32.1%（差 +11.5pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 08-28 220C ΔOI +35,710（距现价 -2.7%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-02 225C ΔOI +8,671 占该期限总 OI 12.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## NVDA

📋 Thesis Scorecard（今晨条件 vs 收盘实况，只打事实勾）
NVDA: 今晨 226.51 → 收盘 226.14（-0.2%） ｜ 今日高 230.47 ｜ 低 220.90
Target 状态: PENDING（evaluation date …）——窗口结束前禁止'预测正确'类措辞

Options: P/C量 0.53 | OI比 0.50 | ATM IV 43.6% | Skew 0.8pp | Term 0.77 | ExpMove ±2.1%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.53×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±2.1% ｜ 08-31（4D）±2.9% ｜ 09-02（6D）±3.8% ｜ 09-04（8D）±4.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 208.30（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 97%（带内） ｜ IV 有效性: VALID 707 / LOW 232 / INVALID 359
结构观察区: ≈208（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 190: +19.0% | 距 Call Wall 230: -1.7%
最近结构参考: Call Wall 230（距现价 -1.7%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall）；上方 230（Call Wall）。
• Gamma 区域：切换参考 208（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 220.0C — Vol 126,703 | 最新价 $8.25 | OI 60397→96107 (ΔOI +35710张) | ΔOI/Volume 28.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35710张（+59.1% vs前日OI），连续性待观察（方向未知）
08-28 200.0P — Vol 63,437 | 最新价 $0.03 | OI 36789→58748 (ΔOI +21959张) | ΔOI/Volume 34.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21959张（+59.7% vs前日OI），连续性待观察（方向未知）
08-28 230.0C — Vol 684,401 | 最新价 $1.15 | OI 194582→210864 (ΔOI +16282张) | ΔOI/Volume 2.4% | Magnitude: MEDIUM | 完整度: HIGH
   ⇒ 放量且净增16282张（+8.4% vs前日OI），值得跟踪（方向未知）
08-28 235.0C — Vol 209,455 | 最新价 $0.25 | OI 41317→57195 (ΔOI +15878张) | ΔOI/Volume 7.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15878张（+38.4% vs前日OI），连续性待观察（方向未知）
09-04 115.0P — Vol 339 | 最新价 $0.01 | OI 16267→31530 (ΔOI +15263张) | ΔOI/Volume 4502.4% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15263张（+93.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +183.1k / P +149.3k ｜ Activity HIGH ｜ 1D
08-31  C +34.4k / P +24.1k ｜ Activity HIGH ｜ 4D
09-02  C +20.3k / P +12.1k ｜ Activity HIGH ｜ 6D
09-04  C +41.0k / P +57.9k ｜ Activity HIGH ｜ 8D

📆 08-28 Forward Structure
OI:       C 1169.3k / P 581.8k
ΔOI:      C +183.1k / P +149.3k
ATM:      C 3.80 / P 1.00
ATM IV:   43.6%
ΔOI Δ Exposure*: 9.0M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 220 ｜ +35,710 ｜ $8.25 ｜ 名义 $29.46M* ｜ -2.7%
P 200 ｜ +21,959 ｜ $0.03 ｜ 名义 $65.9k* ｜ -11.6%
C 230 ｜ +16,282 ｜ $1.15 ｜ 名义 $1.87M* ｜ +1.7%
结构参考：230（+1.7%）上方 / 220（-2.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-31 Forward Structure
OI:       C 117.1k / P 62.8k
ΔOI:      C +34.4k / P +24.1k
ATM:      C 4.70 / P 1.79
ATM IV:   32.1%
ΔOI Δ Exposure*: 1.8M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 230 ｜ +8,750 ｜ $2.04 ｜ 名义 $1.78M* ｜ +1.7%
P 210 ｜ +5,816 ｜ $0.15 ｜ 名义 $87.2k* ｜ -7.1%
P 205 ｜ +4,604 ｜ $0.11 ｜ 名义 $50.6k* ｜ -9.3%
结构参考：230（+1.7%）上方 / 210（-7.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 50.9k / P 20.6k
ΔOI:      C +20.3k / P +12.1k
ATM:      C 5.85 / P 2.67
ATM IV:   35.2%
ΔOI Δ Exposure*: 1.1M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 225 ｜ +8,671 ｜ $5.85 ｜ 名义 $5.07M* ｜ -0.5%
P 195 ｜ +6,088 ｜ $0.13 ｜ 名义 $79.1k* ｜ -13.8%
C 230 ｜ +2,552 ｜ $3.18 ｜ 名义 $811.5k* ｜ +1.7%
结构参考：230（+1.7%）上方 / 225（-0.5%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 212.0k / P 249.8k
ΔOI:      C +41.0k / P +57.9k
ATM:      C 6.50 / P 3.50
ATM IV:   36.0%
ΔOI Δ Exposure*: 1.8M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 115 ｜ +15,263 ｜ $0.01 ｜ 名义 $15.3k* ｜ -49.1%
P 125 ｜ +11,843 ｜ $0.01 ｜ 名义 $11.8k* ｜ -44.7%
C 240 ｜ +10,572 ｜ $1.21 ｜ 名义 $1.28M* ｜ +6.1%
结构参考：240（+6.1%）上方 / 115（-49.1%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 43.6% vs 08-31 32.1%（差 +11.5pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/NVDA_evening.json