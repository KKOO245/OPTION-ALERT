# 期权晨报 2026-08-28

📊 市场环境

SPY $769.34 ｜ QQQ $716.43
VIX 14.19 ↓2.2%（5D -6.2%） ｜ Vol Regime: LOW
CNN 恐惧贪婪 54.4（neutral）

⇒ VIX ↑ = SPX 期权隐含的近 30 日预期波动率上升；不判方向，不进入 Direction Edge。

## 📅 本周重要美国宏观日历（仅【高】，美东时间）
- 周五 08-28 10:00　【高】Non Farm Payrolls Annual Revision Prel　实际 -79 ｜ 前值 -911　✅ 今日已公布
- 周五 08-28 10:00　【高】美联储主席讲话 Warsh Speech　实际 待公布　✅ 今日已公布

🔍 重点速览
🟡 **单日价格波动**: -3.5%（vs 前收盘）
   ⇒ 价格变动超阈值；纯事实，不解释方向
🟡 **近现价集中开仓**: 09-04 185P ΔOI +1,070（距现价 -0.0%）
   ⇒ 高等级 OI 变化且贴近现价；方向 Unknown（买开/卖开不可观测）
🔵 **期限 OI 集中**: 09-04 202C ΔOI +9,601 占该期限总 OI 12.1%
   ⇒ 新增仓位相对该期限总量显著（结构观察，非资金方向）


## COIN

📋 昨日晚报 → 今日晨报（只列关键项，低于阈值不单列）
COIN  昨收 191.15 → 今晨 185.01（-3.2%） | 较昨收变动（含盘初走势） ｜ 今日高 189.10 ｜ 低 181.78

Options: P/C量 0.35 | OI比 0.73 | ATM IV 79.8% | Skew -4.8pp | Term 0.79 | ExpMove ±1.6%（近端） | Rank — (历史不足)
   ⇒ Put/Call Volume: 0.35×（Call 成交量高于 Put）→ 方向 Unknown
   ⇒ Put/Call OI: 0.73×（存量 Call 仓位高于 Put）→ 存量 Call-dominant
   ⇒ 两者结构一致
   ⇒ 当日成交 vs 存量仓位：当日成交偏 Call，存量Call-dominant
   ExpMove 期限化（expmove_v1）: 09-04（7D）±6.6% ｜ 09-11（14D）±9.3% ｜ 09-18（21D）±11.7% ｜ 09-25（28D）±14.4%
🔧 结构（未验证研究层：Mechanism Scenario A/B——OI 开仓方向不可观测）
Gamma Regime: POSITIVE（模型分类） | GEX(存量) N/A | GEX Change N/A | Flip: Primary Flip: 160.52（PRIMARY，全链重定价 + 覆盖达标）
🔎 测量完整性: GEX 符号契约 gex_sign_v1（Model A: Call+ / Put−）｜ Gamma 口径 全链重定价 ｜ Effective GEX 覆盖: 98%（带内） ｜ IV 有效性: VALID 579 / LOW 194 / INVALID 327
结构观察区: Primary Flip 160.52（全链重定价，覆盖 98%）
Put Wall 100（现价高于该位 85.0%） | Call Wall 200（现价低于该位 7.5%）
最近结构参考: Call Wall 200（现价低于该位 7.5%）
🧭 结构解读（全部依赖上方假设）
• 支撑/压力参考：下方 100（Put Wall）；上方 200（Call Wall）。
• Gamma 区域：切换参考 161（全链重定价，覆盖 98%）。
• 做市商（条件机制）：若 Scenario A + 负 Gamma 成立，跌破关键位下方可能对应顺周期卖出压力增加；实际做市商对冲流量不可观测。Scenario B → 方向相反。不进入方向决策。
• 失效参考：跌破关键位结构参考失效（结构性参考，非预测）。
🔺 Activity（事实层，方向 Unknown）
09-04 202.5C — Vol 1,183 | 最新价 $1.56 | OI 1247→10848 (ΔOI +9601张) | ΔOI/Volume 811.6% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9601张（+769.9% vs前日OI），连续性待观察（方向未知）
09-04 195.0C — Vol 558 | 最新价 $2.94 | OI 1673→11205 (ΔOI +9532张) | ΔOI/Volume 1708.2% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增9532张（+569.8% vs前日OI），连续性待观察（方向未知）
08-28 200.0C — Vol 6,282 | 最新价 $0.03 | OI 9839→12261 (ΔOI +2422张) | ΔOI/Volume 38.5% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增2422张（+24.6% vs前日OI），连续性待观察（方向未知）
08-28 195.0C — Vol 9,577 | 最新价 $0.08 | OI 3051→4405 (ΔOI +1354张) | ΔOI/Volume 14.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1354张（+44.4% vs前日OI），连续性待观察（方向未知）
09-04 185.0P — Vol 748 | 最新价 $6.05 | OI 403→1473 (ΔOI +1070张) | ΔOI/Volume 143.1% | Magnitude: HIGH | 完整度: HIGH
   ⇒ 大额净增1070张（+265.5% vs前日OI），连续性待观察（方向未知）
