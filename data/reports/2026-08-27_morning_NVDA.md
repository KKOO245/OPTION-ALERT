# 期权晨报 2026-08-27

📊 市场环境

SPY $770.63 ｜ QQQ $719.23
VIX 14.49 ↓4.7%（5D -9.5%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 58.3（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 待公布 ｜ 前值 -911


## NVDA

🔍 重点速览
🟡 **单日价格波动**: +4.0%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **事件差分**: 08-28 ATM IV 47.2% vs 08-31 33.2%（差 +14.0pp）
   ⇒ 覆盖事件的期限隐含波动相对相邻期限偏高（观察，非因果）
🟡 **近现价集中开仓**: 08-28 220C ΔOI +35,710（距现价 -2.9%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
NVDA  昨收 217.91 → 今晨 226.51（+3.9%） | 较昨收变动（含盘初走势） ｜ 今日高 227.31 ｜ 低 220.90

Options: P/C量 0.49 | OI比 0.50 | ATM IV 47.2% | Skew 0.2pp | Term 0.70 | ExpMove ±2.2%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.49×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.50×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 08-28（1D）±2.2% ｜ 08-31（4D）±2.9% ｜ 09-02（6D）±3.7% ｜ 09-04（8D）±4.3%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 207.53（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 99%（带内） ｜ IV 有效性: VALID 703 / LOW 212 / INVALID 383
结构观察区: ≈208（局部 Gamma 切换，低置信；Top-3 近似，需全链重定价验证）
距 Put Wall 190: +19.2% | 距 Call Wall 230: -1.5%
最近结构参考: Call Wall 230（距现价 -1.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 190（Put Wall）；上方 230（Call Wall）。
• Gamma 区域：切换参考 208（Top-3 近似，需全链重定价验证）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
08-28 220.0C — Vol 75,705 | 最新价 $6.86 | OI 60397→96107 (ΔOI +35710张) | ΔOI/Volume 47.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增35710张（+59.1% vs前日OI），连续性待观察（方向未知）
08-28 200.0P — Vol 37,638 | 最新价 $0.03 | OI 36789→58748 (ΔOI +21959张) | ΔOI/Volume 58.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增21959张（+59.7% vs前日OI），连续性待观察（方向未知）
08-28 230.0C — Vol 236,440 | 最新价 $1.12 | OI 194582→210864 (ΔOI +16282张) | ΔOI/Volume 6.9% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增16282张（+8.4% vs前日OI），连续性待观察（方向未知）
08-28 235.0C — Vol 64,297 | 最新价 $0.29 | OI 41317→57195 (ΔOI +15878张) | ΔOI/Volume 24.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15878张（+38.4% vs前日OI），连续性待观察（方向未知）
09-04 115.0P — Vol 59 | 最新价 $0.01 | OI 16267→31530 (ΔOI +15263张) | ΔOI/Volume 25869.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增15263张（+93.8% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

08-28  C +183.1k / P +149.3k ｜ Activity HIGH ｜ 1D
08-31  C +34.4k / P +24.1k ｜ Activity HIGH ｜ 4D
09-02  C +20.3k / P +12.1k ｜ Activity HIGH ｜ 6D
09-04  C +41.0k / P +57.9k ｜ Activity HIGH ｜ 8D

📆 08-28 Forward Structure
OI:       C 1169.3k / P 581.8k
ΔOI:      C +183.1k / P +149.3k
ATM:      C 1.94 / P 3.10
ATM IV:   47.2%
ΔOI Δ Exposure*: 8.2M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 220 ｜ +35,710 ｜ $6.86 ｜ 名义 $24.50M* ｜ -2.9%
P 200 ｜ +21,959 ｜ $0.03 ｜ 名义 $65.9k* ｜ -11.7%
C 230 ｜ +16,282 ｜ $1.12 ｜ 名义 $1.82M* ｜ +1.5%
结构参考：230（+1.5%）上方 / 220（-2.9%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 08-31 Forward Structure
OI:       C 117.1k / P 62.8k
ΔOI:      C +34.4k / P +24.1k
ATM:      C 2.69 / P 3.82
ATM IV:   33.2%
ΔOI Δ Exposure*: 1.7M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 230 ｜ +8,750 ｜ $1.76 ｜ 名义 $1.54M* ｜ +1.5%
P 210 ｜ +5,816 ｜ $0.17 ｜ 名义 $98.9k* ｜ -7.3%
P 205 ｜ +4,604 ｜ $0.10 ｜ 名义 $46.0k* ｜ -9.5%
结构参考：230（+1.5%）上方 / 210（-7.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-02 Forward Structure
OI:       C 50.9k / P 20.6k
ΔOI:      C +20.3k / P +12.1k
ATM:      C 3.70 / P 4.60
ATM IV:   35.2%
ΔOI Δ Exposure*: 975k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 225 ｜ +8,671 ｜ $4.92 ｜ 名义 $4.27M* ｜ -0.7%
P 195 ｜ +6,088 ｜ $0.10 ｜ 名义 $60.9k* ｜ -13.9%
C 230 ｜ +2,552 ｜ $2.64 ｜ 名义 $673.7k* ｜ +1.5%
结构参考：230（+1.5%）上方 / 225（-0.7%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-04 Forward Structure
OI:       C 212.0k / P 249.8k
ΔOI:      C +41.0k / P +57.9k
ATM:      C 4.42 / P 5.30
ATM IV:   35.5%
ΔOI Δ Exposure*: 1.7M shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 115 ｜ +15,263 ｜ $0.01 ｜ 名义 $15.3k* ｜ -49.2%
P 125 ｜ +11,843 ｜ $0.01 ｜ 名义 $11.8k* ｜ -44.8%
C 240 ｜ +10,572 ｜ $0.97 ｜ 名义 $1.03M* ｜ +6.0%
结构参考：240（+6.0%）上方 / 115（-49.2%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📅 事件差分（观察，非因果）: 08-28（1D）ATM IV 47.2% vs 08-31 33.2%（差 +14.0pp）——覆盖 美联储主席讲话 Warsh Speech、Non Farm Payrolls Annual Revision Prel
   符合'覆盖事件的期权溢价更高'（美联储 IFDP 1376 实证；单日截面，需连续多日确认）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-27/NVDA_morning.json