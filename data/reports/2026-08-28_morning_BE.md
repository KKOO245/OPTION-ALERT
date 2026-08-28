# 期权晨报 2026-08-28

📊 市场环境

SPY $774.48 ｜ QQQ $723.08
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 56.4（greed）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🟡 **近现价集中开仓**: 09-11 225C ΔOI -1,880（距现价 +3.2%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）


## BE

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
BE  昨收 215.90 → 今晨 218.00（+1.0%） | 较昨收变动（含盘初走势） ｜ 今日高 222.40 ｜ 低 213.33

Options: P/C量 1.23 | OI比 0.84 | ATM IV 93.8% | Skew -5.9pp | Term 0.90 | ExpMove ±1.8%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 1.23×（Put 成交量高于 Call）→ 方向 Unknown
   ⇒ Put/Call OI: 0.84×（两侧接近均衡）
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Put，存量接近均衡
   ExpMove 期限化（expmove_v1）: 09-04（7D）±9.9% ｜ 09-11（14D）±12.8% ｜ 09-18（21D）±16.2% ｜ 09-25（28D）±18.0%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 203.42（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 100%（带内） ｜ IV 有效性: VALID 574 / LOW 91 / INVALID 225
结构观察区: Primary Flip 203.42（全链重定价，覆盖 100%）
Put Wall 180（现价高于该位 21.1%） | Call Wall 250（现价低于该位 12.8%）
最近结构参考: Flip 203（现价高于该位 7.2%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 180（Put Wall）；上方 250（Call Wall）。
• Gamma 区域：切换参考 203（全链重定价，覆盖 100%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 275.0C — Vol 44 | 最新价 $1.01 | OI 666→2595 (ΔOI +1929张) | ΔOI/Volume 4384.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1929张（+289.6% vs前日OI），连续性待观察（方向未知）
09-04 272.5C — Vol 222 | 最新价 $0.93 | OI 33→1764 (ΔOI +1731张) | ΔOI/Volume 779.7% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1731张（+5245.4% vs前日OI），连续性待观察（方向未知）
08-28 220.0C — Vol 1,475 | 最新价 $1.05 | OI 2236→3209 (ΔOI +973张) | ΔOI/Volume 66.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增973张（+43.5% vs前日OI），连续性待观察（方向未知）
09-04 270.0C — Vol 747 | 最新价 $0.99 | OI 405→1167 (ΔOI +762张) | ΔOI/Volume 102.0% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增762张（+188.2% vs前日OI），连续性待观察（方向未知）
09-18 225.0C — Vol 53 | 最新价 $14.70 | OI 289→1046 (ΔOI +757张) | ΔOI/Volume 1428.3% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增757张（+261.9% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +6.7k / P +2.5k ｜ Activity HIGH ｜ 7D
09-11  C -1.5k / P -0.9k ｜ Activity HIGH ｜ 14D
09-18  C +3.4k / P +1.7k ｜ Activity HIGH ｜ 21D
09-25  C +0.8k / P +0.7k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 23.0k / P 28.8k
ΔOI:      C +6.7k / P +2.5k
ATM:      C 10.85 / P 10.70
ATM IV:   88.3%
ΔOI Δ Exposure*: 43k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 275 ｜ +1,929 ｜ $1.01 ｜ 名义 $194.8k* ｜ +26.1%
C 272 ｜ +1,731 ｜ $0.93 ｜ 名义 $161.0k* ｜ +25.0%
C 270 ｜ +762 ｜ $0.99 ｜ 名义 $75.4k* ｜ +23.9%
结构参考：275（+26.1%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 11.8k / P 9.7k
ΔOI:      C -1.5k / P -0.9k
ATM:      C 14.51 / P 13.50
ATM IV:   85.6%
ΔOI Δ Exposure*: -59k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 225 ｜ -1,880 ｜ $13.54 ｜ 名义 $-2.55M* ｜ +3.2%
P 195 ｜ -1,038 ｜ $5.10 ｜ 名义 $-529.4k* ｜ -10.6%
C 240 ｜ +58 ｜ $7.14 ｜ 名义 $41.4k* ｜ +10.1%
结构参考：240（+10.1%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 118.3k / P 93.1k
ΔOI:      C +3.4k / P +1.7k
ATM:      C 17.78 / P 17.50
ATM IV:   83.6%
ΔOI Δ Exposure*: 40k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 225 ｜ +757 ｜ $14.70 ｜ 名义 $1.11M* ｜ +3.2%
C 300 ｜ +551 ｜ $1.96 ｜ 名义 $108.0k* ｜ +37.6%
C 270 ｜ +379 ｜ $4.51 ｜ 名义 $170.9k* ｜ +23.9%
结构参考：225（+3.2%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 6.8k / P 5.9k
ΔOI:      C +0.8k / P +0.7k
ATM:      C 19.73 / P 19.46
ATM IV:   84.5%
ΔOI Δ Exposure*: 12k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 250 ｜ +232 ｜ $10.00 ｜ 名义 $232.0k* ｜ +14.7%
C 230 ｜ +224 ｜ $17.39 ｜ 名义 $389.5k* ｜ +5.5%
P 200 ｜ +201 ｜ $11.10 ｜ 名义 $223.1k* ｜ -8.3%
结构参考：250（+14.7%）上方 / 200（-8.3%）下方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/BE_morning.json