📆 Forward Expiration Structure

09-04  C +23.5k / P +5.8k ｜ Activity HIGH ｜ 7D
09-11  C +2.3k / P +0.2k ｜ Activity HIGH ｜ 14D
09-18  C +0.8k / P -0.7k ｜ Activity HIGH ｜ 21D
09-25  C +0.8k / P +0.6k ｜ Activity HIGH ｜ 28D

📆 09-04 Forward Structure
OI:       C 53.3k / P 25.7k
ΔOI:      C +23.5k / P +5.8k
ATM:      C 6.17 / P 6.05
ATM IV:   60.1%
ΔOI Δ Exposure*: 270k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 202 ｜ +9,601 ｜ $1.56 ｜ 名义 $1.50M* ｜ +9.5%
C 195 ｜ +9,532 ｜ $2.94 ｜ 名义 $2.80M* ｜ +5.4%
P 185 ｜ +1,070 ｜ $6.05 ｜ 名义 $647.4k* ｜ -0.0%
结构参考：202（+9.5%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-11 Forward Structure
OI:       C 11.7k / P 7.6k
ΔOI:      C +2.3k / P +0.2k
ATM:      C 8.91 / P 8.35
ATM IV:   58.4%
ΔOI Δ Exposure*: 30k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
C 200 ｜ +705 ｜ $3.59 ｜ 名义 $253.1k* ｜ +8.1%
C 205 ｜ +534 ｜ $2.80 ｜ 名义 $149.5k* ｜ +10.8%
C 220 ｜ +511 ｜ $1.28 ｜ 名义 $65.4k* ｜ +18.9%
结构参考：200（+8.1%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-18 Forward Structure
OI:       C 167.4k / P 74.7k
ΔOI:      C +0.8k / P -0.7k
ATM:      C 11.55 / P 10.05
ATM IV:   60.7%
ΔOI Δ Exposure*: 683 shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 140 ｜ -1,321 ｜ $0.45 ｜ 名义 $-59.4k* ｜ -24.3%
C 187 ｜ +265 ｜ $9.92 ｜ 名义 $262.9k* ｜ +1.3%
C 190 ｜ -194 ｜ $8.83 ｜ 名义 $-171.3k* ｜ +2.7%
结构参考：187（+1.3%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

📆 09-25 Forward Structure
OI:       C 7.1k / P 6.4k
ΔOI:      C +0.8k / P +0.6k
ATM:      C 13.40 / P 13.24
ATM IV:   63.1%
ΔOI Δ Exposure*: -4k shares
Top ΔOI（行权价 ｜ ΔOI ｜ 最新价 ｜ 名义金额* ｜ 距现价）:
P 190 ｜ +304 ｜ $14.50 ｜ 名义 $440.8k* ｜ +2.7%
C 190 ｜ +260 ｜ $10.35 ｜ 名义 $269.1k* ｜ +2.7%
C 240 ｜ +155 ｜ $1.81 ｜ 名义 $28.1k* ｜ +29.7%
结构参考：190（+2.7%）上方形成 OI 变化集中区（结构观察，非价格预测）
*模型估算/名义金额代理；买开/卖开方向不可观测（Scenario A/B）

数据质量: 行情 A ｜ 期权结构 A ｜ 流向 C ｜ 做市商机制 C —— Flow 相关层（Activity 连续性、做市商机制解读）置信度受限。
Setup: 今日无 Setup 触发（机械检查全部 Setup）

数据溯源：完整表见附录 / thesis / analytics/daily/2026-08-28/COIN_morning.json